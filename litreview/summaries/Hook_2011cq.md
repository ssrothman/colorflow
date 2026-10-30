# Jet Dipolarity: Top Tagging with Color Flow
- **ID / links:** Hook:2011cq · INSPIRE 888828 · arXiv 1102.1012 · DOI 10.1007/JHEP04(2012)007
- **Authors / collab, year, journal:** A. Hook, M. Jankowiak, J. G. Wacker, 2012 (arXiv Feb 2011), JHEP 04 (2012) 007 (SLAC-PUB-14369)
- **Type:** phenomenology
- **Relevance:** 2 · RQs: 1a, 1c, 2, 4
- **Full text source:** arxiv

## Takeaways
- Introduces **dipolarity** D = (1/R₁₂²) Σ_{i∈J} (p_Ti/p_TJ) R_i² (Eq. 1). Here R_i is the η–φ distance of cell i from the *line segment* joining the two subjet centres. D is small when radiation lies between the subjets, as expected for a colour singlet (W→qq̄), and large when it lies elsewhere. It is a two-subjet, colour-flow observable that avoids the per-subjet axis noise of pull (p. 2).
- Motivation: the eikonal antenna pattern for a colour-singlet dipole (Eq. 2) vs partons colour-connected to the beam (Eq. 3, Fig. 2). In QCD fakes, the large-N_c colour configurations have the wrong dipole topology, and only one is top-like, suppressed by C_A/C_F (Fig. 3).
- Added to the HEPTopTagger, dipolarity cuts reduce the QCD mistag at fixed S = 20% by up to ~50% (Herwig) or ~30% (Pythia) for 350 ≲ p_T ≲ 800 GeV (Fig. 5, p. 6). The gain is concentrated at low signal efficiency, S ≲ 35% (Fig. 6).
- Strong MC dependence: the Herwig 6 (angular-ordered) vs Pythia 6 difference is attributed to the parton shower, not UE (UE-off test, p. 6). This identifies dipolarity as a probe of shower coherence modelling that needs data validation (RQ4).

## Setup
- LHC √s = 7 TeV BOOST2010 benchmark samples: SM hadronic tt̄ (signal: hardest jet, |η| < 2.5) vs QCD dijets (background: hardest jet) (p. 5).
- Generators: Herwig 6.510 + Jimmy (UE tune of ref. [33]); Pythia 6.4 Q²-ordered with the DW tune; Pythia 6.4 pT-ordered with the Perugia tune (p. 5).
- Detector emulation: 0.1×0.1 η–φ cells as massless pseudoparticles. C/A clustering with FastJet 2.4.2, fat jets R = 1.5. A 1 GeV cell threshold gives "only a mild degradation" (p. 5). No pileup samples.
- HEPTopTagger steps 1–5 (mass-drop with m_j1 < 0.8 m_j, 30 GeV stop; filtering; three-subjet mass cuts i–iii′; p_T > 200 GeV) (p. 3–4). The W candidate is the subjet pair that passes the mass cut; if several pass, the one with the smaller D is used (p. 4). An additional m_filt window is applied, to check orthogonality to kinematic cuts (p. 4).
- Radiation entering D: the two hard W subjets plus all soft radiation (including what was removed by filtering) in cones of radius ΔR/√2 around each W subjet, excluding the smallest cone containing the b subjet (p. 5, Fig. 1). The authors stress that this choice strongly affects performance (p. 4).
- Cuts are optimised by a scan over R_min (70–98% m_W/m_t), m_t window, D_max, l_cut and b_cut at each signal efficiency (p. 5).

## Results
- Eikonal estimate gives D_ns ≈ 2 D_s, but Eqs. 2–3 do not quantitatively match MC (p. 2–3).
- D for reconstructed W's decreases with p_T for both samples. Background central values are O(50–100%) larger than signal, with broad overlapping 10–90% bands (e.g. at 250 GeV, signal median ≈ 0.024 vs background ≈ 0.038; read from Fig. 4, Herwig).
- At S = 20%, the mistag rate with vs without dipolarity is about 0.4% vs 0.7% at 500 GeV and ≈0.6% vs ≈1.0% at 750 GeV for Herwig (read from Fig. 5 top). Pythia DW/Perugia improvements are smaller (Fig. 5 bottom), giving the quoted ~50% vs ~30% (p. 6).
- Optimised working points at S = 20% (equal admixture of the three samples), with B for Herwig / Pythia DW / Pythia Perugia (Tab. I):
  - Low p_T (200–500 GeV): 0.47 / 0.48 / 0.41% without D, 0.41 / 0.38 / 0.30% with D (D_max = 0.021).
  - High p_T (400–800 GeV): 0.92 / 0.79 / 0.59% without D, 0.58 / 0.58 / 0.39% with D (D_max = 0.023).
  - Including D loosens the optimal mass cuts (Tab. I caption).
