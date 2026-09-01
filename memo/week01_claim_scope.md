# Week 1 — Claim and Scope Memo

**Status:** living memo  
**Aktueller Stand:** C01 akzeptiert, C02 zur Entscheidung vorgelegt

## 1. Methodologischer Status

Die Trias **Realität – Theorie – Berechnung/Umsetzung** wird zunächst als methodologisches Audit-Framework untersucht. Es wird nicht behauptet, dass sie eine universale Ontologie wissenschaftlicher Erkenntnis darstellt.

## 2. Akzeptierte zentrale Arbeitsthese

> Im Drei-Körper-Fall kann die explizite Trennung von Zielsystem, theoretischer Beschreibung und operativer Umsetzung diagnostische Unterschiede sichtbar machen, die in einer bloßen Theorie–Experiment-Beschreibung unterbestimmt bleiben. Der beanspruchte Mehrwert besteht nicht darin, Berechnung erstmals als epistemisch relevante Praxis zu identifizieren, sondern darin, entsprechende Einsichten in ein explizites Audit-Schema zu überführen, das Annahmen, Transformationen und Validierungsanforderungen den drei Polen und ihren Übergängen zuordnet.

### Revisionskriterium

Die These muss abgeschwächt werden, wenn die Trias keine zusätzliche diagnostische Arbeit gegenüber etablierter Simulationsphilosophie, numerischer Fehleranalyse, Modellvalidierung oder Reproduzierbarkeitsprüfung leistet.

## 3. Operationale Rollen

### Realität

Das Zielsystem, relativ zu dem eine wissenschaftliche Repräsentation, Vorhersage oder Berechnung bewertet wird. „Realität“ wird hier funktional und nicht als vollständige metaphysische Kategorie verwendet.

### Theorie

Die strukturierte Gesamtheit aus Gleichungen, Gesetzen, Idealisierungen, Symmetrien, Invarianten, Annahmen und Interpretationsregeln, mit denen das Zielsystem beschrieben wird.

### Berechnung/Umsetzung

Die endliche operative Realisierung theoretischer Strukturen: numerische Repräsentation, Diskretisierung, Solver, Schrittweite, Präzision, Code, Ressourcen und — falls später relevant — ML-Architektur, Loss und Optimierung.

## 4. Aktuell offene C02-Entscheidung

Vorgeschlagen wird, im Drei-Körper-Fall nicht von „synthetischer Realität“ als technischem Kernbegriff zu sprechen, sondern von einem **synthetischen Zielsystem**.

Vorgeschlagene Arbeitsdefinition:

> Ein synthetisches Zielsystem ist ein durch explizite Festlegungen konstruiertes System, dessen Zustandsraum, Dynamik, Parameter und Anfangsbedingungen so spezifiziert werden, dass Aussagen und rechnerische Repräsentationen relativ zu diesem System bewertet werden können.

Schematisch:

\[
S_{\mathrm{syn}}=(\mathcal X,F,\theta,x_0).
\]

Wichtig ist die Trennung von diesem Zielsystem und einer konkreten numerischen Trajektorie

\[
\hat{x}_0,\hat{x}_1,\ldots,\hat{x}_N.
\]

Die drei Pole werden damit als **analytisch unterscheidbare Rollen** behandelt, nicht als notwendig ontologisch unabhängige Entitäten.

## 5. Drei-Körper-Schichtung

Der spätere Worked Example soll mindestens unterscheiden:

1. physisches oder synthetisches Zielsystem,
2. formale analytische Resultate,
3. konvergente, aber möglicherweise praktisch nicht traktable Reihendarstellungen,
4. numerische Integration,
5. optionales ML-Surrogat.

Die Aussagen zu Sundman werden erst in C03 präzise verifiziert.

## 6. Minimaldemonstrator — Scope

Noch keine Implementierung. Später sollen bei identischem Zielsystem, identischer Theorie und identischen Anfangsbedingungen wenige numerische Realisierungen verglichen werden.

Der Demonstrator ist nur dann für die Trias relevant, wenn er nicht bloß numerische Unterschiede zeigt, sondern eine spezifischere Diagnose oder Validierungsanforderung erzeugt.

## 7. Nächster Schritt

Nach Entscheidung über C02 folgt ausschließlich:

**C03 — präzise Prüfung der Sundman-Claims.**