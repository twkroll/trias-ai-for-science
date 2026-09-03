# Edge Semantics + Evidence Ledger v0.1

**Status:** PENDING REVIEW  
**Stand:** 2026-09-03  
**Depends on:** D024 / C08-D-R

## 1. Zweck

Dieses Dokument präzisiert die Descriptive Trias so weit, dass `R–T`, `T–C` und `C–R` nicht nur als intuitive Dreieckskanten, sondern als **claim- und evidenzgebundene epistemische Relationen** verwendet werden können.

Die Trias bleibt zunächst deskriptiv. Sie soll nicht automatisch entscheiden, welches Modell vorzuziehen ist. Sie soll explizit machen:

1. worüber ein wissenschaftlicher Claim handelt;
2. welche Relation durch die vorliegende Evidenz tatsächlich gestützt wird;
3. welche Relationen offen bleiben;
4. unter welchen zusätzlichen Bridge-Annahmen Evidenz über Kanten hinweg weiterverwendet werden darf.

Die Minimalstruktur lautet:

```text
R = intendiertes Zielsystem / Realität
T = theoretische, formale, mechanistische oder erklärende Repräsentation
C = konkrete computational realization
U = spezifizierter wissenschaftlicher Use Case
```

Ein Profil ist kein Dreier-Score, sondern ein Ledger von claimspezifischen Relationen.

---

## 2. Semantik der drei Rollen

### 2.1 R — Realität / intendiertes Zielsystem

`R` bezeichnet das System, relativ zu dem der wissenschaftliche Anspruch bewertet wird.

Zulässige Typen:

```text
R_real       reales empirisches Zielsystem
R_syn        explizit konstruiertes synthetisches Zielsystem
R_hybrid     empirisch kalibriertes/teilsynthetisches Ziel mit expliziter Konstruktion
```

Wichtig ist nicht, dass `R` theorieunabhängig existieren muss. Entscheidend ist, dass das Ziel **vor der Bewertung des Claims explizit fixiert** wird.

Beispiele:

```text
R_syn  = idealisierte Newtonsche Figure-eight-Dynamik
R_real = reales atmosphärisches System
R_real = experimenteller Materialprozess
R_syn  = PDE-Simulator als bewusstes Teacher-Target für einen Surrogat-Use-Case
```

Ein Wechsel von `R_syn` zu `R_real` erzeugt ein neues Profil, selbst wenn `T` und `C` unverändert bleiben.

### 2.2 T — Theorie

`T` bezeichnet den expliziten theoretischen Inhalt, über den ein wissenschaftlicher Claim gemacht wird.

Dazu können gehören:

```text
- Differentialgleichungen;
- mechanistische Modelle;
- Symmetrien / Erhaltungssätze;
- konstitutive Gesetze;
- formale Approximationen;
- erklärende Struktur;
- symbolisch inferierte Gleichungen, falls sie als Theorieclaim interpretiert werden.
```

Nicht jede Modellannahme oder jeder ML-Inductive-Bias wird automatisch zu `T`. Ein Bias zählt für die Trias nur dann als theoretische Repräsentation, wenn er Teil des wissenschaftlichen Theorieclaims ist.

Ein Black-box-Predictor kann daher für einen engen Prediction-Claim sinnvollerweise `T = absent/not claimed` haben.

### 2.3 C — computational realization

`C` bezeichnet die konkrete operative Berechnungsinstanz, nicht bloß abstrakt "Computer".

Dazu können gehören:

```text
- numerischer Integrator + Diskretisierung + Toleranzen;
- Implementierung einer analytischen Repräsentation;
- Optimierungs-/Inferenzpipeline;
- neuronales Netz einschließlich Training und Inferenz;
- Surrogat oder Emulator;
- Datenrekonstruktions-/Preprocessing-Pipeline, sofern sie Bestandteil der operativen Realisierung ist.
```

`C` ist damit eine konkrete wissenschaftliche Repräsentations- und Transformationspraxis.

---

## 3. Semantik der Kante R–T

### 3.1 Leitfrage

> In welchem Sinn ist die behauptete Theorie für das intendierte Zielsystem epistemisch adäquat?

### 3.2 Kernfacetten

Ein R–T-Eintrag muss mindestens eine Facette nennen. Zulässige Minimalfacetten sind:

```text
RT_EMPIRICAL       empirische Adäquanz der Theorie
RT_MECHANISTIC     mechanistische/kausale Repräsentation
RT_EXPLANATORY     erklärende Adäquanz
RT_SCOPE           Geltungsbereich / Idealisation / Regimeadäquanz
RT_STRUCTURAL      strukturelle Form der Theorie relativ zum Target
```

