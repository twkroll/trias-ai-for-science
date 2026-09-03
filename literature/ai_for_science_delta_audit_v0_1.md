# AI-for-Science Delta Audit v0.1

**Status:** COMPLETE / PENDING CLAIM DECISION  
**Stand:** 2026-09-03  
**Depends on:** D027, C08-D-R2, `paper/paper_contribution_boundary_v0_2.md`

## 1. Prüfgegenstand

Dieser Audit prüft ausschließlich den nach D026/D027 verbleibenden Delta gegenüber der klassischen Model-Credibility-Genealogie. Nicht erneut geprüft werden die bereits verworfenen Neuheitsclaims zur Dreieckstopologie, Verification/Validation, intended use, sim-to-real oder Prediction-vs.-Understanding als Einzelproblem.

Zu prüfen sind vier Rollenveränderungen:

```text
A. T = NONE_CLAIMED
B. T = INFERRED_BY_C
C. layered synthetic surrogate pipelines
D. hybrid physics/theory + learned C
```

Die harte Frage lautet:

> Existiert bereits ein einzelner etablierter wissenschaftsphilosophischer/Credibility-Rahmen, der diese vier Rollenformen gemeinsam mit target-relativer Evidenz als Generalisierung der klassischen Reality–Conceptual Model–Computerized Model-Triade organisiert?

---

## 2. Delta A — T = NONE_CLAIMED / Prediction ohne expliziten Theorieclaim

### Starke Vorarbeit

Die Philosophie und Methodologie von ML in der Wissenschaft unterscheidet längst verschiedene epistemische Funktionen von ML. Naser (2025) organisiert ML explizit über `Prediction, Explanation, Discovery, Understanding, Decision-making (P.E.D.U.D.)` und behandelt Black-box Prediction als legitimen epistemischen Erfolg, der nicht mit Erklärung/Understanding identisch ist.

Auch neuere Philosophy-of-ML-/Scientific-Discovery-Literatur diskutiert, dass hochperformante neuronale Modelle wissenschaftlich nützlich sein können, ohne einen mechanistisch interpretierbaren Theorieoutput zu liefern.

Vinuesa et al. (Communications Physics, 2026) organisieren ML-Anwendungen sogar nach dem Grad vorhandener theoretischer Kenntnis: wenig/keine bekannte governing equations, partielle Kenntnis, weitgehend bekannte Gleichungen. Bei geringer Theoriekenntnis übernimmt ML primär Representation Learning, Pattern Discovery und ähnliche datengetriebene Rollen.

### Urteil

**FAIL als Einzelneuheit.**

Die Idee, dass `C` wissenschaftlich nützlich sein kann, obwohl kein expliziter mechanistischer `T`-Claim vorliegt, ist klar etabliert.

### Verbleibender Delta

Weniger etabliert ist lediglich die explizite Eintragung dieses Falls in die genealogisch von Model Credibility abgeleitete Rollenstruktur als

```text
T = NONE_CLAIMED
C-R prediction claim = evaluierbar
T-bezogene Kanten = claimabhängig N/A / UNTESTED
```

Das ist Notation/Synthese, nicht neue epistemologische Entdeckung.

---

## 3. Delta B — T = INFERRED_BY_C / Equation Discovery

### Starke Vorarbeit

Automated Scientific Discovery und Equation Discovery behandeln seit Jahrzehnten genau den Fall, dass ein computational system aus Daten wissenschaftliche Gesetze oder Gleichungen erzeugt.

Kramer et al. (Machine Learning, 2026) beschreiben ausdrücklich ein Spektrum von Equation Discovery/Symbolic Regression bis zu autonomen Discovery-Systemen. Ziel vieler Equation-Discovery-Verfahren ist ein human-understandable scientific model in Form von Gleichungen. Neural networks können dabei Suche/Representation unterstützen; Neural Operators können stattdessen direkt Dynamik lernen und Interpretierbarkeit aufgeben.

Damit ist die Rollenform

```text
R / observations -> C_inference -> T_hat
```

als wissenschaftliche Praxis vollständig etabliert.

### Urteil

**FAIL als Einzelneuheit.**

