# Paper Claim + Outline Freeze v0.3

**Working title:** *From Model Credibility to AI for Science: A Descriptive Trias of Target, Theory, and Computation*  
**Status:** PENDING REVIEW  
**Stand:** 2026-09-03  
**Depends on:** D028 / C08-D-R3 / `paper/paper_contribution_boundary_v0_2.md` / `literature/ai_for_science_delta_audit_v0_1.md`

## 1. Zweck dieses Freeze-Dokuments

Dieses Dokument beendet die explorative Claim-Suche und legt die engste Version des Projekts fest, die nach den bisherigen positiven, negativen und inconclusive Tests noch als eigenständiges Paper sinnvoll geschrieben werden kann.

Es ist ausdrücklich **kein Manuskriptentwurf**. Vor dem Schreiben soll entschieden werden, ob die verbleibende Contribution hinreichend kohärent und interessant ist, um als eigenständige wissenschaftsphilosophische Perspective/Synthese verfolgt zu werden.

Die Leitfrage lautet nicht mehr:

> Ist ein Dreieck aus Realität, Theorie und Berechnung neu?

Diese Frage ist negativ entschieden.

Die Leitfrage lautet:

> **Kann die klassische Model-Credibility-Triade für AI for Science fruchtbar als claim-relative Rollenstruktur gelesen werden, sodass unterschiedliche Arten computationalen wissenschaftlichen Erfolgs danach unterschieden werden, welches Target, welcher Theorieclaim und welche computational practice durch die jeweilige Evidenz tatsächlich miteinander verbunden werden?**

---

## 2. Empfohlener finaler Principal Claim P3

> **P3 — Genealogical Role-Profile Claim:** Die Descriptive Trias ist keine neue Reality–Model–Computation-Topologie, sondern eine wissenschaftsphilosophische Reinterpretation und Synthese der klassischen Model-Credibility-Genealogie für AI for Science. Sie behandelt `R` als den claimspezifischen realen, synthetischen oder hybriden Referenten, `T` als den wissenschaftlichen Theorie-, Mechanismus- oder Erklärungsclaim, der vorhanden, partiell, nicht beansprucht oder computational inferiert sein kann, und `C` als konkrete numerische, gelernte oder inferierende computational practice. Evidenz wird nicht als globale Modellgüte gelesen, sondern danach profiliert, welchen Target–Theory-, Theory–Computation- oder Computation–Target-Claim sie in einem angegebenen Use Case und Scope stützt. Der Beitrag liegt in dieser genealogischen gemeinsamen Lesart verschiedener etablierter AI-for-Science-Erfolgsformen, nicht in neuen V&V-, ML-, Identifiability- oder Discovery-Kategorien.

### Warum P3 schreibbar ist

P3 beansprucht nur drei Dinge:

1. **Genealogische Kontinuität:** Schlesinger/Sargent und moderne V&V-/Credibility-Ansätze sind der historische Ausgangspunkt.
2. **Rollen- statt Lifecycle-Lesart:** In AI for Science sind `T` und `C` nicht notwendig feste aufeinanderfolgende Workflow-Stufen; Theorie kann fehlen, partiell eingebettet oder Output computationaler Inferenz sein.
3. **Evidenzlokalisierung:** Dieselbe Metrik oder dasselbe Erfolgslabel kann epistemisch Unterschiedliches stützen, abhängig davon, gegen welchen Referenten und für welchen Claim sie erhoben wurde.

Nicht behauptet wird, dass diese drei Gedanken einzeln neu sind. Der beanspruchte Eigenwert ist ihre **gemeinsame genealogische Synthese**.

---

## 3. Unterstützende Subclaims

### P3a — Classical genealogy

> Die klassische Model-Credibility-Triade aus Problem Entity/Reality, Conceptual Model und Computerized Model mit conceptual model validity/qualification, verification und operational validity/validation ist ein direkter historischer Vorläufer der R/T/C-Struktur.

**Status:** stark gestützt.

### P3b — Dynamic role occupation in AI for Science

> AI-for-Science-Workflows lassen sich nicht immer sinnvoll als eine einzige feste Kette `Conceptual Model -> Computerized Model` lesen: predictive ML kann ohne expliziten Theorieclaim verwendet werden, Equation Discovery kann Theorie als Output computationaler Inferenz erzeugen, Surrogate können auf synthetische Referenten zielen und PIML kann Theorie- und Datenconstraints in einer computational practice überlagern.

