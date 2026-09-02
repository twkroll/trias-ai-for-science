# ML Implementation Contract v0.1

**Status:** PENDING REVIEW  
**Depends on:** D010  
**Purpose:** alle technischen Entscheidungen des minimalen AI-for-Science-Provenance-Tests vor Datengenerierung, Training und Interpretation einfrieren.  
**Rule:** keine Trainingsläufe und kein Hyperparameter-Tuning vor Akzeptanz dieses Contracts.

## ML-IC-01 — Wissenschaftlicher Zweck

Der Contract operationalisiert ausschließlich die in D010 akzeptierte Frage:

> Kann generatorrelative ML-Güte von ziel-/referenzrelativer wissenschaftlicher Güte abweichen, wenn simulationsgenerierte Labels von unterschiedlichen numerischen Operationalisierungen stammen, und lässt sich diese Herkunft kontrolliert bis in One-Step- und Rollout-Ergebnisse verfolgen?

Der Contract dient nicht der Suche nach einem möglichst leistungsfähigen neuronalen Netz.

## ML-IC-02 — Unverändertes synthetisches Zielsystem

Es gelten unverändert die akzeptierten Figure-eight-Einstellungen:

```text
G = 1
m1 = m2 = m3 = 1
T_pub = 6.32591398
```

mit den bereits in D006 eingefrorenen publizierten gerundeten Anfangsdaten.

Keine Anfangsdatenverfeinerung, kein neues System, keine Perturbation, keine Kollisionsregularisierung.

## ML-IC-03 — Phaseninputs

Es werden exakt `N = 1000` Startphasen verwendet:

```text
t_j = j * T_pub / 1000
j = 0, ..., 999
```

Der Endpunkt `T_pub` wird nicht zusätzlich aufgenommen, damit keine nominal doppelte Phase entsteht.

Die Inputzustände `x_j` werden mit der bereits akzeptierten primären DOP853-Konfiguration entlang einer nominellen Periode erzeugt:

```text
method = DOP853
rtol = 1e-12
atol = 1e-14
float64
```

Eine zweite Inputtrajektorie mit

```text
rtol = 1e-13
atol = 1e-15
```

wird ausschließlich als Referenz-Cross-Check erzeugt. Trainiert wird auf den gespeicherten primären `x_j`, sodass beide Teacher-Datensätze exakt dieselben Inputs verwenden.

## ML-IC-04 — Teacher-Map und Labelerzeugung

Der gemeinsame Vorhersagehorizont ist

```text
Delta_t = T_pub / 50
```

Für jeden gespeicherten Inputzustand `x_j` werden die Labels **unabhängig vom Phasen-Trajektorienlauf** durch Neustart am gleichen `x_j` erzeugt.

### Reference teacher `G_ref`

Von `x_j` aus wird DOP853 für genau `Delta_t` integriert mit

```text
rtol = 1e-12
atol = 1e-14
```

und zusätzlich mit der engeren Cross-Check-Konfiguration

```text
rtol = 1e-13
atol = 1e-15.
```

Damit entstehen

```text
y_ref[j]
y_ref_tight[j]
```

für exakt denselben Startzustand.

### Coarse teacher `G_rk4`

Von demselben `x_j` wird genau **ein** klassischer RK4-Schritt mit

```text
h = Delta_t = T_pub / 50
```

ausgeführt. Es wird dieselbe RHS-/Kraftimplementierung wie im akzeptierten numerischen Demonstrator verwendet.

### Lernziel

Für beide Teacher wird der Inkrementoperator gelernt:

```text
delta_ref[j] = y_ref[j] - x_j
delta_rk4[j] = y_rk4[j] - x_j
```

## ML-IC-05 — Gespeicherter Datensatz und Provenance

Der generierte Datensatz speichert mindestens:

```text
phase_index
phase_time
x
y_ref
y_ref_tight
y_rk4
delta_ref
delta_rk4
split
```

