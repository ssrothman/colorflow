# A model independent observation of the string effect using quark tagging at LEP
- **ID / links:** OPAL:1991xwi · INSPIRE 314333 · arXiv — · DOI 10.1016/0370-2693(91)90337-P
- **Authors / collab, year, journal:** OPAL Collaboration (M.Z. Akrawy et al.), 1991, Phys. Lett. B 261 (1991) 334–346
- **Type:** experimental
- **Relevance:** 3 · RQs: 1b, 2, 3
- **Full text source:** zotero

## Takeaways
- This is the first string-effect measurement in which the gluon jet is identified by lepton (b/c semileptonic) tagging of the quark jets rather than by energy ordering. That lets OPAL select events where the q–g and q–q̄ inter-jet regions are geometrically equivalent (ψ_A ≈ ψ_C), or the same geometry with the g and q̄ swapped. The comparison therefore needs neither an independent-fragmentation reference nor a qq̄γ reference sample (p. 336–337).
- In all 6 independent inter-jet regions the particle density between the quark and gluon jets is larger than between the quark and antiquark jets. The combined ratio is R̃ = 1.62 ± 0.07 (all particles, 8.9σ from 1, statistical errors only), 1.66 ± 0.09 (charged only, 7.3σ) and 1.68 ± 0.09 (energy flow, 7.6σ) (Tab. 3, Tab. 4).
- Jetset 7.2 (coherent parton shower + Lund string) reproduces the effect: R̃ = 1.67 ± 0.07 at detector level (Tab. 4) and 1.54 ± 0.02 at generator level (p. 344). Cojets 6.12 (incoherent shower + independent fragmentation) gives R̃ = 1.02 ± 0.01. It stays at about 1.03–1.04 even with extreme suppression of large-angle soft hadrons, and the IF options in Jetset also give R̃ ≈ 1 (p. 344).
- This rebuts Ballocchi–Odorico (Nucl. Phys. B345 (1990) 173), who argued that the earlier string-effect observations came purely from the geometric asymmetry of energy-ordered events. The authors conclude the asymmetry is dynamical and tied to the different colour charges of quarks and gluons (p. 344). They explicitly do not distinguish perturbative coherence (with LPHD), the Lund string, or q/g fragmentation differences (p. 336, p. 345–346).
- MC study: the asymmetry is flavour-independent (dd̄ vs bb̄ consistent), so the heavy-flavour-enriched tagged sample does not bias the result (p. 345). Footnote 5 notes that perturbative QCD also predicts no light/heavy difference for these configurations (Khoze, ref. [23]).

## Setup
- LEP1, OPAL, √s = 88.3–95.0 GeV (mean 91.3 GeV). 140 189 multihadron events, 116 953 after containment cuts, ≈ 6.5 pb⁻¹ (p. 337–338, Tab. 1).
- 3-jet selection: modified JADE (P-scheme) invariant-mass algorithm with y_cut = 0.03. Requirements: angle sum > 358° (planarity); each jet ≥ 3 particles, E_vis > 5 GeV and polar angle > 30°; jet energies computed from the inter-jet angles, with a consistency cut (Eq. 1). This leaves 22 721 3-jet events (p. 338, Tab. 1). Jet resolutions (Jetset + detector sim): energy 8.1 / 11.4 / 22.1 %, angle 2.6° / 3.9° / 10.6° for the highest / middle / lowest energy jet (p. 338).
- Lepton tagging: μ with p > 3 GeV or e with p > 2 GeV (p. 339–340).
  - Single tag: the lepton is in one of the two lower-energy jets; the highest-energy jet is taken as a quark and the lepton jet as the other quark. The energy difference between the highest-energy jet and the gluon-tagged (untagged) jet must exceed 8 GeV. 1311 events (933 μ, 378 e).
  - Double tag: the two lepton jets are the quarks. 258 events (Tab. 1).
  - Purities from Jetset: single tag 96 ± 1 % (q1) / 88 ± 1 % (q2) / 84 ± 1 % (g); double tag 96 / 87 / 84 % (p. 340).
  - Flavour content of the single-tag sample: ≈ 47 % b, 20 % c (p. 340).
