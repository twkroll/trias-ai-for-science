# D020 — Inverse Full Run v0.1 als INFORMATIVE_NEGATIVE akzeptiert

**Datum:** 2026-09-02  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D018, D019

## Entscheidung

Der wissenschaftliche `Inverse-Direction Scientific Full Run v0.1` wird als gültiger vorregistrierter Projektbefund akzeptiert.

Die Resultatklasse lautet:

```text
INFORMATIVE_NEGATIVE
```

Die Gates G1–G3 bestehen. Der lineare Rekonstruktionspfad zeigt nur in `1/3` Mask-Seeds eine substantielle strukturelle Perturbation; der kubische Rekonstruktionspfad in `0/3`. Damit wird die vorregistrierte Seed-Konsistenz von mindestens `2/3` nicht erreicht.

Der einzelne Fall `linear / seed 2` mit zusätzlichem konstanten Term in `dz/dt` bei gleichzeitig bestandener operativer Äquivalenz wird ausschließlich als **explorative Beobachtung** behandelt und nicht zum Hauptergebnis hochgestuft.

## Anti-Confirmation-Bias Guardrail

Nach Sichtung des Ergebnisses werden nicht rückwirkend verändert:

- Missingness-Rate;
- Mask-Seeds;
- SINDy-Threshold;
- Feature-Library;
- Structural-Perturbation-Schwellen;
- operative Äquivalenztoleranzen;
- Resultatlogik.

Insbesondere wird kein `inverse v0.2` allein deshalb gestartet, um einen positiven Provenance-Effekt zu erzwingen.

## Wissenschaftliche Bedeutung

Der akzeptierte Befund lautet eng:

> Die konkrete Minimalisierung mit 20% zufälliger punktweiser Missingness, gepaarter linearer bzw. kubischer Rekonstruktion und eingefrorener SINDy-Pipeline erzeugt keinen seed-robusten strukturellen Rekonstruktionsprovenance-Effekt.

Nicht widerlegt werden dadurch klassische Nichtidentifizierbarkeit, observational equivalence/equifinality oder der externe Zhai–Lucarini–Lai-Befund.

## Erlaubter nächster Schritt

Als nächste Abhängigkeit ist ausschließlich der bereits vorregistrierte **Comparator-Audit auf genau diesem negativen Ergebnis** freigegeben. Der Befund wird gegen folgende Rahmen verglichen:

1. System Identification / SINDy robustness / structural error;
2. structural/practical identifiability und observability;
3. Scientific-ML / Modeling & Simulation V&V und credibility;
4. Workflow/Data Provenance;
5. Directed Trias.

Als zusätzlicher Stress-Comparator darf Claims–Arguments–Evidence / Assurance-Case-Literatur herangezogen werden, weil sie unmittelbar prüft, ob die vermeintlich verbleibende Trias-Leistung `welche Evidenz rechtfertigt welchen Claim?` bereits etabliert ist.

## Strategischer Freeze

Bis zum Abschluss dieses Comparator-Audits bleiben sowohl der wissenschaftliche ML-v0.2-Full-Run als auch eine Revision des inversen Experiments pausiert.