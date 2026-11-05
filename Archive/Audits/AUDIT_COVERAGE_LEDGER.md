# AUDIT_COVERAGE_LEDGER — LazarusForge pass-coverage and Rule 7 trigger register

Status: Rule 5 verification pending — this register is not independently verified (Genesis Phase, disclosed below). It is a register, not an audit disposition record: every aggregate it cites carries its own Status line, and Rule 5 verification of those aggregates is tracked per-aggregate, not here.
Created: 2026-11-05 UTC under session MAINT-59, enacting Rule 10 of the AGGREGATE_METHOD_UPGRADE proposal (ratified by the human governing authority on 2026-11-04; ratification recorded in Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md Addendum #3). Backfilled in full at creation from the live Routing.md audit-artifact homes at LazarusForge head 7782650d and the 28 aggregates in Admin/AAudits/ — 93 rows. First allocation of MAINT-59 under the ratified ID-allocation rule.
Non-independence: Vibe holds Architect + Repo Custodian (Genesis Phase; formal Auditor seat open under GOV-008; Q-2 invoked). The counts below were produced by the same line that composed the aggregates they summarize; they are custodial bookkeeping, not independent verification.
Note: not relocated; lives beside the aggregates it indexes (Archive/Audits/ home follows the MAINT-47 tranche-1 precedent for audit meta-artifacts).

## Counting convention

- One row per pass-holding target: a file with at least one registered audit pass deposit in Routing.md. Meta-artifacts (templates, registries, logs about audits, correction files, verification packets) are excluded by convention.
- Passes: era-tagged deposit tags as registered in Routing.md (AU-xx | CA-xx | C2-xx | C3-xx), in deposit order.
- Aggregate: the tranche-1 or tranche-2 aggregate in Admin/AAudits/, or — when no aggregate is owed or composed.
- Open M/W/F: number of §2 ledger rows in the target's aggregate with severity MAJOR, WARNING, or FAIL whose disposition is a carrying state (Standing-open, Not re-tested, Asserted). Dispositions Enacted, Closed-by-ruling, Positive-record, Superseded, and Corrected-by-later-fact do not count. NOTE and INCOMPLETE rows never count. Zero is recorded as 0.
- Rule 7 trigger state: as concluded in the target's aggregate ("blocked" = carrying rows exist but action is held pending a human ruling; "no aggregate — deferred" = multi-pass target deliberately not aggregated pending rulings; "single pass" = aggregate not owed under the template's 2+ pass threshold).
- Last counted: 2026-11-04, Vibe (Repo Custodian seat), MAINT-59. Backfill date for all rows.
- Last counted: 2026-11-05, Vibe (Architect line PRIMARY; MAINT-63 execution pass over the human-ratified MAINT-62 ruling set). Disposition changes recorded by dated row annotation for rows 7, 13, 18, 20, 21, 23, 24, 27, 28 — owning-register closure in each target aggregate's §5 Addendum 2026-11-05; row 24's deferral cleared (AUDIT_86 F1 repaired by execution; aggregate still owed). No other row changed; no history rewritten.

## Maintenance rule

