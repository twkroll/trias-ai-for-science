# Trias audit — full demonstrator v0.1

## Status

Full frozen v0.1 calculation completed and reference/refinement gates checked. This file states the fixed audit reading used before C05/C06 decisions.

## Target system → theory

Frozen equal-mass planar Newtonian Figure-eight instance, with rounded published initial values treated as a nominal target specification rather than exact periodic data.

## Theory → computation

DOP853, classical RK4 and Velocity-Verlet realize the same Newtonian dynamics differently. The full run reveals method-dependent differences among trajectory accuracy, energy-error amplitude, secular energy drift, angular-momentum preservation and resource cost.

## Computation → target system

Primary/tight DOP853 normalized position gaps:

- U1: `8.854e-12`;
- U2: `6.163e-08`.

These gaps are safely below the fixed-step trajectory errors used in the current interpretation and satisfy the accepted reference gate.

## Use-case dependence

### U1

For the short-term trajectory-oriented use, RK4 is clearly more accurate at matched `n` and shows near-fourth-order refinement.

### U2

No single unqualified method ranking is justified. RK4 remains much more trajectory-accurate and can have smaller maximum energy-error amplitude, while Velocity-Verlet has dramatically smaller fitted secular energy drift and preserves total angular momentum close to roundoff.

## Claim localization

This is positive evidence for C05: implementation choice can produce scientifically relevant profiles whose evaluation depends on the intended scientific use and relevant theoretical structure.

It is not yet positive evidence for a strong C06. Standard numerical analysis, geometric integration and V&V already diagnose much of the underlying numerical behavior. C06 requires a direct comparison of what the Trias adds to that established diagnosis.