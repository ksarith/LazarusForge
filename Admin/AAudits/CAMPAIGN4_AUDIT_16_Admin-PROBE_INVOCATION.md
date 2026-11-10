# CAMPAIGN4_AUDIT_16_Admin-PROBE_INVOCATION.md

**Campaign 4 (Adversarial Sweep), artifact 16. Findings-only deposit per PKC-020 — advances no Last Audit, Last Reviewed, version, or Status.**
**Deposited:** 2026-11-10, Vibe (GLM 5.3 Flash architecture; no adjacent seat held on this file; adjacency disclosed: Vibe lines authored this file's v1.2–v1.4 maintenance passes and its Last Audit cells — those records are audited here as third-party content per the kickoff seat disclosure).
**Commission:** human-authorized continuation of the Campaign 4 sweep (kickoff resume point, tracker addendum 13).

## AUDIT: Admin/PROBE_INVOCATION.md
- Size fetched / sections not read: 20,554 chars / 168 lines, none (full text, plain decode)
- Head at fetch: `aa35b129` (LF main; the CAMPAIGN4_AUDIT_15 landing commit)
- File: Version 1.4; Status Draft; Spec Gates "N/A — operational prompt template, not a doctrine or specification claim"; Open Unknowns 0 (tracked at AP-030, mechanism-level); Ethical Anchor canonical
- Computed SHA-256 of the audited file: `e329cb4cb34aa918d8aa353ec5925db5f4c054dde5f092b3d416ddc1856dee46`
- FT exemption class 6 confirmed live ("Operational seeds and invocation templates" — PROBE_INVOCATION named verbatim; verified during AUDIT_15): template checks adapted; absent wrapper sections are not findings.

### Checks 1–11 (adapted per class 6)
1. **Fetch completeness — PASS.** 20,554 chars / 168 lines, plain decode, no truncation exposure.
2. **Sidecar count parity (X10, adapted) — VERIFIED CLEAN.** No sidecar; three-way parity holds: File State Open Unknowns 0; zero PROBE- rows in Unknowns.md v5.79; the mechanism-level pointer resolves to AP-030, verified open in AP v0.47 (open list) and registered (sidecar RL: "AP-030 registered to track").
3. **Header vs body — VERIFIED CLEAN.** Header Version 1.4 = the RL's latest version action (v1.4, 2026-10-30); the 2026-10-31 entry is explicitly path-only, no version bump — chain consistent.
4. **Source reconciliation — PERFORMED IN FULL** against AP v0.47 §Mission Drift Review (live fetch): the Trigger Cadence (5 ratified governance/canonical changes / 60-day backstop) matches How-To step 1; the eight axiom names match AP Phase B and the Charter's FROZEN Tier 1 block ("Axiom P-1 — Preservation of Life", line 101; P-4/Q-2 verified in AUDIT_11); the Silent→Atrophied rule quoted in the History Appendix matches AP's wording; step 5's log-derived counter matches AP's "running count in this section's own Resolution Log entries, not a separate file". Divergences found are F-PI-1/2/3 below — logged, not silent.
5. **Cross-references — all targets exist and resolve:** `Admin/Auditor_Protocols.md` (v0.47, §Mission Drift Review present), `Admin/Governance_Charter.md`, `README.md`, `Discovery.md` (root), `Admin/ALogs/Auditor_Protocols_Logs.md` (199,945 chars — step 4's post-repair destination verified live, carrying the AP-030 Invocation Record, the Cycle 1 record and the second-rater record), `Automation/cold_session_bundler.py` (16,295 chars, implements AP-017 — the v1.1 independence-language citation verifies).
6. **Bare citations — FINDING (F-PI-4).** One unqualified colliding-range MAINT citation in operative text; zero operative `Archive/` pre-relocation references (the v1.2 RL entry's `Archive/Logs/...` citation is declared frozen history by the 2026-10-31 entry, and the 2026-10-31 entry's old-path mention is the repair's own record — third file running with no unremediated Pattern 2 exposure in its own text, though F-PI-1 finds one in its source).
7. **Drift Indicators — none present** (class 6; not a finding). Compound Drift Rule vacuously did not fire.
8. **Section integrity — PASS.** Both `====` delimiters present; How-To steps 1–5 contiguous; paste-block structure (Step 1 / Step 2 / Output format / History Appendix) intact.
9. **Version/registry consistency — PASS** at file level (no VSR obligation; Discovery tree entry and maturity-snapshot row present).
10. **Ethical Anchor — VERIFIED CLEAN.** Exact canonical string, one occurrence.
11. **Highest Risk parity — N/A:** field absent, no invented value; Discovery's Risk cell honestly "—" (the CAMPAIGN_AUDIT_30 F1 header-fields data point, now under the class-6 exemption per the ISP precedent).

### Findings

- **F-PI-1 — WARNING (cross-file; the source-prevails chain terminates in a stale destination).** How-To step 4 directs the operator to log "per the Invocation Record fields in `Admin/Auditor_Protocols.md` §Mission Drift Review", and the file's own Derived-from fence says the source prevails on conflict — but the source section's live Invocation Record subsection (AP v0.47) still routes the record to the pre-relocation home: "Record belongs in the document's sidecar audit trail (`Archive/Logs/Auditor_Protocols_Logs.md`)." The log was relocated 2026-07-23; the MDR section is v0.29 text (2026-07-26) — written three days AFTER the relocation and never repaired. The 2026-10-31 MAINT-29 follow-up fixed this file's step 4 but not the governing source subsection, so on the very conflict the fence exists to resolve, the stale path wins. CAMPAIGN4_AUDIT_01 (AP's own sweep pass) did not record this (its deposit contains no Invocation Record or stale-path mention) — flagged to AP's audit record (item 1). Relocation-repair-miss, Pattern 2 instance 12; the instance sits in AP's text and is established from this file's deference chain.
- **F-PI-2 — NOTE (unresolved recurrence; CAMPAIGN_AUDIT_30 F2).** The paste block's evidence scale still presents four bullets with "Simulated/Analogous" merged into one label, while AP's live MDR section (v0.46 A4, 2026-11-02) reaffirms the five-label Evidence Classification ("Measured / Replicated / Simulated / Analogous / Placeholder … not a new confidence scale"). AUDIT_30 F2 recorded the identical divergence against v1.1 and routed it to the AP audit; v1.2–v1.4 did not remediate it, and Cycle 1's own logged records used the merged label. Folds into the F-ISP-6 class-6 family harmonization option.
- **F-PI-3 — NOTE (stale Derived-from pin; CAMPAIGN_AUDIT_30 F5 recurrence).** "Derived from: `Admin/Auditor_Protocols.md` v0.31" vs live v0.47; the MDR section gained the 2026-11-02 Measured-scope sentence post-derivation. Mitigated by the source-prevails fence; the corpus-wide pin-retirement disposition AUDIT_30 queued remains open (the F-FAK-6/F-ISP-3 class).
- **F-PI-4 — NOTE (unqualified colliding-range citation).** The operative Last Audit cell cites "MAINT-15" bare (origin: the frozen 2026-10-29 instrument-change RL entry). MAINT-15 exists in BOTH frozen logs with different content (LOG-1028: PKC-045 ratified and parked; LOG-1029: the front-door P-1/P-3 visibility edits), and PKC-003's qualified-citation precedent requires home qualification in the colliding MAINT-03..17 range. The content uniquely identifies LOG-1029's MAINT-15 (verified against the MAINT_INDEX row: "Front-door P-1/P-3 visibility edits enacted (human-ratified; instrument change recorded)"), so no live ambiguity; the cell predates MAINT-63's colliding-ID straggler batch and is not in its touched-file list (GMP, RIP, OC, the aggregates, Unknowns, ISP, IIL). Batch-eligible: sixth evidence point for the bare-citation grep remedy.
- **F-PI-5 — NOTE (MAINT-56-retired rows; conformant-at-touch).** The Last Audit and Auditor rows (retired 2026-11-04, MAINT-56) are carried; their latest write is 2026-10-31, before the retirement — the conformant-at-touch shape (the F-SEC-6/F-EP-6/F-CT-5 class; contrast F-ISP-4's post-retirement write). Next substantive touch must retire them.
- **F-PI-6 — NOTE (Verification Ref; the recorded class-6 divergence family, third instance).** Verification Ref points at a single AP section (`Admin/Auditor_Protocols.md` §Mission Drift Review), not FT-mandated `Admin/Verification_Gates.md` — the shape already recorded and reasoned in ISP's v1.0.2 RL entry ("PROBE_INVOCATION and BATTERY_SEED point at single AP sections per the same record"). Folds into the same harmonization option as F-PI-2.

**Aging Rule:** vacuous — Open Unknowns 0 at file level; the campaign's sixth no-trip control case (the mechanism-level unknown AP-030 is verified open and ages at AP, where AUDIT_01 F3 already covers it). **Compound Drift Rule:** vacuously did not fire (no Drift Indicators section; class 6).

### Clean checks / fabrication probes (all verified against live source)
- The v1.4 fixes are in place: the Step 2 output-format table's eight cells blank; the History Appendix Cycle 1 column carries the ratings (P-1 Insufficient Evidence, P-2 Aligned, P-3 Weakened, P-4–Q-4 Aligned) exactly as the v1.2/v1.4 RL entries record them — internal consistency verified three ways (appendix, RL, the logged Invocation Record's vocabulary in the sidecar).
- The v1.3 fixes are in place: How-To step 3 and the appendix note both carry the blank-every-cell-and-metadata rule for Cycles 2–3 pastes.
- The v1.4 entry's claim "CAMPAIGN_AUDIT_30 did not mention it" verified true (the 2026-10-29 report, run against v1.1, contains no pre-filled-example or appendix-empty mention; the defect was introduced by v1.2 later that day).
- The instrument-change rule (v1.3) was followed: the same-day input-set edit is recorded as an INSTRUMENT CHANGE with the old-set-baseline note; v1.3's "no input-set change has been made" was true at its writing and superseded hours later by the recorded change — no contradiction.
- The 2026-10-29 MAINT-15 instrument change corroborated by the MAINT_INDEX LOG-1029 row.
- CAMPAIGN_AUDIT_30's F1 exemption question is now answered by FT class 6 (verified live in AUDIT_15) — positive closure; its F3 (Cycle 1 execution) was resolved the same day (the v1.2 RL entry + the Invocation Record in the sidecar, the missed-backstop lapse folded in per human ruling).
- Discovery parity: the maturity snapshot's PROBE_INVOCATION row reads "Draft" with the same Spec Gates wording — File State and snapshot AGREE (contrast F-ISP-1; no recurrence).
- Ethical Anchor exact; both `====` delimiters present; all three canonical inputs exist.

### Out-of-scope observations (recorded, not findings)
- Status remains "Draft" while the instrument has a completed human-ruled Cycle 1 and four maintenance passes; File State and Discovery agree, so no mismatch — any promotion mirrors AUDIT_31 F2 and is the human's alone.
- AP-030's sidecar entry still carries no field table (the AUDIT_01 F4 recurrence — AP's audit record).
- The X3 straggler batch's published instance list should be checked against this file's MAINT-15 cell when the bare-citation remedy is ruled (F-PI-4).

### Bottom line
The instrument itself is in strong shape: every fix claimed by v1.3/v1.4 verifies in place, the Cycle 1 record chain is internally consistent three ways, the source section's mechanics (trigger cadence, rating vocabulary, escalation rule, log-derived counter) are faithfully mirrored, and the file's own text has no unremediated relocation exposure. The real defect is one step removed: the source section this file defers to still sends its records to a home that has not existed since 2026-07-23 (F-PI-1), and the two template-source divergences AUDIT_30 routed to the AP audit remain open (F-PI-2/3). Recommended human-ruled remedies: repair AP's Invocation Record destination line (or record the exemption), rule the class-6 family harmonization (evidence labels + Verification Refs + pin retirement in one pass), and fold the MAINT-15 cell into the bare-citation batch remedy.

### Disclosures
- Event: (ii) recurrence — the stale-pin class (F-PI-3, CAMPAIGN_AUDIT_30 F5), the evidence-label vocabulary divergence (F-PI-2, CAMPAIGN_AUDIT_30 F2), the retired-rows class (F-PI-5) and the recorded Verification Ref family (F-PI-6, the F-ISP-6 class) all recurred; one new Pattern 2 instance established (F-PI-1, instance 12).
- Adjacency: Vibe lines authored this file's v1.2–v1.4 passes and its Last Audit cells; those records are audited here as third-party content; the pass is non-independent with respect to this line's own repairs, disclosed per the kickoff seat disclosure.
- No tooling defects this pass: all fetches arrived plain; the SHA-256 implementation reused unchanged, the sanity vector passing before use.

### Next
- CAMPAIGN4_AUDIT_17: `Admin/BATTERY_SEED.md` (FT exemption class 6 — seed payload; template checks adapt).
- Next IDs: MAINT-105; Intake Log entry 22 (untouched all campaign).
