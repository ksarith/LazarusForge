# Routing.md — LazarusForgeV0
**Canonical Navigation and Link Mapping Index.**
**Last updated: 2026-07-25 (v2026-07-25 Schema Overhaul — corrected)**

## File Purpose

This file acts as the primary network lookup table for automated agents, continuous integration systems, and human collaborators. It provides programmatic access to the raw data payloads of the repository while enforcing bi-directional link traceability via the File Template.

* **Load this file** when you need to fetch specific files by path or resolve payload URLs.
* **Load Discovery.md** when you need to understand scope relationships and routing logic.
* *These files are complementary — Routing.md owns **where**, Discovery.md owns **what and why**.*

## Master Routing Map

| File Path / Name | Asset Type | Raw Content Target (LLM Context) | Repository Target (Human View) | Backlink Requirement |
|---|---|---|---|---|
| **Root Layer** |  |  |  |  |
| `README.md` | Core Index | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/README.md | https://github.com/ksarith/LazarusForgeV0/blob/main/README.md | Explicit |
| `Discovery.md` * | Context Directory | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Discovery.md | Explicit |
| `Routing.md` | Routing Registry | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Routing.md | *Self-referential* |
| `Unknowns.md` | Epistemic Ledger | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Unknowns.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Unknowns.md | Explicit |
| **Admin/ Layer** |  |  |  |  |
| `Admin/Governance_Charter.md` | Governance Charter | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Governance_Charter.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Governance_Charter.md | Explicit |
| `Admin/Ethical_Constraints.md` | Ethical Constraint | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ethical_Constraints.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Ethical_Constraints.md | Explicit |
| `Admin/Auditor_Protocols.md` | Audit Protocol | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Auditor_Protocols.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Auditor_Protocols.md | Explicit |
| `Admin/Forge_Audit_Kit.md` | Audit Specification | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Forge_Audit_Kit.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Forge_Audit_Kit.md | Explicit |
| `Admin/Verification_Gates_LF.md` | Gate Specification | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Verification_Gates_LF.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Verification_Gates_LF.md | Explicit |
| `Admin/File_Template.md` | Schema Template | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/File_Template.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/File_Template.md | Explicit |
| `Admin/Canonical_Terms.md` | Taxonomy / Glossary | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Canonical_Terms.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Canonical_Terms.md | Explicit |
| `Admin/Engineer_Protocols.md` | Engineering Protocol | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Engineer_Protocols.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Engineer_Protocols.md | Explicit |
| `Admin/Safety_Protocols.md` | Safety Protocol | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Safety_Protocols.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Safety_Protocols.md | Explicit |
| `Admin/Security_Protocols.md` | Security Protocol | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Security_Protocols.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Security_Protocols.md | Explicit |
| `Admin/Repository_Integrity_Protocol.md` | Integrity Protocol | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Repository_Integrity_Protocol.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Repository_Integrity_Protocol.md | Explicit |
| `Admin/Repository_Structure.md` | Structural Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Repository_Structure.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Repository_Structure.md | Explicit |
| `Admin/Governance_Migration_Protocol.md` | Migration Protocol | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Governance_Migration_Protocol.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Governance_Migration_Protocol.md | Explicit |
| `Admin/Ship_of_Theseus.md` | Philosophy Anchor | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ship_of_Theseus.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Ship_of_Theseus.md | Explicit |
| `Admin/Trajectories.md` | Trajectory Map | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Trajectories.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Trajectories.md | Explicit |
| `Admin/Economics.md` | Economic Model | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Economics.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Economics.md | Explicit |
| `Admin/Environmental_Constraints.md` | Constraint Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Environmental_Constraints.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Environmental_Constraints.md | Explicit |
| `Admin/Experiments.md` | Experiment Registry | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Experiments.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Experiments.md | Explicit |
| Admin/Nothingness Theorem | Substrate Theory | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Nothingness%20Theorem | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Nothingness%20Theorem | Explicit |
| Admin/Computational Institutional Reasoning | Formal Theory Paper | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Computational%20Institutional%20Reasoning | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Computational%20Institutional%20Reasoning | Explicit |
| `Admin/Autonomy_Divergence_Protocol.md` | Governance Draft | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Autonomy_Divergence_Protocol.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Autonomy_Divergence_Protocol.md | Explicit |
| **Automation/ Layer** |  |  |  |  |
| `Automation/AUDIT_HARNESS.py` | Executable Script | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/AUDIT_HARNESS.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/AUDIT_HARNESS.py | N/A (Script) |
| `Automation/parser.py` | Executable Script | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/parser.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/parser.py | N/A (Script) |
| `Automation/audit_lib.py` | Shared Library | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/audit_lib.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/audit_lib.py | N/A (Library) |
| `Automation/integrity_check.py` | Executable Script | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/integrity_check.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/integrity_check.py | N/A (Script) |
| `Automation/cold_session_bundler.py` | Executable Script | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/cold_session_bundler.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/cold_session_bundler.py | N/A (Script) |
| `Automation/Colab_cold_session.py` | Session Launcher | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/Colab_cold_session.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/Colab_cold_session.py | N/A (Launcher) |
| `Automation/Colab_Launcher.py` | Session Launcher | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/Colab_Launcher.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/Colab_Launcher.py | N/A (Launcher) |
| `Automation/Colab_Integrity.py` | Session Launcher | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/Colab_Integrity.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/Colab_Integrity.py | N/A (Launcher) |
| **Architecture/ Layer** |  |  |  |  |
| `Architecture/Forge_flow.md` | System Flow | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Forge_flow.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Forge_flow.md | Explicit |
| `Architecture/Components.md` | Component Registry | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Components.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Components.md | Explicit |
| `Architecture/Facilities.md` | Facility Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Facilities.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Facilities.md | Explicit |
| `Architecture/Geck_forge_seed.md` | Seed Architecture | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Geck_forge_seed.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Geck_forge_seed.md | Explicit |
| `Architecture/Engineering.md` | Engineering Doctrine | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Engineering.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Engineering.md | Explicit |
| `Architecture/Precision.md` | Precision Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Precision.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Precision.md | Explicit |
| `Architecture/Mechanical_Structures.md` | Mechanical Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Mechanical_Structures.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Mechanical_Structures.md | Explicit |
| `Architecture/Thermal_Systems.md` | Thermal Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Thermal_Systems.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Thermal_Systems.md | Explicit |
| `Architecture/Friction_Dynamics.md` | Tribology Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Friction_Dynamics.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Friction_Dynamics.md | Explicit |
| `Architecture/Chemistry.md` | Chemical Process | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Chemistry.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Chemistry.md | Explicit |
| `Architecture/Cognitive_Frameworks.md` | Cognitive Model | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Cognitive_Frameworks.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Cognitive_Frameworks.md | Explicit |
| `Architecture/Forge_Net.md` | Network Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Forge_Net.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Forge_Net.md | Explicit |
| **Operations/ Layer** |  |  |  |  |
| `Operations/Gate_01_Intake.md` | Operational Gate | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_01_Intake.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_01_Intake.md | Explicit |
| `Operations/Gate_02_Triage.md` | Operational Gate | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_02_Triage.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_02_Triage.md | Explicit |
| `Operations/Gate_03_Reduction.md` | Operational Gate | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_03_Reduction.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_03_Reduction.md | Explicit |
| `Operations/Gate_04_Separation_Mechanical.md` | Operational Gate | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_04_Separation_Mechanical.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_04_Separation_Mechanical.md | Explicit |
| `Operations/Gate_05_Separation_Thermal.md` | Operational Gate | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_05_Separation_Thermal.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_05_Separation_Thermal.md | Explicit |
| `Operations/Gate_06_Fabrication.md` | Operational Gate | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_06_Fabrication.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_06_Fabrication.md | Explicit |
| `Operations/Gate_07_Utilization.md` | Operational Gate | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_07_Utilization.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_07_Utilization.md | Explicit |
| `Operations/Electronics.md` | Domain Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Electronics.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Electronics.md | Explicit |
| `Operations/Energy.md` | Domain Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Energy.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Energy.md | Explicit |
| `Operations/Air_Scrubber.md` | Domain Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Air_Scrubber.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Air_Scrubber.md | Explicit |
| `Operations/Plastics.md` | Domain Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Plastics.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Plastics.md | Explicit |
| `Operations/Woodworking.md` | Domain Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Woodworking.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Woodworking.md | Explicit |
| **Tests/ Layer** |  |  |  |  |
| `Tests/Support_Raft.md` | Test Suite | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Support_Raft.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Support_Raft.md | Explicit |
| `Tests/Leviathan_testing.md` | Test Suite | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Leviathan_testing.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Leviathan_testing.md | Explicit |
| `Tests/Living_Waters.md` | Test Suite | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Living_Waters.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Living_Waters.md | Explicit |
| `Tests/Trophic_Forge.md` | Test Suite | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Trophic_Forge.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Trophic_Forge.md | Explicit |
| `Tests/Solar_Descent.md` | Test Suite | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Solar_Descent.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Solar_Descent.md | Explicit |
| `Tests/Cognitive_Salvage_Layer.md` | Test Suite | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Cognitive_Salvage_Layer.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Cognitive_Salvage_Layer.md | Explicit |
| `Tests/Hydrologic_Resource_Cascade.md` | Test Suite | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Hydrologic_Resource_Cascade.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Hydrologic_Resource_Cascade.md | Explicit |
| `Tests/Chaos_Dynamics.md` | Test Suite | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Chaos_Dynamics.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Chaos_Dynamics.md | Explicit |
| **Challenges/ Layer** |  |  |  |  |
| `Challenges/Water.md` | Challenge Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Water.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Water.md | Explicit |
| `Challenges/Biofouling.md` | Challenge Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Biofouling.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Biofouling.md | Explicit |
| `Challenges/Waste.md` | Challenge Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Waste.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Waste.md | Explicit |
| `Challenges/Planned_Obsolescence.md` | Challenge Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Planned_Obsolescence.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Planned_Obsolescence.md | Explicit |
| `Challenges/Critical_Minerals.md` | Challenge Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Critical_Minerals.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Critical_Minerals.md | Explicit |
| `Challenges/Emergence.md` | Challenge Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Emergence.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Emergence.md | Explicit |
| `Challenges/Energy_Scarcity.md` | Challenge Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Energy_Scarcity.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Energy_Scarcity.md | Explicit |
| `Challenges/Return_To_Eden.md` | Challenge Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Return_To_Eden.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Return_To_Eden.md | Explicit |
| `Challenges/Closed_Loop_Feedstock.md` | Challenge Spec | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Closed_Loop_Feedstock.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Closed_Loop_Feedstock.md | Explicit |
| **Archive/Logs/ Layer** |  |  |  |  |
| `Archive/Logs/Unknowns_Changelog.md` | Historical Log | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/Logs/Unknowns_Changelog.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/Logs/Unknowns_Changelog.md | N/A (History) |
| `Archive/Logs/Governance_Charter_Changelog.md` | Historical Log | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/Logs/Governance_Charter_Changelog.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/Logs/Governance_Charter_Changelog.md | N/A (History) |
| `Archive/Logs/Forge_Audit_Kit_Changelog.md` | Historical Log | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/Logs/Forge_Audit_Kit_Changelog.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/Logs/Forge_Audit_Kit_Changelog.md | N/A (History) |
| `Archive/Logs/Auditor_Protocols_Logs.md` | Historical Log | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/Logs/Auditor_Protocols_Logs.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/Logs/Auditor_Protocols_Logs.md | N/A (History) |
| `Archive/Logs/AUDIT_HARNESS_CHANGELOG.md` | Historical Log | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/Logs/AUDIT_HARNESS_CHANGELOG.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/Logs/AUDIT_HARNESS_CHANGELOG.md | N/A (History) |

** **Discovery.md Description Context:** The foundational navigational directory and behavior scope boundary map for the active working repository layer. It anchors incoming multi-agent analysis runs and human code reviews, defining active document maturity gates, dependency maps, and evolutionary path tracking parameters without cluttering data extraction queries with long textual strings.*

## File Template Backlink Requirement

To prevent dead-ends and maintain rigorous structural provenance, every markdown documentation asset within this repository must explicitly mount this navigation anchor block inside its upper context/metadata parameters:

```markdown
---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)
---
