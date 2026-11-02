# QCD coherence studies using two particle azimuthal correlations
- **ID / links:** OPAL:1992lzb · INSPIRE 343082 · arXiv — · DOI 10.1007/BF01560339
- **Authors / collab, year, journal:** OPAL Collaboration (P.D. Acton et al.), 1993, Z. Phys. C 58 (1993) 207–217
- **Type:** experimental
- **Relevance:** 3 · RQs: 1a, 1b, 2, 3
- **Full text source:** zotero

## Takeaways
- The paper tests soft-gluon interference with two-particle azimuthal correlations at the Z⁰, using two observables:
  - the Dokshitzer et al. energy-multiplicity-multiplicity correlation (EMMC), which needs no event axis or jet selection;
  - two-particle azimuthal correlations (TPAC) in 2-jet events about the sphericity axis.
- The leading-order QCD expectation (Eq. 2) is that, for two soft gluons at similar rapidity, emission back-to-back in azimuth is suppressed, by a factor 7/16 relative to φ = π/2 at η₃₄ ≈ 0. The authors say this has "the same dynamical origin as the string effect" (p. 208).
- Measured EMMC at φ = π: C(π) = 0.787 ± 0.002 ± 0.04 (p. 213). This is well above LO (7/16 ≈ 0.44) and below the higher-order estimate ≈ 0.93. The authors cite ref. [8] for an argument that further higher orders lower that by ≈ 10 %, to ≈ 0.8 (p. 209, 213).
- Models were all tuned to OPAL global event shapes. Coherent ones (Jetset J1/J2 with angular ordering, Herwig 5.0, Ariadne 3.1) describe both observables. Incoherent ones fail:
  - Jetset incoherent shower + string (J3) and Cojets 6.20 (incoherent + IF) are ≈ 0.08 too high in EMMC over the whole φ range, 2–3σ for φ > 1 (Fig. 1b, p. 214).
  - In TPAC they are 3.7σ / 5.0σ (0 < |η₁| < 1) and 4.4σ / 5.2σ (1 < |η₁| < 2) away, averaged over φ > 1 (Fig. 2, p. 214).
  - Cojets 6.12 has the wrong shape.
- The key logical step: J3 uses the same string hadronization as J1 but fails. The authors conclude that "string hadronisation alone is not able to reproduce the observed correlations" and that coherence in the shower is needed (p. 214, 216). This directly addresses the loophole left by the ξ-peak test (OPAL:1990vmr, Boudinov:1993mc).
- Caveats from the authors' own MC study:
  - Hadronization strongly distorts φ < π/2. Momentum conservation produces φ ≈ π correlations.
  - The analysis method itself depopulates φ ≈ π.
  - J1 (no azimuthal asymmetry in g→gg) and J2 (with it) differ at parton level but are nearly identical at hadron level (p. 216).
  - The quantitatively interpretable region is 0 < |η₁| < 1, φ > π/2 (p. 216).

## Setup
- Data and selection (p. 208–209):
  - LEP1, OPAL, ≈ 146 900 hadronic Z⁰ decays, ≈ 6.5 pb⁻¹, ⟨√s⟩ = 91.3 GeV.
  - Charged tracks with p_T to the beam > 150 MeV/c and ≥ 40 space points; ECAL clusters > 200 MeV spanning ≥ 2 blocks and not associated to tracks.
  - ≥ 5 tracks, |cos θ_thrust| < 0.9, |cos θ_sph| < 0.875, charged energy 20–100 GeV. About 114 000 events pass.
  - TPAC additionally requires 2 jets (E0 scheme, y_cut = 0.05), leaving ≈ 77 500 events (p. 209).
- Theory (p. 208):
  - qq̄gg with one soft gluon factorizes, σ(q₁q̄₂g₃g₄) = σ(q₁q̄₂g₃)σ(q₁q̄₂g₄)C/σ(q₁q̄₂), with the correlation term C of Eq. 1 (from the ξ_ij = 1 − cos θ_ij antennae).
  - For collinear qq̄, Eq. 2 gives C = 1 + N²/(N²−1)·cos φ₃₄/(cosh η₃₄ − cos φ₃₄).
- Observables:
  - dC/dφ(η₁, η₂, φ) = σ dσ/dη₁dη₂dφ / (dσ/dη₁ · dσ/dη₂) (Eq. 3).
  - EMMC: each particle in turn defines the axis. Both other particles must lie in 1 < η < 2 relative to it, and each pair is weighted by the axis particle's energy. φ ∈ [0, π] (p. 209).
  - TPAC: the sphericity axis is used, with η₁₂ = η₂ − η₁ fixed (Eq. 4). Bins 0 < |η₁| < 1 and 1 < |η₁| < 2, both with 0 < |η₁₂| < 1 (p. 209).
