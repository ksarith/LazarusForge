# Routing.md — LazarusForge
**Canonical Navigation and Link Mapping Index.**
**Last updated: 2026-08-10**

---

## File Purpose
This file acts as the primary network lookup table for automated agents, continuous integration systems, and human collaborators. It provides programmatic access to the raw data payloads of the repository while enforcing bi-directional link traceability via the File Template.

## Scope of this Routing Table

**Routing.md is the map of the *active operational repository*, not a complete inventory of every file that exists on disk.**

Intentionally excluded from the Master Routing Map (by design, not by oversight):

- All content under `Archive/` and `Archive/Logs/` — historical preservation layer. These files are not part of the live operational surface and are not required to carry Navigation Anchors or participate in the backlink requirement.
- Pure implementation artifacts under `Automation/` (the `.py` sources themselves). Supporting documentation that is doctrine may still appear.
- Transient or generated artifacts that may appear in working trees but are not committed doctrine.

The difference between the number of paths listed here (~112) and the total number of non-directory files in a full checkout is therefore expected. Agents must not treat a missing entry for an Archive file as registry drift or an integrity failure. If an active (non-Archive) doctrine or protocol file is absent from this table, that *is* a defect and should be logged.

Last scope clarification: 2026-08-10 (integrity cleanup pass).

---

## Master Routing Map

