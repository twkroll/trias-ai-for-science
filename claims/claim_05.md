# C05 — Implementierungswahl kann wissenschaftlich relevante Profile erzeugen

**Status:** PENDING REVIEW  
**Evidence status:** empirisch durch Full Demonstrator v0.1 gestützt; Interpretation absichtlich moderat  
**Stand:** 2026-09-02

## Vorgeschlagene Claim-Fassung

> Bei identischem synthetischem Zielsystem, identischer Theorie und identischen Anfangsdaten können unterschiedliche numerische Operationalisierungen verschiedene wissenschaftlich relevante Fehler- und Strukturprofile erzeugen. Welche Operationalisierung für eine wissenschaftliche Aufgabe vorzuziehen ist, kann deshalb vom spezifizierten wissenschaftlichen Gebrauch und den dafür relevanten theoretischen Strukturen abhängen und ist nicht notwendig durch eine einzelne globale Genauigkeitsmetrik bestimmt.

## Empirische Basis

Der akzeptierte v0.1-Demonstrator vergleicht DOP853 als provisorisch hochgenaue Referenz, klassischen Fixed-Step-RK4 und Velocity-Verlet auf der equal-mass Figure-eight-Konfiguration.

### Reference gate

Primary-versus-tight DOP853 max position gap:

- U1: `8.854e-12`;
- U2: `6.163e-08`.

Diese Werte liegen für alle interpretierten Fixed-Step-Ergebnisse mindestens zwei Größenordnungen unter dem jeweiligen Trajektorienfehler. Das zuvor akzeptierte Referenz-Gate ist erfüllt.

### U1 — trajectory-oriented use

RK4 zeigt eine Near-fourth-order-Verfeinerung der Endpoint-Positionserrors (`4.74, 4.62, 4.46, 4.30`). Verlet nähert sich zweiter Ordnung (`1.75, 1.87, 1.97, 1.99`).

Bei `n=200` beträgt der maximale normalisierte U1-Positionsfehler:

- RK4: `8.037e-06`;
- Verlet: `6.389e-03`.

Für die explizit trajectory-orientierte U1-Frage ist RK4 im getesteten Vergleich klar vorzuziehen.

### U2 — structure-oriented use

Bei `n=200`:

- RK4: max `|e_H| = 8.304e-05`, Drift-Slope `-8.305e-07` pro nomineller Periode;
- Verlet: max `|e_H| = 6.019e-04`, Drift-Slope `-5.783e-09` pro nomineller Periode.

RK4 hat also die kleinere Energiefehler-Amplitude, Verlet jedoch etwa 144-mal weniger fitted secular energy drift.

Bei `n=400` ist der fitted Drift bei Verlet etwa 60-mal kleiner. Zugleich bleibt der normalisierte Drehimpulsfehler von Verlet über U2 ungefähr auf Rundungsniveau (`~1e-14`), während RK4 bei gleichem `n` größere, mit Refinement abnehmende Fehler besitzt.

RK4 bleibt gleichzeitig bei der Trajektoriennähe zur DOP853-Referenz deutlich besser. C05 behauptet deshalb ausdrücklich **keine globale Rangumkehr** und keine allgemeine Überlegenheit symplektischer Verfahren.

## Methodologische Lesart

Der Befund zeigt eine Differenz zwischen mindestens folgenden Kriterien:

1. Trajektoriennähe zu einer hochgenauen Referenz;
2. maximale Energiefehler-Amplitude;
3. secular drift behavior;
4. Erhaltung theoretischer Invarianten;
5. Ressourcenaufwand.

Die Antwort auf „welcher Solver ist besser?“ ist daher ohne Spezifikation des wissenschaftlichen Gebrauchs unterbestimmt.

Für C05 genügt diese moderate Aussage. Ob die Trias selbst hierfür zusätzlichen epistemischen Mehrwert gegenüber Standard-Numerik/V&V liefert, ist **nicht Teil von C05** und bleibt C06 vorbehalten.

## Explizite Nicht-Claims

Das Projekt behauptet mit C05 nicht:

- dass Velocity-Verlet allgemein besser als RK4 ist;
- dass Invariantenerhaltung immer wichtiger als Trajektoriengenauigkeit ist;
- dass RK4 für langfristige Dynamik grundsätzlich wissenschaftlich unbrauchbar ist;
- dass ein kleiner fitted energy-drift slope allein numerische Stabilität beweist;
- dass der getestete reguläre Figure-eight-Fall Aussagen über chaotische Drei-Körper-Dynamik trägt;
- dass C05 bereits die Originalität oder Überlegenheit des Trias-Audits gegenüber V&V zeigt.

## Revisionsbedingung

C05 muss abgeschwächt werden, falls unabhängige Reproduktion oder weitere Referenzprüfung zeigt, dass der beobachtete Profilkontrast ein Implementierungsfehler oder Referenzartefakt ist. Eine spätere Feststellung, dass Standard-V&V denselben Befund vollständig diagnostiziert, widerlegt C05 selbst nicht, wäre aber zentral gegen einen starken C06-Claim.

## Entscheidungsempfehlung

**ACCEPT in der moderaten, zweckrelativen Form.**

Nach `GO` wird C05 als D008 akzeptiert. Der nächste abhängige Schritt ist C06: ein expliziter Vergleich derselben Resultate unter (a) gewöhnlicher numerischer Analysis/V&V und (b) dem Trias-Audit. Erst dieser Vergleich entscheidet, ob die Trias zusätzlichen diagnostischen Wert besitzt.