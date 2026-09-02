# Claim Registry

Das Register enthält die wissenschaftlich relevanten Claims und Demonstratorentscheidungen des Projekts in Abhängigkeitsreihenfolge.

| ID | Kurzbezeichnung | Status | Evidenzstatus | Entscheidung |
|---|---|---|---|---|
| C01 | Diagnostischer Mehrwert der Trias | ACCEPTED / UNDER TEST | Reiner Solverfall stützt nur schwache integrative Fassung; Directed-Trias-Schärfung wird geprüft | D001 |
| C02 | Synthetisches Zielsystem als Realitäts-Pol | ACCEPTED | Begrifflich anschlussfähig; konkrete Trias-Rolle ist methodologische Setzung | D002 |
| C03 | Sundmans konvergente Reihenlösung und praktische Traktabilität | ACCEPTED | mathematisch-historischer Kern gut gestützt; methodologische Lesart projektintern | D003 |
| C04 | Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ wissenschaftliche Nutzbarkeit | ACCEPTED | numerisch gut gestützt; Identifizierbarkeit wird als neue querliegende Auditdimension geprüft | D004 |
| DMO | Numerischer Minimaldemonstrator | ACCEPTED / COMPLETE | Scope D005/D006, Skeleton D007, Full Run abgeschlossen | D005–D007 |
| C05 | Implementierungswahl kann wissenschaftlich relevante Profile erzeugen | ACCEPTED | Full numerical v0.1 run stützt moderate zweckrelative Fassung | D008 |
| C06-R | Integrations-/Provenance-Wert des Trias-Audits | ACCEPTED / UNDER REFINEMENT | starke Neuheitsform im Solverfall verworfen; Directed-Trias-Bridge könnte integrative Fassung schärfen | D009 |
| AFS-DMO | Minimaler ML/AI-for-Science-Provenance-Demonstrator | ACCEPTED | v0.1 ausgeführt; v0.2 technisch vorbereitet | D010 |
| ML-IC-v0.1 | ML Implementation Contract v0.1 | ACCEPTED | technische Vorregistrierung eingefroren | D011 |
| ML-SKEL-v0.1 | ML Dataset-/Training-Skeleton v0.1 | ACCEPTED | technische Tests/Smoke bestanden | D012 |
| ML-RUN-v0.1 | Wissenschaftlicher ML-Provenance-Run | COMPLETE / INCONCLUSIVE | Reference gate bestanden; Learner-Resolvability klar verletzt | D013 |
| C07 | ursprünglicher ML-Provenance-Claim-Kandidat | NOT ASSESSABLE | v0.1 entscheidet den Claim wegen fehlender Signalauflösung nicht | — |
| ML-v0.2 | Resolvability Repair | ACCEPTED / PAUSED | Splitgeometrie + gemeinsamer Target-Scaler genehmigt; Full Run strategisch pausiert | D013–D014 |
| ML-IC-v0.2 | Implementation Contract v0.2 | ACCEPTED | v0.2-Reparatur eingefroren | D014 |
| ML-SKEL-v0.2 | v0.2 Dataset-/Training-Skeleton | READY / PAUSED | technische Tests bestanden; Full Run vorerst nicht gestartet | — |
| DT-v0.1 | Directed Trias: gerichtete nichtinvertierbare Transformationen | WORKING THEORY REVISION | Synthese aus C03/C05/C06-R + inverse Identifiability-Literatur; Novelty ungeklärt | — |
| C07-L | Operative Äquivalenz ≠ theoretische Identifizierbarkeit | PENDING REVIEW | Zhai–Lucarini–Lai stützt konkreten chaotischen Equation-Discovery-Fall; Vergleich mit Identifiability/Equifinality ausstehend | — |

## Arbeitsregel

Ein wissenschaftlicher Claim erhält den Status `ACCEPTED`, wenn die vorgeschlagene Arbeitsfassung im Forschungsdialog durch `GO` bestätigt wurde. `ACCEPTED` bedeutet nicht endgültig bewiesen, sondern als aktuelle Forschungsgrundlage akzeptiert.

## Aktueller Evidenzstand

Der numerische Demonstrator stützt C05, nicht aber eine starke Originalitätsbehauptung gegenüber V&V. ML v0.1 blieb wegen fehlender Learner-Resolvability unentschieden.

Die neue Directed-Trias-Arbeitsrevision verschiebt den Fokus von drei statischen Polen auf gerichtete operative Transformationen. Forward-Fälle (`T -> C -> R_hat`) werden durch Sundman und den Solververgleich repräsentiert; die inverse Richtung (`R -> C_observation/preprocessing -> C_inference -> T_hat`) wird nun mit Zhai–Lucarini–Lai und etablierter Identifiability-/Equifinality-Literatur geprüft.

Wichtig: Nichtidentifizierbarkeit, Observability und Equifinality sind etablierte Konzepte. C07-L kann nur dann Trias-relevant werden, wenn die gemeinsame Auditierung von Forward- und Inverse-Provenance eine zusätzliche Integrations-/Zuordnungsleistung zeigt.

## Abhängigkeitslogik

```text
C01–C06-R
-> ML v0.1 inconclusive
-> D013/D014 v0.2 vorbereitet
-> Directed Trias working revision
-> C07-L Claim-to-Evidence + comparator audit
-> moderate C07-L GO decision
-> minimal inverse-direction demonstrator
-> decision: resume ML v0.2 vs secondary vs replace
-> renewed originality test
```

## Dialogkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen Projektstand als ausführliches Kooperationsbriefing neu synthetisieren und als PDF plus LaTeX-Quelle erzeugen; Directed Trias und C07-L werden berücksichtigt.
