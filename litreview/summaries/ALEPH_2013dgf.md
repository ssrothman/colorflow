# Electroweak Measurements in Electron-Positron Collisions at W-Boson-Pair Energies at LEP
- **ID / links:** ALEPH:2013dgf · INSPIRE 1219330 · arXiv 1302.3415 · DOI 10.1016/j.physrep.2013.07.004
- **Authors / collab, year, journal:** ALEPH, DELPHI, L3, OPAL collaborations and the LEP Electroweak Working Group, 2013, Phys. Rept. 532 (2013) 119
- **Type:** experimental (LEP-wide combination / review)
- **Relevance:** 3 · RQs: 1b, 2, 3
- **Full text source:** arxiv

Read for this summary: Ch. 4 (Final-State Interconnection: CR §4.1, BEC §4.2, pp. 66–84), the W-mass systematics and consistency checks (§7.3–7.7, pp. 135–143), and App. D (CR combination tests, pp. 186–189). The rest of the report (cross sections, TGCs, etc.) was not read.

## Takeaways
- This is the final LEP-wide colour-reconnection (CR) result in W⁺W⁻→qq̄qq̄. It combines DELPHI, L3 and OPAL particle-flow measurements with ALEPH, DELPHI and OPAL m_W-estimator differences, all interpreted in the Sjöstrand–Khoze SK-I model: **k_I = 1.26 (+0.84 −0.64)**, i.e. a preferred **reconnection probability of 51 % at 189 GeV**, with a 68 % CL range of 0.62 ≤ k_I ≤ 2.10 (Eq. 4.10; Fig. 4.3; §4.1.5, p. 74).
- **No-CR is disfavoured at 2.8σ (99.5 % CL) but not excluded.** The "100 %-reconnection" SK-I extreme is excluded at 6.9σ (§4.1.5, p. 74). No single experiment excludes no-CR at 2σ: from the App. D fits, ALEPH's interval includes k_I = 0, L3's is ~0.6σ from it, and DELPHI and OPAL alone prefer k_I > 0 at only ~1.6σ. The 2.8σ preference appears only in the combination (Fig. 4.3; App. D).
- **The combination is SK-I specific.** ARIADNE-2 (~22 % reconnected at 189 GeV) and HERWIG CR (1/9) are related to it only through the claim that models behave similarly at equal reconnection fraction (p. 67). No separate combined limits on them are given. ARIADNE-1 and Rathsman GAL with default parameters are ruled out by Z→3-jet data (p. 66–67).
- CR remains the **largest single systematic on m_W(qqqq): 35 MeV** after the modified jet reconstruction. This compares with 19 MeV for hadronisation and 7 MeV for BEC (Tab. 7.3). As a result the qqqq channel gets only 22 % weight in the LEP m_W (p. 139). Δm_W(qqqq − lνqq) = −12 ± 45 MeV with the FSI uncertainties set to zero (Eq. 7.10), so there is no sign of an FSI bias.
- **Inter-W Bose–Einstein correlations are disfavoured.** The measured strength relative to LUBOEI "full BE" is 0.17 ± 0.13 (Eq. 4.23), with a 68 % CL upper limit of 0.30. This gives |Δm_W(BEC)| ≤ 7 MeV (§4.2.5, p. 80).

## Setup
- LEP-II e⁺e⁻→W⁺W⁻ at √s = 183–209 GeV (particle flow: data extrapolated to 188.6 GeV), with the full LEP-II luminosity (Tab. 4.2: 550–683 pb⁻¹ per experiment for BEC).
- **CR model.** SK-I (string "flux tubes" as Gaussian cylinders): p_reco = 1 − exp(−I k_I), where I is the space-time overlap integral of the strings from the two Ws (p. 67). p_reco(k_I) comes from a common LEP SK-I MC sample at 189 GeV (Fig. 4.1 top). In the same picture, perturbative interference is expected to shift m_W by only O(1 MeV), while non-perturbative CR shifts it by O(10 MeV) (p. 66).
- **Particle-flow method** (DELPHI, L3, OPAL; analogous to the 3-jet "string effect"). Four jets are assigned to Ws, giving 2 intra-W and 2 inter-W planes. Particles are projected onto these planes, and densities in the normalised angle φ_r = φ/φ₀ are summed over the two regions of each type. The observable is R_N = ∫_{0.2}^{0.8} (intra-W) / ∫_{0.2}^{0.8} (inter-W) (Eq. 4.1), and CR lowers R_N.
  - DELPHI and L3 use a "topological selection" of planar events: efficiency 12–22 %, purity 70–85 %, correct pairing 70–91 %. OPAL uses its m_W selection: efficiency 40 %, purity 86 %, correct pairing 90 % (p. 68).
  - **Normalisation:** each experiment's R_N is divided by its own R_N for a *common* no-CR sample (KORALW + JETSET) passed through each detector simulation: r = R_N^data / R_N^no-CR (Eq. 4.2). Inputs from L3 and OPAL are in Tab. 4.1. DELPHI supplies Δχ²(k_I) likelihoods instead.
  - The SK-I r(k_I) is parametrised by Eq. 4.4 (Fig. 4.1 bottom). r saturates at ~0.87 (L3) and ~0.835 (OPAL) for k_I→∞.
