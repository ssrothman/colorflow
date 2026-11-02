# Test of Colour Reconnection Models using Three-Jet Events in Hadronic Z Decays
- **ID / links:** ALEPH:2006jcu · INSPIRE 715094 · arXiv hep-ex/0604042 · DOI 10.1140/epjc/s10052-006-0017-5
- **Authors / collab, year, journal:** ALEPH Collaboration (S. Schael et al.), 2006, Eur. Phys. J. C (per DOI; the arXiv v1 PDF says only "Submitted to Eur. Phys. J. C", so the volume and page are not stated here). Preprint CERN-PH-EP/2006-xxx, 21 April 2006.
- **Type:** experimental
- **Relevance:** 3 · RQs: 1a, 1b, 2, 3
- **Full text source:** arxiv

Page anchors are arXiv PDF page numbers (pp. 1–25; text pp. 5–17, references pp. 18–19, figures pp. 20–25). The printed pages carry no page numbers.

## Takeaways
- This is a LEP1 test of CR within a single colour singlet. Using 3.38 M hadronic Z decays, the observable is the rate r(0) of gluon(-enriched) jets that have a rapidity gap (no particles in 0 ≤ y ≤ y_u) and zero charge beyond the gap. Following OPAL [8] and Friberg–Gustafson–Häkkinen [7], this is a signature of the gluon hadronising as a separate closed string after reconnection (p. 10).
- The string-based CR models are disfavoured at their default strengths. JETSET+GAL (R₀ = 0.10) overpredicts r(0) in the jet-3 sample by δ ≈ +23 % at y_u = 1.5. That is a 17σ (statistical) deviation (p. 13, Fig. 4). ARIADNE AR1 behaves similarly, with a slightly weaker effect (δ ≈ +20 %). The b-tag (≈97 % pure gluon) sample confirms this at ~7σ, with δ ≈ +1.2 for GAL at y_u = 2 (read off Fig. 10; text p. 15: "values around 1").
- The non-CR models fail in the other direction. JETSET and ARIADNE (AR0) underpredict r(0) for jets with a gap: δ ≈ −14 % and −11 % at y_u = 1.5 in jet 3 (Fig. 4), and ≈ −30 % in the b-tagged gluon jets (Fig. 10). This confirms DELPHI's (Siebel, hep-ex/0505080) finding that the standard string model underestimates neutral gluon jets with a gap (pp. 13–14).
- A tuned GAL needs a small strength: R₀ ≈ 0.02 from r(0) and ≈ 0.01 from f(0) (p. 15), versus the HERA-motivated default of 0.10 (p. 7). HERWIG cluster CR is essentially insensitive to r(0) (Fig. 5).
- The authors' inference: if Z and WW colour rearrangement are alike, JETSET+GAL and ARIADNE CR overestimate the CR-induced m_W shift (p. 17).

