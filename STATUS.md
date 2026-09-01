# Current Status

## Phase

**Week 1 — Claim and Scope / Demonstrator Freeze**

Ziel dieser Phase ist ein belastbares Claim-and-Scope-Memo plus eine minimal eingefrorene Spezifikation, bevor Implementierung beginnt.

## Akzeptierte Entscheidungen

### C01 — Diagnostischer Mehrwert der Trias
**Status:** ACCEPTED — D001

Die Trias wird zunächst als methodologisches Audit-Framework untersucht. Es wird keine universale ontologische Dreiteilung der Wissenschaft behauptet.

### C02 — Synthetisches Zielsystem
**Status:** ACCEPTED — D002

Der Realitäts-Pol wird funktional als Zielsystemrolle behandelt. Im Drei-Körper-Fall wird ein explizit konstruiertes **synthetisches Zielsystem** verwendet; die Trennung der Pole ist methodologisch und nicht notwendig ontologisch.

### C03 — Sundmans Reihenlösung und praktische Traktabilität
**Status:** ACCEPTED — D003

Der akzeptierte methodologische Befund lautet: **formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.**

### C04 — Evaluationsdimensionen operativer Verfügbarkeit
**Status:** ACCEPTED — D004

Reihenkonvergenz, numerische Verfahrenskonvergenz, operative Machbarkeit, numerische Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden nicht vermischt. Verification & Validation bleibt ein expliziter Vergleichsrahmen.

### Minimal Demonstrator Specification v0.1
**Status:** ACCEPTED — D005

Akzeptierter Scope:

- planare gleichmassige Figure-eight-Choreographie;
- DOP853 als provisorisch hochgenaue Referenz;
- fester RK4 als Baseline;
- Velocity-Verlet/Leapfrog als symplektischer Kontrast;
- U1 = kurzfristige Trajektorienfrage;
- U2 = langfristige Strukturfrage;
- kein ML und kein chaotischer Fall in v0.1;
- positiver wie negativer Befund zur Trias ist zulässig.

## Aktuelle Aufgabe

### Implementation Contract v0.1
**Status:** PENDING REVIEW

Zu akzeptieren sind vor Codebeginn die exakten Anfangsdaten, Zeiträume, Referenztoleranzen, Schrittweitenfamilie, Metrikdefinitionen, Referenz-Gates, Tests und Ausgabeartefakte.

Siehe [`demonstrator/implementation_contract_v0_1.md`](demonstrator/implementation_contract_v0_1.md).

## Danach

Nach Akzeptanz des Implementation Contract wird ausschließlich ein minimaler getesteter Code-Skeleton umgesetzt. C05 und C06 werden erst anhand der erzeugten Resultate bewertet.

## Noch nicht gestartet

- C05: Implementierungswahl kann epistemisch relevante Profile erzeugen.
- C06: Trias-Audit liefert zusätzliche Fehlerzuordnung/Validierungsfragen.
- ML-Modul.

## Arbeitsregel

`GO` im Forschungsdialog = aktuelle Empfehlung akzeptiert; Decision-/Status-/Spezifikationsdokumentation aktualisieren; anschließend zum nächsten abhängigen Schritt übergehen.