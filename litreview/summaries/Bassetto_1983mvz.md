# Jet Structure and Infrared Sensitive Quantities in Perturbative QCD
- **ID / links:** Bassetto:1983mvz · INSPIRE 201902 · arXiv — · DOI 10.1016/0370-1573(83)90083-2
- **Authors / collab, year, journal:** A. Bassetto, M. Ciafaloni, G. Marchesini, 1983, Phys. Rept. 100 (1983) 201–272
- **Type:** review
- **Relevance:** 3 · RQs: 1a, 1b, 2, 4
- **Full text source:** zotero

## Takeaways
- An early textbook-style derivation of soft-gluon coherence. The eikonal insertion current J^μ(q) = Σ_i T_i (q_i^μ/q_i·q − n^μ/n·q) (Eq. 3.29) acts as an operator in colour space. Large-angle soft emission factorizes and "measures the total colour charge" T_Jet of the jet it surrounds, so gluons at large angle are radiated coherently "as if [by] a single parton" (Eqs. 3.33–3.35, Fig. 3.5; p. 270).
- The strongly-ordered tree-level multi-gluon emission probability from a colour-singlet gg source has a "closed-chain" (antenna/dipole) structure: a sum over permutations of products of nearest-neighbour factors 1/(ζ_{i1i2} ζ_{i2i3} ⋯) with ζ_ij = 1−cosθ_ij (Eqs. 3.40, 3.43, 6.12; Fig. 3.6). This is the colour-connected, dipole-like structure later used by dipole/antenna showers and colour-flow pictures.
- Interference ("crossed") diagrams cancel the ladder contribution outside the angular-ordered region θ_12 ≪ θ_23 ≪ ⋯ (Eqs. 5.12–5.17, Fig. 5.1). The result is an angular-ordered branching process: Altarelli–Parisi vertices with the angle ζ as evolution variable and the constraint ζ′, ζ″ < ζ (Eqs. 6.7–6.9, 6.26–6.27; Fig. 6.1b).
- Consequences: (i) a multiplicity anomalous dimension γ_{N=1} = √(ᾱ_s/2) + C_1 α_s, giving n_jet ∝ (log Q²/Λ²)^{K_1} exp(K_0 √log(Q²/Λ²)) with K_0 ≈ 1.7 and K_1 ≈ 0.73 for N_F = 4 (Eqs. 5.7, 8.1–8.4). (ii) The "hump-backed" Gaussian in log(1/x), peaking at x ≈ (Q_0/Q)^{1/2} with a dip at x ≈ Q_0/Q (Eq. 5.26). A coherent MC shows it (Figs. 6.5–6.6); a non-coherent MC does not (Fig. 6.7).
- Colour structure (planar, large-N_c): partons "close in colour" have Sudakov-damped mass spectra, M² dσ/dM² ≈ F²(M², Q_0²) (Eq. 6.55). Colour-connected clusters have masses of a few Q_0 in the MC (Fig. 6.8), which is the perturbative basis of preconfinement and of cluster hadronization (p. 251–258). The authors also propose testable signatures (depletion at small x, multiplicity growth, KNO dispersions, cone/energy-flow form factors) (Sec. 8, p. 268–270).

## Setup
Theory review. Leading-logarithmic-derivative (LLD) / double-log accuracy, mostly frozen or one-loop running α_s. Massless partons with an infrared virtuality cutoff Q_0 (Q_0 ≈ 0.4 GeV and Λ = 0.2 GeV in the MC, p. 256). Processes: e⁺e⁻ → qq̄ (and a fictitious colour-singlet gg "jet" used for the explicit colour algebra), DIS (x → 1, small x / Regge), Drell–Yan.

- **Sec. 3 (soft-gluon techniques).** Eikonal vertices in a physical (n·A = 0) gauge. Strong energy ordering |q_1| ≪ |q_2| ≪ ⋯ ≪ Q/2 (Eq. 3.19). Only external-leg insertions are kept, and virtual corrections are omitted in Sec. 3.4.
- **Sec. 4.** Semi-inclusive form factors: Sudakov resummation for x → 1 and p_⊥ → 0, back-to-back energy correlations, Sterman–Weinberg cone distributions.
- **Secs. 5–6.** Multiplicity and the interference (coherence) structure; the angular-ordered branching process and its generating functional; the colour structure of the final state; Monte Carlo results from ref. [42] (Marchesini–Webber).
- **Sec. 7.** DIS and Drell–Yan applications, and the BFKL/Lipatov small-x regime.
- **Sec. 8.** Summary and proposed checks.