**Status:** stark als Beschreibung etablierter Praktiken gestützt; nicht neu als Einzelbeobachtung.

### P3c — Relation-specific evidence semantics

> Ein Performancewert besitzt keinen vollständigen epistemischen Sinn ohne Angabe, welcher Claim und Referent bewertet wird. Teacher-/Simulator-Treue, reale Prediction, Physics-Constraint-Erfüllung und mechanistische/strukturelle Unterstützung sind Evidenz für verschiedene Relationen und dürfen nicht stillschweigend global gleichgesetzt werden.

**Status:** analytisch positiv in den Projekt-Profiltests; stark kompatibel mit bestehender Credibility-/V&V-Logik.

### P3d — Descriptive, not ranking

> Die Trias beschreibt Arten und Grenzen wissenschaftlichen Erfolgs; sie verlangt nicht, dass ein Modell auf allen Relationen stark ist, und erzeugt keinen globalen Qualitäts- oder Trade-off-Score.

**Status:** normative Selbstbegrenzung des Ansatzes.

---

## 4. Explizite Non-Claims — finaler Freeze

Das Paper darf nicht behaupten:

1. `Reality / Theory / Computation` oder `Reality / Conceptual Model / Computerized Model` sei eine neue Dreiecksidee.
2. Die Unterscheidung von Verification und Validation sei neu.
3. Conceptual model validity, intended use, scope oder adequacy-for-purpose seien neue Trias-Kategorien.
4. Prediction ohne Understanding/Theorie sei neu.
5. Equation Discovery oder AI-generated scientific models seien neu.
6. Synthetic-data-/sim-to-real-Probleme seien neu.
7. Physics-informed oder theory-guided ML sei neu.
8. Verschiedene epistemische ML-Ziele wie Prediction, Explanation, Discovery und Understanding seien neu.
9. Claim–Evidence-Traceability, Provenance, Assurance Cases oder Bridge-Argumente seien neue Erfindungen der Trias.
10. Die drei Kanten seien unabhängig, eindimensional oder skalare Gütekoordinaten.
11. Zwischen den Kanten bestehe ein notwendiger Nullsummen-Trade-off.
12. Ein Black-box-Predictor sei epistemisch minderwertig, nur weil kein `T` beansprucht wird.
13. Ein Modell müsse alle drei Relationen gleichzeitig etablieren.
14. Die Trias sei empirisch nützlicher, leichter verständlich oder entscheidungswirksamer als V&V/Credibility/SciML-Frameworks.
15. Der Figure-eight-Fall zeige neue numerische Fehlerkategorien.
16. Der Lorenz/SINDy-Fall zeige einen robusten positiven Provenance-Effekt.
17. ML-v0.1 entscheide den Teacher-Provenance-Claim.
18. Das Nichtfinden eines einzelnen Direktanalogs im Audit beweise Originalität.

---

## 5. Abstract-Logik — fünf Sätze

Ein späterer Abstract sollte logisch ungefähr diese fünf Funktionen erfüllen:

1. **Genealogie:** Model credibility besitzt seit Jahrzehnten eine explizite Trennung von problem entity, conceptual model und computerized model sowie von conceptual validity, verification und validation.
2. **Problemverschiebung:** In AI for Science ist computation jedoch nicht mehr nur Implementierung eines gegebenen conceptual model, sondern kann prediction, surrogation, reconstruction und theory inference übernehmen.
3. **Vorschlag:** Wir reinterpretieren die klassische Triade als claim-relative epistemische Rollen `R/T/C` und profilieren Evidenz danach, welche Relation, welcher Use Case und welcher Scope tatsächlich gestützt werden.
4. **Demonstration:** Black-box prediction, synthetic surrogates, physics-informed learning und equation discovery zeigen unterschiedliche Rollenbelegungen; klassische numerische Fälle dienen als Kontrollfälle, und eigene negative/inconclusive Demonstratoren zeigen die Grenzen der Interpretation.
5. **Boundary:** Der Beitrag ist eine genealogische Philosophy-of-Science-Synthese für AI for Science, keine neue V&V-Theorie und kein empirisch validierter Überlegenheitsclaim.

