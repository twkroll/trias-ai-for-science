# C07-L — Lucarini–Trias Bridge: operative Äquivalenz ≠ theoretische Identifizierbarkeit

**Status:** PENDING REVIEW  
**Stand:** 2026-09-02  
**Depends on:** C06-R / D009, D013–D014 as current ML branch background  
**Primary literature anchor:** Z.-M. Zhai, V. Lucarini, Y.-C. Lai, *Deficiency of equation-finding approach to data-driven modeling of dynamical systems*, arXiv:2509.03769 (2025; current arXiv version 2026).

## Vorgeschlagene Claim-Fassung

> **C07-L:** Bei datengetriebener Modellierung kann die konkrete Beobachtungs-, Rekonstruktions- und Inferenzprovenance beeinflussen, welche theoretische Repräsentation aus einem dynamischen System gewonnen wird. Strukturell verschiedene inferierte Modelle können bezüglich ausgewählter dynamischer oder statistischer Observablen praktisch äquivalent sein. Daher rechtfertigt erfolgreiche dynamische Reproduktion allein nicht die Behauptung, eine eindeutige physikalische Gleichungsstruktur identifiziert zu haben.

## Engerer mathematischer Kern

Für eine Beobachtungs-/Inferenzpipeline `p` sei

```text
T_hat_p = I_p(R)
```

und für eine Menge relevanter Observablen `O` gelte möglicherweise

```text
O(T_hat_1) ≈ O(T_hat_2) ≈ O(T*)
```

während zugleich

```text
T_hat_1 != T_hat_2 != T*
```

auf Gleichungs- bzw. Termstruktur-Ebene gilt.

Projektintern wird dies als zweckrelative operative Äquivalenz notiert:

```text
T1 ~_(O,epsilon) T2
```

ohne daraus strukturelle Identität abzuleiten.

## Was Zhai–Lucarini–Lai tatsächlich stützt

Das Paper berichtet für chaotische Systeme, insbesondere den Lorenz-Fall:

- zufällige Missingness in Beobachtungszeitreihen;
- Rekonstruktion/Imputation der fehlenden Daten;
- anschließende sparse equation discovery;
- deutlich unterschiedliche inferierte Gleichungssätze je nach Beobachtungs-/Missingness-Situation;
- dennoch ähnliche chaotische Attraktoren und ähnliche Lyapunov-Exponenten/KL-basierte Attraktorstatistik;
- Übereinstimmung vieler dominanter Koopman-Eigenwerte, mit Unterschieden in subdominanteren Bereichen;
- lokal meist ähnliche Geschwindigkeitsfelder mit seltenen größeren Abweichungen.

Damit liefert das Paper einen konkreten Fall, in dem Gleichungsstruktur und dynamisch-statistische Adäquanz auseinanderfallen.

## Was daraus nicht folgt

Nicht aus dem Paper allein ableitbar sind:

1. allgemeine Nichtidentifizierbarkeit aller datengetriebenen Gleichungsmodelle;
2. Gleichwertigkeit aller strukturell verschiedenen Modelle;
3. Unmöglichkeit physikalisch sinnvoller Equation Discovery;
4. Einzigartigkeit oder Neuheit der Trias;
5. die These, dass direkte ML-Modelle epistemisch grundsätzlich besser als Gleichungsmodelle sind;
6. dass die beobachtete Nicht-Eindeutigkeit identisch mit klassischer structural identifiability ist.

## Anschluss an etablierte Literatur

Vor Akzeptanz muss C07-L gegen mindestens vier etablierte Begriffsfamilien geprüft werden:

- structural identifiability;
- practical identifiability / estimability;
- observability;
- equifinality / observational equivalence / model non-uniqueness.

Diese Literatur zeigt bereits lange, dass verschiedene Parameter/Modelle unter bestimmten Beobachtungen nicht eindeutig unterscheidbar sein können. Der mögliche Mehrwert der Trias kann daher nicht in der Entdeckung von Nichtidentifizierbarkeit liegen.

## Möglicher Trias-Mehrwert

Der zu testende Eigenbeitrag lautet enger:

> Die Trias könnte Forward- und Inverse-Probleme in einem gemeinsamen Provenance-Audit zusammenführen: `T -> C -> R_hat` für Operationalisierung und `R -> C -> T_hat` für Observation/Inference. Dadurch würden unterschiedliche Arten von Nicht-Eindeutigkeit, Verlust und Zweckrelativität in derselben methodologischen Grammatik lokalisiert.

Das wäre eine Schärfung von C06-R, falls sie gegenüber bestehenden Identifiability-/V&V-/Credibility-Frameworks tatsächlich zusätzliche integrative Arbeit leistet.

## Verbindung zu bestehenden Claims

### C03

```text
analytische Verfügbarkeit not=> operative Verfügbarkeit
```

### C05

```text
gleiche Theorie not=> gleiches Implementierungsprofil
```

### C07-L

```text
ähnliche operative/dynamische Adäquanz not=> eindeutige Theorie
```

Diese drei Befunde bilden eine symmetrische Arbeitsstruktur, ohne dass daraus bereits ein universaler Satz folgt.

## Konsequenz für die Lösungsleiter

Die sechs-stufige Lösungsleiter aus D004 bleibt erhalten. **Theoretische Identifizierbarkeit wird als querliegende Auditdimension ergänzt**, nicht als neue lineare Stufe.

## Revisions-/Widerlegungskriterium

C07-L muss stark abgeschwächt oder als eigener Trias-Claim aufgegeben werden, wenn

1. der gesamte relevante Befund ohne Rest in etablierter Identifiability/Observability/Equifinality-Terminologie aufgeht und die gerichtete Trias keine zusätzliche Integrations- oder Zuordnungsleistung bietet;
2. die Zhai–Lucarini–Lai-Befunde bei genauer Prüfung enger sind als hier formuliert;
3. ein eigener Minimaldemonstrator die behauptete Trennung von struktureller und operativer Adäquanz nicht reproduzierbar zeigt.

## Entscheidungsempfehlung

**Noch nicht ACCEPT.**

Nächster Schritt ist ein Claim-to-Evidence- und Comparator-Audit. Erst danach wird eine endgültige moderate C07-L-Fassung zur GO-Entscheidung vorgelegt.