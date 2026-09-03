# D026 — Novelty-Audit akzeptiert; C08-D-R2 und genealogischer Paper-Rebase

**Datum:** 2026-09-03  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D024, D025, `literature/relational_profile_novelty_audit_v0_1.md`

## Entscheidung

Der `Relational-Profile Novelty Audit v0.1` wird als verbindlicher aktueller Literaturstand akzeptiert.

Damit wird ausdrücklich verworfen, die bloße Dreieckstopologie

```text
Reality/Target — Theory/Conceptual Model — Computation/Computerized Model
```

oder die drei Paarrelationen als originäre Trias-Neuheit zu beanspruchen. Die klassische Model-Credibility-/V&V-Tradition um Schlesinger/Sargent ist hierfür ein zentraler historischer Direktvorläufer und muss im Paper genealogisch, nicht nur als Randvergleich, behandelt werden.

## C08-D-R2

Die revidierte Fassung **C08-D-R2** wird als aktueller Working Claim akzeptiert:

> Die Descriptive Trias wird nicht als neue Dreieckstopologie von Realität, Theorie und Berechnung beansprucht; eine strukturell sehr ähnliche Triade aus Reality/Problem Entity, Conceptual Model und Computerized Model mit den Relationen qualification/conceptual validity, verification und validation ist in der klassischen Model-Credibility-Literatur etabliert. Der mögliche Beitrag der Trias liegt in einer wissenschaftsphilosophischen Generalisierung dieser Struktur für Computational Science und AI for Science: `T` wird als expliziter theoretischer, mechanistischer oder erklärender Claim typisiert und kann fehlen oder datengetrieben inferiert werden; `C` umfasst numerische, gelernte und inferierende computational realizations; und Evidenz wird claimspezifisch danach profiliert, welche Relation sie tatsächlich stützt. Diese Generalisierung ist als interpretative Synthese zu positionieren, nicht als neue V&V-Theorie.

## Akzeptierter Evidenzstatus

```text
R/T/C topology novelty: REJECTED
edge distinction novelty: REJECTED
analytical discrimination across project cases: POSITIVE
AI-for-Science reinterpretation/generalisation: PLAUSIBLE
practical utility: UNTESTED
unique originality of the generalisation: NOT YET ESTABLISHED
```

## Genealogischer Rebase

Das Paper darf nicht mehr mit `we introduce a triangle of reality, theory and computation` eröffnen.

Stattdessen lautet die neue genealogische Logik:

```text
classical model credibility triangle
        ↓ generalisation
scientific-theory claim + computational practice + target
        ↓ extension to AI for Science
black-box prediction / surrogate learning / PINNs / equation discovery
        ↓ descriptive reading
which kind of scientific success is evidenced, and relative to what target/claim?
```

Schlesinger/Sargent werden damit zu konstitutiven Vorläufern des Projekts.

## Verbleibender zu prüfender Delta

Der Mainline-Claim darf nur dort stärker werden, wo die Generalisierung über klassische Simulation-V&V hinausgeht. Kandidaten sind:

1. `T` als wissenschaftlicher Theorie-/Mechanismus-/Erklärungsclaim statt nur als simulation conceptual model;
2. `T = NONE_CLAIMED` bei Prediction ohne Theorieclaim;
3. `T` als Output einer computational inference, etwa Equation Discovery;
4. `C` als learned/inferential computational practice statt nur als Implementierung eines gegebenen Modells;
5. gleiche Metrik, aber unterschiedliche epistemische Bedeutung je nach Relation und Target;
6. deskriptive Profilierung von Arten wissenschaftlichen Erfolgs statt primär normative Credibility-Zertifizierung.

Diese Punkte sind noch keine final bewiesene Originalität.

## Strategischer Freeze

Keine neue numerische Mainline. ML-v0.2 und inverse v0.2 bleiben pausiert. C06-R2 bleibt konservative Fallback-Boundary.

## Freigegebener nächster Schritt

Als nächste Abhängigkeit wird ausschließlich ausgearbeitet:

`Paper Contribution Boundary v0.2 — From Model-Credibility Triangle to Descriptive Trias for AI for Science`.

Dieses Dokument muss den genealogischen Hauptclaim, Non-Claims, den exakten AI-for-Science-Delta, die Rolle der bestehenden Projektfälle, die Paperstruktur und harte Abbruch-/Abschwächungskriterien vor dem eigentlichen Manuskriptschreiben festlegen.