## Setup
- ALEPH at the Z pole (E_cm ≈ 91.2 GeV), 1992–1995. There are 3 378 000 hadronic events after selection: ≥ 5 good tracks with energy > 10 % E_cm, ≥ 14 energy-flow objects, E_vis > 50 % E_cm (p. 10).
- **Models (Tab. 1, p. 6):** SK-I (not implemented in Z decays) and SK-II (no effect in Z → qq̄) are not testable. Tested: ARIADNE 4.08 AR1 (reconnect with probability 1/N_C² if the string length λ decreases; N_C² = 9). Rathsman GAL in JETSET 7.4 (P_reco = R₀(1 − exp(−bΔA)), Eq. 1, default R₀ = 0.10, determined by Rathsman from a comparison with HERA data on the proton diffractive structure function, p. 7; interfaced with PYTHIA 5.7/JETSET). HERWIG 6.1 cluster CR (P_reco = 1/9 if the sum of squared cluster sizes decreases, p. 7). Each CR model is compared with its own non-CR version: JETSET, AR0, HW0.
- **Retuning (Sect. 3, Tabs. 2–5, pp. 7–9):** All generators are retuned with and without CR to ALEPH event shapes and charged-particle spectra (about 1 M events from 1992+1993). CR changes ⟨n_ch⟩ by −2 % (GAL), −1 % (AR1) and +1 % (HW-CR) before retuning (p. 7). Fraction of reconnected events: GAL(0.04) 0.10, GAL(0.10) 0.18, AR1 0.15, HW-CR 0.08 (Tabs. 2–4). The global-fit R₀ minimum is ≈ 0.04, and the fitted N_C² in AR1 is 8.4 ± 1.1 (p. 9). Total χ² for 168 bins (Tab. 5): JETSET 1592, GAL(0.04) 1488, GAL(0.10) 1563, AR0 1409, AR1 1190, HW0 1374, HW-CR 1476. The authors say the χ² values are only relative measures, because the systematic errors are rough. Global variables "show a slight preference for the string-based CR models" but "may not be specific enough" (p. 9).
- MC statistics after full detector simulation: 0.5–7.6 M events per model (Tab. 6, p. 11).
- **Energy-ordered analysis (Sect. 6):** Durham y_cut = 0.02 (k_T,cut = 6.5 GeV), exactly 3 jets, |cos θ_j| < 0.90, smallest interjet angle > 40°, x_j > 0.1, jet energies recomputed from angles. N_3j = 539 000 (p. 11). Jet 3 (lowest energy) has ⟨E⟩ = 17.7 GeV and gluon probability P_g = 0.693 (Tab. 7, p. 12).
- **Observables:** jet charge Q_j = n₊ − n₋ (Eq. 2). Rapidity relative to the jet axis, with neutrals included only for E > 0.6 GeV (p. 12). Gap means zero charged+neutral particles in 0 ≤ y ≤ y_u. Q_j is then computed from charged particles with y > y_u (p. 13). r(0) = N(Q_j = 0, gap)/N_3j (Eq. 3). δ = (r(0)_MC − r(0)_data)/r(0)_data. f(0) = N(Q_j = 0, gap)/N(gap) (Eq. 4).
- **b-tag analysis (Sect. 7):** two lifetime-tagged jets (P_jet < 0.01) and the third untagged (P_jet > 0.01), with |cos θ_j| < 0.766 and x_g < 0.85. About 24 600 events. The tagged jet is the true gluon jet in 97.2 % of cases (JETSET), ⟨E_g⟩ = 19.8 GeV. 18 700 of these are also the lowest-energy jet (p. 15).

## Results
- **Inclusive jet-3 charge (Fig. 1, p. 20):** JETSET describes Q₃ well, including the Q₃ = 0 fraction. GAL predicts too many neutral jets (p. 12). The data show a slight positive shift, attributed to protons from nuclear interactions in the material and reproduced by the simulation (p. 12).
- **Gap rate (Fig. 2, p. 20):** About 7 % of jet-3s in data have zero particles in 0 ≤ y ≤ 1.5. JETSET predicts too few (≈0.066 vs data ≈0.073, read off the figure) and GAL too many (≈0.079). Above y_u = 1.0 the gap-jet rate falls nearly exponentially with y_u (p. 13).
- **Neutral gap jets, jet 3 (Fig. 3, p. 21):** In the Q₃ = 0 bin with a gap in 0–1.5, data ≈ 0.0295, JETSET ≈ 0.025 and JETSET+GAL ≈ 0.036 (read off the figure). "None of the models agrees well with the data" (p. 13).
- **δ versus y_u, jet 3 (Fig. 4, p. 21; values read off the figure, statistical errors only):**

  | Model | δ at y_u = 1.0 | δ at y_u = 1.5 | δ at y_u = 2.0 |
  |---|---|---|---|
  | JETSET+GAL (R₀ = 0.10) | ≈ +0.11 | ≈ +0.23 (17σ stat, p. 13) | ≈ +0.33 |
  | ARIADNE AR1 | ≈ +0.10 | ≈ +0.20 | ≈ +0.32 |
  | JETSET+GAL (R₀ = 0.04) | ≈ +0.04 | ≈ +0.09 | ≈ +0.10 |
  | JETSET+BE₃₂ | ≈ −0.04 | ≈ −0.09 | ≈ −0.07 |
  | ARIADNE (AR0) | ≈ −0.06 | ≈ −0.11 | ≈ −0.11 |
  | JETSET | ≈ −0.06 | ≈ −0.14 | ≈ −0.20 |

  The points are cumulative and not statistically independent (p. 13). With no gap requirement (y_u = 0), all models lie within about ±0.05. GAL(0.04) "still gives somewhat too high predictions" (p. 13). BE₃₂ correlations shift δ by ≈ −0.02 for the full jet-1 and jet-3 samples, and in the opposite direction for gap events (pp. 13–14).
