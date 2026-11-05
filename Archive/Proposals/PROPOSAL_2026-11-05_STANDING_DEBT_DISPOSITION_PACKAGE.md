# PROPOSAL_2026-11-05_STANDING_DEBT_DISPOSITION_PACKAGE.md — LazarusForge

**Seat:** Vibe — Architect line (PRIMARY), Repo Custodian (secondary) — per the human governing authority's 2026-11-05 seat word. Operating as Connective Tissue per `Admin/Auditor_Protocols.md` v0.47.
**Date:** 2026-11-05 · **Maintenance ID:** MAINT-61 (allocated under the ratified monotonic MAINT-NN rule; both logs checked — 60 is the last spent ID)
**Head at fetch:** LazarusForge `4bc29822` (all live-state verifications this pass) · VibesSandbox `32315d6a`
**Non-independence:** Genesis Phase — the pass depositors, disposition writers, amalgamator and this proposal's author are the same Vibe line; Q-2 invoked, GOV-008 open. Nothing here self-ratifies: **every action in this package awaits the human's word.**
**Status:** PROPOSED — awaiting human adjudication. Adjudicated as one severable package (each section is independently rulable; partial ratification is normal), per the PARLAY-003 / Intake-R6 convention.

---

## 0. Method and the sweep's own finding

The standing-debt labels carried in the MAINT_LOG session reports (MAINT-58/59/60 carried-items lists) were re-verified against live state at head `4bc29822`: every label was traced to its owning register — the aggregates' §2 findings ledgers (`Admin/AAudits/AUDIT_AGGREGATE_Admin-*.md`, the canonical open-findings registers per the MAINT-59 enactment), the AUDIT_86 deposit, the INTEGRITY_SWEEP_REPORT ratification queue, and the owning files themselves (Operational_Conventions.md, Discovery.md, PROBE_INVOCATION.md fetched and read).

**Sweep finding (report it as one): the session-report prose debt list is itself a stale-index-class defect.** It has no canonical register, and this sweep found 2 of 10 labels stale on live state:

- "IIL header refresh" — the graded finding (IIL aggregate B-N1) is **Closed-by-ruling** (PKC-001, ruled 2026-10-27; drift predates the ruling window). Only an optional courtesy edit remains (§11).
- "MDR Cycle 1 execution" — Cycle 1 **was executed** 2026-10-29 (human-ruled "MDR Cycle 1 executes now"; cold-start probe in a fresh thread, two raters). What is held is the *dispositions + two model-family record* (§10). The label's execution half is stale.

