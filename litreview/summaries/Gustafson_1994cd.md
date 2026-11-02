# Colour Interference and Confinement Effects in W-Pair Production
- **ID / links:** Gustafson:1994cd · INSPIRE 374622 · arXiv — · DOI 10.1007/BF01957774
- **Authors / collab, year, journal:** G. Gustafson, J. Häkkinen (Lund), 1994, Z. Phys. C 64 (1994) 659–664
- **Type:** phenomenology / MC model (recoupling algorithm on top of ARIADNE + JETSET)
- **Relevance:** 3 · RQs: 1b, 2, 4
- **Full text source:** zotero (6-page journal scan with a text layer; figures readable but small)

## Takeaways
- **Hard gluons come first, and this changes the recoupling picture.** Gluons with E ≳ Γ_W are radiated incoherently by the two W systems before any recoupling (citing Dokshitzer–Khoze–Orr–Stirling and Sjöstrand–Khoze). The objects that can recouple are therefore two colour-connected parton chains, not two bare qq̄ pairs. Every cut of the q₁g₁…g_n q̄₂ chain combined with every cut of the Q₁G₁…G_m Q̄₂ chain gives a singlet pair with probability 1/N_c² = 1/9. With ⟨n⟩ = ⟨m⟩ ≈ 4.3 gluons (E > Γ_W, k⊥ > 1 GeV) there are (n+1)(m+1) options, so "the total recoupling probability could in principle be very large" (p. 660, Fig. 1).
- **Group theory alone barely constrains the probability.** Treating the two colour bases as non-orthogonal states with ⟨1|2⟩ = 1/N_c = 1/3, the recoupling probability is only bounded to δ < P < 1−δ with δ = 1/2 − √2/3 ≈ 0.03 (p. 660; Eqs. 3–6, Appendix, p. 663). In other words, 1/9 is *not* a derived probability.
- **Proposed dynamical selection (the "GH" recoupling).** Recoupling is assumed to favour "short strings": the configuration that minimises λ₁ + λ₂, where λ ≈ Σ ln[(p_i + p_{i+1})²/m₀²] with m₀ ≈ 1 GeV is the Lund effective rapidity length (∝ multiplicity). Their benchmark takes only this configuration, at a total rate of ~10 % (p. 661).
  - These recouplings shorten the string length by ⟨Δλ⟩ ≈ 2 units, compared with ≈ 0.7 for the purely geometric SK-I selection (p. 661).
  - Like SK, they split each W system into roughly equal halves: ⟨d_rec⟩ = ⟨|E₁−E₂|/(E₁+E₂)⟩ ≈ 0.2 (p. 661).
- **Proposed test (RQ4): events with zero central particles.** Inclusive dN/dy shows a central suppression but cannot establish a ~10 % admixture (Fig. 3; p. 662). However, the probability of having *no* particle in |y| < 0.5 (thrust cut T > 0.76, which keeps 60 % of events) is a factor 55 higher for recoupled events. With 5000 hadronic WW events and 10 % recoupling this gives 13 signal vs 1.9 background events with n_central = 0 (Fig. 4b; p. 662). S/B is stated to be roughly constant from threshold to 190 GeV.
- **Mass systematic.** As a first approximation the m_W uncertainty scales with the total recoupling probability. The authors quote the SK result of ~40 MeV at 35 % recoupling and state that their states would give a similar uncertainty (p. 663). They also flag colour-singlet gg pairs in Z → qq̄gg (probability 1/(N_c²−1) = 1/8), which would hadronize as a closed gluon string loop (Fig. 6). This idea was followed up by Friberg–Gustafson–Häkkinen.

## Setup
- **Process:** e⁺e⁻ → W⁺W⁻ → (q₁q̄₂)(Q₁Q̄₂) at √s = 170 GeV. Results are stated to be representative from threshold to ~180 GeV, because the W width keeps the decay-vertex separation nearly constant in that range; S/B is stated to be constant up to 190 GeV (p. 662).
- **Space-time scales:** Δx ~ 0.05 fm and Δt ≲ 0.1 fm between the W decays (p. 659), so hard gluons with E > Γ_W are emitted incoherently. A footnote gives the soft-gluon relative emission probability as a function of x = γ(v)E_g/Γ_W and the gluon–W angle (p. 660).
- **Vacuum picture** (same as Gustafson_1988fs):
  - type-I superconductor: a bag-like flux tube ~1 fm wide, so recoupling is likely if the production points are < 1 fm apart;
  - type-II superconductor: a thin vortex core, so recoupling is unlikely unless the separation is ≪ core size (p. 659).