- **HERWIG (Fig. 5, p. 22):** Both HW0 and HW-CR overpredict r(0) for jet 3: δ ≈ +0.08 and +0.13 at y_u = 1.5, read off the figure. r(0) has "little or no sensitivity" to HERWIG CR (p. 13). For the quark-enriched jet 1 (Fig. 6), HERWIG fails badly (δ ≈ +0.22 at y_u = 1.5 and ≈ +0.5–0.6 at y_u = 2). This is attributed to HERWIG's systematically low rapidity distributions and narrow Q_j distributions (p. 13). HERWIG also has a 1.5–2.5 % per-jet multiplicity deficit in 3-jet events (p. 16).
- **Jet 1 (quark-enriched, Fig. 6):** little CR sensitivity for all models. JETSET describes the data well, and ARIADNE deviates somewhat with a gap (p. 13).
- **Normalised fraction f(0) (Eq. 4, p. 14):** The model–data differences are similar but less significant. Non-CR JETSET and ARIADNE are low by ≈ 6 % for a gap in 0–1.5, "confirming" DELPHI [11] (p. 14).
- **Corrected data and R₀ (Tab. 8, p. 14; p. 15):** r(0)_corr = 0.0234 ± 0.0004 (stat) ± 0.0015 (syst) and f(0)_corr = 0.437 ± 0.006 ± 0.010 (jet 3, gap 0–1.5). The correction factor C comes from JETSET (Eq. 5). The systematic is the largest difference when correcting with JETSET, GAL(0.04) or ARIADNE. These are compared with generator-level JETSET+GAL with Λ, σ, b retuned at each R₀ and Q₀ fixed at 1.5 GeV, because f(reco) depends strongly on Q₀ and weakly on b (pp. 14–15). Optimal R₀ ≈ 0.02 from r(0) and ≈ 0.01 from f(0) (p. 15). The paper gives no uncertainty on R₀; the abstract and conclusions quote "0.01–0.02".
- **b-tagged gluon jets (Sect. 7, Figs. 7–11, pp. 15, 23–25):** The lifetime-tag rate is 7.6 % in data vs 7.4 % in JETSET. The inclusive Q_g = 0 rate is well described by JETSET, and GAL shows a clear excess (Fig. 7). There are 1090 gap jets in data (p. 15). Q_g = 0 bin with gap (Fig. 9): data ≈ 0.018, JETSET and AR0 ≈ 0.013, CR models ≈ 0.027–0.033 (read off the figure; the dashed/dotted line styles for GAL vs AR1 are hard to separate). δ (Fig. 10) at y_u = 1.5: GAL ≈ +0.76, AR1 ≈ +0.48, JETSET ≈ −0.29, ARIADNE ≈ −0.31. At y_u = 2: GAL ≈ +1.2, AR1 ≈ +1.0, JETSET ≈ −0.53, ARIADNE ≈ −0.41. GAL deviates by ≈ 7σ (stat) at y_u = 1.5 (p. 15). The charged multiplicity of gap gluon jets (Fig. 11) shows no "clear evidence" for the spikes at n_ch = 2, 4, 6 that GAL and AR1 predict (p. 15). Data ≈ 0.0073, 0.0080, 0.0090 at n_ch = 2, 3, 4, versus GAL ≈ 0.012, 0.0093, 0.015 (read off the figure).
- **Systematics (Sect. 8, p. 16):** The authors varied y_cut over 0.01–0.03, used the JADE algorithm (y_cut = 0.08), reassigned particles to jets by angle, defined gaps with charged tracks only, and shifted the gap region to 0.5–1.5 and 1.0–2.0. "In all five cases the qualitative features of the results remain the same, although the numerical values ... may change". Track and |cos θ_j| cut variations (Tab. 9) were done for the normalised charge distributions only. There, model–data differences change within statistical errors. No full systematic error is given for δ. The 17σ and 7σ figures are statistical only.

