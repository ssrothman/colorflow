# Colour reconnection in e+e- -> W+W- at sqrt(s) = 189-209 GeV
- **ID / links:** OPAL:2005cdr · INSPIRE 691121 · arXiv hep-ex/0508062 · DOI 10.1140/epjc/s2005-02439-x
- **Authors / collab, year, journal:** OPAL Collaboration (G. Abbiendi et al.), 2006, Eur. Phys. J. C 45 (2006) 291 (CERN-PH-EP/2005-035)
- **Type:** experimental
- **Relevance:** 3 · RQs: 1b, 2, 3
- **Full text source:** arxiv

Page anchors are the preprint's printed page numbers (printed p. N = PDF page N+1). All 31 PDF pages were read; the author list was skipped.

## Takeaways
- This is OPAL's final LEP2 inter-W CR measurement in fully hadronic WW (~625 pb⁻¹, 189–209 GeV). It uses two probes:
  - inclusive multiplicity, Δ⟨n_ch⟩ = ⟨n^4q⟩ − 2⟨n^qqℓν⟩;
  - particle flow, R_N, the intra-W/inter-W flow ratio integrated over 0.2 < χ_R < 0.8 (Eq. 1).
  It supersedes the earlier OPAL papers (p. 4).
- **R_N = 1.243 ± 0.025 (stat) ± 0.023 (syst)** (Eq. 2). Only **SK-I with ~100 % reconnection (k_I = 100) is excluded, at 4.4σ** (Tab. 2).
  - All other CR models (SK-I k_I = 0.9, SK-II, SK-II′, ARIADNE AR-2, HERWIG-CR) lie within 1.2σ.
  - The no-CR models (JETSET, ARIADNE, old JETSET, AR-1, HERWIG) lie 1.1–2.0σ *above* the data. Conventional HERWIG is "slightly disfavoured" at −2.0σ (Tab. 2; p. 17).
- **SK-I fit: best P_reco ≈ 37 % (k_I = 1.0), with 0.10 < P_reco < 0.56 at 68 % CL**, at a reference √s = 199.5 GeV (Fig. 9; p. 16). No-CR is not excluded: the Δχ² curve is only ≈1.3 at P_reco ≈ 0.06, its lowest plotted point (≈ read from Fig. 9b).
- **Multiplicity has no sensitivity to CR**: Δ⟨n_ch⟩ = −0.04 ± 0.25 ± 0.17. All models lie within 1.2σ, and even SK-I 100 % shifts ⟨n^4q⟩ by only ~1 % against a 0.7 % experimental error (p. 15; Tab. 2; pp. 16–17). Assuming no CR, ⟨n_ch^qq⟩ = 19.38 ± 0.05 ± 0.08 per hadronic W (p. 16).
- The expected statistical sensitivity ΔR_N/σ_stat is 7.9 for SK-I 100 %, 1.7 for SK-I k_I = 0.9, 1.3 for AR-2, 0.9 for HERWIG-CR and 0.5–0.6 for SK-II/II′ (Tab. 4). Particle flow can therefore only bound SK-I-like models in a meaningful way. These OPAL R_N inputs are the ones used in the LEP combination (ALEPH_2013dgf, Tab. 4.1).

## Setup
- **Data.** OPAL 1998–2000, ~625 pb⁻¹, six √s points from 188.6 to 206.0 GeV, with everything above 202.5 GeV merged at 206.0 (p. 5).
  - Events: 5401 W⁺W⁻ → qq̄qq̄ and 2757 qq̄ℓν candidates selected; only qq̄ℓν events with an identified e or μ are used (p. 5; the text does not say whether the 2757 is before or after this restriction).
  - Tracks: p_T > 0.15 GeV, |cos θ| < 0.96, ≥ 40 hits in the central region (p. 5).
