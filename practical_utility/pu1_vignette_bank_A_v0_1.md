# TPUT PU1 Vignette Bank A v0.1 — Black-box Prediction + Synthetic Surrogates

**Status:** CANDIDATE INSTRUMENT / AUTHOR DRAFT / NOT EXPERT-KEYED  
**Date:** 2026-09-04  
**Parent:** `practical_utility/research_program_v0_1.md`  
**Decision:** D040

## Instrument rule

Every candidate has one canonical fact sheet and two renderings. The two renderings must convey the same scientific facts. The Trias rendering may reorganize and label those facts by `R/T/C`, relation, scope, and status, but must not add a result, limitation, numerical value, or scientific premise unavailable to the generic control condition.

Participant-facing claim items are identical across conditions. `J1–J4` are binary warrant judgments (`WARRANTED` / `NOT WARRANTED`) with confidence. `J5` is a status judgment. `J6` asks what relation/referent the principal reported evidence directly concerns, using short neutral definitions supplied in the response interface.

Author-intended keys are kept in a separate file and must not be shown to external keying experts in round 1.

---

# BLACK-BOX PREDICTION

## BB01 — Battery remaining-capacity predictor

### Canonical fact sheet

- Scientific use: estimate remaining discharge capacity of lithium-ion cells during a fixed laboratory cycling protocol.
- Target: physical cells measured in the same laboratory protocol; real referent.
- Input: voltage, current, temperature, and cycle count from the first 20% of each discharge cycle.
- Model: gradient-boosted predictor; no mechanistic battery model is claimed by the study.
- Training: 80 cells.
- Test: 20 previously unseen cells from the same manufacturer and protocol.
- Test mean absolute percentage error: 2.8%.
- A simple linear baseline has 6.9% error on the same test cells.
- No cells from another manufacturer, chemistry, temperature protocol, or laboratory are tested.
- Feature importance is reported, but the authors explicitly do not claim that it identifies electrochemical mechanisms.

### Condition A — Generic structured control

**Scientific question / use.** A gradient-boosted model estimates remaining discharge capacity of physical lithium-ion cells during one fixed laboratory cycling protocol from voltage, current, temperature, and cycle-count data observed during the first 20% of a discharge cycle. The study makes no claim that the predictor is a mechanistic battery model.

**Reported evidence.** The model is trained on 80 cells and tested on 20 previously unseen cells from the same manufacturer and protocol. Mean absolute percentage error on these held-out cells is 2.8%, compared with 6.9% for a linear baseline. Feature-importance values are also reported.

**Scope / regime.** The held-out test covers the same manufacturer and laboratory protocol used to construct the dataset.

**Known limitations / unresolved claims.** Cells from other manufacturers, chemistries, temperatures, or laboratories are not tested. The study explicitly does not interpret feature importance as identification of electrochemical mechanism.

### Condition B — Trias role/evidence profile

**R — target / referent.** Physical lithium-ion cells measured under the same laboratory protocol (`REAL`).

**T — theory-level claim.** `NONE_CLAIMED` for the narrow prediction use; the study does not claim that the learned representation identifies an electrochemical mechanism.

**C — computational practice.** Gradient-boosted predictor using voltage, current, temperature, and cycle count from the first 20% of each discharge cycle.

**Directly assessed relation.** Computational prediction versus the real held-out target cells.

**Evidence.** Training uses 80 cells; testing uses 20 previously unseen cells from the same manufacturer and protocol. Test MAPE is 2.8%, versus 6.9% for a linear baseline. Feature importance is reported.

**Use / scope.** Same manufacturer and cycling protocol. Other manufacturers, chemistries, temperatures, and laboratories are not tested.

**Status / explicit non-implication.** Prediction is supported in the tested regime; electrochemical mechanism identification is not established by the reported performance or feature importance.

### Participant claim items

