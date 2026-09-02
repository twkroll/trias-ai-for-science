# C07-L Comparator Audit — Identifiability, Observability, Equifinality, System Identification, SciML Credibility

**Status:** COMPLETE FOR CLAIM REVIEW  
**Stand:** 2026-09-02  
**Purpose:** prüfen, welcher Teil des Lucarini–Trias-Bridge-Claims durch Literatur gestützt ist, welcher Teil etablierte Vorarbeit wiederholt und welcher mögliche Trias-Beitrag nach dem Vergleich übrig bleibt.

## 1. Literaturkern Zhai–Lucarini–Lai

Primäranker:

- Zheng-Meng Zhai, Valerio Lucarini, Ying-Cheng Lai, *Deficiency of equation-finding approach to data-driven modeling of dynamical systems*, arXiv:2509.03769; aktuelle Fassung 22. März 2026.

Das Manuskript stützt für mehrere chaotische Systeme, insbesondere Lorenz, folgende konkrete Kette:

```text
chaotisches Zielsystem
-> Mess-/Missingness-Realisierung
-> ML-basierte Datenrekonstruktion
-> sparse equation discovery
-> strukturell verschiedene inferierte ODEs
-> sehr ähnliche Attraktoren / Lyapunov-Exponenten / dominante Koopman-Strukturen
```

Im Lorenz-Beispiel berichten die Autoren bei unterschiedlichen Missingness-Verhältnissen deutlich verschiedene Gleichungssätze mit zusätzlichen, fehlenden oder stark veränderten Termen/Koeffizienten, während die rekonstruierten Systeme ähnliche chaotische Attraktoren und Lyapunov-Exponenten erzeugen. Die dominanten Koopman-Eigenwerte stimmen über einen größeren Bereich überein; Unterschiede treten stärker in subdominanten Bereichen auf.

### Direkt gestützter Schluss

Für diesen experimentellen Aufbau gilt:

```text
starke dynamisch/statistische Ähnlichkeit
not=> identische inferierte Gleichungsstruktur
```

und die konkrete Beobachtungs-/Rekonstruktionspipeline beeinflusst das Equation-Discovery-Ergebnis.

### Nicht direkt gestützt

Das Paper beweist weder allgemeine Nichtidentifizierbarkeit datengetriebener Dynamik noch eine universelle Unmöglichkeit physikalisch interpretierbarer Equation Discovery. Seine normative Empfehlung zugunsten direkter datengetriebener/ML-Methoden ist zudem von der empirischen Diagnose logisch zu trennen.

---

## 2. Comparator A — Structural identifiability

Klassische structural identifiability fragt bei **vorgegebener Modellstruktur**, ob unbekannte Parameter aus idealisierten, rauschfreien Outputs eindeutig bestimmt werden können. In der üblichen ODE-Fassung gilt beispielsweise sinngemäß:

```text
y(t,p_hat) = y(t,p*)  =>  p_hat = p*
```

für globale Identifizierbarkeit unter den jeweiligen Regularitätsbedingungen.

Relevante Anker:

- Bellman/Åström-Tradition der structural identifiability;
- Ljung & Glad (1994), *On global identifiability for arbitrary model parametrizations*;
- Villaverde et al. / Systems-Biology-Reviews zu structural identifiability und observability.

### Überlappung mit C07-L

Hoch bezüglich der Grundfrage `Output -> eindeutige interne/theoretische Größe?`.

### Wichtiger Unterschied

Zhai–Lucarini–Lai variiert faktisch nicht nur Parameter innerhalb einer fest fixierten korrekten Modellstruktur. Die inferierte **Term-/Gleichungsstruktur selbst** ändert sich. Daher ist die klassische Parameter-identifiability-Terminologie allein zu eng, um den konkreten Befund vollständig zu beschreiben.

### Novelty-Folge

C07-L darf Nicht-Eindeutigkeit nicht als neue Entdeckung der Trias darstellen. Structural identifiability ist ein klarer Prior-art-Comparator.

---

## 3. Comparator B — Practical identifiability / estimability

