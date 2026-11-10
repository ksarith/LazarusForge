# CAMPAIGN4_AUDIT_12 — Admin/Forge_Audit_Kit.md

**Campaign:** Campaign 4 adversarial sweep of `Admin/` (34 files), artifact 12 of 34.
**Auditor:** Vibe (Repo Custodian line). **Date:** 2026-11-10.
**Base commit:** `94f57c8c1a8cbfdd7a487f53b56f97a2f0f0d933` (LF main at compose).
**File:** `Admin/Forge_Audit_Kit.md` (the Kit), 47,525 chars, 440 lines, fetched complete at the base commit. SHA-256 of the file as found: `0cd1730a76340c05cdba2c0591f06a5b57b72130ddbc9ee77deb2bb87ad4f188`.
**Method:** full-text read plus live-source verification of the Kit’s own cross-references, its sidecar home (`Admin/ALogs/Forge_Audit_Kit_Changelog.md`, 61,847 chars, fetched full), the Unknowns index, the Intake Log, the archived proposal, and the source files the Kit condenses.
**Findings-only per PKC-020:** this pass does not advance Last Audit, Last Reviewed, version, Status, Spec Gates, or unknown states, and does not modify the audited file. Conversion to audits of record is the human’s alone (MAINT-26 / AP-032).

---

## File State as found

| Field | Value as found |
|---|---|
| Status | Draft |
| Spec Gates | 0/6 — hold dissolved by human ruling 2026-10-29 (PKC-022 option-B precedent); gates advance only by fresh audit + human ratification, no self-approval |
| Verification Ref | Admin/Verification_Gates.md |
| Last Audit | 2026-11-04 (v1.31 → v1.32, Rule 12 Aggregate Finding-Line Schema, MAINT-57; non-independence disclosed) — 6 days before this pass |
| Open Unknowns | 4 (FAK-001, FAK-006, FAK-009, plus the Cycle/CURRENT_CYCLE Battery finding flagged for Canonical_Terms) |
| Sidecar Link | Admin/ALogs/Forge_Audit_Kit_Changelog.md#sidecar--auditor-notes--unknowns (correct post-relocation home; the 2026-10-31 MAINT-29 repair verified applied) |
| Ethical Anchor | canonical, exact |

Note: the File State table still carries Last Audit and Auditor rows (retired field class per MAINT-56, 2026-11-04); migration is at next substantive touch per the recorded convention — not a finding.

---

## Findings

### F-FAK-1 — WARNING — Stale mirrored claim in the Kit’s own sidecar (candidate new pattern, first instance)

The Kit’s sidecar entry FAK-009 still reads: “Status: Open (VG-001 itself remains unresolved in `Admin/Verification_Gates.md`; the kit’s citation is corrected)”. VG-001 has been Resolved — Discharge via Lessons Learned since 2026-07-03; `Admin/Verification_Gates.md` recounts zero open unknowns. The Unknowns index’s FAK-009 row was corrected 2026-11-03 (MAINT-54 / CAMPAIGN2_AUDIT_83 F1) — the repair reached the mirror but not the owning sidecar. The Kit’s subsequent v1.31 (2026-11-02) and v1.32 (2026-11-04) passes post-date the resolution by months and did not touch the entry. Distinct from Pattern 2 (wrong home) and Pattern 3 (stale condition): a repair was propagated to the mirror while the owning record stayed stale. One instance — recorded as a candidate; Xn registration requires two.

**Suggested remedy (human queue):** update FAK-009’s Status parenthetical in the changelog sidecar to record VG-001’s 2026-07-03 resolution.

### F-FAK-2 — WARNING — RIP-011 anchor fields absent from the Kit’s Resolution Log home

The Kit’s RL lives in its changelog (in-body RL says “add new entries there, not here”). Grep of `rl_entry_count_after` across the changelog (61,847 chars): 0 occurrences. The substantive post-ratification entries — v1.31 (2026-11-02, EIP- row registration) and v1.32 (2026-11-04, Rule 12 added) — carry no anchor fields and no logged exemption. Same class as F-GMP-2 and F-ADP-2; folds into the queued human item (anchor-fields retrofit-or-exemption).

### F-FAK-3 — WARNING — Aging Rule not computable: the sidecar home carries zero Last Reviewed fields