- **J1.** The reported evidence supports that the predictor estimates capacity more accurately than the stated linear baseline for the held-out cells in the tested protocol.
- **J2.** The reported evidence supports predictive performance on previously unseen cells from the same manufacturer and protocol.
- **J3.** The reported evidence establishes that the gradient-boosted model has identified the electrochemical mechanism governing capacity fade.
- **J4.** The reported evidence establishes comparable predictive accuracy for cells from other manufacturers and chemistries.
- **J5.** What is the status of a claim about accuracy on another manufacturer under a different temperature protocol?
- **J6.** What does the principal reported test evidence directly compare, and what is its referent type?

---

## BB02 — Stellar effective-temperature estimator

### Canonical fact sheet

- Scientific use: estimate effective temperature `T_eff` for stars from low-resolution spectra.
- Target: stars with independent high-resolution spectroscopic temperature estimates; real referent.
- Model: convolutional neural network.
- No claim is made that internal CNN filters correspond to stellar-atmosphere mechanisms.
- Training set: 30,000 spectra.
- Held-out test set: 5,000 stars in the same survey footprint and instrument configuration.
- Median absolute error: 74 K.
- A template-fitting baseline has median absolute error 118 K on the same test set.
- The test set contains few metal-poor stars below `[Fe/H] = -2` and no spectra from a different instrument.
- No causal or mechanistic interpretation of latent features is validated.

### Condition A — Generic structured control

**Scientific question / use.** A convolutional neural network estimates stellar effective temperature from low-resolution spectra. Reference temperatures come from independent high-resolution spectroscopic analyses of physical stars. The work evaluates prediction, not whether learned filters instantiate stellar-atmosphere mechanisms.

**Reported evidence.** The network is trained on 30,000 spectra and tested on 5,000 held-out stars observed with the same survey instrument and footprint. Median absolute error is 74 K, while a template-fitting baseline reaches 118 K on the same stars.

**Scope / regime.** The held-out sample is drawn from the same observational program and instrument configuration. Very metal-poor stars below `[Fe/H] = -2` are rare.

**Known limitations / unresolved claims.** No independent instrument is tested. Internal features are not validated as causal or mechanistic representations of stellar atmospheres.

### Condition B — Trias role/evidence profile

**R — target / referent.** Physical stars with independent high-resolution temperature estimates (`REAL`).

**T — theory-level claim.** `NONE_CLAIMED` for the CNN representation; no mechanistic interpretation of learned filters is asserted.

**C — computational practice.** Convolutional neural network mapping low-resolution spectra to `T_eff`.

**Directly assessed relation.** Computation–target predictive agreement on held-out real stars.

**Evidence.** 30,000 training spectra and 5,000 held-out stars from the same survey configuration. Median absolute error is 74 K versus 118 K for template fitting.

**Use / scope.** Same instrument and survey footprint; very metal-poor stars are sparse and no other instrument is tested.

**Status / explicit non-implication.** Target-relative prediction is supported in the tested sample; the evidence does not establish a mechanistic interpretation of CNN filters or transport to a new instrument.

### Participant claim items

- **J1.** The CNN has lower median temperature error than the stated template baseline on the held-out survey stars.
- **J2.** The study provides direct evidence about prediction relative to physical stars in the tested survey configuration.
- **J3.** The study establishes that the learned CNN filters correspond to the causal radiative-transfer mechanisms of stellar atmospheres.
- **J4.** The reported test establishes the same error level for spectra obtained with a different instrument.
- **J5.** What is the status of a claim about performance for `[Fe/H] < -2.5` stars observed by another spectrograph?
- **J6.** What relation/referent does the principal held-out evaluation directly address?

---

## BB03 — Turbulent-drag prediction from surface sensors

### Canonical fact sheet

