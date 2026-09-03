# W9 — Source & Bibliography Audit v0.1

**Status:** COMPLETE / PENDING AUTHOR DECISION  
**Stand:** 2026-09-03  
**Depends on:** D038, `paper/manuscript_integrated_v0_2.md`

## 1. Audit-Ziel

W9 prüft die extern gestützten Claims des integrierten Manuskripts gegen Primärquellen, Standards oder belastbare Fachquellen und trennt dabei:

```text
VERIFIED_PRIMARY / OFFICIAL
VERIFIED_SECONDARY
PREPRINT_ONLY
PROJECT_INTERNAL
REQUIRES_WORDING_CHANGE
```

Der Audit ist kein neuer Novelty-Test. Ein fehlender Direktanalog darf weiterhin nur als Ergebnis der dokumentierten Projekt-Audits formuliert werden, nicht als beweisbare universelle Abwesenheitsbehauptung.

## 2. Gesamturteil

```text
OVERALL = PASS_TO_SOURCE_INTEGRATION
```

Kein zentraler Manuskriptclaim fällt durch die Quellenprüfung. Die Genealogie, die vier AI-for-Science-Archetypen, der Zhai-Brückenfall, der Sundman-Kontrollfall und die Comparator-Boundary sind grundsätzlich belegbar.

Vor einer Submission sind aber **fünf verbindliche Quellen-/Wortlautkorrekturen** erforderlich:

1. Schlesinger 1979: `R-T` historisch als **model qualification** bezeichnen; `conceptual-model validity` Sargent zuordnen.
2. Zhai–Lucarini–Lai: ausschließlich als **arXiv preprint (2025), arXiv:2509.03769** zitieren; keine implizite peer-reviewte 2026-Publikation behaupten.
3. Sundman: Jahr im Manuskript/Bib konsistent auf **1912** setzen; Primärscan von Acta Mathematica 36 nennt Druckdatum 8. Juli 1912, obwohl manche spätere Metadaten 1913 führen.
4. Provenance: W3C PROV nicht so formulieren, als seien `parameters` eine eigene Kernklasse; Kernbegriffe sind insbesondere Entity, Activity, Agent sowie Usage/Generation/Derivation. Parameter können als Entities/Attribute modelliert werden.
5. Identifiability: Villaverde et al. stützen primär **parametrische structural identifiability**; Aussagen über strukturell verschiedene Modellformen müssen zusätzlich mit Hadaegh–Bekey / system-identification / equation-discovery Literatur gestützt werden.

Diese Änderungen schwächen P3 nicht.

---

# 3. Genealogie: Schlesinger / Sargent

## 3.1 Schlesinger et al. (1979)

**Bibliographie — VERIFIED PRIMARY / bibliographic + reproduced primary text**

Schlesinger, S.; Crosbie, R. E.; Gagné, R. E.; Innis, G. S.; Lalwani, C. S.; Loch, J.; Sylvester, R. J.; Wright, R. D.; Kheir, N.; Bartos, D. (1979). **Terminology for model credibility.** *SIMULATION*, 32(3), 103–104. DOI: `10.1177/003754977903200304`.

**Direkt gestützt:**

- Dreiteilung `REALITY – CONCEPTUAL MODEL – COMPUTERIZED MODEL`.
- `MODEL QUALIFICATION`: Angemessenheit des Conceptual Model relativ zu Intended Application.
- `MODEL VERIFICATION`: Computerized Model repräsentiert Conceptual Model innerhalb spezifizierter Genauigkeit.
- `MODEL VALIDATION`: Computerized Model besitzt innerhalb Domain of Applicability eine für Intended Application zufriedenstellende Genauigkeit.
- Damit ist Topologie-Novelty der Trias klar ausgeschlossen.

**Maximal zulässiger Manuskriptclaim:**

> The 1979 SCS credibility terminology already organized simulation credibility around reality, a conceptual model, and a computerized model, linked by qualification, verification, and validation.