---

## 6. Empfohlene Paper-Architektur

### Section 1 — Introduction: When “the model works” is epistemically incomplete

Ziel:

- Einstieg über eine konkrete Ambiguität: dieselbe gute RMSE kann Teacher-Treue oder reale Prediction meinen;
- AI for Science erzeugt häufig starke computational outputs, deren wissenschaftlicher Bedeutungsumfang nicht allein durch Performance bestimmt ist;
- direkte Anerkennung: Credibility/V&V hat die Grundrelationen lange vor der Trias unterschieden;
- Paperfrage: Was verändert sich, wenn computation selbst unterschiedliche epistemische Rollen übernimmt?

Die Introduction darf **nicht** mit einer Novelty-Behauptung des Dreiecks beginnen.

### Section 2 — Genealogy: the model-credibility triangle

Kernliteratur:

```text
Schlesinger et al. 1979
Sargent
ASME / AIAA / NASA credibility/V&V
modern VVUQ / context-of-use
```

Ziel:

- die nahezu isomorphe historische Topologie zeigen;
- Mapping zu `R/T/C` offenlegen;
- erklären, welche Teile des eigenen Projekts dadurch nicht neu sind;
- Credibility als konstitutive Genealogie etablieren.

Schlüsselsatz dieser Section:

> **The triangle is not new.**

### Section 3 — From lifecycle stages to claim-relative epistemic roles

Definitionen:

```text
R = claim-relative target/reference: REAL / SYNTHETIC / HYBRID
T = scientific theory/mechanism/explanation claim: PRESENT / PARTIAL / NONE_CLAIMED / INFERRED
C = concrete computational practice: solver / predictor / surrogate / reconstruction / inference / hybrid
```

Hier wird die entscheidende Reinterpretation formuliert:

> `R`, `T`, `C` sind analytische Rollen in einem wissenschaftlichen Claim, nicht notwendig zeitlich geordnete Entwicklungsstufen.

Minimaler Evidence-Ledger:

```text
edge | facet | claim | evidence | use case | scope | status
```

Statussprache nur knapp einführen:

```text
ESTABLISHED / PARTIAL / UNCERTAIN / UNTESTED / NOT_APPLICABLE
```

Keine Quantifizierung und kein globaler Score.

### Section 4 — Four AI-for-Science role configurations

#### 4.1 Predictive black-box: useful C with no explicit T claim

Schema:

```text
R -> data -> C
T = NONE_CLAIMED for the narrow prediction claim
```

Aussage:

- hohe reale Prediction kann `C-R` stark stützen;
- sie ist kein automatischer Mechanismus-/Erklärungsclaim;
- keine Abwertung der Prediction.

Comparatoren: Philosophy of ML, Naser/P.E.D.U.D., prediction-vs-understanding literature.

#### 4.2 Synthetic surrogate: changing the referent

Schema:

```text
T -> C_sim -> D_syn -> C_surrogate
```

Zentraler Kontrast:

```text
RMSE against teacher -> evidence about teacher/synthetic referent relation
RMSE against real data -> evidence about real-target relation
```

Nicht als neuer sim-to-real-Befund verkaufen. Zweck: zeigen, warum der Referent Teil der Claimsemantik sein muss.

#### 4.3 Physics-informed / hybrid ML: overlapping relations

Drei getrennte Fragen:

```text
Ist Theorie in C implementiert/satisfied? -> T-C
Ist T für R im Regime adäquat?            -> R-T
Funktioniert C auf R?                      -> C-R
```

Comparator: Karniadakis et al. + SciML/PIML literature.

#### 4.4 Equation Discovery: computation produces a theory claim

Schema:

```text
R -> observations/data -> C_infer -> T_hat
```

Dies ist der strukturell wichtigste Inversionsfall für das Paper.

Trennung:

```text
dynamical/statistical adequacy of inferred model
!= automatically
structural/mechanistic identification of T
```

Comparatoren: Equation Discovery / automated scientific discovery / identifiability / Zhai–Lucarini–Lai.

### Section 5 — Classical controls: where ordinary V&V already suffices

Diese Section schützt das Paper vor Überdehnung.

#### 5.1 Sundman

Nur als kompakter historischer T-C-Fall:

