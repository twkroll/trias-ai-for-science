# ML Full Run v0.1 — Scientific Gate Report

**Status:** COMPLETE — `INCONCLUSIVE_LEARNER_ERROR`  
**Date:** 2026-09-02  
**Depends on:** D010–D012  
**Scientific ML-Provenance claim:** not assessable from v0.1.

## Execution note

The frozen v0.1 experiment was executed with the accepted `N=1000` dataset, contiguous 60/20/20 phase split, DOP853 primary/tight teachers, one-step coarse RK4 teacher, Residual-MLP `12-128-128-128-12`, seeds `{0,1,2}`, float64 CPU, Adam and the preregistered stopping rules.

The monolithic execution exceeded the available tool wall time during dataset/training execution. The deterministic calculation was therefore completed in pieces: the paired dataset was generated once by the frozen code, and the six teacher/seed trainings were executed separately with identical frozen settings and then aggregated. No scientific setting, split, teacher, architecture, seed, optimizer or gate was changed.

## G1 — Reference separation: PASSED

On the held-out test phase block:

- `D_teacher = RMSE(y_rk4, y_ref) = 1.3035448186e-05`;
- `D_ref = RMSE(y_ref_tight, y_ref) = 5.8302465944e-14`.

Thus

```text
D_ref / D_teacher ≈ 4.47e-09
```

and the preregistered gate

```text
D_ref <= 0.01 * D_teacher
```

is satisfied by a very large margin.

The primary-versus-tight DOP853 rollout position gap over ten nominal periods is `6.6866649382e-10`, so reference uncertainty is not the limiting factor of this experiment.

## G2 — Paired initialization: PASSED

All three teacher pairs were initialized from bit-identical model parameters before optimization.

## G3 — Learner resolvability: FAILED

The preregistered requirement was

```text
median_seed(RMSE_own_teacher_test) < D_teacher_test
```

for both teachers.

Observed median own-teacher test RMSE:

- DOP853-trained model: `7.1872683682e-01`;
- RK4-trained model: `7.1718938925e-01`.

Compared with

- `D_teacher_test = 1.3035448186e-05`.

The learner/test-distribution error is therefore roughly `5.5e4` times larger than the numerical teacher difference. The experiment cannot resolve the provenance signal it was designed to test.

Per D011, the mandatory result status is consequently:

```text
INCONCLUSIVE_LEARNER_ERROR
```

No hyperparameter sweep or architecture expansion is performed within v0.1.

## Seed-wise one-step results

| Seed | Teacher | Epochs | RMSE own teacher | RMSE vs common reference |
|---:|---|---:|---:|---:|
| 0 | ref | 4103 | 0.7789582 | 0.7789582 |
| 0 | rk4 | 5000 | 0.7777018 | 0.7777013 |
| 1 | ref | 5000 | 0.6288772 | 0.6288772 |
| 1 | rk4 | 5000 | 0.6268043 | 0.6268038 |
| 2 | ref | 5000 | 0.7187268 | 0.7187268 |
| 2 | rk4 | 5000 | 0.7171894 | 0.7171906 |

These differences must not be interpreted as a teacher-provenance effect because G3 failed.

## Quantitative provenance decomposition

For the RK4-trained model the exact identity

```text
e_total = e_model + e_teacher
```

closed numerically to approximately machine precision for every seed.

However, the magnitude decomposition shows why v0.1 is non-informative. On the test set:

- teacher contribution `mean_sq_teacher_vec = 2.0391e-09` for all seeds;
- learner/model contribution ranges from about `4.71` to `7.26`.

The model-error contribution is therefore billions of times larger than the teacher contribution. The decomposition works technically, but the scientific signal is submerged by learner error.

## Training/split diagnosis

Training losses become much smaller than validation losses, but even the best training MSE is of order `2e-06`, corresponding to an increment RMSE of order `1e-03`. This alone remains roughly two orders of magnitude above the teacher difference.

The contiguous phase split also requires the MLP trained on the first 60% of the orbit to predict held-out later phase blocks. The standardized validation/test inputs are not astronomically distant (`max |z| ≈ 3.48`), but the observed validation/test errors show that the current learning problem behaves as a difficult phase-extrapolation task. Thus v0.1 tests learner extrapolation much more strongly than the intended tiny teacher-label provenance effect.

## MU1/MU2 rollouts

All twelve rollouts remained finite and did not trigger the `minimum pair distance < 0.1` technical guard, but they are scientifically unusable under the failed learner gate.

Representative one-period final normalized position errors range from roughly `23` to `131`, and ten-period errors from roughly `398` to `1516`. Standardized network inputs grow far outside the training range during rollout (up to thousands in MU2). Energy and angular-momentum errors are correspondingly enormous.

These rollouts diagnose surrogate failure/OOD accumulation, not teacher provenance.

## Scientific interpretation

### What v0.1 establishes

1. The paired-teacher and reference-control logic is technically implementable.
2. The DOP853 primary/tight uncertainty is negligible relative to the RK4-vs.-DOP853 label difference.
3. The exact provenance error identity can be evaluated quantitatively.
4. The preregistered learner-resolvability guard correctly prevents an attractive but invalid provenance interpretation.

### What v0.1 does not establish

The run does **not** support or refute the candidate claim that good generator-relative ML performance can mask target-relative degradation. The learner never reached the precision needed to separate the two teacher maps on the held-out phase block.

It therefore also does not strengthen C06-R or establish an original Trias contribution relative to standard ML provenance/credibility approaches.

## Consequence

C07 must not be accepted from v0.1. Any follow-up must be a separately preregistered v0.2 rather than an in-run rescue or hyperparameter sweep.

The most direct redesign target is not a larger benchmark but **signal resolvability**: the next specification should make the learner capable of fitting/interpolating the common one-step map substantially below the fixed teacher difference while retaining a non-leaky held-out evaluation and a shared, teacher-independent preprocessing pipeline.