- Scientific use: predict instantaneous drag coefficient on a wind-tunnel bluff body.
- Target: physical wind-tunnel measurements; real referent.
- Inputs: 16 surface pressure sensors.
- Model: multilayer perceptron.
- Test runs use unseen time segments but the same body geometry and Reynolds-number interval as training.
- Test normalized RMSE: 0.06.
- Persistence baseline normalized RMSE: 0.14.
- A different body geometry and Reynolds numbers outside the training interval are not tested.
- The MLP is not analyzed for recovery of coherent structures or Navier–Stokes mechanisms.
- The authors claim only a sensor-to-drag predictor for the tested operating range.

### Condition A — Generic structured control

**Scientific question / use.** A multilayer perceptron predicts instantaneous drag coefficient on a bluff body in a wind tunnel from 16 surface-pressure sensors. The goal is sensor-based prediction in the tested operating range, not mechanistic recovery of the underlying flow equations or coherent structures.

**Reported evidence.** Test runs use unseen time segments from the same geometry and Reynolds-number interval as training. Normalized RMSE is 0.06, compared with 0.14 for a persistence baseline.

**Scope / regime.** The evidence concerns the same body geometry and Reynolds-number interval represented in training.

**Known limitations / unresolved claims.** A different geometry and extrapolative Reynolds numbers are not evaluated. The network representation is not tested for recovery of Navier–Stokes mechanisms or physically unique coherent structures.

### Condition B — Trias role/evidence profile

**R — target / referent.** Physical wind-tunnel drag measurements (`REAL`).

**T — theory-level claim.** `NONE_CLAIMED` for the learned representation in the stated prediction use.

**C — computational practice.** MLP mapping 16 surface-pressure measurements to instantaneous drag.

**Directly assessed relation.** Computation–target predictive agreement.

**Evidence.** On unseen time segments from the same geometry and Reynolds interval, normalized RMSE is 0.06 versus 0.14 for persistence.

**Use / scope.** Same geometry and represented Reynolds-number interval.

**Status / explicit non-implication.** Predictive adequacy is supported in that regime. No evidence establishes extrapolation to a new geometry or recovery of unique flow mechanisms/coherent structures.

### Participant claim items

- **J1.** The MLP predicts drag more accurately than the persistence baseline on the reported held-out runs.
- **J2.** The reported evidence supports drag prediction for the tested geometry and Reynolds-number interval.
- **J3.** The reported prediction error establishes that the network has recovered the unique coherent structures causing drag.
- **J4.** The reported evidence establishes accuracy on a different body geometry.
- **J5.** What is the status of the claim that the model remains accurate at Reynolds numbers outside the tested interval?
- **J6.** Which relation/referent is directly tested by the drag RMSE?

---

## BB04 — Materials-property screening model

### Canonical fact sheet

- Scientific use: predict experimentally measured thermal conductivity of polymer composites from composition and processing descriptors.
- Target: measured thermal conductivity; real referent.
- Model: random forest.
- Dataset: 1,200 samples from three laboratories using a harmonized measurement protocol.
- Split: one laboratory is held out entirely for testing.
- Test RMSE: 0.18 W m^-1 K^-1.
- Mean-prediction baseline RMSE: 0.31 W m^-1 K^-1.
- All three laboratories use the same set of polymer families; no new family is tested.
- The study does not claim that random-forest feature importance recovers microscopic heat-transport pathways.
- The model is proposed for screening within the represented material families.

### Condition A — Generic structured control

**Scientific question / use.** A random forest predicts measured thermal conductivity of polymer composites from composition and processing descriptors. Data come from three laboratories using a harmonized protocol. The intended use is screening within the represented polymer families, not microscopic explanation.

**Reported evidence.** The dataset contains 1,200 samples. One laboratory is held out entirely for testing. On that laboratory, RMSE is 0.18 W m^-1 K^-1, compared with 0.31 for a mean-prediction baseline.

**Scope / regime.** The held-out laboratory is new, but the polymer families are represented in the training laboratories.

**Known limitations / unresolved claims.** No entirely new polymer family is evaluated. Feature importance is not validated as a microscopic heat-transport mechanism.

