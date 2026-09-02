# ML Implementation Contract v0.2 — Resolvability Repair

**Status:** PENDING REVIEW  
**Depends on:** D013  
**Purpose:** repariert ausschließlich die in ML v0.1 identifizierte fehlende Learner-Resolvability, bevor C07 erneut geprüft werden darf.  
**Rule:** keine Implementierung oder Trainingsläufe vor Akzeptanz dieses Contracts.

## ML2-IC-01 — Wissenschaftlicher Zweck

v0.2 prüft dieselbe Kernfrage wie v0.1:

> Kann generatorrelative ML-Güte von ziel-/referenzrelativer wissenschaftlicher Güte abweichen, wenn simulationsgenerierte Labels von unterschiedlichen numerischen Operationalisierungen stammen, und lässt sich diese Herkunft kontrolliert bis in One-Step- und Rollout-Ergebnisse verfolgen?

v0.2 verändert nicht den Claim und vergrößert nicht künstlich die Teacher-Differenz. Es korrigiert nur zwei in v0.1 diagnostizierte Hindernisse: globale Phasenextrapolation und ungünstige rohe Target-Skalierung.

## ML2-IC-02 — Unverändertes Zielsystem und Teacher

Unverändert gelten:

```text
G = 1
m1 = m2 = m3 = 1
T_pub = 6.32591398
N = 1000
Delta_t = T_pub / 50
```

Teacher:

```text
G_ref: DOP853, rtol=1e-12, atol=1e-14
G_ref_tight: DOP853, rtol=1e-13, atol=1e-15
G_rk4: exakt ein klassischer RK4-Schritt mit h=Delta_t
```

Die 1000 Inputzustände werden wie in v0.1 aus der primären DOP853-Phasentrajektorie erzeugt. Für jeden gespeicherten Zustand werden beide Teacher-Labels separat neu gestartet. Keine Teacher-Einstellung wird geändert.

## ML2-IC-03 — Phase-stratifizierter Blocksplit

Die geordneten Phaseindizes

```text
j = 0, ..., 999
```

werden in exakt 200 zusammenhängende Blöcke der Länge 5 zerlegt:

```text
block_id = floor(j / 5)
block_id = 0, ..., 199
```

Die Split-Zuweisung ist deterministisch:

```text
block_id mod 5 in {0,1,2} -> train
block_id mod 5 == 3       -> validation
block_id mod 5 == 4       -> test
```

Damit entstehen exakt:

```text
train      = 600 samples
validation = 200 samples
test       = 200 samples
```

Alle drei Splits decken die gesamte nominelle Figure-eight-Phase ab. Innerhalb eines Fünferblocks werden keine Punkte auf verschiedene Splits verteilt.

### Interpretationsgrenze

v0.2 ist ausdrücklich ein **same-orbit interpolation/provenance test**. Die Splitwahl darf nicht als Evidenz für Generalisierung auf neue Orbits, neue Anfangsbedingungen oder starke zeitliche Extrapolation interpretiert werden.

## ML2-IC-04 — Inputnormalisierung

Wie in v0.1:

```text
x_norm = (x - mu_x) / sigma_x
```

`mu_x` und `sigma_x` werden ausschließlich aus den 600 Trainingsinputs berechnet. Komponentenfloor:

```text
sigma_x >= 1e-12
```

Beide Teacher-Modelle verwenden bitgleich denselben Input-Scaler.

## ML2-IC-05 — Gemeinsamer Target-Scaler

Neu in v0.2 wird ein einziger teacher-unabhängiger Target-Scaler ausschließlich aus dem Trainingssplit erzeugt:

```text
Delta_train_shared = concatenate(
    delta_ref[train],
    delta_rk4[train],
    axis=0
)

mu_delta = mean(Delta_train_shared, axis=0)
sigma_delta = std(Delta_train_shared, axis=0)
sigma_delta = maximum(sigma_delta, 1e-12)
```

