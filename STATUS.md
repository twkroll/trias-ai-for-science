# Current Status

## Phase

**Directed Trias / C07-L-R Claim Review**

Das Claim-and-Scope-Fundament und der numerische Drei-Körper-Demonstrator sind abgeschlossen. C05 ist akzeptiert; C06-R beschränkt den derzeit belegbaren Trias-Mehrwert auf eine Integrations-/Provenance-Funktion. Der ursprüngliche ML-Provenance-Test v0.1 blieb `INCONCLUSIVE_LEARNER_ERROR`; die v0.2-Resolvability-Reparatur ist technisch vorbereitet, ihr wissenschaftlicher Full Run jedoch strategisch pausiert. Der aktuelle Fokus liegt auf der inversen Richtung `target/observation -> data -> inference -> theory`.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol.
- **C03 / D003:** Sundman als konvergente, praktisch extrem ineffiziente Reihenrepräsentation; formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.
- **C04 / D004:** Konvergenz, operative Machbarkeit, Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt; die sechs-stufige Lösungsleiter bleibt erhalten.
- **Numerischer Demonstrator / D005–D007:** Figure-eight + DOP853 + RK4 + Velocity-Verlet, implementiert, getestet und vollständig ausgeführt.
- **C05 / D008:** verschiedene numerische Operationalisierungen erzeugen use-case-relative Fehler-/Strukturprofile.
- **C06-R / D009:** starke Neuheitsbehauptung gegenüber V&V verworfen; verbleibender Mehrwert ist integrative Provenance/Mapping.
- **AFS-DMO / D010:** minimaler ML-Provenance-Test akzeptiert.
- **ML-IC v0.1 / D011:** Dataset-, Netzwerk-, Optimierungs-, Gate-, Rollout- und Scope-Entscheidungen eingefroren.
- **ML-SKEL v0.1 / D012:** getesteter ML-Skeleton akzeptiert.
- **ML v0.1 Review + v0.2 Direction / D013:** v0.1 endgültig als `INCONCLUSIVE_LEARNER_ERROR`; C07 unentschieden; v0.2 als Resolvability-Reparatur zugelassen.
- **ML-IC v0.2 / D014:** phase-stratifizierter Split und gemeinsamer teacher-unabhängiger Target-Scaler eingefroren.
- **Directed Trias / D015:** gerichtete Trias als Arbeitsrevision für den nächsten Novelty-Test akzeptiert; ML-v0.2-Full-Run pausiert; C07-L muss zuerst gegen starke Comparatoren geprüft werden.

## Directed Trias — aktueller Arbeitsrahmen

Die drei Pole bleiben funktionale Rollen. Methodologisch wird jetzt stärker zwischen gerichteten Transformationen unterschieden:

```text
Forward: T -> C_forward -> R_hat
Inverse: R -> C_obs -> D -> C_pre -> C_infer -> T_hat
```

`C` darf für Auditzwecke in Observation/Datafication, Preprocessing/Reconstruction, Inference, Forward-Simulation, ML und Comparison/Credibility zerlegt werden. Daten sind Zwischenartefakte, kein vierter ontologischer Pol.

Die sechs-stufige Lösungsleiter bleibt unverändert. Theoretische Identifizierbarkeit wird als querliegende Auditdimension behandelt.

Details: [`theory/directed_trias_v0_1.md`](theory/directed_trias_v0_1.md).

## C07-L Comparator Audit

**Status:** COMPLETE FOR CLAIM REVIEW.

Der Vergleich mit structural/practical identifiability, observability, equifinality/observational equivalence, System Identification mit structural error/near-identifiability, Equation-Discovery-Robustheit, wissenschaftsphilosophischer Underdetermination/Model Pluralism sowie SciML-V&V/Provenance ergibt:

1. Nichtidentifizierbarkeit, observational equivalence, Near-Equivalence und pipelineabhängige Inferenz sind **keine neuen Trias-Befunde**.
2. Besonders die ältere Near-Identifiability-/structural-error-Literatur ist ein starker Comparator für die Idee `strukturell verschieden, outputseitig nahe äquivalent`.
3. Zhai–Lucarini–Lai bleibt als aktueller, klarer chaotischer Equation-Discovery-Fall wissenschaftlich wertvoll: stark verschiedene inferierte ODEs können bei ausgewählten Langzeit-/Koopman-Eigenschaften ähnlich bleiben.
4. Der verbleibende mögliche Trias-Beitrag ist ausschließlich eine **gemeinsame richtungssensitive Audit-Grammatik**, die etablierte Forward- und Inverse-Probleme zusammenführt und explizit markiert, welches epistemische Objekt an welchem Übergang gerechtfertigt wird.
5. Auch dieser Integrationsclaim ist noch nicht bewiesen; moderne SciML-V&V- und Provenance-Frameworks sind starke Comparatoren.

Details: [`literature/c07_l_comparator_audit.md`](literature/c07_l_comparator_audit.md).

## C07-L-R

**Status:** PENDING REVIEW.

Vorgeschlagene moderate Fassung:

> Bei datengetriebener Equation Discovery ist die Güte eines inferierten Modells mehrdimensional: strukturelle Übereinstimmung der Gleichungen, dynamisch-statistische Adäquanz und physikalische Interpretierbarkeit sind nicht gleichzusetzen. Zhai, Lucarini und Lai liefern einen konkreten chaotischen Fall, in dem unterschiedliche Beobachtungs-/Rekonstruktionsbedingungen zu strukturell verschiedenen inferierten ODEs führen, während ausgewählte Langzeit- und Koopman-Eigenschaften ähnlich bleiben. Für die Trias dient dieser Befund nicht als neue Identifiability-Theorie, sondern als inverser Testfall für die Hypothese, dass wissenschaftliche Rechtfertigung die Provenance und Richtung der Transformation `target/observation -> data -> inference -> theory` explizit auditieren sollte.

Details: [`claims/claim_07_lucarini_bridge_revised.md`](claims/claim_07_lucarini_bridge_revised.md).

## ML v0.2

**Status:** TECHNICALLY READY / SCIENTIFIC FULL RUN PAUSED.

D014 und der getestete v0.2-Skeleton bleiben gültig. Es findet derzeit kein Full Run statt. Nach dem inversen MVP wird entschieden, ob der Branch fortgesetzt, sekundär gestellt oder ersetzt wird.

## Nächste Entscheidung

Zu entscheiden ist, ob

1. die starke C07-L-Neuheitsfassung verworfen wird;
2. C07-L-R als moderate Arbeitsfassung akzeptiert wird;
3. als nächste Abhängigkeit ein **Minimal Inverse-Direction Demonstrator v0.1** spezifiziert wird, zunächst ohne Code.

## Projektkommando `PDF`

`PDF` erzeugt aus dem aktuellen Repository- und Entscheidungsstand ohne Rückfrage ein neues ausführliches Kooperationsbriefing als PDF plus LaTeX-Quelle. Details: `collaboration/PDF_WORKFLOW.md`.

## Arbeitsregel

`GO` = aktuelle wissenschaftliche Empfehlung akzeptieren, dokumentieren und zum nächsten abhängigen Schritt übergehen.

`PDF` = aktuellen detaillierten Kooperationsstand neu synthetisieren und als PDF bereitstellen.
