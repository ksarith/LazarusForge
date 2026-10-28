# CROSS-FILE PATTERN FINDINGS — Session 2 (Files 6–8)

Issued 2026-10-27, Vibe (Skeptic/Auditor). Findings-only (PKC-020). Covers files 6–8: Admin/Security_Protocols.md (AUDIT_06), Admin/Safety_Protocols.md (AUDIT_07), Admin/Engineer_Protocols.md (AUDIT_08). Session 1's patterns X1–X7 remain in force (see CROSS_FILE_PATTERN_FINDINGS_Session1.md); this document records new instances per pattern and any genuinely new pattern.

## X1 — Scope Boundary lags body state
New instance, with a twist: AUDIT_07 F1 (MAJOR). In Safety_Protocols, the same pass that resolved SP-001 updated the Advisory and both sidecars but left the Scope Boundary's "(intended resolution of EP-005; confirmation pending, see SP-001)", Section I's "until the SP-001 cross-file review confirms", and the File Purpose gap-list asserting the pre-resolution state. X1 has now escalated from "boundary lags later additions" to "boundary lags the very pass that changed the state" — the same-pass reconciliation failure. Recommendation upgrade: the "Scope Boundary reconciled" line X1 already proposed should explicitly cover dependent stale claims (advisory/sidecar/body/boundary must flip together).

## X2 — PKC-031 "Proposed"→"Exploration" retirement
No new instance in files 6–8 (all three use current Status vocabulary).

## X3 — Colliding ASM-/unregistered prefixes
Three new instances: AUDIT_06 F1 (CF-006 defined in Security_Protocols' sidecar while CF- is Cognitive_Frameworks.md's namespace; no Kit ID-Reference row); AUDIT_07 F4 (Safety_Protocols defines ASM-001–006, and its ASM-001 basis cites Components.md ASM-002 — a sixth ASM- namespace surfaced); AUDIT_08 F4 (Engineer_Protocols defines ASM-001–004, fifth independent series). The ASM- collision is now confirmed in at least five audited files plus Components.md (unfetched). Recommendation unchanged but stronger: this is now past per-file notes — a single human namespace ruling (per-file prefixed ASM series, or Kit ID-Reference disambiguation rows) should precede the Operations/ sweep, where Gate_02's own ASM-006 already waits.

## X4 — Same-day pass logging
Two positive instances: Safety_Protocols' and Engineer_Protocols' 2026-10-27 passes (and their 2026-10-23/24/25 predecessors) are all logged same-day in RIP form, and the SP-001/EP-001 joint resolution is symmetrically recorded in both owning files with matched wording. Security_Protocols' 2026-10-23 pass likewise. No negative instances. The wave of PKC-028 "human-authorized autonomous management" passes (2026-10-27, SP+EP) is the best-logged doctrine change audited so far. Pattern risk shrinking; keep recording.

## X5 — Stale claims pinned against the Kit's ID Reference
New instance: AUDIT_06 F1 is the inverse case — a sidecar entry (CF-006) lives in a namespace the Kit's table does not cover at all. Combined with Session 1's GMP case (claims coverage that doesn't exist) and X3's ASM- silence, the ID Reference table is now stale in three directions. Recommendation: regenerate the table from a direct listing of live prefixes before the Operations/ sweep.

## X6 — Section-shape drift vs template
No new instances. Files 6–8 conform to the confirmed template shape (resolution of Session 1's X6 stands in AUDIT_01-05_TEMPLATE_RESOLUTION_2026-10-27.md). Security_Protocols carries non-template sections (Trust Boundary Declaration, EDL, Relationship, trailing Status) — legitimate additions, not drift.

## X7 — Trailing `## Status` staleness pending PKC-002
One new instance: AUDIT_06 F3 (Security_Protocols' trailing Status block date-stamped 2026-09-03 while passes ran through 2026-09-16; content still accurate). Safety_Protocols and Engineer_Protocols have no trailing Status block — noting as a positive divergence. PKC-002 ruling still pending; three files now ride on it.

## X8 (NEW, WARNING) — Drift-indicator condition text itself goes stale
AUDIT_08 F1: Engineer_Protocols' final local trigger enforces "Measured / Estimated / Analogous / Placeholder" — a set containing AP-021-retired "Estimated" and misapplied to the Lessons Learned Evidence Type column, which correctly uses File_Template §7's separate vocabulary. The indicator survived the 2026-10-23 section merge unreconciled. This is a genuinely new pattern: governance instruments (drift indicators) are not covered by their own drift indicators. Watch for it in every remaining file with local triggers — a trigger whose condition text cites another file's content must be re-derived against that file at each merge/touch pass.

## X9 (NEW, WARNING) — Stale "pending" narration after reconciliation completes
AUDIT_06 F2 (Security_Protocols' Relationship section: "SEC-008 through SEC-012 to be registered/reconciled at next Unknowns.md update; ... pending sync into this file's own sidecar" — all long since done) and AUDIT_07 F1's File-Purpose instance (gap list asserting EP-005 "has no definition" after the same-day definition). Distinguishable from X1: these are narration-of-intent passages left behind after the intended work completes, in sections the sweep's checks don't naturally revisit (Relationship, File Purpose). Recommendation: the "Scope Boundary reconciled" same-pass line from X1 should extend to a one-line "pending-work narration" check (Relationship section, File Purpose gap lists, advisory dependency sentences).

## Session 2 summary
Files done: 6, 7, 8. Findings this session: 0 CRITICAL, 1 MAJOR (AUDIT_07 F1), 6 WARNING (AUDIT_06 F1/F2/F5; AUDIT_07 F3; AUDIT_08 F1/F2), 5 NOTE. Positive patterns: X4 logging form now standard in new passes; §8 hazard-table in-row ID qualification (AUDIT_08) is the best citation practice seen — recommend the Kit cite it as the exemplar.

## Resume point
File 9 = Admin/Verification_Gates.md, then the rest of Admin remaining (File_Template itself, Canonical_Terms, Repository_Structure, Trajectories, Progress_Log, Forge_Audit_Kit, Operational_Conventions (exempt-class checks), Engineer/Skeptic support files as listed in Discovery), Auditor_Protocols last; then Architecture/ (15), Operations/ (19, Gates first), Tests/ (19) + Challenges/ (10), root navigation last. Automation/ skipped; Archive/ exempt. Carry X1–X9; carry the SESSION_STATUS open questions; the X3 namespace ruling is recommended before the Operations/ sweep.
