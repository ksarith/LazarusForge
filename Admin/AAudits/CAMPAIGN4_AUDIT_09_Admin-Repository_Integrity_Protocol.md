# CAMPAIGN4_AUDIT_09 — Admin/Repository_Integrity_Protocol.md

**Campaign 4 adversarial sweep of Admin/ (kickoff: `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md`), artifact 09 of 34.** Date: 2026-11-10. Auditor: Vibe (GLM 5.3 Flash architecture); no adjacent seat held; Vibe authored none of this file's doctrine (prior Vibe-line maintenance passes are the file's own logged history and were audited as third-party content). **Findings-only per PKC-020: nothing on the target file, Unknowns.md, or any other file was advanced — no Last Audit, Last Reviewed, version, Status, Spec Gate, or unknown.** Conversion to an audit of record is the human's alone (MAINT-26 / AP-032).

## Fetch record

- Fetched full at LF main `19ec7fb5` (the CAMPAIGN4_AUDIT_08 landing commit): 114,151 chars, 1,060 lines, no truncation (fetch guard passed; tail intact through the Status section's closing doctrine lines).
- Fetched-file SHA-256: `d7793a0d66341a211cbcba18cdd719f571746510c52adb9cc01adb5674e4897f`.
- Method: kickoff §Method steps 1–5 — Auditor Prompt §3.3 checks 1–11 from live source, adversarial probes (fabrication, self-attestation, staleness, wrapper-decay, index-parity), grading per §4.


## File State as found (recomputed, not accepted)

- Status Draft; Body Stability Transitional; Spec Gates 2/6; Last Audit 2026-11-05 (MAINT-63 X3 straggler pass, 6 days before this audit); Open Unknowns 5; Active Disputes 0; Highest Risk High; Ethical Anchor canonical.
- Status section: Version 0.10 (2026-09-03), history v0.5–v0.10 present with the documented v0.1–v0.4 Resolution-Log-only gap note (2026-10-23).


## Findings

### F-RIP-1 — WARNING (cross-file staleness / relocation-repair-miss, Pattern 2 instance 7)

The Unknowns.md Active Index row for RIP-005 still reads: "Security_Protocols.md Phase 3 dependency — **file exists at v0.5**; cryptographic implementation not yet operational." The sidecar's own 2026-09-03 correction (RIP-AUD-004, recorded in the sidecar **Correction** block, the Resolution Log v0.10 entry, and the Status section) removed exactly this stale v0.5 anchor from the sidecar and the Status cross-reference list, explicitly "rather than updating it to a new fixed number, since the same staleness would recur at the next Security_Protocols revision" — and the file's Relationship section now correctly says "check that file directly for current version." The index row was missed: the repair was applied to the owning file but not propagated to the global index the sidecar correction was about. The claim is doubly stale: Security_Protocols.md advanced substantially after v0.5 (SEC-002/007a/009 closures, per the correction's own text) and, per CAMPAIGN4_AUDIT_07, no longer carries a current version string at all. A fresh agent reading the index gets a false version pin in the navigation layer whose owning entry says not to trust version pins. (Probe: Unknowns.md fetched full at `19ec7fb5`, index row located verbatim.)


### F-RIP-2 — WARNING (staleness probe / Aging Rule, systemic instance 6)

The 90-day Aging Rule trips on 3 of 5 open entries (computed 2026-11-10 against each sidecar's Last Reviewed): RIP-005 (2026-06-19, 144 days), RIP-006 (2026-06-27, 136 days), RIP-009 (2026-07-09, 124 days). Clean: RIP-002 (2026-09-03, 68 days), RIP-007 (2026-08-16, 86 days — see F-RIP-3 on which date governs). Sixth systemic instance of the campaign (AP 8/10, EC 3/7, Charter 13/13, CT 9/10, Security 9/11, now RIP 3/5); queued for the human's consolidated Aging-Rule ruling per the pattern document.


### F-RIP-3 — NOTE (section integrity / duplicate field table)

The RIP-007 sidecar carries two field tables: the main table (Last Reviewed 2026-06-19) plus an orphan second table containing only a "Last Reviewed 2026-08-16" row, appended after the Resolution Path. This is outside the File_Template single-field-table pattern (same structural family as AP-030's missing field table, AUDIT_01 F4) and makes the entry's review date ambiguous. This audit computes the Aging Rule on the later addendum table (2026-08-16, 86 days, no trip); if the main table's 2026-06-19 were read as governing, RIP-007 would also trip (144 days) and F-RIP-2 would become 4/5. The Description's "(Updated 2026-08-16)" marker corroborates the later date as intended; recorded, not repaired.


### F-RIP-4 — NOTE (cross-file date discrepancy, recurrence of the F-VG-2 class)

RIP-001's discharge date is 2026-06-27 in its own sidecar ("Discharge via Lessons Learned — 2026-06-27"; Last Reviewed 2026-06-27) but 2026-06-28 in Unknowns.md's resolved-entries paragraph ("Discharged via Lessons Learned 2026-06-28"). Second instance of the exact class flagged as F-VG-2 in CAMPAIGN4_AUDIT_04 (VG-001 field 2026-06-27 vs Unknowns 2026-06-28 — same one-day skew, possibly the same source confusion). No material consequence; recorded-not-repaired.


### F-RIP-5 — NOTE (bare path citations, batch-eligible; fourth evidence point for the grep remedy)

Bare citations to subfolder-homed files in this file's own text — the class the 2026-11-05 MAINT-63 X3 pass did NOT cover (it fixed colliding-ID prefixes only) and no recorded retrofit claims: clearly operative — Scope Boundary "beyond the minimum in Integrity_Incident_Log.md" (home `Admin/Integrity_Incident_Log.md`); Post-Exit Monitoring body "blocked on Auditor_Protocols.md's formally-deferred thresholds" (home `Admin/Auditor_Protocols.md`); RIP-007 Resolution Path "paper-complete via Integrity_Incident_Log.md"; RIP-005 sidecar heading "Security_Protocols.md Phase 3 dependency". Narrative-adjacent (dated correction/closure notes): "no `Verification_Gates.md` amendment" ×2 (ratified-subsection note and RIP-011 sidecar; home `Admin/Verification_Gates.md`), "see Auditor_Protocols.md" (2026-07-29 correction note). The file uses qualified forms everywhere else (e.g. `Admin/Security_Protocols.md` ×8, `Admin/Governance_Charter.md` ×6), so these are residue, not convention. No root-resolved file exists for any of them. Batch-eligible with the F-SEC-2/F-SP-2 corpus-wide grep remedy.


### F-RIP-6 — NOTE (log-ordering shape, ruled historical per the kickoff's PKC-007 standing rule)

The Resolution Log's newest-first order slips once: the 2026-09-04 entry sits after the 2026-09-03 entry. Cause is visible in the record — the 09-03 entry is itself a 2026-10-23 backfill and was inserted above the older in-time 09-04 entry. Head of log still matches Last Audit (2026-11-05); within-window, content-current; NOTE per the standing rule.


## Verified clean (checks 1–11, all from live source)

- **X10 count parity, four-way exact:** File State Open Unknowns 5 = open/in-progress sidecar entries 5 (RIP-002 Open, RIP-005 In Progress, RIP-006 In Progress, RIP-007 Open, RIP-009 Open) = Unknowns.md Active Index rows 5 = the log's own anchor `open_unknowns_after` 5. Closed entries RIP-001/003/004/008/010/011/012 correctly absent from the index per Size Management Rule 2, with the index's resolved-entries paragraphs covering RIP-001/003/010/011/012.
- **Index Status and Priority parity exact:** all five rows match their sidecars field-for-field (statuses Open/In Progress/In Progress/Open/Open; Priorities Major/Major/Minor/Major/Minor; Subtype Vehicle on RIP-005/006 only, matching their resolution-vehicle framing).
- **Highest Risk parity:** High = RIP-005 Risk High, the maximum among open entries (others Medium/Medium/Low/Medium).
- **Active Disputes:** 0 in File State = the section's "No active disputes" row.
- **Ethical Anchor:** File State value matches the §Ethical Anchor Field canonical string character-for-character.
- **Resolution Log integrity:** 18 dated bullets = the 2026-11-05 entry's `rl_entry_count_after` anchor; head entry date = Last Audit date; `file_line_count_after` 1060 verified against the live fetch (1,060 lines).
- **Fabrication probe (every cited ID/path verified in its claimed owner):** AP-031 live in Auditor_Protocols.md (formally-deferred Post-Exit thresholds); GOV-013 Post-Exit Monitoring Reversion Mechanism live in Governance_Charter.md; ASM-006 is this file's own Assumption row; `Archive/Transcripts/RIP_GMP-Copilot.md` exists (22,622 bytes); `Automation/AUDIT_HARNESS.py` and `Automation/audit_lib.py` exist; `Admin/Integrity_Incident_Log.md`, `Admin/Repository_Structure.md`, `Admin/File_Template.md`, `Admin/Forge_Audit_Kit.md`, `Admin/Governance_Migration_Protocol.md`, `Challenges/Biofouling.md`, `Discovery.md`, `Routing.md`, `Unknowns.md` all exist.
- **RIP-002's "3 of 6 live" implementation claim verified current** against harness v18 + audit_lib.py source: exactly three Phase 1 checks implemented (Ethical Anchor exact-match, required File State fields, cross-reference resolution via audit_lib.check_cross_refs); FROZEN validation, navigation spot-check, and sidecar↔index parity absent from both modules. A rare fully-current implementation-status claim.
- **Self-consistency:** Status precedence line present (2026-10-28 propagation, per Verification_Gates.md); Status v0.10 date matches the Resolution Log; version history v0.5–v0.10 present with the documented v0.1–v0.4 gap note; Scope Boundary items consistent with the body; the v0 Integrity Reality and Governance Enforcement States tables internally consistent.


## Collation

- **Compound Drift Rule: did not fire.** None of this file's own 18 Drift Indicators activated (the WARNINGs are external-consistency findings in Unknowns.md and the Aging Rule, not conditions from this file's indicator list). Weight recorded for the pattern document: two WARNINGs + four NOTEs, between the Safety control case (no fire) and the CT/Security activations.
- **TWGW candidates: none.** No harness/tooling defect with a usable correction surfaced this pass.
- **Out-of-scope observation (for the Unknowns.md owner pass):** the UNK-009 span annotation is asymmetric — the Critical Watch row annotates GOV-003 as "Resolved 2026-08-23, no longer a live span component" but RIP-001 (Resolved 2026-06-27, the earliest-resolved span component) remains listed without annotation in both the index row and the Critical Watch row.
- **Aging-Rule systemic tally after artifact 09:** six instances (AP 8/10, EC 3/7, Charter 13/13, CT 9/10, Security 9/11, RIP 3/5 = 45 of 56 open entries), three control cases (VG, FT, Safety).


## Disclosures

- Event: (iii) harness defect — two minor items this pass, both worked around: (a) `github_app.get_reference` is not exposed in this connector build (full head SHA obtained via `list_commits` with `fields:["sha"]`); (b) the run_typescript sandbox exposes no client write_file, so the first scratch-save attempt failed (recovered by extracting the saved tool-result JSON with jq). Also re-confirmed: directory listings return per-entry objects, not text (known class, hardened scan used).
- Continuity note: this artifact's audit was executed against head `19ec7fb5` throughout; no intermediate commits landed mid-pass.


## Next

- CAMPAIGN4_AUDIT_10: `Admin/Governance_Migration_Protocol.md` (191,505 chars at the pre-campaign count — largest file in the sweep; may need a two-pass read). Cross-file pattern document update due in the AUDIT_11–14 window.
- Human queue unchanged: consolidated Aging-Rule ruling; batch bare-citation grep remedy; F-SEC-1 log-or-correct; F-SP-1 repoint; F-RIP-1 index-row repair.
