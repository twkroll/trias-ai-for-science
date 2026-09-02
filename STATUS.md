# Current Status

## Phase

**Directed Trias / Comparator Audit Complete / C06-R2 Review**

Der numerische Drei-Körper-Demonstrator ist abgeschlossen. Der ML-v0.1-Provenance-Zweig blieb `INCONCLUSIVE_LEARNER_ERROR`; ML v0.2 ist technisch vorbereitet, aber pausiert. Der inverse Lorenz/SINDy-Full-Run wurde nach D018/D019 ausgeführt und mit D020 als vorregistrierter wissenschaftlicher Befund `INFORMATIVE_NEGATIVE` akzeptiert. Der verpflichtende Comparator-Audit auf genau diesem negativen Resultat ist nun abgeschlossen.

## Akzeptierte Entscheidungen

- **D001–D004:** Claim-/Scope-Fundament, synthetisches Zielsystem, Sundman, Bewertungsdimensionen.
- **D005–D008:** numerischer Figure-eight-Demonstrator und C05 abgeschlossen/akzeptiert.
- **D009:** starke Trias-Neuheitsbehauptung gegenüber V&V verworfen; C06-R = Integrations-/Provenance-Fassung.
- **D010–D014:** ML-Provenance-Zweig v0.1 ausgeführt (`INCONCLUSIVE_LEARNER_ERROR`), v0.2 technisch vorbereitet.
- **D015:** Directed Trias als Arbeitsrevision akzeptiert; ML-v0.2-Full-Run pausiert.
- **D016:** starke C07-L-Neuheitsfassung verworfen; C07-L-R als moderate Equation-Discovery-Bridge akzeptiert.
- **D017:** Minimal Inverse-Direction Demonstrator v0.1 akzeptiert und eingefroren.
- **D018:** Inverse-Direction Implementation Contract v0.1 akzeptiert und eingefroren.
- **D019:** Inverse-Direction Code Skeleton v0.1 akzeptiert.
- **D020:** Inverse Full Run v0.1 als `INFORMATIVE_NEGATIVE` akzeptiert; Seed-2-Einzelfall bleibt explorativ; kein post-hoc Tuning zur Erzeugung eines positiven Effekts.

## Directed Trias

```text
Forward: T -> C_forward -> R_hat
Inverse: R -> C_obs -> D -> C_pre -> C_infer -> T_hat
```

Die drei Pole bleiben funktionale Rollen; Daten sind Zwischenartefakte. Identifizierbarkeit ist eine querliegende Auditdimension, keine neue Stufe der sechs-stufigen Lösungsleiter.

## Inverser Full Run v0.1

**Status:** COMPLETE / ACCEPTED SCIENTIFIC RESULT — D020  
**Classification:** `INFORMATIVE_NEGATIVE`

G1–G3 bestehen. P0 rekonstruiert den exakten Lorenz-Support. Unter 20% zufälliger punktweiser Missingness entsteht:

```text
linear reconstruction: structural perturbation 1/3 seeds
cubic reconstruction:  structural perturbation 0/3 seeds
pre-registered robust threshold: >=2/3
```

Der lineare Seed-2-Fall mit zusätzlichem konstanten `dz/dt`-Term und bestandener operativer Äquivalenz bleibt explorativ und wird nicht als positiver Haupteffekt gewertet.

Details: [`demonstrator/inverse_full_run_v0_1_results.md`](demonstrator/inverse_full_run_v0_1_results.md).

## Comparator Audit

**Status:** COMPLETE.

Der negative inverse Befund wurde gegen folgende Rahmen geprüft:

1. System Identification / SINDy robustness / structural error;
2. structural/practical identifiability und observability;
3. Modeling & Simulation V&V / Scientific-ML credibility;
4. Workflow/Data Provenance einschließlich W3C PROV;
5. Claims–Arguments–Evidence / Assurance Cases als zusätzlicher Stress-Comparator;
6. Directed Trias.

