# Evidence Register

Dieses Register dokumentiert, welche Evidenz für die einzelnen Claims benötigt wird. Es trennt externe Literaturbelege von projektinternen methodologischen Setzungen und Ergebnissen des Demonstrators.

## E01 — Evidenz für C01

**Claim:** diagnostischer Mehrwert der Trias.

### Benötigte externe Evidenz

- Wissenschaftsphilosophie zu Computational Science und Computersimulation.
- Arbeiten, die Modelle oder Simulationen als vermittelnde bzw. eigenständige epistemische Praxis behandeln.
- Gegenpositionen gegen einen zu starken Sonderstatus von Simulation.
- Literatur zu Modellvalidierung, numerischer Fehleranalyse, System Identification, Identifiability und Reproduzierbarkeit als Vergleichsmaßstab.

### Benötigte interne Evidenz

Der Drei-Körper-Demonstrator und mindestens ein inverser AI-for-Science-Fall müssen prüfen, ob die explizite gerichtete Zuordnung von Zielsystem, Theorie, operativer Vermittlung und Zwischenartefakten eine spezifischere Integrations-/Rechtfertigungsstruktur ermöglicht als etablierte Alternativen.

### Aktueller Status

**PARTIAL / UNDER TEST.** Der Solverfall stützt C05, aber nicht eine starke Neuheitsbehauptung. D015 verschiebt den nächsten Test auf eine Directed-Trias-Fassung, die Forward- und Inverse-Transformationen gemeinsam auditiert.

---

## E02 — Evidenz für C02

**Claim:** ein synthetisches Zielsystem kann im Audit die methodologische Rolle des Realitäts-Pols übernehmen.

### Benötigte externe Evidenz

- etablierte Verwendung des Begriffs `target system` in der Philosophie wissenschaftlicher Repräsentation,
- Literatur zur Modell–Target- bzw. Modell–Welt-Beziehung,
- Prüfung, ob auch hypothetische, konstruierte oder nicht unmittelbar empirische Targets zugelassen werden.

### Projektinterne Setzung

Die Zuordnung des konkret instanziierten Newtonschen Drei-Körper-Systems zum Realitäts-Pol der Trias ist **keine aus der Literatur abzuleitende Tatsache**, sondern eine methodologische Designentscheidung. Ihre Rechtfertigung hängt davon ab, ob sie diagnostisch produktiv ist.

### Aktueller Status

**ACCEPTED AS WORKING BASIS — D002.** Begrifflich anschlussfähig; die konkrete Trias-Rolle bleibt eine revidierbare methodologische Setzung.

---

## E03 — Evidenz für C03

**Claim:** Sundmans klassisches Resultat liefert unter der Voraussetzung nichtverschwindenden Gesamtdrehimpulses nach Regularisierung und Zeittransformation eine global konvergente Potenzreihendarstellung in einer Hilfsvariablen; die Darstellung ist wegen extrem langsamer praktischer Konvergenz für gewöhnliche Bahnberechnung ungeeignet.

### Gefundene Evidenz

- **Sundman, Mémoire sur le problème des trois corps, Acta Mathematica 36, 105–179.** Primärquelle des klassischen Resultats; bibliographische Datierung wird in Datenbanken teils 1912, teils 1913 geführt.
- **Belorizky (1930).** Praktische Untersuchung der Sundman-Methode; nennt die Bedingungen der Konstruktion und zeigt am speziellen Fall die extreme Zahl benötigter Reihenterme.
- **Henkel (2001).** Historisch-philosophische Darstellung; betont, dass entgegen einer verbreiteten Verkürzung eine analytische Lösung im präzisen Sinn einer konvergenten Reihenrepräsentation existiert.
- **Chenciner/Scholarpedia und Encyclopedia of Mathematics.** Moderne mathematische Zusammenfassungen: binäre Kollisionen werden regularisiert; bei nichtverschwindendem Gesamtdrehimpuls ist die totale Kollision ausgeschlossen; die Reihen sind wegen extrem langsamer Konvergenz praktisch nicht brauchbar.

### Noch zu kontrollieren

- endgültige bibliographische Jahresangabe für das Mémoire,
- exakte Form der Nichtnull-Drehimpuls-Bedingung in der zitierten Fassung,
- quantitative Termzahl-Angaben nur nach direkter Quellenrekonstruktion.

### Aktueller Status

**ACCEPTED AS WORKING BASIS — D003.** Qualitativer Kern gut gestützt.

---

## E04 — Evidenz für C04

**Claim:** mathematische Konvergenz, operative rechnerische Machbarkeit, numerische Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit sind verschiedene Bewertungsebenen.