- **m_W-estimator method** (ALEPH, DELPHI, OPAL). The observable is the difference Δm_W between a standard estimator and a CR-suppressed one. Because only differences are used, the correlation with the m_W measurement itself is ~10 % (p. 73). The estimators are:
  - ALEPH: p_cut 1–3 GeV and cone radius R = 0.4–1.0 rad with Durham-PE jets.
  - DELPHI: cone cut R = 0.5 rad and p_cut = 2 GeV, with an iterative cone around Durham jets.
  - OPAL: p_cut = 2.5 GeV versus p^κ weighting with κ = −0.5 (p. 73).
- **Statistical combination.** A total Δχ²(k_I, c₁…c₆) is formed (Eq. 4.9). Correlated systematics enter through auxiliary nuisance shifts c_i·δ_i(k_I), with correlation coefficient 0.5 between the c_i (Eqs. 4.3, 4.5–4.8; p. 74).
  - The correlated sources are hadronisation-model spread (JETSET/ARIADNE/HERWIG), background (qq̄, ZZ) scale and shape, and intra-W BEC. Detector effects and 4-jet background corrections are uncorrelated (p. 69, p. 73).
  - The ALEPH δ values are scaled up by 11 % to account for BEC, which the original ALEPH analysis did not include (p. 73).
- **BEC method.** The "mixing method" compares hadronic WW events with "mixed" events built from the hadronic sides of two different semileptonic events. Inter-W correlations then appear in Δρ(Q), D(Q) and δ_I(Q) (Eqs. 4.16–4.18). Like-sign minus unlike-sign double differences/ratios remove non-BEC sources such as CR and energy-momentum conservation (Eqs. 4.19–4.20). D′ and Δρ′ (Eq. 4.21) instead normalise data to MC without inter-W BEC, to reduce mixing artefacts. ALEPH also uses R*(Q) (Eq. 4.22).
  - The model is LUBOEI (BE₃₂), tuned to Z and semileptonic-W data. Results are expressed as the fraction of the "fullBE" − "noBE" difference that is seen in data (p. 78).

## Results
**Colour reconnection**
- Particle-flow inputs: L3 R_N^data = 0.8436 ± 0.0217 vs JETSET 0.8622, SK1(100 %) 0.7482, HERWIG 0.8822, ARIADNE 0.8754. OPAL R_N^data = 1.2426 ± 0.0248 vs JETSET 1.2910, SK1(100 %) 1.0780, HERWIG 1.3110, ARIADNE 1.2860 (Tab. 4.1). The absolute R_N differs a lot between experiments because the selections differ. Only the ratio r to common MC is combined.
- Individual results re-derived with the common machinery (App. D, pp. 186–189; Fig. 4.3):

| Experiment | k_I in this combination | Original publication |
|---|---|---|
| ALEPH | 0.34 (+1.86 −0.34) incl. +11 % BEC syst. (Eq. D.5); 0.33 (+1.82 −0.33) without (Eq. D.4) | Eq. D.4 "agrees well" with Ref. 111 (value not quoted) |
| DELPHI | 2.12 (+2.61 −1.33) (Eq. D.9, ρ = 0.5 between inputs) | 2.2 (+2.5 −1.3), Ref. 128 (Eq. D.6) |
| L3 | 0.76 (+1.89 −1.22) (Eq. D.10) | 0.08 (+1.02 −0.08), Ref. 129 |
| OPAL | 1.24 (+1.13 −0.77) (Eq. D.11) | p_reco = 0.43 (+0.15 −0.20), i.e. k_I ≈ 1.3 (+1.1 −0.8); k_I < 2.3 at 68 % CL — from Ref. [114], OPAL EPJC 45 (2006) 307 (m_W paper, particle flow + ΔM_W combined), p. 188; the particle-flow-only paper OPAL:2005cdr quotes 37 % (10–56 % at 68 % CL) |

  - The L3 difference is attributed to L3 using its own tuned no-CR reference MC instead of the common sample. It is called compatible within the hadronisation systematic (p. 188).
  - In Fig. 4.3 (curves start at k_I ≈ 0.1) no single-experiment curve exceeds Δχ² ≈ 4 at low k_I, so none alone excludes no-CR at 2σ. From the quoted errors, the Δχ² at k_I = 0 is roughly 0 for ALEPH, ~0.4 for L3, and ~2.5 for both DELPHI and OPAL (our parabolic estimate, not stated in the paper).