Practical identifiability behandelt, ob Parameter unter endlichen, verrauschten, unvollständigen oder ungünstig verteilten Daten praktisch hinreichend bestimmt werden können. Sie hängt stärker von Messgenauigkeit, Sampling, Experimentdesign und real verfügbaren Daten ab als structural identifiability.

### Überlappung

Sehr hoch mit dem Aspekt, dass Missingness und Rekonstruktion die inferierten Resultate beeinflussen.

### Unterschied

Auch practical identifiability wird häufig innerhalb einer vorgegebenen Modellfamilie formuliert. Der Zhai-Fall enthält zusätzlich **Modellstrukturwahl/Termselektion** durch sparse equation discovery.

### Novelty-Folge

Die Beobachtung, dass Mess-/Datenqualität die inverse Inferenz beeinflusst, ist vollständig etablierte Vorarbeit und kein Trias-Claim.

---

## 4. Comparator C — Observability

Observability fragt, ob interne Zustände aus verfügbaren Outputs unterschieden bzw. rekonstruiert werden können. In nichtlinearen Systemen existieren klassische lokale Rangbedingungen; structural identifiability kann durch Parameters-as-states als erweiterte Observability behandelt werden.

### Überlappung

Observability betrifft die gerichtete Kante

```text
R -> C_obs -> state information
```

und ist deshalb für die Directed-Trias-Terminologie direkt relevant.

### Unterschied

Observability allein beantwortet nicht die nachgelagerte Frage, welche symbolische Gleichungsstruktur eine konkrete Preprocessing-/Equation-Discovery-Pipeline auswählt.

### Novelty-Folge

`R -> C` als nichttriviale epistemische Transformation ist keineswegs neu. Die Trias darf höchstens die Position dieser Frage in einem größeren Audit graphisch/konzeptionell integrieren.

---

## 5. Comparator D — Equifinality / observational equivalence / model non-uniqueness

In mehreren Disziplinen ist seit Langem etabliert, dass verschiedene Modelle oder Parametrisierungen mit denselben oder praktisch nicht unterscheidbaren Beobachtungen vereinbar sein können.

Relevante Anker:

- Errors-in-variables-Systemidentifikation: Klassen observationally equivalent systems;
- Beven (2001) zur Equifinality in hydrologischer Modellierung;
- philosophische Literatur zu empirischer Äquivalenz und underdetermination;
- Philosophie wissenschaftlicher Modelle: mehrere inkompatible Modelle können für bestimmte Zwecke empirisch/prediktiv erfolgreich sein.

### Überlappung

Sehr hoch mit der projektinternen Notation

```text
T1 ~_(O,epsilon) T2
```

für observable- und toleranzrelative operative Äquivalenz.

### Konsequenz

Die **Idee einer Äquivalenzklasse von Modellen nach ausgewählten Observablen ist nicht neu**. Unsere Notation kann als Auditkonvention nützlich sein, darf aber nicht als theoretische Innovation verkauft werden.

---

## 6. Comparator E — System identification mit structural error / near-identifiability

Besonders wichtig ist die ältere Literatur zu `structural error and identifiability` bzw. `near-identifiability`.

Diese Arbeiten thematisieren ausdrücklich, dass klassische structural identifiability häufig eine korrekt spezifizierte Modellstruktur voraussetzt, und führen Äquivalenz bzw. Near-Equivalence zwischen Prozess und Modell unter Modellstrukturfehlern und Output-Toleranzen ein.

### Überlappung

**Sehr hoch.** Dieser Comparator liegt konzeptionell näher am geplanten C07-L als klassische Parameteridentifizierbarkeit.

Er enthält bereits die Idee:

```text
strukturell nicht identisches Modell
+ kleine Output-Abweichung
-> Near-Equivalence / begrenzte Unterscheidbarkeit
```

### Konsequenz

Eine starke Behauptung wie

> „Die Trias entdeckt, dass dynamische Äquivalenz theoretische Identität nicht garantiert“

ist nicht haltbar. Das ist in unterschiedlichen Fachsprachen lange bekannt.

---

## 7. Comparator F — Equation-discovery robustness