### Condition B — Trias role/evidence profile

**R — target / referent.** Experimentally measured thermal conductivity (`REAL`).

**T — theory-level claim.** `NONE_CLAIMED` for microscopic heat transport in the prediction claim.

**C — computational practice.** Random-forest screening predictor from composition and processing descriptors.

**Directly assessed relation.** Computation–target prediction on a held-out real laboratory.

**Evidence.** 1,200 samples across three laboratories; one laboratory held out. Test RMSE 0.18 W m^-1 K^-1 versus 0.31 for a mean baseline.

**Use / scope.** New laboratory under a harmonized protocol, but only polymer families represented in training.

**Status / explicit non-implication.** Cross-laboratory prediction within represented families is supported. Transfer to unseen polymer families and microscopic mechanistic identification are not established.

### Participant claim items

- **J1.** The model outperforms the mean baseline on the held-out laboratory.
- **J2.** The study directly tests some cross-laboratory predictive transfer within represented polymer families.
- **J3.** The reported feature importance establishes microscopic heat-transport pathways.
- **J4.** The held-out-laboratory result establishes performance on entirely new polymer families.
- **J5.** What is the status of the claim about a new polymer family absent from all training data?
- **J6.** What relation/referent is directly assessed by the held-out-laboratory RMSE?

---

## BB05 — Ocean-wave height nowcast

### Canonical fact sheet

- Scientific use: predict significant wave height 30 minutes ahead at one coastal buoy.
- Target: buoy observations; real referent.
- Model: recurrent neural network using the previous two hours of buoy and local wind measurements.
- Training: three years at buoy A.
- Test: final six months at buoy A, held out chronologically.
- Test MAE: 0.22 m.
- Persistence MAE: 0.35 m.
- Extreme storm cases above 6 m wave height constitute less than 1% of test observations.
- No second buoy or different coastline is tested.
- No claim is made that hidden states identify ocean-wave generation mechanisms.

### Condition A — Generic structured control

**Scientific question / use.** A recurrent neural network predicts significant wave height 30 minutes ahead at one coastal buoy using the previous two hours of buoy and local-wind measurements. The goal is local nowcasting; hidden states are not claimed to identify wave-generation mechanisms.

**Reported evidence.** Three years at buoy A are used for training. The final six months are held out chronologically. Mean absolute error is 0.22 m versus 0.35 m for persistence.

**Scope / regime.** The evidence concerns the same buoy and coastline. Extreme events above 6 m are less than 1% of the test set.

**Known limitations / unresolved claims.** No second buoy or different coastline is evaluated. Evidence for rare extreme storms is limited by their frequency.

### Condition B — Trias role/evidence profile

**R — target / referent.** Physical wave-height observations at buoy A (`REAL`).

**T — theory-level claim.** `NONE_CLAIMED` for ocean-wave mechanism identification.

**C — computational practice.** Recurrent 30-minute nowcast using two hours of buoy and wind history.

**Directly assessed relation.** Computation–target prediction at the same real buoy.

**Evidence.** Three years training, final six months held out; MAE 0.22 m versus 0.35 m for persistence.

**Use / scope.** Buoy A and its coastline. Events above 6 m are rare (<1% of test observations); no second buoy is tested.

**Status / explicit non-implication.** Local nowcast performance is supported. Transfer to other coastlines and robust extreme-event performance are not established; hidden-state mechanisms are not claimed.

### Participant claim items

- **J1.** The network improves 30-minute wave-height prediction over persistence on the chronological test period at buoy A.
- **J2.** The evidence directly concerns physical observations at buoy A.
- **J3.** The test establishes that the recurrent hidden states identify the physical mechanism of wave generation.
- **J4.** The test establishes equivalent accuracy at another coastline.
- **J5.** What is the status of a strong accuracy claim specifically for >6 m storms?
- **J6.** What relation/referent is directly assessed by the reported MAE?

---

