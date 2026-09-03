# Descriptive Trias Literature Stress Test v0.1

**Status:** COMPLETE / PENDING CLAIM DECISION  
**Stand:** 2026-09-03  
**Depends on:** D022, `theory/descriptive_trias_v0_1.md`

## 1. Zu prüfende starke These

Der Stress-Test versucht ausdrücklich, die folgende starke Neuheitslesart zu widerlegen:

> Es fehle in der Wissenschaftsphilosophie und Methodologie von Computational Science / AI for Science ein gemeinsamer deskriptiver Rahmen, der `Realität/Zielsystem (R)`, `Theorie (T)` und `Berechnung (C)` als analytisch getrennte Rollen betrachtet und ein Modell primär über die drei paarweisen Relationen `R–T`, `T–C` und `C–R` beschreibt, ohne daraus sofort eine normative Optimierungsregel abzuleiten.

Der Test unterscheidet dabei zwischen:

1. Neuheit der **drei Rollen**;
2. Neuheit einer **Dreiecks-/Trade-off-Metapher**;
3. Neuheit von **purpose-relative adequacy**;
4. Neuheit einzelner AI-for-Science-Spannungen;
5. möglicher Neuheit der **exakten relationalen Profilstruktur**.

---

## 2. Comparator A — Theorie, Experiment und Berechnung als drei wissenschaftliche Modi

### Befund

Die Vorstellung, dass moderne Wissenschaft nicht nur aus Theorie und Experiment besteht, sondern Berechnung/Simulation eine dritte eigenständige wissenschaftliche Praxis bildet, ist weit verbreitet. In Wissenschafts- und Computational-Science-Diskursen wird computation seit Jahrzehnten als `third pillar` bzw. dritte Methode neben theory und experiment beschrieben.

Paul Humphreys entwickelt Computational Science explizit als neue wissenschaftliche Methode. Eric Winsberg diskutiert Simulation als zwischen Theorie und Experiment liegende Praxis. Johannes Lenhard behandelt Simulation Modeling als neuen Typ mathematischer Modellierung mit eigenen epistemischen Eigenschaften.

### Konsequenz

**FAIL für starken Neuheitsclaim:**

```text
"Es gibt drei wissenschaftlich relevante Bereiche Theorie / Empirie / Berechnung"
```

ist nicht neu.

### Wichtige Differenz zur Descriptive Trias

Der klassische Dreiklang lautet meist:

```text
theory / experiment / computation
```

Die Descriptive Trias setzt dagegen

```text
reality/target / theory / computation
```

und behandelt Experiment/Daten nicht als Ersatz für Realität, sondern als Vermittlungs- bzw. Evidenzpraktiken. Diese Differenz ist konzeptionell relevant, aber allein noch kein ausreichender Novelty-Nachweis.

---

## 3. Comparator B — Models as Mediators

### Befund

Morgan und Morrison beschreiben wissenschaftliche Modelle als teilweise autonome Vermittlungsinstrumente zwischen Theorie und Welt. Modelle können genutzt werden, um sowohl über Theorien als auch über die Welt zu lernen.

### Coverage

Sehr hoch für:

```text
R <-> model <-> T
```

und für die Idee, dass epistemische Vermittlung nicht in einer einfachen Theorie-Welt-Abbildung aufgeht.

### Rest

Berechnung ist dort nicht systematisch als dritter Pol mit einer eigenen paarweisen Relation zu Theorie und Zielsystem typisiert.

### Konsequenz

**FAIL** für jede Behauptung, die Trias entdecke erstmals einen vermittelnden Bereich zwischen Theorie und Welt.

**OFFEN** bleibt die exakte `R/T/C edge-profile`-Struktur.

---

## 4. Comparator C — Philosophie der Simulation und Computational Science

### Befund

Humphreys, Winsberg und Lenhard decken große Teile genau jener Spannungen ab, die das Projekt motivieren:

- analytisch gegebene Theorie vs. computational realization;
- epistemische Opazität von Berechnung;
- Simulation als Anwendung, Exploration und teilweise Experiment;
- Beziehung von Simulationsoutput zur Welt;
- Veränderung von Begriffen wie Lösung, Verständnis und Validation durch computation.

Winsbergs Simulationsepistemologie beginnt ausdrücklich bei Fällen, in denen zugrunde liegende Gleichungen analytisch nicht lösbar sind und deren Verhalten über computationale Repräsentationen untersucht wird. Lenhard behandelt explizit `solution or imitation?`, Validation und Reality.