Dass computation Theorie/Modelle erzeugen kann, ist keine neue Trias-Beobachtung.

### Verbleibender Delta

Der klassische Sargent-artige Credibility-Lifecycle nimmt typischerweise ein conceptual model als Input für die computerized implementation. Equation-Discovery-Literatur behandelt dagegen `T` als Output, nutzt aber nicht notwendigerweise dieselbe dreikantige Credibility-/Evidence-Topologie. Die Trias kann diese Literaturen verbinden, nicht die inverse Rollenform erfinden.

---

## 4. Delta C — Layered synthetic surrogate pipelines

### Starke Vorarbeit

SciML-, surrogate-/metamodel- und reduced-order-model-Literatur behandelt ausdrücklich mehrstufige Ketten, in denen numerische Simulationen synthetische Trainingsdaten erzeugen und ML-Modelle diese Simulatoren approximieren oder beschleunigen.

Jakeman et al. (2026) passen klassische V&V-Prinzipien an predictive SciML an und fordern u. a. model purpose, prior knowledge, model structure, code/solution verification, purpose-specific validation, Datencharakteristika/-verarbeitung, uncertainty und interpolation/extrapolation scope. Validation richtet sich auf den physischen Target-Use-Case; reine interne Modell-/Benchmarkgüte ersetzt diesen Schritt nicht.

Vinuesa et al. (2026) beschreiben bei weitgehend bekannten governing equations synthetisch erzeugte Datensätze und ML-Surrogate/ROMs als typische Rollen von ML.

### Urteil

**FAIL als Einzelneuheit / STRONGLY PRECEDED.**

Die Kette

```text
T -> simulator C1 -> D_syn -> learned C2
```

und die Notwendigkeit, Simulator-/Teacher-Treue von Realitätsvalidierung zu unterscheiden, sind etablierte SciML-/Credibility-Themen.

### Verbleibender Delta

Die Trias macht den Referentenwechsel als expliziten epistemischen Profilwechsel sichtbar:

```text
C2-R_syn claim != C2-R_real claim
```

aber diese explizite Typisierung ist eine Synthese etablierter Credibility- und ML-Provenance-Ideen.

---

## 5. Delta D — Hybrid physics/theory + learned C

### Starke Vorarbeit

Physics-informed / physics-guided / theory-guided ML ist ein großes etabliertes Feld. Karniadakis et al. (2021) und neuere Surveys beschreiben die Integration mathematischer Physikmodelle und Daten in learned models, einschließlich Forward- und Inverse-Problemen.

Vinuesa et al. (2026) ordnen ML-Rollen explizit nach vollständiger, partieller oder geringer theoretischer Kenntnis. Bei partieller Kenntnis werden physical constraints, effective theories, generative models, constitutive-law learning und hypothesis generation kombiniert.

### Urteil

**FAIL als Einzelneuheit.**

Dass `T` und `C` hybridisiert bzw. gemeinsam operationalisiert werden können, ist klar etablierte SciML-Praxis.

### Verbleibender Delta

Die Trias kann lediglich unterscheiden:

```text
T-C: wurde die angenommene Physik/Constraint tatsächlich implementiert?
R-T: ist diese Physik für das Target-Regime adäquat?
C-R: funktioniert das resultierende learned model am Target?
```

Diese Trennung ist analytisch nützlich, aber stark mit V&V/Credibility kompatibel.

---

## 6. Härtester neuer Comparator — Vinuesa et al. 2026

Der stärkste neue Druck auf den verbliebenen P2-Delta kommt von:

**Vinuesa et al., “Decoding complexity through machine learning is redefining scientific discovery”, Communications Physics 9, 168 (2026).**

Die Arbeit verwendet einen konzeptionellen Rahmen, in dem ML-Rollen explizit vom Grad theoretischen Vorwissens abhängen:

```text
limited/no governing-equation knowledge
partial knowledge
governing equations well established
```

und ordnet diesen Regimen unterschiedliche ML-Funktionen zu:

```text
representation/pattern discovery
hybrid/physics-constrained/effective-law learning
surrogation/control/acceleration
```

