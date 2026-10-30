# QCD Coherence in High-Energy Reactions
- **ID / links:** Dokshitzer:1987nm · INSPIRE 21868 · arXiv — · DOI 10.1103/RevModPhys.60.373
- **Authors / collab, year, journal:** Yu. L. Dokshitzer, V. A. Khoze, S. I. Troyan (LNPI Gatchina), A. H. Mueller (Columbia); Rev. Mod. Phys. 60 (1988) 373–388
- **Type:** review (theory/phenomenology, with new predictions)
- **Relevance:** 3 · RQs: 1a, 1b, 1d, 1e, 2, 3, 4
- **Full text source:** zotero (16-page scan with a text layer; all pages and figures read)

## Takeaways
- Two kinds of coherence (Sec. II, p. 375). (1) **Intra-jet angular ordering** of successive soft emissions. It follows from the formation-time argument (QED Chudakov effect) and is implementable in MC (Marchesini–Webber). (2) **Inter-jet coherence** (string/drag effect): when ≥3 partons take part, soft radiation between jets depends on the color topology of the whole ensemble, and "the idea of an isolated jet evolution is here lost". The authors say it is an *open question* to what extent type (2) can be generated in MC simulations (p. 375).
- The canonical inter-jet result is the antenna pattern (Eqs. 1–3). In the symmetric qq̄g event, the soft-gluon density midway between q and q̄ is suppressed relative to qq̄γ by **(N_c²−2)/(2(N_c²−1)) = 7/16** (Eq. 4). Hadronization effects should cancel in this ratio. The string effect seen in e⁺e⁻ (JADE, TPC/2γ, MARK II) is described as a test of "very detailed features of color flow in QCD" (p. 376).
- **New tests proposed for hadron colliders (RQ4, Sec. IV):** azimuthal asymmetries of soft hadrons in the event plane in prompt γ+jet (Compton gq→γq), W+jet, and two-jet (gq→gq) production. These might allow the subprocess to be tagged event by event and so give separated quark and gluon jets. Predicted pion densities are quoted at four directions (Eqs. 21, 32, 36), with background estimates.
- **Hump-backed plateau (intra-jet coherence, Sec. V):** the MLLA gives a Gaussian in ln(1/x) peaking at ln(1/x₀) = Y/2 + B√(bY/16N_c) (Eqs. 41–42). The rapidity w.r.t. the jet axis, y_∥, shows *no* dip (Eq. 40), so x or y = ln((E_p+p)/m) should be used (p. 383). The proposed test: restrict particles to a cone θ₀, then check that the peak moves with jet energy with the slope of Eq. 49. A cone cut alone produces an energy-independent hump even without angular ordering (Eqs. 47–48), so a hump by itself is not a coherence test.
- **LPHD:** hadron spectra equal parton spectra (cutoff Q₀≈Λ≈m_π, p. 384) up to a normalization constant K^h (Eqs. 5, 9–10, p. 377), with K^{π±} ≈ 1.1 fitted to e⁺e⁻ data at ~30 GeV (p. 379). The review also pushes **inclusive energy–multiplicity correlations** over jet-finding as the cleanest connection between theory and data (Sec. III).

## Setup
- Framework: perturbative QCD in the **MLLA** (leading plus next-to-leading logs, i.e. double plus single logs; p. 375). Partonic cascades are built from 1→2 branchings with angular ordering. Hadronization is treated by **LPHD** (Sec. II).
- Processes covered:
  - e⁺e⁻ → qq̄g vs qq̄γ (Sec. II);
  - pp̄ → γ/W/Z + jet and pp̄ → 2 jets at large p⊥, with CERN SppS and Fermilab Tevatron kinematics (Sec. IV);
  - single-particle spectra in jets at e⁺e⁻ (SLC/LEP, 50 GeV jets) and in hadron-collider jets (150 GeV) (Sec. V);
  - final states in small-x DIS in the Breit frame (Sec. VI, HERA).
- Benchmarks are illustrative: E = p⊥ = 20 GeV for γ/W + jet, p⊥ = 90 GeV for two-jet events, and 90° parton–parton scattering. The minimum-bias background is modeled as dN^charged/dy ≈ 6, flat in y and φ, with exp(−k⊥²/(0.45 GeV)²) (p. 380 for the ≲6 bound; pp. 384–385 for the flat/Gaussian model used in Figs. 10–11).