- Event configurations, using the angles in the event plane (ψ_A = q1–g sector, ψ_C = q1–q2 sector) (p. 341–342, Tab. 2):
  - Symmetric: (I) ψ_A = ψ_C = 150 ± 10°, 188 events; (II) 130 ± 10°, 36 events.
  - Transposed pairs, in which g and the lower-energy quark swap direction and energy: (IIIa/IIIb) ψ = 150°/130° and 130°/150°, 34/169 events; (IVa/IVb) 170°/150° and 150°/170°, 55/210 events.
  - In total 692 events, with gluon purity between 49 % (IVa) and 87 % (IIIb) (Tab. 2).
- Observable: the detector-level particle flow (1/N) dn/dψ in the event plane, uncorrected (Fig. 2, Fig. 3).
  - R is the ratio of the flow integrated over the central 25–75 % of the q–g sector to the same integral over the corresponding q–q̄ sector (p. 341).
  - The combined R̃ uses the normalized angle ψ̃ = ψ/ψ_A or ψ/ψ_C, integrated over 0.25–0.75 and summed over the 6 regions (Eq. 2).
  - Charged-only and energy-flow versions are also given.
- Models compared: Jetset 7.2 (parton shower + string, tuned to OPAL event shapes, full detector simulation); Cojets 6.12 (incoherent shower + independent fragmentation, with gluon fragmentation the same as for light quarks; tuning provided by Odorico); the independent-fragmentation options in Jetset (p. 343–344).

## Results
- Symmetric configurations: the q–g region has more particles than the q–q̄ region, by 3.3σ in each case. R = 1.40 ± 0.12 (I) and 2.46 ± 0.44 (II) (Fig. 2, p. 341, Tab. 3).
- Transposed configurations. Small-angle regions: R = 1.86 ± 0.29 (III, 3.0σ) and 1.22 ± 0.15 (IV, 1.5σ). Large-angle regions: R = 1.56 ± 0.21 (III, 2.7σ) and 1.53 ± 0.21 (IV, 2.5σ) (Fig. 3, Tab. 3, p. 343).
- All 6 regions give R > 1. Charged-only R ranges from 1.21 to 2.42 and energy-flow R from 1.25 to 2.56 (Tab. 3).
- Combined: R̃ = 1.62 ± 0.07 (8.9σ); charged 1.66 ± 0.09 (7.3σ); energy flow 1.68 ± 0.09 (7.6σ) (Tab. 4). Errors are statistical only, and no systematic uncertainty is quoted anywhere.
- Jetset 7.2 at detector level: R̃ = 1.67 ± 0.07 / 1.65 ± 0.08 / 1.78 ± 0.09 for all / charged / energy flow, in good agreement with data (Tab. 4). At generator level with perfect q/g identification, R̃ = 1.54 ± 0.02 (p. 344).
- Cojets 6.12 at generator level gives R̃ = 1.02 ± 0.01.
  - Raising the large-angle soft-hadron suppression (FRALOG(6), FRALOQ(6) from 0 to 1) gives R̃ = 1.03 ± 0.01. The event-shape χ² rises from 129 to 571 for 110 bins (footnote 3, p. 344).
  - An extreme setting (both parameters = 2) gives R̃ = 1.04 ± 0.01 with χ² = 1358 (footnote 4, p. 344).
  - The IF models in Jetset could not produce an R̃ substantially different from 1 for any parameter set tried (p. 344).
- The authors note Cojets *might* describe the data if q/g fragmentation differences were allowed, but they did not test this (p. 344).
- Flavour dependence (Jetset): dd̄ and bb̄ events give the same R within statistics in all 6 regions. A normal flavour mix with the measured purities gives R(I) = 1.36 ± 0.03, consistent with data (p. 345).
- Systematic check: requiring a p > 3 GeV/c track in the gluon jet gives consistent asymmetries (p. 342).
- Authors' interpretation: dynamical differences exist between quarks and gluons, or between q–g and q–q̄ systems. These could be explained by:
  - perturbative coherence with LPHD (Azimov et al. 1985, ref. [5]; the paper does not use the later "drag" terminology);
  - string fragmentation;
  - possibly differences between quark and gluon jet fragmentation.

  They use "string effect" purely as the name of the observed asymmetry (p. 336, p. 345–346).

