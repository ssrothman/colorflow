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

## Iteration 2 — 2026-10-30

- **Batch:** 28 papers selected; 16 blocked (pre-arXiv journal articles with no free full text; OpenAlex gave a wrong arXiv id for Sjostrand:1993hi, reverted). `blocked_2026-10-30.bib` exported for Zotero import.
- **Read** 12 papers (8 readers; all were interrupted by an API usage limit and resumed): JADE:1981ofk (scan), Gallicchio:2010sw, Hook:2011cq (rel. 2), ALEPH:2013dgf, Sjostrand:2013cya (rel. 2), Christiansen:2015yqa, Osborn:2018bwn, Gieseke:2012ft, Rathsman:1998tp, CMS:2013cvx, CMS:2021hnp (rel. 2), Khoze:1996dn.
- **Key new results:** LEP CR combination (k_I = 1.26, no-CR disfavoured at 2.8σ, L3/DELPHI tension mostly reference-MC); CMS 7 TeV coherence: no generator fits, forward worst; at large N_c drag = string, only 1/N_c² effects discriminate; colour-entanglement search null.
- **Expansion:** references of all 12 (topical filters for ALEPH:2013dgf and Khoze:1996dn); citing papers for relevance-3 papers (filtered for >300 citations). Citing lists of CR-model papers added almost nothing new (e.g. 0 new / 29 known for Christiansen:2015yqa): CR-titled literature looks saturated.
- **Triage:** 482 candidates (12 subagents; 170 came from the PHENIX thesis reference list, mostly generic TMD/spin) → 47 next, 76 later, 359 rejected. Fraction of newly triaged with expect ≥ 2: ≈ 26 % (iteration 1: ≈ 46 % over 932) — not yet converged.
- **Verification:** all 9 relevance-3 summaries checked; 4–13 corrections each (e.g. Christiansen: local not global λ minimum; ALEPH: no single experiment > 2σ; CMS: excess at β≈0 only; Khoze: R_γ comparison is for a restricted interval).
- **DB:** 1445 records: 27 read, 153 queued next, 359 queued later, 890 rejected, 16 blocked.
- **CHECK-IN: 2026-10-30, 27 papers read so far.** Triggered by 16 blocked papers, all with expect = 3.

## Check-in resolution — 2026-11-02

- User imported `blocked_2026-10-30.bib` into Zotero. 14 PDFs linked (each checked against the paper's first page) → `queued`/`next`. JADE:1985mmd and Andersson:1983ia were already in Zotero (RWSDB93D, 7JD44EC5). OPAL:1990vmr has two near-identical Zotero copies (4T84ZBNQ linked, AHSGJWSI unused).
- Azimov:1986rv: no PDF obtainable (user) → stays `blocked`, marked inaccessible in `notes`.
- Ermolaev:1981cm: the first Zotero attachment (CZKED47X) was the Sjostrand:1993hi PDF; user attached the correct scan (E2ELN4KD, 4 pp., no text layer; checked page 1) → `queued`/`next`.
- SKILL.md: check-in trigger no longer counts blocked papers marked `notes="inaccessible: …"`; these are listed in `open_questions.md`.

## Iteration 3 — 2026-11-02

- **Batch:** the 15 papers unblocked at the check-in (all Zotero PDFs; Ermolaev:1981cm is a scan read from page images). 8 readers.
- **Read** 15 papers, all relevance 3: Andersson:1983ia, Bassetto:1983mvz (reviews); Ermolaev:1981cm, Azimov:1985zta, Sjostrand:1993hi (theory); Andersson:1980vk, Khoze:1989km, Lonnblad:1995yk (MC); Boudinov:1993mc, Gustafson:1988fs, Gustafson:1994cd (pheno); JADE:1985mmd, L3:1995ahv, OPAL:1990vmr, OPAL:1992lzb (exp).
- **Key new results:** angular ordering arises only after summing diagrams (Ermolaev–Fadin, BCM); string kink and perturbative antenna give the same q–q̄ depletion at leading N_c, and PETRA data (r = 1.39 ± 0.04) are fitted by Lund and by the angular-ordered Webber shower alike, only incoherent/independent models fail; ξ-peak slope is weak coherence evidence (Boudinov critique), azimuthal/PPCA correlations stronger; early CR theory: perturbative CR negligible (≲ 5 MeV), SK-I/II non-perturbative ~40 MeV, SK-II shift negative while SK-I of uncertain sign; Gustafson–Häkkinen zero-central-particle WW test never measured at LEP2 (as far as known).
- **Expansion:** references of all 15 (reviews in full: 96 and 89 resolved refs); citing papers (top-30 + 15 most recent) for 10; topical filtered citing for the 5 with > 300 citations; 12 journal-reference lookups of reader leads (11 already known). Reconnection-filtered citing lists added ~0 new (saturated, as in iteration 2).
- **Triage:** 346 candidates (9 subagents) → 18 next, 59 later, 269 rejected; expect ≥ 2 fraction ≈ 22 % (iter. 2 ≈ 26 %, iter. 1 ≈ 46 %) — not converged. Override: Mukhi:1982bk rejected → later (flagged by Bassetto reader). Raised to next: Fadin:1983aw, Mueller:1981ex, OPAL:1992cqm.
- **Verification:** all 15 summaries checked (6 verifiers, ~900 claims); ~55 corrections, mostly figure read-offs (L3 Fig. 3b, Khoze Fig. 2, Gustafson figures), plus anchors, two misattributions, two σ recalculations (JADE ≈ 10σ; Boudinov 2.7σ/1.3σ) and the SK-I/SK-II m_W sign statement.
- **Docs:** synthesis.md (RQ1–4 rewritten/restructured; new string-effect and CR-model-chronology sections) and open_questions.md (18 items; 7 new) revised by a subagent; review.bib 42 entries.
- **Process note:** triage workers collided on shared temp file names in $TMPDIR; two re-ran into unique files. Use unique temp names in future triage prompts.
- **DB:** 1791 records: 42 read, 174 queued next, 414 queued later, 1160 rejected, 1 blocked (Azimov:1986rv, inaccessible).
