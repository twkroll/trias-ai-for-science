# Descriptive Trias Profile Test v0.1

**Status:** COMPLETE / PENDING CLAIM DECISION  
**Stand:** 2026-09-03  
**Depends on:** D023, `theory/descriptive_trias_v0_1.md`, `literature/descriptive_trias_literature_stress_test_v0_1.md`

## 1. Ziel

Dieser Test prüft nicht, ob die Trias neue Einzelprobleme entdeckt. Er prüft ausschließlich, ob die feste relationale Beschreibung

```text
P(M;U) = [A_RT, A_TC, A_CR]
```

für unterschiedliche Computational-Science-/AI-for-Science-Fälle einen analytischen Unterschied sichtbar macht, der durch grobe Labels wie `accurate`, `validated`, `physics-informed`, `interpretable` oder `good model` leicht verdeckt wird.

Dabei gilt:

```text
R = intendiertes Zielsystem / Realität
T = theoretische, formale oder mechanistische Repräsentation
C = computational realization / gelernte oder numerische Realisierung
U = konkret spezifizierter wissenschaftlicher Gebrauch
```

## 2. Statussprache

Die Kanten erhalten keine numerischen Scores. Verwendet werden nur evidenzbezogene Statusangaben:

```text
ESTABLISHED      direkte, use-case-passende Evidenz liegt vor
PARTIAL          relevante Evidenz liegt vor, aber mit klarer Scope-/Idealiserungsgrenze
UNCERTAIN        die Relation ist wissenschaftlich relevant, aber nicht ausreichend entschieden
UNTESTED         die Relation wurde für den betrachteten Use Case nicht direkt geprüft
NOT_APPLICABLE   die Relation ist im spezifizierten Fall/Claim nicht ausgebildet
```

Wichtig: Diese Status sind **claim- und use-case-relativ**, nicht intrinsische Eigenschaften eines Modells.

## 3. Fall 1 — Sundman / Drei-Körper-Problem

### Spezifizierter Fall

```text
R = synthetisches Newtonsches Drei-Körper-Zielsystem
T = Sundmans regulierte konvergente Reihenrepräsentation
C = praktische Evaluation dieser Repräsentation
U = konkrete Bahnberechnung mit praktisch erreichbarer Genauigkeit
```

### Profil

```text
A_RT = ESTABLISHED* 
A_TC = PARTIAL
A_CR = UNTESTED / praktisch kaum zugänglich über genau diese Repräsentation
```

`*` Das `ESTABLISHED` gilt hier nur relativ zum synthetischen Newtonschen Zielsystem, dessen Dynamik durch die Theorie konstituiert ist. Für ein reales astrophysikalisches Zielsystem wäre `A_RT` wegen Idealisationen enger zu bewerten.

### Analytischer Gewinn

Das grobe Label `analytisch gelöst` verdeckt, dass der relevante Engpass nicht auf `R–T`, sondern auf `T–C` liegt. Die konvergente Darstellung ist formal verfügbar, aber praktisch extrem ineffizient evaluierbar.

Der Fall zeigt außerdem: Der Target-Begriff ist konstitutiv für das Profil. Ein Wechsel von `synthetisches Newton-Ziel` zu `reales Himmelskörpersystem` ändert vor allem `A_RT`, ohne die mathematische Sundman-Repräsentation zu ändern.

## 4. Fall 2 — Figure-eight / numerische Solver

### Spezifizierter Fall

```text
R = synthetisches Newtonsches Figure-eight-Zielsystem
T = Newtonsche Drei-Körper-Gleichungen
C = RK4 bzw. Velocity-Verlet
U1 = kurzfristige Trajektorienrekonstruktion
U2 = langfristige Strukturerhaltung
```

### Profil auf grober Kantenebene

Für beide Solver:

```text
A_RT = ESTABLISHED*      (synthetisches Target)
A_TC = ESTABLISHED/PARTIAL abhängig vom Use Case und der verlangten Struktur
A_CR = PARTIAL           numerisch stark gegen Referenz kontrolliert, aber keine unabhängige physische Realität
```

### Wichtige Subprofil-Differenz

Die Full-Run-Evidenz zeigt:

- RK4 ist im getesteten Bereich deutlich trajectory-genauer;
- Velocity-Verlet hat viel kleineren fitted secular energy drift und Drehimpulserhaltung nahe Rundungsniveau.

Das heißt: Selbst **innerhalb einer Kante** ist `A_TC` nicht eindimensional. Für `U1` ist die relevante Treue anders als für `U2`.

### Analytischer Gewinn

Das Profil verhindert zwei Verkürzungen:

1. `same theory + accurate computation = globally best model`;
2. `synthetic validation = independent reality validation`.