Weitere domänenspezifische Facetten sind zulässig, müssen aber explizit definiert werden.

### 3.3 Direkte Evidenztypen

Mögliche direkte oder zielgerichtete Evidenz für R–T:

```text
- Experiment-/Beobachtungsvergleich, dessen Claimobjekt explizit T ist;
- Parameter-/Strukturtests der Theorie gegen R;
- Interventions-/Mechanismusevidenz;
- Regime- und Idealisationstests;
- unabhängige empirische Bestätigung theoretisch spezifischer Vorhersagen.
```

### 3.4 Was R–T nicht automatisch etabliert

R–T wird nicht allein dadurch etabliert, dass:

```text
- ein numerischer Code stabil läuft;
- ein Surrogat seinen Teacher gut imitiert;
- ein Physics-Loss klein ist;
- ein Modell auf synthetischen Daten geringe RMSE besitzt;
- eine konkrete C-Ausgabe realistische Bilder/Trajektorien erzeugt, ohne dass der Theorieclaim isoliert wird.
```

---

## 4. Semantik der Kante T–C

### 4.1 Leitfrage

> In welchem Sinn ist die Theorie operativ realisierbar und in welchem Sinn repräsentiert die konkrete Berechnung die für den Claim relevante theoretische Struktur treu?

### 4.2 Kernfacetten

```text
TC_TRACTABILITY     praktische Berechenbarkeit / Ressourcenmachbarkeit
TC_FIDELITY         Implementierungs-/Approximationstreue zu T
TC_CONVERGENCE      numerische/algorithmische Konvergenz im relevanten Sinn
TC_STABILITY        numerische/algorithmische Stabilität
TC_STRUCTURE        Erhaltung relevanter theoretischer Struktur/Invarianten
TC_RESOLVABILITY    kann C die relevante theoretische Differenz überhaupt auflösen?
TC_SURROGATE        Teacher-/Simulator-Treue eines gelernten Surrogats
```

### 4.3 Direkte Evidenztypen

```text
- Refinement-/Convergence-Study;
- Code-/Solution-Verification;
- Fehlerabschätzungen gegenüber analytischer oder hochgenauer Referenz;
- Invariant-/Strukturtests;
- Laufzeit-/Speicher-/Ressourcenmessung relativ zum Use Case;
- Teacher-vs.-Surrogate-Held-out-Test;
- kontrollierter Approximations-/Diskretisierungsvergleich;
- Resolvability-Gates.
```

### 4.4 Wichtige Trennung innerhalb T–C

`theory is computable` und `this implementation faithfully realizes theory` sind nicht identisch.

Beispiel Sundman:

```text
TC_FIDELITY      kann formal hoch sein
TC_TRACTABILITY  kann praktisch schwach sein
```

Beispiel Figure-eight:

```text
TC_TRAJECTORY_FIDELITY   RK4 im getesteten U1 stärker
TC_STRUCTURE             Verlet im getesteten U2 bezüglich secular drift/Lz stärker
```

Damit ist auch innerhalb einer Kante kein globaler Status ohne Facet zulässig.

---

## 5. Semantik der Kante C–R

### 5.1 Leitfrage

> In welchem Sinn ist die konkrete computational realization oder ihr Output gegenüber dem intendierten Zielsystem empirisch bzw. repräsentational verankert?

### 5.2 Kernfacetten

```text
CR_PREDICTION       predictive adequacy auf realem/target-passendem Holdout
CR_CALIBRATION      probabilistische Kalibrierung
CR_DISTRIBUTION     statistische/verteilungsbezogene Adäquanz
CR_EXTERNAL         externe Gültigkeit / Transfer in neues Regime
CR_SIM2REAL         synthetisch/Simulator -> Realität
CR_ROBUSTNESS       Robustheit gegenüber target-relevanten Variationen
CR_REPRESENTATION   repräsentationale Adäquanz eines Outputs relativ zu R
```

### 5.3 Direkte Evidenztypen

```text
- held-out reale Beobachtungsdaten;
- externe Datensätze / neue Messregime;
- experimentelle Reproduktion;
- prospektive Prediction;
- sim-to-real Evaluation;
- target-spezifische calibration/coverage tests;
- reale Intervention oder deployment-nahe Validation.
```

### 5.4 Synthetische Targets

Bei `R = R_syn` kann C–R durchaus `ESTABLISHED` sein, aber der Claim ist dann ausschließlich relativ zu diesem synthetischen Target.

Beispiel:

```text
R = DOP853-defined synthetic teacher system
C = ML surrogate
```

