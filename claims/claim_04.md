# C04 — Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ wissenschaftliche Nutzbarkeit

**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Evidenzstatus:** numerisch gut gestützt; „operative rechnerische Machbarkeit“ und „wissenschaftliche Nutzbarkeit“ sind projektinterne Synthese- bzw. Auditbegriffe  
**Stand:** 2026-09-01

## C04a — Nichtäquivalenz der Evaluationsdimensionen

> Mathematische Konvergenz, operative rechnerische Machbarkeit, numerische Stabilität und wissenschaftliche Nutzbarkeit beantworten unterschiedliche Bewertungsfragen und dürfen nicht gleichgesetzt werden. Insbesondere impliziert mathematische Konvergenz allein weder praktische Machbarkeit noch numerische Stabilität oder wissenschaftliche Nutzbarkeit.

Im Projekt wird zusätzlich zwischen **Reihenkonvergenz** einer analytischen Darstellung und **Verfahrenskonvergenz** eines numerischen Verfahrens unterschieden.

## C04b — Zweckrelativität wissenschaftlicher Nutzbarkeit

> Wissenschaftliche Nutzbarkeit ist keine rein interne Eigenschaft eines mathematischen oder rechnerischen Outputs, sondern hängt vom intendierten wissenschaftlichen Gebrauch, den erforderlichen Genauigkeits- und Strukturkriterien sowie der verfügbaren Validierungs- und Unsicherheitsevidenz ab.

„Wissenschaftliche Nutzbarkeit“ ist ein projektinterner Auditbegriff. Er darf nicht so behandelt werden, als gebe es eine einzige universelle Nutzbarkeitsmetrik.

## C04c — Systemsensitivität versus algorithmische Stabilität

> Die Sensitivität des mathematischen Zielproblems gegenüber Änderungen der Eingabedaten ist von der numerischen Stabilität des verwendeten Algorithmus zu unterscheiden. Insbesondere darf chaotische bzw. sensitive Dynamik im Drei-Körper-System nicht ohne weitere Analyse als numerische Instabilität interpretiert werden.

Diese Unterscheidung ist für den späteren Demonstrator verpflichtend.

## Operative rechnerische Machbarkeit

Projektinterne Arbeitsdefinition:

> Eine Repräsentation oder ein Verfahren ist für einen spezifizierten wissenschaftlichen Zweck operativ rechnerisch machbar, wenn das benötigte Ergebnis mit den vorgesehenen Ressourcen bis zur erforderlichen Genauigkeit erzeugt werden kann.

Die Kategorie ist daher relativ zu Probleminstanz, Genauigkeitsanforderung, Ressourcenbudget und wissenschaftlichem Zweck. Sie ist ausdrücklich nicht mit Turing-Berechenbarkeit oder allgemeiner Komplexitätstheorie gleichzusetzen.

## Verhältnis zur Lösungsleiter

Die bisherige Lösungsleiter bleibt bestehen:

Existenz → analytische Repräsentation → praktische Evaluierbarkeit → numerische Simulation → Vorhersage → wissenschaftliche Nutzbarkeit.

Konvergenz, Machbarkeit, Stabilität und Systemsensitivität werden jedoch **nicht** als zusätzliche lineare Stufen behandelt. Sie sind querliegende Prüfdimensionen, die an mehreren Übergängen relevant werden.

## Verhältnis zu Verification & Validation

Verification-and-Validation-Ansätze werden als bestehender Vergleichsrahmen anerkannt. Das Projekt behauptet nicht, die Unterscheidung zwischen Modell, numerischer Lösung und Zielsystem erstmals einzuführen.

Eine spätere Aufgabe von C06 ist daher explizit zu prüfen, ob der Trias-Audit gegenüber V&V, numerischer Fehleranalyse, Reproduzierbarkeits- und Unsicherheitsrahmen tatsächlich zusätzliche diagnostische Arbeit leistet.

## Explizite Nicht-Claims

Das Projekt behauptet nicht:

- dass Konvergenz und Stabilität mathematisch unverbunden sind;
- dass „operative rechnerische Machbarkeit“ ein etablierter universeller Fachbegriff in der hier verwendeten Definition ist;
- dass operative Machbarkeit mit theoretischer Berechenbarkeit identisch ist;
- dass langsame Reihen-Konvergenz numerische Instabilität bedeutet;
- dass chaotische Sensitivität schlechte Numerik bedeutet;
- dass numerische Genauigkeit allein wissenschaftliche Nutzbarkeit garantiert;
- dass eine einzelne universelle Metrik wissenschaftliche Nutzbarkeit messen kann;
- dass die Trias Verification & Validation bereits nachweislich überlegen ist.

## Konsequenz für den Demonstrator

Der Demonstrator darf nicht nur Solverfehler vergleichen. Er muss getrennt prüfen:

1. Verfahrenskonvergenz bzw. Verfeinerungsverhalten,
2. Ressourcenkosten und praktische Machbarkeit,
3. numerische Fehler- und Stabilitätsindikatoren,
4. Systemsensitivität versus algorithmische Herkunft beobachteter Divergenzen,
5. Relevanz des Outputs für eine explizit formulierte wissenschaftliche Frage.

## Nächste Abhängigkeit

Nach C04 folgt die **Minimal-Spezifikation des Drei-Körper-Demonstrators**. Erst danach werden C05 und C06 empirisch prüfbar.