Gleichzeitig deckt dieser Fall eine Schwäche der v0.1-Trias auf: Jede Kante braucht mindestens eine **Facet-/Use-Case-Spezifikation**, sonst wird ein Status wie `ESTABLISHED` zu grob.

## 5. Fall 3 — Black-box ML auf realen Daten

### Archetyp

```text
R = reales Zielsystem
T = keine explizite mechanistische Theorie im Modell
C = datengetriebener Black-box Predictor
U = Vorhersage einer klar definierten realen Zielgröße auf repräsentativen Held-out-Daten
```

### Mögliches Profil bei tatsächlich guter externer Prediction

```text
A_RT = NOT_APPLICABLE / UNTESTED bezüglich mechanistischer Theorie
A_TC = NOT_APPLICABLE bezüglich Implementierung einer expliziten Theorie
A_CR = ESTABLISHED für den engen Prediction-Use-Case
```

### Analytischer Gewinn

Das Modell kann wissenschaftlich erfolgreich sein, ohne theoretisches Verständnis zu liefern. Das Profil sagt nicht `schlecht`, sondern präzisiert die Art des Erfolgs:

```text
prediction-grounded success != theory-grounded success
```

Das grobe Label `highly accurate AI model` unterscheidet diese beiden Aussagen nicht.

## 6. Fall 4 — ML-Surrogat auf synthetischen Daten

### Archetyp

```text
R = intendiertes reales physisches Zielsystem
T = physikalisches/theoretisches Simulationsmodell
C = ML-Surrogat, trainiert ausschließlich auf Simulatorlabels
U = schnelle Approximation des Simulators; optional wissenschaftliche Aussage über R
```

### Profil bei sehr guter Teacher-Imitation, aber ohne Real-World-Validation

```text
A_RT = PARTIAL oder UNCERTAIN   abhängig von der Validierung des Simulators gegenüber R
A_TC = ESTABLISHED              relativ zum Simulator/Teacher
A_CR = UNTESTED                 wenn das Surrogat nicht gegen R validiert wurde
```

### Analytischer Gewinn

Dies ist der zentrale AI-for-Science-Fall der ursprünglichen Autorenintuition. Zwei Systeme können beide als `excellent ML surrogate` bezeichnet werden, obwohl nur eines zusätzlich realweltlich validiert wurde.

Trias unterscheidet dann:

```text
Surrogat A: [PARTIAL, ESTABLISHED, UNTESTED]
Surrogat B: [PARTIAL, ESTABLISHED, ESTABLISHED/PARTIAL]
```

Die Teacher-Güte allein ist also eindeutig auf `T–C` lokalisiert und darf nicht stillschweigend zu `C–R` umgedeutet werden.

## 7. Fall 5 — Physics-informed ML

### Archetyp

```text
R = reales Zielsystem
T = bekannte oder angenommene physikalische Gleichungen/Constraints
C = physics-informed learned model
U = Prediction oder Rekonstruktion im physikalischen Zielregime
```

### Mögliches Profil bei gut erfülltem Physics-Loss, aber begrenzter externer Validation

```text
A_RT = PARTIAL       die eingebettete Theorie kann idealisiert oder regimebegrenzt sein
A_TC = PARTIAL/ESTABLISHED relativ zu den implementierten Constraints
A_CR = UNTESTED/PARTIAL abhängig von realer Validation
```

### Analytischer Gewinn

Das Label `physics-informed` beschreibt primär eine Beziehung zwischen `T` und `C`. Es garantiert weder, dass `T` das reale Regime adäquat beschreibt, noch dass der resultierende `C`-Output realweltlich validiert ist.

Damit trennt die Trias drei Fragen, die im allgemeinen Sprachgebrauch leicht zusammenfallen:

```text
Ist Physik eingebaut?          -> T-C
Ist diese Physik passend?      -> R-T
Funktioniert das Modell real?  -> C-R
```

## 8. Fall 6 — Equation Discovery

### Archetyp

```text
R = beobachtetes dynamisches Zielsystem
T = inferierte symbolische Gleichungsstruktur
C = Observation-/Reconstruction-/Inference-/Forward-Pipeline
U1 = dynamisch/statistische Reproduktion
U2 = mechanistische/strukturelle Theorieidentifikation
```

### Typisches Profil eines Zhai-artigen Falls

Bei guter dynamischer Reproduktion, aber pipelineabhängiger Gleichungsstruktur:

```text
A_RT = UNCERTAIN/PARTIAL bezüglich mechanistischer Struktur
A_TC = ESTABLISHED/PARTIAL bezüglich operativer Inferenz und Forward-Realisierung
A_CR = ESTABLISHED/PARTIAL für ausgewählte dynamische/statistische Observablen
```

