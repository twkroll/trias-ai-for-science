# ML Provenance Demonstrator v0.2 — Resolvability Repair Proposal

**Status:** PENDING REVIEW  
**Depends on:** ML Full Run v0.1 = `INCONCLUSIVE_LEARNER_ERROR`  
**Purpose:** repariert ausschließlich die in v0.1 identifizierte fehlende Signalauflösung; noch keine Implementierung.

## Ausgangsbefund

v0.1 kann den Teacher-Provenance-Claim nicht testen, weil

```text
D_teacher_test ≈ 1.30e-05
```

während die mediane own-teacher Test-RMSE etwa `0.72` beträgt. Selbst die besten Trainings-MSEs entsprechen einer Rohinkrement-RMSE von Größenordnung `1e-03` und liegen damit noch deutlich über dem Teacher-Signal.

Zugleich macht der contiguous 60/20/20-Phasensplit den Test zu einer starken Held-out-Phasenextrapolation, obwohl D010 ausdrücklich keine Generalisierung auf neue Orbits oder schwierige Phasenextrapolation beansprucht.

## Designprinzip

v0.2 soll **nicht** die Teacher-Differenz künstlich vergrößern und keinen Architektur-/Teacher-Sweep durchführen. DOP853, coarse RK4, `Delta_t=T_pub/50`, Figure-eight, `N=1000`, Residual-MLP und Seeds `{0,1,2}` bleiben zunächst unverändert.

Es werden nur zwei direkt aus dem v0.1-Fehlerbild begründete Designkorrekturen vorgeschlagen.

## R1 — Phase-stratifizierter Blocksplit statt globaler Phasenextrapolation

Die 1000 geordneten Phasenpunkte werden in 200 aufeinanderfolgende Blöcke zu je 5 Punkten geteilt. Die Blockzuweisung folgt deterministisch einem Fünferzyklus:

```text
block mod 5 in {0,1,2} -> train
block mod 5 == 3       -> validation
block mod 5 == 4       -> test
```

Damit bleiben exakt 60/20/20 Prozent erhalten, aber alle Splits decken die gesamte Figure-eight-Phase ab. Innerhalb jedes Blocks bleiben zeitlich benachbarte Punkte zusammen; es gibt weiterhin keinen zufälligen Punkt-Split.

Diese Auswertung ist bewusst ein **same-orbit interpolation/provenance test**, kein Generalisierungstest. Nähe zu Trainingsphasen wird nicht als Evidenz für neue-Orbit- oder Langzeit-Generalisation ausgegeben.

## R2 — Ein gemeinsamer, teacher-unabhängiger Target-Scaler

Die beiden Inkrementtargets werden nicht mehr roh optimiert. Stattdessen wird **ein gemeinsamer** komponentenweiser Scaler ausschließlich aus dem Trainingssplit beider Teacher zusammen berechnet:

```text
Delta_train_shared = concatenate(delta_ref_train, delta_rk4_train)
mu_delta = mean(Delta_train_shared)
sigma_delta = max(std(Delta_train_shared), 1e-12)
```

Beide Modelle lernen

```text
(delta_teacher - mu_delta) / sigma_delta
```

mit exakt demselben Scaler. Evaluation, Teacher-Gates und Provenance-Zerlegung werden nach Rücktransformation weiterhin in den ursprünglichen dimensionslosen Zustandskoordinaten durchgeführt.

Damit wird die Optimierungsskala verbessert, ohne einen teacher-spezifischen Target-Scaler einzuführen.

## Unverändert gegenüber v0.1

- synthetisches Figure-eight-Zielsystem;
- DOP853 primary/tight teacher;
- coarse RK4: exakt ein Schritt `h=T_pub/50`;
- identische Inputzustände für beide Teacher;
- `N=1000`;
- Inputnormalisierung nur aus Training;
- Residual-MLP `12-128-128-128-12`, `tanh`, float64 CPU;
- Seeds `{0,1,2}` mit bitgleicher Paarinitialisierung;
- Adam, gleiche Lernrate und kein Hyperparameter-Sweep;
- gemeinsame Reference-/Teacher-Metriken und exakte Provenance-Zerlegung;
- keine Physics-Regularisierung, neue Orbits oder zusätzliche Teacher.

## Resolvability-first Gates

Vor jeder Teacher-Provenance-Interpretation gelten weiterhin:

```text
G1: D_ref <= 0.01 * D_teacher
G2: paired inputs/splits/scalers/initialization identical
G3: median_seed(RMSE_own_teacher_test) < D_teacher_test
```

Zusätzlich wird diagnostisch berichtet, ob die Rohkoordinaten-Train-RMSE selbst unter `D_teacher` liegt. Scheitert G3 erneut, endet v0.2 wieder als `INCONCLUSIVE_LEARNER_ERROR`; es folgt kein automatischer Architektur- oder Teacher-Sweep.

## Rollout-Regel

MU1/MU2 werden erst als wissenschaftliche Diagnostik interpretiert, wenn G1–G3 bestanden sind. Bei erneutem G3-Scheitern werden Rollouts höchstens als technische/OOD-Diagnostik gespeichert, nicht als Provenance-Evidenz.

## Warum nicht zuerst den Teacher gröber machen?

Ein deutlich schlechterer oder niederordentlicher Teacher würde das Signal einfacher vergrößern, könnte aber den gewünschten Befund künstlich trivial machen. Der konservativere nächste Test ist deshalb, dieselbe numerische Teacher-Differenz beizubehalten und zuerst sicherzustellen, dass der Learner genau diese Differenz prinzipiell auflösen kann.

## Erfolg und Misserfolg

### Informativ

v0.2 ist erst dann informativ, wenn die Learner-RMSE unterhalb des unveränderten Teacher-Signals liegt. Erst danach dürfen own-teacher versus common-reference Unterschiede, Provenance-Zerlegung und MU1/MU2 als Evidenz für oder gegen den Claim-Kandidaten genutzt werden.

### Erneut nicht informativ

Scheitert G3 trotz phase-stratifiziertem Split und gemeinsamem Target-Scaling, wird nicht weiter innerhalb derselben Version getunt. Dann muss grundsätzlich entschieden werden, ob die Teacher-Differenz für einen MLP-Provenance-Demonstrator zu klein gewählt ist oder ob ein anderer kontrollierter AI-for-Science-Fall geeigneter wäre.

## Entscheidungsempfehlung

**ACCEPT als nächste v0.2-Spezifikationsrichtung**, jedoch erst nachdem der v0.1-Status `INCONCLUSIVE_LEARNER_ERROR` als Ergebnis akzeptiert wurde. Nach einem GO wird ein exakter v0.2 Implementation Contract erstellt; es erfolgt noch kein Training.