### Konsequenz

**FAIL** für starke Einzelclaims wie:

```text
T-C Spannung ist neu
C-R Spannung ist neu
Berechnung verändert den Lösungsbegriff erstmals
```

### Rest

Die Literatur analysiert diese Probleme meist thematisch und fallbezogen. Im Stress-Test wurde kein kanonischer Rahmen identifiziert, der **alle drei paarweisen Relationen R–T, T–C, C–R als gleichrangige deskriptive Profilachsen eines konkreten Modells** verwendet.

---

## 5. Comparator D — Levins, Modelltradeoffs und "Position im Dreieck"

### Befund

Dieser Comparator ist strukturell besonders wichtig. Levins' Modellierungsdiskussion behandelt Tradeoffs zwischen `realism`, `generality` und `precision`. Spätere Darstellungen visualisieren Modelle ausdrücklich als Punkte in einem Dreieck; zusätzliche Arbeiten formalisieren Tradeoffs zwischen theoretischen Desiderata. Tractability wurde in der Debatte außerdem als zusätzliche praktische Dimension diskutiert.

### Konsequenz

**FAIL** für eine starke Behauptung wie:

> Die Idee, Modelle in einem Dreiecksraum zu positionieren und Spannungen/Tradeoffs zwischen Dimensionen zu beschreiben, sei neu.

Sie ist klar nicht neu.

### Sehr wichtiger Guardrail

Die Levins-These notwendiger Tradeoffs ist selbst umstritten. Orzack und Sober bestreiten eine notwendige allgemeine Tradeoff-Struktur; spätere Autoren rekonstruieren sie eher als pragmatische Modellierungsproblematik.

Deshalb darf die Descriptive Trias **nicht** ohne weitere Begründung behaupten:

```text
mehr R-T => notwendig weniger T-C oder C-R
```

### Rest

Levins' Achsen sind **Modellvirtues** (`realism`, `generality`, `precision`), nicht epistemische Beziehungen zwischen `target`, `theory` und `computation`. Der Descriptive-Trias-Rest ist deshalb nicht die Dreiecksgeometrie, sondern die **Typisierung der drei Kanten**.

---

## 6. Comparator E — Adequacy-for-purpose

### Befund

Wendy Parker entwickelt ein starkes adequacy-for-purpose-Modell: Modellqualität ist relativ zu einem konkreten Zweck zu beurteilen. Ein Modell kann für einen Zweck geeignet sein, obwohl es in anderer Hinsicht unrealistisch oder unvollständig ist. Die Eignung hängt gemeinsam von Target, User, Methodology, Circumstances und Purpose ab. Auch computational cost und praktische Eigenschaften können relevant sein.

Bokulich und Parker übertragen diese Logik zudem auf Daten und Datenmodelle.

### Konsequenz

**FAIL** für folgende mögliche Trias-Neuheitsclaims:

```text
Modellgüte ist nicht global
Modellgüte ist zweckrelativ
Realitätsnähe allein bestimmt Modellgüte nicht
computational demands können epistemisch/praktisch relevant sein
```

Diese Punkte sind gut etablierte Vorarbeit.

### Rest

Adequacy-for-purpose zerlegt Modellgüte nicht zwingend in die drei spezifischen Relationen

```text
A_RT, A_TC, A_CR.
```

Die Descriptive Trias könnte hier als **feste relationale Dekomposition** eines purpose-relative assessment dienen, nicht als Alternative zur adequacy-for-purpose-Theorie.

---

## 7. Comparator F — AI prediction vs scientific understanding

### Befund

In der AI-for-Science-Literatur ist ausdrücklich diskutiert, dass sehr gute Vorhersage nicht automatisch wissenschaftliches Verständnis erzeugt. Arbeiten zu computer-assisted scientific understanding unterscheiden predictive success von Erklärung/Mechanismus/Verstehen.

Aktuelle Arbeiten zu mechanistic world models formulieren dieselbe Herausforderung zugespitzt: prediction alone is not scientific discovery or reusable explanatory understanding.

### Konsequenz

**FAIL** für die Einzelthese:

```text
Ein AI-Modell kann gut vorhersagen, ohne Theorie/Verständnis zu liefern.
```

Dies ist keine neue Trias-Beobachtung.

### Rest

Innerhalb der Descriptive Trias wird diese bekannte Trennung nur als ein bestimmtes Profil gelesen:

```text
A_CR hoch bezüglich Prediction
A_RT schwach/unklar bezüglich Erklärung/Mechanismus
```

Der mögliche Wert liegt in der Vergleichbarkeit mit anderen, anders gelagerten Fällen.

---

## 8. Comparator G — Synthetic data / sim-to-real gap

### Befund

Die AI-/Robotics-Literatur behandelt die `reality gap` zwischen synthetischen Trainingsdaten bzw. Simulationen und realen Zielsystemen explizit. Neuere Arbeiten sprechen ausdrücklich von einem epistemologischen sim-to-real problem und fordern reale Validation.

### Konsequenz

**FAIL** für die Einzelthese:

```text
Gute Güte auf synthetischen Daten impliziert keine Güte in der Realität.
```

### Rest

In der Descriptive Trias ist dies ein exemplarischer Fall:

```text
A_TC stark relativ zu Simulator/Theorie
A_CR offen oder schwach relativ zur Realität.
```

Auch hier ist die Einzelbeobachtung nicht neu; nur die gemeinsame Profilierung mit den beiden anderen Kanten bleibt Kandidat.

---

## 9. Comparator H — Physics-informed / Scientific Machine Learning

### Befund

Scientific ML und Physics-informed ML verbinden mathematische Modelle, Daten und neuronale Berechnung explizit. Die Literatur betrachtet Forward- und Inverse-Probleme, Datenknappheit, physikalische Plausibilität, Generalisierung und computational cost.

### Konsequenz

**FAIL** für die Behauptung, AI for Science habe bislang Theorie, Daten und Berechnung nicht gemeinsam betrachtet.

### Rest

Diese Literatur ist primär methodisch-technisch organisiert. Der Stress-Test identifizierte keinen etablierten SciML-Rahmen, der ein konkretes Modell **deskriptiv als Dreierprofil der epistemischen Beziehungen `R–T`, `T–C`, `C–R`** klassifiziert.

---

## 10. Direktsuche nach einem isomorphen Rahmen

Gesucht wurde gezielt nach Kombinationen von:

```text
reality / theory / computation
world / theory / simulation
experiment / theory / computation triangle
epistemic triangle computation science
model position triangle computation reality theory
```

### Ergebnis

Gefunden wurden:

- verbreitete `theory / experiment / computation`-Triaden;
- Simulation als dritte oder intermediäre epistemische Praxis;
- andere epistemic triangles mit völlig anderen Vertices;
- Levins-artige Modelltradeoff-Dreiecke;
- purpose-relative problem spaces;
- AI-spezifische Teilspannungen.

Im aktuellen Stress-Test wurde **kein klarer kanonischer Direktanalog** gefunden, der zugleich folgende fünf Eigenschaften besitzt:

```text
1. R = target/reality, T = theory, C = computation;
2. die drei Kanten sind die primären Adäquanzrelationen;
3. ein konkretes Modell erhält ein relationales Profil über diese drei Kanten;
4. die Darstellung ist zunächst deskriptiv, nicht normativ;
5. derselbe Rahmen wird über Simulation, analytische Theorie, synthetic-data ML und AI-driven discovery angewandt.
```

Dies ist ein **Search Result**, kein Beweis der Originalität. Eine systematische bibliographische Prüfung über Fachdatenbanken bleibt für eine Publikation notwendig.

---

## 11. Stress-Test-Matrix

| Kandidat | Bereits klar etablierte Vorarbeit? | Neuheitsstatus |
|---|---:|---|
| Berechnung als dritte wissenschaftliche Praxis | ja | FAIL |
| Modelle vermitteln zwischen Theorie und Welt | ja | FAIL |
| Theorie kann berechnungstechnisch problematisch sein | ja | FAIL |
| Simulation kann von Realität/Experiment abweichen | ja | FAIL |
| Modellgüte ist zweckrelativ | ja | FAIL |
| Modelle stehen in Tradeoffs / können in Dreiecken positioniert werden | ja | FAIL |
| AI-Prediction kann ohne Verständnis funktionieren | ja | FAIL |
| Synthetic-to-real gap | ja | FAIL |
| R/T/C als feste drei Rollen | sehr nahe Vorläufer | höchstens schwache Neuheit |
| **drei paarweise R–T / T–C / C–R-Adäquanzrelationen als gemeinsames deskriptives Modellprofil** | kein Direktanalog im v0.1-Stress-Test gefunden | **PROMISING / NOT YET ESTABLISHED** |

---

## 12. Wichtigste theoretische Korrektur gegenüber früheren Projektphasen

