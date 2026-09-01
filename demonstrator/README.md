# Minimaldemonstrator — vorläufiger Scope

**Status:** noch nicht implementieren.

Der Demonstrator dient nicht dazu, einen numerischen Sieger zu bestimmen oder ein neues Drei-Körper-Verfahren zu entwickeln. Er soll prüfen, ob die Trias eine wissenschaftlich relevante Diagnose erzeugt, die über die bloße Feststellung unterschiedlicher numerischer Fehler hinausgeht.

## Vorläufige Minimalstruktur

Ein kollisionsfreies, planares, dimensionsloses Drei-Körper-System mit festgelegten Anfangsbedingungen.

Geplanter Vergleich:

1. hochgenaue adaptive Integration als vorläufige Referenz,
2. einfache Fixed-Step-Baseline, z. B. RK4,
3. ein strukturerhaltendes Verfahren.

Vorläufige Metriken:

- Trajektorienabweichung im Zeitverlauf,
- Energiedrift,
- Drehimpulsdrift,
- Schrittweitensensitivität,
- Laufzeit.

## Zentrales Erfolgskriterium

Ein numerischer Unterschied allein genügt nicht.

Der Demonstrator ist für das Trias-Projekt nur dann informativ, wenn sich zeigen lässt, dass die explizite Zuordnung zu

- Zielsystem,
- theoretischer Struktur,
- Implementierung,
- oder einer ihrer Übergangskanten

zu einer spezifischeren wissenschaftlichen Diagnose oder Validierungsanforderung führt.

## Noch nicht festgelegt

- konkrete Anfangsbedingung,
- konkrete Referenzsolver,
- konkrete strukturerhaltende Methode,
- Zeitintervall,
- Toleranzen und Präzision,
- Schwellenwerte für praktische Relevanz,
- eventuelle zweite sensitive/chaotische Konfiguration.

Diese Entscheidungen werden erst nach Stabilisierung der Claims getroffen.

## ML

Ein ML-Surrogat ist für die Minimalversion nicht vorgesehen. Es wird nur ergänzt, wenn später eine eigenständige methodologische Frage entsteht, die durch den rein numerischen Vergleich nicht beantwortet werden kann.