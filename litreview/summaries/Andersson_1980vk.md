# How to Find the Gluon Jets in e+e- Annihilation
- **ID / links:** Andersson:1980vk · INSPIRE 152513 · arXiv — · DOI 10.1016/0370-2693(80)90861-8
- **Authors / collab, year, journal:** B. Andersson, G. Gustafson, T. Sjöstrand (Lund), 1980, Phys. Lett. B 94 (1980) 211–215 (received 18 March 1980)
- **Type:** MC/model (phenomenology)
- **Relevance:** 3 · RQs: 1b, 2, 4
- **Full text source:** zotero (5 pp., scanned journal pages with a clean text layer; read from page images)

## Takeaways
- This is the original prediction of what became the **string effect**. In the Lund picture the gluon is a "kink" on the string between q and q̄ (Fig. 1). Hadrons from a qq̄g event therefore lie in momentum space along two hyperbolae spanning the q–g and g–q̄ string pieces, and not along the q–q̄ direction (Fig. 2). The prediction is more particles in the angular region between the gluon and the q (or q̄) than between q and q̄ (pp. 211–212).
- The authors stress that this angular effect and the larger gluon-jet multiplicity are each too small to tag gluons event by event (pp. 211–212). They combine both into an event-level correlation asymmetry, predicted "of the order of 16%" and observable "in a sample of a few hundred three-jet events" (p. 212).
- The quantitative test is a comparison of two MC models at √s = 30 GeV, Lund string vs an independent-fragmentation model "A" (gluon fragments as a quark). Under the stated cuts each of Δn and Δθ picks the gluon correctly in 70% of correctly reconstructed events with a gluon in a weaker jet. Δn·Δθ > 0 occurs in 60% of such events (58% including backgrounds), against 50% if either effect is absent (p. 214).
- The paper presents the asymmetry as a "crucial test" of the string gluon model. Its absence would mean the confining field has "further … non-trivial dynamics" (p. 214). It contains no perturbative or coherence argument: the effect is attributed entirely to the hadronization (string-topology) stage.
- There is no data comparison for the asymmetry itself. The model is said to be in "fair agreement" with PETRA multiplicity, sphericity, thrust and p⊥² data, but so does model A (p. 213).

## Setup
- **Physics picture (pp. 211–213).** The gluon is treated as a point-like, energy-carrying "kink" on a massless relativistic string without transverse excitations.
  - The string acts on the kink with twice the force it exerts on an endpoint quark. The authors compare this with the QCD ratio 2/(1−1/N²) for N colours (p. 211); this is C_A/C_F, a reviewer remark.
  - Hadrons come from qq̄ breaks. Each vertex is weighted by |g(κτ/μ⊥)|² h(πμ⊥²/κ) with h(z) = exp(−z), i.e. Schwinger-type tunnelling (Eqs. 1–2, pp. 212–213).
  - The gluon is fragmented by first cutting off the "first-rank" meson at the kink with one break in each leg. Each remaining leg then fragments like an ordinary qq̄ jet in its own rest frame (p. 213).
  - The typical distance of primary mesons from the hyperbolae is ~300 MeV, comparable to jet p⊥ (p. 211).
- **Partonic input (p. 213).** First-order QCD qq̄g matrix element; 4-jet states are neglected. A qq̄g event is treated as qq̄ if M_qg ≲ 3 GeV, or if E_g ≲ 2 GeV in the frame where q and q̄ are back-to-back and g is perpendicular. The MC is the Lund Jet MC (LUJMC).
- **Alternative model "A" (p. 213).** q, q̄ and g fragment independently. The gluon fragments "as a quark", with flavour u, ū, d, d̄, s, s̄ in the ratio 2:2:2:2:1:1. In model A the gluon jet has no larger multiplicity than a quark jet and the q–q̄ region is not depleted.
- **Study conditions (pp. 213–214).**
  - √s = 30 GeV, generator level, no radiative corrections or acceptance cuts; charged and neutral particles (except ν) are used.
  - Three-jet selection: thrust T < 0.9, both weaker jets within 150° of the strongest jet, and Σ|p| > 5 GeV per jet. About 10% of all events survive (p. 214).
  - The event plane is the thrust and major axes (xz-plane), with the "slim jet" along +z. p_y is ignored.
- **Event classes (p. 214).**
  - I: misidentified qq̄ events, mostly bb̄-like, or badly reconstructed qq̄g events: ~6%.
  - II: correctly identified qq̄g events with the gluon as the strongest jet: ~11%.
  - III: gluon in one of the two weaker jets, the target class (remainder).
