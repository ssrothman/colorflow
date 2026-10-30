# Literature review log

## Iteration 1 — 2026-10-30

- **Seeded** 31 papers from `human_start.bib` (all resolved in INSPIRE, all with Zotero PDFs; `ATLASPythia82014` matched by title and checked: correct).
- **Seed-topic searches** (see `searches.tsv`): CR in WW, CR and top, jet pull, colour flow, rapidity gaps / colour-singlet exchange, string and drag effect, angular ordering, soft-gluon coherence, leading colour, EIC hadronization, ropes, CR and high multiplicity, CR/coherence reviews. Then the full title sets for "colo(u)r reconnection", "colo(u)r coherence", "colo(u)r flow", "leading colo(u)r". Note: INSPIRE title search has no stemming ("shower" ≠ "showers") and titles often write tops as `$t\bar{t}$`, so topic searches must avoid those words.
- **Triage round 1:** 336 search candidates (9 subagents) → 109 next, 160 later, 98 rejected (mostly plasma "magnetic reconnection" and two-loop amplitude papers).
- **Read** 15 papers in 9 clusters (all from Zotero): Amati:1979fg, Bassetto:1979vy, Marchesini:1980cr (rel. 2); Dokshitzer:1987nm, Webber:1983if, Marchesini:1987cf, Ellis:1986bv, CDF:1994zkl, D0:1997tye, D0:1999lfo, OPAL:1991xwi, L3:2003oci, DELPHI:2006tie, ATLAS:2018olo, Argyropoulos:2014zoa (rel. 3).
- **Expansion:** references of all 15; citing papers (30 most-cited + 15 most-recent) of the relevance-3 papers; topical filters for the >300-citation papers (Dokshitzer:1987nm, Webber:1983if, Marchesini:1987cf).
- **Triage round 2:** 596 candidates (15 subagents) → many reference-list items (PDFs, detector papers) rejected. DB now 963 records: 15 read, 146 queued next, 283 queued later, 519 rejected.
- **Verification:** all 12 relevance-3 summaries checked against the PDFs by independent subagents. No fabricated numbers; typical 2–10 corrections per summary (overstatements, plot read-offs, framing, a swapped kinematic value in Dokshitzer:1987nm, a wrong cut description in CDF:1994zkl).
- **Docs:** first `synthesis.md` and `open_questions.md` written.
- **Process notes:** concurrency limit is 20 subagents. Two triage subagents briefly wrote list output to the session scratchpad (outside `~/colorflow`, a HARD RULE breach); the path-guard hook blocked reading it back and they re-ran inside the repo. Triage results were staged and applied in one `setmany` after all pages finished, to keep page offsets stable.
- **Blocked:** 0. Check-in not triggered.
