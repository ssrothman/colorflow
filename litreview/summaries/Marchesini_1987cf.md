# Monte Carlo Simulation of General Hard Processes with Coherent QCD Radiation
- **ID / links:** Marchesini:1987cf · INSPIRE 253353 · arXiv — · DOI 10.1016/0550-3213(88)90089-2
- **Authors / collab, year, journal:** G. Marchesini (Parma), B.R. Webber (Cambridge), 1988, Nucl. Phys. B310 (1988) 461–526
- **Type:** MC/model (with theory derivation)
- **Relevance:** 3 · RQs: 1a, 1b, 1d, 1e, 2, 3, 4
- **Full text source:** zotero

## Takeaways
- The HERWIG paper (version 2.2): extends angular-ordered coherent showers from e⁺e⁻ to **incoming partons** (DIS, Drell–Yan, hadron collisions). Shows that soft-gluon coherence in space-like branching restricts phase space to E_iθ_i < E_{i−1}θ_{i−1} (Eqs. 2, 7), implemented via backward evolution in Q_i = E√ξ_i (Eqs. 3–4, 37–39, 50–56), which interpolates between θ-ordering (soft, z→1) and p_T-ordering (x→0) (p. 469); only this ordering gives the correct inclusive IR cancellation/Sudakov factor (p. 466, Eqs. 44–46).
- **Colour flow → emission cones:** for every 2→2 QCD subprocess the soft-gluon radiation pattern is decomposed (Eqs. 66–73) into positive radiation functions W^i_ij, each confined to a cone around parton i bounded by its **colour-connected partner** j, weighted by planar colour-flow probabilities h_ij (Tabs. 1–3, Figs. 6–10). This covers initial–initial, initial–final and final–final interference at leading 1/N; the same colour connections define the cluster pairing for hadronization (p. 503).
- Non-planar (1/N²-suppressed) interference terms W̃ are dropped; authors argue they are also *dynamically* suppressed (no collinear poles, average to zero), giving only "few percent" errors (p. 474, 492, 494) — claimed first explicit demonstration of planar dominance in pQCD.
- Inter-jet coherence reproduces the **string/drag effect** in e⁺e⁻→qq̄g (Fig. 4) and predicts a hadron-level analogue in p̄p: qg→qg has *fewer* particles between the jets opposite the gluons than W→qq̄ at the same kinematics (Fig. 29, p. 522–523) — a proposed colour-flow test and S/B discriminant for hadronic W decays (RQ4).
- Also introduced: azimuthal correlations from interference (Eq. 78) and gluon polarization (Eqs. 79–80), cluster model for soft/underlying events (Eqs. 82–85); data comparisons (Mark II, R209, UA1, UA5) largely good, with an underestimated UA1 minimum-bias/W-event E_T (Figs. 24–25).

## Setup
- Perturbative components (p. 463–465): LO 2→2 matrix elements (Tab. 1, Eq. 65) for qq'→qq', qq→qq, qq̄→gg, gg→gg and crossings; Sudakov form factors; coherent time-like cascades (as in Webber 1984 / Marchesini–Webber 1984, refs. [7,8]); coherent space-like backward evolution guided by PDFs (Eqs. 50–58, Fig. 5, Tab. 4; EHLQ set 1 and Duke–Owens PDFs).
- Coherence derivation: eikonal current J(q) for soft-gluon emission off all external partons (Eqs. 9–12); J² decomposed into eikonal antenna functions W_ij (Eqs. 16–17) split as W_ij = W^i_ij + W^j_ij (Eqs. 20–21, 69); azimuthal average of W^i_ij vanishes outside cone θ_iq < θ_ij (Eq. 22). Two schemes: plain angular ordering (Eq. 24) and "improved" angular ordering keeping the azimuthal shape inside the cone (Eq. 25). α_s evaluated at Q(1−z) ≈ transverse momentum (Eqs. 40, 42), resumming large IR corrections.
- Initial conditions (Sect. 5.2): a colour structure is first selected by the relative probabilities of Tab. 1, then each parton has a colour-connected partner (connection structure h_ij in Tab. 3) (p. 497); for gluons one of two partners at random; cone half-angle from ξ_ij; jets with ξ>1 generated with rescaled E' = E√ξ (Eq. 76). Heavy-quark decay: W products interfere with each other; spectator quark does not radiate (p. 498).
- Hadronization (Sect. 5.7): non-perturbative g→qq̄ (or diquarks), colour-singlet clusters from planar colour lines (mean mass ≈ 3Q_g), isotropic 2-body decays by density of states, fission above M_f with M_f² = M_c² + (Q₁+Q₂)² (Eq. 81). Underlying event = UA5-style soft collision of beam clusters with negative-binomial multiplicity (Eqs. 82–85); no multiple parton interactions.
- Parameters (Tab. 5): Λ = 0.20 GeV, Q_g = 0.65 GeV, Q_s = 2.5 GeV, M_c = 5 GeV, P_c = 1; no dedicated tuning (p. 508).

