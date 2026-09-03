# Current Status

## Phase

**Descriptive Trias / Writing Goal W1 Complete / Section-4 Survival Review**

Mit D030 wurde das `Actual Manuscript Skeleton v0.1` akzeptiert und Writing Goal W1 freigegeben. Section 4 — `Four AI-for-Science Role Configurations` — ist nun als erster echter Manuskripttext geschrieben und separat gegen das vorab definierte PASS/SHORTEN/STOP-Gate geprüft.

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

## Manuskriptboundary P3

Die schreibbare Paperfassung bleibt eine genealogische Role-Profile-Synthese:

```text
R = claim-relative target/reference, REAL / SYNTHETIC / HYBRID
T = scientific theory/mechanism/explanation claim, PRESENT / PARTIAL / NONE_CLAIMED / INFERRED
C = concrete computational practice, numerical / learned / inferential / hybrid
```

Evidenz wird danach profiliert, welchen `R-T`, `T-C` oder `C-R` Claim sie im angegebenen Use Case und Scope stützt. Der Beitrag ist eine gemeinsame genealogische Lesart etablierter AI-for-Science-Erfolgsformen, keine neue V&V-, ML-, Identifiability- oder Discovery-Kategorie.

## Writing Goal W1 — Section 4

**Status: COMPLETE / PENDING AUTHOR DECISION.**

Manuskripttext:

[`paper/manuscript_section_4_v0_1.md`](paper/manuscript_section_4_v0_1.md)

Die vier geschriebenen Archetypen sind:

```text
4.1 predictive black-box
4.2 synthetic surrogate
4.3 physics-informed / hybrid ML
4.4 equation discovery
```

plus ein cross-case profile table.

Die Section verwendet in allen Fällen dieselbe Minimalgrammatik:

```text
R type / referent
T status
C role
principal evidence
supported relation
explicit non-implication
```

## W1 Survival Evaluation

Dokument:

[`paper/w1_section4_survival_evaluation_v0_1.md`](paper/w1_section4_survival_evaluation_v0_1.md)

**Vorläufige Klassifikation: PASS.**

Begründung:

```text
- gleiche Grammatik ohne ad-hoc Sonderregeln: PASS
- pro Fall mindestens ein präziser Evidenzunterschied: PASS
- weniger Mehrdeutigkeit als globale Labels: PASS
- Equation Discovery als Rollen-/Richtungswechsel: STRONG PASS
- S2 no residual compression: nicht ausgelöst, bleibt Hauptrisiko
- S3 notation-only: nicht ausgelöst
- S6 case incoherence: nicht ausgelöst
```

Der PASS gilt nur für eine Perspective / Conceptual Synthesis. Er stärkt P3 nicht zu einem Framework-Novelty-Claim.

## Gewichtung aus W1

```text
strongest conceptual carriers:
1. Equation Discovery — T as output of C
2. Synthetic surrogate — explicit referent switch R_syn vs R_real

supporting cross-case cases:
3. PIML — overlapping RT/TC/CR claims
4. Black-box prediction — T = NONE_CLAIMED, analytically clean but strongly preceded
```

Die W1-Fassung sollte im Endmanuskript voraussichtlich gestrafft werden; insbesondere wiederholte Boundary-Sätze können reduziert werden.

## Strategischer Freeze

- keine neue numerische Mainline;
- ML-v0.2 pausiert;
- inverse v0.2 pausiert;
- keine weitere freie Novelty-Suche;
- negative/inconclusive Resultate bleiben unverändert;
- neue konkrete Direktanaloge müssen berücksichtigt werden.

## Nächste Entscheidung

Empfehlung: **W1 = PASS akzeptieren und das Manuskript fortsetzen.**

Bei `GO` wird als nächste Abhängigkeit ausschließlich Writing Goal W2 ausgeführt:

> **Section 2 — Genealogy: From model credibility to the present problem + Table 1 genealogy/comparator mapping.**

Nach W2 folgt ein lokaler `genealogy-dominance`-Check gegen Survival-Kriterium S4. Noch keine Introduction und keine neuen Experimente.

## Projektkommandos

- `GO`: akzeptiert W1 = PASS und startet W2 Genealogy + Table 1.
- `PDF`: aktuellen detaillierten Kooperationsstand als PDF plus LaTeX-Quelle neu synthetisieren; D030, W1 Section 4, PASS-Evaluation, P3, Genealogie, negative/inconclusive Resultate und pausierte Branches werden berücksichtigt.