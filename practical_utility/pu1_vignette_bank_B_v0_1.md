# TPUT PU1 Vignette Bank B v0.1 — Physics-Informed / Hybrid ML + Equation Discovery

**Status:** CANDIDATE INSTRUMENT / AUTHOR DRAFT / NOT EXPERT-KEYED  
**Date:** 2026-09-04  
**Parent:** `practical_utility/research_program_v0_1.md`  
**Decision:** D040

## Instrument rule

Each candidate has one canonical fact sheet and two information-equivalent renderings. Trias labels may reorganize the same facts but may not add scientific evidence. Participant-facing items are identical between arms. Author-intended keys are stored separately and must be hidden from external keying experts in their first round.

---

# PHYSICS-INFORMED / HYBRID ML

## PI01 — Heat-equation PINN with sparse sensors

### Canonical fact sheet

- Scientific use: reconstruct a 2D transient temperature field in a laboratory metal plate from sparse thermocouples.
- Real target: measured plate temperatures.
- Theory-level content: homogeneous heat equation with fixed conductivity and no internal heat source.
- Computational practice: physics-informed neural network constrained by the heat-equation residual plus sensor data.
- Training uses 12 thermocouples; evaluation uses 8 withheld thermocouples.
- At withheld sensors, temperature RMSE is 0.42 K.
- The PDE residual on a dense collocation set is low relative to the training scale.
- Infrared images reveal a localized heater defect during one time interval; this effect is not represented by the homogeneous PDE.
- During the defect interval, withheld-sensor RMSE rises to 1.8 K.
- The study does not claim that low residual proves the homogeneous PDE is fully adequate for the defective plate.

### Condition A — Generic structured control

**Scientific question / use.** A physics-informed neural network reconstructs transient temperature on a laboratory metal plate from sparse sensors. The model is constrained by a homogeneous heat equation with fixed conductivity and no internal heat source.

**Reported evidence.** Twelve thermocouples are used for training and eight are withheld for evaluation. Overall withheld-sensor RMSE is 0.42 K, and the differential-equation residual is low on a dense collocation set. Infrared imaging independently reveals a localized heater defect during one interval. In that interval, withheld-sensor RMSE increases to 1.8 K.

**Scope / regime.** Most measurements are approximately compatible with the homogeneous model; the defect interval is a known regime mismatch.

**Known limitations / unresolved claims.** The low PDE residual shows that the computational solution satisfies the encoded equation well; it does not by itself establish that the homogeneous equation captures the localized heater defect.

### Condition B — Trias role/evidence profile

**R — target / referent.** Physical plate temperatures measured by thermocouples and infrared imaging (`REAL`).

**T — theory-level claim.** `PARTIAL`: homogeneous heat equation with fixed conductivity; the localized heater defect is not represented.

**C — computational practice.** PINN combining sensor data with the heat-equation residual.

**Directly assessed relations.** PDE residual bears on `T-C`; withheld real sensors bear on `C-R`; infrared evidence reveals a limitation in `R-T` adequacy during the defect interval.

**Evidence.** 12 training sensors, 8 withheld sensors; overall RMSE 0.42 K; low PDE residual. During the independently detected defect interval, withheld RMSE rises to 1.8 K.

**Use / scope.** Plate experiment with one known regime mismatch.

**Status / explicit non-implication.** Encoded-equation satisfaction can be strong while target adequacy is only partial; low residual does not prove the homogeneous theory is complete.

### Participant claim items

- **J1.** The network predicts the withheld thermocouple temperatures with the reported overall RMSE.
- **J2.** The low residual supports that the computational solution approximately satisfies the encoded heat equation on the collocation set.
- **J3.** The low residual establishes that the homogeneous heat equation fully describes the plate during the heater-defect interval.
- **J4.** The overall 0.42 K RMSE establishes that no physically relevant regime mismatch is present.
- **J5.** What is the status of the homogeneous-theory adequacy claim during the defect interval?
- **J6.** Which relation is most directly supported by the low PDE residual, and which by the withheld-sensor RMSE?