**Nicht Schlesinger zuschreiben:** den späteren Terminus `conceptual-model validity` als 1979-Bezeichnung.

**Manuskriptstellen:** Abstract/Introduction knapp; Section 2 Hauptheimat; Section 7 Boundary nur Rückverweis.

## 3.2 Sargent (2013)

**Bibliographie — VERIFIED PRIMARY**

Sargent, R. G. (2013). **Verification and validation of simulation models.** *Journal of Simulation*, 7(1), 12–24. DOI: `10.1057/jos.2012.20`.

**Direkt gestützt:**

- `conceptual model validity`, `model verification`, `operational validity`, `data validity`.
- V&V relativ zum Model-Development-Prozess.
- verschiedene Validierungsansätze/-techniken.

**Maximal zulässiger Claim:**

> Sargent’s V&V formulation explicitly distinguishes conceptual-model validity, computerized/model verification, and operational validity.

**Audit-Folge:** Das Manuskriptmapping

```text
R-T ~ conceptual-model validity / qualification
T-C ~ verification
C-R ~ operational validity / validation
```

ist als **genealogische Approximation** zulässig, solange `~`/“approximately” beibehalten wird.

---

# 4. Moderne V&V / VVUQ / SciML-Credibility

## 4.1 NASA-STD-7009B

**VERIFIED OFFICIAL STANDARD**

NASA (2024). **NASA-STD-7009B, Standard for Models and Simulations**, Version B, document date 2024-03-05.

**Direkt gestützt:**

- M&S lifecycle / development and use;
- credibility assessment;
- V&V, sensitivity/UQ;
- acceptance criteria defined by program/project.

**Zulässiger Claim:** Moderne M&S-Credibility bindet Akzeptanz an purpose/context, credibility evidence und explizite Kriterien.

## 4.2 NASA-HDBK-7009B

**VERIFIED OFFICIAL HANDBOOK**

NASA (2026). **NASA-HDBK-7009B, NASA Handbook for Models and Simulations: An Implementation Guide for NASA-STD-7009B**, document date 2026-02-03.

**Rolle:** aktueller Companion für Good Practice; nicht nötig für jeden V&V-Satz, aber guter moderner Referenzanker.

## 4.3 ASME V&V 40-2018

**VERIFIED OFFICIAL STANDARD / DOMAIN-SPECIFIC**

ASME (2018). **V&V 40-2018: Assessing Credibility of Computational Modeling through Verification and Validation: Application to Medical Devices.**

**Direkt gestützt:** credibility commensurate with model reliance in a decision and consequence of wrong decision; adequacy/relevance of completed V&V activities.

**Boundary:** als **domain-specific credibility exemplar** zitieren, nicht als universeller Standard für alle Computational Science.

## 4.4 Jakeman et al. (2026)

**VERIFIED PRIMARY / PEER-REVIEWED**

Jakeman, J. D.; Barba, L. A.; Martins, J. R. R. A.; O’Leary-Roseberry, T. (2026). **Verification and validation for trustworthy scientific machine learning.** *Machine Learning: Science and Technology*, 7, 025055. DOI: `10.1088/2632-2153/ae59ec`.

**Direkt gestützt:** 16 Empfehlungen u.a.

```text
model purpose + prior knowledge
verification/calibration/validation/application domains
QoIs
model structure
code + solution verification
purpose-specific validation
uncertainty
training-data characteristics + processing
sensitivity
hyperparameters
reproducibility
comparison to alternatives
prediction mechanism / explainability
```

Die Arbeit unterscheidet explizit Verification und Validation und diskutiert auf Simulationen trainierte Surrogates sowie unabhängige Beobachtungsdaten für Validation.

**Manuskriptclaim:** stark gestützt; keine Abschwächung nötig.

---

# 5. AI-for-Science-Rollen

## 5.1 Naser (2025)