### Ergebnis

Die bisherigen Demonstratoren zeigen **keine eigenständige neue Fehler-, Validierungs-, Provenance- oder Identifiability-Kategorie** der Trias. Praktisch alle wesentlichen Diagnosen lassen sich mit einer Kombination etablierter Frameworks formulieren.

Auch zwei mögliche Restclaims sind stark vorbelastet:

- `gerichtete Provenance` ist Kern bestehender Provenance-Modelle;
- `welche Evidenz stützt welchen Claim?` ist Kern von Assurance-Case-/CAE-/GSN-Ansätzen.

Der verbleibende mögliche Wert der Directed Trias ist daher enger: eine kompakte fachübergreifende **konzeptionelle Synthese/Audit-Linse**, die Forward- und Inverse-Fälle in derselben Sprache von Zielsystem, Theorie, operativer Vermittlung, Übergang und zweckrelativer Rechtfertigung ordnet.

Details: [`literature/inverse_negative_result_comparator_audit_v0_1.md`](literature/inverse_negative_result_comparator_audit_v0_1.md).

## Aktueller Claim-Kandidat

### C06-R2
**Status:** PENDING REVIEW

> Die bisherigen Drei-Körper-, ML- und inversen Equation-Discovery-Fälle zeigen keine eigenständige neue Fehler-, Validierungs-, Provenance- oder Identifiability-Kategorie der Trias gegenüber starken etablierten Vergleichsrahmen. Der verbleibende mögliche Beitrag der Directed Trias ist eine kompakte fachübergreifende Synthese, die Forward- und Inverse-Transformationen zwischen Zielsystem, Theorie und operativer Vermittlung in einer gemeinsamen Audit-Sprache ordnet und sichtbar macht, auf welches epistemische Objekt sich eine konkrete Rechtfertigung bezieht. Diese Leistung ist als konzeptionelle Integrations- und Kommunikationsfunktion zu bewerten und nicht als neue mathematische oder technische Credibility-Theorie.

Details: [`claims/claim_06_revised_v2.md`](claims/claim_06_revised_v2.md).

## Strategische Empfehlung

**Paper-Pivot statt weiterer Experiment-Tuning-Schleifen.**

Der Mainline-Pfad sollte vorerst keine neuen Experimente starten. Empfohlen ist ein `Paper Contribution Boundary + Outline v0.1` mit:

```text
1. exakter Hauptclaim + Non-Claims
2. Comparator-Coverage-Matrix
3. Sundman als formal-vs-operational case
4. Figure-eight als forward operationalization case
5. inverse Lorenz/SINDy als pre-registered negative inverse case
6. ML v0.1 als inconclusive provenance/learner-resolvability case
7. klare Entscheidung, was Haupttext vs Appendix ist
8. realistisches Paperformat: conceptual/methodological synthesis, nicht neue V&V-Theorie
```

ML v0.2 und ein möglicher inverse v0.2 bleiben archiviert/pausiert. Sie dürfen später als eigenständige empirische Projekte wieder aufgenommen werden, aber nicht als Rettungsversuch für Trias-Novelty.

## Nächste Entscheidung

Zu entscheiden ist, ob **C06-R2** akzeptiert und der Mainline-Pfad auf die Paper-Ausarbeitung als konzeptionelle Synthese umgestellt wird.

Bei `GO` wird C06-R2 eingefroren und als nächster Schritt ausschließlich `Paper Contribution Boundary + Outline v0.1` ausgearbeitet. Noch kein neues Experiment.

## Projektkommandos

- `GO`: aktuelle Empfehlung akzeptieren, dokumentieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen detaillierten Kooperationsstand als PDF plus LaTeX-Quelle neu synthetisieren; Directed Trias, C06-R2-Status, C07-L-R, negative/inconclusive Resultate und pausierte Branches werden berücksichtigt.
