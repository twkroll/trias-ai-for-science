# Claim Registry

Das Register enthält die wissenschaftlich relevanten Claims und Demonstratorentscheidungen des Projekts in Abhängigkeitsreihenfolge.

| ID | Kurzbezeichnung | Status | Evidenzstatus | Entscheidung |
|---|---|---|---|---|
| C01 | Diagnostischer Mehrwert der Trias | ACCEPTED / UNDER TEST | Reiner Solverfall stützt nur schwache integrative Fassung; AI-for-Science-Test bleibt offen | D001 |
| C02 | Synthetisches Zielsystem als Realitäts-Pol | ACCEPTED | Begrifflich gut anschlussfähig; konkrete Trias-Rolle ist methodologische Setzung | D002 |
| C03 | Sundmans konvergente Reihenlösung und praktische Traktabilität | ACCEPTED | Mathematisch-historischer Kern gut gestützt; methodologische Lesart projektintern | D003 |
| C04 | Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ wissenschaftliche Nutzbarkeit | ACCEPTED | Numerisch gut gestützt; Machbarkeit/Nutzbarkeit projektinterne Auditbegriffe | D004 |
| DMO | Numerischer Minimaldemonstrator | ACCEPTED / COMPLETE | Scope D005/D006, Skeleton D007, Full Run abgeschlossen | D005–D007 |
| C05 | Implementierungswahl kann wissenschaftlich relevante Profile erzeugen | ACCEPTED | Full numerical v0.1 run stützt moderate zweckrelative Fassung | D008 |
| C06-R | Integrations-/Provenance-Wert des Trias-Audits | ACCEPTED | Starke Neuheitsform im Solverfall verworfen; schwache integrative Fassung bleibt prüfbar | D009 |
| AFS-DMO | Minimaler ML/AI-for-Science-Provenance-Demonstrator | ACCEPTED | Testdesign eingefroren | D010 |
| ML-IC | ML Implementation Contract v0.1 | ACCEPTED | technische Vorregistrierung eingefroren | D011 |
| ML-SKEL | ML Dataset-/Training-Skeleton v0.1 | ACCEPTED | technische Tests/Smoke bestanden | D012 |
| ML-RUN-v0.1 | Wissenschaftlicher ML-Provenance-Run | COMPLETE / INCONCLUSIVE | Reference gate bestanden; Learner-Resolvability-Gate klar verletzt | — |
| C07 | ML-Provenance-Claim-Kandidat | NOT ASSESSABLE | Lernfehler ca. fünf Größenordnungen größer als Teacher-Differenz; v0.1 entscheidet den Claim nicht | — |

## Arbeitsregel

Ein Claim erhält den Status `ACCEPTED`, wenn die vorgeschlagene Arbeitsfassung im Forschungsdialog durch `GO` bestätigt wurde. `ACCEPTED` bedeutet **nicht endgültig bewiesen**, sondern als aktuelle Forschungsgrundlage akzeptiert.

## Aktueller Evidenzstand

Der ML Full Run v0.1 erfüllt Reference separation und paired initialization, scheitert aber am vorregistrierten Learner-Resolvability-Gate. Test-`D_teacher` beträgt etwa `1.30e-05`, während die medianen own-teacher Test-RMSEs beider Modellgruppen etwa `0.72` betragen. Die Provenance-Zerlegung ist technisch korrekt, doch der Modellfehler dominiert den Teacher-Beitrag um Milliardenfaktoren in der quadratischen Zerlegung.

Daher wird C07 aus v0.1 weder akzeptiert noch verworfen. Ein Follow-up muss separat preregistriert werden; innerhalb v0.1 findet kein Hyperparameter-/Architektur-/Split-Rescue statt.

## Abhängigkeitslogik

C01 → C02 → C03 → C04 → D005 → D006 → D007 → numerical full run → C05/D008 → C06-R/D009 → AFS-DMO/D010 → ML-IC/D011 → ML-SKEL/D012 → ML Full Run v0.1 (`INCONCLUSIVE_LEARNER_ERROR`) → v0.1 review → optional preregistered v0.2 → erneuter Originalitätstest → möglicher C07.

Die Reihenfolge kann revidiert werden, wenn die Evidenzprüfung eine frühere Annahme problematisch macht.