- **LEP combined: k_I = 1.26 (+0.84 −0.64)** (Eq. 4.10). This corresponds to p_reco ≈ 51 % at 189 GeV (p. 74).
  - No-CR is disfavoured at 99.5 % CL (2.8σ). The paper also says "absence of CR cannot be excluded, but is disfavoured … at more than two standard deviations" (p. 74).
  - The extreme SK-I with ~100 % reconnection is excluded at 6.9σ.
  - 68 % CL: 0.62 ≤ k_I ≤ 2.10 (§4.1.5).
- Other observables (inclusive multiplicity, thrust, rapidity, p_T, ln(1/x_p), identified kaons and protons) were found to have only limited sensitivity (p. 67).

**CR in the W mass**
- With standard jet reconstruction, CR shifts m_W by up to ~100 MeV, and the shifts stay large even inside the measured k_I constraints (p. 137). The experiments therefore cut or de-weight soft particles (p_cut, cone, p^κ). This reduces the CR effect in ARIADNE, SK and HERWIG, at the cost of statistical precision (p. 137).
- The central m_W uses no-CR MC. The CR systematic is the shift from data compared with SK-I at **k_I = 2.10** (the 68 % CL upper limit). It is evaluated per √s, treated as symmetric, and taken as fully correlated across experiments and energies. **It gives 35 MeV on m_W(qqqq)**, 8 MeV on the combined m_W and 27 MeV on Γ_W, where no CR-suppression is applied (Tab. 7.3; pp. 137–138).
- The qqqq error budget (MeV) is: hadronisation 19, CR 35, BEC 7, total systematic 44, statistical 40, total 59 (Tab. 7.3). Without systematics the statistical error would be 31, and the stated reason for the difference is the de-weighting caused by large correlated FSI uncertainties (Tab. 7.3 caption).
- m_W(lνqq) = 80.372 ± 0.030 ± 0.021 GeV and m_W(qqqq) = 80.387 ± 0.040 ± 0.044 GeV, with correlation 0.20 (Eqs. 7.8–7.9; Fig. 7.2). With BEC and CR uncertainties set to zero, Δm_W(qqqq − lνqq) = −12 ± 45 MeV (Eq. 7.10). The authors conclude that the modified jet reconstruction suppresses FSI effects well (p. 140).
- The qqqq weight in the combination is 22 % (p. 139). LEP m_W = 80.376 ± 0.033 GeV (Eq. 7.7/7.12).

**Bose–Einstein correlations**
- Data and samples are listed in Tab. 4.2. Example distributions are Figs. 4.4–4.7: ALEPH Δρ′, DELPHI δ_I, L3 D/D′, OPAL D.
- Most precise input from each experiment, as "fraction of LUBOEI fullBE seen" (Tab. 4.4):

| Experiment (observable) | Fraction of fullBE |
|---|---|
| ALEPH (D′) | −0.05 ± 0.14 ± 0.17 |
| DELPHI (δ_I) | +0.51 ± 0.21 ± 0.12 |
| L3 (D′) | +0.08 ± 0.17 ± 0.12 |
| OPAL (D) | +0.33 ± 0.32 ± 0.32 |

  The ALEPH R* analysis gives −0.23 ± 0.35 ± 0.20 (Tab. 4.4).
- **Combined fraction: 0.17 ± 0.095 (stat) ± 0.085 (syst) = 0.17 ± 0.13**, χ²/dof = 3.5/3 (Eq. 4.23).
  - The LUBOEI inter-W BEC model is "disfavoured" (§4.2.5, p. 80).
  - The 68 % CL upper limit on the strength is 0.30.
  - The full-strength shift is −35 MeV with standard reconstruction and −23 MeV with CR-optimised reconstruction, giving |Δm_W| ≤ 0.30 × 23 = 7 MeV (p. 80).
- Intra-W BEC is included in the MC through BE₃₂, which describes lνqq data well (p. 138).