## Results
**Physical origin (RQ1, Sec. II)**
- Formation-time argument (p. 375): t_form ≈ λ⊥/θ_γe. The pair has transverse separation ρ⊥ ≈ λ⊥ θ_{e+e−}/θ_γe. Photons with θ_γe ≫ θ_{e+e−} cannot resolve the pair and see its total charge (zero), so they are suppressed (Chudakov 1955). Independent emission is allowed only for θ_γe < θ_{e+e−} (Fig. 1).
- In QCD, wide-angle soft emission off an unresolved qq̄ or gg pair acts as if it came from the on-shell parent (Fig. 2). This "furnishes the core idea" of the Marchesini–Webber MC (p. 375), and it gives all leading double and single logs for angular-averaged observables.
- Abelian model of the string effect: the gluon is replaced by a collinear e⁺e⁺ pair of double charge (Fig. 3). In the symmetric configuration there is no radiation directly opposite the pair (p. 375).
- QCD soft-gluon antenna for qq̄g (Eq. 1, with a_ij = 1−n_i·n_j and a_i = 1−n·n_i, Eq. 3): α{N_c[a₂₃/(a₂a₃) + a₁₃/(a₁a₃)] − (1/N_c) a₁₂/(a₁a₂)}. For qq̄γ (Eq. 2) it is 2C_F α a₁₂/(a₁a₂). For n midway between q and q̄ (opposite the gluon) the gluon-to-photon ratio dN_g/dN_γ is 7/16 (Eq. 4); I checked this arithmetic for the Mercedes configuration. Inside the cascade, the MLLA factor N′_g(Y) dresses the antenna (Eq. 14).
- The string effect was predicted first by the Lund model (Andersson et al. 1983) but is "difficult to arrange in Monte Carlo branching models" (p. 375).

**Spectra and LPHD (RQ1a/2, Secs. II, V)**
- The MLLA inclusive spectrum in a gluon jet, xD̄^h_g(x,Y), with Y = ln(E/Λ) or ln(E sin(θ/2)/Λ) for a restricted cone (Eqs. 5–8), is a Mellin integral of a confluent hypergeometric function. Fragmentation enters only through K^h(ω, M_h). In the saddle-point limit ω ~ 1/√Y, K^h becomes a constant, so the x-shape is fully perturbative and nonperturbative smearing is a higher-order effect (p. 377).
- Color shielding (preconfinement; Bassetto et al. 1983, Amati–Veneziano 1979) implies that the transition scale μ is Q-independent, which underpins LPHD (p. 377).
- Spectra of hadrons containing a heavy quark in jets should follow parton evolution down to M_H with smaller nonperturbative effects (p. 377).
- Multiplicities: N_g(Y) is given in terms of Bessel functions (Eq. 16), with an asymptotic form (Eqs. 17–18).
  - K^π = 1.1 with Eq. 16 and Q₀ = Λ reproduces about 11 charged pions in e⁺e⁻ at Q ≈ 30 GeV.
  - K^π ≈ 0.6 is needed when the cruder Eq. 18 is used (p. 379).
  - A quark jet has 4/9 of the gluon-jet multiplicity (p. 384).
- Hump-backed plateau:
  - The peak is at Eq. 42.
  - Predicted slope: d ln(E₀/Λ)/d ln(E/Λ) ≈ 0.4 at E ≈ 30 GeV (Eqs. 43, p. 383).
  - Evidence as of 1988: "probably the most convincing evidence" is the growth of E_hump with jet energy (TASSO, Althoff et al. 1984). In e⁺e⁻ the hump is "less than definitive", because the kinematic zero at x_min is hard to separate from the dynamical dip (pp. 382–383).

**Restricted-cone method (RQ4, Sec. V)**
- With particles in a cone θ₀ around a trigger or jet axis, the inclusive energy–particle correlation is Eq. 44, and the peak moves to Eq. 46. The coherence test is the energy dependence of the peak (Eq. 49), using Y(θ₀) = ln(E sin(θ₀/2)/Λ).
- Caveats the authors raise:
  - (i) Small θ₀ lowers the peak, giving an effective jet with E_eff ≈ E sin(θ₀/2).
  - (ii) Without angular ordering, a cone cut alone produces a peak at ln(E₁/Q₀) = −ln sin(θ₀/2), which does not depend on jet energy (Eqs. 47–48, p. 384).
