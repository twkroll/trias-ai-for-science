# W1 — Section 4 Survival Evaluation v0.1

**Status:** COMPLETE / PENDING AUTHOR DECISION  
**Stand:** 2026-09-03  
**Depends on:** D030, `paper/manuscript_section_4_v0_1.md`

## 1. Gate

Erlaubte Klassen:

```text
PASS
SHORTEN
STOP
```

Bewertet wird ausschließlich, ob Section 4 die verbliebene Synthese-Contribution tatsächlich trägt. Investierte Projektarbeit ist kein positives Kriterium.

## 2. Ergebnis

**Klassifikation: PASS.**

Dies ist ein enger PASS für eine **Perspective / Conceptual Synthesis**, nicht für ein neues Framework-Paper.

## 3. Kriterium 1 — Eine gemeinsame Grammatik ohne ad-hoc Ausnahmen?

**PASS.**

Alle vier Archetypen lassen sich mit derselben Minimalstruktur beschreiben:

```text
R type / referent
T status
C role
principal evidence
supported relation
explicit non-implication
```

Die Rollen verändern ihre Besetzung und Richtung, aber nicht ihre Grundsemantik.

### Black-box prediction

```text
R = REAL
T = NONE_CLAIMED
C = predictor
Evidenz -> C-R prediction
```

Die Theoriebezogenheit wird nicht künstlich erzwungen; `NONE_CLAIMED` / `NOT_APPLICABLE` ist semantisch zulässig.

### Synthetic surrogate

```text
R = SYNTHETIC für Teacher-Fidelity
optional R = REAL für downstream scientific use
T = simulator/model present
C = surrogate
```

Der zentrale Unterschied ist der Referent, nicht eine neue Fehlermetrik.

### Physics-informed/hybrid ML

```text
R-T = adequacy of embedded theory
T-C = implementation/satisfaction of theory
C-R = empirical target adequacy
```

Die drei Relationen bleiben getrennt, obwohl sie in einem einzelnen learned system zusammenlaufen.

### Equation discovery

```text
R -> D -> C_infer -> T_hat
```

`T` wird Output von C, ohne dass die Rollenbegriffe geändert werden müssen.

**Befund:** S6 `case incoherence` tritt in v0.1 nicht ein.

## 4. Kriterium 2 — Pro Fall mindestens ein präziser epistemischer Unterschied?

**PASS.**

Die Section erzeugt pro Archetyp einen klaren Nichtimplikations- oder Lokalisierungsgewinn:

| Fall | Präzisierter Unterschied |
|---|---|
| Black-box | reale Prediction kann `C-R` stützen, ohne dass ein mechanistischer `R-T`-Claim überhaupt gemacht wird |
| Surrogate | gleiche RMSE gegen Teacher und reale Daten besitzt unterschiedlichen Referenten und stützt unterschiedliche Claims |
| PIML | Physics-Constraint-Satisfaction (`T-C`) ist nicht automatisch Theorieadäquanz (`R-T`) oder reale Validation (`C-R`) |
| Equation Discovery | dynamische/statistische Adäquanz ist nicht automatisch strukturelle/mechanistische Identifikation; zudem kann `T` Output von `C` sein |

Diese Unterschiede sind als Einzelideen etabliert, aber die gemeinsame Rollen-/Evidenzsemantik funktioniert über alle vier Fälle.

## 5. Kriterium 3 — Weniger Mehrdeutigkeit als globale Labels?

**PASS.**

Die v0.1-Prosa zeigt überzeugend, warum globale Labels epistemisch unterbestimmt sein können:

```text
accurate
validated
physics-informed
discovered
```

werden durch claimspezifische Aussagen ersetzt, etwa:

```text
accurate relative to which referent?
validated for which target/use/scope?
physics constraint implemented vs theory empirically adequate?
discovered dynamics vs discovered mechanism?
```

Dies ist keine neue V&V- oder ML-Kategorie, aber eine reale begriffliche Kompression über Fachgrenzen hinweg.

## 6. Kriterium 4 — Ist Equation Discovery strukturell instruktiv?

**STRONG PASS.**

Equation Discovery ist der stärkste Fall für P3, weil hier die klassische zeitliche Lesart

```text
Conceptual Model -> Computerized Model
```

nicht die epistemische Rollenordnung abbildet:

```text
R -> D -> C_infer -> T_hat
```

