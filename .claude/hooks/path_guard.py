#!/usr/bin/env python3
"""PreToolUse hook enforcing the project HARD RULE for Claude's file tools (Bash is confined by the sandbox).

The allowed paths come from the same settings as the Bash sandbox, so one list governs both:
  read+write: the project dir and sandbox.filesystem.allowWrite
  read-only:  sandbox.filesystem.allowRead
taken from .claude/settings.json and .claude/settings.local.json (lists merged; missing files add nothing).
Path prefixes follow the sandbox convention: "/" or "//" absolute, "~/" home, "./" or none project-relative.
denyRead/denyWrite and other sandbox keys are not consulted. If a settings file is unreadable or malformed,
everything outside the project is blocked. The project dir is $CLAUDE_PROJECT_DIR, else this file's ../..
Writes to .claude/settings.json, .claude/settings.local.json and .claude/hooks/ are always blocked: only the user
changes the sandbox. Glob is checked on its path and on the fixed prefix of its pattern; patterns with a '..'
component are blocked.
Exit code 2 blocks the call and shows stderr to Claude. Claude Code lets the call proceed on any other
exit code, so every unexpected error is caught and turned into a block.
"""
import json, os, re, sys

WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
PROJECT = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR")
                           or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
PROTECTED = [os.path.join(PROJECT, ".claude", x) for x in ("settings.json", "settings.local.json", "hooks")]


def inside(path, root):
    return path == root or path.startswith(root.rstrip(os.sep) + os.sep)


def resolve(p):
    if p.startswith("//"):
        p = p[1:]
    elif p.startswith("~"):
        p = os.path.expanduser(p)
    return os.path.realpath(os.path.join(PROJECT, p))  # join keeps absolute p as is


def roots():
    """(read_write, read_only) lists of real paths; raises ValueError/OSError on a bad settings file."""
    rw, ro = [PROJECT], []
    for name in ("settings.json", "settings.local.json"):
        f = os.path.join(PROJECT, ".claude", name)
        if not os.path.exists(f):
            continue
        with open(f, encoding="utf-8") as fh:
            cfg = json.load(fh)
        sandbox = cfg.get("sandbox", {}) if isinstance(cfg, dict) else None
        fs = sandbox.get("filesystem", {}) if isinstance(sandbox, dict) else None
        if not isinstance(fs, dict):
            raise ValueError(f"{f}: sandbox.filesystem is not an object")
        for key, out in (("allowWrite", rw), ("allowRead", ro)):
            v = fs.get(key, [])
            if not (isinstance(v, list) and all(isinstance(x, str) and x for x in v)):
                raise ValueError(f"{f}: sandbox.filesystem.{key} must be a list of non-empty strings")
            out += [resolve(x) for x in v]
    return rw, ro


def check(ev):
    """None if the call is allowed, else the reason it is blocked."""
    tool, inp = ev.get("tool_name", ""), ev.get("tool_input", {}) or {}
    cwd = ev.get("cwd") or PROJECT
    paths = [p for p in (inp.get("file_path"), inp.get("notebook_path"), inp.get("path")) if p]
    if tool == "Glob" and inp.get("pattern"):
        pat = inp["pattern"]
        if ".." in re.split(r"[\\/{},]", pat):
            return f"Glob pattern {pat!r} contains a '..' component"
        prefix = re.split(r"[*?\[{]", pat, maxsplit=1)[0]  # fixed leading part of the pattern
        if prefix:
            paths.append(os.path.join(paths[0] if paths else cwd, os.path.expanduser(prefix)))
    if not paths:
        paths = [cwd]  # Glob/Grep without path search the cwd
    rw = ro = None
    err = ""
    for raw in paths:
        path = os.path.realpath(os.path.join(cwd, os.path.expanduser(raw)))
        if tool in WRITE_TOOLS and any(inside(path, p) for p in PROTECTED):
            return f"{tool} on {path}: sandbox settings and hooks are changed by the user only"
        if inside(path, PROJECT):
            continue
        if rw is None:
            try:
                rw, ro = roots()
            except (OSError, ValueError) as e:  # fail closed: only the project stays allowed
                rw, ro, err = [PROJECT], [], f" (settings error, so only the project is allowed: {e})"
        if any(inside(path, r) for r in rw) or (tool not in WRITE_TOOLS and any(inside(path, r) for r in ro)):
            continue
        return (f"{tool} on {path} is outside the allowed paths (project, sandbox.filesystem.allowWrite"
                f"{'' if tool in WRITE_TOOLS else ', allowRead'}){err}")
    return None


try:
    reason = check(json.load(sys.stdin))
except Exception as e:  # any crash must block: exit codes other than 2 let the tool call proceed
    reason = f"hook error, call blocked: {type(e).__name__}: {e}"
if reason:
    print(f"HARD RULE (path_guard hook): {reason}. If you hit this on a persisted tool-result file,"
          " re-run the command with smaller output instead.", file=sys.stderr)
    sys.exit(2)