## Results
**Colour coherence and antenna structure (RQ 1a, 2)**
- Single soft-gluon emission from a colour-singlet pair: dw^(1) = (α_s C_i/π)[dx dθ²/(xθ²) Θ(x−x̄) + (p ↔ p̄)]. This differs from QED only by the Casimir C_i (Eqs. 3.26–3.27).
- Insertion operator I_1 = −g_s² J^(1)·J^(1) with J^μ(q_1) = Σ_i T_i(q_i^μ/q_i·q_1 − n^μ/n·q_1) (Eq. 3.29). It is gauge invariant because Σ T_i |M⟩ = 0 (colour conservation, Eq. 3.25; p. 218). Repeated insertions must respect the non-commutativity of the colour charges (Eq. 3.32).
- **Single-emission factorization:** when q_1 is at large angle to all harder partons, J^(1) ≈ T_Jet(p/p·q_1 − p̄/p̄·q_1). The emission probability is then α_s (2p·p̄)/((p·q_1)(p̄·q_1)) T²_Jet times the (N−1)-gluon cross section (Eqs. 3.33–3.34′). T²_Jet = C_i when all soft gluons come from one parent (p. 220–221).
- **Multiple-emission factorization:** if the angular factors ζ_i = q_i·p_Jet/|q_i||p_Jet| are strongly ordered, dσ = ∏(α_s dφ_i/π z_i² ζ_i) dσ_Jet ⟨(T²_Jet)^n⟩, for any relative ordering of angles and momenta. Some orderings need the colour algebra of ref. [20] (Eq. 3.35, Fig. 3.5b).
- **Two soft gluons from a gg singlet:** the intermediate expression contains explicit T_3·T_4/N_c colour-correlation terms. Using T_3·T_4 = −N_c/2 gives the fully symmetric W = ½ζ_34²[(ζ_12ζ_23ζ_34ζ_41)^{-1} + (ζ_12ζ_24ζ_43ζ_31)^{-1} + (ζ_13ζ_32ζ_24ζ_41)^{-1}]. Each term is a closed chain of nearest-neighbour links, with (N+1)!/2 inequivalent terms in general (Eqs. 3.39–3.40, Fig. 3.6).
- **Limits of the two-gluon result:** with one gluon in each jet cone it factorizes into independent emissions, W ≈ (ζ_1p ζ_2p̄)^{-1} (Eq. 3.41). With both gluons in the same cone it keeps non-trivial correlations, W ≈ ½[(ζ_12ζ_23)^{-1} + (ζ_31ζ_12)^{-1} + (ζ_23ζ_31)^{-1}] (Eq. 3.42).
- **N-gluon generalization:** dw/dφ_1⋯dφ_N = (α_s N_c/π)^N (ω_1²⋯ω_N²)^{-1} W with W = 2^{-(N−1)} ζ²_{pp̄} Σ′_perm (ζ_{i1i2}⋯ζ_{iN+2,i1})^{-1} (Eqs. 3.43a,b). The argument rests on Bose symmetry, and the colour algebra is shown only for the leading chain: Eq. 3.45 is written with "+ ⋯" omitted terms (p. 222–223). The review does not state explicitly whether Eq. 3.43 is exact in N_c for N ≥ 3. It cites an explicit three-loop result [27] (Catani thesis; Catani–Ciafaloni preprint) that "closely parallels" the two-gluon result, Eqs. 3.39–3.40 (p. 222).
- **Angular ordering, second order:** the box diagram (Eq. 5.12) allows the non-angular-ordered region (x_2/x_1)ζ_23 > ζ_12 > ζ_23. The azimuthally averaged crossed diagram gives −Θ(ζ_12 − ζ_23) and cancels exactly that region (Eqs. 5.13–5.14). Their sum reproduces the two-loop γ^(2) (Eq. 5.15). The ladder (box) alone is off by a factor 2, which explains the discrepancy between Eq. 5.4 and Eq. 5.1 (p. 239).
- **Angular ordering, all orders:** the cancellation generalizes to all orders, leaving θ_12 ≪ θ_23 ≪ ⋯ for x_1 ≪ x_2 ≪ ⋯ (Eq. 5.17, ref. [38] = Bassetto–Ciafaloni–Marchesini–Mueller). The physical argument: a large-angle softest gluon sees only the total charge, so it factorizes and gives no leading logs (Eq. 5.18, p. 239).
- **Branching kinematics:** virtuality ordering alone, k′² < zk², allows ζ < ζ′ < ζ/z; interference removes this region, leaving ζ′ < ζ (Eqs. 6.4–6.6, p. 243). The modified vertex is Eq. 6.7, and the form factor with the angular constraint (Eq. 6.9) reproduces the Sudakov form factor F^a to LLD accuracy, because of a factor ½ in the leading logs (Eq. 6.11, p. 244).
- **Gauge invariance:** angular ordering allows a gauge-invariant definition of the two e⁺e⁻ jets, which the earlier tree (ladder) model in physical gauges did not (p. 244 and footnote).
- **Soft-limit evolution:** from the chain formula (Eq. 6.12) the authors derive the evolution equation in ζ for the generating functional (Eqs. 6.15–6.22). Adding virtual corrections gives Eq. 6.26 and its integral form Eq. 6.27, i.e. a coherent branching algorithm.
- **No leading correlations between jets:** to double-log accuracy, jets emitted in different angular regions are uncorrelated, so G_{e⁺e⁻} = G_q · G_q̄ (Eq. 6.28). The authors note that subleading (single-log) correlations exist and "may affect the details" (p. 247, ref. [26]). The unintegrated k_⊥ version (Eq. 6.29, from refs. [37, 39]) does not reduce to a function of E²ζ alone, because azimuthal integrations do not decouple (p. 248).