# SYNTHETIC SURROGATES

## SS01 — Airfoil CFD surrogate

### Canonical fact sheet

- Scientific use: emulate lift and drag coefficients from an expensive RANS CFD solver for rapid design screening.
- Underlying theory/model: the fixed RANS model and boundary-condition specification used by the CFD solver.
- Synthetic referent: outputs of that CFD solver on the defined parameter domain.
- Surrogate: neural operator.
- Training: 40,000 CFD cases over angle of attack `[-4°, 12°]` and Reynolds number `[1e6, 5e6]`.
- Held-out simulator test: relative lift error 0.7%, drag error 1.5%.
- CFD discretization/solver verification has been performed to the project’s stated tolerance.
- No wind-tunnel or flight data are used in the surrogate study.
- The CFD model’s real-world predictive validity for the considered airfoils is not assessed in this study.
- Surrogate use outside the simulator training domain is not tested.

### Condition A — Generic structured control

**Scientific question / use.** A neural operator emulates lift and drag generated by a fixed RANS CFD workflow so that design queries can be evaluated more cheaply.

**Reported evidence.** The surrogate is trained on 40,000 CFD cases spanning angles of attack from -4° to 12° and Reynolds numbers from 1e6 to 5e6. On held-out CFD cases in that domain, relative lift error is 0.7% and drag error is 1.5%. The CFD implementation itself has passed the project’s stated discretization/solver-verification tolerance.

**Scope / regime.** Surrogate performance is tested only within the simulator domain used to generate training data.

**Known limitations / unresolved claims.** No wind-tunnel or flight observations enter this study. The real-world predictive validity of the underlying RANS model is not assessed here, and surrogate extrapolation is not tested.

### Condition B — Trias role/evidence profile

**R — target / referent.** For the reported surrogate metric, the referent is the RANS CFD output (`SYNTHETIC`).

**T — theory-level claim.** `PRESENT`: the fixed RANS model and boundary-condition specification underlying the simulator.

**C — computational practice.** Neural-operator surrogate trained on CFD outputs.

**Directly assessed relation.** Surrogate computation versus simulator-defined synthetic referent.

**Evidence.** 40,000 CFD training cases; held-out in-domain CFD tests give 0.7% relative lift error and 1.5% drag error. The CFD implementation has passed the stated solver-verification tolerance.

**Use / scope.** Angles `[-4°,12°]`, Reynolds `[1e6,5e6]`; no extrapolation test.

**Status / explicit non-implication.** Teacher fidelity is supported in-domain. No wind-tunnel/flight validation is reported, so real-target aerodynamic validity is not established by the surrogate metric.

### Participant claim items

- **J1.** The surrogate closely reproduces the reported CFD outputs on held-out cases within the stated parameter domain.
- **J2.** The study supports use of the surrogate as an emulator of the specified CFD workflow within the tested domain.
- **J3.** The held-out CFD error establishes that the surrogate predicts real wind-tunnel lift and drag to the same accuracy.
- **J4.** CFD solver verification alone establishes that the RANS model is empirically valid for the real airfoils.
- **J5.** What is the status of a claim about real wind-tunnel accuracy in this study?
- **J6.** What relation/referent is directly assessed by the 0.7%/1.5% surrogate errors?

---

## SS02 — Climate-model emulator for regional temperature

### Canonical fact sheet

- Scientific use: emulate annual regional surface-temperature outputs of one Earth-system model under emissions scenarios.
- Synthetic referent: outputs from model `ESM-X`.
- Surrogate: Gaussian-process emulator.
- Training: 600 ESM-X scenario simulations.
- Test: 120 held-out ESM-X simulations.
- Test RMSE: 0.11 °C for the regional annual-mean quantity.
- Emulator uncertainty intervals achieve 93% coverage against held-out ESM-X outputs for nominal 95% intervals.
- Historical observations are not used to evaluate the emulator.
- Structural climate-model uncertainty across other Earth-system models is not part of the surrogate test.
- The study does not claim that emulating ESM-X resolves the real climate system’s structural uncertainty.

