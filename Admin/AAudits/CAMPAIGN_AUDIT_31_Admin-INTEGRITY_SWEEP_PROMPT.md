# CAMPAIGN_AUDIT_31 — Admin/INTEGRITY_SWEEP_PROMPT.md

**Deposited:** 2026-10-29 — Auditor (PKC-020 findings-only campaign pass, Admin sweep file 31; direct deposit per the Auditor deposit convention). No audited-file field was advanced by this pass.

**Target:** `Admin/INTEGRITY_SWEEP_PROMPT.md` — header v1.0.5, File State Status: Draft, Open Unknowns: 0, no sidecar. Blob 27d0fd38, 19,052 bytes, fetch-complete at live head 34f542dc. The target is unchanged since its commissioning annotation (commit 47a469e7, 2026-10-29) — the same blob the campaign recorded at provenance-30 head 7908154.

**Live cross-checks this pass:** `Routing.md` (target row), `Discovery.md` (directory-tree entry + Repository Maturity Snapshot row), git history for the target path (8 commits, 2026-08-30 → 2026-10-29, no discontinuity). `Unknowns.md` not re-fetched: the file's ID references assert no Open/Resolved states beyond those already verified live this session (parked rows 45 total / 37 Resolved / 8 open).

**Grades: 0 CRIT / 0 MAJ / 1 WARN / 4 NOTE.**

---

## Findings

### F1 — WARN: Wrapper gaps (operational-prompt-template family, member 2 of 3)

No Navigation Anchors block (violates `Routing.md`'s File Template Backlink Requirement — the target's own Routing row demands "Explicit"). No Assumptions, Active Disputes, Drift Indicators, Lessons Learned, sidecar, or trailing Status section. Highest Risk absent; Last Reviewed absent (the file carries a current Last Audit field, 2026-10-29, which is not the same field).

One intra-family divergence worth recording: **File Purpose IS present** in this file (unlike PROBE_INVOCATION, AUDIT_30 F1) — and it is strong (documents the canonical-source rationale and the automation-sync instruction). The family is not uniformly minimal.

Family disposition still pending: the enacted exemption classes do not name this operational-prompt-template family (PROBE_INVOCATION, BATTERY_SEED, INTEGRITY_SWEEP_PROMPT); the human ruling requested from AUDIT_30 (6th data point for the exemption-vs-sections family) remains open, and this file is the second of three data points. Compounding observation: the file's own 2026-08-31 Resolution Log entry describes PROBE_INVOCATION.md and BATTERY_SEED.md as "sibling exemption-class-6 files" and corrected this file's Verification Ref to "match that pattern" — so this file implicitly relies on the class-6 exemption pattern without, on any evidence this pass could verify, being named in class 6 itself. Routed to the human (family ruling) and added to the Auditor_Protocols audit inheritance set (AP audited LAST).

### F2 — NOTE: Status "Draft" deliberately held past its own trigger point

The body documents a scheduled daily automation (Grok) running against the live repo, and the instrument is now commissioned (Decision Brief 2026-10-29, item 1 option B) to execute once at campaign end, corpus-wide. Status remains Draft — but this is not unexplained drift: the 2026-08-30 v1.0.1 entry records that promotion to "Active — Operational Template" was deliberately held pending confirmation that the automation actually pulls from this file rather than a hand-copied config, and no such confirmation appears in the Resolution Log in the two months since. The held state is honest, but the pending confirmation is now two months stale and the commissioning makes execution-from-canonical-file the operative plan. Routed to the human: confirm the automation's config source (or rule the Status promotion); any enactment would be a custodian pass, not this one.

### F3 — NOTE: Derived-from pin stale vs live Kit (non-drift per PKC-022 opt B; content-checked)

"Derived from" pins `Admin/Forge_Audit_Kit.md` **v1.15**; the live Kit is v1.29. Stale version pins are non-drift per PKC-022 opt B, so a content-based check was done instead: the prompt depends on the Kit only as (a) the default condensed audit reference fetched first (step 1) and (b) the Ethical Anchor source (step 2) — both stable across v1.15→v1.29. The v1.29 Spec Gates hold dissolution (gates 0/6) does not touch this file's steps or its own N/A cell. The `Admin/Repository_Integrity_Protocol.md` pin is unversioned. No dependency broken.

### F4 — NOTE: Workflow wrapper still describes the finding-application path as zip-only (the file's own step-15 genus, mild)

File Purpose describes the repository as "worked primarily through periodic zip uploads… not continuous live access," and How-To-Use step 4 tells the operator that findings "get fixed against the actual working copy — currently the zip-based session workflow, not directly against GitHub." Both current custodial lines (this auditor line and the delegated custodian line) now work live against GitHub with fetch-before-edit; the target's own recent commits show both workflows in coexistence (2026-10-24/26 "Add files via upload"; 2026-10-27/28/29 direct pushes). The human's own passes may still be zip-primary, so this is not graded drift — but the wrapper describes how findings get applied as zip-only, which no longer matches how maintenance is actually enacted by the custodial lines. Wording-refresh candidate for a custodian pass; harmless to the prompt's function (its own instructions fetch live and are automation-agnostic).

