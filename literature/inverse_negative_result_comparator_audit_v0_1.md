# Comparator Audit des inversen INFORMATIVE_NEGATIVE v0.1

**Status:** COMPLETE / PENDING CLAIM DECISION  
**Stand:** 2026-09-02  
**Depends on:** D020  
**Gegenstand:** derselbe vorregistrierte Lorenz/SINDy-Befund wird ohne Änderung der numerischen Resultate in konkurrierenden methodologischen Sprachen beschrieben.

## 1. Fixierter empirischer Befund

Der Full Run erfüllt G1–G3. P0 rekonstruiert den exakten Lorenz-Termsupport. Unter 20% zufälliger punktweiser Missingness ist die kubische Rekonstruktion deutlich genauer als lineare Rekonstruktion. Trotzdem entsteht kein seed-robuster struktureller Provenance-Effekt:

```text
linear: structural perturbation 1/3
cubic:  structural perturbation 0/3
required: >=2/3
classification: INFORMATIVE_NEGATIVE
```

Der einzige strukturell abweichende Fall (`linear / seed 2`) erzeugt einen zusätzlichen konstanten Term in `dz/dt`, bleibt aber nach den vorregistrierten Kriterien operativ äquivalent. Dieser 1/3-Fall bleibt explorativ.

Der Audit fragt nicht, welches Vokabular den Befund am elegantesten beschreibt, sondern ob die Directed Trias **zusätzliche diagnostische oder rechtfertigungsbezogene Arbeit** leistet.

---

## 2. Comparator A — System Identification / SINDy robustness

### Was dieser Rahmen bereits erklärt

Equation Discovery ist eine inverse Modellierungsaufgabe, deren Ergebnis von Datenqualität, Sampling, numerischer Differentiation, Kandidatenbibliothek, Regularisierung/Threshold und Modellselektion abhängt. Robustere SINDy-Varianten wurden gerade deshalb entwickelt, weil sparse recovery gegenüber Messfehlern und Ableitungsfehlern empfindlich sein kann.

Der vorliegende Befund lässt sich vollständig in dieser Sprache ausdrücken:

```text
reconstruction method
-> reconstruction error
-> derivative error / regression perturbation
-> coefficient/support variability
-> robustness across masks
```

Die Tatsache, dass cubic die fehlenden Zustände deutlich genauer rekonstruiert und anschließend geringere Vector-Field-Fehler zeigt, ist ein normaler Pipeline-Robustheitsbefund. Dass nur eine lineare Maske einen spurious term erzeugt, ist ebenfalls als finite-data/perturbation-sensitive Support-Selektion verständlich.

### Was dieser Comparator am Seed-2-Fall sagt

`linear / seed 2` ist kein Beleg für eine neue epistemische Kategorie. Es ist ein klassischer Fall, in dem eine kleine Daten-/Preprocessing-Perturbation eine andere sparse representation erzeugt, während das resultierende Modell für bestimmte Outputs weiterhin gut funktioniert.

### Rest für die Trias

Kein neuer numerischer Fehlertyp und keine neue System-Identification-Frage. Die Trias kann höchstens markieren, **an welcher gerichteten Pipeline-Stufe** die Variation eingeführt wurde und welche nachgelagerte Aussage betroffen ist.

**Coverage:** sehr hoch.

---

## 3. Comparator B — Structural/practical identifiability, observability und near-identifiability

Structural identifiability fragt klassisch nach Eindeutigkeit unbekannter Größen bei idealisierten Outputs; Observability nach Rekonstruierbarkeit interner Zustände aus Outputs. Practical identifiability erweitert die Frage auf endliche, verrauschte oder unvollständige Daten.

Für unseren konkreten SINDy-Fall ist klassische Parameter-identifiability allein zu eng, weil auch die Termstruktur selektiert wird. Der ältere structural-error/near-identifiability-Ansatz ist jedoch näher: Er formuliert ausdrücklich **Near-Equivalence von strukturell nicht identischen Modellen bei tolerierten Outputabweichungen**.

Der explorative Seed-2-Fall lässt sich deshalb direkt lesen als:

```text
structural non-identity
+
output / dynamical near-equivalence
```

Das ist konzeptionell keine neue Trias-Entdeckung.

Der negative Haupteffekt ist ebenfalls kompatibel mit diesem Rahmen: Unter der konkreten Beobachtungs- und Inferenzkonfiguration bleibt die identifizierte Struktur weitgehend robust. Ein identifiability-orientierter Ansatz erwartet nicht, dass jede Datenperturbation zwingend Nicht-Eindeutigkeit sichtbar machen muss.

