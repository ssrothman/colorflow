# Colour reconnection and its effects on precise measurements at the LHC
- **ID / links:** Sjostrand:2013cya · INSPIRE 1262718 · arXiv 1310.8073 · DOI —
- **Authors / collab, year, journal:** T. Sjöstrand (Lund), 2013, proceedings of ISMD13 (Chicago, Sept. 2013), LU TP 13-37 / MCnet-13-16
- **Type:** review
- **Relevance:** 2 · RQs: 1, 2, 3, 4
- **Full text source:** arxiv

## Takeaways
- Short (6-page text) status review of colour reconnection (CR). It explains why CR is expected at the LHC: about 10 strings cross y = 0 in a typical event, mostly from MPI. Strings are about as wide as hadrons and are produced inside the pp overlap region, so they overlap in space-time. With N_C = 3, it is also ambiguous which partons form singlets (p. 2).
- The key LHC evidence is the rise of ⟨p⊥⟩(n_ch). Pythia 8 Tune 4C with CR fits ATLAS 7 TeV data, but with CR switched off the curve flattens far below the data (Fig. 1). The author says the near-perfect agreement is "fortuitous" and worse for other selections (p. 5).
- LEP2 W⁺W⁻ was not conclusive. Perturbative CR gives ⟨δM_W⟩ ≤ 5 MeV. Aggressive non-perturbative models were ruled out. Conservative SK-type models were "not favoured" but survive at about 40 MeV. Bose–Einstein effects give about 40 MeV (up to 100 MeV) and are disfavoured but not excluded (p. 3).
- Top mass: Pythia 6.4 Tevatron studies gave a total MC-model uncertainty approaching 1 GeV, of which up to 0.5 GeV is CR-related. In Pythia 8.1, switching CR on/off shifts m_t by about 0.15 GeV, with no strong dependence on obvious kinematic variables (pp. 5–6).
- CR in pp can mimic heavy-ion-like flow through boosted string pieces (mass-dependent p⊥), referring to Ortiz et al. 2013 (p. 6).

## Setup
Conference review with one figure: ⟨p⊥⟩ vs N_ch (N_ch > 1, p⊥ > 0.5 GeV) at 7 TeV, ATLAS data vs Pythia 8.175 Tune 4C with and without CR, from MCPLOTS/Rivet (Fig. 1). The paper surveys earlier CR literature:
- colour-octet J/ψ and B → J/ψ (p. 2);
- ⟨p⊥⟩(n_ch) from UA1 (p. 2);
- LEP2 SK-I/SK-II models and BE effects (p. 3);
- soft colour interactions and rapidity gaps at HERA (p. 3);
- CR models in Pythia 6.4, Pythia 8.1, Herwig++ and Sherpa (p. 5);
- top-mass systematics (pp. 5–6).

## Results
- **Physical picture.** CR is the non-linear interaction of many colour charges at high density (p. 2). The alternatives are colour ropes or a QGP, which modify hadronisation itself. CR is the "less dramatic" option: it only reassigns colours among partons and leaves hadronisation unchanged (p. 2).
- **λ measure.** Reconnections tend to reduce the total string length λ ≈ Σ ln(m_ij²/m_0²), with m_0 ≈ 1 GeV (Eq. 1).
- **Why ⟨p⊥⟩(n_ch) needs CR.** If MPIs hadronise independently, ⟨p⊥⟩ should not depend on n_MPI and hence on n_ch. With CR, each additional MPI adds fewer particles but the same p⊥ kick, so ⟨p⊥⟩ rises (p. 2).
- **Low n_ch.** Other effects drive the rise at low n_ch. The absolute ⟨p⊥⟩ normalisation there comes from e⁺e⁻ hadronisation tunes, which supports beam-remnant hadronisation being "jet-like" at low string density (p. 3).
- **LEP2.** The SK models are space-time based. SK-I (Type-I superconductor) treats strings as bags, with reconnection probability set by their space-time overlap. SK-II (Type-II) treats strings as vortex lines that reconnect only where their cores cross. Both can favour reconnections that reduce λ (p. 3). Numbers on δM_W are listed under Takeaways (p. 3).
- **Future e⁺e⁻ tests.** A Higgs factory would provide a much larger WW sample. The energy and angular-orientation dependence of any CR effect could then discriminate between models (p. 3, p. 6).
- **Diffraction.** HERA diffractive DIS can be interpreted as CR (soft colour interactions; Buchmüller–Hebecker, Edin–Ingelman–Rathsman) or as Pomeron exchange (Ingelman–Schlein). Both describe the data comparably (p. 3). The author speculates that gaps between high-p⊥ jets are dominated by CR, while low-mass diffraction is more naturally described by Pomerons (p. 4).
- **Beam remnants.** In the N_C → ∞ limit, every MPI adds string endpoints to the remnant. With N_C = 3, colour correlations between MPIs reduce the remnant charge and give a rising ⟨p⊥⟩(n_ch), "but nowhere near enough", so CR is still required (p. 4).
- **Pythia 6.4 models.** About a dozen CR scenarios minimise λ, or Σm² in the generalised area law (GAL), using simulated annealing (p. 5):
  - P_rec = 1 − (1−χ)^n_MPI, with a free strength parameter χ;
  - string pieces are chosen as reconnection candidates with probability P_rec;
  - annealing then minimises λ.