---

## PI02 — Conservation-constrained river-flow predictor

### Canonical fact sheet

- Scientific use: forecast downstream river discharge 6 hours ahead.
- Real target: gauge measurements at a downstream station.
- Computational practice: neural sequence model with a penalty enforcing mass-balance consistency across three gauged reaches.
- Theory-level content: local water mass conservation over the modeled reaches.
- Training: five years of gauge/rainfall data.
- Held-out test: one later year.
- Test MAE: 18 m^3/s; unconstrained neural baseline: 22 m^3/s.
- Mean mass-balance discrepancy is reduced by 70% relative to the unconstrained baseline.
- An ungauged tributary enters during extreme storms and is absent from the balance model.
- For the top 2% discharge events, MAE is 61 m^3/s and no separate unconstrained-baseline advantage is established.

### Condition A — Generic structured control

**Scientific question / use.** A neural sequence model forecasts downstream discharge six hours ahead and includes a penalty for water-mass balance over three gauged river reaches.

**Reported evidence.** Five years of gauge and rainfall data are used for training and one later year is held out. Test MAE is 18 m^3/s, compared with 22 m^3/s for an otherwise similar unconstrained neural model. Mean mass-balance discrepancy is 70% lower than in the unconstrained baseline.

**Scope / regime.** The balance model covers the three gauged reaches. During extreme storms, an ungauged tributary contributes flow that is not represented.

**Known limitations / unresolved claims.** For the top 2% discharge events, MAE rises to 61 m^3/s, and the study does not establish a separate extreme-event advantage of the constraint.

### Condition B — Trias role/evidence profile

**R — target / referent.** Physical downstream-gauge discharge (`REAL`).

**T — theory-level claim.** `PARTIAL`: mass conservation over the three modeled reaches; an ungauged tributary is omitted during extreme storms.

**C — computational practice.** Sequence predictor with a mass-balance penalty.

**Directly assessed relations.** Reduced balance discrepancy supports `T-C`; held-out gauge accuracy supports `C-R`.

**Evidence.** Five years training, one-year chronological test; MAE 18 versus 22 m^3/s for the unconstrained baseline; 70% lower mean mass-balance discrepancy. Extreme top-2% MAE is 61 m^3/s.

**Use / scope.** Ordinary represented flow regimes are better covered than extreme storms with the ungauged tributary.

**Status / explicit non-implication.** Constraint satisfaction and ordinary predictive improvement are supported, but they do not establish complete hydrological adequacy or extreme-event superiority.

### Participant claim items

- **J1.** The constrained model has lower overall held-out MAE than the stated unconstrained baseline.
- **J2.** The conservation penalty reduces the reported mass-balance discrepancy relative to the baseline.
- **J3.** The reduced balance discrepancy establishes that all relevant inflows, including the ungauged tributary, are physically represented during extreme storms.
- **J4.** The overall test result establishes superior prediction for the top 2% extreme events.
- **J5.** What is the status of a claim that the encoded balance model is complete during extreme storms?
- **J6.** Which relation is directly addressed by the balance discrepancy and which by held-out gauge error?

---

## PI03 — Hamiltonian neural oscillator model

### Canonical fact sheet

- Scientific use: learn long-horizon dynamics of a laboratory coupled-pendulum system.
- Real target: motion-capture trajectories of the physical apparatus.
- Computational practice: Hamiltonian neural network (HNN).
- Theory-level content: conservative Hamiltonian structure with no explicit damping term.
- Training uses low-amplitude trajectories where damping is weak over the observation horizon.
- Held-out low-amplitude rollout error after 20 periods is 0.08 normalized units; standard neural ODE error is 0.19.
- HNN energy drift is much smaller than standard neural ODE energy drift.
- At high amplitudes the physical apparatus exhibits measurable frictional damping.
- No high-amplitude test is included in the main evaluation.
- The authors do not claim that the real apparatus is exactly conservative.

