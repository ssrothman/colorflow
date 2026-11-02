# A study of coherence of soft gluons in hadron jets
- **ID / links:** OPAL:1990vmr · INSPIRE 297564 · arXiv — · DOI 10.1016/0370-2693(90)91911-T
- **Authors / collab, year, journal:** OPAL Collaboration (M.Z. Akrawy et al.), 1990, Phys. Lett. B 247 (1990) 617–628
- **Type:** experimental
- **Relevance:** 3 · RQs: 1a, 2, 3
- **Full text source:** zotero

## Takeaways
- This is the first LEP measurement of the charged-particle ξ = ln(1/x_p) spectrum (the "hump-backed plateau") at the Z⁰, put forward as a test of intra-jet soft-gluon coherence via MLLA + LPHD. At 91 GeV the peak is at ln(1/x₀) = 3.603 ± 0.013 (stat) ± 0.040 (syst), i.e. p₀ = 1.24 GeV/c (p. 626).
- Combined with TASSO 14–44 GeV, the peak moves linearly in ln E_cm with slope b = 0.637 ± 0.016 (Eq. 6, p. 626). The MLLA predicts 0.627 (Tab. 4). Pure phase space (no coherence) would give b = 1 according to the authors (p. 626).
- The ξ shape at 91 GeV is described by the coherent MCs and also by an incoherent shower with string fragmentation; only incoherent shower + IF misses it (Fig. 2, p. 623; Ariadne is not shown in Fig. 2). Only the energy evolution of the peak discriminates (Tab. 4):
  - Jetset coherent + string: 0.663 ± 0.019.
  - Herwig (coherent + cluster): 0.629 ± 0.036.
  - Ariadne (dipole + string): 0.686 ± 0.020.
  - Jetset incoherent + string: 0.692 ± 0.012, which the authors call 2.8σ above the data (p. 627).
  - Jetset incoherent + independent fragmentation (IF): 0.952 ± 0.017, or 1.004 ± 0.023 for E_cm ≥ 35 GeV. This model clearly fails.
- The authors state that string fragmentation "partly incorporates coherence effects" (p. 623, 627). So the clean exclusion is only of incoherent shower + IF. Incoherent shower + string is disfavoured but not excluded, and by our arithmetic it is only about 1σ further from the data than coherent Ariadne (see Assessment).
- In every MC the hadron-level slope is larger than the parton-level slope: Jetset coherent 0.597 → 0.663, Herwig 0.600 → 0.629 (Tab. 4). Hadronization therefore shifts the observable. This is the opening that Boudinov et al. (Boudinov:1993mc) later exploit.

## Setup
- LEP1, OPAL, E_cm = 88.28–95.04 GeV, ≈ 1.3 pb⁻¹. The cuts below leave 22 959 multihadronic events (p. 619–620).
- Track selection (p. 619–620):
  - ≥ 5 well-measured tracks, each with ≥ 40 jet-chamber hits (|cos θ| ≲ 0.92), p_T to the beam > 200 MeV/c and |d₀| < 5 cm.
  - Track energy sum > 5 GeV; |cos θ_thrust| < 0.86.
- Observable: the charged-particle (1/σ) dσ/d ln(1/x_p), with x_p = 2p/E_cm.
  - Corrected bin by bin for acceptance, resolution and ISR using MC + detector-simulation factors c(x_p) (ref. [9]; corrections from Jetset and Herwig agree within statistics, p. 620), which are < 20 % everywhere.
  - Range 0.20 ≤ p ≤ 45 GeV/c (0 ≤ ln(1/x_p) ≤ 5.4) (p. 620).
  - 5 % normalization systematic. Bin-to-bin systematics are "much smaller" and are not shown. Errors in Tab. 1 are statistical only (p. 620–621, Tab. 1).
  - Hadronization model dependence of the correction is ≤ 0.5 % (p. 620).
- Lower-energy input: TASSO ln(1/x_p) and ln p spectra at 14, 22, 35 and 44 GeV (ref. [2], DESY 90-013) (p. 623–624, Fig. 3).
- Analytic formulae (all assume N_f = 3; fits are restricted to 2.5 ≤ ln(1/x) ≤ 4.5) (p. 621–622):
  - Full MLLA spectrum (Eq. 1), with free parameters Λ_eff and K(Y). K(Y) is the LPHD normalization.
  - Gaussian approximation (Eq. 2), with peak ln(1/x₀) = 0.5Y + c₂√Y + O(1) (Eq. 3).
  - Gaussian with higher moments (Fong–Webber, Eq. 4), with free Λ_eff, N(Y) and O(1).