Ein sehr guter Teacher-Holdout kann dann direkt `CR` relativ zu `R_syn` stützen.

Wenn der wissenschaftliche Claim jedoch ein reales System `R_real` betrifft, wird derselbe Test nicht automatisch zu `CR(R_real)`-Evidenz. Dann muss das Profil neu spezifiziert werden.

Diese Target-Relativität ist zentral, weil dieselbe numerische Metrik sonst unterschiedlich starke wissenschaftliche Aussagen zu tragen scheint.

---

## 6. Statussemantik

Jeder Ledger-Eintrag erhält genau einen evidenzbezogenen Status.

### ESTABLISHED

Zulässig, wenn:

1. die Relation/Facette für den Use Case klar definiert ist;
2. direkte oder über einen expliziten akzeptierten Bridge-Argumentpfad ausreichend spezifische Evidenz vorliegt;
3. die Evidenz im angegebenen Scope die Claimschwelle erfüllt;
4. kein offener kritischer Widerspruch die Claimstützung dominiert.

`ESTABLISHED` bedeutet **nicht wahr ohne Einschränkung**, sondern `innerhalb des angegebenen Use Case/Scopes durch die dokumentierte Evidenz hinreichend gestützt`.

### PARTIAL

Zulässig, wenn relevante positive Evidenz vorliegt, aber mindestens eine wesentliche Einschränkung besteht, z. B.:

```text
- nur Teilregime getestet;
- starke Idealisation;
- nur Teilmenge der relevanten Observablen;
- bekannte residuale Abweichung;
- Evidenz nur für eine Unterfacette;
- Transfer nur innerhalb enger Domain.
```

### UNCERTAIN

Zulässig, wenn die Relation relevant ist, aber der Evidenzstand keine stabile Zuordnung erlaubt, z. B.:

```text
- widersprüchliche Evidenz;
- sehr indirekte Evidenz;
- Identifiability-/Resolvability-Problem;
- Evidenzsignal kleiner als Methodenunsicherheit;
- wichtige ungetestete Bridge-Annahme.
```

### UNTESTED

Zulässig, wenn die Relation für den Claim relevant ist, aber keine ausreichend direkte Prüfung stattgefunden hat.

`UNTESTED` ist besonders wichtig für AI-for-Science, weil gute Teacher-/Synthetic-Performance häufig eine reale C–R-Frage schlicht offen lässt.

### NOT_APPLICABLE

Zulässig, wenn die Relation für den spezifizierten Claim tatsächlich nicht ausgebildet ist.

Beispiele:

```text
- reiner Black-box Prediction-Claim ohne explizite wissenschaftliche Theorie -> T-C kann N/A sein;
- ein enges mathematisches Benchmark-Ziel ohne empirischen Realitätsclaim -> bestimmte CR_real-Facetten N/A.
```

`NOT_APPLICABLE` bedeutet nicht `schlecht` und darf nicht in eine Rangfolge eingerechnet werden.

---

## 7. Nicht-Transitivität als Default

Die zentrale Default-Regel lautet:

```text
A_RT + A_TC  -/->  A_CR
A_TC + A_CR  -/->  A_RT
A_RT + A_CR  -/->  A_TC
```

Das Symbol `-/->` bedeutet: **keine automatische epistemische Übertragung ohne expliziten Bridge-Claim**.

Diese Regel behauptet keine logische Unmöglichkeit von Übertragung. Sie verbietet lediglich stillschweigenden Evidenztransfer.

### 7.1 Beispiel: Theorie + Implementierung -> Realität

Angenommen:

```text
R-T = gut gestützte Theorie im Regime U
T-C = numerisch treue Implementierung
```

Daraus kann C–R für bestimmte Observablen plausibel abgeleitet werden, aber nur wenn zusätzlich explizit festgelegt ist:

```text
- identisches Target/Regime;
- dieselben relevanten Observablen/QoIs;
- Fehler-/Approximationstransfer kontrolliert;
- keine zusätzliche nichtmodellierte C-Komponente;
- Scope der R-T-Evidenz deckt den C-Use-Case.
```

Ohne diese Bridge-Bedingungen bleibt C–R separat offen.

### 7.2 Beispiel: gute reale Prediction -> Theorie

```text
C-R = hohe Prediction auf realem Holdout
T-C = Modell implementiert/enkodiert eine Theorie
```

Dies kann Evidenz für `RT_EMPIRICAL` liefern, **aber nicht automatisch** für:

```text
RT_MECHANISTIC
RT_EXPLANATORY
RT_STRUCTURAL
```

