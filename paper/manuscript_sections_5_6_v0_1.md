# Sections 5–6 — Classical controls and negative/inconclusive stress tests

**Status:** DRAFT v0.1 / W5  
**Stand:** 2026-09-03  
**Depends on:** D034 / P3 / W1–W4 PASS

> **Manuscript note:** These sections are intended as near-manuscript prose. Their purpose is not to add a new empirical contribution to the paper, but to test whether the descriptive vocabulary can accommodate ordinary numerical cases, negative evidence, and inconclusive evidence without changing the status of the underlying results.

## 5. Classical controls: where ordinary numerical analysis and V&V already suffice

A useful conceptual vocabulary should not claim a distinctive contribution in cases where established analysis already supplies the relevant distinctions. Two cases from the development of the present proposal therefore function as controls rather than demonstrations of novelty. The first separates formal analytical availability from practical computational availability; the second shows that different numerical realizations of the same theory can produce different use-dependent error profiles without requiring a new validation framework.

### 5.1 Sundman: analytical availability without practical evaluability

Sundman's classical treatment of the Newtonian three-body problem provides a particularly clear theory–computation example. Under the standard nonzero-total-angular-momentum condition, binary collisions can be regularized and a transformed time variable introduced so that the motion is represented by convergent power series in the regularized variable. The relevant historical point is therefore not that the series fail to converge. They do converge under the conditions of the theorem. The practical difficulty is that their convergence is so slow that the representation is unsuitable for ordinary trajectory or ephemeris computation (Sundman; Belorizky; Henkel; Chenciner).

In the present vocabulary, this case separates two questions that can both lie on the theory–computation side of the analysis. One concerns formal representability or fidelity: does the mathematical representation encode the relevant solution under its stated assumptions? A second concerns tractability or evaluability: can that representation be used to generate the required scientific output with acceptable resources and accuracy? The first can be strong while the second is weak. Thus

\[
\text{formal analytical availability}
\not\Rightarrow
\text{practical computational availability}.
\]

This distinction is not a novelty claim for the Trias. Numerical analysis and the history of the three-body problem already distinguish mathematical existence or representation from feasible evaluation. The case is included because it provides a clean control for the descriptive semantics: a theory-related claim can be well established without implying that the corresponding computational task is practically useful. It also guards against a recurring but misleading shorthand in which “an analytical solution exists” is treated as equivalent to “the trajectory is operationally available.”

### 5.2 Figure-eight: different computational profiles, no new validation category

A second control uses the periodic equal-mass figure-eight orbit as a synthetic target. The target system, Newtonian theory, initial conditions, output sampling, and reference solution were fixed in advance. Two fixed-step numerical realizations—classical fourth-order Runge–Kutta and Velocity-Verlet—were then compared against a tightly controlled DOP853 reference over a one-period trajectory-oriented use case and a one-hundred-period structure-oriented use case.

The short-horizon result is conventional. The observed refinement behavior approaches fourth order for RK4 and second order for Velocity-Verlet. At the representative resolution with 200 steps per nominal period, the maximum normalized one-period position error is approximately

\[
8.0\times 10^{-6}
\]

for RK4 and

\[
6.4\times 10^{-3}
\]

for Velocity-Verlet. For the trajectory-oriented question, RK4 is therefore clearly the more accurate of the two realizations at equal step count.

The long-horizon comparison separates different numerical qualities. At the same resolution, RK4 has the smaller maximum energy-error amplitude, but Velocity-Verlet exhibits a much smaller fitted secular energy drift. At 200 steps per period, the fitted drift magnitude differs by roughly a factor of 144; Velocity-Verlet also preserves total angular momentum at approximately roundoff scale, whereas RK4 has a larger but systematically decreasing angular-momentum error. At the finest tested resolution, RK4 remains substantially closer to the reference trajectory than Velocity-Verlet.