## Results
- Soft-gluon pattern in e⁺e⁻→qq̄g (q, q̄, g at 0°, 155°, 230°): both angular-ordered and improved-AO approximations (non-planar 1/N² term dropped) reproduce the large dip around θ ≈ 80° between q and q̄ — the string effect — while improved AO is better in the constructive-interference dips (Fig. 4, Eq. 26, p. 475).
- qg→qg at 90°: improved AO reproduces the exact soft pattern [Ellis–Marchesini–Webber 1987], with destructive interference between the quark jets (0°–90°) and constructive in other regions (Fig. 11, Eq. 75, p. 494).
- Space-like coherence: E_iθ-ordering cancels the leading α_s²/(N−1)³ term of the gluon anomalous dimension at small x, consistent with the two-loop result γ_N^S (Eqs. 32–36); with naive θ-ordering one would get the time-like behaviour (Eq. 33). Only leading IR singularities (g₁) are captured; BFKL/CCFM-type non-leading small-x terms (ref. [5], Ciafaloni) are not included (p. 478).
- Neglecting coherence in the Sudakov form factor gives Δ'(Q) ≈ Δ(Q)² (p. 481); neglecting α_s rescaling gives a much less steep form factor (Eq. 46).
- e⁺e⁻: mean charged multiplicity up to 10 TeV agrees with NLL analytic predictions (shape only; normalised at 1 TeV) (Fig. 14); Mark II at 29 GeV: sphericity, aplanarity, x_p, p_in, p_out all in very good agreement except too few hadrons at highest x_p (Figs. 15–17, p. 509). Azimuthal correlations (5.5–5.6) have negligible visible effect on p_in/p_out (p. 511).
- DIS: backward evolution reproduces EHLQ structure-function moments M_n(Q_s) for 2.5 < Q < 1000 GeV within errors (Figs. 18–19); MC lies between LO and higher-order curves (p. 514). No hadronic-final-state DIS comparison (p. 514).
- Drell–Yan: R209 (√s = 62 GeV) dimuon q_T reproduced without explicit intrinsic k_T, via forced non-valence branching (Fig. 20); UA1 W p_T at 630 GeV (⟨p_T⟩ ≈ 8 GeV) slightly narrower than data (Fig. 21); agreement with Altarelli et al. and Davies et al. resummations for q_T > 6 GeV (Fig. 22). Hard-process E_T in W events matches Altarelli et al. (Fig. 23); full E_T narrower than UA1 preliminary (Fig. 24).
- Minimum bias at 546 GeV: UA5 multiplicities/⟨p_T⟩ reproduced (e.g. ⟨n_ch⟩ 29.7 vs 29.4 ± 0.3), with too much K⁰ (2.89 vs 2.24 ± 0.16) and Λ (0.87 vs 0.53 ± 0.11) (Tab. 6); mean E_T ≈ 21–23 GeV vs UA1 calorimetric ⟨E_T⟩ = 33 GeV — unexplained 10 GeV deficit (Fig. 25, p. 518–519).
- Jets: UA1 jet E_T profiles for E_T(event) > 200 GeV (Fig. 27) and core fraction ⟨F_0.2⟩ vs jet E_T (Fig. 28) well described.
- Jet–jet interference at hadron level (Fig. 29): after hadronization and underlying event, qq̄→W→qq̄ vs qg→qg at 90° (jet E_T sum > 80 GeV) — the destructive region between the quark jets remains visible; replacing two quark jets by gluon jets *decreases* the hadron flow opposite the gluons, analogous to the e⁺e⁻ qq̄γ vs qq̄g string effect (p. 522–523). Event-by-event fluctuations limit its use alone as a W selection cut (p. 523).

