# Jet Final States in WW Pair Production and Colour Screening in the QCD Vacuum
- **ID / links:** Gustafson:1988fs · INSPIRE 261993 · arXiv — (pre-arXiv) · DOI 10.1016/0370-2693(88)91836-9
- **Authors / collab, year, journal:** G. Gustafson, U. Pettersson (Lund), P.M. Zerwas (Aachen), 1988, Phys. Lett. B 209 (1988) 90–94
- **Type:** phenomenology (MC study with a toy "all-or-nothing" reconnection hypothesis)
- **Relevance:** 3 · RQs: 1b, 2, 4
- **Full text source:** zotero (5-page journal scan with a text layer; all figures readable)

## Takeaways
- **This is the original proposal of colour reconnection ("quark exchange pairing", later "recoupling") in e⁺e⁻→W⁺W⁻→qq̄′QQ̄′.** At LEP200 the two W decay vertices are only ~0.1 fm apart, far below the ~1 fm confinement scale. So besides the "natural" singlets qq̄′ and QQ̄′, the cross pairs qQ̄′ and Qq̄′ can form the colour singlets that hadronize (p. 91, Fig. 1).
- **Naive colour counting gives 1/9 = 1/N_c².** The colour state Σ q_i q̄′_i Q_j Q̄′_j = (1/3)(Σ q_i Q̄′_i)(Σ Q_j q̄′_j) + octet terms, so the singlet weight of the recoupled pairing is 1/9 (p. 91, unnumbered equation). The authors expect non-perturbative dynamics to move this value, and they tie it to the QCD vacuum (p. 91):
  - A **type-I superconductor** vacuum (bag-like flux tube ~1 fm wide) lets soft gluons exchange colour until the charges are ~1 fm apart, so the recoupling probability is *enhanced*.
  - A **type-II** vacuum (vortex line with a thin core) fixes the string geometry at the core size. The recoupling probability is then *suppressed* if the core is smaller than the W–W separation.
- **Predicted signal, before any gluon radiation is taken into account in the reconnection:** when the angle α between q and Q̄′ is small, recoupled events have much lower multiplicity than independent WW fragmentation. Examples are 18.4 vs 45.0 at α = 20° and 22.7 vs 45.0 at α = 30° (Tab. 1). The large-angle region is emptied and the rapidity distribution becomes strongly double-peaked instead of nearly flat (Fig. 2).
- **Proposed test (RQ4):** count particles with |y| < 2 event by event at α = 30°. The recoupled and normal classes are "very well separated" (Fig. 3; p. 93). The fraction of recoupled events as a function of √s (i.e. W–W separation) and of jet angle would then give information on the QCD vacuum and confinement (conclusion (iii), p. 93); conclusion (ii) relates the recoupling probability to the colour screening length.
- The paper already warns that "precision tests of W properties must take this complication into consideration" (conclusion (i), p. 93). This is the seed of the m_W colour-reconnection systematic, although the paper gives no m_W shift.

## Setup
- **Process:** e⁺e⁻ → W⁺W⁻ → qq̄′QQ̄′ "near threshold" at LEP200. The hadronic BR of the pair is quoted as ~0.7² ≈ 0.5 (p. 91).
- **Space-time estimate:** the W–W decay separation grows only to ~0.1 fm from threshold to √s = 200 GeV. It stays < 1/4 fm even at 1/2 TeV, and the time separation between the decays averages ~0.1 fm (p. 91).
- **Two extreme configurations are compared** (Fig. 1):
  - (a) independent WW fragmentation, with strings qq̄′ and QQ̄′;
  - (b) quark-exchange pairing, with strings qQ̄′ and Qq̄′.
  - Each configuration is simulated as 100 % of the sample. There is no dynamical model of *when* recoupling happens and no treatment of gluons emitted before recoupling.
- **MC:** the dipole cascade (Gustafson–Pettersson; ARIADNE, LU TP 88-5) followed by Lund string fragmentation (JETSET) (refs. [15–17]; p. 92). The authors say the model reproduces PETRA–PEP data. They also note it gives a somewhat larger central multiplicity at higher energies than other cascades, which they call "not essential" for the conclusions (pp. 92–93).
- **Observables:**
  - total multiplicity vs α (Tab. 1);
  - particle flow in angle and rapidity w.r.t. the thrust axis at α = 30° (Fig. 2);
  - the distribution of the number of particles with |y| < 2 at α = 30° (Fig. 3).
  - The text defines the rapidity axis as the one "cutting the small angle in two" (p. 92). The Fig. 2 caption says thrust axis.
- **B-decay analogy** (footnote 2, p. 91): in B → J/ψ X (b → cW⁻ → cc̄s) the cc̄ is a colour singlet with probability 1/9 when no colour is exchanged. The measured BR is ~1 %. Estimates that ignore the 1/9 give 3–5 %, while estimates that include it plus short-distance QCD give 0.3–0.5 %. The authors conclude that recoupling at short distance happens, with probability "somewhat larger than (but still compatible with)" 1/9, but not as large as for free soft-gluon colour exchange.

## Results
- **Multiplicities (Tab. 1, p. 92):**

| α (q–Q̄′ angle) | Independent WW | Quark-exchange pairing | qq̄ continuum |
|---|---|---|---|
| 20° | 45.0 | 18.4 | 31.2 |
| 30° | 45.0 | 22.7 | 31.2 |
| 45° | 45.0 | 27.8 | 31.2 |
| 90° | 45.0 | 37.9 | 31.2 |

  - Independent WW multiplicity does not depend on α. The recoupled multiplicity drops strongly at small α because the recoupled singlet masses are ≪ √s/2 (p. 92).
  - The table does not state whether the multiplicities are charged or all particles, or the exact √s ("near threshold").