Sie behandelt außerdem AI-basierte Hypothesen-/Gesetzesgenerierung und unterschiedliche Formen wissenschaftlichen Verständnisses.

### Konsequenz

Eine starke Aussage wie

> “Erst die Trias zeigt, dass die Rolle von computation davon abhängt, ob Theorie vorhanden, partiell oder fehlend ist.”

ist **nicht haltbar**.

Die verbleibende Trias-Differenz ist enger: nicht die Klassifikation nach Theory Availability, sondern deren Einbettung in eine aus Model Credibility genealogisch abgeleitete **claim-relative Evidence-Relation-Topologie**.

---

## 7. Härtester epistemischer Comparator — P.E.D.U.D.

Naser (Technology in Society, 2025) behandelt ML über fünf epistemische Funktionen:

```text
Prediction
Explanation
Discovery
Understanding
Decision-making
```

und betont explizit, dass verschiedene Anwendungen unterschiedliche epistemische Ziele priorisieren.

### Konsequenz

Auch der Satz

> “AI kann auf verschiedene Arten wissenschaftlich erfolgreich sein.”

ist als Grundidee **nicht neu**.

Die Trias darf daher nicht beanspruchen, die Pluralität wissenschaftlicher Erfolgsarten entdeckt zu haben.

Ihr möglicher Delta ist nur die Frage:

> Auf welche Relation zwischen Target, Theory-Claim und computational practice bezieht sich die konkrete Evidenz für diesen epistemischen Erfolg?

---

## 8. Gesamtvergleich: Gibt es einen einzelnen direkten Isomorph?

Im Audit wurde **kein einzelner etablierter Rahmen identifiziert**, der zugleich alle folgenden Elemente explizit kombiniert:

```text
1. genealogische Reality / Conceptual Model / Computerized Model-Triade;
2. T als claim-typisierte wissenschaftliche Theorie-/Mechanismus-/Erklärungsrolle;
3. T kann NONE_CLAIMED sein;
4. T kann Output von computational inference sein;
5. C kann Forward-Implementierung, learned predictor, surrogate oder inference sein;
6. REAL/SYNTHETIC/HYBRID referent typing;
7. Evidence wird einer RT/TC/CR-Relation + Claim/Facet/Use/Scope zugeordnet;
8. epistemischer Transfer zwischen Relationen wird nicht stillschweigend vorausgesetzt;
9. dieselbe Sprache deckt klassische Simulation, predictive ML, PIML und Equation Discovery ab.
```

Dieser Befund ist **kein Beweis einzigartiger Originalität**. Die Einzelbestandteile sind durch mehrere Literaturen sehr stark vorweggenommen. Die Distinktheit liegt höchstens in ihrer gemeinsamen genealogischen Komposition.

---

## 9. Delta-Matrix

| Kandidat | Stärkster Comparator | Urteil |
|---|---|---|
| C ohne expliziten T-Claim | Philosophy of ML; P.E.D.U.D.; Vinuesa et al. | **PRECEDED** |
| T wird von C inferiert | Equation Discovery / Automated Scientific Discovery | **PRECEDED** |
| Synthetic simulator -> surrogate | SciML / metamodel / V&V | **PRECEDED** |
| Physics/theory + learned C | PIML/SciML | **PRECEDED** |
| ML-Rolle hängt vom Grad theoretischer Kenntnis ab | Vinuesa et al. 2026 | **STRONGLY PRECEDED** |
| verschiedene epistemische ML-Erfolge | P.E.D.U.D. 2025 + Philosophy of ML | **PRECEDED** |
| alle Fälle in klassischer Credibility-Genealogie als claim-relative Edge-Evidence-Profile | kein einzelner Direktanalog im Audit | **POTENTIAL SYNTHESIS DELTA** |

---

## 10. Ergebnis

Der AI-for-Science Delta Audit schwächt P2 weiter, verwirft ihn aber nicht vollständig.

### Verworfen als Neuheit

```text
- prediction without theory
- AI-generated theory/equations
- layered surrogate pipelines
- physics-informed hybridization
- role variation with amount of prior theory
- plurality of epistemic success (prediction/explanation/discovery/etc.)
```

