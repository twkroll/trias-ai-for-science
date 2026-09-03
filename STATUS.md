# Current Status

## Phase

**Descriptive Trias / Literature Stress Test v0.1 Complete / C08-D Review**

Mit D021 wurde C06-R2 akzeptiert und die experimentelle Mainline vorerst beendet. Die anschließende Autorenklärung hat jedoch gezeigt, dass die ursprüngliche Trias-Idee bisher zu stark als V&V-/Provenance-Neuheitsclaim operationalisiert wurde. D022 präzisiert die Autorenintention als primär **deskriptive wissenschaftsphilosophische Theorie** über drei Rollen und drei paarweise Spannungs-/Adäquanzrelationen.

## Akzeptierte Entscheidungen

- **D001–D004:** Claim-/Scope-Fundament, synthetisches Zielsystem, Sundman, Bewertungsdimensionen.
- **D005–D008:** numerischer Figure-eight-Demonstrator und C05 abgeschlossen/akzeptiert.
- **D009:** starke Trias-Neuheitsbehauptung gegenüber V&V verworfen.
- **D010–D014:** ML-Provenance-Zweig v0.1 ausgeführt (`INCONCLUSIVE_LEARNER_ERROR`), v0.2 technisch vorbereitet und pausiert.
- **D015–D016:** Directed Trias als Arbeitsrevision; starke Lucarini-Neuheitsfassung verworfen, moderate Bridge behalten.
- **D017–D020:** inverser Lorenz/SINDy-Zweig vorregistriert, implementiert und als `INFORMATIVE_NEGATIVE` akzeptiert.
- **D021:** C06-R2 akzeptiert; bisheriger Restwert der Trias = konzeptionelle fachübergreifende Synthese/Audit-Linse.
- **D022:** Autorenintention präzisiert: Mainline prüft nun eine deskriptive `R/T/C`-Theorie mit drei paarweisen Adäquanzrelationen statt eine neue V&V-/Provenance-Kategorie.

## Descriptive Trias v0.1

**Status:** WORKING THEORY / PENDING CLAIM REVIEW.

Drei funktionale Rollen:

```text
R = Realität / intendiertes Zielsystem
T = Theorie / formale, mechanistische oder erklärende Repräsentation
C = Berechnung / computational realization
```

Primäre Analyse sind die drei Kanten:

```text
A_RT = Realität <-> Theorie
A_TC = Theorie <-> Berechnung
A_CR = Berechnung <-> Realität
```

Ein Modell wird nicht durch einen einzigen globalen Gütewert beschrieben, sondern zunächst durch ein relationales epistemisches Profil:

```text
P(M;U) = [A_RT, A_TC, A_CR]
```

mit qualitativen Status wie `ESTABLISHED`, `PARTIAL`, `UNCERTAIN`, `UNTESTED`, `NOT_APPLICABLE` relativ zu einem wissenschaftlichen Gebrauch `U`.

### Guardrails

- keine notwendige Nullsummen-Trade-off-These;
- keine Behauptung, dass hohe Adäquanz auf allen drei Kanten prinzipiell unmöglich ist;
- keine Behauptung, computation als dritte wissenschaftliche Praxis sei neu;
- keine Neuheitsbehauptung für einzelne bekannte Probleme wie sim2real oder prediction-vs-understanding.

Details: [`theory/descriptive_trias_v0_1.md`](theory/descriptive_trias_v0_1.md).

## Descriptive Trias Literature Stress Test v0.1

**Status:** COMPLETE / PENDING CLAIM DECISION.

### Harte negative Ergebnisse

Der Stress-Test verwirft starke Neuheitsfassungen für:

```text
- theory / experiment / computation als Dreiklang;
- computation als epistemisch eigenständige wissenschaftliche Praxis;
- models as mediators zwischen Theorie und Welt;
- T-C- und C-R-Spannungen als Einzelprobleme;
- Dreiecks-/Trade-off-Metaphern für wissenschaftliche Modelle;
- purpose-relative model adequacy;
- prediction != scientific understanding;
- synthetic-to-real / sim-to-real gap;
- Integration von Physics/Theory und Data in Scientific ML.
```

Besonders starke Comparatoren sind Humphreys/Winsberg/Lenhard für Computational Science, Morgan/Morrison für model mediation, Levins/Weisberg für Modelltradeoffs und Parker für adequacy-for-purpose.

### Verbleibender Kandidat

Im v0.1-Stress-Test wurde **kein klarer kanonischer Direktanalog** gefunden, der zugleich:

```text
1. R = target/reality, T = theory, C = computation setzt;
2. R-T, T-C und C-R als drei primäre Adäquanzrelationen verwendet;
3. ein konkretes Modell über diese drei Kanten profiliert;
4. die Darstellung zunächst deskriptiv statt normativ versteht;
5. denselben Rahmen auf Simulation und AI for Science anwendet.
```

Das ist kein Originalitätsbeweis, aber ein deutlich präziserer verbleibender Eigenbeitragskandidat.

Details: [`literature/descriptive_trias_literature_stress_test_v0_1.md`](literature/descriptive_trias_literature_stress_test_v0_1.md).

## Aktueller Claim-Kandidat

### C08-D — Descriptive Relational Profile Claim

**Status:** PENDING REVIEW.

> Für Computational Science und AI for Science ist es analytisch nützlich, drei verschiedene epistemische Adäquanzrelationen zu unterscheiden: `R–T`, `T–C` und `C–R`. Erfolg auf einer dieser Relationen impliziert nicht ohne zusätzliche Evidenz, dass die übrigen Relationen gleichermaßen etabliert sind. Ein Modell kann deshalb deskriptiv durch ein relationales epistemisches Profil über diese drei Kanten charakterisiert werden. Der beanspruchte Beitrag liegt in dieser festen gemeinsamen Profilstruktur, nicht in der Neuheit der zugrunde liegenden Einzelprobleme oder in einer notwendigen Trade-off-These.

Details: [`claims/claim_08_descriptive_relational_profile.md`](claims/claim_08_descriptive_relational_profile.md).

## Strategischer Freeze

Keine neuen numerischen Experimente als Mainline. ML v0.2 und inverse v0.2 bleiben pausiert. Der Paper-Pivot D021 bleibt als Fallback gültig, wird aber nicht endgültig eingefroren, bevor C08-D getestet ist.

## Nächste Entscheidung

Empfehlung: **Akzeptiere das Ergebnis des Literatur-Stress-Tests, aber akzeptiere C08-D noch nicht als etablierte Contribution.**

Bei `GO` wird als nächster Schritt ausschließlich ein **Descriptive Trias Profile Test v0.1** durchgeführt. Sechs Fälle werden mit demselben `A_RT/A_TC/A_CR`-Schema profiliert:

```text
1. Sundman
2. Figure-eight numerical solver
3. real-data black-box predictor
4. synthetic-data ML surrogate
5. physics-informed ML
6. equation discovery
```

Der Test soll prüfen, ob die Kantenprofilierung tatsächlich analytische Unterschiede sichtbar macht, die bei einer bloßen `theory / experiment / computation`-Taxonomie oder einem einzigen globalen Adequacy-Urteil verloren gehen.

## Projektkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen detaillierten Kooperationsstand als PDF plus LaTeX-Quelle neu synthetisieren; Descriptive Trias, D022, C08-D, bisherige positive/negative/inconclusive Resultate und pausierte Branches werden berücksichtigt.