**Interjet / wide-angle effects (RQ 1b)**
- Jets formed at wide relative angle have only single-log soft-gluon correlations, not double-log ones (ref. [26], Mukhi–Sterman). Therefore "single jet events are well defined, i.e., less contaminated by a soft tail than it was thought before" (p. 270).
- DIS: initial- and final-state jets factorize in the Breit frame. Their multiplicities match e⁺e⁻ jets asymptotically, apart from phase-space rescaling (Eqs. 7.8–7.9, p. 261). The authors attribute the absence of leading multiplicity correlations between oppositely directed jets to angular ordering (p. 261).
- Footnote, p. 261: extending this to many-jet events has "intrinsic limitations" because overlap regions are frame dependent, owing to single-log correlations.
- The review contains no string/drag effect or three-jet interjet-asymmetry discussion. I searched the text for "string", "interjet", "three-jet" and "asymmetr" and found no such section.

**Multiplicity and hump-backed plateau (RQ 2)**
- γ^S_N = −(N−1)/4 + [((N−1)/4)² + ½ᾱ_s]^{1/2} → √(ᾱ_s/2) as N → 1 (Eq. 5.7). This is smaller by 1/√2 than the ladder-with-phase-space result (Eq. 5.4).
- ⟨n_g(Q²)⟩ ∝ (log)^{C_1/b} exp[√(2N_c/πb)(√log(Q²/Λ²) − √log(Q_0²/Λ²))] (Eq. 5.8). The qq̄-pair to gluon ratio is ⟨n_q̄⟩/⟨n_g⟩ = (N_F/6N_c)(N_cα_s(Q_0²)/π)^{1/2} (Eq. 5.9).
- The full e⁺e⁻ multiplicity is twice the single-jet result, because angular ordering confines counting to one hemisphere per jet (p. 240).
- **Subleading coefficient:** C_1 = (1/12π)[111/4 − (43/18) N_F] > 0 (Eq. 5.27, from Mueller [41]). It gives a (log Q²)^{K_1} prefactor of order 1 for N_F = 4. K_0 = (2N_c/πb)^{1/2} ≈ 1.7 and K_1 = C_1/b ≈ 0.73 (Eq. 8.4).
- **Hump-backed plateau:** xD(x,Q²) = [n(Q²)/n(Q_0²)](πΔ)^{-1/2} exp[−(1/Δ)(log(1/x) − log√(Q/Q_0))²] with Δ = (1/6)√(πb/2N_c)(log Q²/Λ²)^{3/2} (Eq. 5.26). It peaks at x = (Q_0/Q)^{1/2} and is depleted toward x = Q_0/Q.
- **Peak shift:** subleading terms move the peak toward small x by Δ(log 1/x)_max = C′_1(πb/2N_c · log Q²/Λ²)^{1/2}, with C′_1 = (1/12π)(11N_c − 2C_F N_F/N_c) (Eqs. 5.28–5.29). This is of relative order √α_s and "may contribute … to make the experimental detection of the dip more difficult" (p. 242).
- **MC comparison (pure gluon jet, Q = 100 and 1000 GeV):**
  - Coherent branching gives x dσ/dx peaking near √(Q_0/Q) (Fig. 6.5). In rapidity, dσ/dy peaks near |y| ≈ 1 and falls toward |y| ≈ 5 (Fig. 6.6).
  - The conventional non-coherent branching peaks in the soft region x ≈ Q_0/Q instead (Fig. 6.7; p. 257).
  - The asymptotic multiplicity Eq. 5.8 is in "fairly good agreement" with the MC at accessible energies. Non-leading terms still matter for multiplicity moments, so KNO is "not yet set up" (p. 258).