### F5 — NOTE: ID hygiene clean; no dangling IDs

All bare tier-2 IDs are consistent with live-known states: PKC-001 (×4) correctly framed as resolved 2026-10-27 / closed satisfied-by-adoption 2026-10-29 (matching the Decision Brief item 2 option A ruling ingested this session); PKC-020 (split policy, 2026-10-25) correct; PKC-026 (open; one of the eight parked open rows) used only as historical attribution with no status claim; X11 is a Decision Brief ruling label, not an Unknown; GOV-003/SEC-007a and WA-002/PL-001 appear only inside a dated 2026-08-30 Resolution Log narrative as historical cluster examples, correctly framed as history. No dangling IDs. No Open/Resolved claims required a fresh Unknowns fetch. The X3 designation retrofit (authorized, staged Admin/ first) will qualify these citations in the separate custodial pass — not this session's claim, and not drift while that pass is pending.

---

## Positives

1. **Commissioning annotation integrity** — the exact test the 2026-10-29 ruling set: header honestly stayed 1.0.5 ("No step changed or renumbered" — verified against the body: steps 1–15 sequential, steps 13/14/15 added in order per the Resolution Log, none renumbered); Last Audit updated same-day with full provenance; Resolution Log cascade followed (2026-10-29 entry present). The file passes its own step-14 (log-vs-body) and step-7 (header-vs-body) checks.
2. **Scope honesty** — the commissioning annotation explicitly records that the recommendation's original scope statement was conversational, not deposited as an artifact, and that the human governing authority sets the target set at execution. This matches the Decision Brief item 1 option B ruling exactly as ingested this session.
3. **PKC-001 closeout consistency** — step 14 is correctly identified as the adopted inverse check; the 2026-10-27 entry names it "the PKC-001 row's sweep-prompt candidate"; the closeout cross-reference to `Admin/Progress_Log.md` is present; step 14's body text carries the correct resolution date (2026-10-27) and the correct PKC-020 findings-only exemption.
4. **Registration parity exact** — Routing row present (Explicit backlink demanded); Discovery directory-tree entry present; Repository Maturity Snapshot row present with Status Draft matching the file, the Spec Gates N/A string matching the file's File State cell **verbatim** (the same verbatim-parity pattern AUDIT_30 verified for PROBE_INVOCATION), and the Highest Risk cell honestly "—" mirroring the absent field. Three-way consistent (file / Routing / Discovery).
5. **Decline-with-evidence practice** — the 2026-08-31 entry documents two sweep findings checked against `Admin/File_Template.md` directly, found to be false positives (the lean Challenges schema is a documented deliberate choice; "Pending Ratification" is not a File_Template column), and declined with citations. Exemplary.
6. **Honesty-rules block** — the embedded anti-invention guards (no Major for the V0 legacy alias, no sidecar-parity claims for files not opened, no invented version bumps or closures, cluster-ID grading guards requiring the owning sidecar before grading) are the sweep's own PKC-020-adjacent protections and are in good order.
7. **Evidence-label family: no divergence** — the file defines its own report shape and does not mis-reuse AP's five-label evidence set (unlike PROBE_INVOCATION's Step 2 four-label divergence, AUDIT_30 F2). This file contributes no data point to the AP evidence-label family.
8. **Git continuity clean** — 8 commits, 2026-08-30 → 2026-10-29, no delete+re-add discontinuity (unlike PROBE_INVOCATION's 2026-08-10 dec3f13f→60469463 break); the "Add files via upload" commits are the documented coexisting workflow, not lost history.
9. **Open Unknowns = 0 with no sidecar** — trivially consistent (nothing to miscount).
10. **Ethical Anchor** — exact canonical string, verbatim.

---

## PKC-020 compliance

Findings-only pass: no Last Audit, Last Reviewed, version, or Status field of the audited file was advanced; nothing was ratified; no doctrine was edited; the single repository write performed by this pass is this report's own deposit into the append-only `Archive/Audits/`; no previously deposited artifact was edited. Roles segregated: the custodial commissioning annotation (commit 47a469e7) was the delegated custodian line's act; this pass made no edits to the target.

**Routed items:** F1 → human (operational-prompt-template family exemption ruling; AP audit inheritance set). F2 → human (Status promotion / automation-source confirmation). F4 → custodian backlog (wording refresh of File Purpose + How-To-Use step 4, next custodial pass). F5 → X3 retrofit pass (already authorized, staged Admin/ first, custodial line).

**Next:** CAMPAIGN_AUDIT_32 = `Admin/BATTERY_SEED.md` (the third and final member of the operational-prompt-template family).