- **Comparison to Sjöstrand–Khoze (p. 660–661):**
  - SK-II (type II) treats strings as thin lines that recouple with unit probability at the first crossing. It gives ~35 % recoupling at √s = 170 GeV, which GH regard as an upper limit for type II.
  - SK-I (type I) uses Gaussian flux tubes with r_had = 0.5 fm. The probability density is a free parameter, 0.9 fm⁻⁴, chosen to give the same 35 %. GH stress that this value "has no dynamical motivation".
  - SK-II′ allows only recouplings that shorten strings.
- **B → J/ψ X analogy (p. 660).** Branching-ratio analyses suggest ~15–20 % recoupling at zero distance and low energy (ref. [4], Neubert et al.; Henderson, Moriond 1994). The 1988 paper gave no number for the same analogy, only "somewhat larger than (but still compatible with)" 1/9 (see Gustafson_1988fs).
- **Simulation (p. 662):**
  - ARIADNE dipole cascade for gluons with E ≳ Γ_W;
  - recoupling to the min(λ₁+λ₂) configuration;
  - JETSET string fragmentation, with soft gluons (E < Γ_W) neglected.
  - Thrust cuts are used instead of the earlier 30° opening-angle selection, because gluon recoil spoils the angle cut.
- **Observables:**
  - dN/dy for T > 0.92 and T > 0.76 (Fig. 3);
  - the multiplicity distribution in |y| < 0.5 (Fig. 4);
  - the expected number N₀ of events with zero central particles vs the rapidity window |y| < y_cut (Fig. 5; 5000 hadronic WW events).

## Results
- **Inclusive rapidity (Fig. 3):** recoupled events show a suppressed central region but it is "not totally empty". This is called similar to SK's results. The average distribution cannot reveal an admixture of order 10 % (p. 662).
- **Central multiplicity (Fig. 4, |y| < 0.5, including π⁰):**
  - The difference between normal and recoupled events is larger for T > 0.92, but only ~4 % of events pass that cut.
  - For T > 0.76 (60 % of events), P(0) is 55× larger for recoupled events.
  - P(1) also differs strongly and can be added to the analysis (p. 662).
  - Implied P(0) values from the quoted counts (our arithmetic, not stated in the paper): 13/(0.6·0.1·5000) ≈ 4.3 % for recoupled events vs 1.9/(0.6·0.9·5000) ≈ 0.07 % for normal events. Their ratio of ≈ 61 is roughly consistent with the quoted factor 55, given that the counts are rounded.
- **Window dependence (Fig. 5):**
  - N₀ falls steeply with y_cut for both classes: ~32 (recoupled) and ~29 (normal) at y_cut = 0.3; normal reaches ~0 at y_cut ≈ 0.7 and recoupled near 0 at y_cut ≈ 1 (read off the figure). Normal events fall faster, so S/B improves with larger windows at the cost of statistics.
  - The caption does not say which thrust cut or recoupling fraction applies. The curves at y_cut = 0.5 (~13 recoupled, ~2 normal, read off the figure) match the quoted 13 vs 1.9, which is consistent with T > 0.76 and 10 %, but this is not stated.
- **Recoupled-string kinematics (p. 661):** ⟨Δλ⟩ ≈ 2 for min-λ recoupling (larger with the thrust cut), vs ≈ 0.7 for SK-I geometric selection; ⟨d_rec⟩ ≈ 0.2.
- **m_W:** no new computation. The ~40 MeV SK estimate at 35 % recoupling is quoted, with uncertainty taken as proportional to the recoupling probability (p. 663).
- **Appendix bound:** sin 2θ · cos φ = 1/3 implies |sin 2θ| ≥ 1/3, so 0.03 < |β|² < 0.97 (Eqs. 5–6). We checked: 1/2 − √2/3 = 0.0286.

## Assessment
- **Conceptual contributions.** The paper makes three points that remain central to CR modelling:
  - The (n+1)(m+1) combinatorics after hard-gluon emission means "1/N_c²" does not fix the total CR rate. This is the same tension later seen in LEP2's preferred SK-I p_reco ≈ 51 % at 189 GeV, far above 1/9 (ALEPH_2013dgf).
  - The rigorous 3 %–97 % bound shows that the 1/9 counting carries little weight on its own.
  - Recoupling may be dynamically driven by string-length (λ) minimisation, i.e. in momentum space rather than by space-time overlap.
  - This λ/area-minimisation idea is the ancestor of later λ-based models: Rathsman's GAL (Rathsman_1998tp) and, per the L3_2003oci summary, the ARIADNE AR-2 inter-W reconnection, which L3 cites to this paper and to Lönnblad 1996 (refs. [3], [9]). The DELPHI_2006tie summary describes AR-2 but does not record which papers DELPHI cites for it. It also anticipates the PYTHIA 8 / gluon-move style "minimise string length" CR.