- **Multiplicity distributions:** the generating function obeys d²log G/ds² = G − 1 with s = (N_cα_s/2π)^{1/2} log(2E²ζ/Q_0²) (Eqs. 6.30–6.31), giving ⟨n⟩ = cosh s (Eq. 6.33). There is approximate KNO scaling (Eq. 6.36) and a soliton solution (Eqs. 6.40–6.42, Fig. 6.2). The low-multiplicity tail is σ_n/σ_Jet ≈ (1/⟨n⟩) exp[−½(log(n/⟨n⟩))²] (Eq. 6.44).
- **Dispersions:** c_2 = D²/⟨n⟩² ≈ 1/3 for a gluon jet (Eq. 6.45) and ≈ 3/4 for a quark jet (Eq. 6.47). Corrections are O(√α_s) (p. 251).

**Colour structure, preconfinement, cluster masses (RQ 2)**
- In the angular-ordered region only planar diagrams contribute, so a large-N_c (colour-line) description is used (Fig. 6.3; p. 251).
- Definitions: two gluons are "close in colour" if their colour lines are connected only through virtual gluons. A qq̄ pair is "colour connected" if their colour lines are connected at most through emitted gluons; such a pair defines a minimal "colourless cluster" (p. 251).
- The probability ψ that a gluon stays close in colour to its parent obeys an AP-like equation with a factor ½ in real emission (Eq. 6.48). Its solution is tied to the Sudakov form factor (Eq. 6.49) and satisfies ∫ψ dx = 1 (Eq. 6.50). The result is ⟨x⟩_colour ≈ Q_0/k (Eq. 6.51): colour screening is fast and soft.
- The two-gluon "close in colour" mass spectrum is M² dσ/dM² ≈ F²(M², Q_0²) (Eqs. 6.52–6.55, Fig. 6.4). This is Sudakov-damped, i.e. preconfinement.
- **Colourless qq̄ clusters:** roughly 6(N_c/N_F)(N_cα_s(Q_0²)/π)^{-1/2} ≈ 3–6 gluons per qq̄ pair, and a perturbative ⟨M⟩ ≈ 10 GeV for (1/π)α_s(Q_0²) = ½. Clusters are "rather large objects" with important subasymptotic terms for central clusters (p. 254). Remedies suggested: enhance g → qq̄ by hand, or allow non-singlet clusters plus a local colour interaction (p. 254–255). This anticipates the forced g → qq̄ splitting in cluster models.
- **MC cluster masses (Fig. 6.8):** ⟨ln M⟩ (M in GeV) for general colour-connected clusters is ≈ 0–0.1 and roughly Q-independent at large Q (band a). For the "central" cluster that "screens the colour between quarks in opposite cones" it rises from ≈ 0.15–0.55 at Q = 10 GeV to ≈ 0.5–0.75 at Q = 10⁴ GeV and is still rising slowly (band b). The authors say this answers Bjorken's [48] criticism (p. 258). Values were read off the figure and are approximate.