### Condition A — Generic structured control

**Scientific question / use.** A Gaussian-process emulator approximates annual regional surface-temperature outputs produced by one Earth-system model, ESM-X, across emissions scenarios.

**Reported evidence.** The emulator is trained on 600 ESM-X scenario runs and tested on 120 held-out ESM-X runs. RMSE is 0.11 °C for the chosen regional annual-mean quantity. Nominal 95% emulator intervals contain the held-out ESM-X value in 93% of cases.

**Scope / regime.** The evidence concerns reproduction of ESM-X across the represented scenario domain.

**Known limitations / unresolved claims.** Historical observations are not used in this surrogate evaluation. Structural disagreement among other climate models is not assessed. The study does not claim that faithful emulation of ESM-X resolves uncertainty about the real climate system.

### Condition B — Trias role/evidence profile

**R — target / referent.** ESM-X simulator output for the surrogate-evaluation claim (`SYNTHETIC`).

**T — theory-level claim.** `PRESENT` through the physical/climate model encoded by ESM-X, but its adequacy for the real climate is not tested by this surrogate study.

**C — computational practice.** Gaussian-process emulator over emissions scenarios.

**Directly assessed relation.** Emulator computation versus ESM-X synthetic referent.

**Evidence.** 600 training runs, 120 held-out ESM-X runs; RMSE 0.11 °C; nominal 95% intervals cover 93% of held-out simulator outputs.

**Use / scope.** Represented scenario domain for the regional annual mean.

**Status / explicit non-implication.** Emulator fidelity to ESM-X is supported; real-climate validation and inter-model structural uncertainty remain untested here.

### Participant claim items

- **J1.** The emulator is evaluated directly against held-out ESM-X simulations.
- **J2.** The reported RMSE supports fidelity to ESM-X for the stated regional quantity within the represented scenario domain.
- **J3.** The 0.11 °C emulator RMSE establishes 0.11 °C error relative to the real future climate.
- **J4.** The emulator’s interval coverage resolves structural uncertainty across different climate models.
- **J5.** What is the status of a claim that the emulator has been validated against historical observations?
- **J6.** What relation/referent is directly tested by the held-out ESM-X comparison?

---

## SS03 — Molecular-dynamics force-field surrogate

### Canonical fact sheet

- Scientific use: approximate energies and forces from a fixed density-functional-theory (DFT) setup for molecular dynamics.
- Synthetic referent: outputs of that DFT setup.
- Surrogate: message-passing neural potential.
- Training: 50,000 DFT configurations from temperatures 300–1200 K.
- Held-out DFT test: force MAE 35 meV/Å and energy MAE 2.1 meV/atom.
- A 100 ps surrogate MD trajectory at 800 K remains numerically stable and reproduces the DFT-trained radial-distribution target within the reported tolerance.
- No experimental thermodynamic or spectroscopic data are used for validation.
- Alternative exchange-correlation functionals are not compared.
- The study claims a fast surrogate of the chosen DFT level, not experimental truth.

### Condition A — Generic structured control

**Scientific question / use.** A message-passing neural potential approximates energies and forces generated by one fixed density-functional-theory setup to accelerate molecular dynamics.

**Reported evidence.** Training uses 50,000 DFT configurations from 300–1200 K. On held-out DFT configurations, force MAE is 35 meV/Å and energy MAE is 2.1 meV/atom. A 100 ps surrogate trajectory at 800 K is numerically stable and reproduces the DFT-trained radial-distribution target within the reported tolerance.

**Scope / regime.** The target for evaluation is the chosen DFT setup over the represented temperatures.

**Known limitations / unresolved claims.** No experimental thermodynamic or spectroscopic validation is reported. Other exchange-correlation functionals are not evaluated. The intended claim is fidelity to the chosen DFT level.

