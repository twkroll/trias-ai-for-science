# Projektkommando `PDF` — aktuelles Kooperationsbriefing

**Status:** ACTIVE PROJECT WORKFLOW  
**Stand:** 2026-09-02

## Trigger

Wenn im Forschungsdialog als Nachricht allein oder sinngemäß **`PDF`** steht, wird ohne weitere Rückfrage ein **neues, aktuelles und ausführliches Projektbriefing als PDF** erzeugt.

Das Dokument ist für eine mögliche langfristige wissenschaftliche Kooperation gedacht, insbesondere für eine promovierte Physikerin mit wissenschaftsphilosophischem Hintergrund.

## Grundregel

Das PDF wird **jedes Mal neu aus dem aktuellen Projektstand synthetisiert**. Es darf nicht lediglich ein früheres Briefing mit geändertem Datum reproduzieren.

Vor der Erstellung sind mindestens die aktuellen Fassungen von

- `STATUS.md`,
- `claims/claim_registry.md`,
- den seit dem letzten Briefing hinzugekommenen/änderten Claim-Dateien,
- den relevanten Decision-Dateien unter `decisions/`,
- den aktuellen Demonstrator-Spezifikationen/Contracts,
- den wissenschaftlichen Resultatdateien,
- und dem Evidence Register

zu berücksichtigen.

`collaboration/PROJECT_BRIEFING.md` dient als Stil- und Strukturvorlage, nicht als alleinige Wahrheitsquelle.

## Ziel des Dokuments

Das Briefing soll einer fachlich starken externen Person ermöglichen,

1. die Grundidee des Projekts ohne Kenntnis des Chatverlaufs zu verstehen;
2. die physikalische und wissenschaftsphilosophische Motivation nachzuvollziehen;
3. klar zwischen akzeptierten Claims, Arbeitshypothesen, verworfenen starken Claims und offenen Fragen zu unterscheiden;
4. die mathematischen und numerischen Demonstratoren einschließlich wichtiger Formeln und Resultate zu verstehen;
5. nachzuvollziehen, welche Evidenz tatsächlich vorliegt und welche Aussagen bewusst nicht gemacht werden;
6. den aktuellen Originalitäts-/Novelty-Stresstest gegenüber Numerik, V&V, Simulation Philosophy und ML-Credibility zu erkennen;
7. den aktuellen nächsten Schritt und die Stellen zu sehen, an denen kritische Mitarbeit besonders wertvoll wäre.

## Standardinhalt

Das PDF soll, soweit aktuell relevant, folgende Teile enthalten:

1. **Executive Summary** — Projektidee, aktueller Stand, stärkste und schwächste Punkte.
2. **Motivation** — Warum Realität/Zielsystem, Theorie und Berechnung/Umsetzung getrennt auditiert werden sollen.
3. **Begriffe und Trias-Struktur** — Pole, Kanten, synthetisches Zielsystem, methodologischer statt ontologischer Status.
4. **Lösungsleiter und operative Verfügbarkeit** — mathematische Existenz, analytische Repräsentation, Konvergenz, Machbarkeit, Stabilität, wissenschaftliche Nutzbarkeit.
5. **Sundman** — historisch-mathematischer Kern, praktische Traktabilität und methodologische Rolle mit allen akzeptierten Einschränkungen.
6. **Akzeptierte Claims und Decisions** — chronologisch und in Abhängigkeitslogik, jeweils mit Evidenzstatus und Revisionskriterium.
7. **Numerischer Figure-eight-Demonstrator** — Design, Referenzlogik, Solver, Metriken, Gates und zentrale Resultate.
8. **C05/C06-Ergebnis** — use-case-relative Implementierungsprofile; starke Neuheitsbehauptung gegenüber V&V verworfen; verbleibender Integrations-/Provenance-Claim.
9. **AI-for-Science/ML-Provenance-Zweig** — Teacher-Kette, ML-v0.1-Design, Fehlerzerlegung, Gate-Ergebnis und korrekte `INCONCLUSIVE_LEARNER_ERROR`-Interpretation.
10. **Aktueller Follow-up** — z. B. v0.2-Resolvability-Reparatur mit klarer Begründung, was geändert und was bewusst nicht geändert wird.
11. **Vergleich mit bestehenden Frameworks** — V&V/Credibility, Simulationsphilosophie, Dataset-/Model-Provenance; keine überzogenen Neuheitsclaims.
12. **Offene wissenschaftsphilosophische und physikalische Fragen**.
13. **Mögliche Rolle einer Kooperationspartnerin** — konkrete Stellen für konzeptionelle Kritik, Literaturvergleich, Interpretation, Methodologie und gegebenenfalls neue Fallstudien.
14. **Nächste Abhängigkeiten / Arbeitsplan** — möglichst klein und entscheidungsorientiert.
15. **Literaturanker und Evidenzstatus** — Quellen klar von projektinternen Setzungen und eigenen Resultaten trennen.

## Stil

- Deutsch.
- Wissenschaftlich, ausführlich und kooperationsorientiert.
- Formeln sauber gesetzt.
- Keine Marketing-Sprache und keine künstliche Bestätigung des Projekts.
- Negative und inconclusive Resultate werden genauso prominent dokumentiert wie positive Befunde.
- Neue Begriffe werden als projektintern gekennzeichnet, sofern sie nicht etablierte Terminologie sind.
- Literaturbehauptungen werden nicht stärker formuliert, als die vorhandene Evidenz trägt.
- Der Text soll für eine Physikerin mit wissenschaftsphilosophischem Hintergrund geschrieben sein, nicht für ein allgemeines Publikum.

## Ausgabe

Standardmäßig werden erzeugt:

- ein aktuelles PDF;
- die zugehörige LaTeX-Quelldatei.

Dateinamen sollen den Stand enthalten, z. B.

```text
Trias_Projektbriefing_2026-09-02.pdf
Trias_Projektbriefing_2026-09-02.tex
```

Wenn am selben Tag mehrfach `PDF` angefordert wird, wird die jeweils neueste Fassung erzeugt und bei Bedarf versioniert.

## Abgrenzung

`PDF` bedeutet nicht automatisch Paper-Draft, Reviewer-Response oder technische Dokumentation. Es bedeutet das **aktuelle ausführliche Kooperationsbriefing über das gesamte Trias-Projekt**.
