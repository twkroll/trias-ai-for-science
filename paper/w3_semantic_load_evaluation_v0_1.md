# W3 — Semantic-Load / Notation-Only Evaluation v0.1

**Status:** COMPLETE / PENDING AUTHOR DECISION  
**Stand:** 2026-09-03  
**Depends on:** D032, `paper/manuscript_section_3_v0_1.md`, W1 PASS, W2 PASS

## 1. Prüfziel

W3 prüft Survival-Kriterium S3:

> Besteht der verbleibende Beitrag im Manuskript praktisch nur aus neuen Labels `R/T/C`, Statuswerten und einer Tabelle für bereits vollständig bekannte Inhalte?

Erlaubte lokale Urteile:

```text
PASS
SHORTEN
STOP
```

Der Test bewertet nicht, ob einzelne semantische Bausteine neu sind. Das ist bereits weitgehend negativ entschieden. Geprüft wird ausschließlich, ob ihre gemeinsame minimale Semantik im Manuskript **argumentative Last** trägt.

## 2. Ergebnis

**Klassifikation: PASS — eng, nur für Perspective / Conceptual Synthesis.**

S3 `notation only` ist in W3 **nicht ausgelöst**.

Der Grund ist nicht, dass `R/T/C`, Statuswerte oder Bridge Claims als Einzelideen neu wären. Der Grund ist, dass die Semantik im geschriebenen Abschnitt mehrere zulässige und unzulässige inferentielle Übergänge explizit unterscheidet und diese Regeln bereits in W1 über vier unterschiedliche AI-for-Science-Konfigurationen ohne ad-hoc Änderungen verwendet werden.

## 3. Wo reale semantische Last entsteht

### 3.1 `R` ist nicht bloß ein neues Wort für Reality

Der manuscript-relevante Gehalt liegt in der **claim-relativen Referentenfixierung**:

```text
R_REAL
R_SYNTHETIC
R_HYBRID
```

und in der Regel:

> Ein Referentenwechsel ist ein Claimwechsel, selbst wenn `C` und die numerische Metrik identisch bleiben.

Dies ist besonders im Surrogate-Fall argumentativ wirksam:

```text
RMSE_teacher = epsilon
```

und

```text
RMSE_real = epsilon
```

stützen nicht denselben Claim.

Die Grundidee ist stark vorbelastet, aber die Regel trägt in der gemeinsamen Cross-case-Semantik echten Gehalt.

### 3.2 `T` hat semantischen Gehalt durch claim-relative Zustände

Die vier Zustände

```text
PRESENT
PARTIAL
NONE_CLAIMED
INFERRED
```

sind nicht bloß kosmetisch, weil sie unterschiedliche argumentative Konsequenzen erzwingen.

`NONE_CLAIMED` erlaubt:

```text
CR_PREDICTION = ESTABLISHED
T-related claim = NOT_APPLICABLE
```

ohne einen versteckten Defizitwert einzuführen.

`INFERRED` erlaubt:

```text
R -> D -> C_infer -> T_hat
```

ohne `T` weiterhin künstlich als vorgängige Lifecycle-Stufe zu behandeln.

Dies ist für Equation Discovery der stärkste semantic-load Punkt.

### 3.3 Statuswerte unterscheiden Failure, Uncertainty und Nichtanwendbarkeit

Die Statussprache trägt nur dann Gehalt, wenn sie unterschiedliche wissenschaftliche Aussagen erzwingt. Das ist im Projekt der Fall:

```text
UNTESTED       != failed
UNCERTAIN      != refuted
NOT_APPLICABLE != deficient
```

Die eigenen Projektfälle liefern dafür reale Beispiele:

```text
ML v0.1      -> UNCERTAIN / INCONCLUSIVE_LEARNER_ERROR
Lorenz/SINDy -> negative Evidenz für robusten structural-effect Claim
Black-box T  -> NOT_APPLICABLE für einen engen mechanistischen Claim, wenn keiner gemacht wird
Surrogate CR_real -> UNTESTED, falls nur Teacher-Holdout vorliegt
```

Damit ist die Statussprache mehr als ein kosmetisches Rating.

### 3.4 Default-Nichttransfer erzeugt explizite inferentielle Verbote

Die Regeln

```text
RT + TC -/-> CR
TC + CR -/-> RT
RT + CR -/-> TC
```

sind nicht als neue logische Theoreme zu verstehen. Im Manuskript tragen sie aber semantische Last, weil sie konkrete unzulässige Kurzschlüsse markieren.

Beispiele:

```text
small physics residual -/-> validated real-world model
teacher fidelity        -/-> real-target validity
real prediction         -/-> unique mechanism
```

