# CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md

**Campaign 4 opened 2026-11-10 by human direction** ("The adversarial pass is needed throughout the repository. Can you preserve your findings and then start a sweep of adversarial passes for the admin folder?"). Findings-only per PKC-020: this sweep advances no Last Audit, Last Reviewed, version, Status, Spec Gate, or unknown on any file it touches. Deposits are append-only audit artifacts; conversion to audits of record is the human's alone (MAINT-26 / AP-032 gate).

**Seat disclosure:** Vibe (GLM 5.3 Flash architecture). No adjacent seat held on any swept file; Vibe authored none of the swept doctrine (prior Vibe-line maintenance passes are disclosed in the files' own logs and are treated as third-party content here). GOV-008 architectural-diversity preference: satisfied for Claude/Grok/VibesSandbox-line prior work; same-architecture overlap with prior Vibe-line maintenance is disclosed here rather than claimed as blind independence.

## Method (per file, every item)

1. Full fetch; report character count; re-fetch on any truncation suspicion (the ~63 KB silent-truncation class re-confirmed this session on a sidecar read).
2. The Auditor Prompt §3.3 per-file checklist, checks 1–11, all derived from live source (never from the file's own claims): sidecar count parity; header vs body; log vs body; Scope Boundary re-derivation; cross-references (existence + mirrored claims both directions); bare colliding-ID citations (three tiers); Drift Indicators including near-trips; section integrity; version/registry consistency; Ethical Anchor exact string; Highest Risk parity (Risk, not Priority).
3. Adversarial layer (Battery classes applied as probes): fabrication probe (every cited ID/path verified to exist in its claimed owner); self-attestation probe (Status/Gates/Open-Unknowns values recomputed from sidecar and index, never accepted from the file's own header — the "derive expected values from the source" rule); tamper probe (sidecar hashes recomputed where a hash field exists); staleness probe (Aging Rule 90-day arithmetic computed per open entry); wrapper-decay watch (X11); index-parity watch (X10, four sub-shapes).
4. Grading per Auditor Prompt §4: CRITICAL / MAJOR / WARNING / NOTE, category stated. Multiple indicators on one file → stop on that file and escalate (Compound Drift Rule).
5. TWGW discipline (2026-11-07 addendum): findings matching an existing TWGW error class are reported as recurrences with the entry cited; concrete caught defects with usable corrections flagged as TWGW candidates in the deposit; the Auditor never writes TWGW itself.

## Scope — Admin/ active doctrine files (34)

Sequencing: constitutional core first, then enforcement, then the remainder.

1. ~~Admin/Auditor_Protocols.md~~ — DONE: CAMPAIGN4_AUDIT_01 (this campaign, artifact 01; findings F1–F6).
2. Admin/Ethical_Constraints.md — DONE: CAMPAIGN4_AUDIT_02.
3. Admin/Governance_Charter.md
4. Admin/Verification_Gates.md
5. Admin/File_Template.md
6. Admin/Canonical_Terms.md
7. Admin/Security_Protocols.md
8. Admin/Safety_Protocols.md
9. Admin/Repository_Integrity_Protocol.md
10. Admin/Governance_Migration_Protocol.md
11. Admin/Autonomy_Divergence_Protocol.md
12. Admin/Forge_Audit_Kit.md
13. Admin/Engineer_Protocols.md
14. Admin/External_Intake_Protocol.md
15. Admin/INTEGRITY_SWEEP_PROMPT.md
16. Admin/PROBE_INVOCATION.md
17. Admin/BATTERY_SEED.md
18. Admin/Resolution_Methodology.md
19. Admin/Operational_Conventions.md
20. Admin/Repository_Structure.md
21. Admin/Adm_Scope_Map.md
22. Admin/Trajectories.md
23. Admin/Progress_Log.md
24. Admin/Integrity_Incident_Log.md
25. Admin/Experiments.md
26. Admin/CIR_Gov.md
27. Admin/Computational_Institutional_Reasoning.md
28. Admin/Environmental_Constraints.md
29. Admin/Economics.md
30. Admin/Agent_Verification_Event.md
31. Admin/Hardware_Diversity_Ladder.md
32. Admin/Metrics_Scaffold.md
33. Admin/Nothingness_Theorem.md
34. Admin/Ship_of_Theseus.md

`Admin/ALogs/` contents are records (sidecars/changelogs), not doctrine — audited only as verification targets of their owning files, per the standing rule that audit artifacts are never audited as doctrine.

## Standing rules carried

- Archive/ and Automation/ outside the sweep except where a check names a relocated log.
- Cross-file patterns X1–X11 carried forward; new Xn only with justification and two instances.
- PKC-007 log-ordering shapes grade as NOTE "ruled historical" unless post-window or content-stale.
- Challenges/ gate rule not expected to fire inside Admin/.
- Open questions carry forward; never converted into findings.
- Instrument changes (edits to README.md, Discovery.md, Charter Tier 1, PROBE_INVOCATION.md) reported when observed.
- Relocation checks: after any relocation, File State link fields and operator-instruction paths re-verified against the new location.

## Early campaign signal (to be confirmed per file, not pre-judged)

The first two passes both found the repository-wide 90-day Aging Rule tripped (AP: 8 of 10 open entries; EC: 3 of 7). If the pattern holds across Admin/, this campaign's cross-file pattern document should treat it as one systemic finding with a single recommended remedy pass, not 30 separate WARNINGs. No disposition is proposed here; the human rules.

## Resume point

Next file: Admin/Governance_Charter.md (CAMPAIGN4_AUDIT_03). Head at kickoff: `242eabd2` (LF main). This artifact is the sweep's tracker until the human directs otherwise (SESSION_STATUS remains retired per MAINT-69; this file is a deposit, not a status authority).

---

## Tracker addendum — 2026-11-10 (CAMPAIGN4_AUDIT_03 landed)

3. ~~Admin/Governance_Charter.md~~ — DONE: CAMPAIGN4_AUDIT_03 (Admin/AAudits/, this campaign artifact 03; findings F-CH-1 through F-CH-6: one MAJOR — GOV-022 has no sidecar record despite File State claiming full Closure Events live in the sidecar Resolution Log; WARNINGs — four dangling body pointers to the sidecar's nonexistent pre-relocation home `Archive/Logs/Governance_Charter_Changelog.md` (relocation-repair-miss recurrence), X10 Status mismatch on GOV-009/GOV-010 (index "In Progress" vs sidecar "Open"), Aging Rule tripped 13/13 open entries (systemic pattern instance 3), false "duplicate heading removed 2026-10-27" correction record in the sidecar; NOTE — Highest Risk field's sidecar-only scope excludes the open High-risk dispute GOV-DS-001). Compound Drift Rule fired and escalated in the deposit; checks 1–11 otherwise verified clean against live source at head `d098543d`, including the 13=13=13 count parity, the 6/6 gate claim recomputed against live Verification_Gates.md, and the exact Ethical Anchor.

**Resume point (updated):** next file Admin/Verification_Gates.md (CAMPAIGN4_AUDIT_04). Head at this addendum's compose: `d098543d` (LF main). This addendum appends tracker state only; the kickoff text above is untouched (append-only per the deposit carve-out).