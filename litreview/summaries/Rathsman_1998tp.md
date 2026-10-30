# A Generalised Area Law for Hadronic String Reinteractions
- **ID / links:** Rathsman:1998tp · INSPIRE 481076 · arXiv hep-ph/9812423 · DOI 10.1016/S0370-2693(99)00291-9
- **Authors / collab, year, journal:** J. Rathsman (SLAC), 1999, Phys. Lett. B (SLAC-PUB-8034-Rev)
- **Type:** MC/model
- **Relevance:** 3 · RQs: 1b, 2, 3, 4
- **Full text source:** arxiv

## Takeaways
- Proposes the "generalised area law" (GAL) string-reinteraction model. Any two string pieces may swap partners with probability P = R0[1 − exp(−bΔA)], where ΔA = A_old − A_new is the decrease in Lund string area (Eq. 2). It is a dynamical extension of the SCI model, which uses a constant probability.
- A single parameter, R0 = 0.1 (≈ 1/N_C^2 colour suppression), is fixed by HERA diffractive DIS. The same model, with b and Q0 retuned, reproduces default-Jetset LEP1 charged multiplicity and momentum spectra, the string effect, and the gap distribution up to Δy ≈ 4 to within a few percent (pp. 3–7); event shapes are not shown. It is an early "universal" CR model applied to e+e-, DIS and WW, but WW is a prediction only, with no data comparison.
- Predicts a W-mass shift Δm_W = +65 ± 15 MeV (stat.) at √s = 183 GeV (Fig. 5a) and Δ⟨n_ch⟩ = −0.4 in fully hadronic WW (Fig. 5b).
- Proposed e+e- test: an enhanced tail of the largest rapidity gap Δy_π,max at Z ("as large as a factor 2" for Δy > 6, p. 6, Fig. 3b), with no plateau, only a gradually flattening exponential slope (pp. 6–7). The string effect is changed by less than a few percent (Fig. 3a).
- Physics motivation: the strings' colour fields (octet-carrying) interact, not the endpoint charges. Rearrangements that lower the area are favoured, the string-area analogue of λ/cluster-mass minimisation (p. 3).

## Setup
- Area of a string piece between partons i and j: A_ij = (p_i + p_j)^2 − (m_i + m_j)^2 = 2(p_i·p_j − m_i m_j). This reduces to the Lund area (E+|p_z|)^2 in the CM frame (p. 2). For two q q̄ strings, A_old = A12 + A34 and A_new = A14 + A23 (Fig. 1).
- Relative weight from the area law: [exp(−bA_new) − exp(−bA_old)]/exp(−bA_new) = 1 − exp(−bΔA) (Eq. 1), times a colour-matching factor R0 ~ 1/N_C^2 (Eq. 2). The implementation loops over all pairs of string pieces, as in SCI. Order dependence is neglected because P is small (p. 4).
- e+e- → Z: Jetset 7.4. Retuned to b = 0.45 GeV^-2 and shower cut-off Q0 = 2 GeV to reproduce the default-Jetset ⟨n_ch⟩ = 20.9 and D = 6.2 (p. 4). Compared to ALEPH multiplicity and OPAL π± momentum data (Fig. 2). Default Jetset is used as the reference: differences below a few percent are deemed satisfactory (p. 4).
- String effect: JADE y_cut = 0.05 three-jet events, particle flow vs angle ω in the event plane (Fig. 3a). Rapidity gaps: largest gap in y_π along the thrust axis, n_ch ≥ 7, cf. SLD measurement (Fig. 3b).
- DIS: Lepto 6.5 with CTEQ4L, the same Q0 and b, and SCI sea-quark treatment v2. Compared to the H1 F2^D(3)(Q², β, x_P) via HzTool (Fig. 4, p. 7).
- WW: Pythia 5.7 at √s = 183 GeV, fully hadronic, JADE y_cut = 0.015, four-jet events. The Breit–Wigner plus constant fit to dijet mass is compared with default Pythia (Fig. 5).

## Results
- **LEP1 tune:** after retuning, the multiplicity distribution agrees with default Jetset to within a few % for 12 ≲ n_ch ≲ 35, but is ≈15%+ above at n_ch < 10 and ≈10% below at n_ch ≈ 40–50 (≈, read from Fig. 2a, p. 5). Without retuning, the model differs strongly (Fig. 2a). For the π± momentum spectrum the retuned model is "actually closer to the data than the default version", with differences of a few percent, comparable to the data errors (Fig. 2b, p. 4). Identified-particle multiplicities are within ~1% of default (p. 4).
- **String effect:** the particle-flow ratio Model/Default stays within ≈±3% (≈, read from Fig. 3a; text: "below a few percent", p. 4). The model without the area suppression factor (P = R0) fills in the inter-quark depletion more (dotted curve, Fig. 3a). The area factor therefore preserves the string effect.
- **Rapidity gaps in e+e-:** the model and default agree for Δy_π,max < 4. The ratio grows to "as large as a factor 2" for Δy_π,max > 6 (p. 6; in the plot individual bins above Δy ≈ 6.5 exceed 2, ≈ read from Fig. 3b). The existing SLD data have errors of comparable size in that region, so they cannot discriminate (p. 6). There is no plateau, only a gradual decrease of the exponential slope (pp. 6–7).
- **Diffractive DIS:** with only R0 free, the agreement with H1 F2^D(3) is "very good" across Q² = 4.5–75 GeV² and β = 0.04–0.65. This covers both the small-x_P (Pomeron-like) and the 0.01 < x_P < 0.1 (Reggeon-like) regions (Fig. 4, p. 8; text p. 7). The model fails only at small M_X (large β, hatched in Fig. 4), which the M_X² > 4 GeV² matrix-element cut-off excludes (p. 7). Visually, the model also undershoots several β = 0.04 points (≈, read from Fig. 4).
- **W mass:** Δm_W = m_W^Model − m_W^Def = +65 ± 15 MeV (stat.) (Fig. 5a). This is about twice the anticipated LEP2 final statistical error (p. 9). Δ⟨n_ch⟩ = −0.4 with unchanged dispersion, and the thrust distribution is unchanged (Fig. 5b, p. 9). The author notes that the precise number depends on the analysis method.

