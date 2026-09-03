# Current Status

## Phase

**Descriptive Trias / Profile Test Complete / C08-D-R Review**

Mit D021 wurde C06-R2 akzeptiert und die experimentelle Mainline vorerst beendet. D022 präzisierte die ursprüngliche Autorenintention als primär deskriptive wissenschaftsphilosophische Theorie über `R/T/C` und deren paarweise Adäquanzrelationen. D023 akzeptiert den Literatur-Stress-Test und begrenzt die verbleibende Neuheitsfrage auf die feste relationale Profilstruktur. Der anschließende `Descriptive Trias Profile Test v0.1` ist nun abgeschlossen.

## Akzeptierte Entscheidungen

- **D001–D004:** Claim-/Scope-Fundament, synthetisches Zielsystem, Sundman, Bewertungsdimensionen.
- **D005–D008:** numerischer Figure-eight-Demonstrator und C05 abgeschlossen/akzeptiert.
- **D009:** starke Trias-Neuheitsbehauptung gegenüber V&V verworfen.
- **D010–D014:** ML-Provenance-Zweig v0.1 ausgeführt (`INCONCLUSIVE_LEARNER_ERROR`), v0.2 technisch vorbereitet und pausiert.
- **D015–D016:** Directed Trias als Arbeitsrevision; starke Lucarini-Neuheitsfassung verworfen, moderate Bridge behalten.
- **D017–D020:** inverser Lorenz/SINDy-Zweig vorregistriert, implementiert und als `INFORMATIVE_NEGATIVE` akzeptiert.
- **D021:** C06-R2 akzeptiert; bisheriger Restwert der Trias = konzeptionelle fachübergreifende Synthese/Audit-Linse.
- **D022:** Autorenintention präzisiert: deskriptive `R/T/C`-Theorie mit drei paarweisen Adäquanzrelationen statt neue V&V-/Provenance-Kategorie.
- **D023:** Literatur-Stress-Test akzeptiert; starke Einzelneuheitsclaims und notwendige Trade-off-These verworfen; Profile Test freigegeben; C08-D noch nicht automatisch akzeptiert.

## Descriptive Trias

```text
R = Realität / intendiertes Zielsystem
T = Theorie / formale, mechanistische oder erklärende Repräsentation
C = computational realization

A_RT = Evidenzstatus Zielsystem–Theorie
A_TC = Evidenzstatus Theorie–Berechnung
A_CR = Evidenzstatus Berechnung–Zielsystem
```

Die Trias ist zunächst deskriptiv. Es wird weder ein globaler Modellscore noch ein notwendiger Nullsummen-Trade-off behauptet.

Ein Modellprofil ist use-case- und claim-relativ:

```text
P(M;U) = [A_RT, A_TC, A_CR]
```

mit qualitativen Statuswerten `ESTABLISHED`, `PARTIAL`, `UNCERTAIN`, `UNTESTED`, `NOT_APPLICABLE`.

## Literatur-Stress-Test

**Status: ACCEPTED — D023.**

Klar etablierte Vorarbeit existiert für:

- computation als dritte wissenschaftliche Praxis;
- Modelle als Vermittler zwischen Theorie und Welt;
- Modelltradeoffs und Dreiecksmetaphern;
- adequacy-for-purpose;
- Prediction ohne Understanding;
- sim-to-real/synthetic-to-real gaps;
- physics-informed / Scientific ML.

Im v0.1-Stress-Test wurde jedoch kein kanonischer Direktanalog identifiziert, der `R/T/C` als Rollen und `R–T`, `T–C`, `C–R` als gemeinsame deskriptive Profilstruktur über Computational Science und AI for Science verwendet. Das bleibt ein Search Result, kein Originalitätsbeweis.

## Descriptive Trias Profile Test v0.1

**Status: COMPLETE / PENDING CLAIM DECISION.**

Sechs Falltypen wurden mit derselben Profilgrammatik analysiert:

```text
Sundman
Figure-eight / numerical solvers
Black-box ML on real data
ML surrogate on synthetic data
Physics-informed ML
Equation Discovery
```

### Positives Ergebnis

Der Test zeigt analytische Diskriminationsleistung. Insbesondere kann dieselbe Performancemetrik je nach Workflow Evidenz für unterschiedliche Kanten darstellen:

```text
synthetic teacher accuracy -> primär T-C
real held-out prediction   -> primär C-R
physics constraint         -> primär T-C
mechanistic adequacy       -> primär R-T
```

Damit unterscheidet das Profil Fälle, die globale Labels wie `accurate`, `validated`, `physics-informed` oder `excellent surrogate` epistemisch zusammenwerfen können.

Weitere positive Tests:

- Target-Wechsel von synthetischem zu realem Zielsystem verändert das Profil, obwohl Modell/Theorie gleich bleiben können.
- Zwei physics-informed Modelle mit gleicher T-C-Anbindung können sich in C-R-Evidenz unterscheiden.
- Figure-eight zeigt, dass sogar eine einzelne Kante use-case-/facet-spezifisch ist.

### Zentrale Einschränkung

Die drei Kanten sind selbst multidimensional. Ein Kantenstatus ist nur sinnvoll, wenn er an mindestens

```text
Use Case
Claim/Facet
Evidence
Scope
```

gebunden wird. Die Trias ist daher eine einfache Topologie, nicht drei skalare Qualitätsachsen.

Details: [`theory/descriptive_trias_profile_test_v0_1.md`](theory/descriptive_trias_profile_test_v0_1.md).

## Aktueller Claim-Kandidat

### C08-D-R — Descriptive Relational Profile

**Status: PENDING REVIEW.**

> In Computational Science und AI for Science kann der Evidenzstatus eines Modells deskriptiv in drei relationsspezifische Bereiche zerlegt werden: Zielsystem–Theorie (`R–T`), Theorie–computational realization (`T–C`) und computational realization–Zielsystem (`C–R`). Dieselbe globale Erfolgsbezeichnung oder Performancemetrik kann je nach wissenschaftlichem Workflow Evidenz für unterschiedliche dieser Relationen darstellen; Evidenz auf einer Relation etabliert die anderen daher nicht automatisch. Ein relationales Profil macht diese Differenz explizit, sofern jeder Kantenstatus an einen konkreten wissenschaftlichen Claim/Facet, einen Use Case, Evidenz und Scope gebunden wird. Der beanspruchte Beitrag ist diese gemeinsame deskriptive Profilgrammatik, nicht ein neuer Fehlertyp, eine notwendige Trade-off-Theorie oder eine normative Rangordnung von Modellen.

Evidenzstatus:

```text
analytische Diskriminationsleistung: POSITIVE
praktische Nutzer-/Entscheidungsnützlichkeit: UNTESTED
starker Novelty-Nachweis: UNVERIFIED
```

Details: [`claims/claim_08_descriptive_relational_profile.md`](claims/claim_08_descriptive_relational_profile.md).

## Strategischer Freeze

Keine neue numerische Mainline. ML-v0.2 und inverse v0.2 bleiben pausiert.

## Nächste Entscheidung

Empfehlung: **C08-D-R als Working Claim akzeptieren**, aber nicht als finalen Originalitätsclaim.

Bei `GO` wird C08-D-R eingefroren. Danach wird ausschließlich ein `Edge Semantics + Evidence Ledger v0.1` ausgearbeitet, das Claim-/Facet-Typen, zulässige Evidenz, Statusregeln, synthetische vs. reale Targets und use-case-spezifische Mehrfachprofile präzisiert. Erst danach erfolgt ein finaler Paper-/Novelty-Test.

## Projektkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen detaillierten Kooperationsstand als PDF plus LaTeX-Quelle neu synthetisieren; Descriptive Trias, C08-D-R, negative/inconclusive Resultate und pausierte Branches werden berücksichtigt.