## Assessment
- This is the cleanest early refutation of the "purely kinematic / energy-ordering artefact" explanation of the string effect. Geometric symmetry within each event removes the main loophole of the JADE/TPC/TASSO/MARK II analyses. The statistics are small (692 events), but the combined significance is robust.
- The paper does **not** separate the perturbative (antenna/coherence, drag) explanation from the non-perturbative (Lund string boost) one. Both give an excess in the q–g sector, and Jetset contains both. The 8.9σ result therefore rules out *incoherent* shower + flavour-blind independent fragmentation, not a particular hadronization model. The perturbative prediction (Azimov–Dokshitzer–Khoze–Troyan, ref. [5]) is discussed qualitatively but never compared numerically. For RQ2, later analyses are needed: ones that compare to analytic LO/MLLA inter-jet particle-flow ratios, or that compare the string effect against cluster (HERWIG) and dipole (ARIADNE) models. No cluster model is compared here.
- The loophole left open is q/g fragmentation differences in IF. The authors acknowledge it (p. 344), but no quantitative check was done. Gluon-jet softness could raise particle density near the gluon, partly inside the 25–75 % window, especially given angular resolution and smearing (lowest-energy jet resolution ≈ 10.6°).
- Statistical errors only; there are no systematic uncertainties, no unfolding, and no correction for gluon impurity (as low as 49–68 % in some samples). Impurity dilutes R toward 1, so the true asymmetry is if anything larger. The flow distributions are uncorrected, so the R values cannot be compared directly with other experiments' numbers or with analytic calculations.
- The sample is heavy-flavour enriched (≈ 47–70 % b). Dead-cone and B-decay effects could in principle change inter-jet populations. The MC dd̄/bb̄ check is reassuring but model-dependent.
- The method (heavy-quark tagging to identify gluon jets, geometrically symmetric "Y"-shaped configurations, e.g. 150°/150°/60°, not Mercedes) became the template for later OPAL q/g-jet and string-effect studies at LEP [unverified: not stated in this paper; it only claims to be the first analysis to use lepton tagging for q/g separation, p. 345]. It is useful context for RQ1b (inter-jet coherence) and for RQ4-style "clean" tests of colour-flow topology.

## Leads
- Azimov, Dokshitzer, Khoze, Troyan, Phys. Lett. B165 (1985) 147: perturbative (coherence/drag) prediction of the string effect via LPHD; core theory for RQ1b/RQ2.
- Ballocchi & Odorico, Nucl. Phys. B345 (1990) 173: claims the string effect is a geometric artefact reproducible by IF (Cojets); the counter-position this paper tests.
- Andersson, Gustafson, Sjöstrand, Phys. Lett. B94 (1980) 211: original Lund string-effect prediction.
- JADE Collab., Bartel et al., Phys. Lett. B101 (1981) 129 and Z. Phys. C21 (1983) 37: first observation of the string effect.
- TPC/2γ Collab., Aihara et al., Phys. Rev. Lett. 54 (1985) 270 and 57 (1986) 945, Z. Phys. C28 (1985) 31: qq̄g vs. qq̄γ comparison.
- MARK II Collab., Sheldon et al., Phys. Rev. Lett. 57 (1986) 1398 and TASSO Collab., Althoff et al., Z. Phys. C29 (1985) 29: early PEP/PETRA string-effect measurements.
- V.A. Khoze, Proc. Lepton-Photon 1989 (Stanford): perturbative-QCD inter-jet predictions, including flavour (in)dependence.
- Nilles & Streng, Phys. Rev. D23 (1981) 1944: proposal to use heavy-quark leptons to separate quark and gluon jets.

## Verification
Checked 2026-10-30 by an independent reader: 62 claims checked, 4 corrected, 1 unverifiable.
- Single-tag 8 GeV cut: it is on the energy difference between the highest-energy jet and the gluon-tagged jet, not "the other jets" (p. 339).
- "Mercedes" configurations removed: the symmetric configurations are Y-shaped (ψ_A = ψ_C ≈ 150° or 130°), not 120°-symmetric (p. 340–341, Tab. 2).
- Page anchor for the "different colour charges" conclusion corrected to p. 344.
- "Drag" is a reviewer gloss: the paper only cites Azimov et al. [5] for perturbative coherence (p. 345–346).
- Claim that the method became the template for later OPAL studies is marked [unverified] (outside this paper).