Zusätzlich werden sämtliche Generatorparameter, Softwareversionen und die Hashes bzw. Versionsstände der verwendeten Dynamik-/Integratorimplementierung in einer maschinenlesbaren Konfiguration dokumentiert.

Die Datensätze werden nicht separat erzeugt und später zusammengeführt; beide Teacher-Labels werden in einem gemeinsamen deterministischen Datengenerationslauf an dieselben `x_j` gebunden.

## ML-IC-06 — Split

Der in D010 akzeptierte zusammenhängende Phasenblock-Split wird exakt eingefroren:

```text
train:      j =   0, ..., 599   (600 samples)
validation: j = 600, ..., 799   (200 samples)
test:       j = 800, ..., 999   (200 samples)
```

Es gibt kein zufälliges Mischen über Splitgrenzen und keine Ersetzung durch einen random split.

Der Test beansprucht damit keine Generalisierung auf neue Orbits. Er prüft eine gehaltene Phase derselben Zielinstanz unter kontrollierter Teacher-Provenance.

## ML-IC-07 — Normalisierung

Nur die **Inputs** werden komponentenweise standardisiert:

```text
x_norm = (x - mu_x) / sigma_x
```

wobei `mu_x` und `sigma_x` ausschließlich aus den 600 Trainingsinputs berechnet werden.

Für jede Komponente gilt ein numerischer Floor

```text
sigma_x >= 1e-12.
```

Die Zielinkremente `delta_ref` und `delta_rk4` werden in den dimensionslosen physikalischen Koordinaten **nicht teacherabhängig standardisiert**. Dadurch besitzt kein Modell einen durch den jeweils anderen Teacher bestimmten Target-Scaler.

Beide Modelle eines Seeds verwenden exakt dieselben `mu_x` und `sigma_x`.

## ML-IC-08 — Modellarchitektur

Genau eine Modellklasse wird verwendet:

```text
12 -> 128 -> 128 -> 128 -> 12
```

mit

```text
activation = tanh
bias = True
```

und Residualausgabe

```text
x_hat_next = x + f_theta(x_norm).
```

Keine Dropout-, BatchNorm-, LayerNorm-, Attention- oder rekurrenten Komponenten.

Gewichtinitialisierung:

```text
Xavier uniform, tanh gain
bias = 0
```

Alle Trainings- und Inferenzrechnungen laufen in `float64` auf CPU.

## ML-IC-09 — Gepaarte Seeds und Determinismus

Verwendet werden exakt

```text
seeds = {0, 1, 2}
```

Für jeden Seed wird die Architektur genau einmal initialisiert. Der resultierende `state_dict` wird anschließend bitgleich in das `G_ref`- und das `G_rk4`-Modell geladen.

Damit gilt innerhalb eines Seed-Paares vor dem ersten Optimierungsschritt:

```text
parameters_ref == parameters_rk4
```

Es werden, soweit von der verwendeten PyTorch-Version unterstützt,

```text
torch.use_deterministic_algorithms(True)
torch.set_num_threads(1)
```

aktiviert.

Ein fehlgeschlagener Seed wird nicht durch einen neuen Seed ersetzt.

## ML-IC-10 — Optimierung

Training erfolgt full-batch auf den 600 Trainingssamples.

Optimizer:

```text
Adam
learning_rate = 1e-3
betas = (0.9, 0.999)
eps = 1e-8
weight_decay = 0
```

Loss:

```text
mean squared error of the 12 raw state increments
```

also

```text
L = mean((f_theta(x_norm) - delta_teacher)^2).
```

Trainingsbudget:

```text
max_epochs = 5000
validation_every = 1 epoch
```

Early stopping:

```text
patience = 500 epochs
absolute min_delta = 1e-10 in validation MSE
restore best validation checkpoint = True
```

Keine Lernratenscheduler, kein Gradient Clipping, keine Weight Decay und kein nachträgliches teacher-spezifisches Tuning.

