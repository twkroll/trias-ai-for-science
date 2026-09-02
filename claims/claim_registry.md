# Claim Registry

Das Register enthält die wissenschaftlich relevanten Claims des Projekts in Abhängigkeitsreihenfolge.

| ID | Kurzbezeichnung | Status | Evidenzstatus | Entscheidung |
|---|---|---|---|---|
| C01 | Diagnostischer Mehrwert der Trias | ACCEPTED | Plausibel; endgültige Prüfung durch Literatur + Demonstrator ausstehend | D001 |
| C02 | Synthetisches Zielsystem als Realitäts-Pol | ACCEPTED | Begrifflich gut anschlussfähig; konkrete Trias-Rolle ist methodologische Setzung | D002 |
| C03 | Sundmans konvergente Reihenlösung und praktische Traktabilität | ACCEPTED | Mathematisch-historischer Kern gut gestützt; methodologische Lesart projektintern | D003 |
| C04 | Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ wissenschaftliche Nutzbarkeit | ACCEPTED | Numerisch gut gestützt; Machbarkeit/Nutzbarkeit projektinterne Auditbegriffe | D004 |
| DMO | Minimal-Spezifikation des Drei-Körper-Demonstrators | ACCEPTED | Technischer Scope durch D005/D006 eingefroren; Skeleton durch D007 akzeptiert | D005–D007 |
| C05 | Implementierungswahl kann wissenschaftlich relevante Profile erzeugen | ACCEPTED | Full v0.1 run stützt moderate zweckrelative Fassung | D008 |
| C06 | Zusätzlicher diagnostischer Wert des Trias-Audits | PENDING REVIEW — REVISE | Starke Form im reinen Solverfall nicht gestützt; integrative C06-R-Fassung vorgeschlagen | — |

## Arbeitsregel

Ein Claim erhält den Status `ACCEPTED`, wenn die vorgeschlagene Arbeitsfassung im Forschungsdialog durch `GO` bestätigt wurde. `ACCEPTED` bedeutet **nicht endgültig bewiesen**, sondern als aktuelle Forschungsgrundlage akzeptiert.

## Aktueller Evidenzstand

Der vollständige v0.1-Demonstrator erfüllt die Referenz-/Refinement-Gates und stützt C05. Der anschließende harte Vergleich gegen etablierte numerische Analysis, V&V/Credibility und Simulationsphilosophie spricht jedoch gegen die starke C06-Fassung, nach der die Trias neue numerische Validierungsfragen erzeugt.

Zur Entscheidung steht daher C06-R: ein schwächerer Integrations-/Mapping-Claim. Siehe `claims/claim_06.md` und `demonstrator/c06_comparison_v0_1.md`.

## Abhängigkeitslogik

C01 → C02 → C03 → C04 → D005 → D006 → D007 → Full v0.1 run → C05/D008 → C06-R review → optional minimaler AI-for-Science/ML-Test.

Die Reihenfolge kann revidiert werden, wenn die Evidenzprüfung eine frühere Annahme problematisch macht.