Grep of “Last Reviewed” across the changelog: 0 occurrences. None of the Kit’s open unknowns (FAK-001, FAK-006, FAK-009, the CT-flagged item) carries a Last Reviewed date, so the 90-day Aging Rule cannot be evaluated for any of them — and the Kit’s own Audit Opening Checklist step 3 (Expiry Watch) instructs computing aging “directly from the target file’s own sidecar entries,” which is impossible for the Kit itself. The instrument that codifies the Expiry Watch procedure cannot run it on its own unknowns as the data stands. Derivation limit disclosed; no aging instance is claimed for this file (the campaign’s Aging tally is unchanged). The Kit is not counted as a control case — the rule does not fire, but not because the entries are young.

### F-FAK-4 — WARNING — FAK-005’s Resolved row remains in Unknowns’ Active Index

Unknowns’ Active Unknowns Index still carries the FAK-005 row, annotated in place: “Resolved — ceiling retired as a drift trigger by human ruling 2026-10-29 (Kit v1.27; PKC-022 dissolve-not-refresh; closure note in the changelog §Sidecar)”. Unknowns’ own Size Management Rule 2: “Resolved entries leave the Active Index immediately… Active tables show Open, In Progress, and Reopened only.” The Kit’s own Resolved Unknown Discharge Procedure step 6 says the same (remove from the active index; add one line to Expiry Watch or the Audit Trail). The closure itself is real and honestly annotated — the row’s presence in the Active table is the defect. The v5.75 header recorded the count change but kept the row.

**Suggested remedy (human queue):** remove the FAK-005 row from the Active Index and add the step-6 pointer line (Expiry Watch or Audit Trail) back to the changelog sidecar’s closure note.

### F-FAK-5 — WARNING — The Kit’s own maintenance trigger fired; drift indicator 2 in firing state

The Kit’s maintenance trigger: update when a source changes a section this kit condenses — explicitly including `Admin/Verification_Gates.md` (gate definitions). VG went v0.7 → v0.8 on 2026-11-02 (ratified batch A2, recorded in AP v0.46’s entry): the Gate 2 Not-Applicable definition was added to VG’s gate definitions. The Kit’s condensed Verification Gates section (updated last at v1.32, 2026-11-04 — after the VG change — but only for Rule 12) carries no trace of the N/A definition, and the Derived-from reconciliation date still reads 2026-10-27. The Kit’s own drift indicator 2 (“a source this kit condenses or copies has changed a listed section since the Derived-from reconciliation date, and the kit was not updated”) is in a firing state with solid derivation — unlike GMP’s cycle-unit case (F-GMP-6), no derivation limit applies. Compound Drift Rule: exactly one indicator firing → not fired. AP v0.47’s changes (sidecar RL write, AP-036 recompute-on-log) touch no condensed section; EF text, role declaration, and sign-off format are unchanged in v0.46/v0.47 — the firing is specific to the VG Gate 2 N/A definition.

**Suggested remedy (human queue):** a Kit pass adding the Gate 2 N/A definition to the condensed gate section and advancing the Derived-from reconciliation date (a body-changing pass — human ratification per the Kit’s own rules).

### F-FAK-6 — NOTE — File State template conformance gaps

File_Template §2’s File State block includes Body Stability, Active Disputes, and Highest Risk rows; the Kit’s File State carries none of the three (it carries retired-field Last Audit/Auditor rows instead). Fields are absent, not wrong; no sidecar Risk or Priority exists to mirror (the Unknowns cluster note records “the sidecar carries no Priority classification and none is invented here”). The Kit’s documented sidecar-relocation exception (v1.11) covers where entries live, not these rows.

### F-FAK-7 — NOTE — In-body Resolution Log summary one version behind

The Kit’s in-body RL block reads “Most recent: v1.31 (2026-11-02)” while the header, File State, and the authoritative changelog are at v1.32 (2026-11-04). Stale summary line only; the changelog’s v1.32 entry is present and newest-first order holds (the v1.32 pass’s disclosed mechanical repair verified).

### F-FAK-8 — NOTE — The Cycle/CURRENT_CYCLE governance flag: open 119 days, still without its CT entry

