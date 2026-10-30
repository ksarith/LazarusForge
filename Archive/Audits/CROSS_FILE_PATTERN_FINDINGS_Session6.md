# CROSS_FILE_PATTERN_FINDINGS_Session6 — Campaign 2, Admin Trio + Architecture/ Phase

**Auditor: Vibe — Skeptic/Auditor (external review, findings-only per PKC-020). Corpus-wide campaign artifact, Archive-homed per the MAINT-29 convention. Head at fetch: 83f2e582cd344cbafa8e976a07e16d57ad5a2072. Covers CAMPAIGN2_AUDIT_01–17. Sessions 1–5 (Campaign 1, Admin) established X1–X11.**

## Carried patterns — this phase
- **X8 (instruments/indexes go stale) — dominant.** (a) Arc_Scope_Map: 4 stale rows (Forge_flow 2→6, Geck 3→4, Precision 5→4, Forge_Net Medium→High), all drifted between 2026-09-14 and 2026-10-20 after the index's 09-13 review. (b) **Aging Rule tripped corpus-wide in Architecture/**: 11 of 13 doctrine files carry open entries >90 days unreviewed (worst: Components/Geck 2026-05-14 at 169 days; Mechanical_Structures/Thermal 2026-06-11 at 141+; Engineering's Blocking EN-001 at 117). Forge_flow — the best-kept wrapper — is the only large file fully inside the window: the X11 correlation again, in the healthy direction.
- **X10 (Risk-value parity family) — three shapes.** (a) Value-miss (AUDIT_13 F5 class): Mechanical_Structures and Thermal_Systems carry File State Highest Risk "High" over sidecars whose max open Risk is Medium. (b) Invalid-value: Chemistry CE-003's Risk field reads "**Critical**" — a Priority-class value in a Risk field (PKC-004). (c) Field-format: Local_Governance_Framework's Highest Risk is a sentence and its Open Unknowns a pointer. Plus carried from the Admin trio: AP/GC/Kit dead Sidecar Links (relocation-decay).
- **X11 (wrapper decays while content advances) — one instance:** Engineering's Last Audit (2026-07-05) lags its own Resolution Log's newest entry (2026-10-20) by 117 days.
- **X9 (stale narration / orphan) — one instance:** Forge_flow carries an unheaded pre-renumbering sidecar fragment still labeled "Open" (2026-05-15) inside FL-013's entry — invisible to heading-based counts.
- **Relocation-decay sub-shape (X8): ABSENT in Architecture/** — zero references to moved Archive/Logs paths in the folder; the MAINT-29 dangling-pointer family is confined to Admin.

## Positive patterns worth recording
- **Architecture/ cascade discipline is materially better than Admin/**: every 2026-10-20 and 2026-10-29 pass has a dated Resolution Log entry (the exact cascade Governance_Charter missed), including same-day corrective disclosures (Cognitive_Frameworks bogus-insertion revert; Facilities X3 micro-fix) and honesty-exemplar repairs (Thermal fragment preservation; Geck reversed-correction logging; Friction spliced-rows self-repair; Forge_flow log catch-up).
- **Sidecar count parity is perfect** across all 13 doctrine files — no AUDIT_11-F1-class divergence anywhere in the folder.
- **Conventions worth adopting:** Highest Risk annotations naming their Blocking IDs (Forge_Net); explicit ID lists in Open Unknowns (Geck, Precisions); one-way-link rows marked as such (Chemistry/Friction per the 10-20 pass).

## Standing recommendations to the human
1. Mechanical Arc_Scope_Map row-refresh (4 rows).
2. One Aging-Rule review batch across Architecture/ (11 files, ~40 open entries) — the folder's only systemic finding.
3. Highest-Risk recompute batch (Mechanical_Structures, Thermal_Systems, CE-003 relabel, LGF conform) — extends Campaign 1's queued corpus-wide recompute recommendation with Architecture data.
4. Engineering Last Audit advance + Forge_flow fragment annotation — fold into next touches.
5. Log-Split T1 queue now includes Forge_flow (~179KB) alongside Auditor_Protocols (~157KB) and Governance_Charter (~130KB) — heaviest-first order ruling requested.