- **Particle flow (Fig. 2, α = 30°):**
  - With quark-exchange pairing, the large-angle segment between the jet pairs is "completely depleted" (p. 93; Fig. 2b left).
  - Independent WW fragmentation leaves a non-zero flow (~0.04–0.05, read off the figure) across the large-angle segment, similar to the qq̄ continuum (Fig. 2a, 2c left). The dip between the two close jets is similar in depth (~0.15) for both configurations (Fig. 2a, 2b left; read off the figure).
- **Rapidity (Fig. 2, α = 30°):**
  - Independent WW gives a broad plateau (the authors call it "almost flat", p. 93), with maxima of ~11 near |y| ≈ 1.8 and a shallow central dip to ~8 (Fig. 2a right; values read off the figure).
  - Quark-exchange gives two narrow peaks near |y| ≈ 2 with an essentially empty centre (Fig. 2b right).
  - qq̄ continuum is shown for comparison (Fig. 2c). The authors say the differences grow as α decreases and wash out at large α (p. 93).
- **Event-by-event separation (Fig. 3, α = 30°, |y| < 2):**
  - Recoupled events peak sharply at roughly 10 particles.
  - Independent WW events form a broad distribution centred at roughly 35.
  - These positions are our reading of the figure; the paper only states that the two classes are "very well separated" and better still at smaller α (p. 93).
- **No m_W shift and no expected admixture fraction are computed.** The 1/9 is given only as a group-theory baseline (p. 91).

## Assessment
- **Historical importance.** This is the paper that LEP CR literature cites as the origin of the idea (ALEPH_2013dgf Leads [101]; Rathsman_1998tp). It contains the main conceptual ingredients used later:
  - the 1/N_c² colour-counting baseline;
  - the link between the reconnection probability and the vacuum or flux-tube structure (type I vs type II). This becomes SK-I vs SK-II in Sjöstrand–Khoze 1994, as reported in Gustafson_1994cd;
  - the √s and angle dependence as a probe of the screening length;
  - the warning about W-property measurements.
- **The predicted signal is far too optimistic.** The striking effects (multiplicity halved, empty central region, clean event-by-event separation) come from treating recoupling as acting on the bare qq̄′QQ̄′ system with no prior hard-gluon emission, and from selecting a narrow q–Q̄′ angle.
  - The authors themselves revised this in Gustafson_1994cd: gluons with E > Γ_W are radiated independently by each W before recoupling. They fill the central region, so the inclusive rapidity signal can no longer establish a ~10 % admixture.
  - Sjöstrand–Khoze (as quoted in Gustafson_1994cd, p. 661) likewise found only small effects on averages.
- **The √s-scan proposal was later undercut.** The paper suggests using √s to vary the W–W separation (p. 93). Gustafson_1994cd (p. 662, citing SK) notes that the finite W width keeps the separation nearly constant across the LEP2 range, so this lever arm is weak.
- **Relation to the LEP2 outcome (ALEPH_2013dgf).** LEP2 saw no clean event-by-event recoupled sample. CR was constrained only statistically:
  - via the inter-W/intra-W particle-flow ratio R_N, a descendant of the large-angle depletion idea in Fig. 2;
  - via m_W-estimator differences.
  - The SK-I combination prefers p_reco ≈ 51 % at 189 GeV, with no-CR disfavoured at 2.8σ. This is well above the 1/9 baseline. In the type-I/type-II language of this paper that would point toward the "enhanced" scenario, but the combination is SK-I-specific, so it does not test the vacuum picture in a model-independent way.
  - CR ended up as the dominant m_W(qqqq) systematic (35 MeV), which confirms conclusion (i).
- **Caveats.** Tab. 1 does not specify whether the multiplicities are charged or total, or the exact √s. The ARIADNE version used predates later tunes. The B → J/ψ argument depends on 1980s branching-ratio estimates.

## Leads
- Sjöstrand & Khoze, Z. Phys. C 62 (1994) 281 and PRL 72 (1994) 28: the SK-I/SK-II models that made the type-I/type-II idea quantitative and computed the m_W shift. These are the core of the LEP2 CR analyses (likely already queued via ALEPH_2013dgf).
- Gustafson & Häkkinen, Z. Phys. C 64 (1994) 659: direct follow-up that adds gluon emission before recoupling (summarized: Gustafson_1994cd.md).
- Gustafson & Pettersson, "Dipole formulation of QCD cascades", LU TP 87-9 / Nucl. Phys. B 306 (1988) 746, and U. Pettersson, ARIADNE, LU TP 88-5: the MC used here. Context for dipole-cascade colour flow (RQ2).
- Gustafson, Phys. Lett. B 175 (1986) 453: dipole picture of coherent emission (RQ1a/2).
- Kühn, Nussinov & Rückl, Z. Phys. C 5 (1980) 117, and related B → J/ψ X colour-suppression papers (ref. [12]): the colour-recoupling analogy at zero distance. Low priority (relevance ~1); useful only if the review discusses colour suppression in weak decays as a calibration of "1/N_c² recoupling".
- Mättig & Dittmar, Z. Phys. C 35 (1987) 221, and the ECFA LEP200 workshop (Aachen 1985): the pre-LEP2 WW-physics context. Low priority.