### Eigener Projektfall

Der vorregistrierte Lorenz/SINDy-Minimalfall erzeugte den strukturell-anderen-aber-dynamisch-ähnlichen Effekt **nicht seed-robust** (`linear 1/3`, `cubic 0/3`). Das verhindert, diesen Archetyp aus unserem eigenen Run als robusten positiven Befund zu verkaufen.

### Analytischer Gewinn

Die Trias zwingt dazu, `dynamically adequate` nicht automatisch mit `theoretically identified` gleichzusetzen. Der Einzelgedanke ist aus Identifiability-/System-ID-Literatur bekannt; der Profiltest prüft nur seine strukturelle Vergleichbarkeit mit den fünf anderen Fällen.

## 9. Gemeinsame Profilmatrix

| Fall | A_RT | A_TC | A_CR | grobes Erfolgslabel, das Information verlieren kann |
|---|---|---|---|---|
| Sundman / synthetisches Newton-Target | ESTABLISHED* | PARTIAL | UNTESTED über Sundman-Evaluation | `analytisch gelöst` |
| Figure-eight Solver | ESTABLISHED* | ESTABLISHED/PARTIAL use-case-relativ | PARTIAL | `numerisch genau` |
| Black-box ML, reale Daten | N/A/UNTESTED | N/A | ESTABLISHED für Prediction | `high accuracy AI` |
| synthetisch trainiertes ML-Surrogat | PARTIAL/UNCERTAIN | ESTABLISHED | UNTESTED | `excellent surrogate` |
| Physics-informed ML | PARTIAL | PARTIAL/ESTABLISHED | UNTESTED/PARTIAL | `physics-informed` |
| Equation Discovery | UNCERTAIN/PARTIAL | ESTABLISHED/PARTIAL | ESTABLISHED/PARTIAL für ausgewählte QoIs | `discovered governing equations` |

Die Profile sind nicht als Rangfolge zu lesen.

## 10. Discrimination Test A — gleiche globale Güte, anderes Profil

### Black-box Real-Data Predictor vs synthetisches Surrogat

Beide können nahezu identische Test-RMSE-Werte berichten. Trotzdem ist die Evidenz semantisch verschieden:

```text
real-data predictor:
RMSE -> direktes Evidenzstück für A_CR

synthetic surrogate:
RMSE -> primär Evidenzstück für A_TC
```

Ohne Angabe der Relation ist `RMSE = 0.01` epistemisch unterbestimmt.

**Resultat:** PASS — das Profil unterscheidet Fälle, die eine globale Accuracy-Sprache zusammenwerfen kann.

## 11. Discrimination Test B — gleicher Methodenname, anderes Profil

Zwei `physics-informed` Modelle können denselben Physics-Loss erfüllen. Modell 1 kann zusätzlich gegen reale Daten validiert sein, Modell 2 nicht.

```text
Modell 1: [PARTIAL, ESTABLISHED, PARTIAL/ESTABLISHED]
Modell 2: [PARTIAL, ESTABLISHED, UNTESTED]
```

Das Label `physics-informed` allein ist deshalb kein vollständiges epistemisches Profil.

**Resultat:** PASS.

## 12. Discrimination Test C — gleiche Theorie, andere Berechnung

Figure-eight zeigt bei identischem `R` und `T` unterschiedliche `C`-Profile. Die relevante Differenz liegt nicht in theoretischer Wahrheit, sondern in der Operationalisierung und im Use Case.

**Resultat:** PASS, aber bestehende Numerical Analysis erklärt den Einzelfall bereits vollständig.

## 13. Discrimination Test D — gleiche Berechnungsgüte, andere Target-Aussage

Ein Surrogat kann den Simulator hervorragend approximieren. Wenn der Simulator nur ein synthetisches Zielsystem ist, ist `A_TC` stark; wenn das wissenschaftliche Claim-Ziel jedoch die reale Welt ist, bleibt `A_CR` separat zu etablieren.

**Resultat:** PASS. Dieser Test trifft die ursprüngliche Autorenintuition besonders direkt.

## 14. Discrimination Test E — Target-Wechsel ändert das Profil

Dasselbe mathematische Modell kann relativ zu einem synthetischen Target und relativ zu einem realen Target verschiedene `A_RT`-/`A_CR`-Status besitzen.

Beispiel:

```text
Newtonian figure-eight as synthetic target:
A_RT = established by construction

real astrophysical three-body system:
A_RT = at best partial because omitted physics/measurement context matter
```

**Resultat:** PASS. Das Profil macht explizit, dass `target` keine austauschbare Hintergrundvariable ist.

## 15. Wichtigste Schwäche des Profilansatzes

