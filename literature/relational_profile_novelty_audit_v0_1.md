# Relational-Profile Novelty Audit v0.1

**Status:** COMPLETE / PENDING CLAIM DECISION  
**Stand:** 2026-09-03  
**Depends on:** D025, C08-D-R, `theory/edge_semantics_evidence_ledger_v0_1.md`

## 1. Prüfgegenstand

Dieser Audit prüft nicht mehr allgemeine Aussagen wie `computation matters`, `prediction != understanding` oder `model quality is purpose-relative`. Diese wurden bereits als etablierte Vorarbeit anerkannt.

Geprüft wird ausschließlich die präzisierte Struktur:

```text
R = target/reality
T = theory / conceptual-scientific representation
C = computational realization

R-T = target/theory adequacy
T-C = theory/computation fidelity + tractability
C-R = computation/target adequacy
```

plus:

```text
claim/facet/use/evidence/scope binding
real vs synthetic target typing
default non-transitivity
explicit bridge claims
application to simulation + AI for Science
```

Die zentrale Frage ist, ob diese Struktur als eigenständige neue Trias-Topologie tragfähig ist oder einen bereits etablierten direkten Vorläufer besitzt.

---

## 2. Entscheidender Direktvorläufer: Schlesinger / SCS Model Credibility

Der stärkste Befund dieses Audits ist ein historischer Direktvorläufer, der im ersten Descriptive-Trias-Stress-Test nicht hinreichend berücksichtigt wurde.

Die SCS Technical Committee on Model Credibility veröffentlichte 1979 `Terminology for model credibility` (SIMULATION 32(3), 103–104, DOI 10.1177/003754977903200304). Die daraus etablierte Model-Credibility-Terminologie wird in der späteren V&V-Literatur als Dreieck aus folgenden Rollen reproduziert:

```text
Reality / Problem Entity
Conceptual Model
Computerized Model
```

mit den drei Beziehungen:

```text
Reality <-> Conceptual Model      = model qualification / conceptual model validity
Conceptual Model <-> Computerized = model verification
Computerized Model <-> Reality    = model validation / operational validity
```

Diese Struktur ist der Descriptive Trias topologisch nahezu isomorph:

```text
Trias R  ~ Reality / Problem Entity
Trias T  ~ Conceptual Model
Trias C  ~ Computerized Model

Trias R-T ~ qualification / conceptual model validity
Trias T-C ~ verification
Trias C-R ~ validation / operational validity
```

### Konsequenz

**FAIL für den Neuheitsclaim der R/T/C-Dreieckstopologie.**

Die bloße Existenz dreier Rollen und dreier paarweiser Bewertungsrelationen ist historisch klar vorbelastet und kann nicht als originäre Trias-Struktur beansprucht werden.

---

## 3. Sargent: fast direkte semantische Entsprechung der drei Kanten

Robert G. Sargents langjährige Arbeiten zu Verification and Validation of Simulation Models machen die Zuordnung noch deutlicher.

Sargent unterscheidet:

```text
Conceptual model validity
Computerized model verification
Operational validity
Data validity
```

Conceptual model validity betrifft, ob die Theorien und Annahmen des conceptual model korrekt sind und seine Repräsentation des problem entity für den intendierten Zweck angemessen ist.

Computerized model verification betrifft, ob die Implementierung das conceptual model korrekt repräsentiert.

Operational validity betrifft, ob das Verhalten des computerized model für den intendierten Zweck im vorgesehenen Anwendungsbereich hinreichend genau ist.

### Mapping

```text
R-T:
Trias RT_EMPIRICAL / RT_SCOPE / Teile von RT_STRUCTURAL
~ Sargent conceptual model validity

T-C:
Trias TC_FIDELITY / TC_CONVERGENCE / TC_STABILITY / implementation fidelity
~ computerized model verification

C-R:
Trias CR_PREDICTION / CR_REPRESENTATION / application-domain adequacy
~ operational validity
```

### Konsequenz

**FAIL für die Behauptung, die Trias habe erstmals drei unterschiedliche relationsspezifische Adäquanzfragen zwischen Target, Theorie und Berechnung explizit gemacht.**