### Verbleibender Kandidat

Nur folgende Fassung überlebt:

> Die Descriptive Trias ist eine genealogisch transparente **Synthese**, die die klassische Model-Credibility-Relationstopologie mit AI-for-Science-Literaturen über unterschiedliche Theorieverfügbarkeit, predictive vs explanatory/discovery goals, surrogate learning und computational theory inference verbindet. Ihr spezifischer analytischer Vorschlag ist, diese Fälle in einer gemeinsamen claim-relativen Rollen- und Evidenzgrammatik zu lesen: Nicht die AI-Rollen oder epistemischen Ziele selbst sind neu, sondern ihre systematische Zuordnung zu Target–Theory, Theory–Computation und Computation–Target bei dynamisch besetzten Rollen.

Der Originalitätsstatus dieser Komposition ist **moderate / plausible synthesis originality**, nicht `new framework/theory` im starken Sinn.

---

## 11. Vorgeschlagener Claim C08-D-R3 — noch NICHT akzeptiert

> **C08-D-R3:** Die Descriptive Trias beansprucht weder die klassische Reality–Conceptual Model–Computerized Model-Topologie noch AI-spezifische Rollen wie Prediction ohne Theorie, Equation Discovery, Surrogate Learning oder Physics-informed Hybridisierung als neue Einzelideen. Ihr möglicher Beitrag ist eine genealogische wissenschaftsphilosophische Synthese: Die klassische Model-Credibility-Triade wird als claim-relative Rollenstruktur gelesen, in der `T` vorhanden, partiell, nicht beansprucht oder computational inferiert sein kann und `C` unterschiedliche numerische, gelernte oder inferierende Praktiken besetzen kann. Die zugehörige Evidenz wird danach profiliert, ob sie einen Target–Theory-, Theory–Computation- oder Computation–Target-Claim im angegebenen Use Case und Scope stützt. Dadurch werden etablierte AI-for-Science-Erfolgsarten in einer gemeinsamen Credibility-Genealogie vergleichbar, ohne sie als globale Modellgüte oder neue V&V-Kategorien zu behandeln.

### Evidenzstatus

```text
individual AI-role novelty: REJECTED
plural epistemic-success novelty: REJECTED
common relation/evidence profiling: analytically positive in project cases
genealogical synthesis originality: PLAUSIBLE / MODERATE
single direct analogue: NOT FOUND IN v0.1 AUDIT
practical superiority: UNTESTED
```

---

## 12. Literaturanker

- Schlesinger et al. (1979), *Terminology for model credibility*, Simulation 32(3), 103–104.
- Sargent, *Verification and Validation of Simulation Models* (multiple editions/reviews).
- Karniadakis et al. (2021), *Physics-informed machine learning*, Nature Reviews Physics 3, 422–440.
- Naser (2025), *A decision architecture for epistemic prioritization: Machine learning at the intersection of technology and society*, Technology in Society 83, 103039.
- Kramer et al. (2026), *Automated Scientific Discovery: From Equation Discovery to Autonomous Discovery Systems*, Machine Learning 115, 109.
- Vinuesa et al. (2026), *Decoding complexity through machine learning is redefining scientific discovery*, Communications Physics 9, 168.
- Jakeman et al. (2026), *Verification and validation for trustworthy scientific machine learning*, Machine Learning: Science and Technology 7, 025055.

---

## 13. Empfehlung

**Akzeptiere den Delta Audit und ersetze C08-D-R2 durch C08-D-R3 als Working Claim.**

Danach keine weitere Novelty-Suche in immer engeren Formulierungen. Der nächste Schritt sollte ein finaler `Paper Claim + Outline Freeze v0.3` sein, der die Contribution ausdrücklich als genealogische Synthese/Perspective positioniert und Schlesinger/Sargent, Vinuesa, Naser, Kramer und Jakeman als konstitutive Vergleichsachsen einbaut.

Falls eine solche Synthese-Originalität als zu schwach für ein eigenständiges Paper eingeschätzt wird, ist der saubere Fallback C06-R2 bzw. die Integration als Perspective/Essay statt Framework-Paper.