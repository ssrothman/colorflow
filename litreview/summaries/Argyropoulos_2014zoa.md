# Effects of color reconnection on tt̄ final states at the LHC
- **ID / links:** Argyropoulos:2014zoa · INSPIRE 1307773 · arXiv 1407.6653 · DOI 10.1007/JHEP11(2014)043
- **Authors / collab, year, journal:** S. Argyropoulos, T. Sjöstrand, 2014, JHEP 11 (2014) 043 (LU TP 14-23, DESY 14-134, MCnet-14-15)
- **Type:** MC/model (phenomenology)
- **Relevance:** 3 · RQs: 2, 3, 4 (also 1b)
- **Full text source:** zotero

Page numbers below are the paper's printed page numbers (arXiv v1). Printed p. N is PDF page N+1.

## Takeaways
- Standard practice estimates the CR systematic on m_top as (CR on − CR off) in Pythia 8 default CR. This underestimates it, because (i) default CR never touches top-decay products ("late resonance decays") and (ii) CR off is excluded by minimum-bias data (pp. 2, 5, 15).
- Two new model classes are introduced in Pythia 8.185. The first is "top-specific" toy models (forced random/nearest/farthest, forced smallest Δλ, smallest Δλ), which reconnect gluons from top decays with the rest of the event after default CR. The second is global λ-minimising models ("swap", "move", optionally followed by a "flip" step that can reconnect the b with a q̄ from the W or with MPI partons) (pp. 5–8, Eqs. 2.5–2.6, Figs. 1–3).
- At maximal strength, forced models shift the reconstructed m_top by up to −7 GeV, against −0.4 GeV for default (Tab. 1). After tuning (forced models α ≈ 7.5% to ATLAS 7 TeV tt̄ jet shapes; swap/move to ATLAS 7 TeV min-bias), shifts are −0.6 to +0.36 GeV (Tab. 2). The authors quote ~+200/−800 MeV around default for all models and ~500 MeV for the "sophisticated" minimisation models as a realistic CR uncertainty (p. 15).
- Mechanism: m_top shifts come from (a) jet broadening/narrowing (out-of-cone leakage; Fig. 5) and (b) changed opening angles between top-decay jets (string-effect-like; Fig. 6). These compete, and negative shifts are easier than positive (pp. 11–13, 15).
- RQ4 proposals (tt̄ lepton+jets): charged multiplicity and ΣpT of particles outside the b and W jets; pT spectrum and ⟨pT⟩(n_ch) of particles outside pT > 5 GeV jets; UE pT density ρ from jet areas; ⟨n_ch⟩ in a ΔR < 0.4 cone around the top direction vs ΔR(W,b) (Figs. 8–9). Jet-axis shift Δφ(φ̄_b) and jet pull showed no significant discrimination after tuning (p. 18).

## Setup
- Pythia 8.185, tune 4C, CTEQ6L1, LO tt̄ at √s = 8 TeV, m_top = 171 GeV, Γ = 1.4 GeV (pp. 8–9). Semileptonic (e/μ) selection: anti-kt R = 0.4 jets with pT > 25 GeV and |η| < 2.5, b-tag by B-hadron ghost presence. W candidate = light-jet pair closest to m_W; top pairing minimises |m_t − m_t̄| (p. 9; Rivet).
- m_top estimator: Gaussian fit (Eq. 4.1) to the hadronic-top mass for events with 75 ≤ m_W ≤ 85 GeV and all jets pT > 40 GeV. Also a "rescaled" version with an in-situ JES factor R_JES = 80.385 GeV/m̂_W, with m̂_W fitted from the W-candidate dijet mass (defined in the text, p. 10).
- Default Pythia 8 MPI-based CR: P_rec(pT) = (R_rec pT0)²/((R_rec pT0)² + pT²) (Eq. 2.1). Gluons are inserted to minimise the λ string length (Eqs. 2.2–2.4). "Late resonance decays" (default: top shielded, decays after CR) vs "early resonance decays" (ERD: top and W decay products enter CR) (p. 5).
- Timescale argument: γ ≈ 1.5 gives a top transverse decay length ≈ 0.2 fm, below the ~1 fm hadronisation scale. So top-decay partons are "late starters" in an already partly formed string environment, which justifies separate CR rules for them. Perturbative interference above Γ_t is neglected (Khoze–Sjöstrand 1994) (pp. 1, 4–6).
- Top-specific models: after default CR, each gluon from top decay {g_t} is forced to swap colours with a gluon of {g_r} (random; nearest/farthest in invariant mass; min Δλ forced; min Δλ only if Δλ < 0). Strength α ∈ [0,1], gluons only (p. 6). Global models: swap (pairwise colour exchange if Δλ ≤ Δλ_cut), move (relocate gluon to the dipole minimising λ, Eq. 2.6), plus optional flip (one flip per singlet system, with/without junctions) (pp. 7–8).