- Fig. 10: e⁺e⁻ at W = 100 GeV with cones of 180°, 45° and 20°.
- Fig. 11: gluon jet with E ≈ 150 GeV at a hadron collider, cones of 60°, 35°, 20° and 10°, including the background. For θ₀ = 35° the peak is about 3 GeV, and at 2 GeV the dip is "already pronounced" with small background contamination (p. 385). The authors conclude that Eq. 49 "should be testable at hadronic colliders".

**Drag effects at hadron colliders (RQ1b/1e/4, Sec. IV)**
- Prompt γ:
  - For x ≲ 0.1, gq→γq dominates qq̄→γg (Eqs. 11–13).
  - At E = p⊥ = 20 GeV the pion densities π dN/dn in the scattering plane are A ≈ 4, B ≈ 3, C ≈ 3, D ≈ 11 (Eq. 21; directions defined in Fig. 7). The enhancement is between the incoming gluon and the outgoing quark.
  - Background: π dN/dn = dN^soft/dy ≲ 6 charged pions (Eqs. 22–23), so the asymmetry "should be dominant".
  - Rate: σ_γ ≈ 2×10⁻³⁴ cm² x_q D x_g D per unit rapidity at p̄⊥ = 20 GeV (Eq. 26), "probably large enough" at Fermilab. Below p⊥ ≈ 10 GeV the background dominates (p. 380).
- W + jet:
  - The ratio r of qq̄→Wg to qg→Wq (Eq. 30) is >1 at CERN energies and ≲1 at Fermilab energies.
  - The annihilation pattern (Eq. 31) gives A = B ≈ 1 and C = D ≈ 8 (Eq. 32), clearly different from the Compton pattern (Eq. 21). The authors say the difference "might make it possible" to decide the production mechanism "for a given event" (p. 381).
- Two-jet:
  - Only gq→gq has a large asymmetry. The full antenna is Eq. 34, using Ellis–Marchesini–Webber hard amplitudes.
  - At 90° (Eq. 35): A = C ≈ 1.7 N′_g, B ≈ 2.1 N′_g, D ≈ 0.5 N′_g (Eq. 36).
  - At p⊥ = 90 GeV, dN^π/dy ≈ 9 (p. 382).
  - gq→gq is only about 50% of two-jet production at Fermilab with p⊥ = 90 GeV, x_g ≈ 0.03 and x_q ≈ 0.33, rising slowly with x_q (p. 381). The asymmetry would therefore be used to *tag* gq events, which would give quark and gluon jets of equal energy in the same event. Event-by-event fluctuations are left to MC (p. 382).

**Selection procedures (Sec. III)**
- Assigning particles to a fixed number of jets is ambiguous: subjets, and particles whose emission depends on the jet ensemble. Non-IR-safe jet finding cannot be compared with higher-order QCD.
- The authors recommend purely inclusive energy–multiplicity correlations (an Σ∫E₂E₃E₄ … dσ observable, p. 377) as a more quantitative measure of the string effect. Crude jet axes suffice for qualitative tests (p. 378).

**DIS (RQ1b, Sec. VI)**
- In the Breit frame (Eq. 50), the current jet is e⁺e⁻-like.
- The target region at small x gets three hard contributions (Eqs. 54–56; Fig. 15 at ln(q/Λ) = 5 and ln(1/x) = 5):
  - I: emission off the quark box;
  - II: coherent "t-channel" color radiation off the ladder;
  - III: fragmentation of ladder rungs.
- Coherence conditions for emission off the ladder are Eqs. 51–53 (Figs. 13–14).
- Predicted: a striking dip at y = 0 between the current and target regions (Fig. 16), with a 1/σ dσ/dy that rises rapidly with Q². The soft-hadron background "we do not yet know how to" estimate, but it is expected to be weakly Q²-dependent, so the effect "should be visible, at least at HERA" (p. 387).

**Experimental status cited (RQ3)**
- String effect in qq̄g vs qq̄γ observed by JADE (Bartel et al. 1983), TPC/2γ (Aihara et al. 1986) and MARK II (Sheldon et al. 1986); reviewed by Hofmann at ICHEP 1986 (pp. 375–376).
- Hump growth seen by TASSO (Althoff 1984).
- Data reviews by Yamamoto 1985 and Sugano 1986 support LPHD (p. 373).
- No hadron-collider drag-effect data existed yet. All Sec. IV–VI results are predictions.

