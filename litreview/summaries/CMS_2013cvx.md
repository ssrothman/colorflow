# Probing color coherence effects in pp collisions at √s = 7 TeV
- **ID / links:** CMS:2013cvx · INSPIRE 1265659 · arXiv 1311.5815 · DOI 10.1140/epjc/s10052-014-2901-8
- **Authors / collab, year, journal:** CMS Collaboration (CMS-SMP-12-010), 2014, Eur. Phys. J. C 74, 2901
- **Type:** experimental
- **Relevance:** 3 · RQs: 1b, 1d, 2, 3
- **Full text source:** arxiv (v2; anchors are the preprint's printed page numbers 1–14)

## Takeaways
- First LHC measurement ("first" is our context, not a paper claim) of the CDF/D0 β observable (azimuthal orientation of the 3rd jet around the 2nd jet in (η, φ)), unfolded to particle level, in central (|η2| ≤ 0.8) and forward (0.8 < |η2| ≤ 2.5) regions (p. 1–2, 6; Fig. 4, Tabs. 4–5).
- Same qualitative pattern as at the Tevatron: data show an excess near the event plane at β ≈ 0 and a depletion at β ≈ π/2 relative to PYTHIA and MADGRAPH (p. 7); near β ≈ π the data are at or below these MCs (forward PYTHIA overshoots by ≈ 5–9%, ≈ read from Fig. 5). The forward rise is steep (F ≈ 0.039 → 0.079 from β = 0–10° to 170–180°); the central distribution is almost flat with a shallow minimum near 90° (0.055 → 0.051 → 0.064) (Tabs. 4–5).
- **No generator describes the data** (χ²/NDF, 17 dof, central / forward): PYTHIA6 Z2 2.5 / 8.1, PYTHIA8 4C 1.7 / 6.4, HERWIG++ 1.2 / 3.5, MADGRAPH+PYTHIA6 D6T 1.6 / 3.3 (Tab. 6). HERWIG++ is best centrally but fails forward; adding the exact LO 2→3 matrix element (MADGRAPH) helps relative to PYTHIA6 alone (p. 10–11).
- Turning off coherence in the first ISR/FSR branching of PYTHIA6 (D6T) makes agreement much worse, with χ²/NDF rising to 7.7 (central) and 11.5 (forward). The authors conclude that the data "clearly support larger color coherence effects than in present MC implementations" (p. 10, Fig. 6).
- PYTHIA studies show that hadronization and UE have negligible impact on β (p. 10). Our interpretation (not stated in the paper): this supports a perturbative (LPHD-type) origin, as D0 found.

## Setup
- LHC 2010, √s = 7 TeV, 36 pb⁻¹. Single-jet triggers with thresholds 30–140 GeV; the data are split into five unprescaled pT1 bins, luminosity-weighted (Tab. 2, p. 3, 6).
- Jets: anti-kT R = 0.5, particle flow, JEC including pileup jet-area subtraction; tight jet ID (< 1% fakes) (p. 3).
- Selection: ≥ 3 jets with pT > 30 GeV; pT1 > 100 GeV; |η1|, |η2| ≤ 2.5; no η cut on jet 3 (avoids a β bias); M12 > 220 GeV (> 98% of events have |Δφ12 − π| < 1); 0.5 < ΔR23 < 1.5 (Tab. 1, p. 3–4). 193 131 events: 87 510 central, 105 621 forward (Tab. 2). HF energy shows no diffractive component (p. 4).
- Observable: tan β = |Δφ23| / Δη23 with Δη23 = sign(η2)(η3 − η2), 0 ≤ β ≤ π. β = 0 points toward the nearer beam (between jet 2 and the remnant), β = π toward the far beam/centre (Eq. 1, Fig. 1, p. 1–2). F(β) = N_i/N per η2 region, 18 bins of 10° (Eq. 2, Tabs. 4–5). Δη23 and Δφ23 are also shown unfolded (Figs. 2–3).
- Unfolding: iterative Bayesian (D'Agostini, RooUnfold) with a HERWIG++ response matrix; the effect on the normalized distribution is ≈ 1%. Resolution in Δη23 and Δφ23 is ≈ 0.005–0.01 (p. 6).
- Models (p. 5–6): PYTHIA 6.422 with tunes Z2 (pT-ordered shower) and D6T (Q²-ordered), with coherence switchable via MSTP(67) (ISR) and MSTJ(50) (FSR); PYTHIA 8.145 tune 4C (pT-ordered, coherence "similar" to PYTHIA6 pT-ordered); HERWIG++ 2.4.2 (angular-ordered coherent branching, cluster hadronization, eikonal MPI; legends say "2.3"); MADGRAPH 4 (v2.24) with 2–4 partons, kT-MLM at 60 GeV, + PYTHIA6 D6T.

## Results
- Systematics are small because the distribution is normalized. Typical values (central / forward): JES 1.0 / 1.0%; JER 0.4 / 0.5%; JAR 0.5 / 0.6%; unfolding model 0.6 / 0.7%. Statistical uncertainty dominates at 4.0 / 3.7% (Tab. 3). Total systematic quoted as "about 2%" per bin (p. 7), although the per-bin σ_Syst in Tabs. 4–5 is 0.9–1.9%; each source fully correlated across β and η2 bins, sources mutually uncorrelated (p. 7). The result is insensitive to pileup (≈ 2 interactions on average) (p. 7).
- Central F(β): 0.0549 at 0–10°, minimum ≈ 0.0511–0.0515 at 50–100°, 0.0638 at 170–180° (Tab. 4). Forward F(β): 0.0388 at 0–10°, rising almost monotonically (small dips at 30–40° and 60–70°) to 0.0795 / 0.0791 at 160–180° (Tab. 5).
- MC/data ratios (Fig. 5), all ≈ (read from Fig. 5):
  - Central: PYTHIA6 Z2 and PYTHIA8 ≈ 0.88–0.92 at β < 0.5 and ≈ 1.1 at β ≈ 1.5–2. HERWIG++ is mostly within the ≈ ±4% total band.
  - Forward: PYTHIA6 Z2 and PYTHIA8 ≈ 0.75–0.8 at β < 0.5; MADGRAPH+PYTHIA6 ≈ 0.86; HERWIG++ ≈ 1.0 there. HERWIG++ overshoots (≈ 1.1–1.13) at β ≈ 1–1.6 and undershoots (≈ 0.9) at β > 2.5.
  - Authors: the data show a clear excess over PYTHIA and MADGRAPH near β = 0 and a suppression at β = π/2 (p. 7).
- χ² (full stat + syst correlations, 17 dof) in Tab. 6, as listed under Takeaways. PYTHIA6, "even though adjusted with the Tevatron data", fails at the LHC. Z2 and D6T do not differ significantly. PYTHIA8 4C is better than PYTHIA6 everywhere but is poor forward (p. 7–10).
- Coherence on/off (PYTHIA6 D6T, first branching of ISR and FSR) (Fig. 6, p. 10):
  - Coherence off: central MC/data ≈ 0.8–0.9 at small β and ≈ 1.2 at β ≈ 1.5–2.2; forward ≈ 0.75 at small β and ≈ 1.2 near β ≈ 1.5, all ≈ (read from Fig. 6).
  - Coherence on: still ≈ 0.9 at small β, ≈ (read from Fig. 6).
  - χ²/NDF "increases up to" 7.7 / 11.5 without coherence (p. 10). ISR and FSR first emissions contribute roughly equally (p. 10).
- The Δη23 and Δφ23 distributions show "reasonable agreement" with all models (Figs. 2–3, p. 4).

## Assessment
- Clean, well-unfolded LHC extension of CDF:1994zkl and D0:1997tye, with finer binning (10°; D0's ~20° bins [unverified]) and a forward region reaching |η2| = 2.5 (D0: 1.5 [unverified]).
- The qualitative picture is consistent with the Tevatron, but the hierarchy shifts. At the Tevatron, HERWIG 5.x was best and PYTHIA with AO was acceptable [unverified here; from CDF/D0 papers]. Here HERWIG++ is best only centrally, and the forward region (where coherence with the beam remnant should be strongest) is not described by any tune: the best χ²/NDF there is 3.3.
- The tension is small in absolute terms (≈ 10–25% at the edges) but highly significant given ≈ 4% statistical and ≈ 2% correlated systematic uncertainties.
- "Data support larger coherence than MC" is inferred from one generator (PYTHIA6 D6T) with coherence switched only in the first branching. Missing large-angle soft radiation could also come from:
  - initial-state recoil kinematics;
  - matching (MADGRAPH helps);
  - the treatment of wide-angle ISR in pT-ordered showers.

  The claim is model-dependent. The forward HERWIG++ overshoot at β ≈ 1–1.5 points to a shape problem, not just a lack of coherence.
- The claimed insensitivity to hadronization and UE was checked only with PYTHIA (p. 10). No NLO 3-jet fixed-order comparison was made (unlike D0's JETRAD), so the LPHD comparison is less direct than at the Tevatron.
- Minor: the HERWIG++ version is 2.4.2 in the text but "2.3" in the figure legends.
- HEPData / Rivet: not stated in the paper. The numerical tables are in the paper (Tabs. 4–5). A Rivet analysis (likely CMS_2013_I1265659) should be verified via HEPData/Rivet before relying on it.
- The CMS:2021hnp follow-up (same collaboration) did not repeat β [unverified from this paper]. It moved to ΔR23 and pT3/pT2, which are less directly coherence-specific.

## Leads
- Marchesini & Webber 1988, NPB 310, 461 ("Monte Carlo simulation of general hard processes with coherent QCD radiation"): the ISR/FSR coherence implementation that CDF/D0/CMS credit for the Tevatron success.
- Bengtsson & Sjöstrand 1987, NPB 289, 810 and PLB 185, 435: coherent vs non-coherent showers in PYTHIA; the origin of the MSTJ(50)/MSTP(67) switches.
- Gieseke, Stephens & Webber 2003, JHEP 12, 045: the HERWIG++ angular-ordered shower formalism.
- CMS:2021hnp (follow-up, ΔR23 and pT3/pT2 in 3-jet and Z+2j).
- Forward citations: any re-tune or ATLAS/LHCb coherence measurement using β, or papers using this data to test pT- vs angular-ordered showers (e.g. dipole/antenna shower validation).
- TPC/2γ 1986 PRL 57, 945 and MARK II 1986 PRL 57, 1398 (qq̄g vs qq̄γ particle flow): the e⁺e⁻ coherence references cited as background.

## Verification
Checked 2026-10-30 by an independent reader: 55 claims checked, 6 corrected, 4 unverifiable.
- Takeaway 2: excess is near β ≈ 0 only (not "β ≈ 0, π"), and relative to PYTHIA/MADGRAPH, not all MC; at β ≈ π data are at or below PYTHIA.
- Assessment: "10× finer binning" was wrong (10° vs ~20° is ≈ 2×); D0 binning/η-range now [unverified].
- Forward F(β) is not strictly monotonic (dips at 30–40°, 60–70°, 170–180°).
- "≈ 2% total systematic" is the paper's text; Tabs. 4–5 give 0.9–1.9% per bin — noted.
- "First LHC" and the LPHD/D0 inference flagged as reviewer interpretation, not paper claims.
- Confirmed: Tabs. 2–6 numbers, selection cuts, generator versions/tunes, χ²/NDF 7.7/11.5 without coherence, Fig. 5/6 read-offs, page anchors (PDF page = printed page + 2).
