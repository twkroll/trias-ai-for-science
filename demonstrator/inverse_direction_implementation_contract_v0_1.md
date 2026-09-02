# Inverse-Direction Implementation Contract v0.1

**Status:** PENDING REVIEW  
**Stand:** 2026-09-02  
**Depends on:** D017  
**Purpose:** exakte Vorregistrierung des minimalen inversen Lorenz/SINDy-Provenance-Demonstrators vor jeder Implementierung.

## IC-01 — Wissenschaftliche Leitfrage

Der Run testet ausschließlich:

> Kann bei identischem Lorenz-63-Zielsystem, identischer latenter Referenztrajektorie und identischer Equation-Discovery-Pipeline die kontrollierte Rekonstruktionsprovenance zu reproduzierbar verschiedenen inferierten Gleichungen führen, während vorregistrierte dynamisch/statistische Eigenschaften der inferierten Systeme hinreichend ähnlich bleiben?

Der Run testet **nicht** die Neuheit von Nichtidentifizierbarkeit und nicht die generelle Eignung von SINDy.

## IC-02 — Synthetisches Zielsystem

Lorenz-63 in dimensionslosen Variablen:

```text
dx/dt = 10 (y - x)
dy/dt = 28 x - y - x z
dz/dt = x y - (8/3) z
```

Anfangszustand der latenten Referenzintegration:

```text
x0 = (1.0, 1.0, 1.0)
```

Alle numerischen Rechnungen erfolgen in `float64`.

## IC-03 — Latente Referenztrajektorie

Primäre Referenz:

```text
integrator = DOP853
rtol = 1e-12
atol = 1e-14
t_start = 0.0
t_end = 60.0
dt_obs = 0.01
```

Tight cross-check:

```text
integrator = DOP853
rtol = 1e-13
atol = 1e-15
```

Die gespeicherte primäre latente Trajektorie ist die gemeinsame Quelle für P0/P1/P2.

### Reference gate G1

Auf dem Intervall `[0, 10]` muss der maximale normierte Zustandsabstand zwischen primary und tight reference kleiner als

```text
1e-8
```

sein. Normierung: euklidischer Zustandsfehler geteilt durch `max(1, ||x_tight||_2)` punktweise, anschließend Maximum.

Der lange primary/tight-Trajektorienabstand wird wegen chaotischer Sensitivität **nicht** als globale Ground-Truth-Güte interpretiert und nicht als Gate verwendet.

## IC-04 — Zeitfenster

```text
burn-in / ungenutzt:            [0, 10)
discovery interval:             [10, 50]
held-out vector-field interval: (50, 60]
```

Discovery grid:

```text
N_discovery = 4001
sampling interval = 0.01
```

Held-out grid:

```text
N_holdout = 1000
sampling interval = 0.01
```

Die Missingness/Rekonstruktion wird **nur** auf dem Discovery-Intervall angewendet. Die Held-out-Referenzzustände bleiben vollständig und werden ausschließlich zur unabhängigen Bewertung der inferierten Vektorfelder benutzt.

## IC-05 — Datenpfade

### P0 — complete

```text
reference discovery states
-> no missingness
-> no reconstruction
-> common derivative estimator
-> common SINDy fit
```

### P1 — linear

```text
same reference discovery states
-> 20% missing time points
-> linear interpolation
-> common derivative estimator
-> common SINDy fit
```

### P2 — cubic

```text
same reference discovery states
-> exactly same missing mask as paired P1
-> cubic-spline interpolation
-> common derivative estimator
-> common SINDy fit
```

## IC-06 — Missingness-Masken

Vorregistrierte Seeds:

```text
mask_seeds = {0, 1, 2}
```

Generator:

```text
NumPy Generator(PCG64(seed))
```

Für jeden Seed werden exakt `800` Discovery-Zeitpunkte maskiert. Die zulässigen Mask-Indizes sind

```text
2, 3, ..., N_discovery-3
```

sodass die ersten und letzten zwei Samples beobachtet bleiben. Die 800 Indizes werden ohne Zurücklegen gleichverteilt aus dieser Menge gezogen.

An einem maskierten Zeitpunkt fehlen immer **alle drei** Zustandskomponenten gemeinsam.

P1 und P2 desselben Seeds verwenden bitgleich dieselbe Maske.

### Mask integrity gate G2

Für jeden Seed muss gelten:

- exakt 800 maskierte Zeitpunkte;
- keine maskierten Indizes außerhalb des erlaubten Bereichs;
- P1/P2-Masken identisch;
- P0 enthält keine Missingness;
- alle rekonstruierten Arrays sind endlich.

