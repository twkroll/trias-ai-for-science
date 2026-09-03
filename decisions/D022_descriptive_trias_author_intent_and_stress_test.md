# D022 — Deskriptive Trias als präzisierte Autorenintention; Literatur-Stress-Test freigegeben

**Datum:** 2026-09-03  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D021

## Entscheidung

Die nach D021 konservativ gewählte Paper-Positionierung wird **nicht verworfen**, aber vor einer endgültigen Paper-Fixierung erneut gegen die präzisierte Autorenintention geprüft.

Die präzisierte Intention lautet nicht primär:

- neue Fehlerklassen zu entdecken;
- ein neues V&V- oder Provenance-System zu liefern;
- normative Regeln für gute Wissenschaft vorzuschreiben.

Stattdessen soll geprüft werden, ob eine **deskriptive wissenschaftsphilosophische Trias** tragfähig und eigenständig genug ist:

```text
R = Realität / intendiertes Zielsystem
T = Theorie / erklärende oder formale Repräsentation
C = Berechnung / computational realization
```

Der zentrale Gegenstand sind die drei paarweisen Spannungs- bzw. Adäquanzrelationen:

```text
R <-> T : theoretische/empirische Adäquanz und wissenschaftliches Verständnis
T <-> C : Berechenbarkeit, operative Realisierbarkeit und rechnerische Treue zur Theorie
C <-> R : empirische Grounding-/Transfer-/Repräsentationsbeziehung der Berechnung zum Zielsystem
```

Ein wissenschaftliches oder AI-for-Science-Modell kann auf einer Relation stark und auf einer anderen schwach, ungeklärt oder gar nicht ausgebildet sein. Erfolg auf einer Relation wird nicht automatisch als globaler Erfolg des Systems interpretiert.

## Deskriptiver Status

Die Trias wird in diesem Schritt ausdrücklich **nicht normativ** verstanden. Sie soll zunächst beschreiben:

- welche drei Rollen in einem Fall vorhanden sind;
- welche der drei Relationen tatsächlich untersucht oder validiert wurde;
- welche Relationen offen, schwach oder nicht anwendbar bleiben;
- welche Art von wissenschaftlichem Erfolg jeweils vorliegt.

## Wichtiger Guardrail

Der Begriff `Trade-off` wird vorerst **nicht als notwendiges Nullsummengesetz** verwendet. Die Literatur zu Modelltradeoffs zeigt, dass notwendige Tradeoffs selbst umstritten sind. Projektintern wird zunächst von `Spannungen`, `partiell unabhängigen Adäquanzrelationen` oder `relationalen Profilen` gesprochen.

Ebenso wird nicht behauptet, dass es prinzipiell unmöglich sei, auf allen drei Relationen zugleich hohe Adäquanz zu erreichen. Die schwächere Arbeitsthese lautet nur: Es gibt keine allgemeine Garantie, dass Erfolg auf einer Relation Erfolg auf den anderen impliziert.

## Freigegebener nächster Schritt

Ein **Descriptive Trias Literature Stress Test v0.1** soll ausschließlich prüfen, ob diese genaue deskriptive Struktur bereits explizit in der Literatur vorliegt:

1. drei funktionale Rollen `R/T/C`;
2. die drei paarweisen Relationen als primäre Analyseeinheiten;
3. ein relationales Profil eines wissenschaftlichen/AI-Modells statt einer einzigen globalen Güte;
4. deskriptive statt normative Interpretation;
5. Anwendbarkeit auf analytische Theorie, numerische Simulation, synthetische Daten, ML-Surrogate und datengetriebene Theoriefindung.

Erst nach diesem Stress-Test wird entschieden, ob die präzisierte Trias den konservativen C06-R2-Pivot substanziell schärft.