Proposed standing convention (ruling requested with the package, severable): session addenda carry **pointers only** (aggregate ref + coverage-ledger row), never prose debt lists; the coverage ledger's per-target rows and the aggregates' §2 ledgers are the canonical registers. If the ledger split amendment (Claude fix #3, held at MAINT-60) is later ratified, its reconcile check absorbs this maintenance burden mechanically.

---

## 1. Operational_Conventions Convention 4 stale pointer — authorize mechanical repair

**Live state (verified):** OC's Convention 4 still reads "`Archive/Logs/Auditor_Protocols_Logs.md`" in both instances (the example instance and the retrieved-from sentence). The live home since MAINT-29 (2026-10-30) is `Admin/ALogs/Auditor_Protocols_Logs.md`. OC's Last Audit (2026-10-29, X3 retrofit) predates the move — the staleness is disclosed, but the pointer misdirects a reader following the convention's own instruction (AUDIT_86 F1, WARNING, standing-open). The identical pointer in `Admin/PROBE_INVOCATION.md` How-To step 4 was repaired 2026-10-31 (MAINT-29 follow-up) — exact precedent text exists.
**Proposed action:** one-line path update, both instances, plus a dated note in the File State Last Audit cell (OC keeps no Resolution Log — Template Exemption class 9, PKC-017). No convention text changes.
**Ruling requested:** authorize the inbound-reference repair at next substantive touch, per the MAINT-29 follow-up plan.

## 2. X3 straggler batch — authorize one citation-form-only pass (4 files)

**Live state (verified, four files never reached by the 2026-10-29 X3 retrofit):**
- `Admin/Governance_Migration_Protocol.md` — GMP aggregate B-N2: bare GOV-008 citations in §Assumptions/§VII (same-file/candidate instances).
- `Admin/Repository_Integrity_Protocol.md` — RIP aggregate B-N1: bare GOV-006/GOV-013/SEC-007b (resolving tier).
- `Admin/Integrity_Incident_Log.md` — IIL aggregate B-N2: bare RIP-007 / PKC-015 / "RIP classification" citations (resolving tier).
- `Admin/Experiments.md` — Exp aggregate A-F2: bare CF-001/EN-001/CE-003 candidate pointers (all resolve) **+ A-F5: one-word clarification** of the candidates note against the file's own drift indicator.
**Proposed action:** a single mechanical pass over the four files: qualify bare colliding-prefix citations per PKC-003 format (`File.md ID`), the one-word Experiments clarification, dated Last Audit notes per file. Citation-form-only; no content change; frozen history untouched.
**Ruling requested:** authorize the batch (human-directed per the B-pass recommendations; staged for execution on the word).

## 3. Tier 0 indexing convention — one-line ruling (NT aggregate B-N2)

**Live state:** Unknowns v5.78 carries one NT row (NT-010, Open); NT-001–009 are unindexed in the file's §18. Not a parity failure — indexing is owed for cross-module references only — but the convention is unstated.
**Proposed ruling text:** "Tier 0 files index only cross-module unknowns in `Unknowns.md`; file-internal unknowns remain tracked in the owning file."
**Ruling requested:** ratify the line (records current practice as convention) or amend it.

## 4. AVE-R2/R3 index-owed question — one-line ruling (AVE aggregate B-N2)

**Live state:** AVE-R2/R3 open in the sidecar; only AVE-R1/AVE-R4 are indexed in Unknowns v5.78. The file's own Adm_Scope_Map entry discloses the gap honestly. Whether AVE-R2 (ClosureBlocking / IIL interaction) is cross-module enough to be index-owed is the queued human call.
**Proposed ruling text:** "AVE-R2 (ClosureBlocking / IIL interaction) is index-owed — add to the `Unknowns.md` active index; AVE-R3 remains file-internal." (Alternative: rule both internal-only; the honest-disclosure record then governs.)
**Ruling requested:** choose; if the add row is ratified, it lands as a small Unknowns edit with the §4 provenance line.

## 5. CIR-GOV-002 mirroring — one-line ruling (CIR_Gov aggregate A-F2)

**Live state (re-verified):** CIR-GOV-002 (registered and resolved same-day, 2026-08-18) remains absent from Unknowns v5.78 — active index and resolved-entries paragraph — deviating from Size Management Rule 2's mirroring convention. AUDIT_04's remedy options stand.
**Proposed ruling text:** "Same-day open-and-close entries are exempt from Size Management Rule 2 mirroring; CIR-GOV-002 stays unindexed, recorded as resolved-and-exempt." (Alternative: authorize adding it to the resolved-entries paragraph — a small Unknowns edit.)
**Ruling requested:** choose. The exemption ruling is recommended: it matches existing practice (several same-day pairs already unindexed) and closes the class, not just the instance.

## 6. Ethical_Constraints FROZEN-marker asymmetry — ruling (EthCon aggregate A-F4)

**Live state:** the co-Tier-1 file carries no FROZEN markers while the Charter's Tier 1 blocks gained them 2026-09-03. Queued as a human question since AUDIT_05 (2026-10-27); no pass has enacted anything.
**Ruling requested (two options):** (a) authorize FROZEN markers on the Tier-1-equivalent blocks, matching the Charter convention — a dated, marker-only edit; or (b) rule the asymmetry deliberate (an Exploration-status co-Tier-1 file without markers, ownership resting with the Charter) and record the ruling. Note the interaction with EthCon A-F3 (Charter "Active" vs file "Exploration" status tension — carried for the Rule 5 verifier): option (b) pairs naturally with resolving A-F3 first.

## 7. Repository_Structure §II subfolder convention note — authorize dated note (RS aggregate B-N1)

**Live state:** the 2026-10-30 MAINT-29 pass created `Admin/ALogs/` and `Admin/AAudits/` with no RS decision entry; pass B graded it a near-trip (infrastructure homes governed by File_Template's Log-Split Rule, not content domains) and recommended a dated §II note so the placement doctrine covers the homes its corpus now uses.
**Proposed action:** one dated note in §II recording the per-folder Log/Audit subfolder convention (`Admin/ALogs/`, `Admin/AAudits/`; File_Template Log-Split Rule owns the rule, RS records the placement).
**Ruling requested:** authorize (text lands with §7 provenance).

## 8. INTEGRITY_SWEEP_PROMPT "campaign end" timing — ruling (ISP aggregate B-N1)

**Live state:** the instrument is commissioned (2026-10-29 ruling, Decision Brief item 1B) to execute **once, corpus-wide, at campaign end**; the 2026-10-30 execution was the commissioned run. Whether "campaign end" meant the close of the Admin completion batch (already passed) or a defined future boundary is unstated — the question governs whether any future once-only execution is owed and when.
**Ruling requested:** define "campaign end" — options: (a) the 2026-10-30 corpus-wide execution satisfied the commission (no future run owed); (b) campaign end = the close of the Campaign 2 audit stream (final CAMPAIGN2 deposit) — a run is owed then; (c) a human-set date. Recommend (a): the commissioned execution ran corpus-wide from the canonical file on 2026-10-30 (INTEGRITY_SWEEP_REPORT basis line cites v1.0.6).

## 9. ISP Status-promotion / automation-source confirmation — ruling (ISP aggregate A-F2)

**Live state:** the file held promotion pending confirmation that execution pulls from the canonical file rather than a hand-copied config; two months passed with no confirmation at issuance (2026-10-29). Since then, the 2026-10-30 sweep **executed from the canonical file** (v1.0.6 cited as basis; steps followed verbatim) — execution-from-canonical evidence now exists.
**Ruling requested:** either confirm the automation's config source (closing the original question), or rule the question closed by the 2026-10-30 execution evidence with a dated note in the file's log. No text change without the word.

## 10. MDR Cycle 1 dispositions + two model-family record — ruling (label half-stale; sweep report ratification queue item 7)

**Live state (verified):** the Mission Drift Review (`Admin/Auditor_Protocols.md` §Mission Drift Review; instrument `Admin/PROBE_INVOCATION.md`) Cycle 1 **was executed 2026-10-29** — human-ruled "MDR Cycle 1 executes now"; cold-start probe in a fresh thread (in-session run invalid per cold-start independence); **two raters**; ratings on record in the History Appendix: **P-1 Insufficient Evidence, P-3 Weakened, P-2/P-4/Q-1–Q-4 Aligned**. INSTRUMENT-RELEVANT: Cycle 1 is the **old-set baseline** (pre-MAINT-15 front-door edits); Cycle 2+ run on the new input set. The second-rater pass is recorded. **Execution is done; the label is stale on that half.**
**Held for human (the live debt):** (a) **dispositions of the two off-Aligned ratings** — P-1 (Insufficient Evidence): the input-side gap was substantially addressed by MAINT-15 (Axiom P-1 front-door visibility, 2026-10-29) — propose reading it as superseded-by-input-repair for Cycle 2 purposes, with Cycle 1's rating left as written (frozen); P-3 (Weakened): needs the human's own read of the axiom's live state — no recommendation drafted, by design; (b) the **two model-family record** — ratify which two model families ran Cycle 1 (record held in the sweep report's ratification queue; naming is the human's to ratify, not the Custodian's to assert); (c) optional piggyback: Cycle 2 timing under the §MDR cadence (AP-030's three-real-cycles mechanism question stands).
**Ruling requested:** dispose (a) and ratify (b); (c) optional.

## 11. IIL header refresh — retire the label as stale; optional annotation ruling (IIL aggregates B-N1/B-N3)

**Live state (verified):** the graded finding (B-N1: header predates the 2026-10-25 first incident) is **Closed-by-ruling** — PKC-001, ruled 2026-10-27; the drift predates the ruling window, no post-window edit occurred. The pass's own optional courtesy edit (refresh Last Audit/Auditor with a dated note **when the next incident lands**) remains available and is best folded into that landing, not done standalone. Related live items: B-N2 is covered by §2 of this package; **B-N3** (Highest Risk basis unannotated) has exact annotation text offered by pass B: "Medium — one open Minor-escalated incident, IIL-20261025-01".
**Ruling requested:** retire the "IIL header refresh" standing label (no action owed); optionally authorize the B-N3 Highest Risk annotation now (one-line header edit) or let it ride with the next incident landing.

---

## 12. Parked — verified live, no ruling requested from this package

Verified open but owned by other queues (recorded so the debt list stays honest):

- **Rule 5 verifier scope (when named):** RS A-F1 (Scope Boundary does-item without body section), RS A-F2 (stale ownership narration), GMP A-F2 (Does/Does-not candidate-vs-ratified tension), EthCon A-C8 (Active Disputes section vs header field), EthCon A-F3 (Charter "Active" vs file "Exploration") — all Not-re-tested / carried-for-verifier.
- **X5 Kit ID-Reference regeneration queue:** GMP A-F3 (GMP- prefix absent from the Kit), AVE A-F4 (AVE- prefix absent; two ID families).
- **Tests/ sweep:** AVE A-F3 (QCC-R1 resolution carried to `Tests/Quorum_Agent_Conduct_Protocol.md`).
- **Auditor_Protocols audit (LAST):** the PKC-020 five-variant asymmetry evidence set (NT A-F2 contributes).
- **PKC-030 wording caveat (NT A-F3):** human ruling queued at PKC-030 — unchanged.
- **RIP A-N1:** stale Discovery line ("Archive directory to be added here when established" — Archive/ has existed in Discovery's tree since 2026-08-09); Discovery-owned, Not-re-tested.
- **ISP A-F4:** zip-only workflow wording refresh — custodian backlog, harmless to function.
- **Standing blocked (unchanged):** Auditor_Protocols C3_04 / C2_69 rulings; Forge_Audit_Kit 35K-ceiling; Rule 5 verifier for the 23 tranche-2 aggregates (unnamed) + proposed scope extension to the coverage ledger (MAINT-60 finding 10).
- **Rules 8+10 amendment package (Claude fixes 1–3):** HELD per the human's 2026-11-05 ordering — drafted next, after this package's adjudication.

---

*Proposed 2026-11-05 by Vibe (Architect line primary, Repo Custodian secondary; non-independent Genesis Phase, disclosed). Nothing in this package is enacted by its deposit; every section awaits the human governing authority's word. Corrections by dated addendum only.*