- Monte Carlos (p. 623):
  - Jetset 7.2 (coherent shower + string) and Herwig 3.4 (coherent shower + cluster), both tuned to OPAL event shapes (ref. [9]).
  - Ariadne (dipole cascade).
  - Jetset with incoherent branching + string.
  - Jetset with incoherent branching + IF.
  - The two incoherent options were retuned to reproduce ⟨n_ch⟩ and roughly the peak position at 91 GeV.
  - All fragmentation parameters are frozen at their 91 GeV values when extrapolating to lower energies (p. 623, 626).

## Results
- **Spectrum at 91 GeV:** the broad maximum is at ln(1/x₀) ≈ 3.6 (p. 620). Fit parameters (Tab. 2):
  - Eq. 1: Λ_eff = 0.253 ± 0.030 GeV, K = 1.28 ± 0.01, χ²/df = 1.30.
  - Eq. 2: Λ_eff = 0.203 ± 0.030 GeV, K_G = 0.19 ± 0.01, O(1) = −0.38 ± 0.09, χ²/df = 0.97.
  - Eq. 4: Λ_eff = 0.255 ± 0.026 GeV, N(Y) = 21.4 ± 0.3, O(1) = −1.00 ± 0.07, χ²/df = 0.94.
- **Range of validity of the analytic forms** (Fig. 1, p. 623):
  - Eqs. 1–2 describe the peak and its high-ln(1/x) fall-off but miss the non-relativistic small-x_p region.
  - Eq. 4 fits small x_p very well but overestimates the yield at high x_p.
- **MCs at 91 GeV** (Fig. 2, p. 623):
  - Jetset 7.2, Herwig 3.4 and incoherent shower + string all describe the spectrum well.
  - Incoherent shower + IF predicts a higher maximum and falls faster than the data for x_p > x₀.
- **Energy dependence of the spectra** (Fig. 3a,b; Tab. 3; p. 625):
  - With Λ_eff and O(1) fixed at 91 GeV, Eq. 1 describes TASSO 14–44 GeV for p > Λ_eff, given a per-energy normalization.
  - K(Y) rises from 1.28 ± 0.01 (91 GeV) to 1.46 ± 0.02 (14 GeV). The authors read this as "a 15 % decrease" from 14 to 91 GeV and as possibly an energy-dependent LPHD effect.
  - χ²/df for the K(Y) fits: 1.3, 3.4, 4.9, 0.7, 0.6 at 91, 44, 35, 22, 14 GeV. For the N(Y) (Eq. 4) fits: 0.9, 1.8, 18.0, 1.4, 2.2 (Tab. 3).
  - Eq. 4 underestimates the peak height and overestimates high x_p (p. 625).
- **MCs vs energy** (Fig. 3c, p. 625): Jetset and Herwig tuned at 91 GeV describe high-momentum data at all energies. At small E_cm both overestimate the yield at the peak and at low momenta.
- **Peak position** (p. 625–626):
  - Determined by averaging 5th-order polynomial fits and distorted-Gaussian fits (Eq. 5) over bin ranges: ln(1/x₀) = 3.603 ± 0.013 ± 0.040, ln p₀ = 0.216 ± 0.013 ± 0.040 (p₀ = 1.24 GeV/c).
  - Fig. 4 compares this with Eq. 3 using the 91 GeV shape parameters (Λ_eff = 0.203 GeV, O(1) = −0.384); the agreement is called "excellent".
  - Fitting Eq. 3 to the five peak positions gives Λ_eff = 0.212 ± 0.020 GeV and O(1) = −0.321 ± 0.60 (as printed).
  - Dropping O(1) can be compensated by Λ_eff ≈ 0.35 GeV (p. 626).
- **Linear fit (Eq. 6):** b = 0.637 ± 0.016, c = 0.735 ± 0.067 (p. 626).
- **Slopes in Tab. 4** (partons / hadrons):

  | Model | Coherence | Fragmentation | Partons | Hadrons |
  |---|---|---|---|---|
  | Data | | | — | 0.637 ± 0.016 |
  | MLLA (Eq. 1) | yes | — | 0.627 | — |
  | Herwig | yes | cluster | 0.600 ± 0.012 | 0.629 ± 0.036 |
  | Ariadne | yes | string | — | 0.686 ± 0.020 |
  | Jetset | yes | string | 0.597 ± 0.036 | 0.663 ± 0.019 |
  | Jetset | no | string | 0.666 ± 0.003 | 0.692 ± 0.012 |
  | Jetset | no | independent | — | 0.952 ± 0.017 |

  - For the incoherent Jetset shower the parton ξ distribution is flat with no clear maximum, so the mean ln(1/x_p) is used for the parton slope (p. 626).
  - Ariadne is "slightly larger than observed". Incoherent + string is 2.8σ above the data. Incoherent + IF gives b ≈ 1 ("pure phase space") and is not linear at low E_cm; for E_cm ≥ 35 GeV, b = 1.004 ± 0.023 (p. 626–627, Fig. 4).