Beide Modelle lernen mit demselben Scaler:

```text
z_delta_teacher = (delta_teacher - mu_delta) / sigma_delta
```

Die physikalische Vorhersage wird zurücktransformiert:

```text
delta_hat = mu_delta + sigma_delta * f_theta(x_norm)
x_hat_next = x + delta_hat
```

### Schutzregel

Es gibt keinen teacher-spezifischen Target-Scaler. Validation/Test werden weder für `mu_delta` noch `sigma_delta` verwendet. Alle wissenschaftlichen Metriken, Gates und Provenance-Zerlegungen werden nach Rücktransformation in den ursprünglichen dimensionslosen Zustandskoordinaten berechnet.

## ML2-IC-06 — Modellarchitektur

Unverändert:

```text
12 -> 128 -> 128 -> 128 -> 12
activation = tanh
bias = True
residual output
float64 CPU
```

Initialisierung:

```text
Xavier uniform, tanh gain
bias = 0
```

Keine Dropout-, BatchNorm-, LayerNorm-, rekurrenten oder Physics-informed Komponenten.

## ML2-IC-07 — Gepaarte Seeds

Unverändert:

```text
seeds = {0,1,2}
```

Für jeden Seed wird ein Modellzustand einmal initialisiert und bitgleich in das Reference- und RK4-Modell kopiert. Vor dem ersten Optimierungsschritt muss gelten:

```text
parameters_ref == parameters_rk4
```

Ein fehlgeschlagener Seed wird nicht ersetzt.

## ML2-IC-08 — Optimierung

Unverändert gegenüber v0.1:

```text
optimizer = Adam
learning_rate = 1e-3
betas = (0.9, 0.999)
eps = 1e-8
weight_decay = 0
full_batch = True
max_epochs = 5000
validation_every = 1
patience = 500
absolute min_delta = 1e-10
restore_best_validation_checkpoint = True
```

Der Loss wird jetzt auf den gemeinsam standardisierten Target-Inkrementen berechnet:

```text
L = mean((f_theta(x_norm) - z_delta_teacher)^2)
```

Keine Scheduler, kein Gradient Clipping, kein Learning-Rate- oder Hidden-Width-Sweep.

## ML2-IC-09 — Determinismus und Paaridentität

Soweit unterstützt:

```text
torch.use_deterministic_algorithms(True)
torch.set_num_threads(1)
```

Für beide Teacher eines Seed-Paares müssen bitgleich identisch sein:

- Inputarray;
- Splitindizes;
- `mu_x`, `sigma_x`;
- `mu_delta`, `sigma_delta`;
- initiale Parameter;
- Optimizer-Konfiguration;
- Epochbudget und Early-Stopping-Code.

Der einzige systematische Unterschied bleibt das Teacher-Target.

## ML2-IC-10 — One-Step-Metriken in Rohkoordinaten

Nach Rücktransformation werden auf Train, Validation und Test mindestens berechnet:

```text
RMSE_own_teacher
RMSE_vs_ref
RMSE_vs_rk4
MSE_own_teacher
MSE_vs_ref
MSE_vs_rk4
```

mit

```text
RMSE_12(a,b) = sqrt(mean((a-b)^2))
```

über Samples und alle 12 Komponenten.

Direkte numerische Größen:

```text
D_teacher = RMSE_12(y_rk4, y_ref)
D_ref = RMSE_12(y_ref_tight, y_ref)
```

werden getrennt für Train/Validation/Test dokumentiert.

Zusätzlich wird für jedes Modell die **raw-coordinate train RMSE** berichtet, damit sichtbar bleibt, ob bereits das Fitten des Lerngegenstands das Teacher-Signal auflösen kann.

## ML2-IC-11 — Provenance-Fehlerzerlegung

Unverändert in Rohkoordinaten:

```text
e_model   = y_hat_rk4model - y_rk4
e_teacher = y_rk4 - y_ref
e_total   = y_hat_rk4model - y_ref

e_total = e_model + e_teacher
```

Aggregiert:

```text
mean(||e_model||^2)
mean(||e_teacher||^2)
mean(||e_total||^2)
2*mean(<e_model,e_teacher>)
identity_residual
```

Die Alignment-Cosine-Similarity zwischen Modellpaar-Differenz und Teacher-Differenz wird weiterhin nur deskriptiv berichtet und erhält keinen nachträglich gewählten Erfolgsschwellenwert.

## ML2-IC-12 — Vorregistrierte Gates

### G1 — Reference separation

Auf jedem Split:

```text
D_ref <= 0.01 * D_teacher
```

Scheitert dies auf Test, Status `INCONCLUSIVE_REFERENCE`.

### G2 — Paired-control integrity

Inputs, Splits, beide Scaler, Modellinitialisierung und Trainingseinstellungen müssen zwischen den Teacher-Paaren identisch sein. Verletzung führt zu `INVALID_IMPLEMENTATION`.

### G3 — Learner resolvability

Für beide Teacher muss gelten:

```text
median_seed(RMSE_own_teacher_test) < D_teacher_test
```

Scheitert G3 erneut:

```text
INCONCLUSIVE_LEARNER_ERROR
```

und keine Teacher-Provenance-Interpretation.

### G3a — diagnostische Train-Resolvability

Zusätzlich wird berichtet:

```text
median_seed(RMSE_own_teacher_train) < D_teacher_train
```

Dies ist eine Diagnose und kein Ersatz für G3. Besteht G3a, aber G3 nicht, bleibt v0.2 nicht informativ für C07.

## ML2-IC-13 — Seed-Robustheit

Erst nach bestandenem G1–G3 darf ein systematischer Teacher-Effekt diskutiert werden. Eine Richtung gilt in v0.2 als robust, wenn sie in allen drei gepaarten Seeds übereinstimmt.

```text
3/3 = robust for v0.2
2/3 = exploratory only
<2/3 = no systematic effect
```

Keine asymptotischen p-Werte bei drei Seeds.

## ML2-IC-14 — MU1/MU2

Unverändert:

```text
MU1 = 50 learned steps = 1*T_pub
MU2 = 500 learned steps = 10*T_pub
```

Die Rollouts werden technisch erzeugt, aber **wissenschaftlich erst nach bestandenem G1–G3 interpretiert**.

Metriken:

- normalisierter RMS-Positionsfehler gegen DOP853 primary;
- maximaler Positionsfehler;
- relativer Energiefehler;
- maximaler absoluter Energiefehler;
- normalisierter Drehimpulsfehler;
- minimale Paarentfernung;
- maximale Entfernung vom Schwerpunkt;
- maximaler Betrag von `x_norm`;
- maximaler Betrag der vorhergesagten standardisierten Target-Inkremente als zusätzliche OOD-/Numerikdiagnostik.

Invaliditätsregeln bleiben:

```text
non-finite state
minimum pair distance < 0.1
```

## ML2-IC-15 — Rollout-Referenzgate

Primary-vs.-tight DOP853 wird auf demselben MU1/MU2-Raster berichtet. Eine trajectory-basierte Modellrangfolge wird nur quantitativ interpretiert, wenn die relevante Modellabweichung mindestens zwei Größenordnungen über dem Referenzgap liegt.

Dieses Gate ersetzt G3 nicht.

## ML2-IC-16 — Ergebnisstatus

Der v0.2-Run endet genau in einem der folgenden Status:

```text
INFORMATIVE_POSITIVE
INFORMATIVE_NEGATIVE
INCONCLUSIVE_REFERENCE
INCONCLUSIVE_LEARNER_ERROR
INVALID_IMPLEMENTATION
```

`INFORMATIVE_POSITIVE/NEGATIVE` sind erst zulässig, wenn G1–G3 bestanden sind.