### Condition B — Trias role/evidence profile

**R — target / referent.** Outputs of the chosen DFT setup (`SYNTHETIC`) for the surrogate claim.

**T — theory-level claim.** `PRESENT`: the selected electronic-structure approximation underlying the DFT calculations.

**C — computational practice.** Message-passing neural interatomic potential and its MD rollout.

**Directly assessed relation.** Surrogate computation versus DFT synthetic referent.

**Evidence.** 50,000 training configurations; held-out force MAE 35 meV/Å and energy MAE 2.1 meV/atom; stable 100 ps rollout at 800 K with radial-distribution agreement to the DFT-trained target.

**Use / scope.** 300–1200 K configurations represented by the selected DFT setup.

**Status / explicit non-implication.** DFT-level surrogate fidelity is supported. Experimental material accuracy and robustness to alternative DFT functionals are not established.

### Participant claim items

- **J1.** The neural potential approximates the chosen DFT energies and forces with the reported held-out errors.
- **J2.** The study provides evidence that the surrogate can stably roll out a 100 ps trajectory at 800 K under the reported setup.
- **J3.** The DFT-level error establishes agreement with experimental thermodynamic properties to the same accuracy.
- **J4.** The study establishes invariance of surrogate fidelity to the choice of exchange-correlation functional.
- **J5.** What is the status of a claim about experimental spectroscopic accuracy?
- **J6.** What relation/referent is directly assessed by the held-out energy/force metrics?

---

## SS04 — Tokamak transport surrogate

### Canonical fact sheet

- Scientific use: emulate a computationally expensive gyrokinetic transport code for rapid plasma-profile optimization.
- Synthetic referent: transport fluxes generated by the fixed gyrokinetic code and configuration.
- Surrogate: ensemble neural network.
- Training: 25,000 simulator states within a specified density/temperature-gradient domain.
- Held-out simulator test: median relative flux error 3.2%.
- Surrogate reproduces the simulator’s monotonic trend with temperature gradient over the held-out domain.
- No direct experimental tokamak discharge data are used in the surrogate-validation study.
- The gyrokinetic model’s adequacy for a particular machine/discharge is not evaluated here.
- Surrogate predictions outside the training domain are flagged and not validated.

### Condition A — Generic structured control

**Scientific question / use.** An ensemble neural network emulates transport fluxes from a fixed gyrokinetic code so that plasma-profile optimization can be performed more cheaply.

**Reported evidence.** The surrogate is trained on 25,000 simulator states in a specified density- and temperature-gradient domain. Median relative error on held-out simulator fluxes is 3.2%, and the surrogate reproduces the simulator’s monotonic temperature-gradient trend in that domain.

**Scope / regime.** The evidence concerns the simulator domain represented in training; out-of-domain predictions are flagged and not validated.

**Known limitations / unresolved claims.** No direct tokamak-discharge measurements are included in the surrogate validation. The adequacy of the underlying gyrokinetic model for a specific machine or discharge is not evaluated by this study.

### Condition B — Trias role/evidence profile

**R — target / referent.** Gyrokinetic simulator transport fluxes (`SYNTHETIC`) for the surrogate claim.

**T — theory-level claim.** `PRESENT`: the gyrokinetic transport model encoded by the simulator; target-machine adequacy is not assessed here.

**C — computational practice.** Ensemble neural surrogate.

**Directly assessed relation.** Surrogate computation versus simulator-defined transport referent.

**Evidence.** 25,000 training states; held-out median relative flux error 3.2%; preserved monotonic simulator trend in-domain.

**Use / scope.** Defined density/temperature-gradient domain; out-of-domain predictions are flagged and unvalidated.

**Status / explicit non-implication.** Simulator fidelity is supported in-domain. Real-discharge validation and underlying gyrokinetic model adequacy for a particular machine remain untested in this study.

### Participant claim items