## Assessment
- Conceptually important: an early CR model whose reconnection probability is tied to a measure of "string length" (area/λ). It is not the first: λ/area-based WW reconnection (Gustafson–Häkkinen 1994, Friberg–Gustafson–Häkkinen 1997, refs. [6,9]) predates it, and footnote 1 notes an earlier string-length version. It provides the bridge between SCI (constant probability, partons in a background field) and the later λ/cluster-mass-minimising schemes in Pythia/Herwig. The minimisation of A_ij = 2(p_i·p_j − m_i m_j) is essentially minimisation of the invariant mass of colour-connected pairs, i.e. the same quantity as Herwig's plain CR (cf. Gieseke:2012ft).
- The e+e- validation is weak. The model is compared mainly to default Jetset rather than tuned to data, and only multiplicity and the π± spectrum are shown. Event shapes, identified-hadron ratios and Bose–Einstein effects are not tested. The retuning (b = 0.45, Q0 = 2 GeV, unusually large) may absorb CR effects. Q0 = 2 GeV is far from the standard Jetset tune, so the agreement may partly come from the retuned shower.
- The DIS success is notable, since a single parameter describes F2^D(3), but it relies on the SCI sea-quark treatment and Lepto. The overall normalisation of gap events could be tuned with R0 alone. Inclusive DIS and photoproduction checks are not shown.
- The +65 MeV W-mass shift is model- and method-dependent. It falls in the range of other models of that era (SK-I/II, GH, Ariadne) [unverified: not compared in the paper]. LEP later excluded only very large CR (cf. the LEP-combined Δm_W, and the OPAL/L3 particle-flow measurements). Collinear/IR safety of the area measure and the energy (√s) dependence of R0 are not discussed.
- No hadron-collider (MPI) application. It was applied later in Rathsman's/Enberg–Ingelman–Timneanu work to Tevatron diffraction. It is relevant to RQ1b/4 as a template for "rapidity gaps from soft colour rearrangement".

## Leads
- Edin, Ingelman, Rathsman, PLB 366 (1996) 371 and Z. Phys. C75 (1997) 57: the original SCI model for rapidity gaps in DIS. It is the baseline this paper modifies.
- Gustafson, Pettersson, Zerwas, PLB 209 (1988) 90: first study of colour interference/reconnection in WW.
- Sjöstrand & Khoze, PRL 72 (1994) 28 and Z. Phys. C62 (1994) 281: SK-I/II CR models and the W-mass shift.
- Gustafson & Häkkinen, Z. Phys. C64 (1994) 659; Friberg, Gustafson, Häkkinen, NPB 490 (1997) 289: area/λ-based CR in WW.
- Lönnblad, Z. Phys. C70 (1996) 107: Ariadne CR model.
- Ellis & Geiger, PRD 54 (1996) 1967 and PLB 404 (1997) 230: parton-cascade CR estimates of the W-mass shift (large).
- SLD, PRL 76 (1996) 4886: rapidity-gap distribution in e+e- at the Z. This is the data that tests the model's predicted large-gap enhancement.
- Enberg, Ingelman, Timneanu (2001), "Soft color interactions and diffractive hard scattering at the Tevatron": GAL/SCI applied to hadron colliders.

## Verification
Checked 2026-10-30 by an independent reader: 40 claims checked, 6 corrected, 1 unverifiable.
- Takeaway overstated e+e- validation: the paper shows no event shapes, only multiplicity, momentum spectra, string effect and gaps, all vs default Jetset; WW is a prediction with no data comparison.
- Fig. 2a multiplicity agreement restated: few % only for 12 ≲ n_ch ≲ 35, ≈15%+ high below n_ch ≈ 10, ≈10% low at 40–50.
- Assessment "first CR model tied to string length" softened: λ/area-based GH/FGH models (refs. [6,9]) predate it.
- DIS quote corrected ("very good", not "very well"); Fig. 4 is on p. 8; Δm_W error noted as statistical.
- Plot read-offs (Figs. 2a, 3a, 3b, 4) marked ≈; comparison with SK/GH/Ariadne shifts marked [unverified].
