# Experimental Study of Jets in Electron-Positron Annihilation
- **ID / links:** JADE:1981ofk · INSPIRE 164399 · arXiv — · DOI 10.1016/0370-2693(81)90505-0 (preprint DESY 81-009, Feb 1981)
- **Authors / collab, year, journal:** JADE Collaboration, W. Bartel et al., 1981, Phys. Lett. B 101 (1981) 129
- **Type:** experimental
- **Relevance:** 3 · RQs: 1b, 2, 3
- **Full text source:** inspire-doc (scanned DESY preprint, no text layer; read from page images)

Page anchors (p. N) use the preprint's own page numbers ("- N -"); PDF page = N + 4. Figures are on PDF pp. 14–16 (Figs. 1–3); Table 1 is on preprint p. 7 (= PDF p. 11).

## Takeaways
- First experimental observation of the **string effect** (the "first" is historical context, not a claim made in the paper): in planar 3-jet e⁺e⁻ events at √s = 30–36 GeV, the particle density in the angular region between the two (most likely) quark jets is depleted relative to the regions next to the (most likely) gluon jet (Fig. 3a, Tab. 1).
- Asymmetry measured as the ratio of particle counts in the central angular range 0.3 ≤ θ/θ_ik ≤ 0.7 of region (#3–#1) to region (#1–#2): data 1.35 ± 0.09, Lund string 1.34 ± 0.06, independent fragmentation (Hoyer et al.) 1.08 ± 0.04 (Tab. 1).
- The asymmetry grows with m² + p_out² (p_out > 0.2 GeV: 1.6 ± 0.2; kaons: 2.2 ± 0.7), as expected for a Lorentz-boost (string) origin, and again follows Lund rather than independent fragmentation (Tab. 1, p. 5).
- Authors' conclusion: fragmentation along colour–anticolour axes (via the gluon) describes data better than fragmentation along parton directions; gluons "fragment" differently from quarks (p. 5).
- Interpreted in 1981 purely as a hadronization (string vs independent) discriminant; the later perturbative "drag"/coherence interpretation (radiation antenna patterns) is not discussed here.

## Setup
- PETRA, JADE detector, √s = 30–36 GeV; 2892 multihadron events (p. 1). Charged particles p > 100 MeV and neutral (lead-glass) p > 150 MeV used (p. 3).
- Models (both with first-order QCD matrix element, α_s with Λ = 0.3 GeV, n_f = 5, qq̄/qq̄g split at a phase-space boundary; p. 1, p. 6 footnote *):
  - **Hoyer et al.** (NPB 161 (1979) 349): independent Field–Feynman fragmentation of q, q̄, g along parton directions; the gluon is a qq̄ pair with all momentum on one quark (a = 1) (p. 1–2).
  - **Lund** (Andersson, Gustafson, Sjöstrand PLB 94B (1980) 211): string stretched q–g–q̄; gluon kinematically treated as collinear q′q̄′ sharing momentum equally, each half forming a two-jet system with q or q̄ boosted into the overall c.m. (p. 2, Fig. 1a,b).
  - Shared fragmentation parameters taken from a fit of the **Hoyer** model to the 30 GeV data (≈50% of the sample): f(z) = 1 − a + 3a(1−z)², a = 0.5 for u,d,s; u:d:s = 2:2:1; 50% pseudoscalars; σ_q = 0.33 GeV (p. 2, p. 6). Full detector simulation incl. ISR (p. 2).
  - qq̄g fraction differs: 26% (Hoyer) vs 52% (Lund) (p. 6 footnote **).
- Observables:
  1. Momentum-weighted Σ_∥^(n) = Σ|p_i|ⁿ|cos χ_i| / Σ|p_i|ⁿ (n = 0,1,2), χ = angle to sphericity axis (p. 3, Fig. 2).
  2. String-effect observable: 3-jet selection with planarity Q₂ − Q₁ ≥ 0.07, aplanarity Q₁ ≤ 0.06 → 484 planar events; triplicity jet finding, each jet ≥ 4 particles and ≥ 2 GeV → 326 events (p. 4). Jets ordered by the opposite projected inter-jet angles θ₁₂ ≥ θ₃₁ ≥ θ₂₃ (Fig. 1c), so jet #3 (opposite the smallest angle θ₂₃; by 3-body kinematics the lowest-energy jet — our inference, the paper does not say "energy") is the gluon candidate and region #1–#2 the qq̄ region. Particle density vs normalized projected angle θ_i/θ_ik in the event plane (Fig. 3).
- Jet-to-parton tagging purity from MC: gluon closest to jet #1/#2/#3 in 12/22/51% (Lund), 9/22/49% (Hoyer); 15% (Lund) / 20% (Hoyer) are fake 3-jet qq̄ events (p. 4).

## Results
- **Σ_∥ distributions:** both models reproduce the general trend, but Lund describes Σ_∥^(1) and especially Σ_∥^(0) significantly better (p. 3, Fig. 2a); Σ_∥^(0) data peak ≈ 0.82–0.83 with height ≈ 0.095, close to Lund, while Hoyer's peak height is lower (≈ 0.08) and the distribution broader (≈ read from Fig. 2a). The models' qq̄ parts are similar (Fig. 2b); their qq̄g parts differ, with Lund being more two-jet-like (Fig. 2c), because string fragmentation puts more particles/momentum between q̄ and g (p. 3).
- **Angular particle flow (Fig. 3a):** outside the #1–#2 region both models describe the data reasonably (p. 4). In the #1–#2 (mostly qq̄) region the minimum density in data is ≈ 0.15–0.18 particles/event per bin, Lund ≈ 0.2, Hoyer ≈ 0.25–0.27 (≈ read from Fig. 3a); data agree with Lund, not with Hoyer (p. 4). Minima in regions #2–#3 and #3–#1 are ≈ 0.3–0.35 and ≈ 0.22–0.27 respectively, with both models similar there (≈ read from Fig. 3a).
- **MC truth-ordered (Fig. 3b):** when jet #3 is forced to be the gluon, the q–q̄ minimum is ≈ 0.13 (Lund) vs ≈ 0.25 (Hoyer), i.e. about a factor 2 difference (≈ read from Fig. 3b); the q–g regions are similar or slightly higher for Lund.
- **Table 1** (ratio region #3–#1 / region #1–#2, central range 0.3 ≤ θ/θ_ik ≤ 0.7, statistical errors only):

  | | Data | Hoyer et al. | Lund |
  |---|---|---|---|
  | N, all | 1.35 ± 0.09 | 1.08 ± 0.04 | 1.34 ± 0.06 |
  | N, p_out < 0.2 GeV | 1.23 ± 0.1 | 1.02 ± 0.05 | 1.29 ± 0.07 |
  | N, p_out > 0.2 GeV | 1.6 ± 0.2 | 1.20 ± 0.09 | 1.43 ± 0.12 |
  | N, K (dE/dx-identified, p < 0.7 GeV) | 2.2 ± 0.7 | 0.89 ± 0.2 | 1.74 ± 0.4 |
  | Σ\|p_in\|, all | 1.51 ± 0.1 | 1.18 ± 0.04 | 1.52 ± 0.07 |

  (Tab. 1). Data increase of the asymmetry with m² + p_out² and better agreement with Lund despite large statistical errors (p. 5). For "all", data − Hoyer = 0.27, ≈ 2.7σ with stat. errors combined in quadrature (our arithmetic from Tab. 1); data − Lund ≈ 0.01.
- Conclusion: fragmentation along colour–anticolour axes resembles parton–hadron conversion more closely; this matters when relating jet directions to parton directions, and implies gluons fragment differently from quarks (p. 5).

## Assessment
- Historically decisive and directly on target (string/drag effect seed topic, RQ1b/3), but statistically modest: 326 events, stat. errors only, no systematic uncertainty quoted; the headline discrimination is ~2.5–3σ against one particular independent-fragmentation implementation.
- **Gluon identification is by energy (angle) ordering** only: jet #3 is the gluon in ~50% of events, and ~15–20% are fake 3-jet qq̄ events (p. 4). The measured asymmetry is therefore diluted and model-dependent to interpret; the comparison is valid only through full MC, not as a direct q–q̄ vs q–g measurement. Later analyses (e.g. qq̄γ vs qq̄g comparisons, symmetric/Mercedes topologies, flavour-tagged jets at LEP) were needed to sharpen this.
- **Tuning bias favours Hoyer, not Lund:** parameters were fit to the Hoyer model and reused for Lund, which makes Lund's better agreement more convincing, but also means neither model is optimally tuned; the different qq̄/qq̄g boundaries (26% vs 52%) are a further model difference beyond fragmentation.
- The Hoyer model is a specific IF variant (gluon → single quark carrying all momentum); later work (e.g. Ali et al.-type IF with different gluon treatment, and especially IF with momentum conservation schemes) showed some IF variants could partially mimic the effect, and Azimov–Dokshitzer–Khoze–Troyan showed the effect also arises perturbatively from soft-gluon coherence (colour antenna "drag"), so the observation does not uniquely establish the string picture. The p_out / kaon dependence (Lorentz-boost signature) is the more string-specific evidence, but has large errors.
- Tension check: consistent in direction with later JADE, TASSO, TPC/2γ and LEP measurements of the string effect; the magnitude here (~1.35 in particle number) is not directly comparable to later observables because of the selection and dilution.

## Leads
- Andersson, Gustafson, Sjöstrand, PLB 94B (1980) 211 — the Lund string-gluon model tested here; origin of the string-effect prediction.
- Hoyer, Osland, Sander, Walsh, Zerwas, NPB 161 (1979) 349 — the independent-fragmentation model that fails; needed to judge which IF features cause the failure.
- Ali, Pietarinen, Kramer, Willrodt, PLB 93B (1980) 155 — alternative IF Monte Carlo (cited as parton-direction fragmentation); relevant to model dependence.
- Randa, PRL 43 (1979) 602 and Montvay, PLB 84B (1979) 331 — early proposals of fragmentation along colour axes (colour-flow predictions, RQ2/4).
- JADE follow-ups (Bartel et al., PLB 134 (1984) 275; Z. Phys. C 21 (1983) 37) — higher-statistics confirmation and qq̄γ comparison (not cited here; known follow-ups; PLB 134 (1984) 275 confirmed as JADE "Test of fragmentation models..." via CMS:2013cvx ref. [1], Z. Phys. C 21 [unverified]).
- Azimov, Dokshitzer, Khoze, Troyan, PLB 165 (1985) 147 — perturbative (coherence/drag) explanation of the same effect (not cited here; key for RQ1b/2) [unverified: reference not checkable from this paper].

## Verification
Checked 2026-10-30 by an independent reader: 42 claims checked, 4 corrected, 2 unverifiable.
- Clarified page anchor: Table 1 is on preprint p. 7 = PDF p. 11 (old text read as PDF p. 7).
- "Jet #3 = lowest energy" is an inference from the angle ordering of Fig. 1c, not stated in the paper; marked as such.
- Hoyer minimum in #1–#2 region of Fig. 3a narrowed to ≈ 0.25–0.27; Fig. 2a wording clarified (Hoyer has lower peak height, not lower peak position).
- "First observation" flagged as historical context, not a paper claim; post-1981 follow-up references marked [unverified] except JADE PLB 134 (1984) 275, confirmed via CMS:2013cvx ref. [1].
- All Table 1 entries, event counts (2892/484/326), cuts, tagging fractions (12/22/51/15%, 9/22/49/20%), footnote parameters and 26%/52% qq̄g fractions confirmed.
