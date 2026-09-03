# Descriptive Trias v0.1 — relationale Profile zwischen Realität, Theorie und Berechnung

**Status:** WORKING THEORY / PENDING CLAIM REVIEW  
**Stand:** 2026-09-03  
**Depends on:** D022

## 1. Kernidee

Die Trias wird als **deskriptive wissenschaftsphilosophische Struktur** formuliert. Sie beschreibt nicht zuerst, wie Wissenschaft betrieben werden soll, sondern welche Arten von epistemischer Adäquanz in Computational Science und AI for Science auseinanderfallen können.

Die drei funktionalen Rollen sind:

```text
R = Realität / intendiertes Zielsystem
T = Theorie / formale, mechanistische oder erklärende Repräsentation
C = Berechnung / computational realization, numerische oder gelernte Repräsentation
```

`R`, `T` und `C` sind analytische Rollen, keine notwendig ontologisch unabhängigen Entitäten.

## 2. Die drei primären Relationen

Die Analyseeinheit ist nicht nur der jeweilige Pol, sondern die Beziehung zwischen zwei Rollen.

### A_RT — Realität ↔ Theorie

Frage:

> In welchem Sinn beschreibt, erklärt oder strukturiert die Theorie das intendierte Zielsystem?

Mögliche Zustände:

- gut gestützt;
- partiell/idealisiert;
- umstritten;
- unbekannt;
- keine explizite Theorie vorhanden.

### A_TC — Theorie ↔ Berechnung

Frage:

> In welchem Sinn ist die Theorie operativ berechenbar und wird sie durch die konkrete Berechnung treu realisiert?

Hierzu gehören beispielsweise:

- analytische vs. praktische Evaluierbarkeit;
- numerische Diskretisierung;
- Approximation;
- Stabilität;
- Ressourcenbedarf;
- Surrogat-/Emulator-Treue gegenüber einem theoretisch definierten Simulator.

### A_CR — Berechnung ↔ Realität

Frage:

> In welchem Sinn ist der computational output gegenüber dem intendierten Zielsystem empirisch oder repräsentational verankert?

Hierzu gehören beispielsweise:

- Validation gegen reale Beobachtungen;
- sim-to-real transfer;
- synthetic-to-real gap;
- predictive performance auf realen Daten;
- externe Gültigkeit einer Simulation oder eines ML-Modells.

## 3. Relationales epistemisches Profil

Ein wissenschaftliches Modell oder AI-System wird zunächst nicht durch einen einzigen Skalar `quality` beschrieben, sondern durch ein relationales Profil

```text
P(M;U) = [A_RT, A_TC, A_CR]
```

relativ zu einem intendierten wissenschaftlichen Gebrauch `U`.

Die Einträge sind in v0.1 **qualitative Statusangaben**, keine metrischen Koordinaten. Zulässige Grundstatus sind beispielsweise:

```text
ESTABLISHED
PARTIAL
UNCERTAIN
UNTESTED
NOT_APPLICABLE
```

Damit soll ausdrücklich vermieden werden, aus der Dreiecksmetapher voreilig ein baryzentrisches Nullsummenmodell zu machen.

## 4. Zentrale deskriptive Hypothese

> Wissenschaftlicher Erfolg in Computational Science und AI for Science ist häufig **relationsspezifisch**. Evidenz für hohe Adäquanz auf einer der Relationen `R–T`, `T–C` oder `C–R` rechtfertigt für sich allein keine Aussage darüber, dass die beiden übrigen Relationen gleichermaßen gut etabliert sind.

Dies ist keine Behauptung absoluter Unabhängigkeit. Die Relationen können sich gegenseitig stützen und in speziellen Fällen logisch oder empirisch gekoppelt sein. Behauptet wird nur, dass keine allgemeine automatische Gleichsetzung zulässig ist.

## 5. Keine notwendige Trade-off-These

Die Autorenintuition verwendet die Sprache von Spannungsfeldern. In v0.1 wird daraus **nicht** die starke Behauptung gemacht:

```text
mehr A_RT => notwendig weniger A_TC oder A_CR
```

oder analog für andere Kanten.

Die vorsichtige Fassung lautet:

> Die drei Relationen stellen unterschiedliche wissenschaftliche Anforderungen dar, die in realen Modellierungspraktiken miteinander in Spannung geraten können. Ob ein echter Trade-off vorliegt, ist fallabhängig und muss separat gezeigt werden.

## 6. AI-for-Science-Archetypen

### Black-box predictor auf realen Daten