**VERIFIED PRIMARY / PEER-REVIEWED**

Naser, M. Z. (2025). **A decision architecture for epistemic prioritization: Machine learning at the intersection of technology and society.** *Technology in Society*, 83, 103039. DOI: `10.1016/j.techsoc.2025.103039`.

**Direkt gestützt:** P.E.D.U.D. = Prediction, Explanation, Discovery, Understanding, Decision-making als unterschiedliche epistemische Funktionen.

**Wortlautempfehlung:** statt breit

> philosophy of ML already distinguishes ...

präziser:

> recent methodological and philosophical work on ML explicitly distinguishes prediction, explanation, discovery, understanding, and decision-making (e.g. Naser, 2025).

Damit wird aus einem einzelnen Framework kein Feldkonsens behauptet.

## 5.2 Vinuesa et al. (2026)

**VERIFIED PRIMARY / PEER-REVIEWED PERSPECTIVE**

Vinuesa, R.; Cinnella, P.; Rabault, J.; et al. (2026). **Decoding complexity through machine learning is redefining scientific discovery.** *Communications Physics*, 9, 168. DOI: `10.1038/s42005-026-02676-7`.

**Direkt gestützt:** drei Problemtypen nach Wissen über governing equations:

```text
known
partial knowledge
little/no knowledge
```

und unterschiedliche ML-Rollen je nach theoretischem Kenntnisstand, u.a. surrogate modeling bei gut bekannten Gleichungen und representation/pattern discovery bei geringer Kenntnis.

**Audit:** starker Prior-Art-Anker gegen jede Einzelneuheit von `T=PRESENT/PARTIAL/NONE`.

## 5.3 Karniadakis et al. (2021)

**VERIFIED PRIMARY / PEER-REVIEWED REVIEW**

Karniadakis, G. E.; Kevrekidis, I. G.; Lu, L.; Perdikaris, P.; Wang, S.; Yang, L. (2021). **Physics-informed machine learning.** *Nature Reviews Physics*, 3, 422–440. DOI: `10.1038/s42254-021-00314-5`.

**Direkt gestützt:** Integration von Daten und mathematischer/physikalischer Struktur; breites PIML-Feld.

**Zulässiger Manuskriptclaim:** PIML/Hybridisierung ist etablierte Einzelpraxis; Trias erfindet diese Rollenform nicht.

## 5.4 Kramer et al. (2026)

**VERIFIED PRIMARY / PEER-REVIEWED REVIEW**

Kramer, S.; Cerrato, M.; Brugger, J.; Džeroski, S.; et al. (2026). **Automated Scientific Discovery: From Equation Discovery to Autonomous Discovery Systems.** *Machine Learning*, 115, article 109. DOI: `10.1007/s10994-025-06955-2`.

**Direkt gestützt:** equation discovery/symbolic regression als etablierte Methoden, deren Ziel häufig ein menscheninterpretierbares Modell der Dynamik in Gleichungsform ist; Neural Operators können Dynamik direkt lernen und Interpretierbarkeit aufgeben.

**Audit:** starker Anker für `C_infer -> T_hat` als etablierte Einzelpraxis; die Trias beansprucht nur cross-case Rollenlesart.

---

# 6. Zhai–Lucarini–Lai Bridge

## 6.1 Publikationsstatus

**PREPRINT_ONLY — verbindlich kennzeichnen**

Zhai, Z.-M.; Lucarini, V.; Lai, Y.-C. (2025). **Deficiency of equation-finding approach to data-driven modeling of dynamical systems.** arXiv:`2509.03769` [nlin.CD]. arXiv DOI: `10.48550/arXiv.2509.03769`.

ArXiv-Metadaten am 2026-09-03:

```text
submitted: 3 Sep 2025
version: v1 only
journal reference: none displayed
```

**Verbindliche Änderung:** Manuskript niemals als `2025/2026` oder implizit peer-reviewed zitieren. Verwenden:

