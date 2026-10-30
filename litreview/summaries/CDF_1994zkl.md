# Evidence for color coherence in p p̄ collisions at √s = 1.8 TeV
- **ID / links:** CDF:1994zkl · INSPIRE 374155 · arXiv — · DOI 10.1103/PhysRevD.50.5562
- **Authors / collab, year, journal:** CDF Collaboration (F. Abe et al.), 1994, Phys. Rev. D 50, 5562–5579
- **Type:** experimental (with an extensive MC study section)
- **Relevance:** 3 · RQs: 1b, 1d, 2, 3
- **Full text source:** zotero (journal scan; page anchors below are journal page numbers 5562–5579)

## Takeaways
- First hadron-collider evidence for **initial–final-state color coherence**: the angular distribution of the 3rd-E_T jet around the 2nd jet in 3-jet events (variables η3, R, α) is described by HERWIG 3.2 and by a modified PYTHIA ("PYTHIA+", initial-final angular restriction on the first emission) but not by ISAJET 6.25 or standard PYTHIA 5.6 (Figs. 13–16).
- The signature is α-dependent suppression: data and coherent MCs show a turn-up toward α = +π/2 (3rd jet between 2nd jet and nearer beam), while incoherent MCs fall monotonically from α = −π/2 to +π/2 and overpopulate |α| small (Fig. 15, p. 5571).
- Standard PYTHIA 5.6 (final-state AO only, 180° opening angle in the hard-scattering frame for initial-final dipoles) is indistinguishable from PYTHIA with coherence off (Fig. 10a); i.e. **final-state AO alone is not enough**; the initial-state prong of the initial-final antennae for the first emission is what matters (Sec. VI B, Fig. 24, p. 5575–5576).
- In HERWIG, ~75% of third jets come predominantly from ISR (Tab. III); the coherence effect shows up in both ISR- and FSR-dominated subsamples but is visibly driven by the ISR one (Fig. 25).
- Color flow, not process type, drives the α shape: HERWIG classes with different color topology but same t-channel gluon exchange (qq̄'→qq̄' vs qq'→qq') differ, while gg→gg, qq̄→q'q̄', qq'→qq' (all initial-final connected) agree (Fig. 23). An early "color-flow-sensitive observable" in hadron collisions (relevant to RQ4).