- **J1.** The surrogate reproduces held-out gyrokinetic flux outputs to the reported median error within the training domain.
- **J2.** The surrogate preserves the stated monotonic simulator trend within the tested domain.
- **J3.** The 3.2% simulator error establishes 3.2% error against experimental tokamak discharges.
- **J4.** The surrogate study establishes that the gyrokinetic model is adequate for every tokamak machine.
- **J5.** What is the status of a real-discharge validation claim in this study?
- **J6.** What relation/referent is directly assessed by the 3.2% held-out error?

---

## SS05 — Groundwater-flow emulator

### Canonical fact sheet

- Scientific use: emulate hydraulic-head fields from a calibrated finite-element groundwater simulator for uncertainty propagation.
- Synthetic referent: head fields generated by that fixed simulator after calibration.
- Surrogate: convolutional encoder-decoder.
- Training: 12,000 simulator realizations over permeability fields drawn from the calibration prior.
- Held-out simulator test: spatial RMSE 0.09 m.
- The underlying simulator had previously been calibrated using well measurements, but the surrogate study does not add new observational validation.
- Calibration does not imply that every future hydrogeological regime is validated.
- The surrogate is not evaluated under permeability structures outside the prior family.
- The immediate claim is computational emulation of the calibrated simulator.

### Condition A — Generic structured control

**Scientific question / use.** A convolutional encoder-decoder emulates hydraulic-head fields from a fixed calibrated finite-element groundwater simulator so that uncertainty propagation can be run cheaply.

**Reported evidence.** The surrogate is trained on 12,000 simulator realizations generated from permeability fields drawn from the calibration prior. Spatial RMSE on held-out simulator realizations is 0.09 m. The underlying simulator had previously been calibrated using well measurements.

**Scope / regime.** The surrogate is evaluated only for permeability structures drawn from the same prior family used to generate simulator data.

**Known limitations / unresolved claims.** The surrogate study adds no new observational validation of the physical aquifer. Calibration of the simulator does not by itself establish validity in every future hydrogeological regime. Out-of-family permeability structures are not tested.

### Condition B — Trias role/evidence profile

**R — target / referent.** For the reported surrogate metric, hydraulic-head outputs of the calibrated finite-element simulator (`SYNTHETIC`).

**T — theory-level claim.** `PRESENT`: the groundwater-flow model embodied in the calibrated simulator; its real-target scope is inherited from separate calibration/validation evidence, not established anew here.

**C — computational practice.** Convolutional encoder-decoder surrogate.

**Directly assessed relation.** Surrogate computation versus simulator-defined synthetic head fields.

**Evidence.** 12,000 simulator training realizations; held-out spatial RMSE 0.09 m. The simulator had previously been calibrated to well data.

**Use / scope.** Permeability fields from the calibration-prior family; no out-of-family test.

**Status / explicit non-implication.** Surrogate fidelity to the calibrated simulator is supported in the tested family. The surrogate experiment does not independently validate the real aquifer or unseen hydrogeological regimes.

### Participant claim items

- **J1.** The surrogate reproduces held-out outputs of the calibrated simulator with the reported spatial RMSE.
- **J2.** The study supports use of the surrogate for emulation within the stated permeability-prior family.
- **J3.** The 0.09 m surrogate error directly establishes 0.09 m error relative to future field observations.
- **J4.** Prior calibration of the simulator establishes that every hydrogeological regime generated by the surrogate is physically validated.
- **J5.** What is the status of a claim about surrogate accuracy for permeability structures outside the prior family?
- **J6.** What relation/referent is directly assessed by the 0.09 m held-out metric?

---

## Author-side balance check for Bank A

```text
Black-box candidates      = 5
Synthetic-surrogate       = 5
Directly-supported items  = 20
Unsupported-transfer items= 20
Status items              = 10
Localization items        = 10
```

No candidate is yet valid for the confirmatory instrument. Required next steps are blind expert keying (G0) and independent information-equivalence review (G1).