> Zhai et al. (2025, preprint)

## 6.2 Claimprüfung

**Direkt durch Preprint gestützt:**

- zufällig fehlende / gestörte Beobachtungen als Motivation;
- ML-basierte Rekonstruktion/Imputation;
- sparse equation discovery;
- strukturell stark verschiedene inferierte Gleichungen unter unterschiedlichen Mess-/Rekonstruktionsbedingungen;
- ähnliche chaotische Attraktoren nach ausgewählten Langzeitmaßen;
- Übereinstimmung vieler dominanter Koopman-Eigenwerte, Unterschiede stärker in subdominanten Teilen;
- Warnung vor zu starker physikalischer Interpretation inferierter Gleichungen.

**Nicht zulässig:**

- universelle Nichtidentifizierbarkeit;
- physikalische Äquivalenz der Gleichungen;
- Beweis, dass direkte ML-Modellierung allgemein überlegen ist;
- positive Validierung der Trias.

Der aktuelle Manuskriptclaim liegt innerhalb dieser Boundary.

---

# 7. Sundman-Kontrollfall

## 7.1 Sundman (1912)

**VERIFIED PRIMARY**

Sundman, K. F. (1912). **Mémoire sur le problème des trois corps.** *Acta Mathematica*, 36, 105–179. DOI: `10.1007/BF02422379`.

**Datumsentscheidung:** Primärscan von *Acta Mathematica* 36 enthält `Imprimé le 8 juillet 1912`; zahlreiche mathematische Kataloge führen ebenfalls 1912. Einige spätere DOI-/Springer-Metadaten führen 1913. Für dieses Manuskript wird **1912** verwendet und die Bibliographie intern konsistent gehalten.

**Direkt/über zeitgenössische Reproduktion gestützt:** nach Regularisierung/Variablentransformation konvergente Potenzreihendarstellung, reale Zeitachse über regularisierte Variable; Bedingung nichtverschwindender Flächen-/Drehimpulskonstanten; binäre Kollisionen werden regularisiert.

## 7.2 Belorizky (1930)

**VERIFIED PRIMARY**

Belorizky, D. (1930). **Application pratique des méthodes de M. Sundman à un cas particulier du problème des trois corps.** *Bulletin astronomique. Mémoires et variétés*, 6, 417–434. DOI: `10.3406/bastr.1930.14038`.

Die zugängliche Primärseite bestätigt die Sundman-Transformation, Holomorphie/Serienentwicklung und globale reale Zeitabbildung sowie die bibliographischen Daten.

## 7.3 Sekundäranker für praktische Ineffizienz

Henkel, M. (2001). **Sur la solution de Sundman du problème des trois corps.** *Philosophia Scientiae*, 5(2), 161–184. Numdam.

Chenciner, A. (2007). **Three body problem.** *Scholarpedia*, 2(10):2111. DOI: `10.4249/scholarpedia.2111`.

Musielak, Z. E.; Quarles, B. (2014). **The three-body problem.** *Reports on Progress in Physics*, 77, 065901. DOI: `10.1088/0034-4885/77/6/065901`.

**Direkt gestützt:** Sundmans Serien konvergieren, sind aber wegen extrem langsamer praktischer Konvergenz für Bahnberechnung nicht brauchbar.

**Verbindlicher Guardrail:** keine spektakuläre Termzahl im Hauptargument; qualitative Form `extremely slow / of no practical use for trajectory computation` genügt.

---

# 8. Provenance-Comparator

## 8.1 W3C PROV

**VERIFIED OFFICIAL STANDARD FAMILY**

W3C (2013). **PROV Model Primer.** W3C Working Group Note, 30 April 2013.

**Direkt gestützt:** provenance representation über `Entity`, `Activity`, `Agent`, einschließlich `Usage`, `Generation`, `Derivation`; Herkunft und Transformationsprozesse digitaler Objekte.