This ledger must be updated at every landing that registers a new pass deposit, changes a disposition, or opens/closes a carrying row. An un-updated ledger is itself a stale-index defect (the enacting proposal's own warning). Updates are recorded by changing the Last counted column (dated, attributed) — never by rewriting history rows silently.

## Register — 93 rows

| # | Target | Passes | Aggregate | Open M/W/F | Rule 7 trigger state | Last counted |
|---|---|---|---|---|---|---|
| 1 | `Admin/Adm_Scope_Map.md` | C2-96, CA-26 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Adm_Scope_Map.md` | 2 | blocked (A-F1, A-F2) | 2026-11-04 · Vibe · MAINT-59 |
| 2 | `Admin/Agent_Verification_Event.md` | C2-98, CA-27 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Agent_Verification_Event.md` | 3 | blocked (A-F1, A-F2, A-F3) | 2026-11-04 · Vibe · MAINT-59 |
| 3 | `Admin/Auditor_Protocols.md` | C2-02, C2-69, C3-04 | — | — | no aggregate — deferred (C3_04/C2_69 human rulings pending) | 2026-11-04 · Vibe · MAINT-59 |
| 4 | `Admin/Autonomy_Divergence_Protocol.md` | C2-79, CA-20 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Autonomy_Divergence_Protocol.md` | 6 | blocked (A-F1, A-F2, A-F3, A-F4, A-F5, A-F6) | 2026-11-04 · Vibe · MAINT-59 |
| 5 | `Admin/BATTERY_SEED.md` | C2-92 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 6 | `Admin/Canonical_Terms.md` | A-11, C2-77 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Canonical_Terms.md` | 4 | blocked (A-F2, A-F3, A-F4, B-F1) | 2026-11-04 · Vibe · MAINT-59 |
| 7 | `Admin/CIR_Gov.md` | A-04 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-CIR_Gov.md` | 3 | blocked (A-F1, A-F3, A-F4) | 2026-11-05 · Vibe · MAINT-63 (A-F2 resolved by execution — CIR-GOV-002 mirrored into the Unknowns resolved-entries paragraph per ruling set §3.5; aggregate Addendum 2026-11-05) |
| 8 | `Admin/Computational_Institutional_Reasoning.md` | C2-78, CA-21 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Computational_Institutional_Reasoning.md` | 4 | blocked (A-F1, A-F2, A-F3, A-F4) | 2026-11-04 · Vibe · MAINT-59 |
| 9 | `Admin/Economics.md` | A-19, C2-95, CA-19 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Economics.md` | 0 | computable (all graded findings closed) | 2026-11-04 · Vibe · MAINT-59 |
| 10 | `Admin/Engineer_Protocols.md` | A-08, C2-81 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Engineer_Protocols.md` | 2 | blocked (A-F1, A-F2) | 2026-11-04 · Vibe · MAINT-59 |
| 11 | `Admin/Environmental_Constraints.md` | C2-80, CA-25 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Environmental_Constraints.md` | 5 | blocked (A-F1, A-F2, A-F3, A-F4, A-F5) | 2026-11-04 · Vibe · MAINT-59 |
| 12 | `Admin/Ethical_Constraints.md` | A-05, C2-72 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Ethical_Constraints.md` | 4 | blocked (A-F1, A-F2, A-F3, A-C8) | 2026-11-04 · Vibe · MAINT-59 |
| 13 | `Admin/Experiments.md` | C2-91, CA-28 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Experiments.md` | 0 | computable (all graded findings closed) | 2026-11-05 · Vibe · MAINT-63 (A-F2 resolved by execution — candidate-ID pointers qualified; A-F5 re-verified already-repaired 2026-10-28, no edit; aggregate Addendum 2026-11-05) |
| 14 | `Admin/External_Intake_Protocol.md` | C3-01 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 15 | `Admin/File_Template.md` | A-10, C2-01, C2-99 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-File_Template.md` | 3 | blocked (A-F2, A-F3, B-F1) | 2026-11-04 · Vibe · MAINT-59 |
| 16 | `Admin/Forge_Audit_Kit.md` | A-15, C2-70 | — | — | no aggregate — deferred (FAK 35K-ceiling ruling pending) | 2026-11-04 · Vibe · MAINT-59 |
| 17 | `Admin/Governance_Charter.md` | A-01, C2-03, C2-71 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Governance_Charter.md` | 3 | blocked (B-F1, B-F2, B-F3) | 2026-11-04 · Vibe · MAINT-59 |
| 18 | `Admin/Governance_Migration_Protocol.md` | A-02, C2-73 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Governance_Migration_Protocol.md` | 2 | blocked (A-F1, A-F2) | 2026-11-05 · Vibe · MAINT-63 (B-N2 resolved by execution — X3 straggler pass, 20 citations qualified on the audit-flagged zones; graded rows unchanged; aggregate Addendum 2026-11-05) |
| 19 | `Admin/Hardware_Diversity_Ladder.md` | C2-87, CA-29 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Hardware_Diversity_Ladder.md` | 1 | blocked (A-F1) | 2026-11-04 · Vibe · MAINT-59 |
| 20 | `Admin/Integrity_Incident_Log.md` | C2-90, CA-23 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Integrity_Incident_Log.md` | 0 | computable (all graded findings closed) | 2026-11-05 · Vibe · MAINT-63 (B-N1 and B-N2 resolved by execution — the File State header refresh closes the PKC-001 decay, the two live-section citations qualified with frozen history preserved bare; B-N3 annotation deferred to the next incident landing per ruling set; the IIL header-refresh standing-debt label retired per ruling set §3.11; aggregate Addendum 2026-11-05) |
| 21 | `Admin/INTEGRITY_SWEEP_PROMPT.md` | C2-88, CA-31 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-INTEGRITY_SWEEP_PROMPT.md` | 1 | blocked (A-F1) | 2026-11-05 · Vibe · MAINT-63 (B-N1 resolved by ruling — §3.8 commission-closure note recorded in File State; A-F1 anchor unchanged; aggregate Addendum 2026-11-05) |
| 22 | `Admin/Metrics_Scaffold.md` | A-17, C2-85, CA-17 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Metrics_Scaffold.md` | 0 | computable (all graded findings closed) | 2026-11-04 · Vibe · MAINT-59 |
| 23 | `Admin/Nothingness_Theorem.md` | C2-94, CA-24 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Nothingness_Theorem.md` | 0 | computable (all graded findings closed) | 2026-11-05 · Vibe · MAINT-63 (B-N2 resolved by ruling — Tier 0 convention recorded as Unknowns Size Management Rule 7 per ruling set §3.3; aggregate Addendum 2026-11-05) |
| 24 | `Admin/Operational_Conventions.md` | A-16, C2-86 | — | — | no aggregate — AUDIT_86 F1 (Convention 4 pointer) repaired by execution 2026-11-05 (MAINT-63 §1); aggregate still owed (2 passes) | 2026-11-05 · Vibe · MAINT-63 |
| 25 | `Admin/PROBE_INVOCATION.md` | C2-89, CA-30 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-PROBE_INVOCATION.md` | 3 | blocked (A-F1, A-F2, A-F3) | 2026-11-04 · Vibe · MAINT-59 |
| 26 | `Admin/Progress_Log.md` | A-14, C2-74 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Progress_Log.md` | 1 | blocked (A-F1) | 2026-11-04 · Vibe · MAINT-59 |
| 27 | `Admin/Repository_Integrity_Protocol.md` | A-03, C2-76 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Repository_Integrity_Protocol.md` | 1 | blocked (A-F1) | 2026-11-05 · Vibe · MAINT-63 (B-N1 resolved by execution — 6 citations qualified; A-F1 unchanged; aggregate Addendum 2026-11-05) |
| 28 | `Admin/Repository_Structure.md` | A-12, C2-97 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Repository_Structure.md` | 2 | blocked (A-F1, A-F2) | 2026-11-05 · Vibe · MAINT-63 (B-N1 resolved by execution — §II subfolder-convention note recorded; graded rows unchanged; aggregate Addendum 2026-11-05) |
| 29 | `Admin/Resolution_Methodology.md` | C2-82, CA-22 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Resolution_Methodology.md` | 2 | blocked (A-F1, A-F2) | 2026-11-04 · Vibe · MAINT-59 |
| 30 | `Admin/Safety_Protocols.md` | A-07 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 31 | `Admin/Security_Protocols.md` | A-06, C2-75 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Security_Protocols.md` | 4 | blocked (A-F1, A-F2, A-F5, B-F1) | 2026-11-04 · Vibe · MAINT-59 |
| 32 | `Admin/Ship_of_Theseus.md` | A-18, C2-93, CA-18 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Ship_of_Theseus.md` | 0 | computable (all graded findings closed) | 2026-11-04 · Vibe · MAINT-59 |
| 33 | `Admin/Trajectories.md` | A-13, C2-84 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Trajectories.md` | 3 | blocked (A-F2, A-F3, A-F4) | 2026-11-04 · Vibe · MAINT-59 |
| 34 | `Admin/Verification_Gates.md` | A-09, C2-83 | `Admin/AAudits/AUDIT_AGGREGATE_Admin-Verification_Gates.md` | 3 | blocked (A-F1, A-F2, B-F1) | 2026-11-04 · Vibe · MAINT-59 |
| 35 | `Architecture/Arc_Scope_Map.md` | C2-04 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 36 | `Architecture/Chemistry.md` | C2-05 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 37 | `Architecture/Cognitive_Frameworks.md` | C2-06 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 38 | `Architecture/Components.md` | C2-07 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 39 | `Architecture/Engineering.md` | C2-08 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 40 | `Architecture/Facilities.md` | C2-09 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 41 | `Architecture/Forge_flow.md` | C2-11 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 42 | `Architecture/Forge_Net.md` | C2-10 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 43 | `Architecture/Friction_Dynamics.md` | C2-12 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 44 | `Architecture/Geck_forge_seed.md` | C2-13 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 45 | `Architecture/Local_Governance_Framework.md` | C2-14 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 46 | `Architecture/Mechanical_Structures.md` | C2-15 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 47 | `Architecture/Precision.md` | C2-16 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 48 | `Architecture/Thermal_Systems.md` | C2-17 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 49 | `Challenges/Biofouling.md` | C2-54 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 50 | `Challenges/Cha_Scope_Map.md` | C2-53 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 51 | `Challenges/Closed_Loop_Feedstock.md` | C2-55 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 52 | `Challenges/Critical_Minerals.md` | C2-56 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 53 | `Challenges/Emergence.md` | C2-57 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 54 | `Challenges/Energy_Scarcity.md` | C2-58 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 55 | `Challenges/Planned_Obsolescence.md` | C2-59 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 56 | `Challenges/Return_To_Eden.md` | C2-60 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 57 | `Challenges/Waste.md` | C2-61 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 58 | `Challenges/Water.md` | C2-62 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 59 | `Operations/Air_Scrubber.md` | C2-26 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 60 | `Operations/Automotive.md` | C2-27 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 61 | `Operations/Electronics.md` | C2-28 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 62 | `Operations/Energy.md` | C2-29 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 63 | `Operations/Exception_Evidence.md` | C2-30 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 64 | `Operations/Gate_01_Intake.md` | C2-19 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 65 | `Operations/Gate_02_Triage.md` | C2-20 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 66 | `Operations/Gate_03_Reduction.md` | C2-21 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 67 | `Operations/Gate_04_Separation_Mechanical.md` | C2-22 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 68 | `Operations/Gate_05_Separation_Thermal.md` | C2-23 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 69 | `Operations/Gate_06_Fabrication.md` | C2-24 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 70 | `Operations/Gate_07_Utilization.md` | C2-25 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 71 | `Operations/Ops_Scope_Map.md` | C2-18 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 72 | `Operations/Plastics.md` | C2-31 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 73 | `Operations/Robotics.md` | C2-32 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 74 | `Operations/Tooling_Inventory.md` | C2-33 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 75 | `Operations/Woodworking.md` | C2-34 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 76 | `Tests/Admin_Governance_Teardown_POC.md` | C2-47 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 77 | `Tests/Chaos_Dynamics.md` | C2-36 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 78 | `Tests/Chrono_Divergence_Pilot.md` | C2-46 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 79 | `Tests/Chrono_Divergence.md` | C2-45 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 80 | `Tests/Cognitive_Salvage_Layer.md` | C2-37 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 81 | `Tests/Field_Logs.md` | C2-38 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 82 | `Tests/Hydrologic_Resource_Cascade.md` | C2-39 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 83 | `Tests/Leviathan_testing.md` | C2-40 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 84 | `Tests/Living_Waters.md` | C2-41 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 85 | `Tests/MAQT_Role_Cards_and_Cycle1_Task.md` | C2-43 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 86 | `Tests/Multi_Agent_Quorum_Trial.md` | C2-42 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 87 | `Tests/Persistent_Cognition_Candidates.md` | C2-52 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 88 | `Tests/Pyrolysis_Cascade.md` | C2-48 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 89 | `Tests/Quorum_Agent_Conduct_Protocol.md` | C2-44 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 90 | `Tests/Solar_Descent.md` | C2-49 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 91 | `Tests/Support_Raft.md` | C2-50 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 92 | `Tests/Trophic_Forge.md` | C2-51 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
| 93 | `Tests/Tst_Scope_Map.md` | C2-35 | — | — | single pass — aggregate not owed (template: 2+ passes) | 2026-11-04 · Vibe · MAINT-59 |