- **Observables (Eqs. 3–7, p. 214).**
  - n₁, n₂: multiplicities on the p_x > 0 and p_x < 0 sides with |p_z| < 2 GeV and |p_x| > 0.2 GeV.
  - Angular measures: momentum-weighted direction vectors p̄_k^(i) = Σ_{A_k} |p_j|^(i−1) p_j, with cos θ_k^(i) = (p̄_k^(i))_z / |p̄_k^(i)|. Here A_k means √(p_x² + p_z²) > 0.2 GeV and θ > 30°, plus |p_x| > 0.2 GeV if p_z > 0 (Eqs. 3–4). In the string model θ_k^(2) − θ_k^(0) tends to be more positive on the gluon side.
  - Jet-strength imbalance is corrected with ΔP = Σ_{A₁}|p| − Σ_{A₂}|p| (Eq. 5). This gives Δn = n₁ − n₂ + aΔP (Eq. 6) and Δθ = (θ₁^(2) − θ₁^(0)) − (θ₂^(2) − θ₂^(0)) + bΔP (Eq. 7), with a = 0.08 GeV⁻¹ and b = −0.032 rad GeV⁻¹. a and b are tuned so that model A has ⟨Δn⟩ = ⟨Δθ⟩ = 0 as a function of ΔP, and they depend on energy and acceptance (p. 214).

## Results
- **Gluon tagging (p. 214).** Calling the gluon jet 1 if Δn > 0 (else jet 2) is correct in 70% of class III events. Δθ alone also gives 70%. Other multiplicity or angular variables give similar reliability.
- **Combined asymmetry (p. 214).** Δn·Δθ > 0 in 60% of class III events, and 58% once class I and II backgrounds are included. The no-effect expectation is 50%, provided the jet-strength bias is removed correctly. Δn and Δθ were chosen to maximise this asymmetry.
  - The headline "of the order of 16%" (p. 212) matches 58% − 42% = 16%. This identification is our inference: the paper does not spell it out.
- **Tagging in the enriched subsample (p. 214).** Within Δn·Δθ > 0 the gluon is identified correctly in 80% of class III events. Cuts on |Δn| and |Δθ| raise the asymmetry at a large cost in rate.
- **Model A (p. 214).** No such asymmetry by construction: a and b are calibrated on it.
- **Statistical errors.** None are quoted on the MC fractions, and the generated sample size is not stated.

## Assessment
- **Historical role.** This is the first statement of the string effect, but it is framed as a gluon-tagging recipe built on a correlation of two weak effects. It is not the inter-jet population ratio later used by JADE (JADE_1981ofk: N₁₃/N₁₂-type ratio 1.35 ± 0.09 in data vs 1.34 Lund vs 1.08 IF). The paper itself makes no claim about a depletion ratio's size. Fig. 2 is schematic, so the q–q̄ depletion is a qualitative statement here.
- **Physics content vs. Azimov:1985zta.** The mechanism is purely non-perturbative: two string pieces, each fragmenting isotropically in its own rest frame and Lorentz-boosted. Azimov et al. (Phys. Lett. B 165 (1985) 147) later showed that leading-N_c soft-gluon emission from a qq̄g antenna has the same "two boosted qq̄ dipoles" structure. Their explicit claim is that the perturbative and string explanations "appear to be rather close". The force ratio 2/(1−1/N²) quoted here is exactly C_A/C_F, a sign that the string kink already encodes the colour-charge ratio that drives the perturbative antenna pattern. This paper therefore cannot discriminate the two pictures; it only discriminates string vs independent fragmentation.
- **Caveats.**
  - The asymmetry signal (60% vs 50%) is small and depends on the bias correction (a, b), which is calibrated on an MC model. A real measurement inherits that model dependence, as the authors acknowledge (p. 214).
  - The parton-level input is first-order only. There is no parton shower, so no perturbative coherence. 4-jet events are not included and acoplanarity cuts are left open (p. 214).
  - Hadrons are at generator level without detector effects.
- **Comparison with Khoze:1989km.** That paper (Khoze & Lönnblad 1990) quantifies when the string-only mechanism stops dominating. With an ARIADNE dipole cascade added, the p_out and hadron-mass dependence, which is the hallmark of the boost mechanism proposed here, is "drastically reduced already for LEP energies". So the specific kinematic signature of this paper is a low-energy (PETRA/PEP) phenomenon.

## Leads
- Andersson & Gustafson, Z. Phys. C 3 (1980) 223, "Semiclassical models for gluon jets and leptoproduction based on the massless relativistic string" (= Andersson:1979ij, already queued). This is the gluon-as-kink string model the prediction is built on; needed for RQ2 (string model of colour flow).
- B. Andersson, G. Gustafson, T. Sjöstrand, preprint LU TP 80-1 (journal version not identified; look up on INSPIRE). Defines the transverse-momentum / tunnelling vertex weighting (Eqs. 1–2). Low priority, model detail only.
- Andersson, Gustafson, Ingelman, Sjöstrand, Phys. Rep. 97 (1983) 31 (= Andersson:1983ia, queued). The standard Lund reference, cited by Azimov et al. for the string effect; check its string-effect section for quantitative r predictions.
- JADE Collab., W. Bartel et al., Z. Phys. C 21 (1983) 37 (likely JADE:1983ihf, queued). The first detailed string-effect measurement with r = N₁₃/N₁₂ and p_out / kaon dependences. It is the data that Azimov:1985zta compares to.
- PETRA rapporteur/collaboration talks (Söding, Geneva 1979; FNAL 1979, ref. [1]) are early 3-jet evidence. Not worth queueing for this review.