### Rest für die Trias

Die Trias integriert Observability/Identifiability in eine größere Forward-/Inverse-Kette, entwickelt aber keine neue Identifiability-Theorie und kein neues Eindeutigkeitskriterium.

**Coverage:** hoch bis sehr hoch für die inverse Nicht-Eindeutigkeitsfrage.

---

## 4. Comparator C — Modeling & Simulation V&V / Scientific-ML Credibility

NASA-STD-7009B etabliert M&S-Credibility als lebenszyklus- und anwendungsbezogene Aufgabe mit Verification, Validation, Sensitivity/UQ und programmspezifischen Acceptance Criteria. Neuere SciML-V&V-Arbeiten erweitern diese Logik ausdrücklich um Datencharakteristika, Datenverarbeitung, Hyperparameter, Alternativenvergleich, Reproduzierbarkeit und purpose-specific quantities of interest.

Unser Design passt fast direkt in diese Sprache:

```text
P0 gate                     -> verification / baseline adequacy
held-out vector field       -> independent validation quantity
short-horizon trajectories  -> use-specific predictive quantity
long-time statistics        -> alternative use-specific quantities
reconstruction diagnostics  -> data-processing characterization
paired masks                -> controlled sensitivity comparison
pre-registered thresholds   -> acceptance criteria
```

Auch die zentrale Trennung

```text
structural equation fidelity
!= dynamical/statistical adequacy
```

kann in einem V&V/Credibility-Framework als unterschiedliche quantities of interest bzw. unterschiedliche Validierungsziele formuliert werden.

### Rest für die Trias

Die Trias bietet eine kompakte sprachliche Zuordnung zu `R`, `T`, `C` und gerichteten Übergängen. Aber der Full Run zeigt keine Validierungsfrage, die ein stark ausgeführtes V&V-/Credibility-Programm prinzipiell nicht stellen könnte.

**Coverage:** sehr hoch.

---

## 5. Comparator D — Workflow/Data Provenance

W3C PROV modelliert Provenance ausdrücklich über **Entities**, **Activities**, **Agents**, Usage, Generation und Derivation. Wissenschaftliche Workflow-Provenance erweitert dies um prospektive und retrospektive Workflow-Beschreibungen, Parameter, Zwischenprodukte und Ausführungsumgebungen.

Die gesamte inverse Pipeline kann ohne semantischen Bruch als Provenance-Graph dargestellt werden:

```text
latent trajectory      = entity
sampling               = activity
sampled data           = entity
missingness mask       = entity / parameterized activity input
linear/cubic imputation= activity
reconstructed data     = entity
5-point differentiation= activity
estimated derivatives  = entity
STLSQ fit               = activity
inferred coefficients  = entity
forward validation     = activity
validation metrics     = entities
```

Damit sind `direction`, `intermediate artifacts`, `derivation` und `which operation produced which object` bereits Kernideen etablierter Provenance-Modelle.

### Rest für die Trias

W3C PROV sagt nicht von sich aus, welche **wissenschaftliche Bedeutung** ein Objekt besitzt oder welcher Claim durch eine Validierung legitimiert ist; Rollen können jedoch domänenspezifisch annotiert werden. Die bloße Darstellung einer gerichteten Provenance-Kette ist daher keine ausreichende Trias-Neuheit.

**Coverage:** sehr hoch für Herkunft und Transformationsgraph.

---

## 6. Comparator E — Claims–Arguments–Evidence / Assurance Cases

Dieser Comparator wurde als zusätzlicher Stress-Test aufgenommen, weil ein möglicher Restclaim der Trias lautet:

> Der Audit macht sichtbar, welches epistemische Objekt tatsächlich validiert wurde und welche Aussage daraus gerechtfertigt ist.

Assurance Cases und Goal Structuring Notation organisieren jedoch seit Langem explizit:

```text
claim
+ context / assumptions
+ argument
+ evidence
```

und verlangen, dass Evidenz einem konkreten Claim angemessen zugeordnet wird. Damit ist selbst die allgemeinere Idee `evidence does not automatically license every higher-level claim` keine neue Trias-Idee.

Für unseren inversen Full Run könnte ein Assurance Case beispielsweise getrennte Claims formulieren:

```text
C1: P0 recovers the intended Lorenz support.
C2: P1/P2 are technically valid reconstructions.
C3: inferred vector fields satisfy held-out tolerance.
C4: autonomous statistics satisfy use-specific tolerance.
C5: a reconstruction method causes a robust structural change.
```

