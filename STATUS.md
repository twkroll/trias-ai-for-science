# Current Status

## Phase

**Week 1 — Claim and Scope / First Implementation Skeleton**

Ziel dieser Phase ist ein belastbares Claim-and-Scope-Fundament plus ein minimaler, getesteter Demonstrator-Skeleton, bevor der vollständige wissenschaftliche Lauf interpretiert wird.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework; diagnostischer Mehrwert ist die zentrale Hypothese.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol; keine notwendige ontologische Trennung der Pole.
- **C03 / D003:** Sundman als konvergente, praktisch extrem ineffiziente Reihenrepräsentation; formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.
- **C04 / D004:** Konvergenz, operative Machbarkeit, numerische Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt; V&V bleibt Vergleichsrahmen.
- **Minimal Demonstrator / D005:** Figure-eight + DOP853 + RK4 + Velocity-Verlet, mit U1 und U2 und ohne ML/chaotischen Fall.
- **Implementation Contract / D006:** exakte v0.1-Konfiguration, Referenzlogik, Schrittweiten, Metriken, Gates und Artefakte eingefroren.

## Aktuelle Aufgabe

### Code Skeleton v0.1
**Status:** READY FOR REVIEW

Implementiert sind:

- Figure-eight-Konfiguration;
- gemeinsame Newtonsche Dynamik und Invarianten;
- expliziter RK4 und Velocity-Verlet;
- DOP853 primary/tight reference;
- Positions-, Energie-, Drehimpuls-, Ressourcen- und Refinementmetriken;
- reproduzierbarer Experiment-Runner;
- regelbasierter `trias_audit.md`;
- Unit-/Smoke-Tests und Quick-Run-Modus.

Lokale Vorprüfung vor dem Repository-Write:

```text
pytest -q
4 passed
```

Ein Quick-Pipeline-Run erzeugte erfolgreich alle vertraglich geforderten Artefakttypen. Quick-Werte gelten ausdrücklich nicht als Evidenz für C05/C06.

Details: [`demonstrator/code_skeleton_status_v0_1.md`](demonstrator/code_skeleton_status_v0_1.md).

## Noch nicht wissenschaftlich ausgeführt/entschieden

- vollständiger U2-Lauf über 100 nominelle Perioden mit allen fünf Refinements;
- wissenschaftliche Prüfung aller Reference-/Refinement-Gates;
- C05: Implementierungswahl kann epistemisch relevante Profile erzeugen;
- C06: Trias-Audit liefert zusätzliche Fehlerzuordnung/Validierungsfragen;
- ML-Modul.

## Nächste Abhängigkeit

Nach Review und Akzeptanz des Code Skeleton v0.1 wird der eingefrorene vollständige v0.1-Lauf ausgeführt. Erst danach werden Resultate interpretiert und C05 zur Entscheidung vorgelegt.

## Arbeitsregel

`GO` im Forschungsdialog = aktuelle Empfehlung akzeptiert; Decision-/Status-/Spezifikationsdokumentation aktualisieren; anschließend zum nächsten abhängigen Schritt übergehen.