### Condition A — Generic structured control

**Scientific question / use.** A Hamiltonian neural network learns long-horizon coupled-pendulum dynamics from laboratory trajectories. Its architecture encodes conservative Hamiltonian structure and contains no explicit damping term.

**Reported evidence.** Training and testing use low-amplitude motions where damping is weak over the measured horizon. After 20 periods, normalized rollout error is 0.08 for the HNN and 0.19 for a standard neural ODE. The HNN also exhibits much smaller energy drift.

**Scope / regime.** The evaluation concerns low-amplitude motions.

**Known limitations / unresolved claims.** At high amplitudes the physical apparatus has measurable frictional damping, and the main study contains no high-amplitude test. The authors do not claim that the apparatus is exactly conservative.

### Condition B — Trias role/evidence profile

**R — target / referent.** Physical coupled-pendulum trajectories (`REAL`).

**T — theory-level claim.** `PARTIAL`: conservative Hamiltonian structure is a useful approximation in the low-amplitude regime; high-amplitude friction is known.

**C — computational practice.** Hamiltonian neural network without explicit damping.

**Directly assessed relations.** Reduced energy drift concerns theory–computation structure; low-amplitude rollout error concerns computation–target adequacy.

**Evidence.** At low amplitude, 20-period rollout error 0.08 versus 0.19 for neural ODE; much smaller HNN energy drift. High-amplitude data are not tested.

**Use / scope.** Low-amplitude weak-damping regime.

**Status / explicit non-implication.** Structure preservation and low-amplitude prediction are supported; exact conservativity of the physical apparatus and high-amplitude adequacy are not established.

### Participant claim items

- **J1.** The HNN has lower reported low-amplitude long-horizon rollout error than the stated neural-ODE baseline.
- **J2.** The HNN better preserves the encoded Hamiltonian energy structure in the reported comparison.
- **J3.** The low energy drift establishes that the physical apparatus is exactly conservative at all amplitudes.
- **J4.** The low-amplitude test establishes HNN accuracy in the untested high-amplitude frictional regime.
- **J5.** What is the status of an exact-conservativity claim for the real apparatus?
- **J6.** Which relation is directly supported by energy-drift evidence and which by physical rollout error?

---

## PI04 — PDE-constrained atmospheric downscaling

### Canonical fact sheet

- Scientific use: downscale coarse atmospheric fields to local wind fields over complex terrain.
- Real target: meteorological mast observations.
- Computational practice: convolutional network with a penalty on approximate mass continuity and terrain boundary conditions.
- Theory-level content: incompressible/anelastic-style local continuity approximation plus no-flow terrain condition.
- Training uses reanalysis inputs and 15 masts for two years.
- Test uses a third year at the same masts.
- Wind-speed RMSE: 1.3 m/s, versus 1.6 m/s for the same network without physical penalties.
- Mean continuity residual is 55% lower than for the unconstrained network.
- Stable nocturnal boundary layers are poorly represented by the training data and have RMSE 2.4 m/s.
- The continuity approximation does not encode all turbulence/stratification physics.

### Condition A — Generic structured control

**Scientific question / use.** A convolutional network downscales coarse atmospheric fields to local terrain-resolved wind and is penalized for violation of an approximate continuity equation and terrain boundary condition.

**Reported evidence.** Two years of reanalysis and observations from 15 masts are used for training; a third year at the same masts is held out. Wind-speed RMSE is 1.3 m/s compared with 1.6 m/s for the same architecture without physical penalties. Mean continuity residual is 55% lower.

**Scope / regime.** The test covers the same mast sites. Stable nocturnal boundary layers are sparse in training and show RMSE 2.4 m/s.

**Known limitations / unresolved claims.** The encoded constraints do not include all turbulence and stratification physics; satisfying continuity does not by itself establish complete atmospheric adequacy.

