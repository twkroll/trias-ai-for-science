# Current Status

## Phase

**Week 1 — Claim and Scope / Full Demonstrator v0.1 Review**

Das Claim-and-Scope-Fundament, der Minimaldemonstrator, der Implementation Contract und der getestete Code-Skeleton sind eingefroren. Der vollständige v0.1-Lauf wurde ausgeführt; aktuell wird C05 anhand dieser Ergebnisse bewertet.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework; diagnostischer Mehrwert ist die zentrale Hypothese.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol; keine notwendige ontologische Trennung der Pole.
- **C03 / D003:** Sundman als konvergente, praktisch extrem ineffiziente Reihenrepräsentation; formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.
- **C04 / D004:** Konvergenz, operative Machbarkeit, numerische Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt; V&V bleibt Vergleichsrahmen.
- **Minimal Demonstrator / D005:** Figure-eight + DOP853 + RK4 + Velocity-Verlet, mit U1 und U2 und ohne ML/chaotischen Fall.
- **Implementation Contract / D006:** v0.1-Konfiguration, Referenzlogik, Schrittweiten, Metriken, Gates und Artefakte eingefroren.
- **Code Skeleton / D007:** minimaler getesteter Skeleton als faithful implementation von D006 akzeptiert.

## Full Demonstrator v0.1

**Status:** COMPLETE

Der eingefrorene Lauf wurde für U1 und U2 sowie `n={50,100,200,400,800}` ausgeführt. Der monolithische Runner überschritt die verfügbare Tool-Walltime; deshalb wurde dieselbe unveränderte Rechnung deterministisch in Referenz- und Method/Refinement-Teilläufen ausgeführt und aggregiert.

### Reference gates

- U1 primary-vs-tight DOP853 max normalized position gap: `8.854e-12`.
- U2 primary-vs-tight DOP853 max normalized position gap: `6.163e-08`.
- Selbst der feinste interpretierte Fixed-Step-Trajektorienfehler liegt mehr als zwei Größenordnungen über dem jeweiligen Referenzgap.

Die akzeptierte Referenzregel ist damit für die C05-Auswertung erfüllt.

### Refinement

- RK4 U1 observed endpoint orders: `4.74, 4.62, 4.46, 4.30`.
- Verlet U1 observed endpoint orders: `1.75, 1.87, 1.97, 1.99`.

### Hauptbefund

Für U1 ist RK4 bei gleichem `n` klar trajectory-genauer. Für U2 entsteht dagegen ein mehrdimensionales Profil: RK4 bleibt trajectory-genauer und besitzt teils kleinere maximale Energiefehler-Amplituden, während Velocity-Verlet einen drastisch kleineren fitted secular energy drift und Drehimpulserhaltung nahe Rundungsniveau zeigt.

Details: [`demonstrator/full_run_v0_1_results.md`](demonstrator/full_run_v0_1_results.md).

## Aktuelle Entscheidung

### C05 — Implementierungswahl kann wissenschaftlich relevante Profile erzeugen
**Status:** PENDING REVIEW

Empfohlene moderate Fassung:

> Bei identischem synthetischem Zielsystem, identischer Theorie und identischen Anfangsdaten können unterschiedliche numerische Operationalisierungen verschiedene wissenschaftlich relevante Fehler- und Strukturprofile erzeugen. Welche Operationalisierung für eine wissenschaftliche Aufgabe vorzuziehen ist, kann deshalb vom spezifizierten wissenschaftlichen Gebrauch und den dafür relevanten theoretischen Strukturen abhängen und ist nicht notwendig durch eine einzelne globale Genauigkeitsmetrik bestimmt.

Siehe [`claims/claim_05.md`](claims/claim_05.md).

## Danach

Nach Akzeptanz von C05 folgt **C06**: direkter Vergleich derselben Ergebnisse unter gewöhnlicher numerischer Analysis/V&V versus Trias-Audit. Erst dieser Schritt darf über den zusätzlichen diagnostischen Wert der Trias entscheiden.

ML bleibt weiterhin außerhalb des aktuellen Scope.

## Arbeitsregel

`GO` im Forschungsdialog = aktuelle Empfehlung akzeptiert; Decision-/Status-/Claim-Dokumentation aktualisieren; anschließend zum nächsten abhängigen Schritt übergehen.