### Gefundene Evidenz

- Standardliteratur der numerischen Analysis trennt Konvergenz, Stabilität, Kondition/Sensitivität und Fehlerfortpflanzung; formale Beziehungen zwischen den Begriffen werden ausdrücklich anerkannt.
- V&V-/Credibility-Literatur behandelt Akzeptabilität und Vertrauen relativ zum intended use und zu dokumentierter Evidenz.
- Die Simulationsphilosophie formuliert die Zuverlässigkeitsfrage explizit relativ zum vorgesehenen wissenschaftlichen Zweck.

### Projektinterne Begriffe

`operative rechnerische Machbarkeit` und `wissenschaftliche Nutzbarkeit` sind Synthese-/Auditbegriffe des Projekts und werden nicht als etablierte Standardtermini ausgegeben.

### Aktueller Status

**ACCEPTED — D004.** Die sechs-stufige Lösungsleiter bleibt erhalten. Identifizierbarkeit wird in D015 konsistent als querliegende Auditdimension behandelt, nicht als zusätzliche Stufe.

---

## E05 — Evidenz für C05

**Claim:** verschiedene numerische Operationalisierungen können bei gleichem Zielsystem/Theorie wissenschaftlich relevante, use-case-relative Fehler- und Strukturprofile erzeugen.

### Projektinterne Evidenz

Full Demonstrator v0.1:

- U1 reference gap `8.854e-12`, U2 reference gap `6.163e-08`;
- RK4 U1 observed orders `4.74, 4.62, 4.46, 4.30`;
- Verlet U1 observed orders `1.75, 1.87, 1.97, 1.99`;
- RK4 deutlich trajectory-genauer;
- Verlet deutlich kleinerer fitted secular energy drift und Drehimpulserhaltung nahe Rundungsniveau.

### Aktueller Status

**ACCEPTED — D008.** Moderate zweckrelative Fassung empirisch gestützt; keine globale Solverwinner-Aussage.

---

## E06 — Evidenz für C06-R

**Claim:** Im reinen Solverfall erzeugt die Trias keine eindeutig neuen numerischen Validierungsfragen; ihr derzeit belegbarer Mehrwert ist eine durchgängige Integrations-/Provenance-Zuordnung über Zielsystem, Theorie, Berechnung und wissenschaftlichen Gebrauch.

### Vergleichsquellen

- **NASA-STD-7009B (2024), Standard for Models and Simulations.** Umfasst credibility, verification, validation, sensitivity/uncertainty und acceptance criteria.
- **NASA M&S Use / User Guide guidance.** Intended use, assumptions/abstractions, permissible uses, uncertainty, sensitivity, robustness und supporting evidence gehören zum Credibility-/Use-Assessment.
- **Stanford Encyclopedia of Philosophy, Computer Simulations in Science.** Breite Simulation-Study-Perspektive umfasst Modellwahl, Implementierung, Rechner, Interpretation und Rechtfertigung; Verification wird in code und solution verification unterschieden; Validation ist zweckrelativ zur Repräsentation des target system.
- **Oberkampf/Roy/Trucano-artige V&V/UQ-Literatur.** Numerische Fehler, Modellfehler, Referenz-/Validierungsevidenz, Sensitivität und predictive capability sind etablierte Gegenstände.
- **Jakeman, Barba, Martins & O’Leary-Roseberry (2026), Verification and validation for trustworthy scientific machine learning.** SciML-Credibility umfasst Problemdefinition, Model Purpose, QoIs, Datencharakteristika/-verarbeitung, Verification, Validation, UQ, Sensitivität, Reproduzierbarkeit und Alternativenvergleich.

### Ergebnis des harten Vergleichs

Die C05-Diagnostik kann ohne Informationsverlust in Standard-Numerik/V&V/Credibility-Sprache ausgedrückt werden. Daher ist die starke C06-Fassung — neue numerische Validierungsfragen durch die Trias — im aktuellen Solverfall **nicht gestützt und verworfen**.

D015 prüft nun nur noch die schwächere Hypothese, ob eine gemeinsame richtungssensitive Audit-Grammatik für Forward- und Inverse-Transformationen eine nützliche Integrationsleistung erbringt.

### Aktueller Status

**ACCEPTED IN REVISED FORM — D009 / UNDER REFINEMENT D015.**

---

## E07 — Evidenz für den ursprünglichen ML-Provenance-Zweig

### Geplanter Claim-Kern

Kontrolliert unterscheiden zwischen:

- Qualität relativ zum numerischen Datengenerator,
- Qualität relativ zu einer stärkeren numerischen Referenz,
- Rollout-/Strukturverhalten des gelernten Modells,
- Herkunft einer Abweichung aus Theorie, Datengenerator, Trainingsdaten oder gelerntem Surrogat,
- wissenschaftlicher Schlussfolgerung relativ zum intended use.

### Projektinterne Evidenz

ML Full Run v0.1:

- Reference separation klar bestanden;
- paired initialization bestanden;
- Learner resolvability klar verletzt;
- Lernfehler etwa fünf Größenordnungen über der RK4-vs.-DOP853-Teacher-Differenz.

### Aktueller Status

**INCONCLUSIVE — D013.** v0.2 ist nach D014 technisch vorbereitet, der wissenschaftliche Full Run nach D015 strategisch pausiert. C07 bleibt NOT ASSESSABLE.

---

## E08 — Evidenz für C07-L / C07-L-R und Directed Trias

### Primäranker

- **Z.-M. Zhai, V. Lucarini, Y.-C. Lai, _Deficiency of equation-finding approach to data-driven modeling of dynamical systems_, arXiv:2509.03769; aktuelle Fassung 22. März 2026.**

Für chaotische Systeme, insbesondere Lorenz, berichten die Autoren:

- Missingness/gestörte Beobachtung;
- ML-basierte Rekonstruktion der Zeitreihe;
- sparse equation discovery;
- stark unterschiedliche inferierte Gleichungsstrukturen je nach Beobachtungs-/Missingness-Situation;
- dennoch ähnliche chaotische Attraktoren, Lyapunov-Exponenten und KL-basierte Verteilungsmaße;
- Übereinstimmung vieler dominanter Koopman-Eigenwerte bei stärkeren Unterschieden in subdominanten Bereichen.

### Starke Comparatoren

1. **Structural identifiability:** eindeutige Parameterbestimmung aus idealisierten Outputs bei vorgegebener Modellstruktur; u. a. Ljung & Glad (1994) sowie neuere Reviews.
2. **Practical identifiability / estimability:** Datenmenge, Rauschen, Sampling und Messgenauigkeit beeinflussen praktische Parameterbestimmung.
3. **Observability:** Rekonstruierbarkeit interner Zustände aus Outputs; structural identifiability kann als erweiterte Observability formuliert werden.
4. **Equifinality / observational equivalence:** mehrere Modelle/Parametrisierungen können mit denselben oder praktisch gleichen Beobachtungen vereinbar sein.
5. **Structural error / near-identifiability:** ältere System-Identification-Literatur behandelt ausdrücklich near-equivalence zwischen strukturell abweichenden Modellen und Prozessen unter Output-Toleranzen.
6. **Equation-discovery robustness:** SINDy-artige Verfahren sind bekanntermaßen sensitiv gegenüber Rauschen, Differentiation, Sampling, Library, Sparse Optimizer und Hyperparametern.
7. **Philosophy of science:** empirical equivalence, underdetermination und model pluralism sind etablierte Debatten.
8. **Provenance / SciML credibility:** W3C PROV, Scientific-Workflow-Provenance und moderne SciML-V&V verlangen bereits Dokumentation von Datenentstehung/-verarbeitung, Modellstruktur, Zweck, Unsicherheit und Reproduzierbarkeit.

### Ergebnis

**Starke C07-L-Neuheitsfassung nicht haltbar.** Die Aussage `operative/dynamische Äquivalenz impliziert nicht theoretische Identität` ist als allgemeine Grundidee stark etablierter Vorarbeit ausgesetzt.

### Verbleibende moderate Fassung

**C07-L-R / PENDING REVIEW:** Zhai–Lucarini–Lai dient als konkreter inverser Equation-Discovery-Fall. Der mögliche Trias-Anteil ist ausschließlich die projektinterne Integrationshypothese, Forward- und Inverse-Probleme in einer gemeinsamen richtungssensitiven Audit-Grammatik zu lokalisieren und jeweils zu markieren, welches epistemische Objekt tatsächlich validiert oder identifiziert wurde.

### Revisionskriterium

Wenn ein eigener inverser MVP und der anschließende Framework-Vergleich zeigen, dass diese Zuordnung vollständig ohne Rest in einer Kombination aus System Identification, Identifiability/Observability und SciML-V&V/Provenance aufgeht, wird die Directed-Trias-Neuheitsbehauptung weiter abgeschwächt oder aufgegeben.

Details: [`literature/c07_l_comparator_audit.md`](c07_l_comparator_audit.md).