**Form factors and resolutions (context; possible RQ 4 observables)**
- Back-to-back energy correlation in DLA: σ^{-1}dσ/dη ≈ (α_sC_F/π)(1/η) log(1/η) exp[−(α_sC_F/2π) log²η] (Eq. 4.28). There is an impact-parameter form (Eqs. 4.29–4.34); the LLD description of data is "reasonable", but subleading terms worsen it at present energies (p. 232).
- **Single-cone Sterman–Weinberg f_1:** f_1 = exp[−(C_Fα_s/π)(log ε log δ² + ½ log²ε)] (Eq. 4.41). The extra log²ε comes from backward-hemisphere gluons leaking energy into the forward measurement (Eqs. 4.42–4.43, Fig. 4.5, ref. [33] Curci–Greco).
- **Double-cone f_2:** f_2 = (f_1^{(a)})², with no log²ε term (Eqs. 4.44–4.45).

**Proposed tests (RQ 4; Sec. 8)**
- Multiplicity growth n_jet(Q²) per Eq. 8.3. e⁺e⁻ [61] and Drell–Yan [62] data are roughly consistent, but "a precise check would require a wider range in log Q²" (p. 269).
- Small-x depletion relative to phase-space expectation. Hadronization and subleading terms may fill the dip, so one should look for a depletion rather than the dip itself. A hint is seen in "low rapidity e⁺e⁻ data [63]". The authors suggest checking "higher energy p–p̄ collider jets" (p. 269–270).
- KNO scaling and dispersion values (Eqs. 6.45, 6.47), with sizeable O(√α_s) corrections (p. 270).
- Single- and double-cone (calorimetric, energy-flow) form factors as checks less sensitive to intrinsic p_⊥ (Sec. 4.3.2; p. 268). The authors say this "remains still to be done" (p. 268).
- Coherent MC plus a cluster-hadronization model, as "an indirect, but detailed test of QCD calculations" (p. 270).

## Assessment
- **Why it matters.** This is the most complete 1983 exposition of the Italian-school derivation of soft-gluon coherence. It runs in parallel to Dokshitzer–Fadin–Khoze [39] and Ermolaev–Fadin [37], and it provides the theoretical basis of the Marchesini–Webber coherent shower ([42], later HERWIG).
- **Key content for the review.**
  - The colour-operator formalism (Eq. 3.29) and the factorization theorems (Eqs. 3.33–3.35) state cleanly why large-angle soft radiation sees only the coherent total charge.
  - The closed-chain formula (Eqs. 3.40, 3.43) is in effect the strongly-ordered dipole/antenna factorization. It is the conceptual root of colour-connected (dipole) emission, and hence of the colour-flow observables of RQ 1b.
- **Limitations.**
  - Everything is LLD/double-log, strongly ordered, and either uses a colour-singlet gg source or is planar (large-N_c) for the colour-structure discussion.
  - Virtual corrections are added by the (1−z)₊ recipe rather than derived (p. 247).
  - The N-gluon chain formula's colour exactness is not demonstrated in the text (ellipses in Eq. 3.45). It should be checked against Catani–Ciafaloni/Catani's thesis [27] or BCMM [20/38] before being cited as an exact-colour statement. The two-gluon case (Eq. 3.40) is shown explicitly.
- **Interjet effects.** Multi-jet interference (the string/drag effect in qq̄g) is not treated: the e⁺e⁻ discussion is two-jet only. The single-log interjet correlations are only mentioned and referred to Mukhi–Sterman [26]. For RQ 1b this review is background, not a source. The interjet soft-gluon antenna pattern for qq̄g came later (Azimov–Dokshitzer–Khoze–Troyan 1985, already in the queue as "The String Effect and QCD Coherence").
- **Monte Carlo results.** Figs. 6.5–6.8 come from ref. [42], a then-unpublished preprint. Their numbers are quoted here only qualitatively, and cluster-mass bands were read off a plot.
- **Proposed tests.** All are 1983-era. The small-x depletion (hump-backed plateau) was later tested at LEP (see OPAL_1990vmr; contested by Boudinov_1993mc) [outside this paper]; the review itself has no data comparison for it beyond the hint in [63].
- **Planar colour picture.** The "close in colour" / colourless-cluster construction is the leading-N_c colour-flow assignment that colour-reconnection models later perturb (relevant to RQ 2).