Der stärkste verbleibende Kandidat ist **nicht**:

```text
"Wissenschaft ist ein Trade-off-Dreieck"
```

sondern:

> Ein computational-science/AI-for-Science-System besitzt mehrere **relationsspezifische epistemische Adäquanzen**. Die Trias schlägt vor, diese systematisch als `R–T`, `T–C` und `C–R` zu unterscheiden, anstatt Erfolg durch eine einzige globale Kategorie wie accuracy, realism, validation oder understanding zu repräsentieren.

Diese Formulierung vermeidet drei bisherige Probleme:

1. keine notwendige Nullsummen-Tradeoff-These;
2. keine Behauptung, Berechnung sei als dritte Praxis neu;
3. keine Behauptung, einzelne AI-Probleme wie sim2real oder prediction-vs-understanding seien neu.

---

## 13. Kandidat für einen neuen Hauptclaim — noch NICHT akzeptiert

### C08-D — Descriptive Relational Profile Claim

> **C08-D:** Für Computational Science und AI for Science ist es analytisch nützlich, drei verschiedene epistemische Adäquanzrelationen zu unterscheiden: die Beziehung zwischen Zielsystem und Theorie (`R–T`), zwischen Theorie und computational realization (`T–C`) sowie zwischen computational realization und Zielsystem (`C–R`). Erfolg auf einer dieser Relationen impliziert nicht ohne zusätzliche Evidenz, dass die übrigen Relationen gleichermaßen etabliert sind. Ein Modell kann deshalb deskriptiv durch ein relationales epistemisches Profil über diese drei Kanten charakterisiert werden. Der beanspruchte Beitrag liegt in dieser festen gemeinsamen Profilstruktur, nicht in der Neuheit der zugrunde liegenden Einzelprobleme oder in einer notwendigen Trade-off-These.

### Evidenzstatus

- Einzelprobleme: sehr stark durch bestehende Literatur gestützt;
- analytische Trennbarkeit der drei Relationen: plausibel und durch Projektfälle illustriert;
- direkter literarischer Vorläufer der exakten Profilstruktur: im v0.1-Stress-Test nicht identifiziert;
- praktische analytische Nützlichkeit des Profils: noch nicht demonstriert;
- Originalität: **promising but unverified**.

---

## 14. Empfohlener nächster Schritt

**Noch kein neues numerisches Experiment.**

Empfohlen wird ein `Descriptive Trias Profile Test v0.1` als rein konzeptioneller Härtungsschritt:

Sechs sehr unterschiedliche Fälle werden mit exakt demselben Schema profiliert:

```text
1. Sundman / analytische Repräsentation
2. Figure-eight / numerical solver
3. real-data black-box predictor
4. synthetic-data ML surrogate
5. physics-informed ML
6. equation discovery
```

Für jeden Fall werden ausschließlich die drei Kanten markiert als:

```text
ESTABLISHED / PARTIAL / UNCERTAIN / UNTESTED / NOT_APPLICABLE
```

und geprüft:

1. diskriminiert das Profil Fälle, die in `theory/experiment/computation`-Taxonomien gleich aussehen?
2. entstehen Kategorienfehler, wenn man die drei Kanten nicht trennt?
3. ist die Dreiteilung vollständig genug, oder benötigt sie zusätzliche primäre Achsen?
4. lässt sich das Profil ohne Informationsverlust auf Parker/Levins/Simulation-Philosophie reduzieren?

Erst wenn dieser Test einen echten analytischen Mehrwert zeigt, sollte C08-D akzeptiert und der Paper-Hauptclaim neu aufgebaut werden.

---

## 15. Entscheidungsempfehlung

**REVISE THE PROJECT AROUND C08-D, BUT DO NOT YET ACCEPT C08-D AS AN ESTABLISHED CONTRIBUTION.**

Akzeptiert werden sollte zunächst nur das Ergebnis des Stress-Tests:

1. Die starke Neuheit der drei Pole bzw. der Dreiecksmetapher ist verworfen.
2. Eine notwendige Trade-off-These wird nicht verfolgt.
3. Die präzisierte deskriptive Idee ist deutlich besser abgegrenzt als die frühere V&V-/Provenance-Lesart.
4. Die exakte `R–T / T–C / C–R`-Profilstruktur bleibt ein ernstzunehmender, aber noch unbestätigter Eigenbeitragskandidat.
5. Nächste Abhängigkeit: `Descriptive Trias Profile Test v0.1`.