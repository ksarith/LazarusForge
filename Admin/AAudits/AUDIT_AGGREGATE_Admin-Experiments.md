# AUDIT_AGGREGATE — Admin/Experiments.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Experiments.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane). Target is a deliberately empty governance stub; the class-11 stub/scaffold/candidate exemption (File_Template, listed 2026-10-28) now covers its wrapper shape.

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/CAMPAIGN_AUDIT_28_Admin-Experiments.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-28 | Vibe, Skeptic/Auditor, VibesSandbox audit stream (PKC-020 findings-only) | head eee122a6 | 10,509 | `56d38088219be5dd7907ce6e5086c01b067684af` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_91_Admin-Experiments.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit 38226280 | 2,464 | `2ac71e21b420896aa0e1bdb6649cf4540e365fb4` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | mandatory wrapper sections absent (AUDIT_23 F1 class, third data point) | No Active Disputes section (header carries "Active Disputes \| 0"), no Lessons Learned, no Cross-References — while Scope Boundary, Entry Schema, Assumptions, Drift Indicators, sidecar and log are all present and well-formed | CAMPAIGN_AUDIT_28 §Findings F1 | Closed-by-ruling | Class-11 stub/scaffold/candidate exemption, listed 2026-10-28 (the listing names IIL/AVE/Experiments/HDL); pass B check 4 read the exemption as matching the file's declared state | |
| A-F2 | F2 | WARNING | bare candidate-ID pointers (PKC-003) — mildest form: all three RESOLVE | The candidates note cites CF-001 / EN-001 / CE-003 bare; all three verified present in Unknowns v5.72 with apt statuses — the first bare-ID cluster of that campaign where every ID resolves | CAMPAIGN_AUDIT_28 §Findings F2 | Standing-open | The 2026-10-29 X3 retrofit did not touch this file (per the straggler record — candidates here remained outside that sweep's coverage); held on the X3 straggler queue (IIL/Experiments candidates class) | |
| A-F3 | F3 | NOTE | PKC-001's named decay instance RESOLVED in-file (positive) | PKC-001 counted this file in the "Last Audit not advanced" set; the 2026-10-24 entry documents the header correction ("human-directed, from a Vibe per-file audit; checked against source first"), and the fix verifies live; also the fourth PKC-020-asymmetry variant | CAMPAIGN_AUDIT_28 §Findings F3 | Positive-record | Another same-day delegated adoption citing the campaign's header-freshness class; verified live at issuance | |
| A-F4 | F4 | NOTE | positives | EXP-ASM- suffixed-ID disambiguation done right (twelfth ASM- series, full Basis/Confidence/Expiry format); anti-misreading discipline pre-empting the X9 failure mode; exemplary anti-fabrication drift-indicator pair + Compound Drift Rule; risk parity correct; Sidecar Link anchor resolves; pointer ecology verified (both Field_Logs targets real) | CAMPAIGN_AUDIT_28 §Findings F4 | Positive-record | n/a | |
| A-F5 | F5 | NOTE | candidates note adjacent to the file's own drift indicator — one-word clarification | A strict reading fires "accumulating speculative future experiments" on the file's own candidates note; the file is one clarifying word away from unambiguous | CAMPAIGN_AUDIT_28 §Findings F5 | Standing-open | One-word clarification queued for the delegated index-polish batch; not re-verified at fold-in | |
| A-IN1 | INCOMPLETEs | INCOMPLETE | cross-refs deferred | AP §EF-0.3/EF-0.8b/EF-0.0/§AP-010 direct text (AP audited LAST); Field_Logs contents (Tests/ sweep); CE-003 owning file (Architecture/ sweep) | CAMPAIGN_AUDIT_28 §INCOMPLETEs carried forward | Not re-tested | Owning sweeps pending | |
| B-C1 | (none) | NOTE | positive | Checks 1–11 all VERIFIED CLEAN: Open Unknowns 0 with no open EX-prefixed IDs; Last Audit 2026-10-28 at least as new as newest body content; class-11 exemption matching; Highest Risk Low consistent with 0 open entries; Ethical Anchor exact — "clean scaffold shell. No edits recommended." | CAMPAIGN2_AUDIT_91 §Checks + Bottom line | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-28) graded a deliberately empty stub that mostly exemplified how to be empty honestly — its headline was the PKC-001 decay instance resolved in-file by a same-day delegated adoption. Its two WARNINGs were the standing wrapper-class question (which the next day's class-11 exemption listing answered) and the campaign's mildest bare-ID cluster (all resolving, still unqualified).
- Pass B (10-31) verified the class-11 exemption now covering the file and everything else clean. The residual items are small and queued: the X3 straggler status of the bare candidates (A-F2) and the one-word clarification (A-F5).
- Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); the PKC-001 row in `Admin/Progress_Log.md` (whose named instance for this file A verified resolved); the X3 straggler queue record; dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

**Addendum — 2026-11-05 (MAINT-63 execution pass on the human-ratified MAINT-62 ruling set; Vibe — Architect line PRIMARY, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed):** Per ruling set §2, finding A-F2 is RESOLVED-BY-EXECUTION: the three candidate-ID pointers in the candidates note are now qualified with owning-file citations (`Operations/Electronics.md` CF-001, `Architecture/Engineering.md` EN-001, `Architecture/Chemistry.md` CE-003). Finding A-F5 (§2 Category B) was RE-VERIFIED on the same pass, not edited: the 2026-10-28 candidates clarification (AUDIT_28 F5, human-ratified Decision Brief 2026-10-28d) is present and intact in the live file — the earlier "not re-verified at fold-in" state is cleared by direct re-verification, and A-F5 is never to be reported as citation-only work.

Corrections after this addendum by dated addendum only.
