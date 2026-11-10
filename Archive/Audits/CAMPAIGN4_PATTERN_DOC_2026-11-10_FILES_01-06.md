# CAMPAIGN4_PATTERN_DOC_2026-11-10_FILES_01-06.md

**Campaign 4 cross-file pattern document, files 01–06 (Auditor_Protocols, Ethical_Constraints, Governance_Charter, Verification_Gates, File_Template, Canonical_Terms). Due at the five-to-eight-file mark per the kickoff convention; deposited alongside artifact 06.** Findings-only per PKC-020: this document aggregates already-deposited findings, advances nothing, and proposes no disposition — each pattern's remedy is the human's to rule.

## Pattern 1 — The 90-day Aging Rule is tripped repository-wide (systemic; four instances, two control cases)

- Instances: Auditor_Protocols.md 8 of 10 open entries (CAMPAIGN4_AUDIT_01 F3); Ethical_Constraints.md 3 of 7 open plus one near-trip (AUDIT_02 F-EC-2); Governance_Charter.md 13 of 13, 102–171 days (AUDIT_03 F-CH-4); Canonical_Terms.md 9 of 10, 112–139 days (AUDIT_06 F-CT-2). Aggregate: 33 of 38 open sidecar entries across the four tripping files are past the 90-day bar; the youngest tripped entry is 112 days old.
- Control cases: Verification_Gates.md (zero open unknowns — the rule cannot fire) and File_Template.md (no sidecar — the rule cannot fire). Neither is evidence of compliance; both are structural exemptions.
- Shape: the rule is never violated by commission — every instance is omission. Repository doctrine correctly forbids auditors from advancing Last Reviewed without a substantive review (findings-only per PKC-020), but no standing pass ever performs those reviews: the only entries that get refreshed are those caught by dedicated review passes (e.g. the Grok resolution-path reviews in Operations/, 2026-08-14/15; the X3 ruling annotations of 2026-10-28). The result is a monotonic aging clock that no scheduled mechanism resets.
- Interaction with the Cycle definition (CT-011): the Aging Rule's 90-day bar is Auditor_Protocols doctrine, deliberately much shorter than the one-calendar-year Cycle; the two do not conflict, and the Aging Rule's arithmetic is unaffected by the Cycle definition's propagation.
- Consolidated remedy option (already flagged at kickoff and in AUDIT_01/02; re-presented here as one ruling, not four): either authorize a batch Last-Reviewed refresh pass (re-read each tripped entry against current body state, advance only on genuine review, per the Ship_of_Theseus 2026-10-28 precedent), or amend the rule's remedy (e.g. make the trip a review-scheduling trigger rather than a per-file WARNING), or accept the aging as honest. One ruling covers all four instances and every future one.

## Pattern 2 — Relocation-repair-miss class (four instances, one corroborating instance)

The 2026-10-29/31 relocations (MAINT-29/30/31, the `<Letter>Logs/` homes; the 2026-08-09 Rename Registry migration) were repaired by fixing the fields and pointers named in findings, but never by grepping the corpus for every remaining occurrence of the old home. Instances:

1. Governance_Charter.md 2026-10-31 fix pass: repointed three File State fields, missed all body occurrences (AUDIT_03 F-CH-2 — four dangling pointers).
2. The same class in the Charter sidecar's own annotation (AUDIT_03 F-CH-1 context).
3. File_Template.md Update Procedure step 3: still routes rotation history to pre-relocation homes, never mentions the split triggers or the new homes (AUDIT_05 F-FT-1) — an operator-following-the-procedure defect, the most consequential shape.
4. Canonical_Terms.md: three passages still name `Discovery.md` as the Rename Registry's home four months after the 2026-08-09 migration, against its own two correct citations of `Archive/Rename_Registry.md` (AUDIT_06 F-CT-1).
- Corroborating (outside sweep scope): `Automation/audit_lib.py`'s LEGACY finding message still says "check Rename Registry in Discovery.md" — the stale home is baked into tooling output agents read.
- Remedy option: one corpus-wide grep sweep for the pre-relocation home strings (`Archive/Logs/` as a live-pointer target, `Discovery.md` + "Rename Registry" co-occurrence, `*_Changelog.md` routing language in procedures), each hit either repointed with a dated note or ruled historical per PKC-007. This is a mechanical, batch-eligible repair.

