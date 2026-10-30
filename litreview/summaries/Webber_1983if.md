# A QCD Model for Jet Fragmentation Including Soft Gluon Interference
- **ID / links:** Webber:1983if · INSPIRE 193786 · arXiv — · DOI 10.1016/0550-3213(84)90333-X
- **Authors / collab, year, journal:** B.R. Webber (CERN), 1984, Nucl. Phys. B238 (1984) 492–528
- **Type:** MC/model
- **Relevance:** 3 · RQs: 1a, 2, 3, 4
- **Full text source:** zotero

## Takeaways
- Founding paper of the HERWIG lineage: first full (quark+gluon, 5-flavour) final-state parton shower with soft-gluon interference implemented as **angular ordering** in the variable ξ = q_j·q_k/(ω_j ω_k) ≈ 1−cos θ (Eqs. 1–3, 5–6; p. 495–497), combined with Wolfram-type **cluster hadronization** of colour-singlet qq̄ pairs defined by the **leading-1/N_c planar colour flow** (Fig. 2; p. 499).
- Coherence is physically interpreted as soft long-wavelength gluons not resolving individual colour charges inside the jet, so the jet radiates as a single colour source (p. 496); neglecting it overestimates soft radiation. Parton-level consequences: hump-backed ln x distribution peaked at x ~ √(Q₀/Q), central rapidity dip, multiplicity exponent reduced by 1/√2 (p. 496).
- With 3 parameters (Λ = 0.25 GeV, Q₀ = 0.6 GeV, M_f = 4 GeV; Eq. 17, Tab. 1) it describes PETRA/PEP e⁺e⁻ data (spectra, multiplicities, ⟨p_T²⟩, event shapes) well, except K± normalization (Figs. 7–19, Tab. 2).
- Proposed test (RQ4): the coherence "interference peak" in ln(1/x_p) should show its asymptotic √(Q_h/Q) scaling first for **kaons and baryons** (above ~10 GeV), pions only at much higher Q (Eqs. 24–27, Figs. 25–27; p. 524–525). (Later confirmation of the hump-backed plateau at LEP is outside this paper.)
- Coherence helps resolve the Field–Wolfram conflict between ⟨p_T²⟩ growth and x_p scaling violation (p. 515); gluon jets predicted broader/higher-multiplicity, with qualitative support from UA1/UA2 p̄p jets (Figs. 21–24).

## Setup
- Process: e⁺e⁻ → hadrons at √s ≈ 3–40 GeV (TASSO, JADE, PLUTO, CELLO, DASP, MARK I/II, CLEO data); dijets at the CERN SppS (UA1, UA2). No initial-state shower; p̄p jets are simulated as isolated qq̄ or gg jet pairs with measured dijet angular/mass distributions (p. 518).
- Perturbative stage: Markov branching with Sudakov form factor in ξ (Eqs. 5–6), ξ ordered (upper limit = ξ of previous branching, p. 497), energy-fraction limits z_min = Q_j/(ω√ξ), z_max = 1 − Q_k/(ω√ξ) (Eq. 7), α_s evaluated at q_T² = 2z²(1−z)²ω²ξ (Eq. 8), cutoffs via quark masses and gluon mass Q₀ (Eq. 4). Simplified g→qq̄ form factor (Eqs. 9–10); setting Λ̃ = 2m₀ = Q₀ (Eq. 11) forces all gluons to split non-perturbatively into qq̄ at the end (preconfinement).
- Kinematics: not manifestly covariant; whole final state generated as a single "photon jet" in one hemisphere (θ₀ ≤ π/2) then boosted to the rest frame, so that both jets develop coherently and no angular region is artificially forbidden (p. 498). Azimuths are random (no azimuthal correlations).
- Colour: only the leading term in 1/N_c, planar colour-index structure (Fig. 2); adjacent colour-connected q q̄ form singlet clusters. No colour-suppressed configurations or colour rearrangement.
- Hadronization: isotropic quasi-two-body cluster decay to 0⁻, 1±, 2⁺ meson nonets and ½⁺, 3/2⁺ baryon multiplets, weighted by spin degeneracy × phase space (p. 501); clusters with M_C > M_f split via "symmetrical string breaking" (Eqs. 12–14, Fig. 4); heavy flavour by free-quark β-decay (Fig. 5).