**Wortlautänderung:** In Section 7 Kernliste auf diese Begriffe beschränken. `parameters` nur als mögliche Entities/Attribute erwähnen, nicht als PROV-Kernklasse.

## 8.2 CWLProv

**VERIFIED PRIMARY / PEER-REVIEWED**

Khan, F. Z.; Soiland-Reyes, S.; Sinnott, R. O.; Lonie, A.; Goble, C.; Crusoe, M. R. (2019). **Sharing interoperable workflow provenance: A review of best practices and their practical application in CWLProv.** *GigaScience*, 8(11), giz095. DOI: `10.1093/gigascience/giz095`.

**Direkt gestützt:** prospective/retrospective scientific workflow provenance and interoperable provenance packaging.

**Audit:** stark genug für Claim, dass Pipeline-Lineage und Zwischenartefakte keine Trias-Neuheit sind.

---

# 9. Assurance Cases / Claim–Evidence

## 9.1 Goodenough, Weinstock & Klein (2012)

**VERIFIED OFFICIAL TECHNICAL REPORT**

Goodenough, J. B.; Weinstock, C.; Klein, A. Z. (2012). **Toward a Theory of Assurance Case Confidence.** CMU/SEI-2012-TR-002. DOI: `10.1184/R1/6585362.v1`.

**Direkt gestützt:** Assurance Case = Claim + Argument + Evidence; explizite Begründung, wie Evidenz einen Claim stützt.

## 9.2 GSN Community Standard v3

**VERIFIED STANDARD**

Assurance Case Working Group (2021). **Goal Structuring Notation Community Standard, Version 3**, 4 May 2021.

**Direkt gestützt:** standardisierte Strukturierung von Engineering Arguments; Goals/Claims, Strategies, Context, Solutions/Evidence.

**Audit:** Bridge Claims dürfen nur als Trias-Markierung für nötige inferentielle Arbeit beschrieben werden, nicht als neue Argumentationsmethode.

---

# 10. Identifiability / System Identification / Equation Discovery

## 10.1 Villaverde, Barreiro & Papachristodoulou (2016)

**VERIFIED PRIMARY / PEER-REVIEWED**

Villaverde, A. F.; Barreiro, A.; Papachristodoulou, A. (2016). **Structural Identifiability of Dynamic Systems Biology Models.** *PLoS Computational Biology*, 12(10), e1005153. DOI: `10.1371/journal.pcbi.1005153`.

**Direkt gestützt:** structural identifiability von Parametern in ODE-Modellen; unidentifizierbare Parameter können aus idealisierten Outputs nicht eindeutig bestimmt werden.

**Boundary:** nicht allein für freie Modellstruktur-/Termselektion verwenden.

## 10.2 Hadaegh & Bekey (1985)

**VERIFIED PRIMARY / PEER-REVIEWED**

Hadaegh, F. Y.; Bekey, G. A. (1985). **Near-identifiability of dynamical systems.** *Mathematical Biosciences*, 77(1–2), 325–340. DOI: `10.1016/0025-5564(85)90104-X`.

**Direkt gestützt:** structural model error, near-equivalence under output/modeling-error bounds, near-identifiability.

**Audit:** wichtiger Comparator für `structurally different but output-near-equivalent`.

## 10.3 Brunton, Proctor & Kutz (2016)

**VERIFIED PRIMARY / PEER-REVIEWED**

Brunton, S. L.; Proctor, J. L.; Kutz, J. N. (2016). **Discovering governing equations from data by sparse identification of nonlinear dynamical systems.** *PNAS*, 113(15), 3932–3937. DOI: `10.1073/pnas.1517384113`.

**Direkt gestützt:** sparse regression / SINDy as data-driven equation discovery and system identification.

## 10.4 Kaheman, Kutz & Brunton (2020)

**VERIFIED PRIMARY / PEER-REVIEWED**