- **Robustness of the IF failure** (p. 627): varying the fragmentation-function hardness, transverse momentum, Q₀ and Λ_QCD at fixed ⟨n_ch⟩(91 GeV) never changed b by more than 15 %.
- **Authors' conclusion** (p. 627):
  - The data are consistent with coherence + LPHD.
  - Peak evolution is "accurately predicted" by the analytic formulae.
  - Coherent MCs fit best. Incoherent + string is "somewhat worse". Incoherent + IF is "incompatible with the data".

## Assessment
- The 91 GeV shape alone does not discriminate between models. Incoherent shower + string fits it (Fig. 2), as Dokshitzer et al. had already warned (a cone cut makes a hump without angular ordering; Dokshitzer_1987nm, Eqs. 47–48). The evidential weight therefore rests entirely on the slope b, i.e. one number fitted to five points from two experiments (TASSO + OPAL).
- Our arithmetic from Tab. 4, using quadrature sums of the quoted errors:
  - Coherent Jetset: (0.663 − 0.637)/0.025 ≈ 1.0σ.
  - Ariadne: (0.686 − 0.637)/0.026 ≈ 1.9σ.
  - Incoherent Jetset + string: ≈ 2.75σ, matching the quoted 2.8σ.
  - So coherent and incoherent string models differ by roughly 1σ in data-vs-model tension. Only the IF model is decisively excluded. The authors' remark that string fragmentation "partly incorporates coherence" (p. 627) concedes that the string/no-string comparison is not a clean coherence switch.
- Hadronization contributes. In every MC the hadron-level b exceeds the parton-level b by 0.03–0.07 (Tab. 4), comparable to the coherent/incoherent difference at hadron level (0.03). The MLLA parton slope 0.627 agreeing with the hadron-level 0.637 is therefore partly coincidental within the MC picture. Freezing fragmentation parameters across energies is a strong assumption, and the authors justify it only by the event-shape tune of ref. [9].
- Statistical treatment is limited:
  - Tab. 1 errors are statistical only.
  - The TASSO points' systematics are not discussed.
  - The O(1) uncertainty from the peak-evolution fit (±0.60) is very large. With O(1) dropped, a quite different Λ_eff (≈ 0.35 GeV) also fits (p. 626). The "unambiguous" analytic prediction is thus rather flexible.
  - The rising K(Y) at low energy (Tab. 3) and the χ²/df = 18 for Eq. 4 at 35 GeV are unexplained.
- Comparison with the companion papers:
  - Boudinov:1993mc uses the same Jetset switches (MSTJ(42), MSTJ(46)) and argues that the hadron ξ spectra are insensitive to coherence. Their own quoted JETSET 7.3 slopes (coh 0.67, incoh 0.70, data 0.64 ± 0.02) echo the ≈ 1σ separation noted above.
  - OPAL:1992lzb finds a more discriminating observable (azimuthal correlations), where incoherent + string fails at 3.7–4.4σ.
  - Khoze_1996dn (p. 42) later concedes the ξ shape is not by itself evidence for coherence within MC models.

## Leads
- Yu.L. Dokshitzer, S.I. Troyan, Leningrad preprint LNPI-922 (1984): the original MLLA spectrum formula (Eq. 1). Theory foundation for RQ 2.
- C.P. Fong, B.R. Webber, Phys. Lett. B 229 (1989) 289: higher-moment (distorted-Gaussian) MLLA spectrum used in Eqs. 4–5, and later the standard fit form for ξ*.
- Ya.I. Azimov, Yu.L. Dokshitzer, V.A. Khoze, S.I. Troyan, Z. Phys. C 27 (1985) 65 (LPHD) and Z. Phys. C 31 (1986) 213 (particle-type dependence of spectra; resonance "duality" quote used by Boudinov).
- Yu.L. Dokshitzer, V.A. Khoze, G. Marchesini, B.R. Webber, CERN-TH-5738/90 (1990): cited for the peak-position formula (Eq. 3). Possibly the paper published as Phys. Lett. B 245 (1990) 243 (the EMMC proposal used in OPAL:1992lzb); this identification is not verified.
- TASSO, W. Braunschweig et al., DESY 90-013 = Z. Phys. C 47 (1990) 187: the 14–44 GeV spectra that supply 4 of the 5 points in the slope fit.
- OPAL, M.Z. Akrawy et al., Z. Phys. C 47 (1990) 505 (CERN-EP/90-48): the MC tune that fixes all fragmentation parameters here.
- P. Mättig, Phys. Rep. 177 (1989) 141: review of pre-LEP multiplicity/spectrum tests of coherence, a likely good map of the PETRA/PEP era.
- Forward: later LEP/LEP2 and HERA ξ* vs √s measurements and combined fits (e.g. with Q₀ → hadron mass in the "limiting spectrum"). Use `citing 297564`.