### Condition B — Trias role/evidence profile

**R — target / referent.** Physical mast wind observations (`REAL`).

**T — theory-level claim.** `PARTIAL`: continuity and terrain boundary conditions are encoded, but not complete turbulence/stratification physics.

**C — computational practice.** PDE-constrained convolutional downscaler.

**Directly assessed relations.** Continuity residual addresses `T-C`; mast RMSE addresses `C-R`.

**Evidence.** Third-year RMSE 1.3 m/s versus 1.6 m/s without constraints; continuity residual 55% lower. Stable nocturnal cases show 2.4 m/s RMSE.

**Use / scope.** Same mast sites; nocturnal stable boundary layer underrepresented.

**Status / explicit non-implication.** Constraint satisfaction and overall site-level prediction improve, but complete physical adequacy and strong nocturnal performance are not established.

### Participant claim items

- **J1.** The physically penalized network has lower overall third-year wind RMSE than the unconstrained version.
- **J2.** The reported continuity residual is lower for the constrained model.
- **J3.** The reduced continuity residual establishes that all relevant atmospheric physics are represented.
- **J4.** The overall improvement establishes equally strong performance in stable nocturnal boundary layers.
- **J5.** What is the status of a claim of complete theory adequacy for the encoded constraints?
- **J6.** Which relation is directly tested by continuity-residual evidence and which by mast RMSE?

---

## PI05 — Reaction-diffusion hybrid surrogate with learned closure

### Canonical fact sheet

- Scientific use: predict concentration fields in a laboratory reaction-diffusion experiment.
- Real target: fluorescence-derived concentration fields.
- Theory-level content: known diffusion and two known reaction terms; one unresolved reaction term is represented by a learned closure.
- Computational practice: differentiable PDE solver plus neural closure.
- Training uses six experimental runs; testing uses two held-out runs at interpolation parameter settings.
- Test field RMSE: 4.5% of concentration range; mechanistic model without learned closure: 9.8%.
- Learned closure is constrained to be nonnegative but is not identified with a known chemical pathway.
- No extrapolation to temperatures outside the training range is tested.
- Several distinct closure networks achieve similar held-out field errors.
- The study claims predictive correction, not unique discovery of the missing chemistry.

### Condition A — Generic structured control

**Scientific question / use.** A differentiable reaction-diffusion model predicts laboratory concentration fields. Diffusion and two reaction terms are specified mechanistically; one unresolved contribution is represented by a nonnegative neural closure.

**Reported evidence.** Six experimental runs are used for training and two interpolation-regime runs are held out. Field RMSE is 4.5% of the concentration range, versus 9.8% for the mechanistic model without the learned closure. Several distinct closure networks achieve similar held-out errors.

**Scope / regime.** Testing is interpolative within the experimental parameter range.

**Known limitations / unresolved claims.** The learned closure is not identified with a known chemical pathway. No outside-temperature extrapolation is tested. Similar predictive errors from distinct closures leave the missing chemistry structurally non-unique.

### Condition B — Trias role/evidence profile

**R — target / referent.** Experimental concentration fields (`REAL`).

**T — theory-level claim.** `PARTIAL`: known diffusion/reaction terms plus an unresolved contribution; the neural closure is not claimed as a unique mechanism.

**C — computational practice.** Differentiable PDE solver with learned nonnegative closure.

**Directly assessed relations.** Held-out field error addresses `C-R`; known/unknown reaction content concerns `R-T`; implementation of constraints belongs to `T-C`.

**Evidence.** Two held-out interpolation runs: 4.5% field RMSE versus 9.8% without learned closure. Multiple closure networks reach similar errors.

**Use / scope.** Interpolation within training temperatures; no outside-range test.

**Status / explicit non-implication.** Predictive correction is supported, but a unique missing chemical pathway is not identified and extrapolation is untested.

### Participant claim items