The result therefore does not support a global ranking such as “Velocity-Verlet is the better method.” It supports a narrower claim: different computational realizations can be preferable under different quantities of interest and scientific uses. In Trias terms, the theory and synthetic target remain fixed while different facets of the theory–computation relation are supported to different degrees. However, standard numerical analysis, geometric integration, and V&V already describe this case very well through convergence, trajectory error, invariants, drift, quantities of interest, and intended use. The Trias adds no new error category here.

That non-result is methodologically useful for the paper. It establishes a control condition in which the proposed role vocabulary should remain compatible with established practice without claiming to improve it. The contribution of the later AI-for-Science cases cannot therefore be inferred merely from the fact that the same notation can be applied to numerical solvers.

## 6. Stress tests: negative and inconclusive evidence

The descriptive proposal also needs to distinguish cases in which an interesting claim is not supported from cases in which the experiment never became capable of deciding it. Two preregistered project studies provide these stress tests. Their role in the manuscript is not to validate the Trias empirically. Their role is to test whether a claim-relative evidence profile preserves the difference between negative and inconclusive results instead of absorbing both into an undifferentiated label such as “model failure.”

### 6.1 Lorenz/SINDy: an informative negative result

The inverse-direction experiment was designed around the Lorenz-63 system. A high-accuracy reference trajectory was sampled, 20% of the discovery-window observations were removed using paired random masks, and the same missing observations were reconstructed either linearly or with a cubic spline. A fixed derivative estimator, fixed quadratic candidate library, fixed sparse-regression procedure, and preregistered structural and dynamical criteria were then applied to the resulting data. The baseline path without missing observations first had to recover the intended Lorenz structure accurately before any reconstruction effect could be interpreted.

The technical gates passed. The primary and tight numerical references agreed well within the frozen reference tolerance, each mask contained exactly the prescribed number of missing points, and the no-missingness baseline recovered the true Lorenz support with no missing or spurious terms and very small coefficient error. The experiment was therefore technically capable of asking the preregistered structural question.

The result was nevertheless negative with respect to that question. A substantive structural perturbation occurred in only one of three linear-reconstruction seeds and in none of the three cubic-spline seeds. The preregistered positive classification required seed-consistent structural perturbation in at least two of three trials, together with the specified dynamical-adequacy condition. That criterion was not met. The accepted result class is therefore

```text
INFORMATIVE_NEGATIVE
```

rather than a weakened positive result.

The single structurally different case is scientifically interesting but does not change the classification. In the linear reconstruction with seed 2, the inferred equation contained an additional constant term in the \(z\)-equation while still passing the frozen operational-equivalence criterion. Because this occurred in only one of three seeds, it remains an exploratory observation. No missingness rate, sparse-regression threshold, feature library, structural threshold, or classification rule was changed after inspecting the result.

The evidence profile is therefore asymmetric. The baseline recovery and the technical integrity of the inverse pipeline are supported. Several held-out vector-field and short-horizon adequacy measures are also strong. But the specific claim that the chosen reconstruction perturbation induces a robust structural change is not supported under the frozen scope. This is not evidence that structural non-identifiability is absent in general, nor does it refute external equation-discovery results obtained under different observation and reconstruction conditions. It is negative evidence for one preregistered claim in one deliberately minimal configuration.

This case illustrates why a global statement such as “the pipeline worked” or “the discovery failed” is too coarse. Different claims within the same workflow received different evidential outcomes. The descriptive value lies in preserving those distinctions without converting a negative result into a generalized judgment about the target system, equation discovery, or identifiability.

### 6.2 ML provenance v0.1: an inconclusive result caused by insufficient resolvability

The ML provenance experiment asked a different question. Two paired training sets were generated for the same figure-eight target using two numerical teachers: a high-accuracy DOP853 reference and a coarser one-step RK4 map. The scientific objective was to determine whether a learned one-step surrogate could reproduce each teacher accurately enough that the small difference between the two data generators remained resolvable in the learned models. Only after that prerequisite was satisfied could downstream teacher-provenance effects be meaningfully compared.

