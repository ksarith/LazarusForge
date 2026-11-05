# EXTERNAL_REVIEW_2026-11-05_CLAUDE_MAINT-61_PACKAGE.md

**Provenance:** human-routed external review (Class A intake, External_Intake_Protocol v0.6 R4/R5); claimed identity **Claude (Anthropic)** — self-identified in the formal file below; unauthenticated. Evidence base declared by the reviewer: `LazarusForge-1.33.Alpha.zip` (Unknowns v5.77 — one version behind the live v5.78 at head `946dee90`); advisory only. Two-part relay: an informal summary (which closed with "Want these as a findings file to hand back?") followed by the formal findings file. Deposited verbatim 2026-11-05 at MAINT-62; no disposition, ruling or edit by this deposit. Claim verification results live in Intake Log entry 10 and `Archive/Proposals/ADDENDUM_2026-11-05_MAINT-61_DISPOSITION_RULING_SET.md`.

---

## Part 1 — informal summary (relayed verbatim)

I read the package against 1.33. The checks cover only the claims 1.33 can confirm; its Unknowns is v5.77, while the package was written against head `4bc29822` and v5.78. This is advisory only.

**Verified in 1.33**
- **§1:** both Convention 4 pointers still read `Archive/Logs/Auditor_Protocols_Logs.md`, a path that doesn't exist. Operational_Conventions' Last Audit predates the move.
- **§3 and §4:** NT-010 is the only NT row in the Unknowns index, and only AVE-R1 and AVE-R4 are indexed.
- **§5:** CIR-GOV-002 is absent from Unknowns.
- **§6:** Ethical_Constraints has zero FROZEN markers and an Exploration status. The Charter's marker is dated 2026-09-03.
- **§8:** the sweep prompt says it executes once, at campaign end, and the file is at v1.0.6.
- **§10:** the Cycle 1 table matches (P-1 Insufficient Evidence, P-3 Weakened, the other six Aligned; dated 2026-10-29). I didn't find "two raters" in what I read.

**Concerns, most important first**
1. **§9 may rest on a stale premise.** It says the sweep prompt "held promotion." In 1.33 its Status is already "Active — Operational Template," promoted 2026-10-29 on a human ruling. If so, the sweep missed a third stale label, and the ruling should be only about the config-source confirmation.
2. **§8's recommended option (a) closes a duty by redefinition.** The same seat that ran the 10-30 sweep recommends that it satisfied "campaign end." But the audit streams kept producing afterward (CAMPAIGN3 deposits are in 1.33), and so did stale-index findings. Options (b) or (c) deserve equal weight.
3. **§11's annotation would create an exception to the Highest Risk rule.** The Integrity_Incident_Log shows Open Unknowns 0 and Highest Risk Medium, and the proposed text bases the Medium on an open incident. The Highest Risk convention counts open unknowns, so the real ruling is whether incidents count toward it.
4. **§5's "closes the class" is overstated.** I found 45 resolved sidecar entries, 18 of them absent from Unknowns entirely. Only about 7 look like same-day pairs (FL-008/010/011/012, EP-005, SP-001, VG-002, by a date heuristic). The other 11 are not covered by the exemption.
5. **§2 doesn't say how large the pass is.** The Governance_Migration_Protocol alone mentions GOV-008 54 times. The package should list the instances to change, by file and form, before you authorize it.
6. **§10's P-1 "superseded-by-input-repair" is untested.** No Cycle 2 has run to show the MAINT-15 repair worked. "Carried pending Cycle 2" is safer.
7. **§6 option (a) has a tension.** FROZEN markers on a file whose status is Exploration would put it under a formal amendment cycle while declared exploratory. The package notes the link to A-F3.
8. **I couldn't reproduce one §12 item.** The quoted wording for RIP A-N1 ("Archive directory to be added here when established") isn't in the 1.33 Discovery.md, which has an Archive tree entry. It may have been reworded or fixed since.

**Process:** the package's severable structure is sound. The same Vibe line drafted it, ran the sweep and recommends the dispositions, which it discloses.

Want these as a findings file to hand back?

---