Andernfalls: `INVALID_IMPLEMENTATION`.

## IC-07 — Rekonstruktion

### P1

Lineare Interpolation komponentenweise auf dem gemeinsamen Zeitgitter, ausschließlich zwischen beobachteten Punkten. Keine Extrapolation.

### P2

Kubische Spline-Interpolation komponentenweise mit

```text
scipy.interpolate.CubicSpline
bc_type = "not-a-knot"
extrapolate = False
```

Da die Randpunkte beobachtet sind, ist keine Extrapolation erforderlich.

Die beobachteten Samples werden nach Rekonstruktion unverändert belassen; nur maskierte Samples werden ersetzt.

### Reconstruction diagnostics

Für P1/P2 werden pro Seed berichtet:

- RMSE der rekonstruierten Zustände an ausschließlich maskierten Punkten gegen die latente Referenz;
- maximale absolute Rekonstruktionsabweichung an maskierten Punkten;
- state-wise RMSE an maskierten Punkten.

Diese Werte sind Diagnosegrößen, keine eigenen Positiv-Gates.

## IC-08 — Gemeinsamer Derivative Estimator

Für alle Pfade wird dieselbe explizite zentrale Fünfpunktformel vierter Ordnung verwendet:

```text
dx_i/dt = (x_{i-2} - 8 x_{i-1} + 8 x_{i+1} - x_{i+2}) / (12 dt)
```

für

```text
i = 2, ..., N_discovery-3.
```

Die ersten und letzten zwei Discovery-Punkte werden aus dem SINDy-Fit ausgeschlossen.

Keine pfadspezifische Glättung oder adaptive Ableitung.

## IC-09 — SINDy Feature Library

Zustandsreihenfolge:

```text
[x, y, z]
```

Feature-Reihenfolge exakt:

```text
[1, x, y, z, x^2, x*y, x*z, y^2, y*z, z^2]
```

Es wird keine zusätzliche Feature-Standardisierung und kein condition-spezifisches Rescaling verwendet.

Wahre Support-Struktur in dieser Library:

```text
dx: x, y
dy: x, y, x*z
dz: z, x*y
```

Wahre Koeffizienten:

```text
dx: x=-10, y=+10
dy: x=+28, y=-1, x*z=-1
dz: z=-8/3, x*y=+1
```

## IC-10 — Sparse Regression

Optimizer: STLSQ-artige sequentielle Thresholded Least Squares mit exakt:

```text
threshold = 0.05
ridge_alpha = 1e-8
max_iterations = 20
fit_intercept = False
```

Ablauf pro Gleichung:

1. Ridge regression auf allen aktuell aktiven Features;
2. Koeffizienten mit `abs(coef) < 0.05` werden auf null gesetzt;
3. Refit auf verbleibendem Support;
4. bis Support unverändert oder maximal 20 Iterationen.

Kein Threshold-Sweep, keine pfadspezifische Regularisierung, keine nachträgliche manuelle Termselektion.

## IC-11 — P0 Structural-Recovery-Gate G3

P0 ist nur dann als valide Baseline akzeptiert, wenn gleichzeitig gilt:

```text
overall support precision = 1.0
overall support recall    = 1.0
spurious-term count       = 0
missing-true-term count   = 0
max relative coefficient error on true terms <= 0.05
```

Relative coefficient error pro wahrem Term:

```text
abs(c_hat - c_true) / abs(c_true)
```

Falls G3 scheitert:

```text
INCONCLUSIVE_BASELINE
```

und es erfolgt **keine** Provenance-Interpretation von P1/P2.

## IC-12 — Structural Metrics für P1/P2

Für jeden Seed und Pfad werden berichtet:

```text
support precision
support recall
spurious-term count
missing-true-term count
support Jaccard vs truth
support Jaccard vs P0
max relative coefficient error on true terms
RMS relative coefficient error on true terms
```

Eine **substantielle structural perturbation** gegenüber P0 liegt für einen Seed vor, wenn mindestens eines gilt:

```text
support Jaccard vs P0 < 1.0
```

oder

```text
max relative coefficient deviation from P0 on true terms >= 0.20
```

Ein pfadspezifischer struktureller Effekt gilt für v0.1 als seed-konsistent, wenn er in mindestens `2/3` Mask-Seeds auftritt.

## IC-13 — Held-out Vector-Field Metric

Auf allen vollständigen Zuständen des Held-out-Intervalls `(50,60]` wird das inferierte Vektorfeld gegen das exakte Lorenz-Vektorfeld bewertet.

Normierter RMSE:

```text
VF_NRMSE = RMS(||f_hat(x_i)-f_true(x_i)||_2) / RMS(||f_true(x_i)||_2)
```

Dieser Wert wird für P0 und jede P1/P2-Instanz berichtet.

Für dynamische Adäquanz gilt als Gate-Komponente:

```text
VF_NRMSE <= 0.20
```

## IC-14 — Short-Horizon Forward Test

Fünf held-out anchor states werden aus der Referenztrajektorie genommen bei

```text
t = {50, 52, 54, 56, 58}.
```

Von jedem Anchor werden das wahre Lorenz-System und jede inferierte ODE für exakt

```text
horizon = 1.0
output_dt = 0.01
```

mit DOP853 (`rtol=1e-10`, `atol=1e-12`) integriert.

Pro Anchor wird der normierte RMS-Zustandsfehler berichtet; anschließend Median und Maximum über die fünf Anchors.

Diese Metrik ist **berichtspflichtig, aber nicht Bestandteil der operativen Äquivalenzentscheidung**, da chaotische lokale Divergenz nicht mit Langzeitstatistik gleichgesetzt wird.

## IC-15 — Autonomous Long-Time Statistical Test

Für das wahre Lorenz-System und jede inferierte ODE wird vom gemeinsamen Zustand `x_ref(t=10)` autonom integriert:

```text
t = 0 ... 100
output_dt = 0.01
DOP853 rtol = 1e-10
DOP853 atol = 1e-12
```

Die ersten `20` Zeiteinheiten werden als autonomous burn-in verworfen. Statistikfenster:

```text
[20,100]
```

Ein Rollout ist technisch valide, wenn alle Zustände endlich bleiben und

```text
max_t ||x(t)||_2 < 100
```

gilt. Andernfalls gilt die jeweilige inferierte ODE als `DYNAMICAL_FAILURE`.

## IC-16 — Vorregistriertes Observable-Set O

Auf dem Statistikfenster werden für jedes Modell berechnet:

1. state-wise mean `mu_x, mu_y, mu_z`;
2. state-wise standard deviation `sigma_x, sigma_y, sigma_z`;
3. 3x3 correlation matrix;
4. marginal 1-Wasserstein-Distanz für `x,y,z`, jeweils normiert durch die Referenz-Standardabweichung des Zustands.

Largest-Lyapunov-Exponent wird, falls technisch stabil implementierbar, **sekundär berichtet**, ist in v0.1 aber kein Gate. Dadurch bleibt der MVP klein und die Äquivalenzentscheidung hängt nicht an einem zusätzlichen empfindlichen Estimator.

## IC-17 — Operative Äquivalenztoleranzen

Eine inferierte ODE gilt bezüglich des vorregistrierten Sets `O` als dynamisch/statistisch hinreichend ähnlich zum wahren Lorenz-System, wenn alle folgenden Bedingungen erfüllt sind:

```text
VF_NRMSE <= 0.20
max_j abs(mu_hat_j - mu_ref_j) / sigma_ref_j <= 0.25
max_j abs(sigma_hat_j - sigma_ref_j) / sigma_ref_j <= 0.20
Frobenius_norm(Corr_hat - Corr_ref) <= 0.30
max_j W1_j / sigma_ref_j <= 0.25
```

Zusätzlich muss der autonome Rollout technisch valide sein.

Diese Toleranzen sind vor dem wissenschaftlichen Run eingefroren und dürfen danach nicht angepasst werden.

## IC-18 — Ergebnislogik

### INFORMATIVE_POSITIVE

Nur wenn:

1. G1, G2 und G3 bestehen;
2. mindestens einer der Rekonstruktionspfade P1 oder P2 zeigt einen seed-konsistenten strukturellen Effekt in mindestens `2/3` Seeds;
3. für mindestens `2/3` derselben Seeds ist die betroffene inferierte ODE zugleich nach IC-17 dynamisch/statistisch hinreichend ähnlich;
4. die Differenz ist durch die gepaarte Designlogik einer konkreten inversen Provenance-Stufe zuordenbar.

### INFORMATIVE_NEGATIVE

Wenn G1–G3 bestehen, aber kein Pfad die positive Kombination aus reproduzierbarer struktureller Perturbation und hinreichender dynamischer Adäquanz erfüllt. Dazu zählen sowohl strukturelle Stabilität als auch Fälle, in denen strukturelle Veränderungen stets mit klarer dynamischer Degradation einhergehen.

### INCONCLUSIVE_REFERENCE

G1 verletzt.

### INCONCLUSIVE_BASELINE

G3 verletzt.

### INVALID_IMPLEMENTATION