- Corrections: bin-by-bin to hadron level (π⁰, K⁰_S and hyperons stable) with Jetset 7.2 + detector simulation (111 000 / 75 000 MC events). Correction factors are within 10 % of 1 over most φ (p. 209, 211).
- Errors (p. 211–212):
  - Statistical, from 10 subsamples: < 0.006 (EMMC), < 0.015 (TPAC).
  - Detector systematics, from charged-only vs neutral-only comparison: EMMC < 0.02 except φ < 0.6, where they reach 0.10; TPAC ≈ 0.04 average.
  - Correction-model systematics, the larger of two estimates:
    - Herwig 5.0 corrections: 0.016 (EMMC), 0.020 (TPAC).
    - Cojets 6.12 corrections: 0.026 (EMMC), 0.040 (TPAC).
  - Total for φ > 1: 0.03 (EMMC), 0.05 / 0.04 (TPAC, two η regions). Tab. 1 lists all corrected values.
- Models, all tuned to OPAL data (Tab. 2, p. 212–213):
  - Jetset 7.2 (string fragmentation):
    - J1: coherent shower with angular ordering and no azimuthal asymmetry, MSTJ(42,44,46) = 2,2,0.
    - J2: as J1 plus azimuthal asymmetry in gluon decay, 2,2,2.
    - J3: incoherent shower, 1,1,0, retuned by the authors: Λ = 0.44 ± 0.06 GeV, Q₀ = 1.45 GeV.
  - Ariadne 3.1: colour dipoles + string.
  - Herwig 5.0: angular ordering + azimuthal asymmetry + cluster hadronization.
  - Cojets 6.12 and 6.20: incoherent shower + IF, Λ = 0.17 GeV, Q₀ = 3.0 GeV. 6.20 was retuned (by Mazzanti–Odorico) to fit the LEP string-effect and q/g jet differences.
  - Incoherent-model parameter errors come from a χ² fit to thrust, thrust major, sphericity, aplanarity, the second Fox–Wolfram moment and the 1/x spectrum. Their ±1σ variation defines the bands in Figs. 1–2.

## Results
- **EMMC** (Fig. 1a, Tab. 1, p. 213):
  - A strong peak at φ ≈ 0, dC/dφ = 3.126 ± 0.006 ± 0.126 in the first bin, falling below 1 towards π.
  - C(π) = 0.787 ± 0.002 ± 0.04 (last bin of Tab. 1).
  - All models reproduce the global shape, which is partly an artefact of the method (p. 213): taking each particle as axis creates small-φ correlations and depopulates φ ≈ π even for back-to-back qq̄ without gluons.
- **Model values at φ = π:** Ariadne 0.786 (good agreement); coherent models (J1, J2, Herwig) about 0.80; incoherent models about 0.85 (p. 213).
- **Differences from data** (Fig. 1b, p. 214):
  - Coherent models: Jetset/Ariadne are slightly low at small φ, Herwig slightly high, all within systematics. At φ ≈ π Jetset and Herwig are slightly high.
  - J3 and Cojets 6.20: ≈ 0.080 above the data at all φ, 2–3σ for φ > 1.
  - Cojets 6.12: the difference varies linearly from −0.1 at φ = 0 to ≈ +0.1 at φ = π.
- **TPAC** (Fig. 2, Tab. 1, p. 214):
  - Coherent models are much closer to the data than incoherent ones. Ariadne describes φ > 1 better than Jetset J1/J2 or Herwig. Ariadne is best at φ ≈ π.
  - J3 and Cojets 6.20 agree near φ ≈ 0 but lie above the data elsewhere. At φ = π they are > 4σ high.
  - Averaged over φ > 1, the deviations of J3 and Cojets 6.20 are 3.7σ and 5.0σ (0 < |η₁| < 1) and 4.4σ and 5.2σ (1 < |η₁| < 2).
  - Cojets 6.12 shows the same trend as in EMMC.
  - J3 and Cojets 6.20 give very similar predictions despite different hadronization. Cojets 6.12 and 6.20 differ in shape yet are similar at φ ≈ π.
- **Stability checks** (p. 214):
  - Bose–Einstein correlations (Jetset BE with OPAL parameters) are negligible at hadron level.
  - Changing y_cut from 0.05 to 0.03 leaves the J1–J3 differences in place "at a slightly reduced level".
  - Randomly dropping 20 % of particles changes TPAC by < 0.1 %.
- **Sensitivity:** TPAC is more sensitive than EMMC for φ > 1 (p. 214, 216).
- **Parton level** (Figs. 3–4, p. 214–216):
  - J3 parton TPAC is clearly flatter than the coherent models. In the coherent models (J1, J2, Ariadne, Herwig) the parton TPAC lies below J3 for φ > π/2 in 0 < |η₁| < 1, as Eq. 2 expects (Fig. 3a,b).
  - The cutoff suppresses φ < 1 at parton level. Momentum balance in q₁q̄₂g₃ topologies creates φ ≈ π correlations, especially in 1 < |η₁| < 2 (Fig. 3c,d).
  - Parton EMMC falls to ≈ 0.8 at φ ≈ π for the coherent models, while J3 stays above 1 (Fig. 4a).
  - Cojets is not shown at parton level: its large cutoff leaves only ≈ 3.25 partons per event, so momentum-conservation distortions dominate (p. 216).