## Setup
- Tevatron Run 0 (1988–89), √s = 1.8 TeV, 4.2 pb⁻¹, single-jet trigger E_T > 60 GeV (p. 5567).
- Jets: fixed cone R_cone = 0.7, energy corrected to particle level; no underlying-event subtraction (p. 5567–5568).
- Selection (p. 5568–5569): |z_vtx| < 60 cm; |η1|,|η2| < 0.7; ||φ1−φ2| − π| < 20°; E_T1 > 110 GeV (fully efficient); third jet E_T3 > 10 GeV; cosmic rejection: events with MET significance > 6 rejected if a leading jet has EM fraction < 0.05 or > 0.95 (p. 5568); for α only, 1.1 < R < π. Final sample 13 983 / 10 649 / 8 201 events after cuts 1–4 / 5 / 6 (Tab. II).
- Observables (p. 5566): third jet position relative to the second jet in (|Δφ|, ΔH) with ΔH = sgn(η2)(η3−η2); polar variables R = √(Δη²+Δφ²) and α = tan⁻¹(ΔH/|Δφ|); also η3. α = +π/2 means 3rd jet in the acute angle between jet 2 and the nearer beam (region of initial-final cone overlap, Fig. 4, 6, 7). All distributions shape-only (unit-normalized), detector-level, MC through CDF detector simulation.
- MC: HERWIG 3.2 (full AO incl. initial-final antennae), ISAJET 6.25 (no AO), PYTHIA 5.6 (FSR AO only), PYTHIA off (coherence off), PYTHIA+ (Sjöstrand's private initial-final antenna restriction on first emission, later in PYTHIA 5.7). Parton p_T > 75 GeV, |y| < 1.5, 280k events per sample (p. 5569). Also an ideal-calorimeter fast simulation for generator-level comparisons.

## Results
- PYTHIA+ vs PYTHIA off on absolute scale: coherence depletes 3rd-jet rate (fewer events pass, Tab. II: 6 940 vs 8 382 after cut 6) and depletes central η3, small R and α < 0 regions (Fig. 9).
- MC-vs-MC shapes: PYTHIA ≈ PYTHIA off; HERWIG ≈ PYTHIA+, both clearly different from PYTHIA off (Fig. 10).
- Leading-jet E_T1, E_T2 spectra described by all four generators (Figs. 11, 12) — hard scattering under control.
- η3: HERWIG and PYTHIA+ reproduce the broad, double-humped data distribution; ISAJET and PYTHIA are narrower with an excess at small |η3| (Fig. 13).
- R: PYTHIA peaks too sharply near R ≈ 1 and under-predicts large R; ISAJET deviates less visibly ≈ (read from Fig. 14); HERWIG and PYTHIA+ closer (text p. 5570–5571 only says HERWIG/PYTHIA+ reproduce data better).
- α: data show change of slope sign approaching α = π/2; HERWIG and PYTHIA+ reproduce it, ISAJET and PYTHIA decrease monotonically and overshoot small |α| (Fig. 15). MC/data ratios: HERWIG and PYTHIA+ near 1 with scatter; ISAJET and PYTHIA ratios range ≈ 0.5–1.6 across α ≈ (read from Fig. 16). Authors note "residual differences remain" even for HERWIG/PYTHIA+ (p. 5571). No χ² or quantitative significance is quoted.
- Systematics (shape only): detector effect (ideal vs CDF sim) much smaller than HERWIG–ISAJET difference (Fig. 17); 100% crack-size variations, 1σ calibration, 10% scintillator/gas and WHA scale changes negligible (Fig. 18); HERWIG hadronization on/off, HERWIG v3.2 vs v5.3, PDFs DO1/EHLQ1/EHLQ2/MT1 negligible (Fig. 19). Local η3 distortion at |η3| = 2.5 (crack) not fully reproduced (p. 5573).
- MC dissection: HERWIG coherent (initial-final color connected) subsample looks like data, incoherent subsample (qq̄-type with no I-F connection) looks like ISAJET (Fig. 20); class A vs B α differ, B/S/G alike (Fig. 23). PYTHIA with a fixed FSR first-emission cone δ = 1 rad gives a much smaller effect than observed; δ = 0.5 rad needed for an unequivocal effect (Fig. 24) → FSR restriction alone cannot reproduce the size. HERWIG: 75% "init" (f3 < 0.2) vs 25% "fin" third jets (Tab. III); coherent fraction 93% / 87% (Tab. IV). In PYTHIA (no I-F coherence) class A and B α distributions agree; in PYTHIA+ they differ (Fig. 30). E_T3 spectrum: PYTHIA+ closer to HERWIG and data than PYTHIA (Fig. 29).
- Authors' conclusion: interference between initial- and final-state emission from color-connected partons is the origin of the observed correlations; it survives hadronization and UE; NLO 3-jet parton calculations should be compared (p. 5576–5577).

## Assessment
- Strong qualitative evidence; quantitative power is limited: statistical-only error bars on plots, no χ²/significance, no unfolding. The claim rests on MC-vs-data shape comparison, so "coherence" is defined operationally as "what HERWIG/PYTHIA+ do differently from ISAJET/PYTHIA".
- The α observable is heavily sculpted by selection (η2 < 0.7, R_cone, E_T3 > 10 GeV; Appendix A, Fig. 26), so the monotonic incoherent trend is largely acceptance; the coherence signal is the deviation from it. Requires full MC simulation to interpret.
- 3rd jet at E_T > 10 GeV with R = 0.7 and no UE subtraction is a soft, UE-sensitive object; the paper argues UE is isotropic so cancels in shapes, but MPI modeling of 1994-era generators was crude. Hadronization checks were done only within HERWIG (Fig. 19a) — not a cross-model test.
- Note the MC-side subtlety: the "coherence off" vs "on" comparison in PYTHIA concerns the first ISR/FSR emission's angular restriction; it is a test of a specific shower implementation rather than of interference per se. PYTHIA+'s modifications were included in PYTHIA 5.7 (footnote, p. 5569).
- Compared to D0 (D0:1997tye): same physics idea, similar observable (D0's β plays the role of π/2 − α: β = 0 points to the beam nearer jet 2, like α = +π/2; β = π to the far beam, like α = −π/2; β = π/2 is the transverse plane, like α ≈ 0); CDF uses smaller η2 range only, larger cone, lower E_T3 threshold, less luminosity, no NLO comparison and no χ². D0 extends to forward η2, where the raw β peak toward the far beam is more pronounced (though Data/ISAJET χ² is smaller there), and adds JETRAD O(αs³). The two are consistent: both prefer HERWIG, disfavor ISAJET and PYTHIA without I-F AO.
- Tevatron Run I is the only hadron-collider context of this kind before CMS 7 TeV (2014) repeated the β measurement [unverified — not from this paper]; check that for LHC continuation.

## Leads
- CMS, "Probing color coherence effects in pp collisions at √s = 7 TeV", EPJC 74 (2014) 2901 — LHC repeat of the β/α measurement with modern generators [not cited in this paper; unverified].
- D0:1997tye (D0 PLB 414 (1997) 419) — companion measurement; and D0 W+jet coherence (Abbott et al., PLB 464 (1999) 145) — color coherence in W+jet, RQ1e.
- R.K. Ellis, G. Marchesini, B. Webber, NPB 286 (1987) 643 — initial–final coherence prescription for 2→2 used by HERWIG.
- G. Marchesini, B. Webber, NPB 310 (1988) 461 — HERWIG coherent ISR/FSR shower.
- Yu.L. Dokshitzer, V.A. Khoze, S.I. Troyan, A.H. Mueller, Rev. Mod. Phys. 60 (1988) 373 — coherence/radiation pattern theory, incl. suggestion of prompt-photon+jet tests.
- A. Bassetto, M. Ciafaloni, G. Marchesini, Phys. Rep. 100 (1983) 201 — foundational review of coherence/angular ordering.
- M. Ciafaloni, NPB 296 (1987) 249; S. Catani, F. Fiorani, G. Marchesini, PLB 234 (1990) 339 — spacelike (ISR) coherence.
- CDF preliminary proceedings (Dell'Orso 1989; Harris, Moriond 1992) — early versions, low priority.

## Verification
Checked 2026-10-30 by an independent reader: 52 claims checked, 5 corrected, 2 unverifiable.
- MET cut misdescribed: it is a cosmic-ray rejection (MET significance > 6 combined with leading-jet EM fraction < 0.05 or > 0.95), not a plain MET significance < 6 requirement.
- Fig. 14 R claim narrowed: only PYTHIA clearly peaks too sharply and lacks large-R events; the ISAJET deviation is not clearly of that form.
- Fig. 16 "±50% structure" replaced by ratio range read from the plot.
- "Motivated PYTHIA 5.7" softened to what the paper says (PYTHIA+ changes included in 5.7); D0 comparison "effect stronger forward" reworded.
- Unverifiable from the paper: CMS 2014 lead and the "only hadron-collider context before CMS" claim.