## Results
- Max-strength (R_rec = 10, untuned) Δm̂_top (rescaled) vs CR off (Tab. 1):
  - default −0.415 (+0.209)
  - default ERD +0.381 (+0.285)
  - forced random −6.97 (−6.51)
  - forced nearest −2.87 (−1.44)
  - forced farthest −5.75 (−3.19)
  - forced smallest Δλ −1.73 (−0.75)
  - smallest Δλ −0.73 (+0.16)
  - swap −0.21, move −0.03, swap/move+flip −0.13 to −0.34
  - All ± ~0.04–0.07 GeV statistical.
- Forced random visibly broadens and shifts the m_top peak (Fig. 4). Forced random broadens jets: ratio to CR off ≈0.86 at the smallest r and above the plotted 1.05 range for r/R ≳ 0.4 (≈ read from Fig. 5 left). Minimisation models (move+flip) give slightly narrower jets (Fig. 5). Forced random makes the W decay jets more collinear (Fig. 6).
- Tuning: forced models best fit the ATLAS 7 TeV tt̄ jet shapes at α = 5–10%, fixed to 7.5% (p. 13). Swap/move need maximal strength (Δλ_cut = 0) with pT0^ref = 2.3 (CR off, swap), 2.25 (move), 2.2 (swap+flip), 2.15 GeV (move+flip), vs 2.085 in 4C (p. 14). CR off fails ⟨pT⟩(n_ch). Default and move describe it best; swap gives too small a slope, improved by flip (Fig. 7).
- After tuning, Δm̂_top vs tuned CR off (Tab. 2):
  - default +0.182, ERD +0.360
  - forced random −0.532, forced nearest −0.241, forced farthest −0.610, forced smallest Δλ −0.130
  - smallest Δλ −0.349, swap −0.110, move +0.063
  - flip variants −0.05 to +0.19
  - Rescaled values: −0.52 to +0.27.
- Conclusion from these numbers: around default, max +200 / −800 MeV for all models, ~500 MeV for the minimisation models. The authors suggest asymmetric uncertainties (p. 15).
- Proposed observables (Fig. 8):
  - Charged multiplicity outside the top jets increases strongly for forced farthest (ratio to CR off exceeds 1.8 for n_ch ≳ 120, ≈ read from Fig. 8) and decreases for move.
  - The soft-particle pT spectrum is harder with λ-minimisation.
  - UE ρ discriminates at high ρ (Fig. 9 left).
  - ⟨n_ch⟩ around the top axis is higher than CR off by ≈15–20% for forced farthest and ≈10% for forced nearest, and ≈5% lower for move, across ΔR(W,b) (≈ read from Fig. 9 right).
- Negative results: the ⟨Δφ(φ_b,φ_b̄) − Δφ(φ̄_b,φ̄_b̄)⟩ jet-axis shift separates models only at maximal CR. Jet pull (Gallicchio–Schwartz) shows no significant difference after tuning (p. 18).

