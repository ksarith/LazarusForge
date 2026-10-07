# Things We Got Wrong

**Purpose:** A short, public, evidence-based record of real mistakes, corrections, and lessons so the project does not quietly rewrite its own history or learn the wrong lesson from partial successes.

This is not a performance of humility. It is part of the same salvage discipline applied to claims: nothing is discarded without accounting.

Entries are added only when something concrete was wrong, was caught, and produced a usable correction. Placeholder or speculative items do not belong here.

---

## Navigation Anchors
* **Context Core:** [Discovery.md](Discovery.md)
* **Network Routing:** [Routing.md](Routing.md)
* **Related:** [Tests/Field_Logs.md](Tests/Field_Logs.md), [Admin/Integrity_Incident_Log.md](Admin/Integrity_Incident_Log.md)

---

## File State

| Field            | Value                                      |
|------------------|--------------------------------------------|
| Status           | Active                                     |
| Body Stability   | Living (append-only preferred)             |
| Last updated     | 2026-10-07                                 |
| Seed source      | CAP-meta-stale runs, AVE sample, POC corrections |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## 1. Stale metadata that looked current (2026-10-06)

**What happened**  
`Routing.md` carried a header line “Last updated: 2026-09-30” while its Master Routing Map body already listed newer files (`Tests/Field_Logs/*`, `Admin_Governance_Teardown_POC.md`, CAP run cards). The header had lagged behind the body.

**How it was caught**  
The first CAP-meta-stale-01 run found the lag in the wild: the header said 2026-09-30 while the map body already listed later files. It was corrected the same day (2026-10-06). The Reduced-config run later re-injected the stale header as a seed fault to test whether detection still worked with some documents withheld.

**What we learned**  
A “Last updated” line is only as trustworthy as the discipline that keeps it current. Header lag is a real, recurring class of error. Relying on a single metadata field without cross-checking the body or the filesystem is fragile.

**Evidence**  
- `Tests/Field_Logs/FL-20261006-cap-meta-stale-01.md`  
- `Tests/Field_Logs/FL-20261006-cap-meta-stale-01-reduced.md`  
- `Tests/Field_Logs/RUN_CARD-CAP-meta-stale-01.md`  
- The 2026-10-06 header catch-up, preserved as a "Prior" entry in the `Routing.md` Last-updated line

---

## 2. Incorrect size / count totals that looked authoritative (2026-10-04)

**What happened**  
`Tests/Admin_Governance_Teardown_POC.md` originally stated Tier 1 = 7 files / 245 KB and Tier 2 = 14 files / 653 KB. Recalculation against the actual classification table produced different numbers (Tier 1 = 6 / 330 KB; Tier 2 = 15 / 667 KB). The original figures were wrong.

**How it was caught**  
The totals were recomputed from the classification table on 2026-10-04 and corrected the same day. The error had also propagated into `Adm_Scope_Map.md`, which was fixed too. Two days later, AVE-20261006-013 and -014 recorded the original statements as historical fails.

**What we learned**  
Even internal summary tables can contain arithmetic or classification errors. Treating a “Totals” line as authoritative without recomputing it from the underlying rows is a source of silent drift.

**Evidence**  
- Provenance line and dated correction notes in `Tests/Admin_Governance_Teardown_POC.md`  
- `Tests/Field_Logs/FL-20261006-ave-sample-01.md` (items 013–014, recorded as historical fails)

---

## 3. Scoring design that invited the wrong reading (2026-10-06)

**What happened**  
The CAP-meta-stale-01 Reduced-config run reported an “8/8” result. Under the original framing this figure mixed operational stages with an ablation assessment and invited the misreading “Reduced beat Full.” The card was corrected the same day to separate a 7/7 operational grade from a Pass/Fail ablation assessment.

**How it was caught**  
A dated reviewer note (2026-10-06) on the Reduced-config field log. The log does not name the reviewer. The headline was left unchanged as historical record, with the note explaining the correct reading.

**What we learned**  
A single aggregate number can hide important distinctions. Metric design is itself a claim that needs scrutiny; an /N figure that collapses different kinds of judgment is easy to misread later.

**Evidence**  
- Reviewer note at the top of `Tests/Field_Logs/FL-20261006-cap-meta-stale-01-reduced.md`  
- Stage 8 / ablation rule in `Tests/Field_Logs/RUN_CARD-CAP-meta-stale-01.md`

---

## 4. Scope / inventory statements that went stale (2026-10-06)

**What happened**  
`Tests/Tst_Scope_Map.md` said the Field Logs intake was still empty. That was accurate when written (2026-08-08) and still accurate on 2026-09-18. It became obsolete once entries were filed (the GOV-021c pilot and the CAP-meta-stale runs), but the statement kept reading as current until it was corrected on 2026-10-06. It was never an original error. It is a statement that stayed in place after the world moved, the same pattern as item 1.

**What we learned**  
Inventory and scope claims require the same evidence discipline as any other claim. “Still empty” or “last updated X” must be checked against the filesystem or the body, not trusted by inertia.

**Evidence**  
- Finding 4 and the dated correction notes in `Tests/Tst_Scope_Map.md`  
- AVE-20261006-007 in `Tests/Field_Logs/FL-20261006-ave-sample-01.md`

---

## How new entries are added

1. Something concrete was wrong (a number, a status, a claim of independence, a metric design, a metadata field).
2. It was caught and corrected (or deliberately left visible as a historical record).
3. The correction produced a usable lesson.
4. The entry cites the Field Log, run card, or other primary evidence.
5. Prefer append-only. Do not rewrite earlier entries to make the project look better in hindsight.

If an entry later turns out itself to be incomplete or wrong, add a dated note rather than silently editing the original.

---

## Corrections to this file

- 2026-10-07: Verified each entry against the cited Field Logs after first filing. Four "how it was caught" details were corrected: item 1 (the first CAP run found the lag in the wild; only the Reduced run re-injected it), item 2 (caught by recomputation on 2026-10-04; the AVE rows recorded it later), item 3 (reviewer note, reviewer not named), and item 4 (reframed as staleness, not an original error; evidence cited precisely).

---

## Explicit non-claims

- This file is not a complete history of every mistake.
- Presence on this list does not imply the underlying problem is fully solved.
- Absence from this list does not imply perfection.
- This is not marketing. It is part of the epistemic record.
