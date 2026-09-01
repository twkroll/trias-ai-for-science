# Implementation Contract v0.1

**Status:** PENDING REVIEW  
**Depends on:** D001–D004 and accepted Minimal Demonstrator Specification v0.1  
**Rule:** no large implementation before this contract is accepted.

## IC-01 — Purpose

This contract freezes the smallest technical choices needed to implement the first epistemic demonstrator reproducibly. It is not yet a claim that the selected setup will support C05/C06.

The experiment asks whether the same synthetic target system and Newtonian theory can yield different scientifically relevant evaluation profiles under different numerical operationalizations.

## IC-02 — Synthetic target system

Use the planar equal-mass Newtonian three-body figure-eight choreography in dimensionless units:

- `G = 1`
- `m1 = m2 = m3 = 1`
- state space: three 2D positions and three 2D velocities
- no softening
- no collision regularization

The standard initial values, reported in the Chenciner–Montgomery figure and attributed there to Carles Simó, are frozen as:

```text
r1 = ( 0.97000436, -0.24308753)
r2 = (-0.97000436,  0.24308753)
r3 = ( 0.0,         0.0)

v1 = ( 0.466203685,  0.43236573)
v2 = ( 0.466203685,  0.43236573)
v3 = (-0.93240737,  -0.86473146)
```

Nominal published period:

```text
T_pub = 6.32591398
```

Important epistemic note: the printed initial conditions and period have finite decimal precision. Therefore `T_pub` is used as a nominal period/scale, not as an exact mathematical return time. Exact periodic closure is not assumed in the evaluation.

Primary source basis: Chenciner & Montgomery, *A remarkable periodic solution of the three-body problem in the case of equal masses*, Annals of Mathematics 152 (2000), 881–901.

## IC-03 — Shared equations and force implementation

All solvers use the same Newtonian acceleration function.

For each pair `i < j`, compute one separation vector and update both bodies with equal-and-opposite pair contributions. This makes Newton's third-law symmetry explicit in the implementation and avoids solver-specific force definitions.

The code must expose functions for:

- acceleration / RHS,
- total energy,
- total linear momentum,
- center of mass,
- scalar planar angular momentum,
- minimum pair distance.

All calculations use IEEE float64 in v0.1.

## IC-04 — Time horizons and common observation grid

Two use cases are frozen:

### U1 — short-term trajectory use

```text
t in [0, 1*T_pub]
```

Question: how accurately are positions reproduced over one nominal choreography period?

### U2 — long-term structural use

```text
t in [0, 100*T_pub]
```

Question: how well are relevant invariants and bounded qualitative behavior retained over many nominal periods?

The common reporting grid is

```text
dt_out = T_pub / 50
```

so that all stored comparison times are shared by every fixed-step run. Internal solver steps may be finer.

## IC-05 — Reference calculation

Primary numerical reference:

```text
scipy.integrate.solve_ivp
method = "DOP853"
rtol = 1e-12
atol = 1e-14
dense_output = True
```

Reference cross-check:

```text
method = "DOP853"
rtol = 1e-13
atol = 1e-15
dense_output = True
```

DOP853 is chosen because SciPy explicitly recommends it among its Runge–Kutta solvers for high-precision non-stiff integration.

The primary reference is never labelled exact ground truth.

### Reference acceptance rule

For U1, report the discrepancy between the primary and tighter reference on the common grid. The reference is adequate for ranking a fixed-step result only if its own discrepancy is at least two orders of magnitude below the fixed-step position error being interpreted. If this fails, no ranking is made until the reference is strengthened.

For U2, the main/tight reference discrepancy must be reported alongside long-time trajectory comparisons. If it becomes non-negligible relative to a claimed solver difference, trajectory-ranking claims at that horizon are suspended. Invariant-based statements may still be made if independently justified.

Escalation if needed: add an independent high-accuracy solver rather than silently tightening tolerances indefinitely.

## IC-06 — Fixed-step solvers

Implement exactly two comparison methods in v0.1:

1. classical explicit RK4;
2. velocity-Verlet / kick-drift-kick leapfrog for the separable Newtonian Hamiltonian.

No library wrapper is used for these two methods; the update equations are implemented explicitly and tested.

Step-size family:

```text
h = T_pub / n
n in {50, 100, 200, 400, 800}
```

This gives a shared refinement sequence by factors of two. Comparison by equal step size is reported, but solver efficiency is assessed against actual force/RHS evaluation counts rather than step size alone.

## IC-07 — Primary metrics

### M1 — normalized RMS position error

Let

```text
L0 = sqrt((1/3) * sum_i ||r_i(0)||^2)
```

and define

