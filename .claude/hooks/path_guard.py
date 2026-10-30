#!/usr/bin/env python3
"""PreToolUse hook enforcing the project HARD RULE for file tools.

Allowed: read/write inside ~/colorflow; read-only inside the Zotero storage dir.
Exit code 2 blocks the call and shows stderr to Claude. (Bash is not checked here;
the rule for Bash is enforced by instruction only.)
"""
import json, os, sys

PROJECT = os.path.realpath(os.path.expanduser("~/colorflow"))
READ_ONLY = [os.path.realpath("/mnt/c/Users/simon/Zotero/storage")]
WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}


def inside(path, root):
    return path == root or path.startswith(root + os.sep)


ev = json.load(sys.stdin)
tool, inp = ev.get("tool_name", ""), ev.get("tool_input", {}) or {}
raw = inp.get("file_path") or inp.get("notebook_path") or inp.get("path")
if not raw:
    sys.exit(0)  # Glob/Grep without path -> cwd, which is the project
path = os.path.realpath(os.path.join(ev.get("cwd") or PROJECT, os.path.expanduser(raw)))

if inside(path, PROJECT):
    sys.exit(0)
if tool not in WRITE_TOOLS and any(inside(path, r) for r in READ_ONLY):
    sys.exit(0)
print(f"HARD RULE (path_guard hook): {tool} on {path} is outside ~/colorflow"
      + ("" if tool in WRITE_TOOLS else " and the Zotero storage dir")
      + ". If you hit this on a persisted tool-result file, re-run the command with smaller output instead.",
      file=sys.stderr)
sys.exit(2)
