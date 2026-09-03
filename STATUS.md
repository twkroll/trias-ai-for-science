# Current Status

## Phase

**Descriptive Trias / Writing Goal W2 Complete / Genealogy-Dominance Review**

Mit D031 wurde die W1-Survival-Evaluation als `PASS` akzeptiert und Writing Goal W2 freigegeben. Section 2 — `Genealogy: From model credibility to the present problem` — ist nun als Manuskripttext inklusive Table 1 geschrieben und separat gegen das Survival-Kriterium S4 `genealogy dominates contribution` geprüft.

## Akzeptierte Entscheidungen

- **D001–D004:** Claim-/Scope-Fundament, synthetisches Zielsystem, Sundman, Bewertungsdimensionen.
- **D005–D008:** Figure-eight-Demonstrator abgeschlossen; C05 akzeptiert.
- **D009:** starke Trias-Neuheit gegenüber V&V verworfen.
- **D010–D014:** ML-Provenance v0.1 `INCONCLUSIVE_LEARNER_ERROR`; v0.2 technisch vorbereitet und pausiert.
- **D015–D016:** Directed Trias als Arbeitsrevision; starke Lucarini-Neuheitsfassung verworfen; moderate Equation-Discovery-Bridge behalten.
- **D017–D020:** inverser Lorenz/SINDy-Zweig vorregistriert und als `INFORMATIVE_NEGATIVE` akzeptiert.
- **D021:** C06-R2 als konservative Fallback-Boundary akzeptiert.
- **D022–D025:** Descriptive Trias, Profile Test, C08-D-R, Edge Semantics + Evidence Ledger.
- **D026:** direkte Topologie-Novelty verworfen; Schlesinger/Sargent als Genealogie akzeptiert.
- **D027:** `Paper Contribution Boundary v0.2` akzeptiert.
- **D028:** AI-for-Science Delta Audit akzeptiert; C08-D-R3 als Synthese-Working-Claim; Novelty-Suchstopp.
- **D029:** `Paper Claim + Outline Freeze v0.3` akzeptiert; `WRITE AS PERSPECTIVE / CONCEPTUAL SYNTHESIS`.
- **D030:** `Actual Manuscript Skeleton v0.1` akzeptiert; W1 / Section 4 freigegeben.
- **D031:** W1 = `PASS` akzeptiert; W2 Genealogie + Table 1 freigegeben.

## Manuskriptboundary P3

Die schreibbare Paperfassung bleibt eine genealogische Role-Profile-Synthese:

```text
R = claim-relative target/reference, REAL / SYNTHETIC / HYBRID
T = scientific theory/mechanism/explanation claim, PRESENT / PARTIAL / NONE_CLAIMED / INFERRED
C = concrete computational practice, numerical / learned / inferential / hybrid
```

Evidenz wird danach profiliert, welchen `R-T`, `T-C` oder `C-R` Claim sie im angegebenen Use Case und Scope stützt. Der Beitrag ist eine gemeinsame genealogische Lesart etablierter AI-for-Science-Erfolgsformen, keine neue V&V-, ML-, Identifiability- oder Discovery-Kategorie.

## W1 — Section 4

**Status: ACCEPTED / PASS — D031.**

Manuskripttext:

[`paper/manuscript_section_4_v0_1.md`](paper/manuscript_section_4_v0_1.md)

Stärkste konzeptionelle Träger:

```text
1. Equation Discovery — T as output of C
2. Synthetic Surrogate — explicit referent switch R_syn vs R_real
```

PIML und Black-box Prediction dienen stärker der cross-case Vergleichbarkeit.

## Writing Goal W2 — Section 2 Genealogy

**Status: COMPLETE / PENDING AUTHOR DECISION.**

Manuskripttext:

[`paper/manuscript_section_2_v0_1.md`](paper/manuscript_section_2_v0_1.md)

Section 2 macht nun explizit:

```text
Reality / Problem Entity
Conceptual Model
Computerized Model
```

sowie die starke strukturelle Entsprechung

```text
R-T ~ conceptual-model validity
T-C ~ computerized-model verification
C-R ~ operational validity / validation
```

als konstitutive Schlesinger/Sargent-Genealogie. Moderne V&V/VVUQ- und SciML-Credibility-Arbeiten verstärken diese Prior Art.

### Table 1

Die neue `Genealogy and contribution boundary`-Tabelle markiert für jedes Element:

```text
classical analogue
modern V&V/SciML status
novelty status
role in the paper
```

Die meisten Einzelbestandteile werden explizit als `not new` oder `strongly preceded` ausgewiesen. Als möglicher Rest bleibt nur die gemeinsame Rollen-/Evidenzsynthese über unterschiedlich gerichtete AI-Workflows.

## W2 Genealogy-Dominance Evaluation

Dokument:

[`paper/w2_genealogy_dominance_evaluation_v0_1.md`](paper/w2_genealogy_dominance_evaluation_v0_1.md)

**Vorläufige Klassifikation: PASS.**

```text
S4 genealogy dominates contribution = NOT TRIGGERED / ACTIVE RISK
paper mode                         = CONTINUE PERSPECTIVE
framework novelty                  = NO
synthesis contribution             = PLAUSIBLE / MODERATE
```

Begründung:

- Die Genealogie absorbiert die R/T/C-Topologie und fast alle klassischen Edge-Semantics vollständig.
- Sie absorbiert aber nicht den gesamten in W1 gezeigten Rollenwechsel.
- Equation Discovery (`R -> D -> C_infer -> T_hat`) bleibt der stärkste Fall für `epistemic roles rather than fixed lifecycle stages`.
- Synthetic Surrogate bleibt der stärkste Fall für einen cross-case Referentenwechsel.
- PIML und Black-box dürfen keine Novelty-Last tragen.

### Harte W2-Grenze

Section 2 soll im Endmanuskript kompakt bleiben (`ca. 750–950 Wörter + Table 1`) und darf nicht zu einer ausführlichen Geschichte von V&V wachsen. Die konzeptionelle Hauptlast muss bei Section 4 bleiben.

## Strategischer Freeze

- keine neue numerische Mainline;
- ML-v0.2 pausiert;
- inverse v0.2 pausiert;
- keine weitere freie Novelty-Suche;
- negative/inconclusive Resultate bleiben unverändert;
- neue konkrete Direktanaloge müssen berücksichtigt werden.

## Nächste Entscheidung

Empfehlung: **W2 = PASS akzeptieren und Perspective fortsetzen.**

Bei `GO` wird als nächste Abhängigkeit ausschließlich Writing Goal W3 ausgeführt:

> **Section 3 — From lifecycle stages to claim-relative epistemic roles.**

W3 schreibt nur die minimale Semantik, die Section 4 tatsächlich benötigt, und führt danach einen lokalen `notation-only / semantic-load`-Check gegen Survival-Kriterium S3 durch. Noch keine Introduction und keine neuen Experimente.

## Projektkommandos

- `GO`: akzeptiert W2 = PASS und startet W3 Section 3 + S3 semantic-load check.
- `PDF`: aktuellen detaillierten Kooperationsstand als PDF plus LaTeX-Quelle neu synthetisieren; D031, W1 PASS, W2 Genealogie + Dominance-Evaluation, P3, negative/inconclusive Resultate und pausierte Branches werden berücksichtigt.