- **The 10 % rate is an input, not a prediction.** The proposed observable assumes the extreme selection that only the min-λ state recouples. Its sensitivity depends on this choice, because those are exactly the events that differ most from normal ones (p. 661). If CR instead spreads over many states with small Δλ, as in SK-I (⟨Δλ⟩ ≈ 0.7), the zero-central-particle signal would be much weaker per reconnected event. The paper acknowledges this only qualitatively (p. 662, last paragraph of Sec. 3).
- **Statistics and experimental realism.** The 5000-event benchmark is roughly the order of one LEP2 experiment's fully hadronic WW sample. This is our rough estimate from ~0.6 fb⁻¹ per experiment (Tab. 4.2 of ALEPH_2013dgf) and a WW cross section of order 17 pb with ~46 % fully hadronic BR. The cross section and BR are not verified here.
  - Signal 13 vs background 1.9 is at the generator level. No detector effects, four-fermion/qq̄ background (which can also give central gaps) or hadronisation-model uncertainty on P(0) are included. Normal-event P(0) ~ 10⁻³ is very sensitive to the fragmentation tune. A robust test would need the no-CR rapidity-gap tail controlled at that level.
- **Relation to the LEP2 outcome.** According to ALEPH_2013dgf (p. 67), observables other than particle flow and m_W estimators (multiplicity, rapidity, p_T, etc.) had "only limited sensitivity". The LEP combination constrains SK-I only, and the GH model is explicitly *not* directly constrained (ALEPH_2013dgf Assessment). We have not yet seen any LEP2 analysis of the specific n_central = 0 observable proposed here. Whether one was done is open; searching for it is a lead.
  - The m_W statement (uncertainty ∝ recoupling probability, ~40 MeV at 35 %) is consistent in order of magnitude with LEP's final 35 MeV CR systematic on m_W(qqqq) evaluated at SK-I k_I = 2.10 (ALEPH_2013dgf, Tab. 7.3), though the two numbers come from different jet reconstructions and models.
- **Z → qq̄gg gluon-singlet (closed string loop) remark.** It opens the e⁺e⁻ (single-system) CR test programme: rapidity gaps in gluon jets, tested by OPAL, L3 and ALEPH as noted in Christiansen_2015yqa and ALEPH_2013dgf. This line is relevant to RQ1b/4.

## Leads
- Friberg, Gustafson & Häkkinen, Nucl. Phys. B 490 (1997) 289: the "following paper" promised on p. 663. It covers colour-singlet gluon pairs and closed strings in Z decays and is the origin of the gluon-jet rapidity-gap CR test. High priority.
- Lönnblad, Z. Phys. C 70 (1996) 107: implements dipole-based (λ-minimising) reconnection in ARIADNE (AR-1/2/3), the model LEP experiments used as an alternative to SK. It is the direct implementation of this paper's idea.
- Sjöstrand & Khoze, Z. Phys. C 62 (1994) 281 and PRL 72 (1994) 28 (refs. [2,5]): SK-I/II/II′ and the ~40 MeV m_W estimate.
- Dokshitzer, Khoze, Orr & Stirling, Nucl. Phys. B 403 (1993) 65 (ref. [1]): shows that hard gluons (E > Γ_W) are emitted independently by unstable-particle decay products, which is the perturbative basis of the whole set-up (RQ1b, 2).
- Andersson, Dahlqvist & Gustafson, Phys. Lett. B 214 (1988) 604 and Z. Phys. C 44 (1989) 455 (ref. [6]): definition of the λ measure used for the recoupling selection (RQ2).
- Neubert et al. in "Heavy Flavours" (A.J. Buras & M. Lindner eds., World Scientific 1992; printed "Lindman" in the reference list), and S. Henderson, Moriond 1994 (ref. [4]): source of the 15–20 % B → J/ψ recoupling estimate. Low priority, analogy only.
- Search lead: any LEP2 (or later re-analysis) measurement of the probability of zero or one charged particle in a central rapidity window in fully hadronic WW, i.e. the RQ4 test proposed here. Try INSPIRE `t "colour reconnection" and t "rapidity gap" and t WW`.
