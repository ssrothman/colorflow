# Measurement of colour flow using jet-pull observables in tt̄ events with the ATLAS experiment at √s = 13 TeV
- **ID / links:** ATLAS:2018olo · INSPIRE 1672147 · arXiv 1805.02935 · DOI 10.1140/epjc/s10052-018-6290-2
- **Authors / collab, year, journal:** ATLAS Collaboration, 2018, Eur. Phys. J. C 78 (2018) 847 (CERN-EP-2018-041)
- **Type:** experimental
- **Relevance:** 3 · RQs: 1b, 1d, 2, 3
- **Full text source:** zotero

## Takeaways
- Unfolded (particle-level, charged-particle) jet-pull measurement in tt̄ ("first unfolded" [unverified]: the paper does not claim priority, and the 8 TeV predecessor may also have been unfolded): forward and backward pull angle of the two W-daughter-candidate jets, pull magnitude of the leading W jet, and pull angle between the two b-jets as a "spurious colour flow" control (Tab. 3, Fig. 5).
- The colour-singlet W signal shows the expected peaking at small |θ_P|/π (≈14% above flat in the first bin, read from Fig. 5a), while the b-b̄ control is flat to about ±1–2% (≈ read from Fig. 5d).
- An ad hoc colour-octet ("flipped") W sample is disfavoured: χ²/NDF = 45.3/3 and 45.9/3 for the forward and backward angles, even with the flipped model added as a systematic uncertainty (Tab. 5). Discrimination is real but diluted, because both W jets are correctly matched in only ~30% of events (p. 11).
- No SM generator describes all observables. Powheg+Pythia8 (A14), the nominal ATLAS setup, is strongly excluded (χ²/NDF 50.9/3 forward angle, 24.8/4 magnitude). Powheg+Herwig7 describes the W-jet observables best (p = 0.45, 0.33) but is the worst on the b-b̄ angle (p = 0.19, the only prediction consistently outside the uncertainty bands, pp. 20–21). MC generally predicts stronger colour-flow effects than seen in data (Tab. 5, p. 20).
- The CR systematic (A14.v1 tune variations) on the forward W pull angle is 0.16–0.22% per bin (Tab. 4; only this observable's breakdown is tabulated). Hadronisation (Pythia vs Herwig) is the largest single source (0.55% in the first bin). CR is comparable to the generator, b-tagging and background components (0.1–0.5%). Pull is therefore more sensitive to the shower/hadronisation model than to the CR strength as varied by the tune, though not by a large factor.

## Setup
- pp at √s = 13 TeV, 36.1 fb⁻¹ (2015–16) (p. 5). Lepton+jets tt̄: exactly one e/μ with pT > 27 GeV, ≥4 anti-kt R = 0.4 jets with pT > 25 GeV, ≥2 b-tags (70% WP), E_T^miss > 20 GeV (p. 8). About 1.15M events selected, ~88% purity (Tab. 2, p. 9).
- Pull vector P(j) = Σ_i |Δr_i| pT_i/pT_j · Δr_i (Eq. 1), built from ghost-associated inner-detector tracks (pT > 0.5 GeV, |η_jet| < 2.1, ≥2 tracks). The jet axis is recomputed from the tracks (p. 10). Observable: |θ_P|/π.
- Jet assignment: the W-daughter candidates are the two leading non-b-tagged jets, with both jets correct in ~30% of events and ~50% having one correct. The b-pair is the two leading b-tagged jets, ~80% correct (p. 11). Forward and backward W pull angles are correlated by <1% in data (p. 11).
- Unfolding: iterative Bayesian (RooUnfold) to particle level using charged particles with pT > 0.5 GeV; normalised fiducial distributions (p. 13). χ² uses the full data covariance but no theory uncertainty (p. 20).
- Models: Powheg+Pythia8 (A14), Powheg+Pythia6 (P2012), MG5_aMC+Pythia8, Powheg+Herwig7 (H7UE), Sherpa 2.2.1 (Tab. 1). "Flipped" sample: the Powheg LHE colour lines are rewired so that one W daughter connects to the incoming top and the other to the b, emulating a colour-octet W. It is then showered with Pythia8 (p. 7).

## Results
- Detector level: the W-pair pull angles slope downward and the b-pair angle is flat, both broadly consistent with nominal MC (Fig. 4).
- Forward W pull angle, first bin (0–0.21): data ≈1.14. Pythia8 ≈1.19 (about +4.5%), flipped ≈1.05 (about −8%) (≈ read from Fig. 6a). Total uncertainty 0.91% in this bin (Tab. 4).
- Uncertainty breakdown for the forward angle: systematic 0.44–0.88%, statistical 0.19–0.25%. Leading sources are hadronisation (0.55%), generator, b-tagging, background, then CR (0.16–0.22%) (Tab. 4).
- χ²/NDF (p-value), observables in the order forward / backward / b-b̄ / |P| (Tab. 5):
  - Pw+Py8: 50.9/3 (<0.001), 25.1/3 (<0.001), 0.7/3 (0.87), 24.8/4 (<0.001)
  - Pw+Py6: 23.2/3 (<0.001), 8.2/3 (0.042), 4.2/3 (0.24), 21.1/4 (<0.001)
  - MG5+Py8: 6.8/3 (0.077), 6.7/3 (0.082), 2.0/3 (0.56), 17.6/4 (0.001)
  - Pw+H7: 2.7/3 (0.45), 3.4/3 (0.33), 4.8/3 (0.19), 11.3/4 (0.023)
  - Sherpa: 22.0/3 (<0.001), 11.9/3 (0.008), 0.0/3 (0.998), 14.1/4 (0.007)
  - With the flipped-model systematic included: Pw+Py8 17.1/3, 25.0/3, 0.3/3, 11.1/4; flipped 45.3/3, 45.9/3, 2.6/3, 17.2/4.
- Data prefer larger pull magnitudes and a less steep angular distribution than the MC predictions (the paper says the trend is "similar for the different MC predictions", not strictly all), i.e. "a weaker colour-flow effect" than simulated (p. 20, Fig. 5c). Pythia6 does significantly better than Pythia8 (p. 20).
- The colour-model (flipped) uncertainty is of similar size to the dominant signal-modelling uncertainties (p. 19).

## Assessment
- This is a clean demonstration that the colour-singlet nature of W→qq̄ is visible in radiation patterns at the LHC, and a valuable tuning target (Rivet/HEPData availability [unverified], not stated in the paper). However, discriminating against the flipped model mostly tests a gross colour-octet hypothesis. It does not discriminate between realistic CR models.
- Strong generator dependence with small experimental uncertainties (<1%) means the pull angle is now a precision probe of shower/hadronisation colour treatment. Why Pythia8/A14 fails while Pythia6 and Herwig7 do better is not diagnosed (shower recoil? MPI/UE contamination of R = 0.4 jets? the tune?). It is worth checking whether later Pythia8 tunes or CR models (QCD-based CR, gluon-move) fix it.
- The ~30% correct-pair rate means much of the "signal" sample is mixed pairs (e.g. W jet + ISR jet), so the measured slope is a diluted, model-dependent mixture. Particle-level unfolding does not remove this, since the same assignment is used at particle level. Comparisons with parton-level colour-flow theory are therefore indirect.
- The χ² values exclude theory uncertainties, so the "exclusions" of generators are of nominal predictions, not of model classes.
- The CR systematic enters only via the A14.v1 tune variations. Its smallness here should not be read as evidence that pull is CR-insensitive (cf. Argyropoulos & Sjöstrand 2014, who found pull insensitive after tuning; consistent).
- Tension to track: the 8 TeV ATLAS measurement (PLB 750 (2015) 475) reportedly found broadly good MC agreement [unverified]: this paper only cites it (ref. [7]) and does not characterise its results. This 13 TeV unfolded result shows clear mismodelling.

## Leads
- ATLAS 2015, PLB 750 (2015) 475, arXiv:1506.05629: the 8 TeV jet-pull angle in tt̄ (predecessor; colour-octet W comparison).
- Gallicchio & Schwartz 2010, PRL 105 022001, arXiv:1001.5027: original jet-pull proposal (RQ4).
- D0 1999, PLB 464 (1999) 145, hep-ex/9908017: colour coherence in W+jets (precursor pull-like study).
- L3 2003, PLB 561 (2003) 202, and DELPHI 2007, EPJC 51 (2007) 249: WW particle-flow CR at LEP2 (cited as colour-flow precedents).
- JADE 1983, Z. Phys. C 21 (1983) 37: string effect in three-jet events.
- D0 2011, PRD 83 (2011) 092002 (from memory, not cited here): Tevatron jet-pull colour-flow measurement in tt̄, for an era comparison.
- Forward citations: theory of pull (resummation, Larkoski–Marzani–Thaler style), later Pythia8 CR/tune comparisons to this dataset, and H→bb̄ colour-flow proposals (p. 3 motivates tt̄H(bb̄) jet assignment).

## Verification
Checked 2026-10-30 by an independent reader: 46 claims checked, 3 corrected, 4 unverifiable.
- Takeaway on CR systematic: Tab. 4 covers only the forward W pull angle. CR (0.16–0.22%) is comparable to the generator, b-tagging and background terms, so "hadronisation and generator dominate" was overstated. Rephrased.
- "Data prefer larger magnitudes than all MC": softened to the paper's wording ("similar trend for the different MC predictions").
- Clarified the b-b̄ flatness (≈±1–2%) and marked the plot-read values (Fig. 5a,d, 6a) as ≈.
- Unverifiable from the paper: the "first unfolded" priority, the characterisation of the 8 TeV result, Rivet/HEPData availability, and the D0 2011 lead (still flagged from memory, not in the reference list).
- Confirmed exactly against the text/tables: all Tab. 5 χ²/NDF and p-values, all Tab. 4 numbers, the selection (p. 8), yields (1 153 003 observed, ~88% purity), the 30%/50%/80% matching (p. 11), the <1% correlation, the flipped-sample construction (p. 7), RooUnfold IBU (p. 13), χ² without theory uncertainties (p. 20), the Herwig 7 b-b̄ statement (pp. 20–21), the Tab. 1 generators/tunes, and refs [3]–[8].
