# Current Status

## Phase

**Claim and Scope / Directed Trias + inverse-identifiability bridge**

Das Claim-and-Scope-Fundament und der numerische Figure-eight-Demonstrator sind abgeschlossen. C05 ist akzeptiert; C06-R beschränkt den derzeit belegbaren Trias-Mehrwert auf Integrations-/Provenance-Funktion. ML v0.1 endete korrekt als `INCONCLUSIVE_LEARNER_ERROR`. Die v0.2-Resolvability-Reparatur ist als D014 akzeptiert und technisch implementiert, ihr wissenschaftlicher Full Run wird jedoch strategisch pausiert, während eine neue inverse Identifiability-/Equation-Discovery-Verbindung geprüft wird.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol.
- **C03 / D003:** Sundman: formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.
- **C04 / D004:** Konvergenz, Machbarkeit, Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt; die sechs-stufige Lösungsleiter bleibt erhalten.
- **Numerischer Demonstrator / D005–D007:** Figure-eight + DOP853 + RK4 + Velocity-Verlet.
- **C05 / D008:** verschiedene numerische Operationalisierungen erzeugen use-case-relative Fehler-/Strukturprofile.
- **C06-R / D009:** starke Neuheitsbehauptung gegenüber V&V verworfen; verbleibender Mehrwert ist integrative Provenance/Mapping.
- **AFS-DMO / D010, ML-IC v0.1 / D011, ML-SKEL / D012:** minimaler ML-Provenance-Test vorregistriert und implementiert.
- **D013:** ML v0.1 endgültig `INCONCLUSIVE_LEARNER_ERROR`; C07 bleibt unentschieden; v0.2 als separate Resolvability-Reparatur erlaubt.
- **D014:** v0.2 ändert ausschließlich phase-stratifizierten Blocksplit und gemeinsamen teacher-unabhängigen Target-Scaler; alle übrigen wissenschaftlichen Einstellungen bleiben eingefroren.

## Bestehende Evidenz

### Forward-Richtung

Sundman und der Figure-eight-Solverfall stützen zwei verschiedene Nicht-Implikationen:

```text
analytische Verfügbarkeit not=> operative Verfügbarkeit

gleiche Theorie not=> gleiches operatives epistemisches Profil
```

Der Solverfall allein liefert jedoch keinen starken Originalitätsnachweis gegenüber Standard-Numerik/V&V.

### ML v0.1

Reference separation und paired initialization bestanden, Learner resolvability scheiterte klar. Der Lernfehler lag ungefähr fünf Größenordnungen über der RK4-vs.-DOP853-Teacher-Differenz. Deshalb wurde keine Provenance-Interpretation zugelassen.

Details: [`demonstrator/ml_full_run_v0_1_results.md`](demonstrator/ml_full_run_v0_1_results.md).

## Neue theoretische Arbeitsrevision: Directed Trias

Die drei Pole `Realität/Zielsystem — Theorie — Berechnung/Umsetzung` bleiben funktionale Audit-Rollen. Neu wird geprüft, ob der methodologische Kern besser als System **gerichteter, im Allgemeinen nichtinvertierbarer epistemischer Transformationen** formuliert werden kann.

Forward:

```text
T -> C_forward -> R_hat
```

Inverse:

```text
R -> C_observation/preprocessing -> D -> C_inference -> T_hat
```

Der `C`-Pol wird damit nicht nur als Forward-Solver verstanden, sondern als Familie operativer Vermittlungen: Observation/Datafication, Preprocessing/Imputation, Inference, Forward-Simulation, ML-Surrogat und Vergleich/Validation.

Details: [`theory/directed_trias_v0_1.md`](theory/directed_trias_v0_1.md).

## Zhai–Lucarini–Lai-Bridge

Das Paper *Deficiency of equation-finding approach to data-driven modeling of dynamical systems* liefert einen Literaturfall für die inverse Richtung: unterschiedliche Missingness-/Rekonstruktionssituationen können zu stark unterschiedlichen inferierten Gleichungen führen, obwohl relevante chaotische Attraktor-, Lyapunov- und dominante Koopman-Eigenschaften ähnlich bleiben.

Projektintern motiviert dies die neue Unterscheidung:

```text
operative/dynamische Äquivalenz not=> theoretische Identität
```

und einen neuen Claim-Kandidaten **C07-L**. Dieser ist noch nicht akzeptiert.

Details:

- [`claims/claim_07_lucarini_bridge.md`](claims/claim_07_lucarini_bridge.md)
- [`literature/zhai_lucarini_lai_bridge_note.md`](literature/zhai_lucarini_lai_bridge_note.md)

## Identifizierbarkeit und Lösungsleiter

Theoretische Identifizierbarkeit wird **nicht** als siebte Stufe der Lösungsleiter eingeführt. Konsistent mit D004 wird sie als querliegende Auditdimension behandelt, gemeinsam mit Stabilität, Machbarkeit und Systemsensitivität.

Vor jeder Novelty-Aussage muss C07-L gegen etablierte Literatur zu structural/practical identifiability, observability, equifinality und system identification geprüft werden.

## Status ML v0.2

**D014 bleibt ACCEPTED; Skeleton technisch READY. Scientific full run: PAUSED.**

Die Pause widerruft keine frühere Entscheidung. Sie verhindert lediglich, dass wir den MLP-Zweig automatisch weiterrechnen, obwohl der neue inverse Identifiability-Fall möglicherweise einen stärkeren und direkter messbaren Test von C06-R bietet.

## Aktuelle Aufgabe

### C07-L Claim-to-Evidence + Comparator Audit
**Status:** IN PROGRESS / NEXT DECISION

Nächster Arbeitsschritt:

1. jede Klausel von C07-L auf Zhai–Lucarini–Lai oder projektinterne Interpretation abbilden;
2. structural identifiability, practical identifiability, observability und equifinality sauber von der neuen Bridge unterscheiden;
3. prüfen, ob die Directed-Trias-Fassung gegenüber diesen etablierten Konzepten tatsächlich Integrationsarbeit leistet;
4. erst danach eine moderate C07-L-Fassung zur `GO`-Entscheidung vorlegen;
5. danach einen minimalen inverse-direction Demonstrator spezifizieren, zunächst vorzugsweise als Lorenz/SINDy-Replikation statt als Erweiterung des Drei-Körper-Systems;
6. anschließend entscheiden, ob ML v0.2 fortgesetzt, sekundär gestellt oder ersetzt wird.

## Projektkommando `PDF`

`PDF` erzeugt aus dem jeweils aktuellen Projektstand ein neues ausführliches Kooperationsbriefing als PDF plus LaTeX-Quelle. Die Directed-Trias-/C07-L-Revision wird ab jetzt automatisch berücksichtigt.

## Arbeitsregel

`GO` = aktuelle wissenschaftliche Empfehlung akzeptieren, dokumentieren und zum nächsten abhängigen Schritt übergehen.

`PDF` = aktuellen detaillierten Kooperationsstand neu synthetisieren und als PDF bereitstellen.
