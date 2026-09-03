# Current Status

## Phase

**Descriptive Trias / Source-Hardened Manuscript v0.3 Complete / Journal-Selection Review**

Mit **D039** wurde W9 als `PASS_TO_SOURCE_INTEGRATION` akzeptiert. Writing Goal W10 wurde vollständig ausgeführt.

Aktuelle Paperbasis:

- [`paper/manuscript_source_hardened_v0_3.md`](paper/manuscript_source_hardened_v0_3.md)
- [`paper/references_v0_3.bib`](paper/references_v0_3.bib)
- [`paper/w10_source_hardening_evaluation_v0_1.md`](paper/w10_source_hardening_evaluation_v0_1.md)

Vorläufiges W10-Urteil:

```text
PASS_TO_JOURNAL_SELECTION
```

W10 ist **COMPLETE / PENDING AUTHOR DECISION**.

## Verbindliche Manuskriptboundary P3

Die Paperfassung bleibt eine genealogische Role-/Evidence-Synthese:

```text
R = claim-relative target/reference, REAL / SYNTHETIC / HYBRID
T = theory/mechanism/structure/explanation-level claim,
    PRESENT / PARTIAL / NONE_CLAIMED / INFERRED
C = concrete computational practice,
    numerical / learned / inferential / hybrid
```

Evidenz wird lokalisiert danach, welchen `R-T`, `T-C` oder `C-R` Claim sie im angegebenen Use Case und Scope direkt stützt.

Der Beitrag ist ausdrücklich **keine** neue V&V-/VVUQ-, Provenance-, Assurance-, Identifiability-/System-ID- oder Scientific-ML-Theorie, keine neue Dreieckstopologie und keine notwendige Trade-off-Theorie.

Verbleibender Beitrag:

> **moderate cross-domain synthesis / genealogically grounded evidence-localization vocabulary**.

Praktische Nützlichkeit bleibt `UNTESTED`.

## Akzeptierte Hauptentscheidungen

- **D001–D008:** Claim-/Scope-Fundament, Sundman, Figure-eight-Demonstrator und C05.
- **D009:** starke Trias-Neuheit gegenüber V&V verworfen.
- **D010–D014:** ML-Provenance v0.1 `INCONCLUSIVE_LEARNER_ERROR`; v0.2 pausiert.
- **D015–D020:** Directed-Trias-/Equation-Discovery-Branch; inverser Lorenz/SINDy-Run als `INFORMATIVE_NEGATIVE` akzeptiert.
- **D021–D028:** konservative Fallback-Boundary, Descriptive Trias, Edge Semantics, Schlesinger/Sargent-Genealogie und C08-D-R3.
- **D029–D036:** Perspective-/Conceptual-Synthesis-Paper, Manuskript-Skeleton und W1–W6 als `PASS`.
- **D037:** W7 `REVISE_BEFORE_MERGE` akzeptiert; W8 Editorial Synthesis ausgeführt.
- **D038:** W8 `PASS_TO_SOURCE_AUDIT` akzeptiert; W9 Quellen-Audit freigegeben.
- **D039:** W9 `PASS_TO_SOURCE_INTEGRATION` akzeptiert; W10 Source Hardening freigegeben und ausgeführt.

## Source-Hardened Manuscript v0.3

Empfohlener Titel bleibt:

> **From Model Credibility to AI for Science: Claim-Relative Evidence Across Target, Theory, and Computation**

Die v0.3-Fassung integriert die W9-Regeln vollständig und verwendet journal-neutrale Pandoc-/BibTeX-Citation-Keys.

Verbindlich integriert:

```text
W9-R1 Schlesinger model qualification vs Sargent conceptual-model validity
W9-R2 Zhai et al. = 2025 arXiv preprint only
W9-R3 Sundman = 1912; keine Termzahl-Overclaims
W9-R4 W3C PROV core terminology korrigiert
W9-R5 parameter identifiability vs model-form ambiguity getrennt
W9-R6 Naser als konkretes Framework, nicht Feldkonsens
W9-R7 ASME V&V 40 als domain-specific medical-device standard
W9-R8 Abwesenheitsclaim nur audit-relativ
```

Table 2 ist jetzt explizit nummeriert. Die Source-Hardening-Stufe führt keinen neuen Claim ein.

## Bibliographie

`paper/references_v0_3.bib` enthält die verifizierten Hauptanker für:

```text
Schlesinger / Sargent
NASA-STD-7009B / NASA-HDBK-7009B / ASME V&V 40
Jakeman et al. 2026
Naser 2025
Vinuesa et al. 2026
Karniadakis et al. 2021
Kramer et al. 2026
Zhai–Lucarini–Lai 2025 preprint
Sundman / Belorizky / Henkel / Chenciner / Musielak-Quarles
W3C PROV / CWLProv
Assurance Cases / GSN
Villaverde / Hadaegh-Bekey / SINDy / SINDy-PI
```

## Evidence-status discipline

Unverändert:

```text
Sundman        -> conceptual positive control
Figure-eight   -> positive / use-dependent V&V control
Lorenz/SINDy   -> INFORMATIVE_NEGATIVE
ML v0.1        -> INCONCLUSIVE_LEARNER_ERROR
```

Der inverse `linear / seed 2`-Fall bleibt explorativ. ML v0.1 unterstützt oder widerlegt den Teacher-Provenance-Claim nicht. ML-v0.2 und inverse v0.2 bleiben pausiert.

## W10 Source-Hardening Evaluation

Vorläufiger Befund:

```text
W9-R1…R8 integration          = PASS
citation consistency          = PASS
bibliography coverage         = PASS
publication-status accuracy   = PASS
project evidence preservation = STRONG PASS
P3 consistency                = PASS
blocking bibliographic gap    = NO
---------------------------------------
OVERALL                       = PASS_TO_JOURNAL_SELECTION
```

Keine weitere generische Konzept-, Novelty- oder Quellenrunde wird empfohlen.

## Strategischer Freeze

- keine neue numerische Mainline;
- ML-v0.2 pausiert;
- inverse v0.2 pausiert;
- keine weitere freie Novelty-Suche;
- negative/inconclusive Resultate bleiben unverändert;
- P3 wird durch Journalanpassung nicht gestärkt;
- journal-spezifische Anpassungen erst nach expliziter Venue-Entscheidung.

## Nächste Entscheidung

Empfehlung: **W10 = `PASS_TO_JOURNAL_SELECTION` akzeptieren.**

Danach Zieljournal auswählen. Realistische Optionen:

```text
A. European Journal for Philosophy of Science
B. Synthese
C. Minds and Machines
D. Studies in History and Philosophy of Science
E. Philosophy of Science (stretch)
```

Nach der Venue-Entscheidung folgt ausschließlich ein journal-spezifischer Style-/Submission-Pass.

## Projektkommandos

- `GO`: akzeptiert W10 = `PASS_TO_JOURNAL_SELECTION`; danach muss die Venue-Option entschieden werden, bevor der journal-spezifische Pass startet.
- `PDF`: aktuellen detaillierten Kooperationsstand als PDF plus LaTeX-Quelle neu synthetisieren; D039, Source-Hardened Manuscript v0.3, verified BibTeX, W10-Gate, P3 und alle negativen/inconclusive Resultate werden berücksichtigt.