## Pattern 3 — The GOV-022 missing-sidecar-record cluster (two MAJOR instances, one false verification record)

- AUDIT_03 F-CH-1 (MAJOR): GOV-022 has no sidecar record anywhere despite the Charter's File State claiming full Closure Events live in the sidecar Resolution Log.
- AUDIT_04 F-VG-1 (MAJOR): Progress_Log PKC-006's 2026-10-27 resolution record asserts the opposite ("every named closure event (…GOV-022) present with recorded Closure Events") and was git-verified false at both candidate states of the sidecar (`af611dcb` / `cad08771`: 21 GOV headings, zero GOV-022 occurrences).
- Shape: a record that never existed is attested twice — once by the owning file's File State, once by a verification record in a third file. The TWGW candidate flagged in AUDIT_04 (recorded verification contradicted by the named artifact) is the general class; this cluster is its load-bearing instance because GOV-022's resolution status is unknown.
- Remedy option: reconstruct from git history whether GOV-022 was ever resolved (the AUDIT_77-style provenance reconstruction used on Canonical_Terms' 0.13 bump is the in-corpus precedent), then either restore the Closure Event or correct the File State claim and the PKC-006 record with dated addenda.

## Pattern 4 — The self-application gap lineage (File_Template.md; fifth data point)

- Aggregate lineage A-F3 = B-N2 = C-N2 (Rule 5-verified 2026-11-07) plus AUDIT_05 F-FT-2 (fourth consecutive pass) and the Pattern-A facet (four substantive touches without migration). This document adds no new instance — File_Template was the fifth file examined and the gap held — but records that the lineage is now the campaign's longest-running single open item and that every remedy remains blocked on the same human ruling (add a self-exemption class, or migrate the file).

## Pattern 5 — Stale drift indicators and completion notes tracking resolved events (two instances)

- Ethical_Constraints.md F-EC-1: a drift indicator still reads "before EC-008 is resolved" for an unknown ratified 2026-08-22 (the EC-AUD-003 class recurrence).
- Canonical_Terms.md F-CT-4: a "history ends at v0.6" note contradicted by its own section's later blocks.
- Shape: wrapper text that conditions on an event keeps firing after the event. Distinct from Pattern 2 (wrong home) — this is wrong condition. Remedy option: batch-eligible; each fix is a dated deletion or rewording.

## Positive records worth preserving (the sweep's clean columns)

- Mirrored claims hold in both directions everywhere tested: CT-004↔SEC-005, CT-002↔TS-004, the Emergence.md File Purpose pointer, Forge_flow's Defined Terms local copy, the Kit's CT- registry row, Trajectories' CT-003/CT-007 v0→v1 rows.
- Automation-doctrine claims verified against script source, not descriptions: File_Template's header claims against `integrity_check.py`/`parser.py` (AUDIT_05); Canonical_Terms' `[ExternalRepo]` entry against `audit_lib.py` (AUDIT_06), including the convention's own recorded debugging history matching ADP's log.
- Count and parity recomputes: clean on VG (all values), FT (N/A structure), CT (10=10=10, Highest Risk, disputes, index parity including both In Progress — Vehicle rows).
- The X3 citation retrofit's qualifications are holding everywhere re-checked (AP, CT, ADP texts).

## Coverage note

Six of 34 Admin/ files done. The pattern document's due window (AUDIT_06–08) is satisfied at artifact 06; the next update is due in the AUDIT_11–14 window per the 5–8-file convention, or earlier if a new pattern earns its Xn registration (two instances required).
---

## Update 1 — files 07–11 (2026-11-10, deposited alongside artifact 12)

Covers Security_Protocols.md (07), Safety_Protocols.md (08), Repository_Integrity_Protocol.md (09), Governance_Migration_Protocol.md (10), Autonomy_Divergence_Protocol.md (11), with the Forge_Audit_Kit.md data points noted where a pattern gains them. Append-only: the Patterns 1–5 text above is untouched. Eleven of 34 Admin/ files are now done.

**Pattern 1 (the 90-day Aging Rule) — instances 6–7, control cases 3–4:**

- Instance 6: Repository_Integrity_Protocol.md — 3 of 5 open entries, 124–144 days (AUDIT_09 F-RIP-2).
- Instance 7: Governance_Migration_Protocol.md — 2 of 4, both 107 days (AUDIT_10 F-GMP-4). Running aggregate: **47 of 60** open sidecar entries past the 90-day bar across the seven tripping files (AP 8/10, EC 3/7, Charter 13/13, CT 9/10, Security 9/11, RIP 3/5, GMP 2/4).
- Control case 3: Safety_Protocols.md — all five open entries reviewed 2026-10-27 (14 days), no trip (AUDIT_08).
- Control case 4: Autonomy_Divergence_Protocol.md — GOV-021c at 87 days on 2026-11-10, trips 2026-11-13 if unreviewed (AUDIT_11 F-ADP-3); a near-trip, disclosed as a live test of the consolidated-remedy question.

**Pattern 2 (relocation-repair-miss) — instances 5–10:**

5. Safety_Protocols.md — the 2026-10-28 Resolution Log entry cites the pseudo-audit at `Archive/Audits/AUDIT_07_Admin-Safety_Protocols.md`; the file lives at `Admin/AAudits/` (AUDIT_08 F-SP-1, probe-verified fetch failure at the cited path).
6. Security_Protocols.md — seven bare `Electronics.md` citations remain in operative text of the same file the 2026-10-29 X3 retrofit qualified 8 citations in; no root `Electronics.md` exists (AUDIT_07 F-SEC-2).
7. `Unknowns.md`’s Active Index RIP-005 row still pins "Security_Protocols.md … exists at v0.5" — the exact stale anchor the sidecar’s own 2026-09-03 correction removed; the repair missed the global index (AUDIT_09 F-RIP-1).
8. Governance_Migration_Protocol.md’s Relationship section carries the same "Security_Protocols.md — exists at v0.5 (2026-06-19)" pin (AUDIT_10 F-GMP-3).
9. Autonomy_Divergence_Protocol.md’s File State Governance ID row cites the nonexistent `Archive/Logs/Governance_Charter_Changelog.md`; the registration it describes is verified in the `Admin/ALogs/` copy; the row was written 2026-08-11, after the relocation (AUDIT_11 F-ADP-1).
10. Forge_Audit_Kit.md (AUDIT_12 F-FAK-2, filed in the next window’s numbering, recorded here as the class data point): five-plus operative references — including the Resolution Log’s "add new entries there" routing instruction and the drift indicator’s own designated home — still cite `Archive/Logs/Forge_Audit_Kit_Changelog.md` while the File State Sidecar Link is correctly repointed.

- The corpus-wide grep remedy’s evidence base is now ten instances plus the `audit_lib.py` LEGACY-message corroboration.

**Bare-citation grep remedy — fourth and fifth evidence points:** Repository_Integrity_Protocol.md ~7 bare path citations in operative/narrative text (AUDIT_09 F-RIP-5) and Governance_Migration_Protocol.md ~10 bare path citations, all targets resolving (AUDIT_10 F-GMP-7); both batch-eligible with F-SEC-2/F-SP-2.

**Pattern 4 — first data point outside File_Template:** Forge_Audit_Kit.md’s FAK-005 closure skipped the Kit’s own Discharge Procedure (AUDIT_12 F-FAK-3, with the Kit’s own Lessons-Learned drift indicator in firing state). The self-application gap class is no longer confined to File_Template itself; formal pattern numbering at the next update.

**Coverage note (updated):** eleven of 34 Admin/ files done. The next pattern-document update is due in the AUDIT_19–22 window per the 5–8-file convention (measured from artifact 12), or earlier if a new pattern earns its Xn registration (two instances required).


---

## Update 2 — files 12–21 (2026-11-10, deposited alongside artifact 21)

Covers Forge_Audit_Kit.md (12, canonical composition), Engineer_Protocols.md (13), External_Intake_Protocol.md (14), INTEGRITY_SWEEP_PROMPT.md (15), PROBE_INVOCATION.md (16), BATTERY_SEED.md (17), Resolution_Methodology.md (18), Operational_Conventions.md (19), Repository_Structure.md (20), Adm_Scope_Map.md (21). Append-only: the Patterns 1–5 text and Update 1 above are untouched. Twenty-one of 34 Admin/ files are now done. Provenance note: artifacts 13–19 were executed by a parallel session of this campaign (kickoff tracker addenda 11–17; the MAINT-109 repair restored the canonical chain around them); their findings are aggregated here from the canonical tracker record, and the instance numbering below continues it.

**Pattern 1 (the 90-day Aging Rule) — instances 8–9, control cases 5–11:**

- Instance 8: Forge_Audit_Kit.md — formally inapplicable (sidecar entries predate the field conventions; no Last Reviewed fields to age), substantively FAK-001/006/009 at 119+ days on 2026-11-10 (AUDIT_12 F-FAK-7, derivation limit disclosed).
- Instance 9: Engineer_Protocols.md — 5 of 5 open entries, 164–165 days (AUDIT_13 F-EP-4). Running aggregate: **52 of 65** open sidecar entries past the bar across the nine tripping files.
- External_Intake_Protocol.md: formally inapplicable (no Last Reviewed fields, the F-FAK-7 class); substantively 8 days open, no trip (AUDIT_14 F-EIP-3).
- Control cases (zero open unknowns — the rule cannot fire): INTEGRITY_SWEEP_PROMPT (5th), PROBE_INVOCATION (6th), BATTERY_SEED (7th), Resolution_Methodology (8th), Operational_Conventions (9th), Repository_Structure (10th), Adm_Scope_Map (11th). Neither evidence of compliance nor new systemic instances.

**Pattern 2 (relocation-repair-miss) — instances 11–16:**

11. Engineer_Protocols.md — the 2026-10-28 RL ledger line cites `Archive/Audits/AUDIT_08_Admin-Engineer_Protocols.md`; the report lives at `Admin/AAudits/` (AUDIT_13 F-EP-3; same 2026-10-28 batch as instance 5).
12. PROBE_INVOCATION.md / Auditor_Protocols.md — the source-prevails chain: PROBE's step 4 was repaired 2026-10-31 but the governing AP §Mission Drift Review subsection still routes Invocation Records to the pre-relocation `Archive/Logs/Auditor_Protocols_Logs.md`; on conflict the source prevails by PROBE's own fence (AUDIT_16 F-PI-1).
13. BATTERY_SEED.md — four operative citations route to the pre-relocation `Archive/Logs/Auditor_Protocols_Logs.md` in a file born post-relocation (2026-08-02); the 2026-10-29 X3 pass repaired bare citations but not these (AUDIT_17 F-BS-1).
14. Resolution_Methodology.md — two operative records still cite the pre-relocation `Admin/Cogito_Engine.md`; the file's own 2026-10-31 repoint fixed Core Pattern 10 move 3 only (AUDIT_18 F-RM-1).
15. Operational_Conventions.md — Convention 8 cites the pre-relocation `Archive/Logs/Progress_Log_Changelog.md`; the 2026-11-05 MAINT-63 touch repaired Convention 4 in the same file and missed Convention 8 (AUDIT_19 F-OC-1).
16. Repository_Structure.md — the 2026-10-28 ledger entry routes its report to the pre-relocation `Archive/Audits/` home; the live report sits at `Admin/AAudits/` (AUDIT_20 F-RS-1).

- The corpus-wide grep remedy's evidence base is now sixteen instances plus the `audit_lib.py` LEGACY-message corroboration. Adm_Scope_Map.md's dangling `Repo_Costodian_Prompt.md` citations (AUDIT_21 F-ASM-8) are recorded as the adjacent dangling-citation/typo class, not a Pattern 2 instance — the cited path was never a valid home of anything; the live tree's spelling differs.

**Pattern 3 (GOV-022 missing-record cluster):** no new instances in files 12–21.

**Pattern 4 (self-application gap) — formally numbered:**

- Instance 1: Forge_Audit_Kit.md — FAK-005's 2026-10-29 closure skipped the Kit's own Discharge Procedure (no discharge suffix, no Lessons Learned field or top-table row, step-6 removal skipped), with the Kit's own Lessons-Learned drift indicator in firing state (AUDIT_12 F-FAK-3; first data point outside File_Template, recorded in Update 1, numbered here per that update's deferral). The File_Template lineage (A-F3 = B-N2 = C-N2, F-FT-2, the Pattern-A facet) remains the anchor case; every remedy still awaits the same human ruling.

