# Claim Registry

Das Register enthält die wissenschaftlich relevanten Claims und Demonstratorentscheidungen des Projekts in Abhängigkeitsreihenfolge.

| ID | Kurzbezeichnung | Status | Evidenzstatus | Entscheidung |
|---|---|---|---|---|
| C01 | Diagnostischer Mehrwert der Trias | ACCEPTED / UNDER TEST | Reiner Solverfall stützt nur schwache integrative Fassung; Directed-Trias-Schärfung wird geprüft | D001 |
| C02 | Synthetisches Zielsystem als Realitäts-Pol | ACCEPTED | Begrifflich anschlussfähig; konkrete Trias-Rolle ist methodologische Setzung | D002 |
| C03 | Sundmans konvergente Reihenlösung und praktische Traktabilität | ACCEPTED | mathematisch-historischer Kern gut gestützt; methodologische Lesart projektintern | D003 |
| C04 | Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ wissenschaftliche Nutzbarkeit | ACCEPTED | numerisch gut gestützt; Identifizierbarkeit ist querliegende Auditdimension | D004 |
| DMO | Numerischer Minimaldemonstrator | ACCEPTED / COMPLETE | Scope D005/D006, Skeleton D007, Full Run abgeschlossen | D005–D007 |
| C05 | Implementierungswahl kann wissenschaftlich relevante Profile erzeugen | ACCEPTED | Full numerical v0.1 run stützt moderate zweckrelative Fassung | D008 |
| C06-R | Integrations-/Provenance-Wert des Trias-Audits | ACCEPTED / UNDER REFINEMENT | starke Neuheitsform im Solverfall verworfen; Directed-Trias-Bridge prüft integrative Schärfung | D009 |
| AFS-DMO | Minimaler ML/AI-for-Science-Provenance-Demonstrator | ACCEPTED | v0.1 ausgeführt; v0.2 technisch vorbereitet | D010 |
| ML-IC-v0.1 | ML Implementation Contract v0.1 | ACCEPTED | technische Vorregistrierung eingefroren | D011 |
| ML-SKEL-v0.1 | ML Dataset-/Training-Skeleton v0.1 | ACCEPTED | technische Tests/Smoke bestanden | D012 |
| ML-RUN-v0.1 | Wissenschaftlicher ML-Provenance-Run | COMPLETE / INCONCLUSIVE | Reference gate bestanden; Learner-Resolvability klar verletzt | D013 |
| C07 | ursprünglicher ML-Provenance-Claim-Kandidat | NOT ASSESSABLE | v0.1 entscheidet den Claim wegen fehlender Signalauflösung nicht | — |
| ML-v0.2 | Resolvability Repair | ACCEPTED / PAUSED | Splitgeometrie + gemeinsamer Target-Scaler genehmigt; Full Run strategisch pausiert | D013–D015 |
| ML-IC-v0.2 | Implementation Contract v0.2 | ACCEPTED | v0.2-Reparatur eingefroren | D014 |
| ML-SKEL-v0.2 | v0.2 Dataset-/Training-Skeleton | READY / PAUSED | technische Tests bestanden; Full Run vorerst nicht gestartet | — |
| DT-v0.1 | Directed Trias: gerichtete epistemische Transformationen | ACCEPTED AS WORKING REVISION | Auditgrammatik für Forward/Inverse-Richtung; Originalität ausdrücklich ungeklärt | D015 |
| C07-L | starke Lucarini-Bridge / operative Äquivalenz als Novelty | REJECTED / SUPERSEDED | Comparator-Audit zeigt starke Überlappung mit Identifiability, observational equivalence, near-identifiability, system identification und underdetermination | D016 |
| C07-L-R | moderate Equation-Discovery-Bridge | ACCEPTED AS WORKING CLAIM | Zhai–Lucarini–Lai stützt konkreten Fall; Trias-Anteil bleibt Integrationshypothese | D016 |
| INV-DMO-v0.1 | Minimal Inverse-Direction Demonstrator | ACCEPTED | Lorenz-63 + paired missingness/reconstruction provenance + fixed SINDy pipeline eingefroren | D017 |
| INV-IC-v0.1 | Inverse-Direction Implementation Contract | PENDING REVIEW | exakte Reference-, Mask-, Reconstruction-, Derivative-, SINDy-, Gate- und Äquivalenzparameter vorregistriert; noch kein Code | — |

## Arbeitsregel

Ein wissenschaftlicher Claim erhält den Status `ACCEPTED`, wenn die vorgeschlagene Arbeitsfassung im Forschungsdialog durch `GO` bestätigt wurde. `ACCEPTED` bedeutet nicht endgültig bewiesen, sondern als aktuelle Forschungsgrundlage akzeptiert.

## Aktueller Evidenzstand

Der numerische Demonstrator stützt C05, nicht aber eine starke Originalitätsbehauptung gegenüber V&V. ML v0.1 blieb wegen fehlender Learner-Resolvability unentschieden.

D015 akzeptiert die Directed Trias als Arbeitsrevision und pausiert den ML-v0.2-Full-Run, ohne D014 oder den Skeleton zu widerrufen. D016 verwirft die starke C07-L-Neuheitsfassung und akzeptiert C07-L-R nur als moderate Bridge: Zhai–Lucarini–Lai ist externer Testfall; die Directed-Trias-Lesart bleibt eine zu prüfende Integrationshypothese.

D017 friert nun den minimalen inversen Lorenz/SINDy-Demonstrator ein. Der wissenschaftliche Kontrast ist `P0 complete` gegen gepaarte `P1 linear` / `P2 cubic` Rekonstruktion bei 20% Missingness und drei Mask-Seeds. Structural equation fidelity und dynamical/statistical adequacy werden getrennt bewertet; P0 muss zuerst ein Baseline-Recovery-Gate bestehen.

Der Inverse-Direction Implementation Contract v0.1 liegt zur Review vor. Vor dessen GO erfolgt keine Implementierung.

## Abhängigkeitslogik

```text
C01–C06-R
-> ML v0.1 inconclusive
-> D013/D014 v0.2 vorbereitet
-> D015 Directed Trias + ML-v0.2 pause
-> C07-L comparator audit COMPLETE
-> D016 C07-L strong rejected + C07-L-R accepted
-> D017 INV-DMO-v0.1 accepted
-> INV-IC-v0.1 review
-> inverse code skeleton + smoke
-> inverse scientific full run
-> comparator audit
-> decision: resume ML v0.2 vs secondary vs replace
-> renewed originality test
```

## Dialogkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen Projektstand als ausführliches Kooperationsbriefing neu synthetisieren und als PDF plus LaTeX-Quelle erzeugen; Directed Trias, C07-L-R und der inverse MVP werden berücksichtigt.