Dieser Kern existiert in der klassischen Simulation-V&V-Tradition bereits sehr nahe an unserer Form.

---

## 4. ASME/AIAA/NASA: Verification und Validation als genau T-C vs C-R

Moderne VVUQ-/M&S-Standards verschärfen den Direktvergleich.

ASME beschreibt Verification sinngemäß als Prüfung, ob das computational model zur mathematischen Beschreibung passt; Validation als Prüfung, ob das Modell die reale Anwendung angemessen repräsentiert. NASA definiert Verification als Konformität einer M&S-Implementierung mit conceptual/mathematical model bzw. Anforderungen und Validation als Genauigkeit gegenüber der realen Welt relativ zum intended use.

Damit ist die Trennung

```text
"implements theory correctly" != "represents reality adequately"
```

keine neue Trias-Diagnose, sondern Kern moderner V&V-Terminologie.

Auch `intended use`, `domain of applicability`, `permissible use`, acceptance criteria und dokumentierte Grenzen sind etablierte Credibility-Kategorien.

### Konsequenz

**FAIL** für Neuheitsansprüche auf:

```text
- Use-/Scope-Relativität der Kanten;
- Trennung von implementation fidelity und real-world validity;
- die Idee, dass ein Modell für einen Use Case validiert und für einen anderen unzureichend sein kann.
```

---

## 5. Synthetic target / surrogate: auch der Referentenwechsel besitzt starke Vorarbeit

Der Edge-Ledger betont:

```text
Surrogate accuracy vs simulator
!=
validation vs real target
```

Auch dafür existiert direkte technische Vorarbeit.

Simulation-Credibility-Guides unterscheiden reale Referenzdaten von simulierten Referenten. Hochfidele Physikmodelle können als Referent für niedrigere Modelle oder Metamodelle/Surrogate dienen; eine solche Prüfung etabliert jedoch zunächst die Übereinstimmung mit dem Referenten, nicht automatisch die reale Validität des gesamten Modellstapels. Für real-world model validation wird reale/experimentelle Evidenz verlangt oder der Transfer muss über die Credibility des Referenten begründet werden.

Das entspricht nahezu unserem Bridge-Schema:

```text
surrogate -> simulator fidelity
+
simulator -> reality credibility
+
scope/error compatibility
=> conditional support for surrogate -> reality claim
```

### Konsequenz

**FAIL bis STRONGLY PRECEDED** für die Grundidee `synthetic target must not be conflated with real target`.

Die explizite Schreibweise `R_syn` vs `R_real` ist eine nützliche Projektkonvention, aber keine neue epistemische Entdeckung.

---

## 6. Scientific ML 2026: klassische V&V-Struktur wird bereits in SciML erweitert

Jakeman et al., `Verification and validation for trustworthy scientific machine learning` (Machine Learning: Science and Technology, 2026), übertragen Verification und Validation ausdrücklich auf Scientific ML.

Der Rahmen verlangt unter anderem:

```text
- model purpose / intended use;
- prior knowledge;
- quantities of interest;
- model structure;
- data characteristics and processing;
- code/solution verification;
- independent validation data;
- calibration;
- uncertainty;
- interpolation/extrapolation scope.
```

Verification betrifft dort weiterhin die korrekte computational realization der zugrunde liegenden mathematischen/physikalischen Struktur, während Validation prüft, ob die Modellierungsstruktur einschließlich SciML-Anteilen relevante Eigenschaften des physikalischen Systems für den Modellzweck reproduziert.

### Konsequenz

**FAIL für einen starken Claim**, dass erst die Trias die klassische theory/computation/reality-Trennung auf AI for Science anwendbar macht.

Der AI-for-Science-Transfer der V&V-Semantik ist bereits aktive Forschung.

---

## 7. Digital Twins: reale Verankerung + computational representation + intended use

Neuere Digital-Twin-Credibility-Literatur nutzt dieselbe Grundtrennung ebenfalls explizit:

```text
verification -> computational/conceptual conformance
validation   -> adequacy relative to real-world counterpart and intended use
```

NIST und neuere Reviews behandeln die Credibility digitaler Zwillinge ausdrücklich über real-system grounding, computational realization, V&V, uncertainty und context/intended use.

