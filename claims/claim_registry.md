# Claim Registry

Das Register enthält die wissenschaftlich relevanten Claims und Demonstratorentscheidungen des Projekts in Abhängigkeitsreihenfolge.

| ID | Kurzbezeichnung | Status | Evidenzstatus | Entscheidung |
|---|---|---|---|---|
| C01 | Diagnostischer Mehrwert der Trias | ACCEPTED / UNDER TEST | Reiner Solverfall stützt nur schwache integrative Fassung; Directed-Trias-Schärfung wird geprüft | D001 |
| C02 | Synthetisches Zielsystem als Realitäts-Pol | ACCEPTED | begrifflich anschlussfähig; konkrete Trias-Rolle methodologische Setzung | D002 |
| C03 | Sundman / analytische vs operative Verfügbarkeit | ACCEPTED | mathematisch-historischer Kern gestützt | D003 |
| C04 | Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ Nutzbarkeit | ACCEPTED | Identifizierbarkeit als querliegende Auditdimension | D004 |
| DMO | Numerischer Minimaldemonstrator | ACCEPTED / COMPLETE | Figure-eight Full Run abgeschlossen | D005–D007 |
| C05 | Implementierungswahl erzeugt use-case-relative Profile | ACCEPTED | numerischer Full Run stützt moderate Fassung | D008 |
| C06-R | Integrations-/Provenance-Wert des Trias-Audits | ACCEPTED / UNDER REFINEMENT | starke Neuheitsform gegenüber V&V verworfen | D009 |
| AFS-DMO | ML-Provenance-Demonstrator | ACCEPTED | v0.1 ausgeführt; v0.2 technisch vorbereitet | D010 |
| ML-IC-v0.1 | ML Implementation Contract v0.1 | ACCEPTED | eingefroren | D011 |
| ML-SKEL-v0.1 | ML Skeleton v0.1 | ACCEPTED | technische Tests/Smoke bestanden | D012 |
| ML-RUN-v0.1 | ML Provenance Full Run | COMPLETE / INCONCLUSIVE | Learner-Resolvability verletzt | D013 |
| C07 | ursprünglicher ML-Provenance-Claim | NOT ASSESSABLE | v0.1 entscheidet den Claim nicht | — |
| ML-v0.2 | Resolvability Repair | ACCEPTED / PAUSED | technisch vorbereitet; Full Run strategisch pausiert | D013–D015 |
| ML-IC-v0.2 | ML Implementation Contract v0.2 | ACCEPTED | eingefroren | D014 |
| ML-SKEL-v0.2 | ML Skeleton v0.2 | READY / PAUSED | technische Tests bestanden | — |
| DT-v0.1 | Directed Trias | ACCEPTED AS WORKING REVISION | Forward/Inverse-Auditgrammatik; Originalität ungeklärt | D015 |
| C07-L | starke Lucarini-Bridge als Novelty | REJECTED / SUPERSEDED | Comparator-Audit zeigt etablierte Vorläufer | D016 |
| C07-L-R | moderate Equation-Discovery-Bridge | ACCEPTED AS WORKING CLAIM | externer Zhai–Lucarini–Lai-Fall; Trias-Anteil Integrationshypothese | D016 |
| INV-DMO-v0.1 | Minimal Inverse-Direction Demonstrator | ACCEPTED | Lorenz-63 + gepaarte Missingness/Reconstruction + feste SINDy-Pipeline | D017 |
| INV-IC-v0.1 | Inverse-Direction Implementation Contract | ACCEPTED | Reference-, Mask-, Reconstruction-, Derivative-, SINDy-, Gate- und Äquivalenzparameter eingefroren | D018 |
| INV-SKEL-v0.1 | Inverse-Direction Code Skeleton | ACCEPTED | gezielte Tests 6 passed; Smoke Run nichtwissenschaftlich | D019 |
| INV-RUN-v0.1 | Inverse scientific full run | COMPLETE / PENDING REVIEW | G1–G3 PASS; structural perturbation linear 1/3, cubic 0/3; pre-registered class `INFORMATIVE_NEGATIVE` | — |

## Aktueller Evidenzstand

Der numerische Demonstrator stützt C05, nicht aber eine starke Originalitätsbehauptung gegenüber V&V. Der ML-v0.1-Zweig blieb wegen fehlender Learner-Resolvability unentschieden und v0.2 bleibt pausiert.

D015–D016 verschieben den aktuellen Test auf die Directed Trias und die inverse Equation-Discovery-Kette. D017 friert den minimalen Lorenz/SINDy-Demonstrator ein; D018 friert dessen exakte technische Vorregistrierung ein; D019 akzeptiert den getesteten Code-Skeleton.

Der wissenschaftliche inverse Full Run wurde mit den eingefrorenen D018-Einstellungen ausgeführt. Reference-, Mask- und P0-Baseline-Gates bestehen. Der lineare Rekonstruktionspfad zeigt nur in 1/3 Seeds eine substantielle Structural-Perturbation, der kubische in 0/3. Damit wird die vorregistrierte 2/3-Robustheit nicht erreicht. Die durch D018 determinierte Resultatklasse ist daher `INFORMATIVE_NEGATIVE`. Ein einzelner linearer Seed-2-Fall erzeugt einen zusätzlichen konstanten Term in `dz/dt` bei gleichzeitig bestandener operativer Äquivalenz; er bleibt nach Vorregistrierung explorativ.

## Abhängigkeitslogik

```text
C01–C06-R
-> ML v0.1 inconclusive
-> D013/D014 ML v0.2 vorbereitet
-> D015 Directed Trias + ML-v0.2 pause
-> D016 C07-L-R
-> D017 inverse MVP spec
-> D018 inverse implementation contract
-> D019 inverse code skeleton
-> inverse scientific full run: INFORMATIVE_NEGATIVE / pending review
-> comparator audit on the negative result
-> decision: revise inverse branch vs resume ML v0.2 vs weaken/reposition originality claim
-> renewed originality test
```

## Dialogkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen Projektstand als ausführliches Kooperationsbriefing neu synthetisieren und als PDF plus LaTeX-Quelle erzeugen; Directed Trias, C07-L-R und der inverse MVP werden berücksichtigt.