## Assessment
- This is the key paper behind the "~0.5 GeV CR uncertainty on m_top" lore and the motivation for ERD/gluon-move CR variations used in later ATLAS/CMS top-mass systematics [unverified from this paper: concerns later usage]. Its m_top estimator is a simple Gaussian fit to a LO Pythia sample (acknowledged, p. 10), so the absolute numbers are indicative only. Experimental template/ideogram fits with in-situ JES may respond differently.
- The spread depends on which models one deems "realistic". The toy forced models are deliberately extreme, and their tuning to α ≈ 7.5% uses only 7 TeV jet shapes, a weak constraint. Simultaneous tuning of α_s, fragmentation and MPI parameters is not done (p. 19).
- The finding that pull is insensitive to (tuned) CR matches ATLAS 2018 (CR systematic ≤0.22% on the pull angle). The proposed UE-in-tt̄ observables were later measured (CMS UE in tt̄, EPJC 79 (2019) 123, from memory), which provides a natural cross-check.
- A conceptual point relevant to RQ1/2: CR involving top-decay partons is justified by space-time arguments (decay length ~0.2 fm < 1 fm). These are heuristic. No first-principles colour dynamics are involved. All models are N_C → ∞. Only forced/plain smallest Δλ, swap, move and flip use λ (string length). Forced random is stochastic, and forced nearest/farthest select partners by invariant mass m(g_t,g_r)² (p. 6).
- Some top-specific models change the W jet opening angle (Fig. 6). This links to the string/drag effect and to W-mass-based JES calibration. The rescaled m_top partly absorbs CR effects, which the authors exploit, but this could mask CR in m_W-calibrated analyses.

## Leads
- Christiansen & Skands 2015 ("String formation beyond leading colour", JHEP 08 (2015) 003, publication details not in this paper; ref. [34] "to appear"): the QCD-based CR model in Pythia 8, next generation of CR for top.
- Skands & Wicke 2007, EPJC 52 (2007) 133: non-perturbative QCD effects and the top mass at the Tevatron (Pythia 6 CR models, m_W rescaling).
- Khoze & Sjöstrand 1994, PLB 328 (1994) 466: colour correlations and multiplicities in top events (perturbative interference suppression above Γ_t).
- Sjöstrand & Khoze 1994, Z. Phys. C 62 (1994) 281: CR in W⁺W⁻ (SK-I/II), the geometrical-overlap picture.
- Juste et al. 2013, arXiv:1310.0799: top-mass determination subtleties incl. CR (review).
- Sjöstrand 2013, arXiv:1310.8073: CR and its effects on precise LHC measurements (review).
- Gieseke, Röhr, Siódmok 2012, EPJC 72 (2012) 2225: Herwig++ colour reconnection.
- ATLAS 2013, EPJC 73 (2013) 2676: jet shapes in tt̄ at 7 TeV (data used to tune the forced models). CMS-PAS-TOP-13-007: UE and b-fragmentation in tt̄.

## Verification
Checked 2026-10-30 by an independent reader: 52 claims checked, 4 corrected, 3 unverifiable.
- Eq. 4.1 is the Gaussian fit function. R_JES is defined in the text on p. 10, not by Eq. 4.1. Fixed.
- Fig. 5: forced-random jet-shape ratio leaves the 1.05 range at r/R ≈ 0.4, not ≳0.45. Marked as plot-read.
- Assessment: the claim that all models are string-length minimisation "apart from forced random" was wrong, because forced nearest/farthest use invariant mass. Fixed.
- Mechanism page anchor corrected (pp. 11–13, 15). Fig. 8/9 values are now marked ≈ and refined (Fig. 9: forced farthest ≈+15–20%, nearest ≈+10%, move ≈−5%).
- Unverifiable from the paper: later ATLAS/CMS usage ("lore"), CMS UE-in-tt̄ EPJC 79 (2019) 123 (still from memory), and the Christiansen–Skands publication details (cited only as "to appear").
- Confirmed exactly: every Tab. 1 and Tab. 2 entry and the stated ranges, the +200/−800 MeV and ~500 MeV conclusions (p. 15), α = 5–10% → 7.5% (p. 13), the pT0^ref values and 4C's 2.085 (p. 14), the generator setup (8.185, 4C, CTEQ6L1, 171/1.4 GeV, 8 TeV), the selection and pairing (p. 9), γ ≈ 1.5 / 0.2 fm, Eq. 2.1, the model definitions (pp. 6–8), the swap slope / flip improvement (Fig. 7), the jet-pull null result (p. 18), and the Leads references [2], [6], [7], [12], [15], [17], [19], [28] and [34].
