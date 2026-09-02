# D016 — C07-L-R akzeptiert; starke C07-L-Fassung verworfen; inverser MVP als nächste Abhängigkeit

**Datum:** 2026-09-02  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D009, D015, C07-L Comparator Audit

## Entscheidung

Die starke Neuheitsfassung von C07-L wird verworfen. Das Projekt beansprucht ausdrücklich **nicht**, Nichtidentifizierbarkeit, observational equivalence, equifinality, near-identifiability oder die Trennung von struktureller und outputseitiger Modellgüte entdeckt zu haben.

Die moderate Fassung **C07-L-R** wird als aktuelle Arbeitsgrundlage akzeptiert:

> Bei datengetriebener Equation Discovery ist die Güte eines inferierten Modells mehrdimensional: strukturelle Übereinstimmung der Gleichungen, dynamisch-statistische Adäquanz und physikalische Interpretierbarkeit sind nicht gleichzusetzen. Zhai, Lucarini und Lai liefern einen konkreten chaotischen Fall, in dem unterschiedliche Beobachtungs-/Rekonstruktionsbedingungen zu strukturell verschiedenen inferierten ODEs führen, während ausgewählte Langzeit- und Koopman-Eigenschaften ähnlich bleiben. Für die Trias dient dieser Befund nicht als neue Identifiability-Theorie, sondern als inverser Testfall für die Hypothese, dass wissenschaftliche Rechtfertigung die Provenance und Richtung der Transformation `target/observation -> data -> inference -> theory` explizit auditieren sollte.

## Claim-Grenzen

1. C07-L-Ra (mehrdimensionale Modellgüte) wird als etablierter Kontext behandelt, nicht als Trias-Neuheit.
2. C07-L-Rb (Zhai–Lucarini–Lai-Fall) ist ein externer Literaturclaim und muss im Paper direkt belegt werden.
3. C07-L-Rc (Directed-Trias-Lesart) bleibt eine projektinterne Integrationshypothese und muss durch eigenen Demonstrator plus Comparator-Test geprüft werden.
4. Die Trias wird nicht als Ersatz für Identifiability, Observability, System Identification, SciML-V&V oder Provenance-Frameworks dargestellt.

## Strategische Folge

Der wissenschaftliche ML-v0.2-Full-Run bleibt pausiert. D014 und der technisch fertige v0.2-Skeleton bleiben gültig und werden nicht verworfen.

Als nächste Abhängigkeit wird ein **Minimal Inverse-Direction Demonstrator v0.1** spezifiziert. Sein Zweck ist nicht, Zhai–Lucarini–Lai vollständig zu replizieren, sondern einen kleinen kontrollierten Test der inversen Directed-Trias-Kette zu schaffen:

```text
synthetic target
-> observation / missingness
-> reconstruction
-> fixed equation-discovery pipeline
-> inferred theory
-> forward dynamical assessment
```

## Revisionsbedingung

C07-L-Rc muss abgeschwächt oder gestrichen werden, falls der inverse MVP plus Comparator-Audit zeigt, dass die Directed-Trias-Darstellung keine zusätzliche Integrations-/Zuordnungsarbeit gegenüber etablierten Frameworks leistet.

## Nächste Entscheidung

Review und Freeze der Spezifikation `demonstrator/inverse_direction_spec_v0_1.md`. Vor deren GO erfolgt keine Implementierung.