- **J1.** The hybrid model has lower held-out field error than the mechanistic model without the learned closure.
- **J2.** The study supports predictive value of the learned closure in the interpolation regime.
- **J3.** Similar predictive performance establishes that one learned closure is the unique missing chemical mechanism.
- **J4.** The interpolation test establishes performance at temperatures outside the training range.
- **J5.** What is the status of a claim that the neural closure identifies a unique chemical pathway?
- **J6.** What relation/referent is directly assessed by the held-out concentration-field RMSE?

---

# EQUATION DISCOVERY

## ED01 — Synthetic nonlinear oscillator with omitted coordinate

### Canonical fact sheet

- Scientific use: infer an equation for observed coordinate `x(t)` of a synthetic three-state nonlinear oscillator.
- Synthetic target: simulator with known three-state equations.
- Only `x(t)` and `y(t)` are supplied to the inference algorithm; latent state `z(t)` is omitted.
- Computational practice: sparse polynomial equation discovery on reconstructed derivatives.
- Discovered two-state model gives low one-step derivative error and reproduces the dominant oscillation frequency over 100 periods.
- The discovered equation contains an `x^3` term not present in the projected true `x` equation before eliminating `z`.
- Repeated runs with different smoothing strengths yield two different sparse supports with similar frequency error.
- The study does not claim unique structural recovery.
- The full simulator equations are available to the experimenters for benchmarking.

### Condition A — Generic structured control

**Scientific question / use.** Sparse polynomial regression is used to infer a two-state equation from `x(t)` and `y(t)` generated by a known synthetic three-state nonlinear oscillator. The latent state `z(t)` is intentionally omitted from the inference data.

**Reported evidence.** The inferred model has low one-step derivative error and reproduces the dominant oscillation frequency over 100 periods. Its `x` equation contains an `x^3` term not present in the original projected `x` equation before eliminating the unobserved state. Different smoothing strengths produce two sparse supports with similar frequency error.

**Scope / regime.** The experiment concerns a partially observed synthetic benchmark whose full generating equations are known to the researchers.

**Known limitations / unresolved claims.** Similar dynamics are obtained from different inferred supports; the study therefore does not claim unique structural recovery of the generating equations.

### Condition B — Trias role/evidence profile

**R — target / referent.** Known synthetic three-state oscillator (`SYNTHETIC`).

**T — theory-level claim.** `INFERRED`: candidate two-state symbolic equations are outputs of the computational inference.

**C — computational practice.** Sparse polynomial equation discovery after derivative reconstruction from observed `x,y`.

**Directly assessed relations.** Dynamical agreement of inferred models with the synthetic target is distinct from structural identification of the generating equation.

**Evidence.** Low derivative error; dominant frequency reproduced for 100 periods; an `x^3` term appears; two smoothing choices yield distinct sparse supports with similar frequency error.

**Use / scope.** Partially observed synthetic benchmark with omitted `z`.

**Status / explicit non-implication.** Dynamical adequacy is supported for selected quantities, while unique structural recovery is not established.

### Participant claim items

- **J1.** The discovered models reproduce the dominant oscillation frequency of the synthetic target over the reported horizon.
- **J2.** Different smoothing choices yield different sparse supports with similar reported frequency error.
- **J3.** The low dynamical error establishes that the discovered support is the unique generating equation of the full three-state system.
- **J4.** The presence of an `x^3` term establishes that this term is a literal physical mechanism in the original three-state generator.
- **J5.** What is the status of unique structural recovery in this experiment?
- **J6.** Which claim is directly supported by the frequency comparison: target-relative dynamical adequacy or unique theory identification?

---

## ED02 — Predator–prey inference under measurement noise

### Canonical fact sheet

