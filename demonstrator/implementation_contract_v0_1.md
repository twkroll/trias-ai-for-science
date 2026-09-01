# Implementation Contract v0.1

**Status:** ACCEPTED — D006  
**Akzeptiert durch:** GO  
**Depends on:** D001–D005  
**Rule:** Implementationsumfang bleibt auf diesen Contract begrenzt.

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

Frozen initial values:

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

The printed initial conditions and period have finite decimal precision. `T_pub` is therefore a nominal period/scale, not an exact mathematical return time. Exact periodic closure is not assumed.

Primary source basis: Chenciner & Montgomery, *A remarkable periodic solution of the three-body problem in the case of equal masses*, Annals of Mathematics 152 (2000), 881–901.

## IC-03 — Shared equations and force implementation

All solvers use the same Newtonian acceleration function. For each pair `i < j`, compute one separation vector and update both bodies with the corresponding pair contribution so Newton's third-law symmetry is explicit.

The code exposes:

- acceleration / RHS,
- total energy,
- total linear momentum,
- center of mass,
- scalar planar angular momentum,
- minimum pair distance.

All calculations use IEEE float64 in v0.1.

## IC-04 — Time horizons and common observation grid

### U1 — short-term trajectory use

```text
t in [0, 1*T_pub]
```

### U2 — long-term structural use

```text
t in [0, 100*T_pub]
```

Common reporting grid:

```text
dt_out = T_pub / 50
```

Internal fixed steps may be finer.

## IC-05 — Reference calculation

Primary reference:

```text
scipy.integrate.solve_ivp
method = "DOP853"
rtol = 1e-12
atol = 1e-14
dense_output = True
```

Tighter cross-check:

```text
method = "DOP853"
rtol = 1e-13
atol = 1e-15
dense_output = True
```

The primary reference is never labelled exact ground truth.

### Reference acceptance rule

For U1, the primary/tight reference discrepancy must be at least two orders of magnitude below the fixed-step position error being interpreted. Otherwise no ranking is made until the reference is strengthened.

For U2, the reference discrepancy is reported alongside long-time trajectory comparisons. If it becomes non-negligible relative to a claimed solver difference, trajectory-ranking claims are suspended. Invariant-based statements may remain admissible if independently justified.

If needed, escalation means adding an independent high-accuracy solver rather than silently tightening tolerances indefinitely.

## IC-06 — Fixed-step solvers

Implement exactly:

1. classical explicit RK4;
2. velocity-Verlet / kick-drift-kick leapfrog.

Step-size family:

```text
h = T_pub / n
n in {50, 100, 200, 400, 800}
```

Efficiency is assessed against actual force/RHS evaluation counts, not step size alone.

## IC-07 — Primary metrics

### M1 — normalized RMS position error

```text
L0 = sqrt((1/3) * sum_i ||r_i(0)||^2)
E_pos(t) = sqrt((1/3) * sum_i ||r_i(t)-r_i_ref(t)||^2) / L0
```

For U1 report `E_pos(T_pub)` and `max_t E_pos(t)`.

### M2 — relative energy error

```text
e_H(t) = (H(t)-H(0)) / |H(0)|
```

Report maximum absolute error, final error and a least-squares slope against `t/T_pub` as a descriptive secular-drift indicator.

### M3 — angular-momentum error

Because nominal total angular momentum is zero, use

```text
L_scale = sum_i m_i * ||r_i(0)|| * ||v_i(0)||
e_L(t) = |L_z(t)-L_z(0)| / L_scale
```

rather than division by `L_z(0)`.

### M4 — resource cost

Primary measure: actual RHS/force evaluations. Secondary measure: median wall-clock runtime of repeated identical runs on the same machine/environment.

### M5 — refinement / observed order

```text
p_obs = log(E_h / E_(h/2)) / log(2)
```

where the reference floor has not been reached.

## IC-08 — Secondary diagnostics and implementation guards

Record:

- total linear momentum error,
- center-of-mass drift,
- minimum pair distance,
- maximum distance from center of mass.

Abort and mark invalid if minimum pair distance falls below `0.1`. This is a technical guard, not a collision model.

## IC-09 — Two evaluation views

Every result is summarized twice.

### Baseline view

- short-term position error;
- computational cost.

### Trias view

- U1 versus U2 purpose;
- invariant preservation/drift;
- refinement robustness;
- reference uncertainty;
- resource cost;
- localization at a Trias edge.

No unqualified statement such as “solver X is best” is permitted.

## IC-10 — Minimum scientific gates

Before C05 is evaluated:

1. initial center of mass approximately zero;
2. initial total linear momentum approximately zero;
3. initial total angular momentum approximately zero;
4. pair-force antisymmetry test on deterministic non-collision states;
5. all solvers produce finite U1 outputs for all frozen step sizes;
6. fixed-step errors decrease over at least part of the U1 refinement sequence;
7. primary/tight reference discrepancy is reported;
8. initial state, period, tolerances and step sizes appear in machine-readable configuration output.

Expected RK4 fourth-order and Verlet second-order convergence are diagnostics, not narrow pass/fail bands.

## IC-11 — Required artifacts

A single reproducible command creates at least:

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

`trias_audit.md` is generated from fixed rules, not by an LLM during the numerical run.

## IC-12 — Explicit scope exclusions

Not included in v0.1:

- fitting/refining published initial conditions;
- claiming exact periodic closure;
- chaotic or perturbed initial conditions;
- ML;
- Sundman-series evaluation;
- higher precision arithmetic;
- softening or collision regularization;
- UQ beyond reference/refinement checks.

## IC-13 — Evidence logic

A result can support C05 only if it survives refinement and reference checks.

A result can support C06 only if the Trias view changes or sharpens interpretation relative to the baseline numerical view. Extra plots or restating standard diagnostics do not count as added epistemic value.

A negative result remains admissible.

## Next dependency

After D006, implement and test the minimal code skeleton defined by this contract. No scientific scope is added before that skeleton is reviewed.