## Leads
- A. Bassetto, M. Ciafaloni, G. Marchesini, A.H. Mueller, "Jet Multiplicity and Soft Gluon Factorization", Nucl. Phys. B207 (1982) 189 [refs 20, 38]. Already queued as Bassetto:1982ma. It is the primary all-orders proof of angular ordering and of the factorization theorems (Eqs. 3.35, 5.17) and should be prioritized.
- Yu.L. Dokshitzer, V.S. Fadin, V.A. Khoze, Z. Phys. C15 (1983) 325 and C18 (1983) 37 [ref 39]. These are the independent coherent-cascade derivation, the k_⊥-unintegrated equation (Eq. 6.29) and the hump-backed plateau. Check the DB: Dokshitzer:1982fh was rejected as a near-duplicate of Dokshitzer:1982xr, so make sure one of the two is queued. Dokshitzer:1982ia (sensitivity of inclusive distributions to coherence) is queued.
- B.I. Ermolaev, V.S. Fadin, JETP Lett. 33 (1981) 269 [ref 37]. The original angular-ordering derivation; already queued (Ermolaev:1981cm).
- A.H. Mueller, Phys. Lett. B104 (1981) 161 [ref 36] and Nucl. Phys. B213 (1983) 85 [ref 41]. The first gives the second-order cancellation of non-ordered regions by crossed diagrams; the second gives the next-to-leading multiplicity coefficient C_1 and the plateau peak shift.
- G. Marchesini, B.R. Webber, CERN TH-3525 (1983) [ref 42], published as "Simulation of QCD Jets Including Soft Gluon Interference", Nucl. Phys. B238 (1984) 1 [from the INSPIRE record Marchesini:1983bm, DOI 10.1016/0550-3213(84)90463-2; not stated in this paper]. This is the MC behind Figs. 6.5–6.8 and is already queued (Marchesini:1983bm).
- S. Catani, Univ. of Florence thesis (1983), and S. Catani, M. Ciafaloni, Florence preprint DFF-71/83 [ref 27]. They contain the explicit three-soft-gluon (three-loop) emission result and would settle the colour exactness of the chain formula (Eq. 3.43). Probably published as Catani–Ciafaloni, Nucl. Phys. B236 (1984) 61, "Many gluon correlations and the quark form-factor in QCD"; this attribution has not been checked.
- S. Mukhi, G. Sterman, Nucl. Phys. B206 (1982) 221, and A. Sen, Stony Brook ITP-SB-81-19 (1981) [ref 26]. These cover single-log soft correlations between wide-angle jets, directly relevant to interjet coherence (RQ 1b).
- J.D. Bjorken, Fermilab-Conf-82/42-THY (1982) [ref 48]. A criticism of the perturbative "central cluster" and colour screening between opposite hemispheres, relevant to the colour-flow and CR context.
- S. Bertolini, G. Marchesini, Phys. Lett. B117 (1982) 449 [ref 47]. Perturbative colour-singlet cluster mass; Bertolini:1982em is in the DB, so check its status.
- B.R. Webber, Moriond 1983 talk, CERN TH-3569 (1983) [ref 63]. The first hint of small-x depletion in low-rapidity e⁺e⁻ data (RQ 3 and 4, early evidence for coherence).
- G. Curci, M. Greco, Phys. Lett. B102 (1981) 280 [ref 33]. The single-cone Sterman–Weinberg log²ε term (Eq. 4.41), an early "non-global-like" soft log from out-of-cone emission; low priority.
- K. Konishi, A. Ukawa, G. Veneziano, Nucl. Phys. B157 (1979) 45 [ref 14]. Jet calculus and the KNO dispersion; low priority, as context only.