### Konsequenz

Auch moderne hybride/AI-nahe Systeme werden bereits über eine sehr ähnliche Relationstopologie analysiert.

---

## 8. Default-Nichttransitivität

Die Trias formuliert explizit:

```text
RT + TC -/-> CR
TC + CR -/-> RT
RT + CR -/-> TC
```

Diese genaue Symbolregel wurde im Audit nicht als kanonische V&V-Formel gefunden.

Inhaltlich ist sie jedoch stark durch die etablierte Trennung von qualification/conceptual validation, verification und operational validation vorweggenommen. Dass Verification nicht Validation ersetzt und dass technische Korrektheit allein keine Realitätsvalidität etabliert, ist ein Standardmotiv der V&V-Literatur.

### Konsequenz

**Möglicherweise eigenständige Formulierung, aber keine hinreichend neue Grundidee.**

Der Wert liegt eher in der didaktisch-philosophischen Explizitheit und im Verbot stillschweigenden Evidenztransfers.

---

## 9. Bridge Claims und Evidence Ledger

Das explizite Bridge-Claim-Schema der Trias ist spezifischer als klassische dreieckige V&V-Diagramme. Aber auch hier existiert starke Nachbarschaft:

- Credibility-/Context-of-Use-Frameworks binden Evidenz an einen konkreten Use Case und dessen Anforderungen;
- Assurance Cases / Claims–Arguments–Evidence binden Evidence explizit an Claims und Zwischenargumente;
- Provenance-Frameworks verfolgen Herkunft und Transformation von Artefakten;
- modernere V&V-Standards verlangen dokumentierte Evidenzketten und zulässige Einsatzbereiche.

### Konsequenz

**Kein belastbarer Novelty-Claim für Claim-Evidence-Bridging als solches.**

Das Trias-Ledger kann eine nützliche Komposition dieser Elemente sein, ist aber derzeit als Synthese/Notation zu bewerten.

---

## 10. Entscheidend: T ist nicht exakt dasselbe wie Sargents Conceptual Model

Hier bleibt eine reale Differenz.

Sargents `conceptual model` ist eine logische/mathematische Repräsentation des problem entity für einen Simulationszweck und enthält Theorien/Annahmen. Die Trias verwendet `T` breiter und epistemischer:

```text
- formale Gleichungsstruktur;
- mechanistischer Claim;
- erklärender Claim;
- inferierte symbolische Struktur;
- auch die Möglichkeit T = NONE_CLAIMED.
```

Damit kann die Trias Fälle beschreiben, in denen:

```text
C existiert ohne expliziten T-Claim        (black-box prediction)
T erst durch C inferiert wird              (equation discovery)
C einen Simulator/Teacher approximiert     (surrogate ML)
T und C partiell verschmolzen sind         (physics-informed / hybrid ML)
```

### Bewertung

Dies ist **kein neuer Dreieckstyp**, sondern eine mögliche wissenschaftsphilosophische **Generalisierung der klassischen Model-Credibility-Triade** über traditionelle Simulation hinaus.

Genau hier sollte ein möglicher Paper-Beitrag gesucht werden.

---

## 11. Novelty-Matrix

| Präzisierter Trias-Bestandteil | Direktvorarbeit | Urteil |
|---|---|---|
| R / T / C als Dreiecksrollen | Schlesinger/Sargent: Reality / Conceptual Model / Computerized Model | **FAIL as novelty** |
| R-T / T-C / C-R als drei Bewertungsrelationen | qualification/conceptual validity / verification / validation | **FAIL as novelty** |
| Intended use / scope | Sargent, AIAA, ASME, NASA | **FAIL as novelty** |
| T-C ≠ C-R | Kern von Verification vs Validation | **FAIL as novelty** |
| real vs synthetic referent | simulation/metamodel credibility | **STRONGLY PRECEDED** |
| Evidence nicht automatisch übertragbar | V&V-Trennung + credibility logic | **STRONGLY PRECEDED** |
| explizite Bridge-Claims | CAE/assurance + credibility arguments | **WEAK DISTINCTIVE SYNTHESIS** |
| Facet-Ledger | V&V/QoI/credibility + project-specific typing | **SYNTHESIS / NOT CLEAR NOVELTY** |
| Anwendung auf SciML | aktuelle SciML-V&V-Literatur | **PRECEDED** |
| T kann absent/inferred/explanatory sein | weniger direkt in klassischer Simulation-V&V | **POTENTIAL DELTA** |
| einheitliche epistemische Lesart über Sundman, Simulation, black-box AI, surrogate AI, PINNs, equation discovery | kein einzelner Direktanalog im Audit gefunden | **POTENTIAL SYNTHESIS CONTRIBUTION** |