## Assessment
- Central reference for RQ2: it is the canonical statement of how leading-colour coherence (including initial–final interference) maps onto colour-connected partner cones, and it ties the same planar colour flow to cluster formation — i.e. the baseline colour-flow model that later colour-reconnection studies (e.g. in W⁺W⁻, top) perturb. Its explicit leading-N_c-only treatment and the "few percent" estimate for non-planar terms (based on two illustrative configurations, e⁺e⁻→qq̄g and 90° qg→qg, Figs. 4, 11) is a quantitative claim that later full-colour/subleading-colour shower work tests.
- The colour partner for a gluon is chosen at random between its two partners (p. 497), so the cone choice is stochastic rather than an exact antenna sum; azimuthal correlations are approximate (ξ_mj = ξ_kj, nearest-neighbour only, p. 501–502), and the authors find them unobservable in Mark II p_in/p_out (p. 511).
- Fig. 29 is a genuine proposed test (RQ4) of inter-jet colour coherence/colour flow in hadron collisions, predating jet-pull and CDF/D0 coherence measurements; it is MC-only, with no data comparison.
- Data comparisons are untuned and mostly global; the underlying-event model (no MPI) fails on UA1 E_T (Figs. 24–25), which affects any colour-flow observable in hadron collisions. Space-like coherence is only leading-IR; small-x non-leading (CCFM) effects are deferred (p. 478, 523).
- Hard scale choice Q² = 2stu/(s²+t²+u²) (Eq. 74) is independent of colour connection, though the authors note it should depend on it (p. 493).

## Leads
- Ellis, Marchesini & Webber, Nucl. Phys. B286 (1987) 643 [ref. 23] — soft radiation pattern and emission cones in 2→2 parton scattering; the colour-flow/coherence calculation underlying Sect. 4.
- Ciafaloni, Nucl. Phys. B296 (1987) 249 [ref. 5] and Catani, Ciafaloni & Marchesini, Nucl. Phys. B264 (1986) 588 [ref. 4] — coherence in space-like (initial-state) branching, small-x (CCFM precursor).
- Bassetto, Ciafaloni & Marchesini, Phys. Rep. 100 (1983) 201 [ref. 2] — standard review of jet structure and infrared coherence.
- Azimov, Dokshitzer, Khoze & Troyan, Phys. Lett. B165 (1985) 147 [ref. 16] — perturbative ("drag") explanation of the string effect.
- JADE, Bartel et al., PLB 134 (1984) 275 / B157 (1985) 340; TPC, Aihara et al., Z. Phys. C28 (1985) 31 / PRL 57 (1986) 945; Mark II, Sheldon et al., PRL 57 (1986) 1398 [ref. 17] — string-effect and qq̄γ vs qq̄g measurements.
- Dokshitzer, Khoze & Troyan (1987), and Dokshitzer, Khoze, Troyan & Mueller, Columbia CU-TP-374 (1987) [ref. 59] — colour-coherence ideas for enhancing hadronic W S/B; precursor of rapidity-gap/colour-flow tagging.
- Bengtsson & Sjöstrand, Nucl. Phys. B289 (1987) 810; Gottschalk & Morris, Nucl. Phys. B288 (1987) 729 [ref. 14] — competing coherent (PYTHIA/JETSET) showers.
- Webber, Ann. Rev. Nucl. Part. Sci. 36 (1986) 253 [ref. 13] — review of MC simulation of hard processes with coherence.

## Verification
Checked 2026-10-30 by an independent reader: 62 claims checked, 2 corrected, 0 unverifiable.
- Colour-structure selection uses the Tab. 1 probabilities (p. 497); Tab. 3 gives the resulting colour-connection weights h_ij — summary had attributed the selection to Tab. 3.
- "Few percent" non-planar estimate rests on two configurations (Fig. 4 e⁺e⁻→qq̄g and Fig. 11 qg→qg), not a single one.