```text
formal/analytic availability != practical computational availability
```

Wichtig: Sundmans Reihen konvergieren; die praktische Konvergenz/Evaluierbarkeit ist das Problem.

#### 5.2 Figure-eight

Explizit als **Kontrollgruppe**:

- gleiche Theorie, unterschiedliche Solverprofile;
- RK4 vs Velocity-Verlet je nach Trajektorie/Struktur;
- Numerical Analysis/V&V erklärt den Fall bereits gut;
- Trias beansprucht hier keinen exklusiven Zusatznutzen.

Diese Section sollte kurz bleiben.

### Section 6 — Stress tests: negative and inconclusive evidence

#### 6.1 Lorenz/SINDy

Vorregistriertes Ergebnis:

```text
INFORMATIVE_NEGATIVE
```

- P0 valide;
- linear structural perturbation 1/3 seeds;
- cubic 0/3;
- kein robuster positiver Provenance-Effekt.

Funktion im Paper:

> Eine Rollen-/Evidenzgrammatik muss auch zeigen können, dass ein interessanter theoretischer Claim **nicht** durch vorliegende Evidenz etabliert wurde.

#### 6.2 ML v0.1

Ergebnis:

```text
INCONCLUSIVE_LEARNER_ERROR
```

Funktion:

- `TC_RESOLVABILITY` scheitert;
- dadurch ist der geplante nachgelagerte Provenance-Claim nicht bewertbar;
- Appendix oder kurze Box, kein Hauptergebnis.

### Section 7 — What the Trias adds, and what adjacent frameworks already do better

Vergleich modular statt kompetitiv:

```text
V&V / VVUQ           -> Verification, Validation, credibility evidence
Provenance            -> lineage and transformation history
Assurance cases       -> claims–arguments–evidence structures
Identifiability       -> uniqueness/recoverability of inverse claims
System identification -> robustness of inferred dynamical models
P.E.D.U.D./Philosophy -> plural epistemic functions of ML
SciML frameworks      -> modern hybrid/surrogate/physics-ML practice
```

Verbleibender Trias-Claim:

> eine kompakte genealogische Sprache, die diese Evidenz danach ordnet, **welche epistemische Relation eines claimspezifischen R/T/C-Profils** sie stützt.

Nicht behaupten, dass etablierte Frameworks dies nicht ebenfalls erweitern könnten.

### Section 8 — Discussion: scientific success without global success

Kernpunkte:

- `successful` ist claimspezifisch;
- `NOT_APPLICABLE` ist keine Schwäche;
- unterschiedliche Modelle können unterschiedliche wissenschaftliche Ziele legitim bedienen;
- keine notwendige Trade-off-Geometrie;
- mögliche spätere normative oder empirische Evaluation wird klar als Future Work getrennt.

### Section 9 — Conclusion

Nur drei Schlusssätze nötig:

1. klassische Credibility-Genealogie anerkennen;
2. dynamische AI-for-Science-Rollen + relationale Evidenzsemantik als Synthese festhalten;
3. Grenzen/keine Überlegenheitsbehauptung wiederholen.

---

## 7. Zentrale Abbildungen und Tabellen

### Figure 1 — Genealogy, not invention

Links:

```text
Reality / Problem Entity
Conceptual Model
Computerized Model
```

mit conceptual validity / verification / validation.

Rechts:

```text
R = claim-relative target
T = theory/mechanism/explanation claim
C = computational practice
```

mit explizitem Pfeil `genealogical reinterpretation`, nicht `new framework`.

### Figure 2 — Role configurations in AI for Science

Vier kleine Panels:

```text
black-box:         R -> D -> C, T absent
surrogate:         T -> C1 -> D_syn -> C2
physics-informed:  T + D(R) -> C
Eq. discovery:     R -> D -> C -> T_hat
```

Dies sollte die wichtigste Abbildung des Papers werden.

### Figure 3 — Same metric, different epistemic claim

Konzeptionelles Beispiel:

```text
RMSE = epsilon against simulator -> simulator/teacher-relative evidence
RMSE = epsilon against real data -> real-target predictive evidence
```

Ziel: Evidenzlokalisierung anschaulich machen.

### Table 1 — Genealogy / comparator matrix

Spalten:

```text
Trias element | Schlesinger/Sargent | modern V&V/SciML | claimed novelty? | role in paper
```

### Table 2 — AI-for-Science role profiles

Für black-box, surrogate, PIML, equation discovery:

```text
R type | T status | C role | principal evidence | supported relation | non-implication
```

### Table 3 — Project evidence ledger

Nur kompakt:

```text
Sundman        -> positive conceptual illustration
Figure-eight   -> positive but standard V&V control
Lorenz/SINDy   -> INFORMATIVE_NEGATIVE
ML v0.1        -> INCONCLUSIVE_LEARNER_ERROR
```

Der negative/inconclusive Status muss visuell gleichwertig dargestellt werden.

---

## 8. Literaturachsen, die im Manuskript konstitutiv sein müssen

Keine reine Related-Work-Liste, sondern Argumentachsen:

### Genealogie

- Schlesinger et al. 1979;
- Sargent;
- ASME/AIAA/NASA V&V/Credibility/VVUQ.

### Philosophie von Simulation / Computational Science

- Humphreys;
- Winsberg;
- Lenhard;
- Models-as-Mediators-Linie als wichtiger Hintergrund.

### Purpose-relative adequacy / model pluralism

- Parker;
- Levins/Weisberg nur zur Abgrenzung gegen notwendige Trade-off-Behauptungen.

### AI epistemic roles

- Naser/P.E.D.U.D.;
- Vinuesa et al. 2026;
- weitere prediction/explanation/understanding literature.

### SciML / hybrid / surrogate

- Karniadakis et al.;
- Jakeman et al. 2026;
- einschlägige surrogate/ROM credibility literature.

### Theory inference

- Kramer et al. / Automated Scientific Discovery;
- Equation Discovery/SINDy;
- Zhai–Lucarini–Lai als konkreter aktueller Stressfall.

### Comparatoren für Claim-Evidence-Semantik

- assurance cases / CAE / GSN;
- provenance / W3C PROV;
- identifiability / observability / structural error.

---

## 9. Gewichtung der eigenen Projektresultate

Das Paper ist **kein numerisches Methodenpaper**. Deshalb:

```text
Schlesinger/Sargent genealogy           HIGH
AI archetypes + literature              HIGH
Equation Discovery conceptual case      HIGH
Synthetic surrogate example             HIGH
Figure-eight                             LOW-MEDIUM, control
Sundman                                  LOW-MEDIUM, motivation
Lorenz/SINDy negative run                MEDIUM, methodological stress test
ML v0.1 inconclusive run                 LOW, appendix/box
```

Die eigene numerische Arbeit dient der Claim-Disziplin und Illustration, nicht der Begründung einer neuen technischen Methode.

---

## 10. Empfohlenes Paperformat

**Primäre Empfehlung:** kurze bis mittellange **Perspective / conceptual synthesis paper** mit kontrollierten computational case studies.

Nicht als:

```text
new framework paper
new V&V method
new SciML benchmark
new numerical methodology
new philosophy-of-AI grand theory
```

Zielumfang grob:

```text
main text: etwa 6,000–8,000 Wörter
appendix/supplement: technische Details der eigenen Runs
```

Ein Short Perspective von etwa 4,000–5,000 Wörtern bleibt Fallback, falls die volle argumentative Breite beim Schreiben nicht trägt.

---

## 11. Harte Survival-/Stop-Kriterien vor und während des Schreibens

Das eigenständige Paper sollte **gestoppt oder zu einer kurzen Perspective/Commentary reduziert** werden, wenn mindestens eines der folgenden Probleme eintritt:

### S1 — Direct-isomorph criterion

Während des Schreibens wird ein einzelner etablierter Rahmen gefunden, der die klassische Credibility-Genealogie bereits mit dynamischen AI-Rollen und praktisch derselben claim-relativen RT/TC/CR-Evidenzsemantik verbindet.

**Folge:** Standalone novelty stark geschwächt; höchstens Commentary/Perspective.

### S2 — No residual explanatory compression

Nach fertiger Section 4 lassen sich alle vier AI-Archetypen ohne Informationsverlust allein durch eine direkte Kombination aus Sargent + einem modernen SciML-Review beschreiben, sodass die Trias-Sprache keinerlei zusätzliche begriffliche Kompression oder Vergleichbarkeit erzeugt.

