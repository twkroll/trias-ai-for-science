# Minimal Inverse-Direction Demonstrator v0.1

**Status:** PENDING REVIEW  
**Depends on:** D016  
**Purpose:** minimaler kontrollierter Test der inversen Directed-Trias-Kette `target/observation -> data -> preprocessing -> inference -> theory`.

## 1. Wissenschaftliche Leitfrage

> Kann bei identischem zugrunde liegendem dynamischem Zielsystem und identischer Equation-Discovery-Pipeline eine kontrollierte Änderung der Beobachtungs-/Rekonstruktionsprovenance zu strukturell verschiedenen inferierten Gleichungen führen, während ausgewählte dynamische oder statistische Eigenschaften der daraus erzeugten Systeme ähnlich bleiben?

Der Demonstrator testet damit nicht, ob Nichtidentifizierbarkeit existiert. Er testet, ob die Directed Trias einen klaren, reproduzierbaren inversen Provenance-Fall lokalisieren und anschließend gegen etablierte Identifiability-/System-Identification-/Provenance-Frameworks vergleichen kann.

## 2. Synthetisches Zielsystem

Verwendet wird ausschließlich Lorenz-63:

```text
dx/dt = sigma (y - x)
dy/dt = x (rho - z) - y
dz/dt = x y - beta z
```

mit

```text
sigma = 10
rho   = 28
beta  = 8/3
```

Lorenz-63 wird hier als **synthetisches Zielsystem** genutzt. Die wahre Gleichungsstruktur ist bekannt und dient ausschließlich dazu, structural equation fidelity kontrolliert beurteilen zu können.

Kein Drei-Körper-Chaos in v0.1.

## 3. Reference-Trajektorie

Eine hochgenaue DOP853-Lösung erzeugt eine gemeinsame latente Referenztrajektorie.

Vorläufige Spezifikation für den späteren Implementation Contract:

```text
rtol = 1e-12
atol = 1e-14
sampling interval dt_obs = 0.01
burn-in >= 10 Lorenz time units
usable observation interval >= 50 Lorenz time units
float64
```

Alle Beobachtungs-/Rekonstruktionsbedingungen werden aus **derselben** latenten Referenztrajektorie abgeleitet.

Die exakten Anfangsbedingungen, Zeitfenster und Cross-Check-Toleranzen werden erst im Implementation Contract eingefroren.

## 4. Minimaler Provenance-Kontrast

v0.1 verwendet drei Datenpfade.

### P0 — vollständige Beobachtung

```text
latent trajectory
-> complete sampled state series
-> common derivative estimation
-> common SINDy pipeline
-> T_hat_complete
```

### P1 — Missingness + lineare Rekonstruktion

```text
same latent trajectory
-> fixed random missing-time mask
-> linear interpolation
-> common derivative estimation
-> common SINDy pipeline
-> T_hat_linear
```

### P2 — dieselbe Missingness + kubische Rekonstruktion

```text
same latent trajectory
-> exactly the same missing-time mask as P1
-> cubic-spline interpolation
-> common derivative estimation
-> common SINDy pipeline
-> T_hat_cubic
```

Damit bleibt zwischen P1 und P2 insbesondere **die Beobachtungsmaske identisch**. Der systematische Unterschied ist die Rekonstruktionsoperation.

Vorläufig wird eine Missingness-Rate von **20 % der abgetasteten Zeitpunkte** vorgeschlagen. An einem entfernten Zeitpunkt fehlen alle drei Zustandskomponenten gemeinsam. Die endgültige Rate wird im Implementation Contract nur dann geändert, wenn ein technischer Pilot zeigt, dass 20 % zu einem trivial invaliden Rekonstruktionsproblem führt; eine solche Änderung wäre vor dem wissenschaftlichen Run separat zu genehmigen.

## 5. Mask-Robustheit

Der Missingness-Effekt soll nicht an einer einzigen zufälligen Maske hängen. Deshalb werden drei vorregistrierte Mask-Seeds verwendet:

```text
mask_seeds = {0, 1, 2}
```

P0 wird einmal erzeugt. Für jeden Mask-Seed werden P1 und P2 gepaart aus exakt derselben Maske erzeugt.

Es gibt keinen nachträglichen Mask-Seed-Sweep.

## 6. Gemeinsame Equation-Discovery-Pipeline

Alle Datenpfade verwenden **dieselbe** Inferenzpipeline.

Für v0.1 wird eine klassische SINDy-Variante vorgesehen:

```text
state variables = x, y, z
feature library = polynomial library up to degree 2
optimizer = STLSQ-type sparse regression
same threshold / regularization for all data paths
same derivative estimator for all data paths
no per-condition hyperparameter tuning
```

Die quadratische Bibliothek ist absichtlich minimal ausreichend, um die wahre Lorenz-Struktur zu enthalten.

Der Implementation Contract friert Library ordering, Skalierung, Derivative Estimator, Sparse Threshold, Regularisierung und Fit-Window exakt ein.

### Baseline-Gate

Die vollständige P0-Pipeline muss die bekannte Lorenz-Struktur hinreichend gut rekonstruieren. Falls schon P0 keine sinnvolle structural recovery erreicht, darf ein Unterschied von P1/P2 nicht als Provenance-Effekt interpretiert werden.

## 7. Zwei getrennte Bewertungsachsen

### A. Structural equation fidelity

Mindestens:

```text
true-term support recovery
support precision
support recall
spurious-term count
missing-true-term count
pairwise support Jaccard
coefficient error on true terms
```

Die wahre Lorenz-Struktur ist bekannt:

```text
dx: x, y
dy: x, y, x*z
dz: z, x*y
```

Vorzeichen und Koeffizienten werden separat von bloßer Termpräsenz bewertet.

### B. Dynamical / statistical adequacy

Die inferierten ODEs werden anschließend als eigenständige Forward-Modelle integriert.

Mindestens:

```text
finite/bounded autonomous rollout
short-horizon trajectory error
held-out vector-field error on reference states
state-wise long-time mean and standard deviation
covariance/correlation structure
marginal-distribution distance for x, y, z
largest Lyapunov exponent or a documented lower-cost chaos diagnostic
```

Koopman-Spektren werden **nicht** zum verpflichtenden MVP-Metrikset gemacht. Sie können später ergänzt werden, falls der Minimalfall bereits trägt.

## 8. Operative Äquivalenz

Projektintern wird weiterhin

```text
T1 ~_(O, epsilon) T2
```

verwendet, wenn zwei inferierte Modelle bezüglich eines vorab definierten Observable-Sets `O` innerhalb vorab definierter Toleranzen praktisch ähnlich sind.

Die Toleranzen werden **vor dem wissenschaftlichen Run im Implementation Contract** festgelegt. Sie dürfen nicht nach Sichtung der Resultate gewählt werden.

Wichtig:

```text
operative equivalence != structural identity
```

ist ein etablierter methodologischer Kontext und wird nicht als Trias-Neuheit beansprucht.

## 9. Vorregistrierte Interpretationslogik

Ein **informativ positiver inverser Provenance-Fall** liegt nur vor, wenn alle folgenden Bedingungen erfüllt sind:

1. P0 besteht das Structural-Recovery-Gate.
2. Mindestens eine rekonstruierte Pipeline P1/P2 unterscheidet sich reproduzierbar in Termsupport oder Koeffizientstruktur von P0 bzw. ihrer gepaarten Alternative.
3. Gleichzeitig bleibt diese Pipeline bezüglich des vorregistrierten dynamisch/statistischen Observable-Sets praktisch ähnlich genug, um keine triviale `bad model`-Erklärung zu erzwingen.
4. Der Effekt ist über die drei Mask-Seeds hinreichend konsistent.
5. Die relevante Differenz lässt sich einer konkreten inversen Kante zuordnen, etwa `C_pre -> C_infer`, und nicht nur allgemeinem numerischem Scheitern.