G2 oder andere technische Integritätsprüfungen verletzt.

Ein einzelnes `DYNAMICAL_FAILURE` macht nur die betreffende Modellinstanz dynamisch inadäquat; es macht den gesamten Run nicht automatisch invalid.

## IC-19 — Directed-Trias-Provenance-Audit

Für P0 sowie jedes P1/P2-Modell wird maschinen- und menschenlesbar dokumentiert:

```text
target system
latent reference solver
sampling operator
missingness seed and mask hash
reconstruction operation
derivative estimator
feature library
optimizer and threshold
inferred support and coefficients
forward-validation solver
validated observables
result class
scope of justified interpretation
```

Für jede gerichtete Kante werden zusätzlich vier Auditfragen beantwortet:

1. Welches epistemische Objekt liegt vor dem Übergang vor?
2. Welche Operation transformiert es?
3. Welche Information kann verloren, ergänzt oder verzerrt werden?
4. Welche spätere Aussage wird dadurch konditioniert?

## IC-20 — Comparator-Freeze

Erst **nach** der vorregistrierten numerischen Klassifikation wird derselbe Befund getrennt beschrieben als:

```text
A. Standard System Identification / structural error
B. Identifiability / Observability, soweit begrifflich einschlägig
C. SciML V&V / credibility
D. Workflow/Data Provenance
E. Directed Trias
```

Der Trias-Mehrwert wird nicht aus einem positiven inversen Experiment allein abgeleitet. C06-R/C07-L-Rc dürfen nur gestärkt werden, wenn der anschließende Comparator-Test eine zusätzliche Integrations-/Zuordnungsleistung zeigt.

## IC-21 — Required Artifacts

Der wissenschaftliche Full Run muss mindestens erzeugen:

```text
results/inverse_config.json
results/reference_check.json
results/mask_manifest.json
results/reconstruction_metrics.csv
results/sindy_models.json
results/structural_metrics.csv
results/dynamical_metrics.csv
results/equivalence_summary.json
results/inverse_trias_audit.md
results/scientific_gate_report.md
figures/equation_support_comparison.png
figures/structural_vs_dynamical.png
figures/attractor_comparison.png
```

Zusätzlich werden Software-/Paketversionen und Git-Commit des Runs gespeichert.

## IC-22 — Technische Tests vor Full Run

Vor einem wissenschaftlichen Run müssen mindestens Tests bestehen für:

- Lorenz RHS gegen analytisch bekannte Werte;
- deterministische DOP853-Sampling-Ausgabe;
- exakte Maskenzahl und Seed-Reproduzierbarkeit;
- identische P1/P2-Masken;
- Interpolation erhält beobachtete Punkte exakt;
- Fünfpunkt-Ableitung auf einem analytischen Testsignal zeigt erwartete Verfeinerung;
- Library-Reihenfolge exakt wie IC-09;
- STLSQ-Support-Thresholding deterministisch;
- P0-SINDy-Pipeline auf einem kleinen vollständigen Datensatz läuft end-to-end;
- Structural-Metric-Funktionen gegen handkonstruierte Supports;
- Statistical-Metric-Funktionen gegen identische Zeitreihen liefern Nullabstand.

Ein Smoke Run darf verkürzte Zeitfenster verwenden, ist aber wissenschaftlich nicht interpretierbar.

## IC-23 — Scope Freeze

Verboten vor einem gesonderten GO:

- Änderung von Missingness-Rate oder Seeds;
- zusätzliche Missingness-Arten;
- Measurement Noise;
- alternative Rekonstruktionsverfahren;
- Threshold-/Alpha-Sweeps;
- condition-spezifisches Tuning;
- größere/andere Feature Libraries;
- alternative Equation-Discovery-Algorithmen;
- Neural Networks;
- Three-body chaos;
- ML-v0.2-Full-Run;
- nachträgliches Ändern der Äquivalenztoleranzen;
- verpflichtende Koopman-Analyse.

## Entscheidungsempfehlung

**ACCEPT.**

Der Contract hält den inversen MVP klein, trennt strukturelle von dynamisch-statistischer Güte, kontrolliert die Rekonstruktionsprovenance durch gepaarte Masken und verhindert durch G1–G3 sowie vorregistrierte Äquivalenztoleranzen eine nachträgliche Anpassung an ein gewünschtes Narrativ.

Bei `GO` wird dieser Contract eingefroren. Erst danach darf ein Code-Skeleton implementiert, technisch getestet und in einem nichtwissenschaftlichen Smoke Run geprüft werden. Der wissenschaftliche Full Run benötigt anschließend ein weiteres GO.