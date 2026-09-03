# Current Status

## Phase

**Descriptive Trias / Edge Semantics + Evidence Ledger v0.1 Review**

Mit D024 wurde C08-D-R als Working Claim akzeptiert. Die Mainline prüft damit nicht mehr eine neue V&V-/Provenance-Theorie, sondern eine deskriptive wissenschaftsphilosophische Profilgrammatik über drei relationsspezifische Evidenzbereiche zwischen Zielsystem, Theorie und computational realization.

## Akzeptierte Entscheidungen

- **D001–D004:** Claim-/Scope-Fundament, synthetisches Zielsystem, Sundman, Bewertungsdimensionen.
- **D005–D008:** numerischer Figure-eight-Demonstrator und C05 abgeschlossen/akzeptiert.
- **D009:** starke Trias-Neuheitsbehauptung gegenüber V&V verworfen.
- **D010–D014:** ML-Provenance-Zweig v0.1 ausgeführt (`INCONCLUSIVE_LEARNER_ERROR`), v0.2 technisch vorbereitet und pausiert.
- **D015–D016:** Directed Trias als Arbeitsrevision; starke Lucarini-Neuheitsfassung verworfen, moderate Bridge behalten.
- **D017–D020:** inverser Lorenz/SINDy-Zweig vorregistriert, implementiert und als `INFORMATIVE_NEGATIVE` akzeptiert.
- **D021:** C06-R2 als konservative Fallback-Boundary akzeptiert.
- **D022:** Autorenintention als deskriptive `R/T/C`-Theorie präzisiert.
- **D023:** Literatur-Stress-Test akzeptiert; starke Einzelneuheitsclaims/Nullsummen-Tradeoff verworfen; Profile Test freigegeben.
- **D024:** C08-D-R als Working Claim akzeptiert; Kanten sind claim-/facet-/use-/evidence-/scope-relativ und nicht standardmäßig transitiv.

## Aktueller Working Claim C08-D-R

> In Computational Science und AI for Science kann der Evidenzstatus eines Modells deskriptiv in drei relationsspezifische Bereiche zerlegt werden: Zielsystem–Theorie (`R–T`), Theorie–computational realization (`T–C`) und computational realization–Zielsystem (`C–R`). Dieselbe globale Erfolgsbezeichnung oder Performancemetrik kann je nach wissenschaftlichem Workflow Evidenz für unterschiedliche dieser Relationen darstellen; Evidenz auf einer Relation etabliert die anderen daher nicht automatisch. Ein relationales Profil macht diese Differenz explizit, sofern jeder Kantenstatus an einen konkreten wissenschaftlichen Claim/Facet, einen Use Case, Evidenz und Scope gebunden wird.

Evidenzstatus:

```text
analytische Diskriminationsleistung: POSITIVE
praktische Nutzer-/Entscheidungsnützlichkeit: UNTESTED
starker Literatur-Novelty-Nachweis: UNVERIFIED
```

## Edge Semantics + Evidence Ledger v0.1

**Status: PENDING REVIEW.**

Das neue Dokument `theory/edge_semantics_evidence_ledger_v0_1.md` präzisiert:

```text
R = intendiertes Zielsystem, typisiert als REAL / SYNTHETIC / HYBRID
T = expliziter theoretischer/formaler/mechanistischer Claiminhalt
C = konkrete computational realization
```

### R–T Facets

```text
RT_EMPIRICAL
RT_MECHANISTIC
RT_EXPLANATORY
RT_SCOPE
RT_STRUCTURAL
```

### T–C Facets

```text
TC_TRACTABILITY
TC_FIDELITY
TC_CONVERGENCE
TC_STABILITY
TC_STRUCTURE
TC_RESOLVABILITY
TC_SURROGATE
```

### C–R Facets

```text
CR_PREDICTION
CR_CALIBRATION
CR_DISTRIBUTION
CR_EXTERNAL
CR_SIM2REAL
CR_ROBUSTNESS
CR_REPRESENTATION
```

Jeder Ledger-Eintrag bindet einen Status an `Use Case + Claim/Facet + Evidence + Scope`.

Statussprache:

```text
ESTABLISHED
PARTIAL
UNCERTAIN
UNTESTED
NOT_APPLICABLE
```

## Zentrale neue Präzisierung: keine automatische Transitivität

Default:

```text
A_RT + A_TC  -/->  A_CR
A_TC + A_CR  -/->  A_RT
A_RT + A_CR  -/->  A_TC
```

Evidenz darf zwischen Kanten nur über einen expliziten **Bridge-Claim** übertragen werden. Dieser muss Source-Edge, Target-Edge, Claim, Evidenz, zusätzliche Prämissen und Scope dokumentieren.

Beispiel Synthetic Surrogate:

```text
hohe Teacher-Treue -> direkte T-C-Evidenz
                      nicht automatisch C-R_real-Evidenz
```

Eine Bridge zu `C-R_real` benötigt mindestens eine separat gestützte Simulator/Theorie-Realitätsbeziehung, kompatiblen Scope und einen kontrollierten Fehlertransfer.

## Minimaler Ledger

Pflichtfelder:

```text
case_id
target_id / target_type
theory_id
computation_id
use_case
edge
facet
claim
evidence
evidence_mode
status
scope
dependencies
non_implications
```

Damit wird die Trias nicht zu drei Scores. Die Dreiecksstruktur ist die Topologie; die konkrete Semantik wird durch claimspezifische Ledger-Einträge getragen.

## Strategischer Freeze

Keine neue numerische Mainline. ML-v0.2 und inverse v0.2 bleiben pausiert. C06-R2 bleibt Fallback, falls die präzisierte Profilgrammatik den letzten Novelty-Test nicht übersteht.

## Nächste Entscheidung

Empfehlung: **Edge Semantics + Evidence Ledger v0.1 akzeptieren.**

Bei `GO` wird das Ledger eingefroren. Danach folgt ausschließlich ein `Relational-Profile Novelty Audit v0.1`, der genau die präzisierte Struktur — einschließlich Target-Typen, Facets, Nicht-Transitivität und Bridge-Claims — gegen die stärksten direkten Literaturkandidaten prüft. Erst danach wird der Paper-Hauptclaim finalisiert.

## Projektkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen detaillierten Kooperationsstand als PDF plus LaTeX-Quelle neu synthetisieren; Descriptive Trias, C08-D-R, Edge Semantics, negative/inconclusive Resultate und pausierte Branches werden berücksichtigt.
