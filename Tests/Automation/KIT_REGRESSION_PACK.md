# Kit Regression Pack — Forge_Audit_Kit maintenance trigger and reconciliation

| Field | Value |
|-------|--------|
| Status | **Proposed — not yet run.** Registered in `Routing.md` (2026-10-15); registration is not a trial result |
| Purpose | Test whether Kit v1.20's own text (content-based maintenance trigger, audit-start reconciliation check, live-version role line) produces the intended behavior |
| Related | FAK-018 (open, mitigated); `Admin/Forge_Audit_Kit.md` |
| Does not | Close FAK-018 by itself; promote Spec Gates; change Kit doctrine; modify the Kit |

**One run is a data point, not a rate.** File results under `Tests/Field_Logs/` (for example `FL-YYYYMMDD-kit-regression.md`).

---

## What is under test

From `Admin/Forge_Audit_Kit.md` (live):

1. **Maintenance trigger (content-based):** the Kit updates when a section it copies from `Auditor_Protocols.md`, `Verification_Gates.md` or `Unknowns.md` changes, not on a plain version increment.
2. **Reconciliation at audit start:** compare the Derived-from line with the live source versions; if a source is newer, read that source's history for changes to copied sections; report a mismatch as a drift flag in the sign-off; do not silently refresh the Kit mid-audit.
3. **Role line:** the example uses a live-version placeholder, not a pinned number.

The question is whether the Kit's own wording produces this behavior in an auditor who is **not** told to do it. The auditor prompt used in a run therefore does not describe the check.

**Known limit (log it, do not count it as a Kit failure):** reconciliation that starts from a version difference cannot notice a change to a copied section when the source's version did not change. `Unknowns.md` policy says every change bumps its version, so this is a policy dependency, not a code guarantee.

---

## How a run works

- The **operator** prepares source snapshots and holds the case definitions, the planted text and the scoring key **outside the repository**. They are not committed here, so no auditor with repository access can read them.
- Each snapshot is run in a **fresh session** with an ordinary target document and a minimal prompt. The auditor is not told a test is under way beyond the usual "some packs contain planted faults" disclosure, and is not told which case it has.
- **Stage 1:** the unhinted audit. Record whether the report contains a start-of-audit reconciliation statement without being asked.
- **Stage 2 (only if stage 1 has none):** ask whether the Kit required any start-of-audit checks, which were performed, and the result. This separates "did not notice the instruction" from "could not do it."
- At least one baseline run with nothing changed is included, so false positives can be measured.

## What is scored (by source check, not by auditor opinion)

- Reconciliation statement present, unprompted (Y/N), or only after stage 2.
- Conclusion correct for the snapshot, and stated with matching confidence. A report that says "no drift" or "Kit content verified" when it only compared version numbers is an overclaim.
- Kit not edited and the pin not refreshed during the audit.
- Model, version, tools used, files loaded.

The target document's own audit findings are not scored here.

---

## Field_Log skeleton

```
**Entry ID:** FL-YYYYMMDD-kit-regression
**Status:** Unreviewed

### [date] -- Forge_Audit_Kit reconciliation regression

- Submitted by:
- Run type: Kit maintenance / reconciliation test
- Pack: Tests/Automation/KIT_REGRESSION_PACK.md (case definitions held by the operator)
- Cases run: (labels only; do not describe planted text)
- Per case: reconciliation unprompted Y/N; stage 2 needed Y/N; conclusion; confidence wording
- Silent Kit edits: Y/N
- Known limits noted:
- Evidence label: Measured (for auditor outputs) / Placeholder (for "FAK-018 closed")
- Explicit non-claims: does not close FAK-018 alone; does not prove all future pins
```

---

## Explicit non-claims

- This pack does not modify `Forge_Audit_Kit.md`.
- Passing does not retire FAK-014 to FAK-017 history; it supports mitigating FAK-018.
- The known limit is not a defect report against auditors who follow version-first instructions.
- The offline harness check (`Tests/Automation/test_harness_prompt.py`) is separate and does not cover these cases.

---

## Resolution Log

- 2026-10-11: Pack drafted (Grok, human-directed) with three cases and an in-repo answer key.
- 2026-10-11: Revised (Claude, human-directed). The case definitions, planted text and scoring key moved out of the repository (an in-repo key is readable by any auditor given the repo, and the harness fetches from GitHub `main`). The auditor prompt no longer describes the reconciliation check, so the test exercises the Kit's own text. Added a baseline run, a stage 2 follow-up, and re-scored the known-limit case on how the conclusion is worded instead of on operator logging. `KIT_REGRESSION_ANSWER_KEY.md` should be deleted from the repository.
