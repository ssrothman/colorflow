# Investigation of colour reconnection in WW events with the DELPHI detector at LEP-2
- **ID / links:** DELPHI:2006tie · INSPIRE 737606 · arXiv 0704.0597 · DOI 10.1140/epjc/s10052-007-0304-9
- **Authors / collab, year, journal:** DELPHI Collaboration (J. Abdallah et al.), 2007, Eur. Phys. J. C 51 (2007) 249 (CERN-PH-EP/2006-037)
- **Type:** experimental
- **Relevance:** 3 · RQs: 1b, 2, 3
- **Full text source:** zotero

Page anchors are the paper's printed page numbers (printed p. 1 = PDF page 4).

## Takeaways
- DELPHI combines two nearly uncorrelated CR probes in fully hadronic WW at 183–209 GeV (660.8 pb⁻¹):
  - **Particle flow** (L3 method, charged particles only): ⟨R⟩ = 0.979 ± 0.032 (stat) ± 0.035 (syst) at 189 GeV (Eq. 8, p. 16).
  - **Difference of W-mass estimators:** ΔM_W(std, R_cone = 0.5 rad) = 59 ± 35 (stat) ± 14 (syst) MeV/c² (Eq. 18, p. 27). This compares the standard estimator with a "hybrid cone" estimator. That estimator computes jet directions only from particles within 0.5 rad of the jet axis and keeps the original jet energies.
- Combined SK-I result: κ = 2.2 (+2.5 −1.3). This corresponds to P_reco = 52 %, with 31 % < P_reco < 68 % at 68 % CL (Eq. 22/25, p. 33). The best fit is at non-zero CR, but the preference is not significant. The combined −2 ln L is ≈3.8 at κ = 0.1, the left edge of the plot (≈ read from Fig. 18). That would disfavour no-CR at only ≈1.9σ. The paper itself quotes no significance for κ = 0 and makes no priority claim.
- The m_W-estimator method is much more sensitive to SK-I than particle flow. Particle flow alone gives κ = 4.13 (+20.97 −3.46) (Eq. 12, p. 17). ΔM_W alone gives κ = 1.75 (+2.60 −1.30) (Eq. 19, p. 27).
- The CR bias on the standard M_W(4q) estimator grows with κ:

  | κ | dM_W (MeV/c²) |
  |---|---|
  | 0.66 (SK default) | ≈55–60 |
  | 10 | ≈290 |
  | 100 | ≈435 |

  (All values ≈ read from Fig. 12.) The bias is reduced by about 2 with the R = 0.5 rad cone or p_cut = 2 GeV/c, and by about 4 with p_cut = 3 GeV/c (≈ read from Fig. 12). DELPHI's final m_W analysis uses the hybrid cone estimator for its primary result (pp. 18–19). The wider LEP "CR-robust" strategy is not discussed here.
- DELPHI's κ is "compatible with, but higher than" L3 and OPAL particle flow, and OPAL and ALEPH m_W-estimator results (p. 33).