---

## 12. Gesamturteil

Der Audit widerlegt die stärkste verbleibende Neuheitslesart von C08-D-R:

> Die `R/T/C`-Topologie und ihre drei Paarrelationen sind **nicht** als originär neue Trias-Struktur haltbar.

Der entscheidende historische Vorläufer ist die Model-Credibility-/V&V-Tradition um Schlesinger und Sargent.

Das bedeutet jedoch nicht, dass das Projekt wertlos wird. Es verschiebt den möglichen Beitrag erneut, diesmal sehr konkret:

> Die Trias kann als **wissenschaftsphilosophische Generalisierung und AI-for-Science-Reinterpretation einer etablierten V&V-Dreiecksstruktur** untersucht werden. Der potenzielle Mehrwert liegt darin, `Conceptual Model` zu einem expliziten Theorie-/Erklärungsclaim zu erweitern, `Computerized Model` auf gelernte und inferierende computational practices auszudehnen und die klassische V&V-Trennung als deskriptives epistemisches Profil verschiedener Arten wissenschaftlichen Erfolgs zu lesen.

Diese Fassung muss den Vorläufer **zentral anerkennen**, nicht nur in einer Related-Work-Notiz.

---

## 13. Vorgeschlagener revidierter Claim — C08-D-R2 (noch nicht akzeptiert)

> **C08-D-R2:** Die Descriptive Trias wird nicht als neue Dreieckstopologie von Realität, Theorie und Berechnung beansprucht; eine strukturell sehr ähnliche Triade aus Reality/Problem Entity, Conceptual Model und Computerized Model mit den Relationen qualification/conceptual validity, verification und validation ist in der klassischen Model-Credibility-Literatur etabliert. Der mögliche Beitrag der Trias liegt in einer wissenschaftsphilosophischen Generalisierung dieser Struktur für Computational Science und AI for Science: `T` wird als expliziter theoretischer, mechanistischer oder erklärender Claim typisiert und kann fehlen oder datengetrieben inferiert werden; `C` umfasst numerische, gelernte und inferierende computational realizations; und Evidenz wird claimspezifisch danach profiliert, welche Relation sie tatsächlich stützt. Diese Generalisierung ist als interpretative Synthese zu positionieren, nicht als neue V&V-Theorie.

### Evidenzstatus

```text
historische R/T/C-Topologie als Neuheit: REJECTED
relationale Diskriminationsleistung: POSITIVE
AI-for-Science-Generalisation: PLAUSIBLE
praktische Überlegenheit: UNTESTED
Originalität der Generalisierung: MODERATE / NOT YET DEMONSTRATED AS UNIQUE
```

---

## 14. Empfehlung

**Akzeptiere den Novelty-Audit und rebase das Projekt explizit auf die Schlesinger/Sargent-Genealogie.**

Nicht empfohlen:

```text
- C08-D-R unverändert als neue relationale Topologie verkaufen;
- einen weiteren numerischen Versuch zur Rettung der Neuheit starten;
- den klassischen V&V-Vorläufer nur als Randnotiz behandeln.
```

Empfohlener nächster Schritt:

`Paper Contribution Boundary v0.2 — From Model-Credibility Triangle to Descriptive Trias for AI for Science`

Dort muss der Paper-Hauptclaim erstmals **genealogisch** formuliert werden: nicht `we introduce three relations`, sondern `we generalize/reinterpret an established simulation-credibility structure to distinguish theory claims, learned computation and target-relative evidence in AI for Science`.

Die Paperstruktur sollte anschließend prüfen, ob diese Generalisierung als Philosophy-of-Science/Perspective-Beitrag hinreichend eigenständig ist.