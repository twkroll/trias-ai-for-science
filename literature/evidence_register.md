# Evidence Register

Dieses Register dokumentiert, welche Evidenz für die einzelnen Claims benötigt wird. Es trennt externe Literaturbelege von projektinternen methodologischen Setzungen und späteren Ergebnissen des Demonstrators.

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

**PARTIAL / OPEN.** Die philosophische Anschlussfähigkeit ist plausibel; der eigenständige Mehrwert der konkreten Trias ist noch nicht gezeigt.

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
- **Q. D. Wang / moderne mathematische Einordnung.** Formuliert Sundmans Theorem über Analytizität in einer neuen Zeitvariablen und globale Abdeckung reeller Zeit unter der klassischen Nichtnull-Drehimpuls-Bedingung.

### Noch zu kontrollieren

- endgültige bibliographische Jahresangabe für das Mémoire,
- exakte Form der Nichtnull-Drehimpuls-Bedingung in der zitierten Fassung,
- ob quantitative Angaben zur benötigten Termzahl im Paper verwendet werden; falls ja, direkte Rekonstruktion aus Belorizky statt sekundärer Wiederholung.

### Aktueller Status

**PENDING REVIEW.** Der qualitative Kern ist gut gestützt: Sundman ist ein Konvergenz-, nicht ein Divergenzbeispiel; die praktische Ineffizienz ist separat zu behandeln.

---

## E04 — Evidenz für C04

**Claim:** mathematische Konvergenz, rechnerische Machbarkeit, numerische Stabilität und wissenschaftliche Nutzbarkeit sind verschiedene Bewertungsebenen.

### Aktueller Status

**NOT STARTED.** Abhängig von Entscheidung zu C03.