**Pattern 5 (stale conditions on resolved events):** no new instances in files 12–21. F-EP-1's stale "Active Critical Unknowns" hazard-table rows (Engineer_Protocols, AUDIT_13 — PL-001 and GR-003, both Resolved 2026-08-23/24, still listed active) are recorded as the nearest neighbour observed this window — body content, not wrapper text, so not numbered.

**Pattern 6 (NEW) — index-mirror decay (registered: instances across three files):**

Structural index files that restate per-file fields (scope maps, maturity snapshots, global-index pins) decay faster than the files they mirror, and their own "file wins" disclaimers trigger no recompute. Instances:

1. Adm_Scope_Map.md — six of 32 mirror entries stale against live File States at the same head: Verification_Gates (2/6 + High vs live 6/6 + Low), Security_Protocols (10 vs 11 open, SEC-013), Auditor_Protocols (4/6 vs 5/6), ADP (0/6 vs 6/6), Engineer_Protocols (High vs Medium), INTEGRITY_SWEEP_PROMPT (Draft vs Active — Operational Template) (AUDIT_21 F-ASM-2 through F-ASM-7); plus one doctrine file missing from the index entirely (F-ASM-1).
2. Discovery.md's maturity snapshot — INTEGRITY_SWEEP_PROMPT still listed "Draft" against File State "Active — Operational Template" even though the snapshot's own later update post-dated the promotion (AUDIT_15 F-ISP-1; the F-CH-3 class).
3. Corroborating (already counted in Pattern 2): `Unknowns.md`'s Active Index RIP-005 row pinning "Security_Protocols.md … exists at v0.5" after the sidecar's own correction removed that anchor (AUDIT_09 F-RIP-1).

- Shape: a mirror's Last Reviewed can advance (ASM's did, four times on 2026-10-28 alone) while its rows silently rot, because no standing pass recomputes them all — Pattern 1's omission shape applied to derived data instead of review dates. Remedy option: one batch mirror-recompute pass (re-derive every `*_Scope_Map.md` entry and Discovery's snapshot rows from live File States), one ruling covering the whole class, batch-eligible with the Pattern 2 grep sweep.

**Bare-citation grep remedy — sixth through eighth evidence points:** PROBE_INVOCATION's unqualified "MAINT-15" (AUDIT_16 F-PI-4), BATTERY_SEED's unqualified "MAINT-11" (AUDIT_17 F-BS-3), Adm_Scope_Map's unqualified "AUDIT_01–AUDIT_29" range twice (AUDIT_21 F-ASM-9).

**Coverage note (updated):** twenty-one of 34 Admin/ files done. The next pattern-document update is due in the AUDIT_27–30 window per the 5–8-file convention (measured from artifact 21), or earlier if a new pattern earns its Xn registration (two instances required).