Falls Loss oder Parameter nicht endlich werden, wird der Seed als `INVALID_TRAINING` markiert. Die Architektur oder Lernrate wird im selben Experiment nicht angepasst.

## ML-IC-11 — One-Step-Metriken

Für Zustandsarrays `a,b` mit `N` Samples wird definiert:

```text
RMSE_12(a,b) = sqrt(mean((a-b)^2))
```

über Samples und alle 12 Zustandskomponenten.

Für jedes Modell und jeden Seed werden auf dem Testsplit mindestens berichtet:

```text
RMSE_own_teacher
RMSE_vs_ref
RMSE_vs_rk4
MSE_own_teacher
MSE_vs_ref
MSE_vs_rk4
```

Zusätzlich wird die direkte Teacher-Differenz separat für Train/Validation/Test gespeichert:

```text
D_teacher = RMSE_12(y_rk4, y_ref)
```

und die Referenzunsicherheit

```text
D_ref = RMSE_12(y_ref_tight, y_ref).
```

## ML-IC-12 — Explizite Provenance-Fehlerzerlegung

Für das RK4-trainierte Modell wird auf jedem Testsample die exakte Vektoridentität dokumentiert:

```text
e_model   = y_hat_rk4model - y_rk4
e_teacher = y_rk4 - y_ref
e_total   = y_hat_rk4model - y_ref

e_total = e_model + e_teacher
```

Aggregiert werden:

```text
mean(||e_model||^2)
mean(||e_teacher||^2)
mean(||e_total||^2)
2*mean(<e_model,e_teacher>)
```

sodass geprüft werden kann, ob die gemeinsame Referenzabweichung überwiegend aus ML-Approximation, Teacher-Differenz oder deren Ausrichtung entsteht.

Zusätzlich wird die Alignment-Kennzahl zwischen

```text
(y_hat_rk4model - y_hat_refmodel)
```

und

```text
(y_rk4 - y_ref)
```

als deskriptive Cosine-Similarity auf dem Testsplit berichtet. Für diese Kennzahl wird **kein** nachträglich gewählter Erfolgsschwellenwert verwendet.

## ML-IC-13 — Teacher-/Reference-Gates

Vor Interpretation eines Teacher-Provenance-Effekts müssen folgende Gates erfüllt sein.

### G1 — Reference separation

Auf jedem Split muss die numerische Reference-Tight-Differenz wesentlich kleiner als die Teacher-Differenz sein. Primäres Gate:

```text
D_ref <= 0.01 * D_teacher
```

Wird dies auf dem Testsplit verletzt, werden keine Aussagen über eine durch RK4 versus DOP853 verursachte Labeldifferenz gemacht, bevor die Referenz verstärkt ist.

### G2 — Identical-input gate

Die gespeicherten Inputarrays, Splitindizes und Inputnormalisierung müssen für beide Teacher bitgleich sein.

### G3 — Teacher-resolvability by the learner

Damit der Test den Teacher-Effekt überhaupt auflösen kann, muss für beide Teacher gelten:

```text
median_seed(RMSE_own_teacher_test) < D_teacher_test.
```

Wird dieses Gate verletzt, wird der Provenance-Test als `INCONCLUSIVE / LEARNER ERROR DOMINATES` klassifiziert. Es folgt kein Hyperparameter-Sweep innerhalb v0.1.

## ML-IC-14 — Rollout-Referenzen und Teacher-Baselines

Für Rollouts wird vom publizierten Anfangszustand `x0` aus ein gemeinsames Raster mit

```text
Delta_t = T_pub / 50
```

bis `10*T_pub` erzeugt.

Gespeichert werden:

1. primäre DOP853-Referenz;
2. engere DOP853-Cross-Check-Referenz;
3. wiederholt angewendeter coarse RK4-Teacher mit `h=Delta_t`;
4. jeder gelernte `G_ref`-Surrogat-Rollout;
5. jeder gelernte `G_rk4`-Surrogat-Rollout.