## Assessment
- **Which models survive.** No tested model describes neutral gap gluon jets. String CR at default strength (GAL R₀ = 0.10, AR1 with N_C² = 9) overshoots by ~20–30 % in the jet-3 sample and ~50–120 % in the pure-gluon sample. Non-CR strings undershoot by ~10–20 % and ~30–50 % respectively. The data lie between the two families. A reduced-strength GAL (R₀ ≈ 0.01–0.02) is the only configuration claimed to fit, and that fit is done on just two numbers (r(0), f(0) at y_u = 1.5). A χ² or error on R₀ is not given. HERWIG (with or without CR) is not usable here because it misdescribes even the quark jet.
- **Statistical-only significances.** The 17σ is statistical. The systematic on the corrected r(0) is 6.4 % (Tab. 8, 0.0015/0.0234), which is several times the statistical error. The systematic is model-dependence of the correction only. The data–GAL difference (+23 %) is still large compared with that, so the qualitative exclusion of default GAL/AR1 looks robust. The precise R₀ value is not.
- **Degeneracy with the non-CR baseline.** The "too low" non-CR prediction could also come from colour-octet neutralisation (Minkowski–Ochs, glueballs, ref. [12]) or from gluon-jet fragmentation deficiencies unrelated to CR. A small CR strength is therefore one of several explanations of the DELPHI/ALEPH deficit, not a measurement of CR. The tuning also uses a fixed Q₀ = 1.5 GeV, while f(reco) depends strongly on Q₀ (p. 14). The R₀ value is therefore tied to that shower cut-off.
- **Link to W mass.** The m_W extrapolation assumes Z-internal and inter-W reconnection share dynamics. SK-I, the main LEP2 benchmark, is not testable here (Tab. 1). The constraint therefore applies to ARIADNE- and GAL-type CR in m_W systematics, not to SK-I. This is complementary to the L3 particle-flow result (L3_2003oci), which constrains SK-I but is insensitive to AR2/HERWIG CR (per L3_2003oci, Tab. 4 there: ΔR_N ≤ 0.01 for SK-II, AR2, HERWIG CR).
- **Link to HERA.** GAL's default R₀ = 0.10 came from a HERA F₂^D comparison (p. 7), descending from SCI (Edin:1995gi; the lineage is stated in Rathsman:1998tp, which uses SCI as its baseline — not in this paper). LEP1 wants a 5–10× smaller value. That is a genuine tension in the "universal soft colour interaction" picture, and the synthesis should note it. It may be absorbed by different shower cut-offs, which the paper does not show.
- This agrees qualitatively with OPAL EPJC 35 (2004) 293 and L3 PLB 581 (2004) 19, as the authors state (p. 5). Their numbers are not compared here.

## Leads
- OPAL, Eur. Phys. J. C 35 (2004) 293 (ref. [8]): original gluon-jet-rapidity-gap CR test and glueball search. The direct predecessor, with different conclusions on magnitude to cross-check.
- L3, Phys. Lett. B 581 (2004) 19 (ref. [10]): colour-singlet/CR search with angular gaps in symmetric three-jet Z events.
- M. Siebel (DELPHI), hep-ex/0505080, Moriond 2005 (ref. [11]): DELPHI finding that the non-CR string model underestimates neutral gap gluon jets.
- C. Friberg, G. Gustafson, J. Häkkinen, Nucl. Phys. B 490 (1997) 289 (ref. [7]): theory proposal for colour-suppressed effects and gluon-jet gaps, the RQ4 origin.
- P. Minkowski, W. Ochs, Phys. Lett. B 485 (2000) 139 (ref. [12]): colour-octet neutralisation and glueballs as an alternative explanation.
- J. Rathsman, Phys. Lett. B 452 (1999) 364 (ref. [16]): GAL model definition and the HERA-derived R₀ = 0.10.
- L. Lönnblad, Z. Phys. C 70 (1996) 107 (ref. [15]): ARIADNE dipole reconnection.
- G. Gustafson, U. Pettersson, P.M. Zerwas, Phys. Lett. B 209 (1988) 90 (ref. [1]): original WW colour-screening/CR paper.
- OPAL, Eur. Phys. J. C 45 (2006) 291 (ref. [4]): OPAL WW CR particle-flow result at 189–209 GeV.
- G. Rudolph, Moriond 2000 (ref. [20]): HERWIG CR tuning at LEP, grey literature.
- ALEPH, Phys. Lett. B 606 (2005) 265 (ref. [21]): BE₃₂ tuning, needed for the BEC cross-check.
- Forward: check for later Z-decay CR or gluon-jet gap studies citing this paper (e.g. tests of Pythia 8 CR models or rope models on LEP1 gluon jets).
