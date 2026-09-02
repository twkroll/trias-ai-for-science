# Evidence Register

Dieses Register dokumentiert, welche Evidenz für die einzelnen Claims benötigt wird. Es trennt externe Literaturbelege von projektinternen methodologischen Setzungen und Ergebnissen des Demonstrators.

## E01 — Evidenz für C01

**Claim:** diagnostischer Mehrwert der Trias.

### Benötigte externe Evidenz

- Wissenschaftsphilosophie zu Computational Science und Computersimulation.
- Arbeiten, die Modelle oder Simulationen als vermittelnde bzw. eigenständige epistemische Praxis behandeln.
- Gegenpositionen gegen einen zu starken Sonderstatus von Simulation.
- Literatur zu Modellvalidierung, numerischer Fehleranalyse und Reproduzierbarkeit als Vergleichsmaßstab.

### Benötigte interne Evidenz

Der Drei-Körper-Demonstrator muss mindestens einen Fall liefern, in dem die explizite Trennung von Zielsystem, Theorie und Implementierung eine spezifischere Diagnose oder Validierungsanforderung ermöglicht als eine undifferenzierte Beschreibung des Resultats als „numerischer Fehler“.

### Aktueller Status

**PARTIAL / UNDER REVISION.** Der Demonstrator stützt C05, aber der harte C06-Vergleich spricht gegen eine starke Neuheitsbehauptung für die Trias im reinen Solverfall.

---

## E02 — Evidenz für C02

**Claim:** ein synthetisches Zielsystem kann im Audit die methodologische Rolle des Realitäts-Pols übernehmen.

### Benötigte externe Evidenz

- etablierte Verwendung des Begriffs `target system` in der Philosophie wissenschaftlicher Repräsentation,
- Literatur zur Modell–Target- bzw. Modell–Welt-Beziehung,
- Prüfung, ob auch hypothetische, konstruierte oder nicht unmittelbar empirische Targets zugelassen werden.

### Projektinterne Setzung

Die Zuordnung des konkret instanziierten Newtonschen Drei-Körper-Systems zum Realitäts-Pol der Trias ist **keine aus der Literatur abzuleitende Tatsache**, sondern eine methodologische Designentscheidung. Ihre Rechtfertigung hängt davon ab, ob sie später diagnostisch produktiv ist.

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

**ACCEPTED — D004.**

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

## E06 — Evidenz für C06

**Frage:** Leistet die Trias gegenüber etablierter numerischer Analysis/V&V/Credibility zusätzliche diagnostische Arbeit?

### Vergleichsquellen

- **NASA-STD-7009B (2024), Standard for Models and Simulations.** Etabliert uniform practices für Design, Entwicklung und Nutzung von M&S; umfasst credibility, verification, validation, sensitivity/uncertainty und acceptance criteria.
- **NASA M&S Use / User Guide guidance.** Intended use, assumptions/abstractions, permissible uses, uncertainty, sensitivity, robustness und dokumentierte supporting evidence gehören ausdrücklich zum Credibility-/Use-Assessment.
- **Stanford Encyclopedia of Philosophy, Computer Simulations in Science, Revision 2026.** Breite Simulation-Study-Perspektive umfasst Modellwahl, Implementierung, Rechner, Interpretation und Rechtfertigung; Verification wird in code und solution verification unterschieden; Validation ist zweckrelativ zur Repräsentation des target system.
- **Oberkampf/Roy/Trucano-artige V&V/UQ-Literatur.** Numerische Fehler, Modellfehler, Referenz-/Validierungsevidenz, Sensitivität und predictive capability sind etablierte Gegenstände.

### Ergebnis des harten Vergleichs

Die C05-Diagnostik kann ohne Informationsverlust in Standard-Numerik/V&V/Credibility-Sprache ausgedrückt werden. Daher ist die starke C06-Fassung — neue numerische Validierungsfragen durch die Trias — im aktuellen Solverfall **nicht gestützt**.

Ein möglicher verbleibender Mehrwert liegt in einer expliziten integrativen Zuordnung über Zielsystem–Theorie–Berechnung sowie in der Verbindung von analytischer Traktabilität (Sundman), numerischer Operationalisierung und wissenschaftlichem Gebrauch.

### Aktueller Status

**PENDING REVIEW — REVISE.** Empfohlen wird C06-R statt der starken Fassung. Ein minimaler AI-for-Science/ML-Fall soll anschließend prüfen, ob der Integrations-/Provenance-Vorteil unter einer zusätzlichen lernbasierten Übersetzung tatsächlich diagnostisch trägt.