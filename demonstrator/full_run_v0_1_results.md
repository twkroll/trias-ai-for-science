# Full Demonstrator v0.1 — Scientific Gate Report

**Status:** COMPLETE; C05 pending review.  
**Date:** 2026-09-02  
**Depends on:** D005–D007.

## Execution note

The frozen v0.1 calculation was executed with the accepted Figure-eight target, DOP853 reference settings, RK4/Velocity-Verlet implementations, U1/U2 horizons, five refinements and three timing repetitions. Because the monolithic runner exceeded the available execution wall-time, the same frozen calculation was executed deterministically in pieces (reference pairs and each fixed-step method/refinement separately) and then aggregated. No scientific setting was changed.

## Reference gates

Primary-versus-tight DOP853 normalized position discrepancies:

- U1 max gap: `8.854e-12`;
- U2 max gap: `6.163e-08`.

The smallest fixed-step max position errors are:

- U1: `2.668e-08` (finest RK4), about 3013 times the U1 reference gap;
- U2: `4.687e-05` (finest RK4), about 760 times the U2 reference gap.

Thus the accepted two-orders-of-magnitude reference gate is satisfied for every fixed-step trajectory comparison interpreted below.

## U1 — short-term trajectory use

RK4 endpoint observed refinement orders:

`4.74, 4.62, 4.46, 4.30`.

Velocity-Verlet endpoint observed refinement orders:

`1.75, 1.87, 1.97, 1.99`.

This is consistent with the expected approach toward fourth- and second-order behavior, respectively.

At `n=200`:

- RK4 max normalized U1 position error: `8.037e-06`;
- Verlet max normalized U1 position error: `6.389e-03`.

At equal `n`, RK4 is therefore substantially more accurate for the trajectory-oriented U1 question. This is the straightforward baseline numerical result.

## U2 — long-term structural use

The methods show different error/structure profiles rather than a simple global ranking.

At `n=200`:

- RK4 max absolute relative energy error: `8.304e-05`;
- RK4 fitted energy drift slope: `-8.305e-07` per nominal period;
- Verlet max absolute relative energy error: `6.019e-04`;
- Verlet fitted energy drift slope: `-5.783e-09` per nominal period.

Thus RK4 has the smaller energy-error amplitude at this resolution, while Verlet has approximately 144 times smaller fitted secular energy drift.

At `n=400`:

- RK4 max absolute relative energy error: `2.598e-06`;
- RK4 drift slope: `-2.598e-08` per nominal period;
- Verlet max absolute relative energy error: `1.472e-04`;
- Verlet drift slope: `-4.337e-10` per nominal period.

The fitted secular drift is about 60 times smaller for Verlet, despite its substantially larger bounded energy-error amplitude.

Over U2, Verlet preserves total angular momentum at roughly roundoff scale (`~1e-14` normalized error). RK4's angular-momentum error is larger but decreases systematically with refinement; at `n=800` it is about `1.55e-10`.

Trajectory-wise, RK4 remains much closer to the DOP853 reference at the same `n`. For `n=800`:

- RK4 max normalized U2 position error: `4.687e-05`;
- Verlet max normalized U2 position error: `2.042e-02`.

The result is therefore deliberately **not** interpreted as “Verlet is the better solver.” It is a use-case-dependent profile difference.

## C05 evidence candidate

The full run supports the modest claim:

> For the same synthetic target system, theory and initial data, different numerical operationalizations can produce distinct scientifically relevant error and structure profiles; which profile is preferable depends on the specified scientific use.

The clearest contrast is U2. RK4 can provide much smaller trajectory error and smaller maximum energy-error amplitude, whereas Velocity-Verlet exhibits far smaller secular energy drift and near-roundoff angular-momentum preservation. A statement of the form “solver X is best” is therefore underdetermined until the intended scientific question and relevant theoretical structures are specified.

## Claim boundary

This run does **not** establish that the Trias discovers numerical facts unavailable to geometric numerical integration, standard numerical analysis or Verification & Validation. Those frameworks already have vocabulary for convergence, invariants, solver error and intended use.

Accordingly:

- C05 is empirically supported in a modest, purpose-relative form;
- C06 remains open;
- the next methodological test must compare the Trias interpretation directly against an ordinary numerical-analysis/V&V interpretation of these same results.

## Negative-result guard

If that comparison shows that the Trias merely renames the same diagnostic work without changing error localization, validation questions or the justified scientific conclusion, C06 must be rejected or substantially weakened.