## Results
- Cluster mass spectrum peaks at ~1 GeV, falls steeply and is Q²-independent between 35 and 53 GeV (Fig. 3) — the preconfinement property; ~1 in 10 clusters has M_C > 4 GeV (p. 501).
- Parameter dependence at 34 GeV is weak (Tab. 2); with Eq. 17: ⟨S⟩ = 0.11 vs data 0.13 ± 0.04, ⟨T⟩ = 0.91 vs 0.89 ± 0.02, ⟨n_π±⟩ = 9.6 vs 10.3 ± 0.4, ⟨n_K±⟩ = 1.2 vs 2.0 ± 0.2, ⟨n_p⟩ = 0.6 vs 0.8 ± 0.1 (Tab. 2).
- Inclusive spectra for π±, π⁰, p p̄ agree in shape and absolute normalization; K± is too low by ~×2 (MC curve shown ×2) (Fig. 7c); neutral K⁰ and Λ agree (Fig. 8). TASSO's ~40% charged/neutral kaon excess vs ~5% in the model is flagged as unexplained (p. 506).
- Mean charged multiplicity follows (above the bb̄ threshold) the expected asymptotic coherent-branching form ⟨n⟩ ∝ (ln Q/Λ)^p exp(c√ln(Q/Λ)) with p = −0.492, c = 6.26 (Eqs. 18–20), agreement "satisfactory" though possibly slightly low (Fig. 10). KNO multiplicity distribution matches PLUTO (Fig. 11); ⟨n⟩/D ≈ 3 vs asymptotic 1.63 (Eq. 21).
- ⟨p_T²⟩ vs Q, p_T² spectra, p_T in/out, ⟨1−T⟩, ⟨S⟩ all agree with TASSO/PLUTO (Figs. 12–16).
- Rapidity w.r.t. thrust axis: predicted central dip, a hadron-level remnant of the parton-level coherence dip; it nearly disappears if the sphericity axis is used (Figs. 17–18). At 29 GeV the prediction is 10–20% low for y < 2 (p. 512); x_p scaling violations reproduced in slope; normalization slightly low at the smallest x_p and a little high at large x_p (Fig. 19, p. 514). The author suggests this 10–20% soft-hadron deficit may come from LL coherence being "completely destructive", which non-leading corrections would soften (p. 514–515, 525).
- Comparison with Field–Wolfram [21] (no interference): they needed large Λ to get ⟨p_T²⟩, leading to excessive scaling violation; Gottschalk [22] needed ad hoc early bremsstrahlung enhancement. Here this arises naturally from α_s(q_T²) plus angular ordering being more restrictive late in the cascade (p. 515). FW multiplicity is numerically similar in the accessible range, although neglecting interference doubles the exponent c; at Q = 100 GeV Gottschalk's refined incoherent model [22] already begins to show a faster rise (p. 515).
- Gluon jets (scalar colour-singlet gg source): ⟨n⟩_gg/⟨n⟩_qq ≈ 1.6 in the PETRA range vs asymptotic C_A/C_F = 9/4, with slow O(√α_s) convergence fitted as 9/4 − 1.28 (ln E/Λ)^{-1/2} (Eq. 22, Fig. 20); narrower KNO distribution (Fig. 11, Eq. 23); gluon jets broader, with *fewer* particles at high rapidity, so a small cone (half-angle < 15° at 29 GeV) would contain fewer particles for a gluon jet (p. 516).
- p̄p: UA2 jet charged multiplicity lies above quark-jet prediction and close to gluon-jet prediction (Fig. 21); UA2 E_T azimuthal flow reproduced, jet widths closer to gluon jets (Fig. 22); UA1 z and p_T in 35° cone between quark and gluon predictions (Figs. 23–24); average multiplicities after cuts 5.8 (q) vs 8.1 (g) (p. 520).
- Interference peak: hadron ln x peak shifts to x ~ √(Q_h/Q) with Q_h ≈ m_h/2 (Eqs. 24–25), with low-Q kinematic regime x ~ Q_c/Q, Q_c ≈ 1.5 GeV (Eq. 26); transition at Q_trans ~ 4.5/m_h GeV (Eq. 27) ≈ 30 GeV for pions. MC ⟨ln 1/x_p⟩ shows the asymptotic slope for K± and p above ~10 GeV but not for π± (Fig. 27).