## Assessment
- **How strong the CR evidence is.** The 2.8σ "evidence" only appears after combining. It depends on the common no-CR reference (KORALW + JETSET). The L3 example shows that changing the reference MC tune moves L3's k_I from 0.08 to 0.76 (App. D, p. 188).
  - The hadronisation-model spread is treated as a nuisance parameter. Still, the outcome depends on assuming that JETSET with LEP1 tunes describes the no-CR particle flow at the per-mille level.
  - This result should be read as "the data prefer some reconnection in SK-I relative to a 2013-era JETSET baseline". It is not a model-independent observation of CR.
  - Modern tunes, and CR models such as PYTHIA 8's QCD-based CR, gluon-move or Herwig 7 CR, were never confronted with this combination. Re-analysis would need preserved data or Rivet implementations; it would be worth checking HEPData for availability.
- **Model coverage is narrow.** The constraint is formally only on SK-I. ARIADNE-2 and HERWIG enter only through the "equal reconnection fraction" heuristic (p. 67). SK-II, the Gustafson–Häkkinen model and Ellis–Geiger are not constrained directly.
- **Consistency with the individual papers.** The individual-experiment statements in our other summaries agree with this picture: no single experiment saw significant CR (e.g. L3 R_N = 0.915 ± 0.023 ± 0.021 in its own normalisation; DELPHI κ = 2.2 (+2.5 −1.3)). The combined p_reco ≈ 51 % is notably larger than the ARIADNE-2 (~22 %) and HERWIG (~11 %) default fractions, but the 68 % interval [0.62, 2.10] in k_I is wide.
- **Practical lesson for m_W.** CR, not statistics, limits fully hadronic m_W. It costs ~35 MeV even after soft-particle suppression, which is directly analogous to the CR systematic on the top-quark mass at hadron colliders (seed topic). Δm_W(qqqq − lνqq) = −12 ± 45 MeV is too imprecise to constrain CR further (its error is larger than the CR systematic itself).
- **BEC.** The inter-W BEC limit is fairly robust because the mixing method is model-independent except for background subtraction (p. 76). The translation to an m_W shift is LUBOEI-specific and assumes a linear relation. DELPHI alone sees +0.51 ± 0.24, a ~2σ excess, while the others are near zero; with χ²/dof = 3.5/3 the combination is still consistent.

## Leads
- Sjöstrand & Khoze, Z. Phys. C62 (1994) 281 [102]: defines the SK-I/II CR models used throughout. This is the core CR theory paper.
- Gustafson, Pettersson & Zerwas, PLB 209 (1988) 90 [101]: the original proposal of colour rearrangement in WW.
- Khoze & Sjöstrand, EPJC 6 (1999) 271 [117]: CR signatures in identified hadrons, an RQ4-type test proposal.
- OPAL, EPJC 45 (2006) 291 [115] and DELPHI, EPJC 51 (2007) 249 [128]: the particle-flow CR measurements that feed the combination (check whether they are already in the queue).
- ALEPH, EPJC 47 (2006) 309 [111] and OPAL, EPJC 45 (2006) 307 [114]: CR constraints from m_W estimators (p_cut / κ weighting).
- ALEPH EPJC 48 (2006) 685, L3 PLB 581 (2004) 19 and OPAL EPJC 35 (2004) 293 [108–110]: Z→3-jet tests that rule out ARIADNE-1 and GAL.
- Ellis & Geiger PRD 54 (1996) 1967 [106] and Rathsman PLB 452 (1999) 364 [107]: alternative CR models (space-time parton cascade, GAL).
- De Wolf hep-ph/0101243 [144] and Chekanov, De Wolf & Kittel EPJC 6 (1999) 403 [142]: the inter-W correlation and mixing-method formalism for BEC/CR.

## Verification
Checked 2026-10-30 by an independent reader: 62 claims checked, 5 corrected, 0 unverifiable.
- ALEPH row: the in-combination value is 0.34 (+1.86 −0.34) with BEC syst. (Eq. D.5); the 0.33 (+1.82 −0.33) fit (Eq. D.4) reproduces the original ALEPH result. The lower error was missing.
- DELPHI row: the lower error −1.33 was missing (Eq. D.9).
- Fig. 4.3 reading: the claim that DELPHI's Δχ² at k_I = 0 is below 1 conflicts with D.9 (2.12, −1.33 implies ~2.5). It is replaced by an estimate from the quoted errors. The curves start at k_I ≈ 0.1.
- Takeaway "every experiment is consistent with no CR" was sharpened: DELPHI and OPAL alone each prefer k_I > 0 at ~1.6σ, and none reaches 2σ.
- BEC: Eq. 4.21 (D′, Δρ′) is MC normalisation, not a like/unlike-sign construction. App. D page range corrected to pp. 186–189.