- Scientific use: infer governing interaction terms from a synthetic predator–prey system with known equations.
- Synthetic target: modified Lotka–Volterra generator with one saturation term.
- Observations: both states sampled sparsely with 3% additive Gaussian noise.
- Computational practice: sparse equation discovery after smoothing and numerical differentiation.
- Across 20 noise realizations, the saturation term is recovered in 13 runs.
- In 7 runs, a simpler polynomial interaction term replaces it.
- Both model classes reproduce mean oscillation period within 5% over a held-out trajectory.
- Coefficient estimates of the recovered saturation term vary by 18% across successful runs.
- The study does not claim seed-robust exact structure recovery.
- The generating equations are known for evaluation.

### Condition A — Generic structured control

**Scientific question / use.** Sparse equation discovery is applied to noisy, sparsely sampled observations from a known synthetic predator–prey system containing a saturation interaction.

**Reported evidence.** Across 20 independent noise realizations, the true saturation term is recovered in 13 runs. In the remaining seven, a simpler polynomial interaction is selected. Both classes reproduce the held-out mean oscillation period within 5%. Among successful saturation recoveries, its coefficient varies by 18%.

**Scope / regime.** The result concerns this noise level, sampling scheme, library, and sparse-regression pipeline on a synthetic benchmark.

**Known limitations / unresolved claims.** Exact structural recovery is not stable across noise realizations even though a selected dynamical quantity is often reproduced.

### Condition B — Trias role/evidence profile

**R — target / referent.** Known synthetic predator–prey generator (`SYNTHETIC`).

**T — theory-level claim.** `INFERRED`: interaction terms are produced by sparse computational inference.

**C — computational practice.** Smoothing, differentiation, and sparse equation discovery.

**Directly assessed relations.** Structural recovery can be benchmarked against the known target theory; held-out period agreement separately assesses selected dynamical adequacy.

**Evidence.** Saturation term recovered in 13/20 noise runs; alternative polynomial term in 7/20; both within 5% period error; recovered saturation coefficient varies 18%.

**Use / scope.** Frozen noise/sampling/library setup.

**Status / explicit non-implication.** Some structural evidence exists but exact seed-robust identification is not established; period agreement does not rescue structural instability.

### Participant claim items

- **J1.** The true saturation term is recovered in 13 of the 20 reported noise realizations.
- **J2.** Both recovered model classes reproduce the selected oscillation period within the reported tolerance.
- **J3.** Period agreement within 5% establishes exact structural identification in all 20 runs.
- **J4.** Recovery in 13/20 runs establishes that the inferred coefficient is stable across all noise realizations.
- **J5.** What is the status of seed-robust exact structural recovery?
- **J6.** Which evidence concerns structural identification and which concerns target-relative dynamical adequacy?

---

## ED03 — Fluid-wake reduced-coordinate equation discovery

### Canonical fact sheet

- Scientific use: infer low-dimensional equations for two POD coefficients measured from a cylinder-wake experiment.
- Real target: experimentally measured POD coefficient trajectories.
- Computational practice: sparse polynomial equation discovery.
- Candidate model A and candidate model B have different nonlinear terms.
- Both achieve similar one-step derivative RMSE on held-out trajectories.
- Forward simulations reproduce the dominant shedding frequency within 2% for both models.
- Model A reproduces amplitude distribution better; model B reproduces phase diffusion better.
- No independent measurement can identify which candidate nonlinear term corresponds to a unique physical mechanism.
- The POD truncation omits higher modes containing about 8% of measured fluctuation energy.
- The study claims useful reduced dynamical models, not unique full-fluid equations.

### Condition A — Generic structured control

**Scientific question / use.** Sparse polynomial regression is used to infer low-dimensional equations for two experimentally measured POD coefficients of a cylinder wake.

**Reported evidence.** Two candidate models with different nonlinear terms have similar held-out derivative RMSE. Forward simulations from both reproduce the dominant shedding frequency within 2%. Model A better matches the amplitude distribution, while model B better matches phase diffusion.

**Scope / regime.** The analysis concerns a two-mode reduced representation. Higher POD modes containing about 8% of fluctuation energy are omitted.