Die Rollen bleiben unterscheidbar, obwohl ihre chronologische Reihenfolge wechselt. Dies stützt die Formulierung `epistemic roles rather than fixed lifecycle stages` besser als die anderen drei Fälle.

## 7. Survival-Kriterien S1–S6

### S1 — Direct isomorph

**Nicht ausgelöst in W1.**

Die verwendete Literatur enthält starke Teilanalogien, aber W1 identifiziert keinen einzelnen Direktanalog, der die gesamte genealogische Rollen-/Evidenzgrammatik bereits in derselben Form liefert.

### S2 — No residual explanatory compression

**Nicht ausgelöst; weiterhin Hauptrisiko.**

Sargent + moderne SciML-/Philosophy-of-ML-Literatur erklären die Einzelprobleme. Die Section erzeugt jedoch einen verbleibenden Vergleichsgewinn, weil dieselbe kleine Grammatik die vier Fälle mit unterschiedlichen Referenten, Theorie-Status und Evidenzrelationen beschreibt.

Dieser Gewinn ist moderat, nicht stark.

### S3 — Notation only

**Nicht ausgelöst.**

Die Section verwendet R/T/C nicht nur als Umbenennung. Der relevante Mehrwert liegt in den wiederkehrenden Nichtimplikationen und im Wechsel zwischen `T = NONE_CLAIMED`, `T present/partial` und `T inferred`, gekoppelt an Target-Typen.

### S4 — Genealogy dominates contribution

**Noch nicht testbar in voller Stärke.**

W1 zeigt genug AI-spezifische Rollenvariation, um das Paper weiterzuführen. Section 2 muss später bewusst kurz genug bleiben, damit die Genealogie den neuen Syntheseteil nicht verdrängt.

### S5 — Overclaim pressure

**Nicht ausgelöst.**

Die Section bleibt interessant, obwohl sie ausdrücklich zugibt, dass Prediction, Surrogates, PIML, Equation Discovery und die jeweiligen Einzelprobleme etabliert sind.

### S6 — Case incoherence

**Nicht ausgelöst.**

Keine ad-hoc Änderung der Grundsemantik nötig.

## 8. Schwächen der W1-Fassung

### W1-R1 — Section derzeit etwas zu erklärend

Die v0.1-Fassung ist als Survival-Draft absichtlich ausführlich. Für das Endmanuskript sollte sie wahrscheinlich um etwa 15–25% gestrafft werden, vor allem bei den wiederholten Boundary-Sätzen `this is not new`.

### W1-R2 — Black-box ist der schwächste Delta-Fall

`T = NONE_CLAIMED` ist analytisch sauber, aber literaturseitig stark vorweggenommen. Der Fall sollte im Manuskript kürzer sein als Equation Discovery und Surrogate.

### W1-R3 — PIML kann wie Standard-V&V wirken

Die Trennung `R-T / T-C / C-R` ist hier sehr intuitiv, aber gerade deshalb reviewer-seitig als bekannte Verification-/Validation-Logik lesbar. Die Funktion des PIML-Falls sollte daher primär **cross-case comparability** sein, nicht Novelty.

### W1-R4 — Surrogate und Equation Discovery tragen die stärkste Story

Surrogate zeigt den Referentenwechsel besonders klar; Equation Discovery zeigt die Rollen-/Richtungsverschiebung besonders klar. Diese zwei Fälle sollten im finalen Section-4-Gewicht dominieren.

## 9. Gesamturteil

W1 erfüllt die positive Survival-Bedingung:

> Die vier AI-Archetypen lassen sich mit einer gemeinsamen kleinen Rollen-/Evidenzgrammatik darstellen, und diese Darstellung lokalisiert in jedem Fall mindestens einen wissenschaftlich relevanten Unterschied, den globale Erfolgslabels verdecken.

Der Befund rechtfertigt das Weiterschreiben einer Perspective. Er rechtfertigt **keinen** stärkeren Claim als P3.

```text
W1 = PASS
manuscript mode = CONTINUE PERSPECTIVE
framework novelty = NO
practical superiority = UNTESTED
```

## 10. Empfehlung für die nächste Abhängigkeit

**ACCEPT W1 = PASS.**

Danach Writing Goal W2:

> **Section 2 — Genealogy: From model credibility to the present problem + Table 1 genealogy/comparator mapping.**

W2 muss besonders streng prüfen, ob die historische Genealogie den verbleibenden Beitrag überwältigt. Nach W2 kein erneuter allgemeiner Novelty-Audit, sondern ein lokaler `genealogy-dominance` Check gegen S4.