Die SINDy-/Equation-Discovery-Literatur behandelt bereits ausführlich:

- Messrauschen;
- numerische Ableitung;
- Sampling/Zeitschritt;
- Sparse-Regression-Verfahren;
- Regularisierungs-/Threshold-Hyperparameter;
- Library-Wahl;
- Robustheitsverbesserungen wie weak/ensemble/implicit/RK-inspired SINDy.

### Überlappung

Sehr hoch mit der Aussage, dass die konkrete Inferenzpipeline den gefundenen Gleichungssatz beeinflusst.

### Spezifischer Wert von Zhai–Lucarini–Lai

Der interessante zusätzliche empirische Kontrast liegt nicht nur in `noise makes equation recovery hard`, sondern in der Kombination:

```text
sehr verschiedene gefundene Gleichungen
+
nahezu gleiche relevante chaotische Langzeitdynamik
```

inklusive Lyapunov-/KL-/Koopman-Vergleichen.

Dieser Kontrast ist als **Fallstudie** für unsere Theorie sehr wertvoll, aber kein Beleg für Trias-Neuheit.

---

## 8. Comparator G — Philosophy of science: underdetermination and model pluralism

Die Philosophie der Wissenschaft diskutiert seit Langem empirische Äquivalenz, underdetermination und die Koexistenz mehrerer teilweise inkompatibler, aber empirisch erfolgreicher Modelle.

### Überlappung

Sehr hoch mit dem philosophischen Satz:

```text
empirischer/predictiver Erfolg
not=> eindeutige wahre theoretische Repräsentation
```

### Unterschied

Die Directed Trias könnte stärker auf **konkrete computational transformations** fokussieren: Missingness, Imputation, Differentiation, Sparse Regression, Solver, Surrogate usw. Damit wird ein abstraktes Underdeterminationsproblem an konkrete wissenschaftliche Pipelines gebunden.

### Novelty-Folge

Auch diese Bindung muss als methodologische Synthese, nicht als neue Grundthese über Theorie und Evidenz formuliert werden.

---

## 9. Comparator H — V&V / Scientific ML credibility / provenance

Aktuelle SciML-V&V-Arbeiten fordern bereits explizit:

- Modellzweck und quantities of interest;
- Dokumentation von Modellstruktur;
- Dokumentation von Datencharakteristika und Datenverarbeitung;
- Code-/Solution-Verification;
- Validation gegen purpose-specific requirements;
- UQ, Sensitivität, Reproduzierbarkeit und Alternativenvergleich.

W3C PROV und wissenschaftliche Workflow-Provenance modellieren zudem Herkunft, Aktivitäten und Transformationen digitaler Artefakte.

### Überlappung

Sehr hoch mit dem allgemeinen Wort `provenance`.

### Unterschied

W3C-/Workflow-Provenance ist primär eine Repräsentation der Entstehungsgeschichte von Daten/Artefakten. SciML-V&V ist primär Credibility-/Validation-orientiert. Die Trias versucht stärker, **epistemische Rollen** und die Richtung der Übersetzung zwischen Target, Theory und Computation gemeinsam zu markieren.

### Novelty-Folge

Auch der Integrationsclaim ist noch **nicht bewiesen**. Existierende SciML-Credibility-Frameworks sind inzwischen so breit, dass ein Trias-Paper seinen Mehrwert nicht mit `we document data processing and purpose` begründen kann.

---

## 10. Ergebnis des Comparator-Audits

### Starke C07-L-Fassung

**REJECT AS NOVELTY CLAIM.**

Nicht neu sind:

- Nichtidentifizierbarkeit;
- observational equivalence / equifinality;
- Modellstrukturfehler und near-equivalence;
- Mess-/Sampling-/Preprocessing-Sensitivität von System Identification;
- pipelineabhängige Equation Discovery;
- empirische Unterbestimmtheit / Modellpluralität;
- allgemeine Provenance-Dokumentation.

### Was als wissenschaftlicher, literaturgestützter Claim übrig bleibt