- **Hadronization** (p. 216):
  - In 0 < |η₁| < 1, φ > π/2, the parton- and hadron-level orderings of J1, J2, J3, Herwig and Ariadne are preserved. The one exception is J2, which is above Ariadne at hadron level but below it at parton level.
  - The two Cojets versions (same shower, different IF) differ in hadronic shape, which shows that hadronization can strongly distort the parton correlations.
  - J1 and J2 differ at parton level but agree at hadron level. The authors attribute this to the non-local string. Their conclusion is that hadron-level correlations are sensitive to the global parton topology but not to its details.
- **Authors' conclusion** (p. 216): the correlations "clearly favour" models with interference in the shower, although all models describe global Z⁰ event properties. Coherence "is relevant to the measured distributions". For φ > π/2 the data "reflect the analytic QCD expectations".

## Assessment
- This is the stronger of the two OPAL coherence tests. Compared with the ξ-peak slope (OPAL:1990vmr), where incoherent + string was only ≈ 2.8σ off and ≈ 1σ worse than coherent Ariadne, here the same class of model (J3) fails at 3.7–4.4σ in TPAC with the same string hadronization. This undercuts the specific mechanism invoked by Boudinov:1993mc (string fragmentation washes out shower coherence), at least for this observable.
- The deviations are bin-averaged and the systematic errors are correlated across φ bins. Our view is that the quoted "σ" figures should be read as indicative, not as proper χ² significances; the paper gives no covariance.
- J3 is an incoherent shower with a large cutoff (Q₀ = 1.45 GeV) and a high Λ (0.44 GeV) (Tab. 2). Its parton cascade differs from the coherent one in more than angular ordering (fewer, harder partons [unverified: inferred from the larger Q₀; the paper gives no parton multiplicity for J3, and p. 214 calls the Jetset mean parton multiplicity "large"]), so a failure of J3 does not uniquely isolate interference. Cojets has only ≈ 3.25 partons per event (p. 216). The comparison is "angular-ordered shower vs. a specific tuned incoherent shower", not a pure on/off switch of interference. The authors do not address this directly; their nearest remark is that Jetset's large mean parton multiplicity is "perhaps making the details of the hadronisation model less important" (p. 214).
- J1 ≈ J2 at hadron level (p. 216): the azimuthal-asymmetry part of coherence is invisible after string hadronization. The test therefore probes angular ordering / global parton topology rather than the full soft-gluon interference structure of Eq. 1.
- C(π) = 0.787 is far from LO 7/16. Agreement with the higher-order "≈ 0.8" relies on an argued ≈ 10 % correction (ref. [8]) and on LPHD. At φ ≈ π the method itself and momentum conservation also push the value below 1 (p. 213, 216). So the absolute number is not a clean coherence measurement; only model-to-model discrimination is.
- Comparison:
  - Complements OPAL:1990vmr. It answers the "string mimics coherence" critique better than the ξ slope does, but leaves "an incoherent shower with a different cutoff/tune" as a possible loophole.
  - Boudinov:1993mc does not discuss this paper (published the same year), and its argument is confined to momentum spectra.
  - Conceptually tied to the interjet string effect (OPAL_1991xwi), where Cojets also fails (R̃ ≈ 1.02).

## Leads
- Yu.L. Dokshitzer et al., Phys. Lett. B 245 (1990) 243 (co-authors not listed in this paper): the EMMC proposal (ref. [6]). Theory paper defining the observable (RQ 2/4).
- Yu.L. Dokshitzer, G. Marchesini, G. Oriani, Lund preprint LUTP 92/19 (1992): higher-order EMMC calculation (C(π) ≈ 0.93, argued to drop to ≈ 0.8). Needed to judge the absolute comparison. Look up the published version.
- OPAL, P.D. Acton et al., Phys. Lett. B 287 (1992) 401: two-particle momentum correlations (ref. [20]), described as giving similar model discrimination (Ariadne best). A companion coherence test.
- P. Mazzanti, R. Odorico, Nucl. Phys. B 370 (1992) 23 and Bologna preprint DFUB 92/1: the Cojets retune to LEP string-effect/q-g data. It is also the incoherent-IF ξ fit that Boudinov et al. rely on (their ref. [32]).
- Ya.I. Azimov et al., Phys. Lett. B 165 (1985) 147: interference interpretation of the string effect (ref. [5]).
- L3, B. Adeva et al., Phys. Lett. B 259 (1991) 199: cited with OPAL:1990vmr as coherence evidence from spectra.
- Forward: later LEP azimuthal-correlation / EMMC measurements (e.g. by DELPHI or ALEPH) and theory follow-ups. Use `citing 343082`.