Ein Scheitern löst keinen automatischen Architektur-, Seed-, Split-, Teacher- oder Hyperparameter-Sweep aus.

## ML2-IC-17 — Mindesttests vor Full Run

Vor dem wissenschaftlichen v0.2-Run müssen mindestens bestehen:

1. `N=1000`, endliche Arraywerte und erwartete Formen;
2. exakt 200 Blöcke mit je 5 Indizes;
3. exakt 600/200/200 Samples;
4. kein Block wird über mehrere Splits geteilt;
5. alle drei Splits decken die gesamte Phasenrange verteilt ab;
6. Dataset-Erzeugung deterministisch reproduzierbar;
7. Inputs für beide Teacher bitgleich identisch;
8. Input-Scaler ausschließlich aus Trainingsinputs;
9. Shared Target-Scaler ausschließlich aus den Trainingstargets beider Teacher gemeinsam;
10. derselbe Target-Scaler für beide Modelle;
11. Rücktransformation standardisierter Targets reproduziert die Rohtargets numerisch;
12. initiale Modellparameter innerhalb jedes Seed-Paares bitgleich;
13. Optimizer-/Budgetparameter zwischen Paaren identisch;
14. Checkpoints reproduzieren One-Step-Metriken;
15. Provenance-Identität schließt numerisch;
16. MU1/MU2 erzeugen exakt 50 bzw. 500 learned steps.

## ML2-IC-18 — Artefakte

Ein vollständiger Run erzeugt mindestens:

```text
ml_run_v0_2/results/config.json
ml_run_v0_2/results/dataset_summary.json
ml_run_v0_2/results/scalers.json
ml_run_v0_2/results/teacher_metrics.json
ml_run_v0_2/results/training_metrics.csv
ml_run_v0_2/results/one_step_metrics.csv
ml_run_v0_2/results/rollout_metrics.csv
ml_run_v0_2/results/paired_provenance.csv
ml_run_v0_2/results/gates.json
ml_run_v0_2/results/summary.json
ml_run_v0_2/results/trias_ml_audit.md
ml_run_v0_2/checkpoints/*.pt
```

Abbildungen mindestens:

```text
teacher_difference_by_phase.png
split_by_phase.png
one_step_own_vs_ref.png
train_vs_test_resolvability.png
provenance_error_decomposition.png
mu1_rollout_position_error.png
mu2_rollout_position_error.png
mu2_energy_error.png
```

## ML2-IC-19 — Scope Freeze

Nicht Bestandteil von v0.2:

- gröberer/neuer Teacher;
- anderes `Delta_t`;
- Architekturänderung;
- Hidden-width-Sweep;
- Lernraten-Sweep;
- zusätzliche Seeds;
- random point split;
- teacher-spezifische Target-Scaler;
- Physics-informed Regularisierung;
- neue Orbits/Anfangsbedingungen;
- chaotische Dynamik;
- probabilistische UQ;
- externe Daten.

## ML2-IC-20 — Entscheidung nach v0.2

Falls G3 besteht, wird C07 noch nicht automatisch akzeptiert. Zuerst werden own-teacher/common-reference Differenz, Provenance-Zerlegung, Rollouts und Seed-Robustheit ausgewertet; danach erfolgt erneut ein Vergleich mit einem starken Standard-ML-Provenance-/Credibility-Rahmen.

Falls G3 erneut scheitert, wird nicht automatisch weitergetunt. Die nächste wissenschaftliche Entscheidung lautet dann: Teacher-Signal bewusst vergrößern versus anderen AI-for-Science-Fall wählen versus ML-Provenance-Zweig beenden.

## Entscheidungsempfehlung

**ACCEPT.**

Nach `GO` wird dieser Contract als neue Entscheidung eingefroren. Erst danach werden v0.2-Dataset-/Training-Code angepasst, technische Tests und ein nichtwissenschaftlicher Smoke Run durchgeführt.