**Folge:** STOP standalone paper oder stark kürzen.

### S3 — Notation-only criterion

Der verbleibende Eigenbeitrag lässt sich nur noch als neue Labels `R/T/C` und Tabellenfelder beschreiben.

**Folge:** STOP standalone paper.

### S4 — Genealogy dominates contribution

Die historische V&V-Genealogie erklärt den gesamten interessanten Inhalt, während AI-for-Science nur Beispiele hinzufügt.

**Folge:** maximal historische/philosophische Commentary, nicht eigener Framework-/Synthesis-Artikel.

### S5 — Overclaim pressure

Das Paper wirkt nur dann interessant, wenn wieder Behauptungen eingeführt werden, die durch D009, D020, D026 oder den Delta Audit bereits verworfen wurden.

**Folge:** nicht überdehnen; lieber STOP.

### S6 — Case incoherence

Black-box, surrogate, PIML und equation discovery lassen sich nicht mit derselben claimspezifischen Rolle-/Evidenzsemantik darstellen, ohne ad-hoc Ausnahmen einzuführen.

**Folge:** Syntheseclaim gescheitert.

---

## 12. Positive Survival-Kriterien

Ein eigenständiges Paper ist gerechtfertigt, wenn beim Manuskriptentwurf Folgendes gleichzeitig gelingt:

```text
1. Die historische Genealogie wird transparent anerkannt.
2. Die vier AI-Archetypen lassen sich mit derselben kleinen Rollen-/Evidenzgrammatik darstellen.
3. Diese Darstellung macht mindestens einen epistemischen Unterschied pro Archetyp präziser sichtbar als globale Labels wie accurate / physics-informed / discovered / validated.
4. Der Leser versteht, warum gleiche Performancewerte unterschiedliche Claims stützen können.
5. Equation Discovery zeigt überzeugend, warum T nicht immer als vorgängige Lifecycle-Stufe gelesen werden sollte.
6. Die negative/inconclusive Evidenz kann integriert werden, ohne die Story zu beschädigen.
7. Der Beitrag bleibt interessant, obwohl keine neue V&V-Metrik und keine starke Framework-Novelty behauptet wird.
```

---

## 13. Entscheidung nach diesem Freeze

### Option A — WRITE AS PERSPECTIVE / CONCEPTUAL SYNTHESIS

C08-D-R3 und P3 werden als Manuskriptboundary akzeptiert. Danach wird ein actual manuscript skeleton mit Absatzfunktionen und Quellenzuordnung erstellt und anschließend Abschnitt für Abschnitt geschrieben.

### Option B — SHORT PERSPECTIVE

Die Synthese wird akzeptiert, aber auf eine kürzere argumentative Form reduziert. Eigene numerische Fälle werden auf Boxes/Supplement minimiert; Fokus auf Genealogie + vier AI-Archetypen + Evidence-Semantik.

### Option C — STOP STANDALONE PAPER

Die Trias wird nicht als eigenes Paper weiterverfolgt. Die entwickelte Semantik kann künftig als methodologischer Rahmen in anderen AI-for-Science-Projekten verwendet werden.

### Option D — REVISE

Nur zulässig, wenn ein konkreter inhaltlicher Einwand gegen P3 oder die Outline vorliegt. Keine erneute freie Novelty-Suche.

---

## 14. Empfehlung

**Empfehlung: Option A — WRITE AS PERSPECTIVE / CONCEPTUAL SYNTHESIS.**

Begründung:

- Der starke Novelty-Anspruch ist ausreichend zurückgenommen.
- Die Genealogie ist inzwischen ein Vorteil statt ein versteckter Einwand.
- Die vier AI-Archetypen bilden eine kohärente Rollenvariation.
- Die relationale Evidenzsemantik besitzt demonstrierte analytische Diskriminationsleistung.
- Negative und inconclusive Resultate können als Claim-Disziplin statt als Problem integriert werden.
- Der verbleibende Beitrag ist für ein Perspective-/Philosophy-of-Science-Paper plausibel, auch wenn er für ein technisches `new framework`-Paper zu schwach wäre.

**Nicht empfohlen:** weitere numerische Experimente oder weitere immer enger werdende Novelty Audits vor dem ersten vollständigen Manuskriptentwurf.