| File Path / Name | Raw Content URL (LLM Context Target) | Repository URL (Human Target) | Backlink Requirement |
| :--- | :--- | :--- | :--- |
| **Root Layer** | | | |
| `LICENSE` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/LICENSE) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/LICENSE) | Explicit |
| `NOTICE` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/NOTICE) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/NOTICE) | Explicit |
| `LICENSE.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/LICENSE.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/LICENSE.md) | Explicit |
| `README.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/README.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/README.md) | Explicit |
| `Discovery.md` * | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Discovery.md) | Explicit |
| `Unknowns.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Unknowns.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Unknowns.md) | Explicit |
| `Routing.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Routing.md) | *Self-referential* |
| `CONTRIBUTING.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/CONTRIBUTING.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/CONTRIBUTING.md) | Explicit |
| **Admin/ Layer** | | | |
| `Admin/Adm_Scope_Map.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Adm_Scope_Map.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Adm_Scope_Map.md) | Explicit |
| `Admin/Auditor_Protocols.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Auditor_Protocols.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Auditor_Protocols.md) | Explicit |
| `Admin/Autonomy_Divergence_Protocol.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Autonomy_Divergence_Protocol.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Autonomy_Divergence_Protocol.md) | Explicit |
| `Admin/BATTERY_SEED.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/BATTERY_SEED.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/BATTERY_SEED.md) | Explicit |
| `Admin/CIR_Gov.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/CIR_Gov.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/CIR_Gov.md) | Explicit |
| `Admin/Canonical_Terms.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Canonical_Terms.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Canonical_Terms.md) | Explicit |
| `Admin/Computational_Institutional_Reasoning.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Computational_Institutional_Reasoning.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Computational_Institutional_Reasoning.md) | Explicit |
| `Admin/Economics.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Economics.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Economics.md) | Explicit |
| `Admin/Engineer_Protocols.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Engineer_Protocols.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Engineer_Protocols.md) | Explicit |
| `Admin/Environmental_Constraints.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Environmental_Constraints.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Environmental_Constraints.md) | Explicit |
| `Admin/Ethical_Constraints.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Ethical_Constraints.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Ethical_Constraints.md) | Explicit |
| `Admin/Experiments.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Experiments.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Experiments.md) | Explicit |
| `Admin/File_Template.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/File_Template.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/File_Template.md) | Explicit |
| `Admin/Forge_Audit_Kit.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Forge_Audit_Kit.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Forge_Audit_Kit.md) | Explicit |
| `Admin/Governance_Charter.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Governance_Charter.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Governance_Charter.md) | Explicit |
| `Admin/Governance_Migration_Protocol.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Governance_Migration_Protocol.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Governance_Migration_Protocol.md) | Explicit |
| `Admin/Hardware_Diversity_Ladder.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Hardware_Diversity_Ladder.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Hardware_Diversity_Ladder.md) | Explicit |
| `Admin/Integrity_Incident_Log.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Integrity_Incident_Log.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Integrity_Incident_Log.md) | Explicit |
| `Admin/Progress_Log.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Progress_Log.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Progress_Log.md) | Explicit |
| `Admin/Nothingness_Theorem.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Nothingness_Theorem.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Nothingness_Theorem.md) | Explicit |
| `Admin/PROBE_INVOCATION.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/PROBE_INVOCATION.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/PROBE_INVOCATION.md) | Explicit |
| `Admin/Repository_Integrity_Protocol.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Repository_Integrity_Protocol.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Repository_Integrity_Protocol.md) | Explicit |
| `Admin/Repository_Structure.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Repository_Structure.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Repository_Structure.md) | Explicit |
| `Admin/Resolution_Methodology.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Resolution_Methodology.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Resolution_Methodology.md) | Explicit |
| `Admin/Safety_Protocols.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Safety_Protocols.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Safety_Protocols.md) | Explicit |
| `Admin/Security_Protocols.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Security_Protocols.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Security_Protocols.md) | Explicit |
| `Admin/Ship_of_Theseus.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Ship_of_Theseus.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Ship_of_Theseus.md) | Explicit |
| `Admin/Trajectories.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Trajectories.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Trajectories.md) | Explicit |
| `Admin/Verification_Gates.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Admin/Verification_Gates.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Admin/Verification_Gates.md) | Explicit |
| **Architecture/ Layer** | | | |
| `Architecture/Arc_Scope_Map.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Arc_Scope_Map.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Arc_Scope_Map.md) | Explicit |
| `Architecture/Chemistry.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Chemistry.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Chemistry.md) | Explicit |
| `Architecture/Cognitive_Frameworks.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Cognitive_Frameworks.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Cognitive_Frameworks.md) | Explicit |
| `Architecture/Components.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Components.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Components.md) | Explicit |
| `Architecture/Engineering.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Engineering.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Engineering.md) | Explicit |
| `Architecture/Facilities.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Facilities.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Facilities.md) | Explicit |
| `Architecture/Forge_Net.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Forge_Net.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Forge_Net.md) | Explicit |
| `Architecture/Forge_flow.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Forge_flow.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Forge_flow.md) | Explicit |
| `Architecture/Friction_Dynamics.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Friction_Dynamics.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Friction_Dynamics.md) | Explicit |
| `Architecture/Geck_forge_seed.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Geck_forge_seed.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Geck_forge_seed.md) | Explicit |
| `Architecture/Mechanical_Structures.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Mechanical_Structures.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Mechanical_Structures.md) | Explicit |
| `Architecture/Precision.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Precision.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Precision.md) | Explicit |
| `Architecture/Thermal_Systems.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Architecture/Thermal_Systems.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Architecture/Thermal_Systems.md) | Explicit |
| **Operations/ Layer** | | | |
| `Operations/Air_Scrubber.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Air_Scrubber.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Air_Scrubber.md) | Explicit |
| `Operations/Electronics.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Electronics.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Electronics.md) | Explicit |
| `Operations/Energy.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Energy.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Energy.md) | Explicit |
| `Operations/Gate_01_Intake.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Gate_01_Intake.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Gate_01_Intake.md) | Explicit |
| `Operations/Gate_02_Triage.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Gate_02_Triage.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Gate_02_Triage.md) | Explicit |
| `Operations/Gate_03_Reduction.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Gate_03_Reduction.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Gate_03_Reduction.md) | Explicit |
| `Operations/Gate_04_Separation_Mechanical.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Gate_04_Separation_Mechanical.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Gate_04_Separation_Mechanical.md) | Explicit |
| `Operations/Gate_05_Separation_Thermal.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Gate_05_Separation_Thermal.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Gate_05_Separation_Thermal.md) | Explicit |
| `Operations/Gate_06_Fabrication.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Gate_06_Fabrication.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Gate_06_Fabrication.md) | Explicit |
| `Operations/Gate_07_Utilization.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Gate_07_Utilization.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Gate_07_Utilization.md) | Explicit |
| `Operations/Ops_Scope_Map.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Ops_Scope_Map.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Ops_Scope_Map.md) | Explicit |
| `Operations/Plastics.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Plastics.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Plastics.md) | Explicit |
| `Operations/Woodworking.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Operations/Woodworking.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Operations/Woodworking.md) | Explicit |
| **Challenges/ Layer** | | | |
| `Challenges/Biofouling.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Challenges/Biofouling.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Challenges/Biofouling.md) | Explicit |
| `Challenges/Cha_Scope_Map.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Challenges/Cha_Scope_Map.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Challenges/Cha_Scope_Map.md) | Explicit |
| `Challenges/Closed_Loop_Feedstock.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Challenges/Closed_Loop_Feedstock.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Challenges/Closed_Loop_Feedstock.md) | Explicit |
| `Challenges/Critical_Minerals.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Challenges/Critical_Minerals.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Challenges/Critical_Minerals.md) | Explicit |
| `Challenges/Emergence.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Challenges/Emergence.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Challenges/Emergence.md) | Explicit |
| `Challenges/Energy_Scarcity.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Challenges/Energy_Scarcity.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Challenges/Energy_Scarcity.md) | Explicit |
| `Challenges/Planned_Obsolescence.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Challenges/Planned_Obsolescence.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Challenges/Planned_Obsolescence.md) | Explicit |
| `Challenges/Return_To_Eden.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Challenges/Return_To_Eden.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Challenges/Return_To_Eden.md) | Explicit |
| `Challenges/Waste.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Challenges/Waste.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Challenges/Waste.md) | Explicit |
| `Challenges/Water.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Challenges/Water.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Challenges/Water.md) | Explicit |
| **Tests/ Layer** | | | |
| `Tests/Chaos_Dynamics.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Chaos_Dynamics.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Chaos_Dynamics.md) | Explicit |
| `Tests/Cognitive_Salvage_Layer.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Cognitive_Salvage_Layer.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Cognitive_Salvage_Layer.md) | Explicit |
| `Tests/Field_Logs.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Field_Logs.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Field_Logs.md) | Explicit |
| `Tests/Hydrologic_Resource_Cascade.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Hydrologic_Resource_Cascade.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Hydrologic_Resource_Cascade.md) | Explicit |
| `Tests/Leviathan_testing.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Leviathan_testing.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Leviathan_testing.md) | Explicit |
| `Tests/Living_Waters.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Living_Waters.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Living_Waters.md) | Explicit |
| `Tests/Pyrolysis_Cascade.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Pyrolysis_Cascade.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Pyrolysis_Cascade.md) | Explicit |
| `Tests/Solar_Descent.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Solar_Descent.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Solar_Descent.md) | Explicit |
| `Tests/Support_Raft.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Support_Raft.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Support_Raft.md) | Explicit |
| `Tests/Trophic_Forge.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Trophic_Forge.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Trophic_Forge.md) | Explicit |
| `Tests/Tst_Scope_Map.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Tests/Tst_Scope_Map.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Tests/Tst_Scope_Map.md) | Explicit |
| **Automation/ Layer** | | | |
| `Automation/AUDIT_HARNESS.py` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Automation/AUDIT_HARNESS.py) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Automation/AUDIT_HARNESS.py) | N/A (Script) |
| `Automation/Colab_Integrity.py` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Automation/Colab_Integrity.py) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Automation/Colab_Integrity.py) | N/A (Script) |
| `Automation/Colab_Launcher.py` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Automation/Colab_Launcher.py) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Automation/Colab_Launcher.py) | N/A (Script) |
| `Automation/Colab_cold_session.py` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Automation/Colab_cold_session.py) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Automation/Colab_cold_session.py) | N/A (Script) |
| `Automation/Cold_session_manifest.py` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Automation/Cold_session_manifest.py) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Automation/Cold_session_manifest.py) | N/A (Script) |
| `Automation/audit_lib.py` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Automation/audit_lib.py) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Automation/audit_lib.py) | N/A (Script) |
| `Automation/cold_session_bundler.py` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Automation/cold_session_bundler.py) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Automation/cold_session_bundler.py) | N/A (Script) |
| `Automation/integrity_check.py` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Automation/integrity_check.py) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Automation/integrity_check.py) | N/A (Script) |
| `Automation/parser.py` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Automation/parser.py) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Automation/parser.py) | N/A (Script) |
| **Archive/ Layer** | | | |
| `Archive/Transcripts/ClaudeAudit.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/ClaudeAudit.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/ClaudeAudit.md) | Explicit |
| `Archive/Transcripts/Configurations.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/Configurations.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/Configurations.md) | Explicit |
| `Archive/Transcripts/CopilotClosedLoop.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/CopilotClosedLoop.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/CopilotClosedLoop.md) | Explicit |
| `Archive/Transcripts/CopilotCognitiveSalvage.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/CopilotCognitiveSalvage.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/CopilotCognitiveSalvage.md) | Explicit |
| `Archive/Transcripts/Electronics-talking.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/Electronics-talking.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/Electronics-talking.md) | Explicit |
| `Archive/Transcripts/Energy-copilot-chat.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/Energy-copilot-chat.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/Energy-copilot-chat.md) | Explicit |
| `Archive/Transcripts/Energy-untested.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/Energy-untested.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/Energy-untested.md) | Explicit |
| `Archive/Transcripts/EthicalC-Copilot.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/EthicalC-Copilot.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/EthicalC-Copilot.md) | Explicit |
| `Archive/Transcripts/Gate2-afterupdate-review.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/Gate2-afterupdate-review.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/Gate2-afterupdate-review.md) | Explicit |
| `Archive/Transcripts/Gate2chat.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/Gate2chat.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/Gate2chat.md) | Explicit |
| `Archive/Transcripts/Gov-Copilot.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/Gov-Copilot.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/Gov-Copilot.md) | Explicit |
| `Archive/Transcripts/GrokGeckMaybeOverflowToo.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/GrokGeckMaybeOverflowToo.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/GrokGeckMaybeOverflowToo.md) | Explicit |
| `Archive/Transcripts/Pyrolysis_Cascade-Copilot.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/Pyrolysis_Cascade-Copilot.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/Pyrolysis_Cascade-Copilot.md) | Explicit |
| `Archive/Transcripts/Pyrolysis_Cascade-Grok.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/Pyrolysis_Cascade-Grok.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/Pyrolysis_Cascade-Grok.md) | Explicit |
| `Archive/README.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/README.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/README.md) | Explicit |
| `Archive/Rename_Registry.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Rename_Registry.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Rename_Registry.md) | Explicit |
| `Archive/Transcripts/RIP_GMP-Copilot.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Transcripts/RIP_GMP-Copilot.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Transcripts/RIP_GMP-Copilot.md) | Explicit |
| **Archive/Logs/ Layer** | | | |
| `Archive/Logs/AUDIT_HARNESS_CHANGELOG.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Logs/AUDIT_HARNESS_CHANGELOG.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Logs/AUDIT_HARNESS_CHANGELOG.md) | Explicit |
| `Archive/Logs/Auditor_Protocols_Logs.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Logs/Auditor_Protocols_Logs.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Logs/Auditor_Protocols_Logs.md) | Explicit |
| `Archive/Logs/Forge_Audit_Kit_Changelog.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Logs/Forge_Audit_Kit_Changelog.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Logs/Forge_Audit_Kit_Changelog.md) | Explicit |
| `Archive/Logs/Governance_Charter_Changelog.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Logs/Governance_Charter_Changelog.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Logs/Governance_Charter_Changelog.md) | Explicit |
| `Archive/Logs/Unknowns_Changelog.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Logs/Unknowns_Changelog.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Logs/Unknowns_Changelog.md) | Explicit |
| `Archive/Logs/Progress_Log_Changelog.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Logs/Progress_Log_Changelog.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Logs/Progress_Log_Changelog.md) | Explicit |
| `Archive/Logs/Discovery_Changelog.md` | [Raw](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Archive/Logs/Discovery_Changelog.md) | [Repo](https://github.com/ksarith/LazarusForge/blob/main/Archive/Logs/Discovery_Changelog.md) | Explicit |

*\* **Discovery.md Description Context:** The foundational navigational directory and behavior scope boundary map for the active working repository layer. It anchors incoming multi-agent analysis runs and human code reviews, defining active document maturity gates, dependency maps, and evolutionary path tracking parameters without cluttering data extraction queries with long textual strings.*

---

## File Template Backlink Requirement
To prevent dead-ends and maintain rigorous structural provenance, every markdown documentation asset within this repository must explicitly mount this navigation anchor block inside its upper context/metadata parameters:

```markdown
---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
---

```
## Maintenance Protocol
Update this file whenever:
 * A new file is added to the repository
 * A file is renamed (update entry; old name moves to Archive/Rename_Registry.md)
 * A file is retired to Archive/ (remove from active table; add Archive/ entry if needed)
Routing.md completeness is verified against Discovery.md structure map.
Discrepancies between the two are logged as pending corrections in Discovery.md.

**2026-08-08 rebuild:** This file's prior state (last genuinely updated
2026-06-06, 35 entries) had fallen far behind the actual repository —
missing most of Admin/, half of Architecture/, most of Challenges/ and
Tests/, all of Automation/'s nine scripts, CONTRIBUTING.md, and all five
`*_Scope_Map.md` files created 2026-08-07/08. Rebuilt from a direct
listing of every `.md`/`.py` file actually present in each folder, not
from memory or a prior table. Verified count at the time: 108 entries
across nine sections
(Root, Admin/, Architecture/, Operations/, Challenges/, Tests/,
Automation/, Archive/, Archive/Logs/) — the latter three are new
sections this file did not previously have. Archive/ and Archive/Logs/
are included for completeness even though their contents are prior-state
material, not active doctrine, per `Admin/Repository_Integrity_Protocol.md`'s
append-only rule for that directory. Human-directed, prompted by a direct
request to verify this file's actual state rather than trust a prior
description of it.

**2026-08-16 addition:** `Admin/Resolution_Methodology.md` registered (v0.6 active reference; was the sole active non-Archive Admin file missing from this table after Alpha.03).

**2026-08-09 addition:** three entries added — `Admin/Progress_Log.md` and
`Archive/Rename_Registry.md` (both new, migrated/created same day), plus
`Archive/Logs/Progress_Log_Changelog.md` (added once the first rotation
out of `Progress_Log.md` happened, same day it was created). A fourth,
`Archive/Logs/Discovery_Changelog.md`, added shortly after — Discovery.md's
own inline correction-note history had the same "no dedicated home"
problem as the Rename Registry, caught by direct human review of the
delivered patch. Verified current count: 112 entries. See `Discovery.md`'s
Pending Corrections PC-007 and `Progress_Log.md`'s own Resolution Log
for the full change this accompanies.
