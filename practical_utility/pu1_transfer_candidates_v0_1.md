# TPUT PU1 Transfer Candidates v0.1

**Status:** CANDIDATE INSTRUMENT / AUTHOR DRAFT / NOT EXPERT-KEYED  
**Date:** 2026-09-04  
**Purpose:** Candidate pool for the two identical unformatted post-test vignettes in TPUT v0.1.

These cases are intentionally presented as plain text. Neither condition receives an `R/T/C` card or a generic structured card at transfer. The goal is to test whether any learned claim-discipline transfers beyond the experimental display format.

Four candidates are provided so that two can be selected only after external expert keying and item-validity review. Selection must not use participant outcome data.

---

## TR01 — Weather-model surrogate with observational mismatch

A neural surrogate is trained to emulate hourly precipitation fields from a regional numerical weather model. It is trained on 18,000 simulator outputs and tested on 2,000 held-out simulator cases from the same season and geographical domain. On those held-out simulations, the surrogate has a spatial RMSE of 0.6 mm/h and reproduces the simulator’s domain-mean rainfall within 2%. For a separate descriptive check, both the simulator and the surrogate are compared with rain-gauge observations on 20 days. The simulator has a gauge RMSE of 2.4 mm/h and the surrogate has 2.5 mm/h. The surrogate therefore tracks the simulator closely, but neither matches the gauges nearly as well as the surrogate matches its teacher. No additional calibration to gauges is performed.

### Candidate claim items

- **T1.** The surrogate closely reproduces the numerical weather model on held-out simulator cases.
- **T2.** The 0.6 mm/h surrogate-to-simulator RMSE establishes 0.6 mm/h accuracy relative to rain gauges.
- **T3.** The separate gauge comparison provides some direct evidence about real-observation performance of both simulator and surrogate.
- **T4.** The teacher-fidelity result by itself establishes that the simulator is physically valid.

---

## TR02 — Physics-constrained cardiac activation model

A neural model predicts electrical activation times on patient-specific cardiac meshes. During training, the loss includes a residual derived from an eikonal propagation equation and sparse clinical activation measurements. In a held-out set of 25 patients, median activation-time error is 9 ms. The eikonal residual is also small on the computational mesh. The study notes that the eikonal equation does not explicitly represent several cellular conduction mechanisms and that arrhythmic cases with scar-related conduction block are underrepresented. In the five held-out patients with the largest scar burden, median error is 24 ms. No claim is made that the learned latent representation identifies cellular electrophysiological mechanisms.

### Candidate claim items

- **T1.** The model has the reported held-out activation-time error on the studied patients.
- **T2.** The low eikonal residual establishes that all relevant cellular conduction mechanisms are correctly represented.
- **T3.** The evidence indicates weaker performance in the high-scar subgroup than in the overall held-out set.
- **T4.** Predictive performance establishes that the latent representation is a unique mechanistic explanation of cardiac conduction.

---

## TR03 — Equation discovery with two observationally competitive models

A sparse equation-discovery pipeline is applied to experimental concentration data from an oscillatory chemical reactor. Two candidate models are retained after repeated resampling. Model A and Model B contain different nonlinear interaction terms. On held-out initial conditions, both reproduce the dominant oscillation period within 3%; Model A has lower concentration RMSE, whereas Model B more accurately reproduces the phase response to a small perturbation. The experiment does not directly measure the intermediate chemical species that would distinguish the two candidate pathways. The authors therefore present both as viable reduced models and state that an additional targeted experiment would be required to discriminate the underlying reaction mechanism.

### Candidate claim items

- **T1.** Both candidate models have evidence for selected held-out dynamical adequacy.
- **T2.** Model A’s lower concentration RMSE establishes that its nonlinear interaction terms are the uniquely correct chemical mechanism.
- **T3.** The current experiment leaves pathway discrimination unresolved.
- **T4.** Similar oscillation periods imply that the two candidate equations are physically equivalent in every respect.

---

## TR04 — Black-box microscopy classifier used for scientific screening

A convolutional network classifies microscopy images of cultured cells into two experimentally defined phenotypes. The model is trained on images from four experimental batches and evaluated on a fifth batch acquired with the same microscope and staining protocol. Accuracy is 94%, compared with 82% for a hand-crafted-feature baseline. A saliency analysis highlights membrane regions in many correctly classified images, but no intervention or independent biological assay tests whether those highlighted regions cause the phenotype. A sixth batch acquired with a different staining protocol is not evaluated. The intended use is rapid screening of images produced by the original protocol.

### Candidate claim items

- **T1.** The network outperforms the stated baseline on the held-out fifth batch.
- **T2.** The saliency maps establish that membrane regions are the causal biological mechanism of the phenotype.
- **T3.** The study directly supports screening performance under the original imaging/staining protocol.
- **T4.** The held-out fifth-batch result establishes accuracy under a different staining protocol.

---

## Transfer-candidate constraint

The final two transfer cases should be chosen only after:

```text
expert key agreement >= 4/5 for every scored item
no required specialist knowledge outside the text
no obvious lexical cue that simply repeats training examples
coverage of at least two different archetypes
no participant outcome data viewed
```

The transfer items remain exploratory and cannot rescue a failed primary G3 result.