- For p_T ∈ [400, 500] GeV (Herwig), the ROC curves with and without D merge above S ≈ 35%. Below that, background rejection improves sizeably, e.g. ≈0.15% vs ≈0.35% at S = 15% (read from Fig. 6; relative statistical error ≈25% at the lowest mistag).
- Turning UE off lowers the mistag rate only somewhat and similarly for Herwig and Pythia. So the generator difference "most likely arises from the parton shower" (p. 6). The authors suspect that Herwig's angular ordering models coherence better than Pythia's Q²/p_T ordering with angular vetoes (p. 6).
- Suggested extensions: heavy colour-singlet resonances → tt̄, W/Z→qq̄, heavy singlets → WW/ZZ, SUSY cascades, RPV LSP decays with exotic colour structure, and refining D toward the exact singlet radiation pattern (p. 6–7).

## Assessment
- Conceptually a useful bridge between pull (Gallicchio:2010sw) and antenna-pattern reasoning: it encodes the colour-singlet dipole pattern directly. But the observable is ad hoc (the R² weighting is not derived from Eq. 2), and the authors admit the eikonal estimate fails quantitatively.
- The modest absolute gains (≈0.1–0.3 percentage points of mistag at S = 20%) have large statistical errors (Fig. 5 bands, Fig. 6 note). The generator spread is comparable to the effect, so the main physics output is the demonstration that colour-flow-based taggers depend on shower coherence modelling, which makes them a lever for testing that modelling.
- All results are leading-colour showers from 2006-era generators (Herwig 6, Pythia 6), with no pileup, no detector smearing beyond cells, and no subleading-colour or colour-reconnection variation. With a 1.5-radius fat jet, pileup sensitivity of a soft-radiation, R²-weighted observable is a major unaddressed caveat (the authors note pileup/UE would hurt at low p_T, p. 3). Effects of non-global logarithms are acknowledged only in passing (ref. [40], p. 6).
- Relevance 2 rather than 3: it is primarily a tagging study, with a colour-flow test proposal (RQ4) only implicit. Measuring D on hadronic W's in tt̄ data would be a coherence test complementary to pull.

## Leads
- Plehn, Salam, Spannowsky 2010 (PRL 104 111801), and Plehn, Spannowsky, Takeuchi, Zerwas 2010 (JHEP 1010 078). The HEPTopTagger, context only (relevance 1).
- Larkoski & Peskin 2010, PRD 81 054010 (arXiv:0908.2450). Antenna-pattern calculation of radiation for different colour configurations, suggested as the improved estimate of D (ref. [28]).
- D0 2011, arXiv:1101.0648 (PRD 83 092002). The tt̄ W colour-flow (pull) measurement cited as data–theory agreement (ref. [38]).
- CDF 1994, PRD 50 5562; D0 1997, PLB 414 419 (hep-ex/9706012); Varelas hep-ex/9809019. Tevatron colour-coherence (third-jet) studies where Herwig beat Pythia (ref. [37]). Check whether these are already in the DB (CDF_1994zkl is).
- Black, Gallicchio, Huth, Kagan, Schwartz, Tweedie 2010, arXiv:1010.3698. Pull in particle searches (ref. [27]).
- Rainwater, Szalapski, Zeppenfeld 1996, PRD 54 6680 (hep-ph/9605444), and Barger, Phillips, Zeppenfeld 1995, PLB 346 106 (hep-ph/9412276). Colour-singlet-exchange rapidity-gap / mini-jet veto, a seed topic.
- Dasgupta 2004, Pramana 62 675 (hep-ph/0304086). Non-global logs in radiation patterns, a theory caveat for colour-flow observables.
