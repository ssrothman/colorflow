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

## Iteration 4 — 2026-11-02

- **Batch (gap-filling, approved by user):** 15 papers chosen to cover modern CR models, top-mass CR, small-system flow-like effects, HERA, LEP1 Z-decay CR tests. All arXiv PDFs except Bengtsson:1986et (NPB 289 (1987) 810): no free full text → `blocked` (expect 3 → check-in trigger). 9 readers.
- **Read** 14 papers. Relevance 3: Gieseke:2018gff, Christiansen:2015yca, Skands:2007zg, OrtizVelasquez:2013ofg, Bierlich:2014xba, Altmann:2024odn (reader proposed 2; raised to 3 for concrete RQ4 test proposals + Λb/B⁰ data tension), ATLAS:2022ctr, Edin:1995gi, ALEPH:2006jcu, OPAL:2003njc, OPAL:2005cdr. Relevance 2: Bellm:2019wrh, Lonnblad:2023stc, Sjostrand:2004pf. Raised Sjostrand:2002ip (junction fragmentation) to next.
- **Key new results:** LEP1 gluon-jet rapidity-gap tests (OPAL, ALEPH) disfavour GAL and Ariadne-CR at default strength (GAL R₀ fit ≈ 0.01–0.02 vs 0.1 from HERA: SCI/GAL universality tension); OPAL WW particle flow excludes only SK-I 100 % (4.4σ), best fit 37 %; ATLAS tt̄ CR observables disfavour no-CR but cannot separate CR from MPI and barely probe top-decay CR; ⟨p⊥⟩(N_ch) is the main hadron-collider CR argument (but compared with Tune A, not data, in the 2004/2007 papers); CR gives flow-like mass ordering in pp (MC only); ropes fix strange-baryon ratios but not high-p⊥; junction CR overpredicts Λb/B⁰ ~2× and underpredicts Ξ/Ω; CR from soft-gluon evolution (Herwig) gives reconnection probabilities without a mass veto; future e⁺e⁻ δm_W sign is model-dependent.
- **Expansion:** references of all 14; citing (top-30 + 15 most recent) for the 11 relevance-3 papers; 27 arXiv + 9 journal lookups of reader leads (all already known/added via refs).
- **Triage:** 575 candidates (8 subagents, unique output files — no collisions) → 24 next, 146 later, 405 rejected; expect ≥ 2 fraction 79/575 ≈ 14 % (iter. 3 ≈ 22 %, iter. 2 ≈ 26 %) — not converged (threshold ~10 %). Two candidates without texkey rejected by recid (2780507, 2930353).
- **Verification:** all 11 relevance-3 summaries (5 verifiers, ~950 claims); ~45 corrections. Substantive: OrtizVelasquez Fig. 4 pions (rise with CR, not flat); Gieseke 1/10–9/10 are values at min/max mixing, not bounds; Christiansen_2015yca Fig. 4 model labels swapped. Unverified cross-paper flags resolved from other summaries (SCI→GAL lineage via Rathsman:1998tp; L3 insensitivity via L3_2003oci; Skands vs Argyropoulos m_top comparison rewritten with verified numbers).
- **Corrections to earlier material:** ALEPH_2013dgf's OPAL p_reco = 0.43 traced to Phys. Rept. Ref. [114] (OPAL m_W paper, EPJC 45 (2006) 307, p. 188), not OPAL_2005cdr (37 %); both summaries annotated. Synthesis "~20× heavy baryons" corrected to ×2 (Λc/Λb), ×20–30 (Σc/Σb) per Christiansen_2015yqa.
- **Noted, not resolved:** reconnected fractions differ between ALEPH_2013dgf (AR-2 ≈ 22 %, HERWIG 1/9 at 189 GeV) and OPAL_2005cdr (AR-2 49.4 %, HERWIG-CR ≈ 23 % at 199.5 GeV) — likely definition/energy; both quoted with source. "ARIADNE type 1" (Phys. Rept. p. 66) = intra-singlet CR, consistent with OPAL's AR-1 = CR within each W (naming, not a contradiction). Christiansen_2015yca text 2.2σ vs Tab. 4 2.0σ (quadrature gives 2.0σ).
- **Docs:** synthesis.md revised by subagent (new RQ1 §3 on multi-string colour correlations in small systems with mechanism table; RQ2 CR chronology split e⁺e⁻/DIS vs hadron-collider era; new top-mass and future-e⁺e⁻ subsections; RQ3 table rows for HERA gaps, LEP1 gluon-jet gaps, tt̄ CR, small-system identified hadrons; RQ4 split by collider). open_questions.md 18 → 28 items. review.bib 56 entries.
- **DB:** 2366 records: 56 read, 184 queued next, 559 queued later, 1565 rejected, 2 blocked (Azimov:1986rv inaccessible; Bengtsson:1986et).
