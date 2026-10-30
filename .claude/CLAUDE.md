# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

HARD RULE: You should only read and write files inside `~/colorflow/`, with the exception of read-only access to pdfs already downloaded by zotero (pointed to by the human_start bibliography)

Corollary: keep command output small. Oversized tool output is persisted by the harness under `~/.claude/`, which this rule forbids reading.

## Project

A physics research project, currently a literature review on collective effects in high-energy QCD at colliders: color coherence, color reconnection, color flow. There is no build/test tooling; the repo is documents plus a helper script, version-controlled with git (one commit per review iteration).

- `litreview.md` — the task spec: research questions, scope notes, seed topics, procedure, required outputs. Read it before any review work.
- `.claude/skills/literature-review/` — the `literature-review` skill: the review loop, state-file conventions, subagent fan-out, full-text access, and `scripts/lr.py` (INSPIRE/arXiv queries + `papers.jsonl` bookkeeping). Use it for all review work.
- `litreview/` — review state and outputs: `human_start.bib` (user's Zotero seed list), `papers.jsonl` (source of truth), generated `papers.md` / `queue.md` / `review.bib`, `summaries/`, `synthesis.md`, `open_questions.md`, `log.md`. `litreview/papers/` holds downloaded full texts and is git-ignored.
- `.claude/hooks/path_guard.py` — PreToolUse hook enforcing the HARD RULE for file tools (enabled via `.claude/settings.json`).
