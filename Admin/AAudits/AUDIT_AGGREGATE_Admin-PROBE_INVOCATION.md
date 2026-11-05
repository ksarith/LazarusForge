# AUDIT_AGGREGATE — Admin/PROBE_INVOCATION.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/PROBE_INVOCATION.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane). Target is an operational prompt template (AP §Mission Drift Review turn-key companion); the class-6 operational-template exemption covers its form.

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/CAMPAIGN_AUDIT_30_Admin-PROBE_INVOCATION.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-29 | Vibe, Skeptic/Auditor, VibesSandbox audit stream (PKC-020 findings-only) | head 79081542 | 12,449 | `e106b47d381fdfe6ab3863a07cbce1ed7de72b5f` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_89_Admin-PROBE_INVOCATION.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit 38226280 | 3,930 | `eb1dc3dc35577e7fadb7ea338f85d42852c39294` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | wrapper gaps; no enacted exemption class covered the file at pass time | No Navigation Anchors block (violating Routing.md's File Template Backlink Requirement, a stated MUST); mandatory wrapper sections absent; Highest Risk and Last Reviewed absent (third data point for the header-fields fix); whether the operational prompt template family falls in class 11 was then unresolved | CAMPAIGN_AUDIT_30 §Findings F1 | Closed-by-ruling (sections) / Standing-open (anchors) | Sections: class-6 operational prompt template exemption (pre-existing; pass B check 1 read "operational template (exempt class 6)"). Navigation Anchors block: still owed under the Routing backlink MUST — the one mechanical rule violation of pass A remains queued for the delegated batch | |
| A-F2 | F2 | WARNING | Step 2 evidence-label block diverges from the source (four labels vs five) | AP §Mission Drift Review prescribes the five-label Evidence Classification (Measured/Replicated/Simulated/Analogous/Placeholder); the template's Step 2 gives four with reworded definitions — a cold-start thread following it verbatim logs non-canonical ratings | CAMPAIGN_AUDIT_30 §Findings F2 | Standing-open | Routed to the Auditor_Protocols audit (LAST), which holds the Rule 5 verdict — third data point for the evidence-label-vocabulary family; not re-derived at fold-in | |
| A-F3 | F3 | WARNING | Mission Drift Review never executed while both trigger conditions have fired (X8, cross-file operational) | Calendar backstop elapsed ~2026-09-24 (60 days from the 2026-07-26 adoption; no Invocation Record exists); ratification velocity trivially exceeded; the running ratification count not visibly maintained | CAMPAIGN_AUDIT_30 §Findings F3 | Standing-open | Remedy is operational, not textual — execute Cycle 1 in a brand-new thread via this template and log the Invocation Record; a human operational decision, queued at issuance (also whether the missed-backstop lapse gets an unknown registration) | |
| A-F4 | F4 | NOTE | bare IDs, all tier-2 resolving | Bare "AP-030" ×2 in the Resolution Log and "AP-017" once in the 2026-08-02 entry — both resolve in the live index | CAMPAIGN_AUDIT_30 §Findings F4 | Positive-record | Cleanest citation posture of the small-file batch at pass A; the X3 retrofit pass qualifies this class mechanically when it reaches the file (deferred AP citations sit in frozen history or adjacency-qualified cells per pass B check 6) | |
| A-F5 | F5 | NOTE | Derived-from version pin stale (AP v0.31 vs live v0.45) | A plain version delta with content-based check performed instead — the 2026-08-02 pass updated the pin explicitly and logged why (correct for its era) | CAMPAIGN_AUDIT_30 §Findings F5 | Closed-by-ruling | PKC-022 (2026-10-27, option B) — pins retired, stale pins ruled non-drift; the required content-based check was performed at pass A | |
| A-F6 | F6 | NOTE | git-history discontinuity (bulk-upload mechanism) | File deleted (dec3f13f) and re-added (60469463) two minutes apart 2026-08-10 — the human's bulk re-upload practice; content continuity confirmed across the break | CAMPAIGN_AUDIT_30 §Findings F6 | Positive-record | Frozen-history-exempt class; recorded for provenance completeness only | |
| A-IN1 | checks 2, 3 | INCOMPLETE | cross-refs deferred | Charter Tier 1 full re-verification (rides the AP audit or next Charter touch); AP §Mission Drift Review full text (AP audited LAST); BATTERY_SEED/INTEGRITY_SWEEP_PROMPT exemption-family disposition (rode files 31–32) | CAMPAIGN_AUDIT_30 §INCOMPLETEs carried | Not re-tested | Owning audits pending | |
| B-N1 | NOTEs ×3 | NOTE | instrument changes properly recorded; contamination control verified; v1.4 defect fully repaired | The 2026-10-29 MAINT-15 canonical-input edits logged as "INSTRUMENT CHANGE" with old-set/new-set baseline split; Step 2 output cells blank in all eight cells (v1.4 fix holding); the v1.4 pre-filled-example defect caught by independent review before any Cycle 2 invocation | CAMPAIGN2_AUDIT_89 §Findings (three NOTEs) | Positive-record | All three favorable; "the cleanest instrument state on record… both late repairs verified against live text, not against the fixer's claims" | |
| B-C1 | (none) | NOTE | positive | Checks 1–11 otherwise clean: log chain 10-29 → 10-30 (v1.4) → 10-31 (step-4 logging-path repair to Admin/ALogs) matches the header Prior chain verbatim; the §3.2 relocation check PASSES on the very field the 10-31 repair fixed; Ethical Anchor exact | CAMPAIGN2_AUDIT_89 §Checks + Bottom line | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-29) reconciled the template against AP's live source section in full and found the file's substance sound: divergences (four-label block; wrapper gaps) and one cross-file operational lapse (MDR never executed with both triggers fired). It graded the Navigation Anchors absence as the only mechanical rule violation.
- Between the passes: the 2026-10-30 v1.4 repair (pre-filled example values removed) and the 2026-10-31 step-4 logging-path repair (MAINT-29 relocation) — both Custodian acts, both audited by pass B against live text rather than the fixer's claims.
- Pass B (10-31) found the instrument state the cleanest on record; its checks confirm the class-6 exemption reading that resolves A-F1's sections half. The three standing items are operational or routed: Navigation Anchors block owed (delegated batch); four-label divergence (AP audit LAST, with the Rule 5 verdict); MDR Cycle 1 execution (human). Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit; its backlink MUST is the standing anchor claim); `Admin/Auditor_Protocols.md` §Mission Drift Review (the source section; AP audited LAST); the AP-030 row in `Admin/Unknowns.md`; `Archive/Logs/Auditor_Protocols_Logs.md` (the Invocation Record's home, relocated to `Admin/ALogs/` per MAINT-29); dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

None. Corrections by dated addendum only.