## Assessment
- Historically central for RQ1a/RQ2: establishes angular ordering as the practical MC implementation of intra-jet soft-gluon coherence and ties it to cluster hadronization via leading-N_c colour flow; the planar colour connection of Fig. 2 is the ancestor of all later "colour flow" bookkeeping in HERWIG (and the baseline against which colour reconnection is defined).
- Coherence here is only *intra-jet* angular ordering plus the single-hemisphere trick that makes q and q̄ jets share one cascade; there is no explicit treatment of inter-jet (antenna) interference in multi-jet events, no initial-state shower and no initial–final interference — addressed in Marchesini & Webber 1988.
- Data comparisons are mostly global observables that also incoherent models fit after tuning (the author concedes Field–Wolfram multiplicities are "surprisingly close", p. 515); the direct coherence signatures (rapidity dip; ln x peak for unidentified, mostly pion, hadrons) were not yet resolvable at PETRA (p. 514, 524), though the kaon/baryon peak was claimed testable at existing energies. The discriminating power claimed lies in Q-evolution (exponent c) and the identified-hadron peak test.
- Known weaknesses: K± normalization off by ×2; 10–20% soft-hadron deficit; non-covariant frame-dependent formulation; p̄p jets modelled without underlying event, with large background-subtraction model dependence (p. 518–519). Gluon/quark multiplicity ratio and peak positions sensitive to uncomputed O(√α_s) corrections (p. 525).

## Leads
- Marchesini & Webber, Nucl. Phys. B238 (1984) 1 [ref. 23] — the original coherent gluon-cascade MC; direct predecessor.
- Mueller, Phys. Lett. 104B (1981) 161; Ermolaev & Fadin, JETP Lett. 33 (1981) 269; Dokshitzer, Fadin & Khoze, PLB 115B (1982) 242 / Z. Phys. C15, C18 [refs. 7–9] — derivation of soft-gluon coherence/angular ordering and the hump-backed plateau.
- Bassetto, Ciafaloni, Marchesini & Mueller, Nucl. Phys. B207 (1982) 189; Bassetto, Ciafaloni, Marchesini, Phys. Rep. 100 (1983) 201 [refs. 10, 13] — coherent branching formalism review.
- Field & Wolfram, Nucl. Phys. B213 (1983) 65 [ref. 21] and Gottschalk, Nucl. Phys. B214 (1983) 201 / B227 (1983) 413 [refs. 22, 29] — incoherent cluster-model predecessors; baseline for coherence effects.
- Amati & Veneziano, PLB 83B (1979) 87 [ref. 31] — preconfinement, basis of colour-singlet clustering.
- TASSO, Brandelik et al., Phys. Lett. 89B (1980) 418 / Z. Phys. C4 (1980) 87 [refs. 46, 52] — rapidity distribution where the coherence dip would be tested [46]; thrust/sphericity vs Q [52].
- Later experimental tests of the identified-hadron ln(1/x_p) peak (e.g. TASSO/TPC, OPAL/L3 ξ_p peak vs √s) — natural follow-up for RQ3.

## Verification
Checked 2026-10-30 by an independent reader: 58 claims checked, 6 corrected, 0 unverifiable.
- Q ~ 100 GeV statement: it is Gottschalk's refined incoherent model that begins to rise faster at 100 GeV (p. 515), not a generic "differences appear" prediction for Field–Wolfram.
- Fig. 19: added that the prediction is also a little too high at large x_p (p. 514).
- Removed anachronistic "MLLA-type" label for Eq. 18 (paper: "expected asymptotic behaviour").
- Flagged "later confirmed at LEP" as external to the paper.
- e⁺e⁻ data range starts at ~3 GeV (SPEAR Mark I, Fig. 10), not 5 GeV.
- Clarified PETRA non-resolvability applies to unidentified hadrons; fixed description of refs. [46]/[52].