## Part 2 — formal findings file (relayed verbatim)

# EXTERNAL REVIEW — Skeptic read of PROPOSAL_2026-11-05_STANDING_DEBT_DISPOSITION_PACKAGE

**Reviewer:** Claude (Anthropic) — claimed, unauthenticated, human-routed. Advisory, findings-only. No disposition, ruling, or edit is made or recommended as binding by this file.
**Date:** 2026-11-05
**Subject:** `Archive/Proposals/PROPOSAL_2026-11-05_STANDING_DEBT_DISPOSITION_PACKAGE.md` (MAINT-61), text as relayed by the human.
**Evidence base:** `LazarusForge-1.33.Alpha.zip` (md5 `e1722d6cdb4f8048534af2998b9ec6f8`, byte-identical to the copy in VibesSandbox `Maintenance/`), plus the MAINT_LOG through MAINT-61 and the package text itself.

## Limits of this review

- The package was written against LazarusForge head `4bc29822` (Unknowns v5.78). 1.33 carries Unknowns v5.77. Any claim that depends on post-1.33 state is unverified here and is marked as such.
- The 23 tranche-2 aggregates, the coverage ledger, and the aggregates' §2 ledgers are not in the evidence base. Package claims that cite them (the 8-open / 2-stale split, every "aggregate B-N2"-style label) were not checked.
- Counts below are produced by scripted text matching on 1.33 and are heuristic where stated.
- The reviewer is not independent of the project's multi-agent workflow in the sense of GOV-008; no seat is claimed.

## Verified against 1.33 (no finding)

| Package § | Claim | Result |
|---|---|---|
| §1 | Both Convention 4 pointers in `Admin/Operational_Conventions.md` read `Archive/Logs/Auditor_Protocols_Logs.md` | True; that path does not exist in 1.33. The live file is `Admin/ALogs/Auditor_Protocols_Logs.md`. OC's Last Audit (2026-10-29) predates the move. |
| §3 | NT-010 is the only NT row in the Unknowns index | True (one `\| NT-0` row). |
| §4 | Only AVE-R1 and AVE-R4 are indexed | True. |
| §5 | CIR-GOV-002 absent from Unknowns | True at v5.77 (zero occurrences). |
| §6 | Ethical_Constraints carries no FROZEN markers; Charter's carry a 2026-09-03 marker; EC status is Exploration | True (`Admin/Ethical_Constraints.md`: 0 FROZEN, Status Exploration; Charter marker dated 2026-09-03). |
| §8 | Sweep prompt commissioned to execute once, at campaign end, corpus-wide; v1.0.6 | True. |
| §10 | MDR Cycle 1 ratings and date | True per `Admin/PROBE_INVOCATION.md` History Appendix: P-1 Insufficient Evidence, P-3 Weakened, P-2/P-4/Q-1–Q-4 Aligned; Cycle 1 dated 2026-10-29. "Two raters" not found in the text read; unverified. |

## Findings

Severity labels are the reviewer's, not the repo's grade vocabulary.

### F1 — §9 may rest on a stale premise (Medium)

§9 states the Integrity Sweep Prompt "held promotion pending confirmation" of the automation source. In 1.33, `Admin/INTEGRITY_SWEEP_PROMPT.md` already reads Status "Active — Operational Template", promoted 2026-10-29 on a human ruling (AUDIT_31 F2), version 1.0.5 → 1.0.6. If aggregate finding A-F2 is the same condition, §9's premise is stale and the sweep's "2 of 10 labels stale" undercounts. If A-F2 is a distinct condition (config-source confirmation only), §9's text should say the promotion is already enacted and limit the ruling to the config source. Either way the ruling text should be reconciled with the file header before adjudication.

### F2 — §8 recommended option (a) closes a duty by redefinition (Medium)

The package recommends reading "campaign end" as already satisfied by the 2026-10-30 run. The recommendation comes from the seat that executed that run. Evidence the campaign streams continued afterward: CAMPAIGN3 deposits (`Admin/AAudits` CAMPAIGN3_AUDIT_01/04; `Archive/Audits/ADVERSARIAL_CHALLENGE_BATTERY_2026-11-03_CAMPAIGN3_DEPOSITS.md`) are in 1.33, and the 2026-11-03 fix pass (AUDIT_81/83) found stale-index defects (X10, FAK-009) that a later corpus-wide run would be positioned to catch. Options (b) and (c) merit equal presentation to the human.