- **CR models** (all with KORALW 1.42, tuned to Z data, pp. 5–7):
  - **SK-I.** P_reco = 1 − exp(−V k_I), where V is the space-time overlap of the colour fields. Values used: k_I = 0.9 (P_reco ≈ 34.3 %) and k_I = 100 (≈ 98 %).
    - The SK events are identical to the no-CR events up to the end of the parton shower, so samples with any reconnected fraction can be built.
    - The shower cutoff Q₀ = 1.9 GeV (OPAL JETSET tune); SK-II/SK-II′ "in particular" are sensitive to it (p. 6), and SK-I properties also "vary significantly" with it (p. 16).
  - **SK-II / SK-II′.** Vortex strings; II′ allows reconnection only if it reduces string length. P_reco = 17.2 % / 16.1 % at 199.5 GeV (p. 6).
  - **ARIADNE.**
    - AR-2: inter-W reconnections only for gluons with E_g < Γ_W, 49.4 % reconnected (p. 7).
    - AR-1: same tune, CR within each W only, with the cascade split in two stages at E_g = Γ_W to match AR-2. AR-1 is the no-CR reference for AR-2 (p. 7).
    - AR-3 (no E_g restriction) is dropped as theoretically disfavoured and as disfavoured by the OPAL Z gluon-jet data [25] = OPAL_2003njc (p. 7).
  - **HERWIG-CR.** Cluster reassociation with probability 1/9, ~23 % reconnected (p. 7).
- **No-CR samples.** JETSET 7.408 (default), HERWIG, ARIADNE, "old JETSET" (an OPAL event-shape tune) and AR-1. Inter-W BEC uses LUBOEI in PYTHIA 6.125.
  - Backgrounds: qq̄ (KK2f, plus PYTHIA), 4-fermion processes (KORALW/grc4f, KandY as alternative), ZZ → qq̄qq̄ treated as background (< 5 % in particle flow), and two-photon events (p. 8).
- **Multiplicity.** x_p integration is the default; the direct multiplicity method is a cross-check. Corrections: bin-by-bin for x_p, matrix plus bin-by-bin for n_ch (p. 9). Results are combined over √s, assuming no energy dependence (Fig. 3).
- **Particle flow** (pp. 10–12):
  - Jets: k⊥ jets with a 4C kinematic fit; five-jet-like events are rejected (log y₄₅ > −5.6).
  - Jet pairing: a likelihood combining the 5C mass with variables from OPAL PLB 507 (2001) 29, ~90 % correct.
  - Sample: 2199 events, efficiency ~40 %, purity ~86 % (Tab. 3).
  - Planes: of the two possible inter-W plane pairs, the one with the smaller sum of inter-W angles is chosen, where CR is expected to be most likely.
  - Charged particles are projected onto the 4 planes and the angle is rescaled to χ_R = χ₁/χ₀. A particle lying in several inter-jet regions is assigned to the plane where its p_T is smallest.
  - The analysis is done at detector level with background subtraction; there is no unfolding.
  - R_N errors come from event-by-event numerator and denominator and were validated on MC with > 90× the data statistics (p. 12).
  - Model comparison is done at √s = 199.5 GeV, close to the luminosity-weighted 197.8 GeV (p. 12).
- **Systematics** (Sect. 4; Tabs. 1, 5):
  - Hadronisation: half the maximum pairwise R_N spread among JETSET/HERWIG/ARIADNE/old JETSET/AR-1, dominated by HERWIG vs old JETSET.
  - BEC: 77 % of the (inter − intra)-W BEC effect.
  - Track definition, qq̄ modelling and rate (±5 %), 4-fermion modelling (KandY), ZZ rate (±11 %), and residual backgrounds.
  - √s dependence: 2 % of the statistical error, neglected (p. 15).
  - Cross-check: particle flow in qq̄ℓν events, described by all models (Fig. 8; p. 15).

## Results
- **Multiplicities** (189–209 GeV average; p. 15; Tab. 1):
  - ⟨n^4q⟩ = 38.74 ± 0.12 ± 0.26;
  - ⟨n^qqℓν⟩ = 19.39 ± 0.11 ± 0.09;
  - Δ⟨n_ch⟩ = −0.04 ± 0.25 ± 0.17;
  - combined ⟨n^qq⟩ = 19.38 ± 0.05 ± 0.08 (assumes no CR, p. 16).
  - The largest systematic on ⟨n^4q⟩ is W hadronisation (0.22, dominated by HERWIG).
  - Δ⟨n_ch⟩ predictions (Tab. 2): SK-I 100 % −0.42 (+1.2σ), SK-I 0.9 −0.29 (+0.8σ), SK-II −0.14, SK-II′ −0.16, AR-2 −0.19, HERWIG-CR +0.32 (−1.2σ). No-CR models give |Δ| ≤ 0.04 (Tab. 2; Fig. 3c).
  - The single-energy point at 199.5 GeV sits ~2σ high, ≈ read from Fig. 3c (+1.6 ± ~0.75), and is not discussed by the authors.