Damit kann nicht nur Modell versus Referenz, sondern auch Modell versus eigener Teacher-Rollout verglichen werden.

## ML-IC-15 — MU1 und MU2

### MU1

```text
50 learned steps = 1*T_pub
```

### MU2

```text
500 learned steps = 10*T_pub
```

Für jeden Seed, jedes Teacher-Modell und beide Use Cases werden mindestens berichtet:

- normalisierter RMS-Positionsfehler gegen primäre DOP853-Referenz;
- maximaler Positionsfehler über den Horizont;
- relativer Energiefehler;
- maximaler absoluter Energiefehler;
- normalisierter Drehimpulsfehler;
- minimale Paarentfernung;
- maximale Entfernung vom Schwerpunkt;
- maximaler Betrag der standardisierten Netzwerkeingaben als OOD-Diagnostik.

Ein Rollout wird als invalid markiert, wenn

```text
non-finite state
```

auftritt oder die bereits verwendete technische Guard

```text
minimum pair distance < 0.1
```

ausgelöst wird. Ein invalides Rollout wird nicht stillschweigend abgeschnitten und als erfolgreicher Lauf gewertet.

## ML-IC-16 — Rollout-Referenzgate

Für jede trajectory-basierte MU1/MU2-Aussage wird die primäre-versus-engere DOP853-Differenz auf demselben Raster berichtet.

Eine quantitative Rangfolge der ML-Trajektorien wird nur interpretiert, wenn die relevante Modellabweichung mindestens zwei Größenordnungen über dem Referenzgap liegt. Strukturdiagnostik kann separat diskutiert werden, sofern ihre Evidenz nicht von dieser Trajektorienrangfolge abhängt.

## ML-IC-17 — Seed-Robustheit

Primäre Aussagen über einen systematischen Teacher-Provenance-Effekt werden nur als robust bezeichnet, wenn die Richtung des gepaarten Effekts für alle drei Seeds übereinstimmt.

Beispiel für die gemeinsame Referenzbewertung:

```text
Delta_ref(seed) = RMSE_vs_ref(rk4-trained, seed)
                  - RMSE_vs_ref(ref-trained, seed)
```

Interpretation:

- gleiche Richtung in `3/3` Seeds: robust für v0.1;
- gleiche Richtung in `2/3` Seeds: explorativ, nicht als robuster Hauptbefund;
- keine konsistente Richtung: kein systematischer Teacher-Effekt behauptet.

Mit nur drei Seeds werden keine asymptotischen Signifikanztests oder künstlich präzisen p-Werte berichtet.

## ML-IC-18 — Baseline-ML versus Trias-Provenance

Die Ergebnisinterpretation wird wieder doppelt protokolliert.

### Baseline ML view

- Trainings-/Validierungsverlauf;
- Test-MSE/RMSE;
- Seed-Streuung;
- MU1/MU2-Rolloutfehler.

### Trias-Provenance view

Zusätzlich:

- Herkunft jedes Inputs und Labels;
- numerische Unsicherheit des Reference teachers;
- direkte Teacher-Differenz;
- `ML ↔ Teacher` versus `ML ↔ gemeinsame Referenz`;
- Provenance-Fehlerzerlegung;
- Invarianten-/Strukturverhalten;
- epistemische Lokalisierung einer Abweichung entlang `Theorie → Simulation → Daten → ML → Gebrauch`.

Nach dem Lauf wird diese Trias-Ansicht erneut gegen einen **starken Standard-ML-Provenance-/Credibility-Rahmen** verglichen. Eine neue Terminologie oder zusätzliche Tabelle allein gilt nicht als Originalitätsnachweis.

## ML-IC-19 — Mindesttests vor wissenschaftlicher Interpretation

Vor Auswertung des ML-Claims müssen mindestens folgende technische Tests bestehen:

