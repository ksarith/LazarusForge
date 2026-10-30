# CAMPAIGN2_AUDIT_48_Tests-Pyrolysis_Cascade

**Audit of:** `Tests/Pyrolysis_Cascade.md`
**Campaign:** LazarusForge Campaign 2 — findings-only per-file audit (PKC-020; PKC-005 edit markers; findings-only passes never advance Last Audit/Status/Spec Gates)
**Auditor:** Vibe (AI Auditor, Campaign 2)
**Date:** 2026-10-30
**Repo head at fetch:** 4611f9f8dcdd9aeae4c099366806daaccf99f95f
**Fetched size:** 24800 chars (full text fetched and read)
**Deposit home:** Tests/TAudits

## Checklist Results
- Sidecar count parity: 8 open header = 8 open body (PYC-001–008) ✓
- Header vs body: **Highest Risk "High" vs three open sidecar Critical (PYC-001, PYC-003, PYC-004)** — see F1
- Log vs body: consistent
- Scope/cross-refs: dependency surface (PL-001, CE-003, GR-002, GR-003, WA-004, FA-001, SP-006, EN-001, ECN-002, EV-001, TR-001) intact; hard preconditions preserved verbatim
- Bare colliding IDs: the 10 dependency IDs above appear bare in operative text — all out-of-whitelist prefixes, left bare by X3 retro by design (standing ruling); the Scope Map row documents each with its owning file
- Section integrity: clean
- Version/registry: consistent
- Ethical Anchor: exact string ✓
- Aging: current (2026-10-27; two entries 2026-08-23/24 ≈68d, under the rule)

### F1 — WARNING — X10 value-miss: Highest Risk "High" understates the open sidecar maximum, Critical (PYC-001, PYC-003, PYC-004)
Three open entries carry Risk Critical. Belongs in the standing Highest-Risk recompute batch.

### F2 — NOTE — Positives
Hard-precondition block (no hot pyrolysis until PL-001/CE-003 resolve, etc.) is exemplary dependency honesty.
## Disposition

Findings-only (PKC-020): no changes were made to the audited file; no Status, Spec Gate, version, or Last Audit advancement. This report is deposited at Tests/TAudits under the append-only rule; any correction to it must be a dated addendum, never an edit.