Der Test deckt zugleich eine zentrale Gefahr auf: Die drei Kanten sind **keine Skalare**.

`A_RT` kann beispielsweise enthalten:

```text
empirical adequacy
mechanistic fidelity
explanatory adequacy
scope of idealization
```

`A_TC` kann enthalten:

```text
computational tractability
numerical convergence
implementation fidelity
stability
resource feasibility
```

`A_CR` kann enthalten:

```text
prediction
external validation
calibration
sim-to-real transfer
out-of-distribution validity
```

Ein einzelner Status ohne Facet und Use Case kann deshalb selbst wieder irreführend werden.

Die robuste Minimalform ist daher nicht

```text
A_RT = 0.8
```

sondern eher

```text
A_RT(U, facet, evidence) = STATUS
```

oder als Ledger:

```text
edge | scientific claim/facet | evidence | status | scope
```

Die Dreiecksstruktur bleibt dabei die Topologie, nicht die vollständige Semantik.

## 16. Ergebnis des Profile Tests

### Was der Test positiv zeigt

Die feste R/T/C-Profilstruktur leistet in den sechs Fällen eine echte **deskriptive Dekomposition**:

1. Sie lokalisiert denselben Metriktyp je nach Datenquelle auf unterschiedliche epistemische Relationen.
2. Sie unterscheidet hohe Prediction von theoretischer Adäquanz, ohne Prediction abzuwerten.
3. Sie unterscheidet Simulator-/Teacher-Treue von Realitätsgrounding.
4. Sie zeigt, dass `physics-informed` primär eine T-C-Aussage ist, solange R-T und C-R nicht separat belegt sind.
5. Sie macht den intendierten Target-Wechsel selbst zu einer expliziten Profiländerung.
6. Sie verbindet diese AI-Fälle mit Sundman und numerischer Operationalisierung, ohne zu behaupten, deren Einzelprobleme neu zu entdecken.

### Was der Test nicht zeigt

Nicht gezeigt sind:

- empirische Überlegenheit gegenüber V&V, adequacy-for-purpose oder Assurance Cases;
- dass Wissenschaftler ohne Trias systematisch falsche Entscheidungen treffen;
- dass die drei Kanten unabhängig sind;
- dass ein universeller Trade-off besteht;
- dass jede wissenschaftliche Praxis sinnvoll alle drei Kanten besitzt;
- dass die exakte Profilstruktur in der gesamten Literatur originär ist.

## 17. Claim-Empfehlung

Der ursprüngliche C08-D ist inhaltlich nahe am Ergebnis, sollte aber präzisiert werden.

### Kandidat C08-D-R — noch NICHT akzeptiert

> **C08-D-R:** In Computational Science und AI for Science kann der Evidenzstatus eines Modells deskriptiv in drei relationsspezifische Bereiche zerlegt werden: Zielsystem–Theorie (`R–T`), Theorie–computational realization (`T–C`) und computational realization–Zielsystem (`C–R`). Dieselbe globale Erfolgsbezeichnung oder Performancemetrik kann je nach wissenschaftlichem Workflow Evidenz für unterschiedliche dieser Relationen darstellen; Evidenz auf einer Relation etabliert die anderen daher nicht automatisch. Ein relationales Profil macht diese Differenz explizit, sofern jeder Kantenstatus an einen konkreten wissenschaftlichen Claim/Facet, einen Use Case, Evidenz und Scope gebunden wird. Der beanspruchte Beitrag ist diese gemeinsame deskriptive Profilgrammatik, nicht ein neuer Fehlertyp, eine notwendige Trade-off-Theorie oder eine normative Rangordnung von Modellen.

### Evidenzstatus

```text
analytische Diskriminationsleistung in sechs Falltypen: POSITIVE
praktische Nutzer-/Entscheidungsnützlichkeit: UNTESTED
starker Novelty-Nachweis: UNVERIFIED
notwendige Trade-off-Struktur: NOT CLAIMED
```

## 18. Empfohlener nächster Schritt

**ACCEPT C08-D-R als Working Claim, nicht als finalen Originalitätsclaim.**

Danach sollte kein neues numerisches Experiment folgen. Die nächste Abhängigkeit ist ein `Edge Semantics + Evidence Ledger v0.1`, das für jede Kante exakt festlegt:

```text
1. zulässige Claim-/Facet-Typen;
2. welche Evidenz einen Status begründen kann;
3. wie UNTESTED von UNCERTAIN und NOT_APPLICABLE getrennt wird;
4. wie synthetische und reale Targets unterschieden werden;
5. wie ein Modell mehrere use-case-spezifische Profile besitzen kann.
```

Erst danach sollte der neue Paper-Hauptclaim gegen die Literatur erneut final geprüft werden.