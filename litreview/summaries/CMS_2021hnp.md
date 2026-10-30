# Measurements of angular distance and momentum ratio distributions in three-jet and Z + two-jet final states in pp collisions
- **ID / links:** CMS:2021hnp · INSPIRE 1847230 · arXiv 2102.08816 · DOI 10.1140/epjc/s10052-021-09570-2
- **Authors / collab, year, journal:** CMS Collaboration (CMS-SMP-17-008), 2021, Eur. Phys. J. C (2021), DOI above
- **Type:** experimental
- **Relevance:** 2 · RQs: 1d, 1e, 3
- **Full text source:** arxiv (v2; anchors are the preprint's printed page numbers 1–17)

## Takeaways
- Unfolded, normalized distributions of pT3/pT2 and ΔR23 (y–φ distance between jets 2 and 3) in three-jet events at 8 and 13 TeV and in Z(→μμ)+2-jet events at 8 TeV. Events are classified as soft (pT3/pT2 < 0.3) vs hard (> 0.6) and small-angle (ΔR23 < 1.0) vs large-angle (> 1.0) (p. 1–2, Fig. 1). HEPData record: 10.17182/hepdata.106642 (p. 7).
- Three-jet: **no single generator describes both observables** (p. 8):
  - PS-dominated predictions (PYTHIA8 LO 2j+PS, POWHEG NLO 2j+PS) describe soft radiation at all ΔR23 but fail for hard / large-angle radiation, overshooting by up to ≈ 15–25% (Figs. 2–3).
  - MADGRAPH LO 4j+PS describes hard and large-angle radiation but fails in the soft / collinear region by ≈ ±10–20% (Figs. 2–3).
- No significant √s dependence between 8 and 13 TeV (Figs. 4–5, p. 12).
- Z+2j (Z colour-neutral, so coherence is expected to be weaker, p. 2): all generators are "reasonably" good, but all underestimate j3 emission at large pT3/pT2 by ≈ 10–20%, ≈ (read from Figs. 6–7). Switching off the final-state shower in PYTHIA8 destroys the agreement, while switching off MPI has little effect (Figs. 8–9, p. 10).
- Coherence is not isolated directly (no coherence-off variants, no HERWIG). For this review the value is mainly as a 3-jet vs Z+2-jet radiation-pattern benchmark of PS vs ME merging at LHC energies.

## Setup
- 8 TeV (2012, 19.8 fb⁻¹; Z+2j plots labelled 19.7 fb⁻¹) and 13 TeV (2015, 2.3 fb⁻¹, three-jet only). Anti-kT R = 0.5 (8 TeV) and 0.4 (13 TeV), PF jets, CHS pileup mitigation (p. 2–3).
- Three-jet selection (Tab. 1, p. 3–4):
  - pT1 > 510 GeV; HLT thresholds 320 / 450 GeV, unprescaled; all jets pT > 30 GeV; |y1,2| < 2.5.
  - π − 1 < Δφ12 < π; 0.1 < pT3/pT2 < 0.9; R_jet + 0.1 < ΔR23 < 1.5; pTmiss/ΣpT < 0.3.
  - 777 618 (8 TeV) and 613 254 (13 TeV) events.
- Z+2j selection (Tab. 1, p. 3–4):
  - Muons pT > 25 / 5 GeV; 70 < mμμ < 110 GeV; pT,Z > 80 GeV, |yZ| < 2.
  - j2 (leading jet): pT > 80 GeV, |y| < 1; j3: pT > 20 GeV, |y| < 2.4.
  - 2 < |Δφ(Z, j2)| < π; 0.5 < ΔR23 < 1.5; 15 466 events.
  - Here the Z plays the role of "j1".
- Models (Tabs. 2–3, p. 4–6):
  - Three-jet: PYTHIA 8.219 CUETP8M1 (LO 2j+PS); MADGRAPH5_aMC@NLO 5.2.3.3 LO up to 4 partons + PYTHIA8 (kT-MLM, 10 GeV); POWHEG BOX dijet NLO + PYTHIA8 CUETP8M1.
  - Z+2j: PYTHIA8 LO Z+1j+PS; MADGRAPH LO Z+4j + PYTHIA 6.425 Z2Star; SHERPA 1.4.0 LO Z+4j + CSSHOWER++ (AMISIC++); aMC@NLO NLO Z+1j + PYTHIA 8.223.
  - PDF + 7-point scale bands are given only for POWHEG and aMC@NLO (p. 7–8).
- Unfolding to stable-particle level:
  - Three-jet: D'Agostini / RooUnfold with a MADGRAPH response. Z+2j: SVD with a SHERPA response (p. 6).
  - Normalization: three-jet to the integral; Z+2j to the number of inclusive Z+1j events, so it also tests the j3 emission rate (p. 6).
  - tt̄ / diboson background in Z+2j is not subtracted. It raises j3 emission by 2% (soft) to 10% (hard) (p. 6, 10).

## Results
- Systematics (Tab. 4):
  - Three-jet (8 / 13 TeV): JES 0.15 / 0.24%; JER 0.16 / 0.12%; PU 0.1 / 0.17%; unfolding / model 1.1 / 0.25%.
  - Z+2j: JES 5–10%; JER 2–3%; PU 1%; unfolding 1%. JES and JER drop to 0.3–0.5% if Z+2j is normalized to its own integral, except pT3/pT2, which keeps up to 3% (p. 7).
- Three-jet 8 TeV, pT3/pT2, small ΔR23 (Fig. 2 left). All models show "significant deviations" (p. 8). Values ≈ (read from Fig. 2):
  - Lowest bin (0.1–0.2): PYTHIA ≈ 0.9, MADGRAPH ≈ 1.08, POWHEG ≈ 0.85.
  - Highest bins (pT3/pT2 > 0.6): PYTHIA / POWHEG ≈ 1.12–1.15, MADGRAPH ≈ 0.88.
- Three-jet 8 TeV, pT3/pT2, large ΔR23 (Fig. 2 right): MADGRAPH LO 4j+PS ≈ 1.0 throughout. PYTHIA and POWHEG ≈ 0.9 at low and ≈ 1.15–1.18 at high pT3/pT2, ≈ (read from Fig. 2).
- Three-jet 8 TeV, ΔR23 in the soft region (Fig. 3 left): PYTHIA and POWHEG describe the data. MADGRAPH ≈ 1.2 at ΔR23 ≈ 0.7 and ≈ 0.9 at ΔR23 ≈ 1.4, ≈ (read from Fig. 3).
- Three-jet 8 TeV, ΔR23 in the hard region (Fig. 3 right): PYTHIA LO 2j+PS goes from ≈ 0.9 at ΔR23 ≈ 0.7 to ≈ 1.25 at ΔR23 ≈ 1.45, ≈ (read from Fig. 3). POWHEG and MADGRAPH agree. The authors conclude that higher-multiplicity ME is needed here (p. 8).
- 13 TeV: same pattern (Figs. 4–5). No significant √s dependence (p. 12).
- Z+2j pT3/pT2 (Fig. 6): all models agree within uncertainties except in the hard region.
- Z+2j ΔR23 (Fig. 7):
  - Hard region: all models ≈ 0.8–0.9 of data, ≈ (read from Fig. 7 right), i.e. they underestimate j3 emission (p. 9).
  - aMC@NLO NLO Z+1j deviates at large ΔR23 and small pT3/pT2: ≈ 0.7, ≈ (read from Fig. 7 left).
- PYTHIA8 component switches in Z+2j (Figs. 8–9):
  - No MPI: almost unchanged.
  - No MPI + no FSR: collapses to ≈ 0.3–0.5 of data, ≈ (read from Fig. 8). Without FSR, the remaining ISR jets cluster at small ΔR23 (p. 10).
- Authors' summary (p. 11–13): three-jet data are less consistent with theory than Z+2j. Possible reasons are the much larger pT range (pT1 > 510 vs > 80 GeV) and the different initial-state flavour composition. ME+PS merging "is not yet optimal" over the full phase space.

## Assessment
- These are high-statistics, precisely unfolded data with sub-% three-jet systematics. The deviations of ≈ 10–25% are therefore very significant, but the paper gives no χ² values.
- Relevance to coherence is indirect:
  - ΔR23 is a radial distance. It integrates over the azimuthal orientation β, which carries the initial–final interference pattern (CMS:2013cvx, D0:1997tye).
  - The 3-jet vs Z+2j contrast is motivated by colour (p. 2), but kinematics (pT range, quark/gluon fractions) differ too much to attribute differences to colour flow.
  - No HERWIG (angular-ordered) and no coherence-off variant was tested. That is a missed opportunity, since CMS:2013cvx found HERWIG++ best for β centrally.
- The physics conclusion concerns ME+PS matching (LO 4j vs 2j+PS), not coherence per se. It is still useful for RQ1d/1e as an LHC-era benchmark showing that wide-angle hard emission needs ME, while soft / collinear emission favours PS.
- Caveats:
  - The Z+2j comparison mixes generator families: the MADGRAPH sample uses PYTHIA6 Z2Star, not PYTHIA8.
  - The Z+2j background is not subtracted, and its 2–10% effect is comparable to the observed deficit.
  - The three-jet unfolding / model uncertainty at 8 TeV (1.1%) is MC-statistics driven (p. 7).
- HEPData exists (p. 7, ref. 48). A Rivet analysis is not stated in the paper; check for CMS_2021_I1847230.

## Leads
- Catani, Krauss, Kuhn & Webber 2001, JHEP 11, 063 (CKKW ME+PS merging): the theoretical basis for the PS-vs-ME split this paper tests.
- Alwall et al. 2008, EPJC 53, 473 (comparative study of ME+PS merging algorithms): relevant to the MLM/CKKW differences behind the 4j+PS behaviour.
- Mrenna & Richardson 2004, JHEP 05, 040 (matching ME and PS with HERWIG and PYTHIA): also cited by CMS:2013cvx.
- Buckley et al. 2011, Phys. Rept. 504, 145 (general-purpose event generators review): reference for coherence and shower-ordering implementations.
- Forward citations of this paper: generator studies (e.g. Herwig 7 / dipole / antenna / PanScales showers) that use the HEPData record for wide-angle soft radiation.
