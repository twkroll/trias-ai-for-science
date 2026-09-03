# W4 — Contribution-Boundary / Residual-Compression Evaluation v0.1

**Status:** COMPLETE / PENDING AUTHOR DECISION  
**Stand:** 2026-09-03  
**Depends on:** D033, `paper/manuscript_section_7_v0_1.md`, W1–W3 PASS

## 1. Prüfziel

W4 ist der härteste verbleibende Boundary-Test. Geprüft wird, ob nach direktem Vergleich mit den angrenzenden Frameworks noch genügend eigenständige analytische Kompression für ein Standalone-Perspective-Paper übrigbleibt.

Lokale Survival-Kriterien:

```text
S2 — no residual explanatory compression
S3 — notation only
S5 — overclaim pressure
```

Erlaubte Urteile:

```text
PASS
SHORTEN
STOP
```

## 2. Ergebnis

**Klassifikation: PASS — eng, mit unveränderter Positionierung als Perspective / Conceptual Synthesis.**

W4 liefert keinen neuen technischen oder methodologischen Alleinstellungsanspruch. Der direkte Comparator-Vergleich lässt jedoch einen klar bestimmbaren Rest übrig, der bereits in W1–W3 tatsächlich verwendet wird:

> dieselbe claimspezifische Rollen-/Evidenzsemantik lokalisiert über mehrere fachlich verschiedene AI-for-Science-Workflows, welchen Referenten, welchen Theorieclaim und welche computational practice eine konkrete Evidenz verbindet.

Dieser Rest ist **moderate cross-domain explanatory compression**, nicht exklusive Diagnosefähigkeit.

## 3. Comparator-Ergebnis

| Comparator | Was er klar besser/tiefer leistet | Was die Trias nicht beanspruchen darf | Verbleibender Trias-Rest |
|---|---|---|---|
| V&V / VVUQ / model credibility | Verification, Validation, UQ, QoIs, acceptance, intended use, scope | neue Credibility-Kategorien oder neue drei Kanten | gemeinsame Rollenlesart über variable AI-Workflows |
| Provenance | vollständige Lineage, Activities, Entities, Derivation, Zwischenartefakte | neue Pipeline-/Richtungs-/Herkunftssemantik | epistemische Typisierung der claim-relevanten Artefakte |
| Assurance / CAE / GSN | explizite Claim–Argument–Evidence-Struktur | neue Bridge-/Claim-Evidence-Methode | domänenspezifische Minimaltypen R/T/C für wiederkehrende wissenschaftliche Claims |
| Identifiability / Observability / System ID | Recoverability, uniqueness, inverse robustness | neue Identifiability-/Equation-Discovery-Theorie | Einbettung inverser Claims in dieselbe Sprache wie Forward/Prediction/Surrogate |
| Philosophy of ML / P.E.D.U.D. | Prediction, Explanation, Discovery, Understanding, Decision; epistemische Ziele | Entdeckung pluraler ML-Erfolgsformen | Evidenzlokalisierung innerhalb dieser Erfolgsformen |
| SciML / PIML / surrogate credibility | konkrete hybride Methoden, teacher fidelity, physics constraints, validation, transfer | neue Hybrid-/Surrogate-/PIML-Kategorien | cross-case Vergleich von Referent, T-Status, C-Rolle und Nichtimplikation |

Die Tabelle zeigt zugleich die Grenze: **Kein einzelner technischer Bestandteil der Trias trägt den Paperclaim.** Der Claim überlebt nur als gemeinsame Synthese.

## 4. S2 — No residual explanatory compression

**NOT TRIGGERED, aber weiterhin begrenzend.**

S2 wäre ausgelöst, wenn Section 7 zeigen würde, dass die vier AI-Archetypen ohne Rest lediglich als unabhängige Anwendungen bereits etablierter Frameworks nebeneinanderstehen und die R/T/C-Sprache keine zusätzliche Vergleichsstruktur erzeugt.

Das ist in der geschriebenen Fassung nicht der Fall. Ein wiederkehrendes Schema bleibt erhalten:

```text
referent R
+
claim-status of T
+
role of C
+
direct evidence relation
+
explicit non-implication / bridge requirement
```

Dieses Schema komprimiert mindestens vier fachlich verschieden formulierte Situationen:

```text
real prediction without mechanism claim
synthetic teacher fidelity vs real validation
physics-constraint satisfaction vs theory adequacy vs empirical adequacy
computational inference producing T_hat
```

Der Kompressionsgewinn ist jedoch **moderat**. Er besteht nicht darin, dass ein Spezialframework die Fälle nicht darstellen könnte, sondern darin, dass die Fälle mit derselben kleinen epistemischen Grammatik vergleichbar werden.

### S2-Boundary

Das Manuskript darf deshalb nicht formulieren:

> existing frameworks cannot express these cases.

Zulässig ist nur:

> the same compact role/evidence vocabulary makes the cases comparable while leaving specialist assessment to the established frameworks.

## 5. S3 — Notation only

**NOT TRIGGERED.**

Section 7 bestätigt die W3-Gegenprobe. Der Rest wäre reine Notation, wenn `R/T/C` lediglich die klassischen Begriffe umbenennen würde. Die Manuskriptsemantik trägt darüber hinaus vier wiederkehrende Constraints:

```text
1. Referent changes imply claim changes.
2. T can be NONE_CLAIMED or INFERRED without changing the role grammar.
3. Evidence is relation-specific rather than a global model score.
4. Cross-relation transfer requires an explicit bridge argument.
```

Diese Constraints werden in Section 4 tatsächlich zur Unterscheidung der vier Archetypen benutzt. Daher bleibt S3 nicht ausgelöst.

## 6. S5 — Overclaim pressure

**NOT TRIGGERED.**

Der W4-Text bleibt trotz sehr defensiver Comparator-Anerkennung noch kohärent. Er benötigt keine Wiederbelebung verworfener Aussagen wie:

```text
new triangle
new validation questions
new provenance framework
new identifiability theory
AI breaks classical V&V
first account of prediction without explanation
first account of computational theory discovery
```

Das ist ein wichtiges positives Survival-Signal: Die Story bleibt lesbar, obwohl fast alle Einzelneuheiten explizit abgegeben werden.

## 7. Was W4 dem Manuskript abverlangt

### W4-R1 — Contribution Statement muss kompakt bleiben

Die stärkste zulässige Fassung lautet sinngemäß:

> a genealogically grounded evidence-localization vocabulary for comparing heterogeneous computational scientific workflows.

Nicht zulässig:

> a unified framework replacing V&V, provenance, assurance, or identifiability.

### W4-R2 — Specialist frameworks müssen funktional priorisiert werden

Das Manuskript sollte wiederholt klar machen:

```text
Trias says where/what kind of claim
specialist framework says how deeply to assess it
```

Diese Arbeitsteilung ist stärker als ein Konkurrenznarrativ.

### W4-R3 — Section 7 straffen

Die v0.1-Fassung ist als Gate-Draft etwas ausführlicher. Für das Endmanuskript Ziel:

```text
ca. 900–1,100 Wörter
```

Comparatoren nicht als Mini-Reviews ausbauen. Jede Subsection soll nur drei Funktionen erfüllen:

```text
what comparator already does
what Trias therefore cannot claim
what residual cross-case role remains
```

### W4-R4 — Equation Discovery + Surrogate bleiben zentrale Belege

Auch nach Comparator-Stress sind diese zwei Fälle die stärksten Träger:

```text
Equation Discovery -> T as output of C / role-order reversal
Surrogate          -> R_syn vs R_real / referent-sensitive evidence
```

Black-box und PIML bleiben unterstützende Vergleichsfälle.

## 8. Paper-Level Urteil nach W4

Nach W4 sind die wichtigsten Survival-Risiken wie folgt:

```text
S1 direct isomorph         -> not triggered; reopen only for a concrete new source
S2 no residual compression -> NOT TRIGGERED, but residual is moderate
S3 notation only           -> NOT TRIGGERED
S4 genealogy dominates     -> NOT TRIGGERED / active risk, controlled by length
S5 overclaim pressure      -> NOT TRIGGERED
S6 case incoherence        -> W1 PASS
```

Damit überlebt die zentrale Contribution-Boundary den bislang härtesten Manuskriptvergleich.

## 9. Gesamturteil

```text
W4 boundary gate         = PASS
paper mode               = CONTINUE PERSPECTIVE
technical/framework novelty = NO
residual contribution    = MODERATE CROSS-DOMAIN SYNTHESIS
practical superiority    = UNTESTED
```

Der Standalone-Artikel bleibt gerechtfertigt, **wenn** er als Philosophy-of-Science/AI-for-Science-Perspective geschrieben wird und die Contribution als begriffliche Kompression/Evidence Localization statt als neue Methodik behandelt.

## 10. Empfehlung für die nächste Abhängigkeit

**ACCEPT W4 = PASS.**

Danach Writing Goal W5:

> **Sections 5–6 — Classical controls and negative/inconclusive stress tests.**

W5 soll Sundman und Figure-eight bewusst kurz als klassische Kontrollfälle integrieren und anschließend Lorenz/SINDy (`INFORMATIVE_NEGATIVE`) sowie ML v0.1 (`INCONCLUSIVE_LEARNER_ERROR`) so schreiben, dass negative, inconclusive und untested Evidenz klar getrennt bleiben.

Nach W5 ist kein neuer Novelty-Gate nötig; geprüft werden nur **case coherence** und **evidence-status discipline**. Introduction und Abstract bleiben weiterhin bis nach Discussion zurückgestellt.