Ein **informativ negatives Ergebnis** liegt vor, wenn P0 valide ist, aber die Rekonstruktionsvarianten entweder strukturell stabil bleiben oder strukturelle Änderungen stets mit klarer dynamischer Degradation einhergehen.

Ein **inconclusive Ergebnis** liegt vor, wenn P0 die wahre Struktur nicht hinreichend rekonstruiert, die Rekonstruktionen technisch invalid sind oder die Bewertung durch numerische/reference Unsicherheit dominiert wird.

## 10. Directed-Trias-Audit für jeden Datenpfad

Für P0/P1/P2 wird dieselbe Provenance-Tabelle ausgefüllt:

```text
target system
observation operator
sampling
missingness mask
reconstruction method
derivative estimation
feature library
sparse optimizer / threshold
inferred equation structure
forward integrator used for validation
validated observables
scope of scientific interpretation
```

Zusätzlich wird explizit dokumentiert:

- welches Objekt an jeder Stufe vorliegt;
- welche Information verloren oder hinzugefügt wurde;
- welche Wahl den nächsten Schluss konditioniert;
- ob die Validierung structural fidelity oder nur dynamical adequacy stützt.

## 11. Minimaler Comparator-Test

Nach dem numerischen Resultat wird derselbe Fall mindestens in folgenden Sprachen beschrieben:

1. Standard System Identification / structural error;
2. structural/practical identifiability + observability, soweit begrifflich passend;
3. SciML V&V / credibility;
4. workflow/data provenance;
5. Directed Trias.

Die Trias gilt nur dann als methodologisch geschärft, wenn sie eine zusätzliche **Integrations- oder Zuordnungsleistung** demonstriert. Neue Fehlertypen sind nicht erforderlich und werden nicht behauptet.

## 12. Scope Freeze v0.1

Nicht Bestandteil:

- Three-body chaos;
- Neural Networks;
- ML-v0.2 Teacher-Provenance-Run;
- PINNs / Neural ODEs;
- große SINDy-Library-Sweeps;
- Hyperparameteroptimierung pro Pipeline;
- Measurement noise zusätzlich zur Missingness;
- mehrere Missingness-Raten;
- block missingness;
- alternative dynamische Systeme;
- full Koopman spectral analysis;
- experimentelle Daten.

## 13. Erfolgswert für das Gesamtprojekt

Der Demonstrator soll die Forward-/Inverse-Symmetrie des Projekts prüfen:

```text
Sundman:      formal T available  not=> operationally useful C
Solver case:  same T              not=> same operational profile C
Inverse case: similar observables not=> uniquely recovered T
```

Die dritte Zeile ist nur dann eigene Demonstratorevidenz, wenn die vorregistrierten Gates bestehen. Selbst dann folgt daraus keine Neuheit der Nichtidentifizierbarkeit; getestet wird die Integrationsleistung der Directed Trias.

## 14. Nächster Schritt nach Akzeptanz

Nach `GO` wird zunächst ein **Inverse-Direction Implementation Contract v0.1** erstellt. Dieser friert exakt ein:

- Lorenz-Anfangsbedingung und Zeitfenster;
- DOP853 reference/cross-check;
- Sampling und Missingness-Masken;
- lineare/kubische Rekonstruktion;
- Derivative Estimator;
- SINDy Library und Optimizerparameter;
- Structural- und Dynamical-Metriken;
- Äquivalenztoleranzen;
- Resultatklassen und Gates;
- erforderliche Artefakte.

Erst ein weiteres GO erlaubt Code/Experiment.

## Entscheidungsempfehlung

**ACCEPT.**

Der vorgeschlagene MVP ist klein genug, um die neue inverse Kante isoliert zu testen, hält den Zhai–Lucarini–Lai-Fall als Inspiration sichtbar, vermeidet aber eine unnötige Vollreplikation und hält den pausierten ML-v0.2-Zweig vollständig reversibel verfügbar.