## Assessment
- Within this review the paper is the conceptual anchor. It cleanly separates intra-jet coherence (angular ordering, already in MC) from inter-jet antenna/color-flow coherence (which, the authors say, MC branching models struggle to reproduce). That split is still the right frame for RQ1a vs 1b. The 7/16 ratio is a large-angle soft-gluon result at the leading order in α_s. Its hadron-level validity rests on LPHD and on hadronization canceling in a ratio, which was not demonstrated here. At these energies the Lund string model gives a similar depletion, so the qq̄g/qq̄γ test does not discriminate between perturbative and string interpretations. Later literature (Lund vs HERWIG/LPHD debates) needs to settle this.
- Sec. IV predictions are explicitly "average properties" at single symmetric 90° points:
  - no detector, jet-reconstruction, or underlying-event modeling beyond a flat dN/dy ≈ 6;
  - initial-state radiation only through the antenna;
  - no multiple-parton interactions.
  These are early versions of the jet–boson radiation-pattern and color-flow tests (Tevatron CDF/D0 coherence in 3-jet and W+jet events; later jet pull). The tagging idea for gq→gq, starting from only a ~50% gq fraction contaminated by symmetric processes, is optimistic.
- The hump-backed caveat (a cone cut produces a hump without coherence, Eqs. 47–48) is an important methodological point for interpreting ξ-distributions measured in cones at hadron colliders.
- The DIS predictions (Fig. 16 dip) depend on the unknown soft background and on small-x ladder dynamics. Cross-check them against HERA Breit-frame measurements.
- Many key references are Leningrad preprints (LNPI 1218, 1230, 922) that are hard to obtain. Their published versions (e.g. the Dokshitzer–Khoze–Mueller–Troyan book "Basics of perturbative QCD", 1991) should be found instead.

## Leads
- Azimov, Dokshitzer, Khoze, Troyan 1985, Phys. Lett. B 165, 147 and Sov. J. Nucl. Phys. 43 (1986) 95: the original perturbative string/drag effect.
- Andersson, Gustafson, Ingelman, Sjöstrand 1983, Phys. Rep. 97, 31 (printed as p. 33 in the paper's reference list): the Lund string model, the original string effect.
- Aihara et al. (TPC/2γ) 1986, PRL 57, 945, and Sheldon et al. (MARK II) 1986, PRL 57, 1398: qq̄g vs qq̄γ measurements.
- Bartel et al. (JADE) 1983, Z. Phys. C 21, 37: the first string-effect observation.
- Azimov et al. 1985a, Z. Phys. C 27, 65: LPHD.
- Azimov et al. 1986a, Z. Phys. C 31, 213: hump-backed plateau and the y_∥ dip issue.
- Marchesini & Webber 1984, Nucl. Phys. B 238, 1: the coherent MC (HERWIG precursor).
- Ellis, Marchesini, Webber 1986, Nucl. Phys. B 286, 643: soft radiation in hadron–hadron collisions, the color-flow antenna for 2→2.
- Ermolaev & Fadin 1981, JETP Lett. 33, 269, and Mueller 1981, PLB 104, 161: the discovery of angular ordering.
- Bassetto, Ciafaloni, Marchesini 1983, Phys. Rep. 100, 201: a coherence review.
- Hofmann 1986, ICHEP Berkeley proceedings: the experimental review of the string effect.
- Gribov, Dokshitzer, Khoze, Troyan 1987, JETP Lett.: coherence in DIS final states.

## Verification
Checked 2026-10-30 by an independent reader: 78 claims checked, 10 corrected, 0 unverifiable.
- Two-jet Fermilab kinematics: x values were swapped; paper has x_g ≈ 0.03, x_q ≈ 0.33 (p. 381).
- 7/16 ratio reworded: it is dN_g/dN_γ (qq̄g vs qq̄γ) midway between q and q̄, not a "ratio between q and q̄".
- "~50% purity" reworded: 50% is the untagged gq→gq fraction, not a tagged purity.
- Event-by-event tagging softened to the paper's "might make it possible" (Takeaways and W+jet).
- Good jet variable is y = ln((E_p+p)/m), not ln(E/m); "(B, D)" removed (paper speaks of heavy-quark hadrons generally).
- Quote fixed ("is here lost"), open-question page narrowed to p. 375; page anchors added for Q₀≈Λ≈m_π (p. 384) and the background model (pp. 384–385).
- Lund Phys. Rep. page: noted that the paper prints p. 33 (31 is the actual first page).