Der negative Full Run unterstützt C1–C4 weitgehend, aber nicht C5. Diese Claim-Evidence-Struktur reproduziert praktisch genau die von uns gewünschte Schutzfunktion gegen ungerechtfertigten Evidenztransfer.

### Rest für die Trias

Die Trias kann diese Argumentstruktur mit den fachwissenschaftlichen Rollen `target / theory / computation` und Forward-/Inverse-Richtung verbinden. Aber **Claim-to-evidence traceability selbst ist bereits etablierte Assurance-Methodik**.

**Coverage:** sehr hoch für Rechtfertigungszuordnung.

---

## 7. Vergleichsmatrix

| Frage im inversen Fall | System ID | Identifiability | V&V/Credibility | Provenance | Assurance Case | Directed Trias |
|---|---|---|---|---|---|---|
| Welche Pipelinewahl verändert SINDy? | stark | mittel | stark | stark dokumentierbar | mittel | stark |
| Ist die Theorie eindeutig rekonstruierbar? | stark | sehr stark | mittel | schwach | mittel | stark integriert |
| Woher stammt ein Artefakt? | mittel | schwach | mittel | sehr stark | mittel | stark |
| Welche QoI/use-case gilt? | mittel | mittel | sehr stark | schwach | stark | stark |
| Welche Evidenz stützt welchen Claim? | mittel | mittel | stark | schwach-mittel | sehr stark | stark |
| Forward + inverse Kette in einer Sprache | mittel | schwach | stark möglich | sehr stark graphisch | stark argumentativ | expliziter Fokus |
| Neuer Fehlertyp / neues mathematisches Kriterium | nein | nein | nein | nein | nein | **nein gezeigt** |

Die Matrix zeigt: Der mögliche Restwert der Trias liegt nicht in einer exklusiven Diagnosefähigkeit, sondern höchstens in einer **kompakten fachübergreifenden Synthese mehrerer bereits etablierter Perspektiven**.

---

## 8. Konsequenz aus dem negativen Resultat

Das negative Experiment ist für den Novelty-Test besonders aufschlussreich, weil die Trias auch ohne spektakulären Provenance-Effekt funktionieren musste.

Tatsächlich lokalisiert der Trias-Audit sauber:

```text
R -> D -> C_pre -> D_recon -> C_infer -> T_hat -> C_forward -> validated observables
```

Aber jede wesentliche Diagnose kann auch mit einer Kombination etablierter Frameworks formuliert werden:

```text
System Identification
+ identifiability / structural error
+ V&V / credibility
+ workflow provenance
+ claim-evidence assurance
```

Damit ist der starke Satz

> `Directed Trias provides a methodologically new audit capability`

auf Basis des derzeitigen Projekts **nicht gestützt**.

---

## 9. Was als vertretbarer Trias-Beitrag übrig bleibt

Der derzeit defensible Rest ist eine **conceptual synthesis / audit lens**:

> Die Directed Trias ordnet heterogene wissenschaftliche Praktiken in einer gemeinsamen, leicht lesbaren Sprache danach, welches Zielsystem, welche Theorie und welche operative Vermittlung an einer Stelle vorliegen, in welche Richtung transformiert wird und auf welches Objekt sich ein Validierungs- oder Nutzbarkeitsurteil bezieht.

Dieser Beitrag kann nützlich sein, insbesondere um Sundman, numerische Solver, datengetriebene Equation Discovery und ML-Surrogate in derselben Darstellung zu diskutieren. Er ist jedoch gegenwärtig eher als **Integrations-, Kommunikations- und Lehrschema** denn als neue V&V-, Provenance- oder Identifiability-Theorie zu positionieren.

Die wissenschaftliche Stärke eines Papers müsste dann aus Folgendem kommen:

1. ungewöhnlich klare Synthese bislang getrennt diskutierter Forward-/Inverse-Fälle;
2. präzise Claim- und Non-Claim-Grenzen;
3. konkrete Fallstudien mit positiven, negativen und inconclusive Resultaten;
4. transparente Comparator-Matrix statt überzogener Neuheitsbehauptung;
5. eventuell ein wiederverwendbares leichtgewichtiges Audit-Template.

---

## 10. Konsequenz für C06-R

C06-R war bereits schwach formuliert. Der neue Audit empfiehlt eine weitere Präzisierung statt Stärkung.

### Kandidat C06-R2 — noch NICHT akzeptiert