Zhai–Lucarini–Lai liefert einen aktuellen, besonders anschaulichen **Equation-Discovery-Fall**, in dem Beobachtungs-/Rekonstruktionsprovenance mit stark variierender inferierter Gleichungsstruktur zusammenfällt, während mehrere relevante dynamische/statistische Eigenschaften ähnlich bleiben.

### Was als Trias-Hypothese übrig bleibt

Der potenzielle Eigenbeitrag ist enger:

> Ein Directed-Trias-Audit könnte etablierte Forward-Fragen (Operationalisierung, Numerical V&V, Surrogate Credibility) und etablierte Inverse-Fragen (Observation, Identifiability, Equation Discovery, observational equivalence) in einer gemeinsamen, richtungssensitiven Audit-Grammatik abbilden und dadurch sichtbar machen, **welches epistemische Objekt an welchem Übergang tatsächlich gerechtfertigt wurde**.

Dies ist eine **Integrationshypothese**, keine neue mathematische Identifiability-Theorie.

---

## 11. Empfohlene revidierte Claim-Fassung C07-L-R

> **C07-L-R:** Bei datengetriebener Equation Discovery ist die Güte eines inferierten Modells mehrdimensional: strukturelle Übereinstimmung der Gleichungen, dynamisch-statistische Adäquanz und physikalische Interpretierbarkeit sind nicht gleichzusetzen. Zhai, Lucarini und Lai liefern einen konkreten chaotischen Fall, in dem unterschiedliche Beobachtungs-/Rekonstruktionsbedingungen zu strukturell verschiedenen inferierten ODEs führen, während ausgewählte Langzeit- und Koopman-Eigenschaften ähnlich bleiben. Für die Trias dient dieser Befund nicht als neue Identifiability-Theorie, sondern als inverser Testfall für die Hypothese, dass wissenschaftliche Rechtfertigung die Provenance und Richtung der Transformation `target/observation -> data -> inference -> theory` explizit auditieren sollte.

### Status

**PENDING REVIEW.**

Der erste Satz ist breit an etablierte Literatur anschlussfähig. Der zweite Satz ist durch Zhai–Lucarini–Lai empirisch gestützt. Der dritte Satz ist projektinterne methodologische Interpretation.

---

## 12. Empfohlener nächster Experimentalschritt

Vor ML-v0.2 wird ein minimaler **inverse-direction MVP** spezifiziert.

Empfohlener Scope:

```text
Lorenz-63 ground truth
-> 3 kontrollierte Observation/Preprocessing-Pipelines
-> eine identische eingefrorene SINDy-Pipeline
-> inferierte Gleichungen
-> structural distance / coefficient support
-> dynamical/statistical comparison
```

Mindestvergleich:

1. vollständige saubere Daten;
2. kontrollierte Missingness + eine festgelegte Rekonstruktion;
3. zweite kontrollierte Missingness-/Rekonstruktionsrealisierung bei gleicher Missingness-Rate.

Primäre Outputs:

- Term-support und Koeffizientendifferenz zur Ground-truth-Gleichung;
- Attraktorgeometrie/Verteilungsdistanz;
- Lyapunov-Spektrum oder mindestens größter Lyapunov-Exponent;
- optional erst danach dominante Koopman-Eigenwerte.

Der MVP soll **nicht** Zhai–Lucarini–Lai vollständig replizieren. Er soll nur testen, ob die Directed Trias bei einem inversen Problem eine klarere Zuordnung von `Observation -> Reconstruction -> Inference -> Theory -> Dynamical use` liefert als eine einfache Aussage `SINDy is sensitive to missing data`.

---

## 13. Entscheidungsempfehlung

1. C07-L in der starken Neuheitsfassung verwerfen.
2. C07-L-R als moderate, literaturgestützte Arbeitsfassung akzeptieren.
3. Directed Trias weiterhin nur als Integrationshypothese behandeln.
4. Als nächsten Schritt einen **Minimal Inverse-Direction Demonstrator v0.1** spezifizieren; noch kein Code.
5. ML-v0.2 pausiert lassen, bis nach diesem MVP entschieden wird, welcher AI-for-Science-Zweig den stärkeren Erkenntnisgewinn verspricht.