- **Pythia 8.1 model.** A single CR model: all or none of a lower-p⊥ MPI's partons are attached to a higher-p⊥ system to keep λ minimal. Low-p⊥ MPIs in busy events reconnect more often (p. 5).
- **Other generators.**
  - Herwig++ CR (Gieseke–Röhr–Siodmok 2012) uses annealing on Σ m²_cluster. It is needed for ⟨p⊥⟩(n_ch) and also for dn_ch/dη (p. 5).
  - Sherpa has a Pythia-like MPI model without CR and fails ⟨p⊥⟩(n_ch). A new KMRZ-based model is in preparation (p. 5).
- **Top mass.**
  - Generator mass definitions are ambiguous relative to MS-bar (p. 5).
  - t, W and Z decay at cτ ≈ 0.1 fm, inside the shower/hadronisation region. The b is necessarily colour-connected elsewhere, and the W → ud̄ system may not stay a singlet (p. 5).
  - The numbers (about 1 GeV total from Pythia 6.4 tunes, up to 0.5 GeV from CR, about 0.15 GeV CR on/off in Pythia 8.1) are listed under Takeaways (pp. 5–6). Tevatron/LHC statistical errors are about 0.5 GeV, with total systematics below 1 GeV (p. 6).
  - CMS has begun studies of m_t vs kinematics (CMS-PAS-TOP-12-029, TOP-13-007), but statistics were still insufficient (p. 6).
- **Proposed tests (RQ4).**
  - Kinematic dependence of the extracted m_t (p. 6).
  - The lepton p⊥ spectrum in t → bℓν as a CR-independent m_t observable (p. 6).
  - Confronting many CR models with a broad range of data to find a pattern (p. 6).
  - Higgs-factory WW (p. 6).
  - Flow-like signatures: boosted strings give larger p⊥ to heavier hadrons (p. 6).
- **Outlook.** CR is "well established", e.g. from B → J/ψ. What is attributed to CR may be a richer mixture of high-density effects (ropes, collective flow). Identified-particle p⊥ spectra are poorly described by Pythia, which hints at a further mechanism (p. 6).

## Assessment
- This is a concise, authoritative snapshot of the 2013 situation from the main author of the Lund/Pythia CR models. It is useful for framing, but the paper contains almost no original results. The only figure is an MC-vs-data comparison taken from MCPLOTS.
- The claim that ⟨p⊥⟩(n_ch) requires CR is model-dependent. It holds within an MPI + independent-string picture, and the author openly says the agreement is partly fortuitous. Hydrodynamics (EPOS) and ropes are named alternatives, and the paper offers no discriminating test beyond hints.
- The 0.15 GeV CR on/off m_t shift (Pythia 8.1) has no figure or table to back it in this paper. It needs to be checked against Argyropoulos & Sjöstrand 2014 (already summarised) and the Skands–Wicke 2007 study.
- The LEP2 statements are qualitative. The quantitative LEP combination (LEP EW WG, Phys. Rept. 532, 2013) should be taken from the primary source.
- The paper anticipates the later Pythia 8 CR development: QCD-based CR (Christiansen–Skands 2015), gluon-move and SK models in pp (Argyropoulos–Sjöstrand 2014).

## Leads
- Sjöstrand & van Zijl, Phys. Rev. D36 (1987) 2019: the original MPI model and first CR to explain the UA1 ⟨p⊥⟩(n_ch).
- Sjöstrand & Khoze, Z. Phys. C62 (1994) 281: SK-I/SK-II space-time CR models and the W-mass shift.
- Khoze & Sjöstrand, Eur. Phys. J. direct C2 (2000) 1: CR tests at linear colliders (energy/angular dependence).
- Skands & Wicke, Eur. Phys. J. C52 (2007) 133, and Sandhoff & Skands FERMILAB-CONF-05-518-T: colour annealing and the top-mass CR uncertainty.
- Rathsman, Phys. Lett. B452 (1999) 364: generalised area law.
- Gieseke, Röhr, Siodmok, Eur. Phys. J. C72 (2012) 2225: Herwig++ CR.
- Ortiz Velasquez et al., PRL 111 (2013) 042001: CR producing flow-like patterns in pp.
- Edin, Ingelman, Rathsman, PLB 366 (1996) 371: soft colour interactions and rapidity gaps.
- Eriksson, Ingelman, Rathsman, PRD 79 (2009) 014011: B → J/ψ as evidence for colour rearrangement.
- CMS-PAS-TOP-12-029 / TOP-13-007: early m_t vs kinematics studies.