The reference-control and paired-initialization gates passed. On the held-out test block, the difference between the RK4 and DOP853 teacher maps was approximately

\[
1.30\times 10^{-5},
\]

while the uncertainty associated with the primary versus tighter DOP853 reference was negligible by comparison. Thus the numerical teachers were cleanly separated at the data-generation level.

The learner-resolvability gate failed by a large margin. The median one-step test RMSE relative to each model's own teacher was about \(0.72\), roughly \(5.5\times 10^4\) times larger than the teacher difference. The learned models therefore could not resolve the signal that the experiment had been designed to attribute to provenance. Per the frozen decision rule, the accepted status is

```text
INCONCLUSIVE_LEARNER_ERROR.
```

This status is intentionally different from a negative result. The run does not show that the teacher-provenance hypothesis is false. It shows that the chosen learner and split did not achieve sufficient accuracy to test that hypothesis. The large rollout errors and out-of-distribution accumulation observed later in the run diagnose surrogate failure; they do not become evidence about the tiny DOP853-versus-RK4 provenance signal.

In the role vocabulary, the immediate bottleneck is a theory/computation or teacher/computation resolvability question: the learned computational realization is not accurate enough relative to the teacher distinction of interest. Because that prerequisite fails, the downstream claim about how generator provenance affects scientific output remains uncertain rather than refuted. The experiment therefore supplies a concrete difference between

```text
negative evidence     -> the test was capable of deciding the claim and the preregistered criterion was not met
inconclusive evidence -> the prerequisite resolution needed to decide the claim was not achieved
untested evidence     -> the relevant relation was never evaluated
not applicable        -> the relation is not part of the specified claim
```

These distinctions are not unique to the Trias, but they are necessary if a common evidence-localization vocabulary is to be scientifically disciplined.

### 6.3 Cross-case evidence ledger

The four control and stress-test cases can therefore be summarized without assigning a global model score:

| Case | Principal role in the manuscript | Evidence status relevant to the paper | What is supported | What is explicitly not supported |
|---|---|---|---|---|
| Sundman | classical conceptual control | positive historical/conceptual illustration | formal analytical availability can coexist with poor practical evaluability | no claim that the series diverge; no unique Trias diagnosis |
| Figure-eight | standard V&V control | positive, use-case-relative numerical evidence | different computational realizations exhibit different trajectory/structure profiles | no new numerical error category; no global solver winner |
| Lorenz/SINDy | inverse stress test | `INFORMATIVE_NEGATIVE` | baseline validity and several dynamical/technical adequacy claims | no seed-robust reconstruction-induced structural effect in the frozen setup |
| ML provenance v0.1 | resolvability stress test | `INCONCLUSIVE_LEARNER_ERROR` | teacher separation and paired design were valid | no support or refutation of the downstream teacher-provenance claim |

The table is deliberately heterogeneous. A positive control, a negative result, and an inconclusive result are not points on one quality scale. They answer different claims. The common function of the role profile is simply to make those claims and their evidential status explicit while leaving the substantive numerical, statistical, or historical assessment to the relevant specialist methods.

This discipline also constrains the broader argument of the paper. The controls do not establish the novelty of the Trias, the negative inverse result does not become positive evidence through selective interpretation, and the inconclusive ML run is not treated as a failed hypothesis test. A descriptive framework that could sustain the paper only by erasing these differences would fail its own evidence-localization objective.

## Reference anchors for final bibliography

- Sundman, K. F., *Mémoire sur le problème des trois corps*.
- Belorizky, D. (1930), practical analysis of Sundman's method.
- Henkel, M. (2001), historical/philosophical discussion of Sundman's solution.
- Chenciner, A., *Three body problem*, Scholarpedia.
- Standard numerical-analysis / geometric-integration / V&V literature for RK4 and Velocity-Verlet interpretation.
- Project Figure-eight Full Demonstrator v0.1 results.
- Project Inverse-Direction Scientific Full Run v0.1 and D020 classification.
- Project ML Full Run v0.1 scientific gate report.