```text
E_pos(t) = sqrt((1/3) * sum_i ||r_i(t)-r_i_ref(t)||^2) / L0.
```

For U1 report:

- `E_pos(T_pub)`;
- `max_t E_pos(t)` on the common grid.

For U2, position error may be shown diagnostically but is not by itself a scientific-quality ranking because phase errors can accumulate over long times.

### M2 — relative energy error

With the Newtonian Hamiltonian `H`, define

```text
e_H(t) = (H(t)-H(0)) / |H(0)|.
```

Report:

- `max |e_H|`;
- final `e_H`;
- least-squares slope of `e_H` against `t/T_pub` as a simple secular-drift indicator.

The slope is descriptive, not a universal stability metric.

### M3 — angular-momentum error

Because the figure-eight has nominal zero total angular momentum, do not use a relative error with `L_z(0)` in the denominator.

Define the nonzero scale

```text
L_scale = sum_i m_i * ||r_i(0)|| * ||v_i(0)||
```

and report

```text
e_L(t) = |L_z(t)-L_z(0)| / L_scale.
```

### M4 — resource cost

Primary resource measure: actual number of RHS/force evaluations.

Secondary measure: wall-clock runtime, reported as the median of repeated identical runs on the same machine and environment. Runtime is never compared across machines without qualification.

### M5 — refinement / observed order

For U1 use the refinement sequence to estimate

```text
p_obs = log(E_h / E_(h/2)) / log(2)
```

where the reference floor has not yet been reached.

This is a validation diagnostic, not a hard assumption that every nonlinear trajectory error must display textbook order at every resolution.

## IC-08 — Secondary diagnostics and implementation guards

Record, but do not use as primary solver-ranking metrics:

- total linear momentum error;
- center-of-mass drift;
- minimum pair distance;
- maximum distance from the center of mass.

Abort a run and mark it invalid if a pair distance falls below `0.1` in v0.1. This is a technical guard for leaving the intended collision-free target regime, not a physical collision model.

## IC-09 — Two evaluation views

Every result must be summarized twice.

### Baseline view

- short-term position error;
- computational cost.

### Trias view

- U1 versus U2 scientific purpose;
- invariant preservation and drift;
- refinement robustness;
- reference uncertainty;
- resource cost;
- localization of the relevant issue at a Trias edge.

No statement such as “solver X is best” is permitted without naming the use case and evaluation criterion.

## IC-10 — Minimum scientific gates

Before C05 is evaluated, the implementation must pass:

1. initial center of mass approximately zero;
2. initial total linear momentum approximately zero;
3. initial total angular momentum approximately zero;
4. pair-force antisymmetry test on several deterministic non-collision states;
5. all solvers produce finite outputs on U1 for all frozen step sizes;
6. fixed-step errors decrease under at least part of the U1 refinement sequence;
7. the primary/tight reference discrepancy is explicitly reported;
8. the common initial state, period constant, tolerances and step sizes appear in machine-readable configuration output.

Expected RK4 fourth-order and Verlet second-order convergence may be checked as a scientific diagnostic, but failure to hit a narrow textbook order band is investigated rather than hidden or automatically treated as a coding failure.

## IC-11 — Required artifacts

A single reproducible command must create at least:

```text
results/reference_check.json
results/metrics.csv
results/summary.json
figures/u1_trajectory_error.png
figures/u2_energy_error.png
figures/error_vs_cost.png
figures/refinement_u1.png
results/trias_audit.md
```

`summary.json` records package versions, platform information, constants, initial state, horizons, tolerances, step sizes and run status.

`trias_audit.md` contains a short structured interpretation and is not generated by an LLM during the numerical run.

## IC-12 — Explicit scope exclusions

Not included in v0.1:

- fitting/refining the published figure-eight initial conditions;
- claiming exact periodic closure from the rounded values;
- chaotic or perturbed initial conditions;
- adaptive-vs-symplectic production benchmarking beyond the three frozen roles;
- ML;
- Sundman-series evaluation;
- higher precision arithmetic;
- softening or collision regularization;
- uncertainty quantification beyond reference/refinement checks.

## IC-13 — Evidence logic

A result can support later C05 only if it survives refinement and reference checks.

A result can support later C06 only if the Trias view changes or sharpens the scientific interpretation relative to the baseline numerical view. Merely producing extra plots or restating standard numerical diagnostics does not count as added epistemic value.

A negative result remains admissible and must be recorded.

## Decision recommendation

Accept this Implementation Contract v0.1 as the frozen technical specification for the first implementation.

After acceptance, the next step is **not** to add further scientific scope. It is to create the minimal tested code skeleton that implements this contract and nothing more.