The Kit’s fourth open unknown (Adversarial Battery record, 2026-07-14) found `AUDIT_HARNESS.py` line 368 `CURRENT_CYCLE = 10` incremented per session while `EXPIRY_THRESHOLD = 2` makes the harness flag unknowns overdue after roughly two to four weeks of session-based aging — not the calendar-year Cycle CT ratifies. The finding explicitly routes itself to a new `Admin/Canonical_Terms.md` entry per CT-011’s “log a new entry rather than reopening this one” instruction. CT’s body still contains no CURRENT_CYCLE/CURRENT_SESSION/EXPIRY_THRESHOLD text; the flag is disclosed in Unknowns’ FAK cluster note (no invented ID, CT-011 scope) but remains a governance call unactioned for ~119 days. The divergence also touches this sweep’s own Expiry Watch step (harness pre-computation would use the session-based arithmetic). Disclosure, not a new grading event — the finding’s own text already routes it correctly.

---

## Clean verification (fabrication probes — all passed against live source)

1. **Intake Log entry 7 exact:** the Intake Log (`Admin/ALogs/External_Intake_Protocol_Logs.md`, 46,373 chars) records the 2026-11-04 Claude reconcile-pass/disposition-ledger design as row 7 of 21 (Class A, human-routed, claimed identity unauthenticated), with the verification record and the “Let’s ratify” partial-ratification disposition. The campaign’s “next: entry 22” arithmetic (21 rows) is consistent.
2. **Proposal archive byte-present:** `Archive/Proposals/PROPOSAL_2026-11-04_RECONCILE_PASS_DISPOSITION_LEDGER.md` (4,768 chars) with the archival header, the PARTIALLY RATIFIED outcome matching Kit Rule 12’s scope, and the preregistered disposition-ledger conditions — including the recorded “78 unparsed rows” provenance debt.
3. **Changelog integrity:** the v1.32 entry is present; newest-first order holds (v1.32 → v1.31 → v1.30 …); the v1.32 pass’s disclosed same-pass mechanical repair (v1.31 had been appended below v1.30) is consistent with the recorded state.
4. **All path targets resolve (14/14 existence checks):** every Governance Sidecar ID Reference owning file (including GH- → `Tests/Cognitive_Salvage_Layer.md`), every ASM- series file, and the Fallacy Checklist’s cross-refs (`Operations/Energy.md`, `Admin/Trajectories.md`, `Admin/Canonical_Terms.md`).
5. **Source anchors verified:** VG carries the m_phys ≥ 0.75 / m_rep ≥ 0.50 thresholds (VG-002’s content; VG-001 and VG-002 both Resolved, VG Open Unknowns 0); AP contains AP-021, AP-033, AP-035, EF-0.0–EF-0.8b anchors, and the L1/L2/L3 decay-trigger language; CT-011 exists and §4 defines the calendar-year Cycle; RIP-001’s “discharged 2026-06-27” matches the RIP sidecar (the 06-28 Unknowns variance is F-RIP-4’s recorded disclosure).
6. **X10 parity:** File State Open Unknowns 4 = sidecar 4 (FAK-001, FAK-006, FAK-009 open; FAK-005 closed with closure note; the CT-flagged item counted per the cluster note’s recorded convention) = Unknowns cluster note’s “fourth open item” counting — with F-FAK-4 recording the one row-presence violation. Active Disputes: empty table = “None open”.
7. **Kit-body history window complies** with the v1.27 recorded relocation cutoff (v1.20+ in body; v1.19 and older in the changelog) — the duplication drift indicator is dormant.
8. **Honest staleness marking:** the token-ceiling note’s figures (146,700 chars @ v0.41; 150,529 bytes @ v0.42) are explicitly dated measurements; live AP v0.47 is 159,639 chars — the note’s guidance is unaffected and its derivation limits are self-disclosed. The “roughly 40,000 characters at v1.26” trend metric (live: 47,525) is a reported trend, not a trigger (ceiling retired by ruling).
9. **Role declaration** uses the live-version placeholder; the gate-scope-vs-promotion-readiness note is present and correctly separates check coverage from promotion blocking.

---

## Out of scope (recorded, not findings against the Kit)

- The CURRENT_CYCLE rename/recalibration decision (F-FAK-8) is a harness governance call — the harness’s own audit is outside this sweep’s Admin/ scope except where a check names it.
- FAK-001/006’s substance (maintenance-trigger ownership; discharge-doctrine migration) is the human’s queue; this pass adds no disposition.
- The Kit’s MAINT-56 field migration (Last Audit/Auditor rows) occurs at next substantive touch per the recorded convention.

---

*Findings-only deposit per PKC-020. Composed 2026-11-10 at base commit `94f57c8c`. Auditor: Vibe (Repo Custodian line). No field of the audited file was advanced or modified by this pass.*