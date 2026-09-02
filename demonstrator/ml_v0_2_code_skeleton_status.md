# ML v0.2 Code Skeleton — Resolvability Repair

**Status:** READY FOR REVIEW  
**Depends on:** D013–D014  
**Scientific claim status:** C07 remains unassessed; no v0.2 scientific Full Run has been interpreted.

## Implemented changes relative to v0.1

Only the two D014-approved changes were introduced:

1. deterministic phase-stratified five-point block splitting;
2. one shared, teacher-independent target scaler derived only from the training targets of both teachers.

The existing v0.1 data generator, Figure-eight target, DOP853/RK4 teacher definitions and base Residual-MLP are reused rather than silently replaced.

## New code paths

- `src/trias_demo/ml_v0_2_data.py`
  - `phase_block_split`;
  - `generate_dataset_v0_2` reuses v0.1 teacher generation and replaces only the split;
  - training-only input scaler;
  - shared target scaler;
  - target scale/unscale helpers.
- `src/trias_demo/ml_v0_2_model.py`
  - bit-identical paired initialization;
  - training on the shared standardized target coordinates;
  - inverse target transform before physical next-state prediction.
- `src/trias_demo/ml_experiment_v0_2.py`
  - v0.2 dataset/scaler persistence;
  - raw-coordinate one-step metrics on train/validation/test;
  - G1/G2/G3/G3a reporting;
  - provenance decomposition in raw coordinates;
  - MU1/MU2 pipeline for the later Full Run;
  - non-scientific `--smoke` mode.
- `tests/test_ml_v0_2_skeleton.py`
  - exact full-size 200-block / 600-200-200 split check;
  - no block splitting across partitions;
  - training-only/shared scaler checks and numerical inverse-transform check;
  - bit-identical pair initialization and finite tiny training.

The CLI entry point is `trias-ml-demo-v02`.

## Local technical validation

The v0.2 wrappers and tests were executed locally against the current v0.1 code semantics:

```text
PYTHONPATH=src pytest -q tests/test_ml_v0_2_skeleton.py
3 passed
```

A separate contract-level split test for `N=1000` confirms exactly 200 five-point blocks and 600/200/200 samples.

## Non-scientific Smoke Run

Executed with the v0.2 code path using:

```text
N = 100
seed = 0
max_epochs = 30
patience = 10
```

These values are deliberately not the scientific Full Run settings.

Technical results:

```text
gate_status = SMOKE_ONLY
G1 reference separation = True on train/validation/test
G2 paired-control integrity = True
D_teacher_test = 1.2628148573e-05
D_ref_test = 8.9846501364e-14
median smoke test RMSE ref model  = 6.3543937701e-02
median smoke test RMSE rk4 model  = 6.3551465222e-02
```

The target scaling/inverse-scaling roundtrip closed to approximately `5.6e-17`, and the provenance identity residual in the technical smoke diagnostic was approximately `-3.7e-18`.

The smoke learner errors are not interpreted. Thirty epochs and `N=100` are only a pipeline test, so the failed smoke G3/G3a values are neither evidence for nor against the v0.2 scientific design.

## Important implementation note

If G1–G3 pass in the later frozen Full Run, the code records the intermediate technical status

```text
GATES_PASSED_AWAITING_SCIENTIFIC_CLASSIFICATION
```

rather than auto-declaring `INFORMATIVE_POSITIVE` or `INFORMATIVE_NEGATIVE`. The final allowed scientific status is assigned only during the preregistered result review, because the Contract does not define a single automatic numerical threshold that distinguishes positive from negative provenance evidence once the resolvability gates pass.

If G1, G2 or G3 fail, the corresponding preregistered failure status is assigned directly.

## Still not executed

- scientific `N=1000` v0.2 dataset/training run;
- all six full-budget teacher/seed trainings;
- scientific G3/G3a result;
- MU1/MU2 scientific interpretation;
- C07 decision;
- comparison with a strong standard ML provenance/credibility framework.

## Review recommendation

**ACCEPT the v0.2 code skeleton.** It implements the two approved resolvability repairs without changing teacher strength, architecture, optimizer, seeds, `Delta_t` or scientific claim. After acceptance, the frozen scientific v0.2 Full Run can be executed.