### F3 — §11's B-N3 annotation would create an exception to the Highest Risk rule (Medium)

`Admin/Integrity_Incident_Log.md` File State shows Open Unknowns 0 and Highest Risk Medium. The proposed annotation bases Medium on "one open Minor-escalated incident." Elsewhere in the corpus Highest Risk is derived from open unknowns, and zero open is recorded as Low (see the v5.77 Verification_Gates fix). Annotating records the exception without deciding it. The underlying ruling is whether open incidents count toward Highest Risk; the annotation should follow that ruling, not precede it.

### F4 — §5's "closes the class" is overstated (Low–Medium)

Scripted scan of non-archive sidecars in 1.33: 45 entries with Resolved/Closed status; 18 are absent from `Unknowns.md` entirely; about 7 of those carry a single date throughout, consistent with same-day open-and-close (heuristic): FL-008, FL-010, FL-011, FL-012 (`Architecture/Forge_flow.md`), EP-005 (`Admin/Engineer_Protocols.md`), SP-001 (`Admin/Safety_Protocols.md`), VG-002 (`Admin/Verification_Gates.md`). That supports the package's "several same-day pairs already unindexed." But roughly 11 other resolved entries are also unindexed and would not be covered by a same-day exemption. The ruling either needs to be broadened to the whole class or described as covering only same-day pairs.

### F5 — §2 does not bound the pass (Medium)

The package authorizes "a single mechanical pass" over four files without listing instances. Raw pattern-match line counts in 1.33 (these include qualified and same-file citations; bare-vs-qualified was not separable by script): `Governance_Migration_Protocol.md` 54 lines mentioning GOV-008; `Repository_Integrity_Protocol.md` 10 (GOV-006/GOV-013/SEC-007b); `Integrity_Incident_Log.md` 6 (RIP-007/PKC-015); `Experiments.md` 1 (CF-001/EN-001/CE-003). The ruling should rest on an enumerated list (file, location, current form, proposed form) and a stated rule for what counts as "bare," so the authorization is checkable after the fact.

### F6 — §10's P-1 "superseded-by-input-repair" is untested (Low–Medium)

The proposal reads Cycle 1's P-1 Insufficient Evidence as superseded because MAINT-15 repaired the input side. No Cycle 2 has run (the History Appendix Cycle 2 column is blank). A disposition of "carried pending Cycle 2" records the same intent without asserting the repair worked.

### F7 — §6 option (a) has an internal tension (Low)

FROZEN markers (as in the Charter) require a full amendment cycle plus human ratification to edit. Applying them to a file whose Status is Exploration freezes content the file declares exploratory. The package notes the interaction with A-F3; the dependency is stronger than "pairs naturally": option (a) arguably presupposes A-F3 is resolved first.

### F8 — One §12 item not reproduced (Low)

RIP A-N1 quotes Discovery as saying "Archive directory to be added here when established." That phrase is not present in the 1.33 `Discovery.md`, which carries an Archive tree entry (around lines 331–332). It may be reworded or already repaired after 1.33; it should be re-checked at live head before it stays on the parked list.

## Process notes

- The severable-section structure and per-section ruling text are sound and make partial ratification straightforward.
- Disclosed non-independence (same line drafted, swept, and recommends) applies to F1, F2, F6: the findings most affected are the ones where a recommendation closes or reclassifies the seat's own earlier work.
- §0's convention (session addenda carry pointers only) depends on the coverage ledger and aggregates' §2 ledgers staying current; MAINT-60 finding 6 (ledger drift by design) applies.

## Non-claims

This file verifies nothing beyond the listed checks, grades no finding in the repo's vocabulary, advances no status, and fills no Verified-by cell. Corrections by dated addendum only.

---

*Deposited at MAINT-62 (2026-11-05). Corrections to this deposit by dated addendum only.*