Kaheman, K.; Kutz, J. N.; Brunton, S. L. (2020). **SINDy-PI: a robust algorithm for parallel implicit sparse identification of nonlinear dynamics.** *Proceedings of the Royal Society A*, 476(2242), 20200279. DOI: `10.1098/rspa.2020.0279`.

**Direkt gestützt:** noise sensitivity of prior implicit approaches and explicit robustness improvements.

**Boundary:** nicht als universeller Beleg für jede Support-Instabilität verwenden; Zhai und der eigene inverse Branch liefern den konkreten Reconstruction/measurement Fall.

---

# 11. Projektinterne Evidenz

Die folgenden Manuskriptaussagen benötigen keine externe Quelle für ihre numerischen Werte, sondern müssen auf das Repository/Supplement verweisen:

```text
Figure-eight full run
Lorenz/SINDy inverse full run = INFORMATIVE_NEGATIVE
ML provenance v0.1 = INCONCLUSIVE_LEARNER_ERROR
project comparator audits / survival gates
```

Externe Literatur darf diese Resultate kontextualisieren, aber nicht als Quelle ihrer Zahlen behandelt werden.

---

# 12. Quellenbedingte Manuskriptänderungen v0.3

Vor dem journal-spezifischen Pass sind folgende Änderungen verpflichtend:

```text
W9-R1  Schlesinger: model qualification vs Sargent: conceptual-model validity sauber trennen.
W9-R2  Zhai: 2025 arXiv preprint, v1, keine Journalreferenz; "2025/2026" entfernen.
W9-R3  Sundman: 1912 konsistent; bei Bedarf kurze bibliographische Notiz zur Metadatenabweichung.
W9-R4  W3C PROV Kernterminologie korrigieren; "parameters" nicht als core class.
W9-R5  Identifiability-Claim auf parameter-identifiability begrenzen und structure-selection mit Hadaegh/System-ID ergänzen.
W9-R6  Naser als konkretes aktuelles Framework formulieren, nicht als alleiniger Beweis eines gesamten Philosophy-of-ML-Feldkonsenses.
W9-R7  ASME V&V 40 ausdrücklich als domain-specific credibility standard kennzeichnen, falls verwendet.
W9-R8  "no single direct analogue" immer als "no direct analogue identified in our documented audits" formulieren.
```

Keine dieser Revisionen erfordert eine Änderung von P3.

---

# 13. Reference-set status

```text
classical credibility genealogy       = VERIFIED
modern M&S credibility                = VERIFIED
predictive SciML V&V                  = VERIFIED
ML epistemic functions                = VERIFIED with wording precision
ML roles by theory availability       = VERIFIED
PIML                                  = VERIFIED
automated/equation discovery          = VERIFIED
Zhai reconstruction/discovery bridge  = VERIFIED AS PREPRINT ONLY
Sundman convergence + practicality    = VERIFIED
workflow provenance                   = VERIFIED
assurance claim-evidence structure    = VERIFIED
parameter identifiability             = VERIFIED
near-equivalence / structural error   = VERIFIED
SINDy / sparse system identification  = VERIFIED
```

## 14. Gesamtklassifikation

```text
source coverage              = PASS
bibliographic resolvability  = PASS
central claim support        = PASS
required wording revisions   = YES / TARGETED
blocking source gap          = NO
--------------------------------------
OVERALL                      = PASS_TO_SOURCE_INTEGRATION
```

## 15. Nächste Abhängigkeit

Empfehlung: **W9 = PASS_TO_SOURCE_INTEGRATION akzeptieren.**

Danach W10:

> **Source-Hardened Manuscript v0.3 — integrate W9-R1…R8, attach verified citations/BibTeX, standardize citation keys, and produce a source-clean manuscript without changing P3.**

Erst nach W10 sollte das Zieljournal festgelegt und ein journal-spezifischer Stil-/Submission-Pass durchgeführt werden.