## Setup
- LEP2 data 1997–2000, √s = 183–209 GeV, ⟨√s⟩ = 197.1 GeV, 660.8 pb⁻¹. Data from 2000 with a dead TPC sector (≈207 GeV) are analysed separately (pp. 2–3).
- MC: WPHACT + PYTHIA (DELPHI tune) for signal and ZZ; KK2f for qq̄(γ). Systematics use ARIADNE and HERWIG. BEC uses PYTHIA BE32. Large EXCALIBUR + PYTHIA samples at 200 and 206 GeV are used for the κ scans (p. 4). "Cetraro samples" are KORALW events at 189 GeV produced by ALEPH and fragmented with PYTHIA, ARIADNE and HERWIG (ALEPH tuning), each with and without CR (SK-I 100 %, AR-2, HERWIG 1/9). They are common LEP reference samples for normalisation (p. 4).
- CR models: SK-I with P_reco = 1−exp(−κV_overlap), default κ = 0.66 (Eq. 1, p. 1); HERWIG CR with probability 1/9 if the cluster mass is reduced; ARIADNE AR-2, where inter-W reconnection is allowed only for gluons with energy below Γ_W (p. 2). SK-II′ is not tested (p. 1).
- **Particle flow (Sec. 4):**
  - Charged particles with p > 100 MeV/c are used. Pre-selection: ≥ 12 charged particles and √s′ > 110 GeV.
  - Exactly 4 Durham jets at y_cut = 0.005, each with multiplicity > 3 (pp. 5–6).
  - Angular cuts: the two smallest jet–jet angles are < 100° and non-adjacent; two other angles lie in 100°–140° and are non-adjacent (p. 6).
  - Efficiency is 22 % → 15 % from 183 to 207 GeV, purity 70–75 %, correct pairing 69–82 % (Tab. 1).
  - Inside-W regions are A, C and between-W regions are B, D (Fig. 3). Projection onto per-region planes discards ≈9 % of particles; ≈13 % are ambiguous (p. 8).
  - R = ∫₀.₂^⁰.⁸ (A+C) / ∫₀.₂^⁰.⁸ (B+D) (Eq. 3, p. 11). Jackknife errors are used.
  - Detector and fragmentation calibration uses mixed semileptonic events (two hadronic W's from qq̄ℓν events combined into a pseudo-4q event) (pp. 12–14).
- **M_W estimators (Sec. 5):**
  - Standard DELPHI 4q likelihood estimator.
  - p_cut estimator: jets built only from tracks with p > p_cut.
  - Hybrid cone estimator: iterative cone of half-angle R_cone inside each Durham jet; the jet momentum is rescaled to the original jet energy (Eq. 13, Fig. 11, pp. 19–20).
  - Intermediate κ is modelled by reweighting per-event likelihoods with P_i(κ) (Eq. 14, p. 20).
  - The observable is ΔM_W(std, i), which depends on κ while common systematics largely cancel. The optimum is R_cone = 0.5 rad; p_cut = 2 GeV/c is a cross-check (p. 22).

## Results
- **Particle flow:**
  - Per-energy R values range from 0.889 ± 0.084 (183 GeV) to 1.116 ± 0.088 (206 GeV). WPHACT no-CR predicts 0.928–1.022, and SK-I 100 % predicts 0.864–0.889 (Tab. 2).
  - Fits to the √s dependence are in Tab. 3. After rescaling to 189 GeV with the no-CR fit, ⟨R⟩ = 0.979 ± 0.032 (Eq. 4, Fig. 7). With the CR-fit rescaling it is 0.987 (Eq. 5); without rescaling it is 0.999 (Eq. 6).
  - Mixed semileptonic data give ⟨R_mixedSL⟩ = 1.052 ± 0.027. The data/MC calibration factors are 1.053 (PYTHIA), 1.044 (ARIADNE) and 0.997 (HERWIG) (Eq. 7, Tab. 4).
  - Systematics (p. 14–15; total 0.035):

    | Source | Uncertainty |
    |---|---|
    | Fragmentation/detector (largest calibrated model spread) | 0.014 |
    | Calibration statistics | 0.026 |
    | BEC (interpolated between BE-inside-only and BE-all using DELPHI's 2.4σ inter-W BEC) | 0.013 |
    | qq̄ background shape | 0.003 |
    | qq̄ cross-section (±10 %) | 0.011 |
    | Energy-rescaling method | 0.009 |

  - Cetraro samples, calibrated (Tab. 5):

    | Generator | No CR | With CR |
    |---|---|---|
    | PYTHIA | 1.037 | 0.917 (SK-I 100 %) |
    | ARIADNE | 1.053 | 1.021 (AR2) |
    | HERWIG | 1.059 | 1.040 (1/9 CR) |

    (All values ±0.003–0.004.)

  - Normalised ratios: r_noCR = 0.944 ± 0.031 ± 0.034 and r_CR = 1.067 ± 0.035 ± 0.039 (Eqs. 9–10). The fractional position between no-CR and SK-I 100 % is δr = 0.49 ± 0.27 ± 0.29 (Eq. 11). This is 1.3σ from SK-I 100 %; the expected separating power is 2.5σ (p. 16). In SK-I, δr = 0.49 corresponds to ≈65 % reconnected events (≈ read from Fig. 9).
  - Particle flow alone: κ = 4.13 (+20.97 −3.46) (Eq. 12, Fig. 10).
- **M_W estimators:**
  - dM_W(κ) for each estimator is shown in Fig. 12. ΔM_W(std, cone 0.5) rises from ≈30 MeV/c² at κ = 0.66 to ≈130–210 MeV/c² at κ ≈ 100, for √s from 188.6 to 206.5 GeV (≈ read from Fig. 15).
  - Data: ΔM_W(std, R_cone) = 59 ± 35 ± 14 MeV/c² and ΔM_W(std, p_cut) = 143 ± 61 ± 29 MeV/c² (Eq. 18).
  - Systematics (Tab. 6, R_cone / p_cut): fragmentation 11/27, calibration 3/3, background 3/3, BEI–BEA 8/9 MeV/c².
  - MLBZ (mixed Lorentz-boosted Z) data/MC double differences are −1.9 (ARIADNE), −5.7 (PYTHIA) and −10.6 (HERWIG) ± 3.9 MeV/c² (Eq. 16, p. 24).
  - Semileptonic cross-check: ΔM_W = 8 ± 56 MeV/c² (Eq. 17).
  - κ from the cone observable: 1.75 (+2.60 −1.30) (Eq. 19, Fig. 16). The p_cut observable gives a minimum near κ ≈ 7 (≈ read from Fig. 17); the two differ by 1–1.5σ (Eq. 20, p. 27).
  - Non-SK-I models predict ΔM_W(std, cone) = 7.2 ± 4.1 (ARIADNE) and 19.7 ± 4.0 (HERWIG) MeV/c². The HERWIG effect is compatible with SK-I once the smaller reconnected fraction is scaled out; ARIADNE's effect is much smaller (Eq. 21, p. 31).
  - Correlations with M_W(std): 11 % (cone) and 8 % (p_cut). The estimator correlations are 83 % and 66 % (p. 31).
- **Combination:** the likelihoods are combined assuming no correlation, giving κ = 2.2 (+2.5 −1.3), i.e. P_reco = 52 % (31–68 % at 68 % CL) (Fig. 18, Eqs. 22/25, p. 33).

## Assessment
- The m_W-estimator method drives the result (Fig. 18). Its sensitivity rests entirely on SK-I's implementation of how CR moves soft, wide-angle particles. The κ value is therefore a model parameter, not a physical CR probability. ARIADNE-type CR (hard-to-see, small-effect) is essentially unconstrained by both methods. The particle-flow error is larger than the ARIADNE and HERWIG CR shifts (p. 16).
- The particle-flow systematic (0.035) exceeds L3's (0.021), driven by calibration statistics from mixed semileptonic events. DELPHI uses charged particles only. Its per-energy statistical errors (0.063–0.150, Tab. 2) are larger than L3's (0.037–0.093), even though it selects about twice as many events (1343 vs 666).
- Absolute R values differ between the experiments (DELPHI ~1.0 vs L3 ~0.92) because of different particle definitions, selections and region conventions. Only the normalised r / δr (via Cetraro samples) are comparable. For this, the LEP experiments agreed to normalise to the Cetraro PYTHIA samples, giving r = ⟨R⟩_data / R_noCR (p. 16). DELPHI's r_noCR = 0.944 ± 0.046 (total) is ~1.2σ below 1.
- In tension: DELPHI's combined κ = 2.2 (+2.5 −1.3) sits just above L3's 95 % CL upper limit k_I < 2.1 (L3:2003oci). OPAL and ALEPH also prefer smaller κ (p. 33). The κ-to-P_reco map differs between the papers: here κ = 2.2 gives 52 %, while L3 has k_I = 2.1 giving 64 % at 189 GeV. In P_reco terms, DELPHI's 31–68 % range is compatible with L3's < 64 % at 95 % CL, so the tension is mild. Given the 1–1.5σ internal disagreement between the cone and p_cut observables, the "non-zero CR" preference should be read as ≲2σ.
- The bias is large for the standard 4q estimator: ≈55–60 MeV at κ = 0.66 and ≈435 MeV at κ = 100 (≈ read from Fig. 12). This directly connects CR to the precision-EW use case and to later top-mass CR systematics.
- The method of reweighting per-event likelihoods to interpolate κ (Eq. 14) assumes the CR effect is linear in P_reco. That is reasonable for SK-I's single-reconnection model, but it is not tested for multiple reconnections.

## Leads
- L3, P. Achard et al., PLB 561 (2003) 202: particle-flow CR (= L3:2003oci, ref. [37]).
- OPAL, G. Abbiendi et al., EPJC 45 (2006) 291: OPAL particle-flow CR (ref. [38]).
- OPAL, G. Abbiendi et al., EPJC 45 (2006) 307: OPAL m_W and CR via estimators (ref. [39]).
- ALEPH, S. Schael et al., EPJC 47 (2006) 309: ALEPH m_W with CR constraint from estimators (ref. [40]).
- LEP Collaborations + LEP WW Working Group, LEPEWWG/FSI/2002-01: combined preliminary particle-flow CR (ref. [4]). The final combination is in the LEP EW W-pair Phys. Rept. 532 (2013) 119 (not cited here; worth queueing).
- J. D'Hondt & N. J. Kjaer, DELPHI 2002-048 CONF 582 (ICHEP'02): m_W-estimator CR method (ref. [12]).
- N. Kjaer & M. Mulders, CERN-OPEN-2001-026: MLBZ technique (ref. [36]).
- DELPHI, EPJC 44 (2005) 161: BEC in WW (ref. [2]). DELPHI, PLB 416 (1998) 233 and EPJC 18 (2000) 203: inclusive CR searches (ref. [10]).
- Khoze, Lönnblad, Møller, Sjöstrand, Todorova, Watson, CERN 96-01 vol. 1 p. 191: interconnection review (ref. [3]).

## Verification
Checked 2026-10-30 by an independent reader: 68 claims checked, 8 corrected, 0 unverifiable.
- Removed the claim that this was the "first LEP result" preferring non-zero CR. The paper makes no such claim. The value −2 ln L ≈ 3.8 is read at κ = 0.1 (the plot edge, Fig. 18), not at κ→0, and the ≈1.9σ is the summary's own inference.
- Hybrid cone description: the estimator excludes particles outside a 0.5 rad cone and rescales to the original jet energy. It does not specifically drop "soft" particles.
- Fig. 12 bias values are re-read (≈290 at κ = 10, ≈435 at κ = 100) and marked as plot readings. The reduction factors are made specific (≈2 for cone 0.5 and p_cut 2, ≈4 for p_cut 3). The claim that this is "the basis of the LEP CR-robust strategy" is replaced by what the paper actually says.
- Fixed the garbled PYTHIA row of the Cetraro table (with CR: 0.917).
- r_noCR deviation from 1 corrected from ~1.3σ to ~1.2σ (total error 0.046). The normalisation statement is rephrased to match p. 16.
- Corrected the implication that charged-only analysis means a smaller sample: DELPHI selects 1343 events vs L3's 666.
- Added that the L3/DELPHI tension is mild in P_reco terms because the κ→P_reco maps differ.
- Plot-derived values (Figs. 9, 15, 17) are marked "≈ read from Fig. N".