Prediction darf also nicht ohne Facet-Wechsel zu mechanistischer Bestätigung werden.

### 7.3 Beispiel: synthetic surrogate

```text
T-C = Surrogat imitiert Simulator/Teacher hervorragend
```

Dies stützt nicht automatisch `C-R_real`.

Eine Bridge zu `R_real` benötigt mindestens eine separat gestützte Simulator-/Theorie-Realitätsbeziehung und einen Scope-kompatiblen Transferclaim.

---

## 8. Bridge-Claim-Schema

Jede erlaubte Übertragung zwischen Kanten muss im Ledger als eigener Eintrag erscheinen:

```text
bridge_id
source_edge
source_claim
source_evidence
target_edge
target_claim
bridge_premises
scope
status
```

Beispiel:

```text
bridge_id: B-SURR-01
source_edge: T-C
source_claim: surrogate reproduces simulator outputs within epsilon
source_evidence: held-out simulator test

target_edge: C-R_real
target_claim: surrogate predicts real target quantity within delta

bridge_premises:
- simulator is externally validated for this QoI/regime
- surrogate input domain is inside validated simulator domain
- epsilon is negligible relative to simulator-vs-reality error budget

status: UNTESTED until these premises are evidenced
```

Damit wird der epistemische Transfer selbst sichtbar, ohne dass die Trias behauptet, Bridge-Argumentation als solche neu erfunden zu haben.

---

## 9. Minimaler Evidence-Ledger-Datensatz

Jeder Eintrag muss mindestens folgende Felder besitzen:

| Feld | Bedeutung |
|---|---|
| `case_id` | eindeutiger Fall |
| `target_id` | explizites R |
| `target_type` | `REAL`, `SYNTHETIC`, `HYBRID` |
| `theory_id` | explizites T oder `NONE_CLAIMED` |
| `computation_id` | konkrete C-Realisierung |
| `use_case` | wissenschaftlicher Zweck |
| `edge` | `RT`, `TC`, `CR` |
| `facet` | z. B. `TC_TRACTABILITY`, `CR_PREDICTION` |
| `claim` | genau der zu stützende Satz |
| `evidence` | konkrete Evidenz/Artefakt/Analyse |
| `evidence_mode` | `DIRECT`, `BRIDGED`, `INDIRECT` |
| `status` | fünfstufige Statussprache |
| `scope` | Regime, Datenbereich, Genauigkeit, Population etc. |
| `dependencies` | notwendige Annahmen/andere Ledger-Einträge |
| `non_implications` | explizit nicht mitbegründete Nachbarclaims |

Empfohlene optionale Felder:

```text
uncertainty
acceptance_criterion
source_reference
provenance_pointer
bridge_id
review_note
```

---

## 10. Kanonische AI-for-Science-Beispiele

### 10.1 Gleiche RMSE, andere Kante

**Fall A — real-data predictor**

```text
claim: predicts measured target Y on representative real holdout
edge: CR
facet: CR_PREDICTION
evidence: held-out RMSE = 0.01
status: ESTABLISHED within holdout scope
```

**Fall B — synthetic surrogate**

```text
claim: reproduces simulator/teacher Y on held-out synthetic states
edge: TC (oder CR relativ zu explizit gesetztem R_syn)
facet: TC_SURROGATE
evidence: held-out RMSE = 0.01
status: ESTABLISHED relative to simulator
non_implication: no direct claim about C-R_real
```

Die Zahl ist identisch, der epistemische Claim nicht.

### 10.2 Physics-informed Modell

```text
claim 1: learned output satisfies PDE residual tolerance
edge: TC
facet: TC_STRUCTURE / TC_FIDELITY

claim 2: PDE is adequate for actual target regime
edge: RT
facet: RT_SCOPE / RT_EMPIRICAL

claim 3: model predicts real measurements in that regime
edge: CR
facet: CR_PREDICTION
```

Keiner dieser drei Claims darf sprachlich durch das einzelne Label `physics-informed` ersetzt werden.

### 10.3 Equation Discovery

```text
claim 1: inferred ODE reproduces selected long-time observables
edge: CR
facet: CR_DISTRIBUTION

claim 2: inferred symbolic terms identify the actual mechanistic structure
edge: RT
facet: RT_STRUCTURAL / RT_MECHANISTIC

claim 3: inference pipeline resolves the structural distinction of interest
edge: TC
facet: TC_RESOLVABILITY
```

Dynamische Adäquanz kann `claim 1` stützen, ohne `claim 2` automatisch zu etablieren.

---

## 11. Anwendung auf die bestehenden Projektfälle

### Sundman

