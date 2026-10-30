# CROSS_FILE_PATTERN_FINDINGS_Session7.md — Operations/ Phase (CAMPAIGN2_AUDIT_18–34)

**Corpus-wide artifact, Archive/Audits/ home per the MAINT-29 convention. Role: Skeptic/Auditor (Vibe). Date: 2026-10-30. Fetch head era: 8ab350e4. Folder: Operations/ — 17 files, all fetched full-text (sizes per report). Companion to Session 6 (Admin 01–03 + Architecture 04–17).**

## Phase totals

- 0 CRITICAL, 0 MAJOR, 6 WARNING (all WARNING-class), 28 NOTE-class observations. No halt triggers. Sidecar count parity: **16/16 perfect** (29/29 across both audited folders).
- **X10 Highest-Risk is the dominant defect of the Operations phase:** 6 of 16 files' Highest Risk fields do not reconcile with their live sidecar values —
  - Understated: Gate_01 (Medium vs High), Gate_05 (Medium vs High), Gate_06 (Medium vs High), Gate_07 (Low vs Medium).
  - Overstated: Gate_02 (High vs Medium), Air_Scrubber (High vs Medium).
  - Correct: Gate_03 (with an explanatory footnote — the convention done right), Gate_04, Electronics, Energy, Plastics, Tooling_Inventory, Woodworking.
  - Field absent (pre-known normalization item, human low-value-polish disposition): Automotive, Robotics, Exception_Evidence.
  - **Recommendation (carried and extended from Session 6): a corpus-wide Highest-Risk recompute batch** — the Session 6 value-misses (Mechanical_Structures, Thermal_Systems) and these six share one cause: Highest Risk is not recomputed when sidecar Risk values change. Ops_Scope_Map correctly mirrors the (defective) owning headers under the file-wins rule; the fix belongs in the owning files.

## X3 mechanical retrofit quality (same-day 2026-10-30 Operations pass)

- 188 in-whitelist citations qualified across 15 files (Automotive needed none; verified). Log discipline: same-day entries everywhere; frozen history untouched as ruled.
- **Two in-whitelist misses found:** Electronics CF-002 (ASM-003 Expiry Trigger) and CF-001 (Hardware Watchdog Doctrine note) — AUDIT_28 F1.
- **New artifact class — doubled parentheticals:** three instances of the insertion producing "\`Owning.md\` ID (\`Owning.md\`)" — Gate_01 §7.1 (AP-024), Gate_05 §EC-013 (EC-013), Gate_06 §EC-013 (EC-013). Citation-form-only; recommend a one-pass citation-form cleanup folded into the next delegated maintenance touch of each file.
- **Out-of-whitelist bare citations remain the standing population** (ST-001/002, SP-003, EL-006, GR-003, GU-002, TI-001, SC-001/004/005, MG, FL, GI, FN, FA, TS instances across operative text) — per the X3 rules these were left bare and reported to the human; the whitelist-expansion ruling remains open and is the single largest remaining citation-form exposure in the corpus.

## X1 retroactivity question (new, for the human)

Resolved unknowns closed before the Discharge Procedure's 2026-10-28 canonization — GR-003 (8-24), GI-004/GI-006 (8-31), GU-002 (9-01), PL-001 (8-23) — all carry Resolution fields but no Lessons Learned field on the sidecar entry (TS-004 conforms; pre-2026-10-28 closures in Admin/Architecture were not re-checked this session). Whether the now-canonical steps 4–5 apply retroactively is a ruling, not a defect; recommend a batched conforming fix if ruled yes.

## Aging — the folder is clean

**Zero files trip the 90-day Aging Rule** (contrast: 11 of 13 in Architecture; Admin AP at 96–128 days). All Operations sidecar entries were reviewed 2026-08-14 through 2026-10-30. Root cause is structural, not incidental: the 2026-08-14/15 Grok/Claude resolution-path review rounds touched every file, and the 2026-10-24/25 wrapper-hygiene passes followed. The Session 6 Aging-batch recommendation does not extend to this folder.

## Index integrity

- **Ops_Scope_Map: zero stale rows** — the only index audited so far with none (Arc_Scope_Map had 4; Discovery's maturity snapshot has the items below). The 2026-10-27 PKC-033 re-derivation is the visible cause.
- **Root-phase findings queued (Discovery.md maturity snapshot):** (a) Exception_Evidence row still reads "Proposed" — the owning file has been Exploration since 2026-10-25 (PKC-031); (b) Automotive and Robotics have no maturity-snapshot rows at all (registered in Routing/Ops_Scope_Map/created-list, but absent from the snapshot table). Grade at the root-index phase.

## Positives recorded

- Sidecar parity 16/16; count conventions (In Progress counted as open; candidate entries disclosed) applied consistently and disclosed in headers.
- Disclosure discipline materially better than either prior folder: retroactive log catch-ups (Gate_01, Gate_02, Gate_05, Electronics), same-day repair logging (Gate_05 stale fragment, Gate_03 GR-009 self-declaration), and honest "does not close the tracker" annotations on all five §EC-013 descent sequences.
- No relocation decay: all Operations sidecars are in-body self-anchors; zero dangling Archive/Logs pointers (the X8 sub-shape from Sessions 1–6 is absent here).
- Automotive/Robotics/Exception_Evidence state their limits plainly (Placeholder thresholds, no Measured claims, maintainer pending).

## Standing recommendations (Operations additions)

1. Highest-Risk recompute batch (corpus-wide; see above).
2. X3 follow-ups: qualify Electronics CF-001/CF-002; clean the three doubled parentheticals at next touch.
3. Whitelist-expansion ruling (ST, FL, GI, TS, MG, SC, GU, SP, EL, GR, TI, FN, FA and the rest of the operational prefixes) — the largest open citation-form decision.
4. X1 retroactivity ruling for pre-canonization resolved entries.
5. Discovery snapshot repairs (Exception_Evidence status; Automotive/Robotics rows) at the root-index phase.

*Findings only. No doctrine file, Status, Spec Gate, or Unknown was altered by this phase (PKC-020). Deposits: Operations/OAudits/ (folder O-letter home per the X3 designation ruling); this corpus-wide artifact in Archive/Audits/.*