**Known limitations / unresolved claims.** Available measurements do not uniquely identify which candidate nonlinear structure is the physical mechanism. The study treats both as reduced dynamical models, not as uniquely recovered full-fluid equations.

### Condition B — Trias role/evidence profile

**R — target / referent.** Experimental POD-coordinate trajectories (`REAL`), with an explicit two-mode reduced scope.

**T — theory-level claim.** `INFERRED`: alternative reduced symbolic dynamics A and B.

**C — computational practice.** Sparse polynomial equation discovery plus forward simulation of candidates.

**Directly assessed relations.** Held-out dynamical metrics support target-relative reduced-model adequacy; they do not uniquely establish which inferred nonlinear structure is mechanistically correct.

**Evidence.** Similar derivative RMSE; both within 2% shedding-frequency error; A better amplitude distribution, B better phase diffusion. Higher modes carry ~8% omitted energy.

**Use / scope.** Two-POD-coordinate reduced dynamics.

**Status / explicit non-implication.** Multiple candidates are empirically competitive on different QoIs; unique mechanism identification remains uncertain/untested.

### Participant claim items

- **J1.** Both candidate reduced models reproduce the dominant shedding frequency within the stated tolerance.
- **J2.** The two candidates have different strengths on amplitude distribution and phase diffusion.
- **J3.** Similar derivative error establishes that one candidate’s nonlinear terms are the uniquely correct physical mechanism of the full wake.
- **J4.** The two-mode result establishes a complete equation for all experimentally measured fluctuation dynamics.
- **J5.** What is the status of unique mechanistic identification of the candidate nonlinear terms?
- **J6.** What relation/referent is directly assessed by the held-out reduced-coordinate trajectory comparisons?

---

## ED04 — Chemical reaction-network discovery

### Canonical fact sheet

- Scientific use: infer reaction terms from concentration time series in a controlled laboratory reactor.
- Real target: measured concentrations of four observable species.
- Computational practice: sparse reaction-library selection constrained by mass-action form.
- Candidate network reproduces all four observed species with normalized RMSE 0.04 on held-out initial conditions.
- A second candidate network, containing one additional hidden intermediate, produces normalized RMSE 0.045.
- The hidden intermediate is not directly measured.
- Both candidates satisfy elemental-balance constraints.
- An isotope-label experiment that could distinguish pathways is not performed.
- The study supports predictive reaction-network candidates but does not claim unique pathway identification.
- The candidate terms are interpretable within the chosen reaction library.

### Condition A — Generic structured control

**Scientific question / use.** A sparse mass-action reaction library is used to infer candidate reaction networks from four measured species in a controlled laboratory reactor.

**Reported evidence.** One candidate predicts all four observed species on held-out initial conditions with normalized RMSE 0.04. A second network containing one extra hidden intermediate gives RMSE 0.045. Both satisfy elemental-balance constraints.

**Scope / regime.** Evaluation uses the four observable species and the tested initial-condition range.

**Known limitations / unresolved claims.** The hidden intermediate is not measured, and no isotope-label experiment is performed to distinguish pathways. The study therefore supports predictive candidate networks but not a unique chemical pathway.

### Condition B — Trias role/evidence profile

**R — target / referent.** Physical concentration measurements of four observable species (`REAL`).

**T — theory-level claim.** `INFERRED`: alternative mass-action reaction networks, one with an unobserved intermediate.

**C — computational practice.** Sparse reaction-library selection under balance constraints.

**Directly assessed relations.** Held-out concentration prediction bears on computation/forward candidate adequacy relative to the real target; pathway uniqueness requires additional target–theory discrimination.

**Evidence.** Candidate RMSEs 0.04 and 0.045; both satisfy elemental balance. No isotope-label test; hidden intermediate unobserved.

**Use / scope.** Four measured species and tested initial conditions.

**Status / explicit non-implication.** Predictive candidate adequacy is supported; unique pathway identification is not established.

