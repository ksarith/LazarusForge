# CAMPAIGN2_AUDIT_35_Tests-Tst_Scope_Map

**Audit of:** `Tests/Tst_Scope_Map.md`
**Campaign:** LazarusForge Campaign 2 — findings-only per-file audit (PKC-020; PKC-005 edit markers; findings-only passes never advance Last Audit/Status/Spec Gates)
**Auditor:** Vibe (AI Auditor, Campaign 2)
**Date:** 2026-10-30
**Repo head at fetch:** 4611f9f8dcdd9aeae4c099366806daaccf99f95f
**Fetched size:** 26850 chars (full text fetched and read)
**Deposit home:** Tests/TAudits

## Checklist Results
**Index audit — 17 entries verified against live owning files at head 4611f9f8.**
- Sidecar count parity: N/A (index creates no unknowns; header 0 ✓)
- Header vs body: File State table well-formed; Status Active — Index; Last Reviewed 2026-10-25
- Scope/cross-refs: all 17 file entries re-checked against live digests (Campaign 2 batches)
- Ethical Anchor: exact string ✓
- Aging: current (Last Reviewed 2026-10-25)

### F1 — WARNING — X8 stale row: MAQT entry says "0 Open Unknowns (registered)" but the live file has 3 registered sidecar entries
`Tests/Multi_Agent_Quorum_Trial.md` now carries MAQT-001–003 in its sidecar (registered 2026-10-10). The map's row still reads "0 Open Unknowns (registered)". Stale by ~20 days. Recommendation: row refresh alongside the standing ASM row-refresh recommendation.

### F2 — WARNING — X8 stale row: Support_Raft entry says "13 Open Unknowns"; live header says 12
`Tests/Support_Raft.md` Open Unknowns was corrected 2026-10-24 from 13 to 12 (SR-010 is Resolved 2026-06-11, retained in the sidecar as institutional memory, and matches the 12 SR rows in `Unknowns.md`). The map's Last Reviewed (2026-10-25) postdates the correction but missed it.

### F3 — WARNING — X8 self-contradictory row: QCC entry says "0 registered Unknowns" while also stating QCC-R2, R5 and R7 "also indexed in `Unknowns.md`"
If R2/R5/R7 are indexed in `Unknowns.md`, three unknowns are registered — "0 registered" cannot simultaneously hold. The live file's File State says "7 (sidecar below, all non-blocking); QCC-R2, QCC-R5, QCC-R7 also indexed in `Unknowns.md`". The map row needs a count-convention decision (registered vs sidecar-tracked) before refresh.

### F4 — NOTE — Inherited X10 risk labels in map rows
The map's Risk fields for Cognitive_Salvage_Layer, Pyrolysis_Cascade and Solar_Descent all read "High", mirroring the owning files' headers — but each file currently has an open Critical sidecar entry (GH-009; PYC-001/003/004; SD-UNK-004). The map is faithful to its sources; the defect is in the owning files (see the standing Highest-Risk recompute batch). No map action until the owning headers are recomputed.

### F5 — NOTE — Positives
- Hydrologic "2 Formal / 6 Unregistered" pattern accurately carried (standing registration decision remains with the human).
- Field_Logs entry current through the 2026-10-06 correction, correctly logged.
- Leviathan forward reference (`Operations/Leviathan.md` "planned") previously verified absent-and-correctly-labeled; no re-check needed.
- 2026-10-25 PKC-041/PKC-031 status corrections properly logged in the map's own Resolution Log.
## Disposition

Findings-only (PKC-020): no changes were made to the audited file; no Status, Spec Gate, version, or Last Audit advancement. This report is deposited at Tests/TAudits under the append-only rule; any correction to it must be a dated addendum, never an edit.
