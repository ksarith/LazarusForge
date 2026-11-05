# CORRECTION — MAINT-54 / MAINT-55 maintenance-ID collisions

**Status:** Dated correction — commit history preserved verbatim; no renumbering.
**Filed:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep, cleanup phase; human-directed session)
**Non-independence:** Genesis Phase — the Custodian line issuing this correction is the same Vibe line that deposited the colliding commits; disclosed per MAINT-38 and Auditor_Protocols v0.47.
**Scope:** Discloses that maintenance-session IDs **MAINT-54** and **MAINT-55** were each spent twice in commit history. No commit is reworded, rebased, or renumbered. This file is the disambiguation record of record.

## 1. MAINT-54 — first spend and reuse

**First spend (the MAINT-54 of record):** commit `c1e86641`, 2026-11-03 01:13Z — "MAINT-54: Intake Log entry 6 — first post-landing intake (Claude review of the landed state, human-routed …)".

**Reuse (2026-11-03 19:05–19:12Z — eight commits, human-directed Repo Custodian fix pass over CAMPAIGN2_AUDIT_81 F1 / CAMPAIGN2_AUDIT_83 F1–F2):**

| # | Commit | Commit message head |
|---|---|---|
| 1 | `568b5907` | MAINT-54 fix pass (1/3): Engineer_Protocols X10 Highest Risk recompute High→Medium per CAMPAIGN2_AUDIT_81 F1 |
| 2 | `54761b65` | MAINT-54 fix pass (2/3): Verification_Gates X10 Highest Risk recompute High→Low per CAMPAIGN2_AUDIT_83 F2 |
| 3 | `62740060` | MAINT-54 fix pass (1b): punctuation normalization — terminal period before Prior chain link (Engineer_Protocols) |
| 4 | `65959bb6` | MAINT-54 fix pass (2b): punctuation normalization — terminal period before Prior chain link (Verification_Gates) |
| 5 | `ebb1698b` | MAINT-54 companion: Unknowns_Changelog v5.77 entry (FAK-009 index correction) |
| 6 | `817cfb48` | MAINT-54 fix pass (3/3): Unknowns.md FAK-009 index row corrected per CAMPAIGN2_AUDIT_83 F1 |
| 7 | `bf5fec32` | MAINT-54 registration pass: CAMPAIGN2 fix-pass commits recorded + 8 unregistered 2026-11-03 CAMPAIGN3 deposits |
| 8 | `501e325f` | MAINT-54 session record (Custodian; human-directed 2026-11-03): fix pass over CAMPAIGN2_AUDIT_81 F1 / _83 F1–F2 |

## 2. MAINT-55 — first spend and reuse

**First spend (stranded label):** commit `58213981`, 2026-11-03 01:19Z — "MAINT-55: External_Intake_Protocol.md v0.6 → v0.7 — post-landing review amendments, human-ratified".

**Reuse (2026-11-04 01:40–01:47Z — nine commits, external-review fix pass; the MAINT-55 of record per the fix-pass addenda and `CORRECTION_2026-11-03_AUDIT81_HEADATFETCH.md`):**

| # | Commit | Commit message head |
|---|---|---|
| 1 | `1c461496` | MAINT-55: Chemistry.md Highest Risk High→Critical (X10 recompute) |
| 2 | `e7fece4e` | MAINT-55: File_Template.md — Critical joins the Risk vocabulary |
| 3 | `4f97d3e4` | MAINT-55: Unknowns.md v5.78 — EN-005/CF-002/TF-002 index status cells sidecar-wins |
| 4 | `b70d26fc` | MAINT-55: Unknowns_Changelog v5.78 entry |
| 5 | `f22101c3` | MAINT-55: dated correction for AUDIT_81 Head-at-fetch blemish |
| 6 | `8f62718e` | MAINT-55: verbatim deposit of external Claude 1.33 Alpha release review |
| 7 | `d2462f8c` | MAINT-55: Rule 5 verification packets for the five standing aggregates (verifier: Claude, named) |
| 8 | `75927fdf` | MAINT-55: Routing registration — external-review fix pass |
| 9 | `654278e9` | MAINT-55: session-status addendum — external-review fix pass report |

**Compounding note:** the External_Intake_Protocol line continued coherently as MAINT-56 (`39498c51`, EIP v0.7→v0.8, 2026-11-04 12:10Z) — only the `58213981` label is stranded.

## 3. Downstream citation effects

- The 23 tranche-2 aggregates deposited under MAINT-58 cite the fix-pass enactment commits by sha with "(MAINT-54)" labels — e.g. Engineer_Protocols Highest Risk `568b5907`/`65959bb6`; Verification_Gates `54761b65`/`62740060` and FAK-009 `817cfb48`. Those shas belong to the 2026-11-03 19:05–19:12 reuse batch; **the sha is the disambiguator and those citations stand**.
- Where a bare "MAINT-54" / "MAINT-55" appears with no sha, read the **first spend** (Intake Log entry 6 / EIP v0.7 amendments) unless a dated addendum's context indicates the fix-pass batch.
- Nothing in `Routing.md`, the aggregates, or the audits is reworded by this correction; disambiguation is by this file plus sha citation going forward.

## 4. Requested human ruling

Ratify an ID-allocation rule: MAINT-NN IDs are allocated monotonically, one per distinct task batch, by checking the Intake Log and MAINT_LOG before assignment; spent IDs are never reused. This correction is filed under MAINT-58 and consumes no new ID.

## 5. Addenda

None. Corrections by dated addendum only.