- **Particle flow.** Data are consistent with conventional models (Fig. 5a). Only SK-I 100 % visibly depletes the intra-W regions and fills the inter-W regions (Figs. 5b, 6b). In the R_flow ratio the data lie slightly below most models away from the jet cores (p. 11; Fig. 6).
- **R_N = 1.243 ± 0.025 ± 0.023** (Eq. 2). Systematics (Tab. 5): hadronisation 0.015, track definition 0.014, qq̄ modelling 0.010, BEC 0.002, qq̄ rate 0.002, 4-fermion 0.002, ZZ 0.001.
- Model R_N at 199.5 GeV and significance = (data − model)/σ_total, with total error 0.034 (Tab. 2):

| Model | R_N | Significance |
|---|---|---|
| SK-I (k_I = 100) | 1.092 | +4.4 |
| SK-I (k_I = 0.9) | 1.246 | −0.1 |
| SK-II | 1.273 | −0.9 |
| SK-II′ | 1.277 | −1.0 |
| AR-2 | 1.271 | −0.8 |
| HERWIG-CR | 1.282 | −1.2 |
| JETSET | 1.291 | −1.4 |
| HERWIG | 1.311 | −2.0 |
| ARIADNE | 1.286 | −1.3 |
| old JETSET | 1.280 | −1.1 |
| AR-1 | 1.304 | −1.8 |

- **SK-I scan** (Fig. 9; p. 16): Δχ²(P_reco) is fitted with a 4th-order polynomial.
  - Best fit: P_reco ≈ 37 %, k_I = 1.0; 68 % CL 0.10 < P_reco < 0.56.
  - Δχ² reaches ≈ 4.5 at P_reco ≈ 0.73 and ≈ 20 at P_reco → 1 (≈ read from Fig. 9a). A 95 % CL upper limit is not quoted; Δχ² = 4 is crossed at P_reco ≈ 0.7 (our reading).
  - The particle-flow and multiplicity results are not combined, because of correlated systematics and no expected gain (p. 16).
- **Caveat stated by the authors:** SK-I properties vary strongly with the shower cutoff, so this k_I "cannot be directly compared" with other LEP experiments. Any combination should use a common simulated sample (p. 16). The result is used to set the CR systematic in OPAL's m_W measurement [20] (p. 17).
- Per-energy R_N values scatter between ≈1.19 and ≈1.34 with errors of 0.04–0.12 (≈ read from Fig. 7). The qq̄ℓν R_N is ≈1.24–1.42, consistent with models (Fig. 8b).

## Assessment
- **What is excluded.** Only the extreme SK-I with ~100 % reconnection is excluded (4.4σ). The OPAL data on their own cannot distinguish any realistic CR model from no-CR: SK-II, SK-II′, AR-2 and HERWIG-CR have expected sensitivities ≤ 1.3σ_stat (Tab. 4).
  - The data prefer *some* reconnection in SK-I (37 %), at a weak significance. With the curve at Δχ² ≈ 1.3 near P_reco ≈ 0.06 and JETSET at −1.4σ, the no-CR disfavouring is ~1.2–1.4σ. This agrees with the LEP combination's re-derivation of OPAL alone, k_I = 1.24 (+1.13 −0.77) on the common sample (ALEPH_2013dgf, Eq. D.11; ~1.6σ from 0 by our parabolic estimate).
- **Pattern worth noting.** Every no-CR model lies *above* the data, by 1.1–2.0σ. Within the same generator, adding CR moves the prediction toward the data: AR-1 → AR-2 goes from −1.8σ to −0.8σ, and HERWIG → HERWIG-CR from −2.0σ to −1.2σ.
  - This is suggestive but not significant. The hadronisation systematic (0.015) is defined from the spread of the same no-CR models, so the significances are not independent.
