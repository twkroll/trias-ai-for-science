# C06 Comparison v0.1 — Standard-Numerik/V&V vs. Trias-Audit

**Status:** COMPLETE FOR REVIEW  
**Purpose:** harter Originalitäts-/Mehrwerttest mit denselben Full-v0.1-Resultaten  
**Stand:** 2026-09-02

## Vergleichsregel

Ein Punkt zählt nur dann als zusätzlicher Trias-Mehrwert, wenn die Trias

1. eine relevante Frage stellt, die im starken Standardrahmen nicht bereits vorhanden ist,
2. eine andere Lokalisierung eines Fehlers/einer Annahme erzwingt,
3. oder die gerechtfertigte wissenschaftliche Schlussfolgerung gegenüber der Standardanalyse nachweislich schärft.

Eine andere Terminologie, Visualisierung oder Gruppierung allein zählt nicht.

## Matrix

| Demonstratorfrage | Standard-Numerik / V&V / Credibility | Trias-Zuordnung | Zusätzlicher Mehrwert im aktuellen Fall? |
|---|---|---|---|
| Implementiert der Code die Newtonsche Dynamik/den Solver korrekt? | Code verification, Unit-/benchmark tests | Theorie → Berechnung | Nein; andere Zuordnung, aber keine neue Frage |
| Nähert sich die numerische Lösung bei Verfeinerung? | Solution verification, convergence/refinement study | Theorie → Berechnung / Berechnung → Zielsystem | Nein |
| Ist die DOP853-Referenz hinreichend vertrauenswürdig? | Numerical uncertainty / solution verification / benchmark credibility | Berechnung → Zielsystem | Nein |
| Welche theoretische Struktur erhält der Solver? | Geometric numerical integration, invariant/error analysis | Theorie → Berechnung | Nein |
| Ist RK4 oder Verlet „besser“? | Intended use + quantities of interest + error/cost tradeoff | wissenschaftliche Nutzung über die drei Pole/Kanten | Nein; intended-use-Relativität ist etabliert |
| Welche Rolle spielen Ressourcen? | Cost/credibility/use assessment | operative Machbarkeit im Berechnungs-Pol | Nein |
| Ist Langzeit-Trajektorienabweichung ein numerischer Fehler oder dynamische Sensitivität? | Sensitivity analysis + numerical error analysis | Zielsystem/Problem vs. Berechnung | Nein; die Trias macht die Herkunft visuell explizit, aber die Unterscheidung ist etabliert |
| Sind gerundete Figure-eight-ICs das Zielsystem oder Ground Truth? | Model/input specification, assumptions, uncertainty, permissible use | synthetisches Zielsystem vs. Rechenoutput | Teilweise nützlich als begriffliche Disziplin, aber nicht eindeutig neu |
| Warum ist Sundmans konvergente Reihe wissenschaftlich-operativ unbrauchbar? | Nicht primär eine klassische V&V-Frage eines ausgeführten Simulationsmodells; behandelbar über computational complexity/tractability und Numerik | Theorie → Berechnung; Lösungsleiter | Hier ist die Trias breiter als der konkrete Solver-V&V-Workflow, aber die Einzelfrage ist nicht philosophisch neu |
| Wie werden analytische Traktabilität, numerische Operationalisierung und intended use gemeinsam dokumentiert? | Kann über mehrere bestehende Frameworks kombiniert werden | gemeinsames Trias-Schema | Möglicher Integrationsvorteil; derzeit noch keine starke Neuheit |

## Ergebnis

### Was der Standardrahmen bereits vollständig leistet

Die Full-v0.1-Befunde zu

- Refinement und beobachteter Ordnung,
- Referenzunsicherheit,
- Energiefehler und Drift,
- Drehimpulserhaltung,
- Ressourcenkosten,
- Zweckrelativität der Solverbewertung,
- Dokumentation von Annahmen und Geltungsgrenzen

lassen sich ohne Informationsverlust in etablierter numerischer Analysis und V&V/Credibility-Sprache ausdrücken.

Damit scheitert der starke C06-Test im reinen Figure-eight-Solverfall: Die Trias hat dort keine eindeutig neue numerische Diagnose erzeugt.

## Wo ein Restmehrwert verbleibt

Der Restmehrwert ist derzeit strukturell:

1. **Durchgängige Provenance:** Zielsystem → Theorie → analytische/formale Zugänglichkeit → numerische Operationalisierung → wissenschaftlicher Gebrauch werden in einer Darstellung gehalten.
2. **Kantenfokus:** Annahmen und Verluste werden nicht nur als globale „model uncertainty“ gesammelt, sondern einem Übergang zugeordnet.
3. **Sundman-Verbindung:** Der Audit beginnt vor dem eigentlichen Simulationslauf und macht sichtbar, warum analytische Repräsentation, operative Machbarkeit und wissenschaftlicher Gebrauch auseinanderfallen können.
4. **Vorbereitung auf hybride AI-for-Science-Ketten:** Bei simulationsgenerierten Daten und gelernten Surrogaten entstehen zusätzliche Übersetzungen, die im einfachen Solverfall noch nicht vorhanden sind.

Punkt 4 ist eine Hypothese und muss erst getestet werden.

## Konsequenz für das Forschungsprogramm

Der reine numerische Demonstrator hat seinen Zweck erfüllt, obwohl er den starken C06-Claim nicht bestätigt:

- C05 ist empirisch gestützt.
- Die starke C06-Neuheitsbehauptung wird nicht gestützt.
- Die Trias sollte deshalb nicht als Ersatz für V&V verkauft werden.
- Der mögliche Beitrag verschiebt sich zu einem kompakten integrativen Audit/Provenance-Schema, das über analytische, numerische und später lernbasierte Übergänge hinweg funktioniert.

## Empfohlener nächster Test

Falls C06-R akzeptiert wird, sollte die nächste Erweiterung minimal bleiben und nur eine zusätzliche AI-for-Science-Übersetzung einführen:

**Newtonian target/theory → trusted numerical data generator → learned surrogate → scientific use.**

Der ML-Teil soll nicht auf Performance optimiert werden. Er soll einen kontrollierten Fall erzeugen, in dem getrennt geprüft werden kann:

- ob Fehler aus dem Datengenerator in das Lernmodell vererbt werden;
- ob Theorie-Struktur im Training vorhanden, verloren oder nur indirekt getestet wird;
- ob gute Test-MSE eine ungerechtfertigte Aussage über das Zielsystem suggeriert;
- ob die Trias diese Herkunft transparenter lokalisiert als ein Standard-ML-/V&V-Audit.

Erst dieser Test kann entscheiden, ob der AI-for-Science-Bezug einen eigenständigeren methodologischen Mehrwert trägt.