1. `N=1000`, erwartete Arrayformen und endliche Werte;
2. deterministische Reproduktion der Dataset-Erzeugung;
3. exakt identische `x_j` und Splitindizes für beide Teacher;
4. keine Nutzung von Validation/Test für `mu_x` oder `sigma_x`;
5. RK4-Labelerzeugung entspricht exakt einem Schritt mit `h=T_pub/50` der akzeptierten Implementierung;
6. DOP853 primary/tight teacher outputs werden separat gespeichert;
7. innerhalb jedes Seed-Paares sind die initialen Parameter bitgleich;
8. Training mit gleichem Optimizer, Budget und Early-Stopping-Code;
9. Checkpoints reproduzieren gespeicherte Testmetriken;
10. MU1/MU2 erzeugen exakt 50 bzw. 500 learned steps;
11. Provenance-Fehleridentität `e_total=e_model+e_teacher` wird numerisch geprüft;
12. alle Configs und Softwareversionen werden maschinenlesbar gespeichert.

## ML-IC-20 — Ergebnisstatus

Der Run endet genau in einem der folgenden Status:

```text
INFORMATIVE_POSITIVE
INFORMATIVE_NEGATIVE
INCONCLUSIVE_REFERENCE
INCONCLUSIVE_LEARNER_ERROR
INVALID_IMPLEMENTATION
```

Ein nichtinformativer oder negativer Status löst **keine** automatische Architekturvergrößerung, Schrittweitenänderung, Seed-Erweiterung oder Hyperparameteroptimierung aus.

## ML-IC-21 — Ausgabeartefakte

Ein vollständiger Lauf erzeugt mindestens:

```text
ml_run_v0_1/results/config.json
ml_run_v0_1/results/dataset_summary.json
ml_run_v0_1/results/teacher_metrics.json
ml_run_v0_1/results/training_metrics.csv
ml_run_v0_1/results/one_step_metrics.csv
ml_run_v0_1/results/rollout_metrics.csv
ml_run_v0_1/results/paired_provenance.csv
ml_run_v0_1/results/summary.json
ml_run_v0_1/results/trias_ml_audit.md

ml_run_v0_1/figures/teacher_difference_by_phase.png
ml_run_v0_1/figures/one_step_own_vs_ref.png
ml_run_v0_1/figures/mu1_rollout_position_error.png
ml_run_v0_1/figures/mu2_rollout_position_error.png
ml_run_v0_1/figures/mu2_energy_error.png
ml_run_v0_1/figures/provenance_error_decomposition.png
```

Checkpoints für alle sechs trainierten Modelle werden ebenfalls gespeichert, aber nicht als wissenschaftliche Evidenz an sich interpretiert.

## ML-IC-22 — Scope Freeze

Nicht Bestandteil dieses Contracts:

- Architekturvergleich;
- hidden-width sweep;
- Lernraten-Sweep;
- zusätzliche Seeds;
- zufälliger Split als Alternative;
- physics-informed Regularisierung;
- neue Teacher-Solver;
- neue Anfangsbedingungen;
- chaotische Dynamik;
- probabilistische UQ;
- externe Daten;
- Anpassung von `Delta_t` nach Sichtung der Ergebnisse.

## Akzeptanzkriterium dieses Contracts

Der Contract soll vor Training sicherstellen, dass ein beobachteter Unterschied möglichst eindeutig der Kette

```text
numerischer Teacher
→ Trainingslabel
→ gelerntes Modell
→ wissenschaftlicher Gebrauch
```

zugeordnet werden kann und nicht nachträglich durch Architektur- oder Tuningentscheidungen erzeugt wird.

## Entscheidungsempfehlung

**ACCEPT.**

Nach `GO` wird dieser Contract eingefroren. Erst dann werden Dataset-/ML-Code implementiert, technische Tests ausgeführt und anschließend ein kleiner Smoke Run durchgeführt. Der wissenschaftliche Full Run folgt erst nach Review des getesteten ML-Skeletons.