Ohne diese Regel könnte die Trias tatsächlich zu reiner Benennung kollabieren. Mit ihr wird die Profilstruktur zu einer expliziten Evidenzlokalisierung.

### 3.5 Bridge Claims markieren die zusätzliche inferentielle Arbeit

Der Surrogate-Fall zeigt einen zulässigen Transfer nur unter Zusatzprämissen:

```text
surrogate fidelity
+
simulator validated for same QoI/regime
+
scope compatibility
+
controlled surrogate error
-> conditional real-target support
```

Die Bridge ist keine neue Methode gegenüber Assurance/Credibility. Sie zeigt aber im gemeinsamen Profil, **wo** zusätzliche Argumentation benötigt wird.

## 4. Gegenprobe: Was wäre nur Notation?

S3 wäre ausgelöst, wenn Section 3 im Wesentlichen nur sagen würde:

```text
Reality = R
Theory = T
Computation = C
```

und anschließend bekannte Verification-/Validation-Fragen neu benennen würde.

Die geschriebene Fassung geht darüber hinaus, weil sie vier constraints enthält:

1. Referent muss claimspezifisch fixiert werden.
2. `T` kann absent oder inferred sein, ohne die Rollenlogik zu ändern.
3. Statuswerte unterscheiden fehlende, unzureichende und nicht anwendbare Evidenz.
4. Evidenztransfer zwischen Relationen ist ohne Bridge nicht zulässig.

Diese constraints werden in W1 tatsächlich gebraucht. Deshalb ist die Semantik nicht redundant mit einer bloßen Grafiklegende.

## 5. Was weiterhin stark vorbelastet ist

Der PASS darf nicht als Neuheitsupgrade gelesen werden. Folgende Elemente haben starke etablierte Analogien:

```text
claim-relative validation / intended use
verification vs validation
real vs synthetic reference
claims-evidence reasoning
provenance / evidence lineage
scope-aware credibility
uncertainty and untested status
```

Daher bleibt der Contribution-Typ:

```text
common semantic synthesis / evidence-localization vocabulary
```

und nicht:

```text
new formal epistemology
new V&V method
new assurance framework
```

## 6. Längen- und Komplexitätsrisiko

W3 zeigt auch ein neues Manuskriptrisiko: Die Semantik kann leicht zu umfangreich werden und dann wie ein technisches Framework wirken, das sie nicht ist.

Für die Endfassung wird deshalb empfohlen:

```text
Section 3 target: ca. 900–1,100 Wörter
retain:
- role definitions
- target typing
- T statuses
- minimal ledger
- three status distinctions
- non-transfer default
- one bridge example

compress or move to appendix:
- long facet catalogues
- exhaustive status criteria
- multiple bridge schemas
- implementation-level ledger details
```

Die v0.1-Fassung ist als W3-Test bewusst etwas vollständiger als die spätere Manuskriptfassung.

## 7. Survival-Kriterien nach W3

```text
S1 direct isomorph             -> nicht ausgelöst; nur bei neuem konkreten Literaturfund wieder öffnen
S2 no residual compression     -> nicht ausgelöst; bleibt Hauptrisiko für Section 7
S3 notation only               -> NOT TRIGGERED / PASS
S4 genealogy dominates         -> nicht ausgelöst; aktives Risiko, Section 2 kurz halten
S5 overclaim pressure          -> nicht ausgelöst
S6 case incoherence            -> W1 PASS
```

## 8. Gesamturteil

W3 trägt genügend argumentative Semantik, um das Perspective-Manuskript fortzuführen:

```text
W3 semantic-load gate = PASS
paper mode             = CONTINUE PERSPECTIVE
notation-only risk     = NOT TRIGGERED
framework novelty      = NO
semantic synthesis     = PLAUSIBLE / MODERATE
```

Der stärkste Punkt ist nicht die Notation, sondern die Kombination aus claim-relativem Referentenwechsel, variablem `T`-Status, nicht-defizitärer `NOT_APPLICABLE`-Semantik und explizitem Verbot stillschweigenden Evidenztransfers.

## 9. Empfehlung für die nächste Abhängigkeit

**ACCEPT W3 = PASS.**

Danach Writing Goal W4:

> **Section 7 — What the Trias adds, and what adjacent frameworks already do better.**

W4 ist der härteste verbleibende Boundary-Test. Dort muss das Paper direkt gegen V&V/VVUQ, Provenance, Assurance Cases, Identifiability/System ID, Philosophy of ML/P.E.D.U.D. und SciML positioniert werden.

Nach W4 ist erneut ein lokaler Gate gegen S2 `no residual explanatory compression` und S3 `notation only` erforderlich. Wenn der Beitrag dort nur als Kombination bestehender Frameworks ohne begrifflichen Rest erscheint, muss auf `SHORTEN` oder `STOP` zurückgegangen werden.