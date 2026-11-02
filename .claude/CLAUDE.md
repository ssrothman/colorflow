# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

HARD RULE: You should only read and write files inside `~/colorflow/`, with two exceptions: read-only access to the Zotero storage folder (pdfs already downloaded by zotero, pointed to by the human_start bibliography), and `/tmp` for temporary files.

Corollary: keep command output small. Oversized tool output is persisted by the harness under `~/.claude/`, which this rule forbids reading.

## Project

A physics research project, currently a literature review on collective effects in high-energy QCD at colliders: color coherence, color reconnection, color flow. The repo is documents plus a helper script with its own regression tests, version-controlled with git (one commit per review iteration).

- `litreview.md` — the task spec: research questions, scope notes, seed topics, procedure, required outputs. Read it before any review work.
- `.claude/skills/literature-review/` — the `literature-review` skill: the review loop, state-file conventions, subagent fan-out, full-text access, and `scripts/lr.py` (INSPIRE/arXiv queries + `papers.jsonl` bookkeeping). Use it for all review work. After changing `lr.py` or `path_guard.py`, run `python3 .claude/skills/literature-review/scripts/test_lr.py` (offline with faked HTTP, ~1 s; `LR_LIVE=1` adds live API checks; pass a class or method name such as `TestHook` to run one test). Tests write to a throwaway, git-ignored `.lrtest-<pid>/` in the project root.
- `litreview/` — review state and outputs: `human_start.bib` (user's Zotero seed list), `papers.jsonl` (source of truth), generated `papers.md` / `queue.md` / `review.bib`, `summaries/`, `synthesis.md`, `open_questions.md`, `log.md`. `litreview/papers/` holds downloaded full texts and is git-ignored.
- Sandbox enforcing the HARD RULE. Bash runs in Claude Code's bubblewrap sandbox (`.claude/settings.json`: no unsandboxed fallback, reads outside the working directories blocked, network limited to `sandbox.network.allowedDomains`). File tools are checked by the PreToolUse hook `.claude/hooks/path_guard.py`, which allows the project, `sandbox.filesystem.allowWrite` (read-write) and `allowRead` (read-only) from both settings files.
  - `.claude/settings.json`, `.claude/settings.local.json` and `.claude/hooks/` are changed by the user only: the hook blocks file-tool writes and the sandbox blocks Bash writes. Propose changes as a diff. Bash also cannot write `.claude/skills/`; edit skill files with the Edit/Write tools.
  - Machine-specific paths live only in the git-ignored `.claude/settings.local.json` (template: `.claude/settings.local.example.json`; on a new machine, copy it, set the paths, restart): `env.ZOTERO_STORAGE` (used by `lr.py seed` and `fetch`), Zotero as `additionalDirectories` + `allowRead` + `denyWrite`, and `/tmp` in `allowWrite` (it has no effect on the sandbox from the shared file).
  - `/add-dir` (or `additionalDirectories`) makes a directory readable *and writable* for Bash, and the hook still blocks it for file tools. For read-only access use the Zotero pattern above.
  - `/tmp` is writable by Bash and the Write tool, but the Read tool cannot open files there (`blockReadsOutsideWorkingDirectories`).
  - Start Claude Code from the project root: a session started with the shell inside `.claude/` cannot run Bash at all.
  - Network: Bash can reach only `sandbox.network.allowedDomains`. In auto mode a command may request further hosts; use only well-known, legitimate operators (publishers, labs, repositories) and say which host and why.

## Behavior

All claims should be backed up by clear evidence (tests, references, etc). NEVER report guesses as fact. ALWAYS ask clarifying questions when there is any doubt or ambiguity about the question or task. Only return to the user when you are >= 95% certain that the answer, script, or similar is correct. 

NEVER make high-level decisions without consultation. 

When writing code, ALWAYS behave as follows:

- Ensure that it is completely clear what the desired behavior should be. If it is unclear or ambiguous, ask additional questions.
- For large tasks write a clear plan and confer with the human about whether the plan is correct.
- Make only the SMALLEST change that achieves the clear objective. Do not touch any code that is not related to the task at hand. 
- All new behavior should be documented and covered by unit tests. 

With these goals in mind, the core development loop looks like:

1. Write the minimal program or edit that achieves the goal. 
2. Add unit tests to ensure that the behavior is correct. 
3. Carefully review the written code (including the unit tests!) (WITHOUT running it) for logical correctness, efficiency, and bugs. 
4. Run the code and the unit tests, and validate the behavior. Also run any pre-existing unit tests to ensure that the new changes have not broken any previous behavior. 
5. IF THERE ARE ANY BUGS: return to step one and loop
6. Return to me only if:
    a. There are no known issues with the new code.
    b. The only known issues relate to other pieces of the codebase that are not related to the task at hand.
    c. We have agreed that the known issues are not breaking. 
    d. Any clarification is needed about the desired behavior, architecture, etc. 
    e. The edits have exposed any issues that we did not know about previously and that require new decisions.