```text
RT_STRUCTURAL: ESTABLISHED relativ zu R_syn/Newton-Scope
TC_FIDELITY:   ESTABLISHED/PARTIAL im formalen Sinn
TC_TRACTABILITY: PARTIAL/schwach für praktische Bahnberechnung
CR:            UNTESTED für den praktischen Sundman-Use-Case
```

Wichtig: Sundmans Reihe konvergiert; das Problem ist praktische Konvergenzgeschwindigkeit bzw. Evaluierbarkeit.

### Figure-eight

```text
RT: synthetisch by construction / scope-fixiert
TC_TRAJECTORY: RK4 im getesteten U1 stark
TC_STRUCTURE:  Verlet im getesteten U2 für bestimmte Invarianten/Drift stark
CR_real: N/A, solange kein reales astrophysikalisches Target beansprucht wird
```

Der Fall zeigt, dass Facetten nötig sind und ein einziges `A_TC` zu grob wäre.

### ML v0.1

```text
TC_RESOLVABILITY: nicht erfüllt
```

Deshalb konnte die geplante teacher-provenance-Frage nicht entschieden werden. Dies ist ein gutes Beispiel dafür, wie ein TC-Problem einen späteren wissenschaftlichen Claim blockiert, ohne ihn zu widerlegen.

### Inverser Lorenz/SINDy-Fall

```text
TC_RESOLVABILITY / baseline: erfüllt
RT_STRUCTURAL provenance effect: nicht seed-robust gezeigt
CR selected dynamical metrics: häufig gut
```

Der negative Run bleibt deshalb ein valides Beispiel für unterschiedliche Claimstatus auf unterschiedlichen Facetten.

---

## 12. Was die Trias hier leistet — und was nicht

### Leistet

Die Trias bietet eine minimale gemeinsame Topologie, die verlangt, Evidenz zunächst auf einen von drei Relationstypen zu beziehen und danach erst mögliche Bridge-Claims zu formulieren.

Insbesondere wird sichtbar:

```text
- welche Art von Erfolg vorliegt;
- relativ zu welchem Target;
- welche Theorie tatsächlich beansprucht wird;
- welche computational realization getestet wurde;
- welche Nachbarkante offen bleibt;
- ob ein Evidenztransfer explizite Zusatzprämissen benötigt.
```

### Leistet nicht automatisch

Die Trias liefert selbst keine neuen:

```text
- Fehlermetriken;
- Validierungsverfahren;
- Identifiability-Kriterien;
- Provenance-Standards;
- Assurance-Logiken;
- normativen Modellrankings.
```

Diese Werkzeuge liefern die konkrete Evidenz; die Trias typisiert, **wofür** sie Evidenz ist.

---

## 13. Falsifikations-/Redundanztest für die Profilgrammatik

Die Profilgrammatik verliert ihren Eigenwert, wenn ein einzelner bereits etablierter wissenschaftsphilosophischer Rahmen ohne zusätzliche projektspezifische Typisierung zugleich zuverlässig erfasst:

```text
1. Targettyp real/synthetisch;
2. Theorieclaim;
3. konkrete computational realization;
4. genau die drei Relationstypen RT/TC/CR;
5. Facet-/Use-/Evidence-/Scope-Bindung;
6. Default-Nichttransitivität von Evidenz;
7. explizite Bridge-Claims zwischen Relationen;
8. dieselbe Semantik über numerische Simulation und AI-for-Science hinweg.
```

Dieser Test muss vor einem finalen Originalitätsclaim literaturseitig erneut durchgeführt werden.

---

## 14. Ergebnis und nächster Schritt

Das Ledger präzisiert C08-D-R in eine implementierbare deskriptive Form:

```text
Trias topology
+
edge facet
+
claim
+
evidence
+
use case
+
scope
+
status
+
optional bridge claim
```

Damit wird der zentrale Satz des Projekts schärfer:

> Nicht jede erfolgreiche wissenschaftliche Berechnung ist auf dieselbe Weise erfolgreich. Die epistemische Bedeutung einer Evidenz hängt davon ab, welche Relation zwischen Zielsystem, Theorie und computational realization sie tatsächlich stützt.

### Empfehlung

**ACCEPT Edge Semantics + Evidence Ledger v0.1.**

Danach kein numerisches Experiment, sondern ein letzter gezielter `Relational-Profile Novelty Audit v0.1`, der genau die präzisierte Struktur — einschließlich Facets, Target-Typen und Bridge-Regeln — gegen die stärksten direkten Literaturkandidaten prüft. Erst danach sollte der Paper-Hauptclaim endgültig eingefroren werden.