Mögliches Profil:

```text
A_CR = stark bezüglich Prediction
A_RT = schwach/unklar bezüglich Mechanismus/Erklärung
A_TC = nur eingeschränkt relevant, wenn keine explizite Theorie implementiert wird
```

Hohe Prediction ist dann wissenschaftlich wertvoll, ohne automatisch theoretisches Verständnis zu liefern.

### ML-Surrogat auf synthetischen Simulationsdaten

Mögliches Profil:

```text
A_TC = stark relativ zum Simulator/Teacher
A_CR = offen, sofern Simulator -> Realität nicht ausreichend validiert ist
A_RT = erbt die theoretische Reichweite und Begrenzung des Simulators, erzeugt sie nicht automatisch neu
```

### Physics-informed ML

Mögliches Profil:

```text
A_TC = explizit durch Theorieconstraints gestärkt
A_CR = weiterhin empirisch zu prüfen
A_RT = hängt von der Adäquanz der eingebetteten Theorie zum Zielsystem ab
```

### Equation Discovery

Mögliches Profil:

```text
A_CR = kann dynamisch/statistisch gut sein
A_RT = strukturelle/mechanistische Identifikation kann dennoch unklar sein
A_TC = Inferenz-/Optimierungspipeline bestimmt, welche Theorie operational erreichbar ist
```

## 7. Verbindung zu bisherigen Projektfällen

### Sundman

Kernspannung:

```text
T -> C
```

Eine konvergente analytische Repräsentation kann mathematisch verfügbar und trotzdem praktisch kaum evaluierbar sein. Wichtig: Die Sundman-Reihe konvergiert; das Problem ist ihre extreme praktische Ineffizienz.

### Figure-eight

Kernspannung:

```text
T -> C -> output
```

Verschiedene numerische Operationalisierungen derselben Theorie erzeugen unterschiedliche use-case-relative Fehler- und Strukturprofile.

### Inverser Lorenz/SINDy-Fall

Kernspannung:

```text
R -> data/reconstruction -> C_infer -> T_hat
```

Der eigene vorregistrierte Minimalfall erzeugte keinen seed-robusten strukturellen Provenance-Effekt. Er bleibt deshalb negativer Test und nicht Beleg für eine allgemeine Nicht-Eindeutigkeitsbehauptung.

### ML v0.1

Kernspannung:

```text
simulator/theory -> synthetic labels -> learned C
```

Der Learner-Fehler dominierte das Teacher-Signal. Damit blieb die Frage, ob teacherrelative und zielsystemrelative Güte auseinanderfallen, in diesem Run unentscheidbar.

## 8. Abgrenzung von bisheriger Directed Trias

Die frühere Directed-Trias-Fassung stellte stark auf Transformationsprovenance und Rechtfertigungsketten ab. Die Descriptive Trias v0.1 verschiebt das Zentrum:

```text
vorher: Welche Transformation/Provenance erzeugt welches Objekt?
jetzt:  Welche der drei epistemischen Relationen ist in diesem Fall wie gut etabliert?
```

Provenance bleibt Hilfsmittel, ist aber nicht mehr der primäre Neuheitskandidat.

## 9. Novelty Guardrails

Nicht behauptet wird:

- Theorie, Experiment und Berechnung als drei wissenschaftliche Modi seien neu;
- Berechnung sei erstmals als epistemisch relevant erkannt;
- Modelle seien erstmals als Vermittler zwischen Theorie und Welt beschrieben;
- Modelltradeoffs seien neu;
- purpose-relative model adequacy sei neu;
- Prediction ohne Understanding sei eine neue AI-for-Science-Beobachtung;
- sim-to-real gaps seien neu;
- alle drei Relationen stünden notwendig in einem Nullsummen-Trade-off.

Der mögliche Eigenbeitrag kann nur enger liegen:

> eine explizite deskriptive Zerlegung wissenschaftlicher/AI-for-Science-Modelle in die drei **paarweisen Adäquanzrelationen** `R–T`, `T–C` und `C–R`, verstanden als relationales epistemisches Profil statt als globale Modellgüte.

## 10. Offene Hauptfrage

Die aktuelle Forschungsfrage lautet:

> Gibt es bereits einen etablierten wissenschaftsphilosophischen Rahmen, der genau diese drei Rollen und ihre drei paarweisen Adäquanzrelationen als gemeinsame deskriptive Profilstruktur für Computational Science bzw. AI for Science verwendet?

Diese Frage wird im `Descriptive Trias Literature Stress Test v0.1` geprüft.