> **C06-R2:** Die bisherigen Drei-Körper-, ML- und inversen Equation-Discovery-Fälle zeigen keine eigenständige neue Fehler-, Validierungs-, Provenance- oder Identifiability-Kategorie der Trias gegenüber starken etablierten Vergleichsrahmen. Der verbleibende mögliche Beitrag der Directed Trias ist eine kompakte fachübergreifende Synthese, die Forward- und Inverse-Transformationen zwischen Zielsystem, Theorie und operativer Vermittlung in einer gemeinsamen Audit-Sprache ordnet und sichtbar macht, auf welches epistemische Objekt sich eine konkrete Rechtfertigung bezieht. Diese Leistung ist als konzeptionelle Integrations- und Kommunikationsfunktion zu bewerten und nicht als neue mathematische oder technische Credibility-Theorie.

### Evidenzstatus

- erster Satz: durch die bisherigen Comparator-Audits und Demonstratoren stark gestützt;
- zweiter Satz: als Beschreibung dessen, was die Trias **tun soll**, plausibel;
- behauptete praktische Nützlichkeit dieser Synthese: noch nicht unabhängig evaluiert;
- Originalität dieser Synthese: höchstens moderat und weiterhin literaturkritisch zu behandeln.

---

## 11. Strategische Optionen nach dem Audit

### A — Paper-Pivot auf konzeptionelle Synthese

Keine weiteren Experimente zur Rettung eines positiven Effekts. Hauptpaper als methodologisches/Perspective-Paper mit:

```text
Sundman -> formal vs operational
Figure-eight -> use-case-relative numerical profiles
inverse Lorenz/SINDy -> pre-registered negative provenance test
ML v0.1 -> inconclusive learner-resolvability example
Comparator matrix -> exact contribution boundary
```

**Vorteil:** wissenschaftlich sauber, nutzt auch negative Befunde produktiv, minimale Confirmation-Bias-Gefahr.

### B — ML-v0.2 wieder aufnehmen

Nur sinnvoll, wenn der ML-Branch als **eigene empirische Frage** weiterverfolgt wird, nicht als Rettungsversuch für Trias-Novelty. Selbst ein positiver ML-Effekt würde die Comparator-Problematik nicht lösen.

### C — Inverse v0.2

Nur bei einer neuen, unabhängig motivierten wissenschaftlichen Hypothese, z. B. einer realistisch begründeten Observation-Operator-/block-missingness-Frage. Nicht zulässig als bloße Erhöhung der Missingness bis der gewünschte Effekt erscheint.

### D — Projekt beenden / stark verkleinern

Falls das Ziel zwingend eine methodologisch **neue** V&V-/AI-for-Science-Theorie ist, ist die derzeitige Evidenz dafür nicht ausreichend.

---

## 12. Empfehlung

**Empfohlen wird Option A.**

C06-R sollte zu C06-R2 präzisiert werden. Die Trias wird als fachübergreifende Directed-Audit-Linse und konzeptionelle Synthese positioniert, nicht als neue Credibility- oder Identifiability-Theorie. Der ML-v0.2- und inverse-v0.2-Branch bleiben archiviert/pausiert und werden nicht mehr zur Hauptroute gemacht.

Der nächste Schritt sollte deshalb kein Experiment sein, sondern ein **Paper Contribution Boundary + Outline v0.1**: exakter Hauptclaim, Non-Claims, Comparator-Matrix, Rolle jedes Demonstrators und Entscheidung, welches Resultat in Haupttext bzw. Appendix gehört.

## Literaturanker

- NASA-STD-7009B (2024), *Standard for Models and Simulations*.
- NASA-HDBK-7009B (2026), Implementierungsleitfaden zu NASA-STD-7009B.
- Jakeman, Barba, Martins & O'Leary-Roseberry (2026), *Verification and validation for trustworthy scientific machine learning*, Machine Learning: Science and Technology 7, 025055.
- W3C (2013), PROV-DM / PROV Primer / PROV Overview.
- Khan, Soiland-Reyes & Sinnott (2019), *Sharing interoperable workflow provenance: ... CWLProv*, GigaScience 8(11).
- Villaverde, Barreiro & Papachristodoulou (2016), *Structural Identifiability of Dynamic Systems Biology Models*, PLoS Computational Biology.
- Hadaegh & Bekey (1985), *Near-identifiability of dynamical systems*, Mathematical Biosciences 77, 325–340.
- SINDy robustness literature, including robust sparse-identification extensions such as SINDy-PI.
- Assurance-case / Goal Structuring Notation literature on claims, arguments, context and evidence.