- **Comparison with the other LEP experiments.**
  - L3 (L3_2003oci): consistent with no CR, best k_I = 0.08, with k_I < 1.1 at 68 % CL in its own normalisation. The LEP common machinery shifts L3 to 0.76.
  - DELPHI (DELPHI_2006tie): κ = 2.2 (+2.5 −1.3), P_reco = 52 %, with the m_W-estimator method dominating.
  - OPAL's 37 % (10–56 %) lies between L3 and DELPHI and is fully compatible with the LEP SK-I average (k_I = 1.26, ~51 % at 189 GeV).
  - **The k_I ↔ P_reco mapping differs**: here k_I = 1.0 ↔ 37 % at 199.5 GeV, while LEP common gives k_I = 1.26 ↔ 51 % at 189 GeV. As the authors warn, k_I depends on Q₀ and √s, so raw numbers should not be compared across papers.
  - Our ALEPH_2013dgf summary lists OPAL's "original publication" as p_reco = 0.43 (+0.15 −0.20). This does not match the 37 % (0.10–0.56) in this paper. Resolved: the Phys. Rept. (ALEPH_2013dgf, p. 188) attributes the 0.43 value to its Ref. [114], the OPAL m_W paper EPJC 45 (2006) 307, which combines particle flow with ΔM_W; it is not this paper's number.
- **Data consistency.** The OPAL R_N in the LEP combination (1.2426 ± 0.0248, ALEPH_2013dgf Tab. 4.1) equals this paper's 1.243 ± 0.025 (stat), so the LEP input is this measurement.
- **Methodological notes.**
  - There is no unfolding, so the comparisons are detector-level and tied to OPAL's simulation. The result cannot be re-used for modern CR models (PYTHIA 8 QCD-CR, gluon-move, Herwig 7) without OPAL software. HEPData/Rivet availability was not checked.
  - The "smaller inter-W angle" plane choice increases sensitivity, but this choice is model-motivated.
  - ZZ → 4q is treated as background without CR (< 5 %, p. 8).
- **Multiplicity as a CR probe is dead at LEP precision.** Even 100 % SK-I gives only a 1.2σ shift. This matches the LEP report's statement that inclusive observables have limited sensitivity (ALEPH_2013dgf, p. 67).

## Leads
- OPAL, "Measurement of the mass and width of the W boson", Eur. Phys. J. C45 (2006) 307 [20]: the companion m_W paper. It uses this CR result and has the p^κ / p_cut CR-suppressed estimators (source of the p_reco = 0.43 figure quoted in ALEPH_2013dgf, p. 188, Ref. [114]).
- T. Sjöstrand & V.A. Khoze, Eur. Phys. J. C6 (1999) 271 [22]: SK model applied to LEP2 WW observables, with the CR signature proposals (RQ4).
- C. Friberg, G. Gustafson & J. Häkkinen, Nucl. Phys. B490 (1997) 289 [4]: the Gustafson–Häkkinen CR model in WW, i.e. the ARIADNE AR-2 lineage.
- J. Ellis & K. Geiger, Phys. Rev. D54 (1996) 1967 [9]: space-time parton-cascade CR model, an alternative not constrained by LEP.
- D. Duchesneau, LAPP-EXP-2000-02 [16]: the original particle-flow method for WW CR. It is a non-journal method paper that all LEP experiments used.
- OPAL, Phys. Lett. B453 (1999) 153 [12] and Eur. Phys. J. C1 (1998) 395 [11]: earlier OPAL WW multiplicity CR tests, superseded here.
- DELPHI, Eur. Phys. J. C18 (2000) 203 [13]: DELPHI inclusive WW properties and CR.
- A. Ballestrero et al., J. Phys. G24 (1998) 365 [15]: cited (with [14], [16]) as a source of the LEP particle-flow CR studies (p. 4); contents not checked.
- CERN 96-01 (LEP2 Workshop) Vol. 1 p. 191 and Vol. 2 p. 159 [14, 7]: the W-mass/CR working-group report and the event-generator report with the HERWIG CR model.
- OPAL, Eur. Phys. J. C36 (2004) 297 [38]: OPAL inter-W BEC, which sets the BEC systematic here.
- OPAL, Phys. Lett. B507 (2001) 29 [27]: jet-pairing method used for the plane definition.