### Participant claim items

- **J1.** Both candidate networks reproduce the four measured species with similar low held-out error.
- **J2.** Both candidates satisfy the stated elemental-balance constraint.
- **J3.** The slightly lower RMSE of the first candidate establishes that its reaction pathway is uniquely correct.
- **J4.** Elemental-balance satisfaction establishes that the unmeasured hidden intermediate does not exist.
- **J5.** What is the status of unique reaction-pathway identification without the isotope-label experiment?
- **J6.** What does the held-out concentration RMSE directly support: predictive candidate adequacy or unique mechanism identification?

---

## ED05 — Power-grid oscillator equation inference

### Canonical fact sheet

- Scientific use: infer reduced phase-dynamics equations from phasor measurement unit (PMU) data in a controlled microgrid experiment.
- Real target: measured phase/frequency trajectories under small disturbances.
- Computational practice: sparse equation discovery in a library containing linear damping and sinusoidal coupling terms.
- Candidate model correctly recovers the sign pattern of all four known physical network couplings.
- Coupling magnitudes differ from engineering reference values by 6–14%.
- Held-out small-disturbance trajectories have phase RMSE 0.03 rad.
- Large fault events are not included in training or testing.
- Two weak extra coupling terms appear in 3 of 10 bootstrap fits and disappear in the other 7.
- The study treats the sign pattern as supported but weak extra terms as uncertain.
- No claim is made about large-disturbance stability from this experiment.

### Condition A — Generic structured control

**Scientific question / use.** Sparse equation discovery is applied to PMU data from a controlled microgrid to infer reduced phase-dynamics equations containing damping and sinusoidal coupling terms.

**Reported evidence.** The inferred model recovers the sign pattern of all four known physical network couplings. Coupling magnitudes differ from engineering reference values by 6–14%. Held-out small-disturbance phase trajectories have RMSE 0.03 rad. Two weak extra couplings appear in three of ten bootstrap fits but not in the other seven.

**Scope / regime.** Training and testing use small disturbances.

**Known limitations / unresolved claims.** Large fault events are not evaluated. The known coupling sign pattern is comparatively stable, while the extra weak terms are bootstrap-unstable and treated as uncertain.

### Condition B — Trias role/evidence profile

**R — target / referent.** Physical PMU trajectories and engineering network reference information (`REAL`).

**T — theory-level claim.** `INFERRED`: reduced phase-dynamics coupling structure, with stable known signs and uncertain weak extra terms.

**C — computational practice.** Sparse equation discovery with bootstrap stability assessment.

**Directly assessed relations.** Structural comparison against known couplings and held-out small-disturbance dynamics are distinct evidence components.

**Evidence.** Correct signs for four known couplings; magnitude errors 6–14%; held-out phase RMSE 0.03 rad; two extra terms present in 3/10 bootstrap fits.

**Use / scope.** Small disturbances only; no large-fault test.

**Status / explicit non-implication.** Known sign structure is supported in this setting; weak extra terms are uncertain, and large-disturbance stability remains untested.

### Participant claim items

- **J1.** The inferred model recovers the reported sign pattern of the four known physical couplings.
- **J2.** The candidate model reproduces held-out small-disturbance phase trajectories with the reported RMSE.
- **J3.** Appearance of two extra terms in 3/10 bootstraps establishes those terms as real physical couplings.
- **J4.** The small-disturbance test establishes large-fault stability of the inferred model.
- **J5.** What is the status of the two weak extra coupling terms?
- **J6.** Which evidence bears on structural recovery and which on target-relative dynamical prediction?

---

## Author-side balance check for Bank B

```text
Physics-informed / hybrid candidates = 5
Equation-discovery candidates         = 5
Directly-supported items              = 20
Unsupported-transfer items            = 20
Status items                          = 10
Localization items                    = 10
```

No candidate is yet valid for confirmatory use. External G0 expert keying and independent G1 information-equivalence review remain mandatory.