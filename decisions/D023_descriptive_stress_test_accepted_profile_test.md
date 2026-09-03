# D023 — Descriptive-Trias-Literatur-Stress-Test akzeptiert; Profile Test freigegeben

**Datum:** 2026-09-03  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D022

## Entscheidung

Der `Descriptive Trias Literature Stress Test v0.1` wird als aktueller Projektstand akzeptiert.

Akzeptiert werden insbesondere folgende Grenzen:

- Berechnung als dritte wissenschaftliche Praxis ist nicht neu;
- Modelle als Vermittler zwischen Theorie und Welt sind nicht neu;
- Modelltradeoffs und Dreiecksmetaphern sind nicht neu;
- purpose-relative adequacy ist nicht neu;
- Prediction ohne Understanding, sim-to-real gaps und physics-informed ML sind keine neuen Einzelprobleme der Trias;
- eine notwendige Nullsummen-Trade-off-These zwischen den drei Kanten wird nicht behauptet.

Als weiterhin prüfbarer Rest wird ausschließlich folgende Struktur zugelassen:

```text
R = Realität / intendiertes Zielsystem
T = Theorie / formale oder erklärende Repräsentation
C = computational realization

A_RT = Status der Relation Realität–Theorie
A_TC = Status der Relation Theorie–Berechnung
A_CR = Status der Relation Berechnung–Realität
```

Ein möglicher Eigenbeitrag liegt höchstens in der festen gemeinsamen **relationalen Profilstruktur** über diese drei Kanten.

## C08-D

Der Claim-Kandidat C08-D wird durch dieses GO **noch nicht akzeptiert**. Seine Neuheit und analytische Nützlichkeit bleiben offen.

## Freigegebener nächster Schritt

Ein `Descriptive Trias Profile Test v0.1` wird ohne neues numerisches Experiment durchgeführt. Der Test muss mindestens folgende sechs Fälle mit derselben Profilgrammatik analysieren:

1. Sundman / Drei-Körper-Problem;
2. Figure-eight / numerische Solver;
3. Black-box ML auf realen Daten;
4. ML-Surrogat auf synthetischen Daten;
5. Physics-informed ML;
6. Equation Discovery.

Die Statussprache bleibt zunächst qualitativ:

```text
ESTABLISHED
PARTIAL
UNCERTAIN
UNTESTED
NOT_APPLICABLE
```

Der Test soll ausdrücklich prüfen:

- ob gleiche grobe Erfolgslabels unterschiedliche R/T/C-Profile verdecken;
- ob Evidenz für eine Kante die anderen Kanten offen lassen kann;
- ob das Profil tatsächlich einen zusätzlichen deskriptiven Unterschied sichtbar macht;
- wo die Dreierprofil-Struktur selbst zu grob oder mehrdeutig wird.

Keine neue Simulation und kein Paper-Hauptclaim vor Abschluss dieses Tests.