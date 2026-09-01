# Trias AI for Science

Dieses Repository dokumentiert und entwickelt das Forschungsprogramm **Realität – Theorie – Berechnung/Umsetzung** am Leitfall des Newtonschen Drei-Körper-Problems.

## Projektziel

Die Trias wird zunächst **nicht** als universale Ontologie der Wissenschaft behandelt, sondern als **methodologisches Audit-Framework**. Untersucht wird, ob die explizite Trennung von

1. Zielsystem / Realitäts-Pol,
2. theoretischer Beschreibung,
3. operativer Berechnung bzw. Implementierung

Annahmen, Transformationen, Verluste und Validierungsanforderungen sichtbar macht, die in einer bloßen Theorie–Experiment-Beschreibung unterbestimmt bleiben.

Der Drei-Körper-Fall dient als kontrollierter Leitfall. Das Projekt soll weder eine neue Lösung des Drei-Körper-Problems noch primär ein SOTA-ML-Ergebnis liefern.

## Aktueller Forschungsstatus

- **Woche 1:** Claim and Scope
- **Claim 1:** akzeptiert
- **Claim 2:** zur Entscheidung vorgelegt
- **Claim 3:** noch nicht begonnen
- **Demonstrator:** bewusst noch nicht implementiert

Siehe [`STATUS.md`](STATUS.md) für den aktuellen Arbeitsstand.

## Arbeitsprinzip

Das Projekt folgt einem expliziten Entscheidungsworkflow:

> Ausarbeitung → Review → Entscheidung → Dokumentation → nächster abhängiger Schritt

Im begleitenden Forschungsdialog bedeutet **GO**:

> Die vorgeschlagene wissenschaftliche Entscheidung wird als aktuelle Arbeitsgrundlage akzeptiert und darf in alle folgenden Schritte eingehen.

Spätere Revisionen bleiben ausdrücklich möglich. Sie werden jedoch als neue Entscheidung dokumentiert, anstatt frühere Entscheidungen stillschweigend zu überschreiben.

## Geplante Repository-Struktur

```text
trias-ai-for-science/
├── README.md
├── STATUS.md
├── DECISIONS.md
├── claims/
│   ├── claim_registry.md
│   ├── claim_01.md
│   └── claim_02.md
├── literature/
│   └── evidence_register.md
├── memo/
│   └── week01_claim_scope.tex
├── demonstrator/
│   └── README.md
└── paper/
    └── README.md
```

Die Struktur wird nur erweitert, wenn eine konkrete Forschungsabhängigkeit dies erfordert.

## Derzeitige zentrale Arbeitsbehauptung

Die Trias beansprucht ihren möglichen Mehrwert **nicht** darin, Berechnung erstmals als epistemisch relevante wissenschaftliche Praxis zu identifizieren. Der mögliche Beitrag liegt vielmehr darin, vorhandene Einsichten aus Modell-, Simulations- und Computational-Science-Philosophie in ein explizites Audit-Schema zu überführen, das Annahmen und Validierungsfragen den drei Polen und ihren Übergängen zuordnet.

## Geplanter Minimaldemonstrator

Der kleinste Demonstrator soll später bei identischem synthetischem Zielsystem, identischer Theorie und identischen Anfangsbedingungen mehrere numerische Umsetzungen vergleichen. Zunächst vorgesehen sind:

- hochgenaue adaptive Referenzintegration,
- Fixed-Step-Baseline, z. B. RK4,
- ein strukturerhaltendes Verfahren.

Er soll nicht bloß zeigen, dass numerische Verfahren verschiedene Fehler besitzen, sondern prüfen, ob die Trias daraus **eine spezifischere wissenschaftliche Diagnose oder Validierungsanforderung** ableiten kann.

Ein ML-Surrogat ist für die Minimalversion ausdrücklich nicht erforderlich.