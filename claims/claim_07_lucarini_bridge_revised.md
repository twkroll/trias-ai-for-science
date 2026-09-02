# C07-L-R — Directed Trias / Equation-Discovery Bridge

**Status:** ACCEPTED AS WORKING CLAIM — D016  
**Stand:** 2026-09-02  
**Depends on:** C06-R / D009, D015, `literature/c07_l_comparator_audit.md`

## Akzeptierte moderate Claim-Fassung

> **C07-L-R:** Bei datengetriebener Equation Discovery ist die Güte eines inferierten Modells mehrdimensional: strukturelle Übereinstimmung der Gleichungen, dynamisch-statistische Adäquanz und physikalische Interpretierbarkeit sind nicht gleichzusetzen. Zhai, Lucarini und Lai liefern einen konkreten chaotischen Fall, in dem unterschiedliche Beobachtungs-/Rekonstruktionsbedingungen zu strukturell verschiedenen inferierten ODEs führen, während ausgewählte Langzeit- und Koopman-Eigenschaften ähnlich bleiben. Für die Trias dient dieser Befund nicht als neue Identifiability-Theorie, sondern als inverser Testfall für die Hypothese, dass wissenschaftliche Rechtfertigung die Provenance und Richtung der Transformation `target/observation -> data -> inference -> theory` explizit auditieren sollte.

## Claim decomposition

### C07-L-Ra — etablierter methodologischer Unterschied

```text
structural equation fidelity
!= dynamical/statistical adequacy
!= physical interpretability
```

Dies wird **nicht** als Trias-Neuheit beansprucht. Es ist anschlussfähig an structural/practical identifiability, observational equivalence/equifinality, system identification mit structural error, model pluralism und underdetermination.

### C07-L-Rb — konkreter Literaturfall

Zhai–Lucarini–Lai zeigt für chaotische Equation Discovery eine Pipeline, in der verschiedene Missingness-/Rekonstruktionsbedingungen stark unterschiedliche inferierte ODE-Strukturen erzeugen, während relevante Attraktor-, Lyapunov- und dominante Koopman-Eigenschaften ähnlich bleiben.

Dieser Teil ist ein Literaturclaim und muss im Paper direkt belegt werden.

### C07-L-Rc — projektinterne Trias-Interpretation

Die Directed Trias behandelt den Fall als inverse epistemische Transformationskette:

```text
R / target
-> C_obs
-> D
-> C_pre
-> C_infer
-> T_hat
```

und fragt an jedem Übergang:

- welche Information wird erzeugt/verloren;
- welche Wahl ist methodologisch relevant;
- welches Objekt wird tatsächlich validiert;
- welche Äquivalenz wird behauptet;
- welcher wissenschaftliche Gebrauch verlangt welche Form von Adäquanz.

Dieser Teil ist eine **Integrationshypothese**, kein etablierter Literaturbefund.

## Explizite Non-Claims

- keine neue Theorie struktureller oder praktischer Identifizierbarkeit;
- keine neue Theorie von Observability;
- keine neue Entdeckung von Equifinality oder observational equivalence;
- kein allgemeiner Beweis für Underdetermination aller datengetriebenen Modelle;
- keine Behauptung, SINDy oder Equation Discovery sei grundsätzlich wissenschaftlich ungeeignet;
- keine Behauptung, direkte ML-Modelle seien epistemisch überlegen;
- keine Behauptung, W3C/workflow provenance oder SciML V&V übersehe Datenverarbeitung;
- keine Behauptung, die Trias sei gegenüber diesen Frameworks bereits überlegen.

## Revisionskriterium

C07-L-Rc wird abgeschwächt oder gestrichen, wenn ein eigener inverser MVP und der anschließende Framework-Vergleich zeigen, dass die Directed-Trias-Darstellung keine zusätzliche Integrations-/Zuordnungsarbeit gegenüber einer Kombination aus System Identification, Identifiability/Observability und SciML/V&V/Provenance leistet.

## Entscheidung D016

Die starke C07-L-Neuheitsfassung ist verworfen. C07-L-R ist als moderate Arbeitsfassung akzeptiert. Als nächste Abhängigkeit wird `demonstrator/inverse_direction_spec_v0_1.md` geprüft. Der ML-v0.2-Full-Run bleibt bis zur späteren strategischen Entscheidung pausiert.