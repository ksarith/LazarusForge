# Routing.md — LazarusForgeV0
**Canonical Navigation and Link Mapping Index.**
**Last updated: 2026-07-25**
## File Purpose
This file acts as the primary network lookup table for automated agents, continuous integration systems, and human collaborators. It provides programmatic access to the raw data payloads of the repository while enforcing bi-directional link traceability via the File Template.
Load this file when you need to fetch specific files by path.
Load Discovery.md when you need to understand scope relationships and routing logic.
These files are complementary — Routing.md owns *where*, Discovery.md owns *what and why*.
## Master Routing Map
| File Path / Name | Raw Content URL (LLM Context Target) | Repository URL (Human Target) | Backlink Requirement |
|---|---|---|---|
| **Root Layer** |  |  |  |
| `README.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/README.md | https://github.com/ksarith/LazarusForgeV0/blob/main/README.md | Explicit |
| `Discovery.md` * | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Discovery.md | Explicit |
| `Routing.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Routing.md | *Self-referential* |
| `Unknowns.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Unknowns.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Unknowns.md | Explicit |
| **Admin/ Layer** |  |  |  |
| `Admin/Governance_Charter.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Governance_Charter.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Governance_Charter.md | Explicit |
| `Admin/Ethical_Constraints.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ethical_Constraints.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Ethical_Constraints.md | Explicit |
| `Admin/Auditor_Protocols.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Auditor_Protocols.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Auditor_Protocols.md | Explicit |
| `Admin/Forge_Audit_Kit.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Forge_Audit_Kit.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Forge_Audit_Kit.md | Explicit |
| `Admin/Verification_Gates_LF.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Verification_Gates_LF.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Verification_Gates_LF.md | Explicit |
| `Admin/File_Template.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/File_Template.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/File_Template.md | Explicit |
| `Admin/Canonical_Terms.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Canonical_Terms.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Canonical_Terms.md | Explicit |
| `Admin/Engineer_Protocols.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Engineer_Protocols.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Engineer_Protocols.md | Explicit |
| `Admin/Safety_Protocols.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Safety_Protocols.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Safety_Protocols.md | Explicit |
| `Admin/Security_Protocols.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Security_Protocols.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Security_Protocols.md | Explicit |
| `Admin/Repository_Integrity_Protocol.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Repository_Integrity_Protocol.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Repository_Integrity_Protocol.md | Explicit |
| `Admin/Repository_Structure.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Repository_Structure.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Repository_Structure.md | Explicit |
| `Admin/Governance_Migration_Protocol.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Governance_Migration_Protocol.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Governance_Migration_Protocol.md | Explicit |
| `Admin/Ship_of_Theseus.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ship_of_Theseus.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Ship_of_Theseus.md | Explicit |
| `Admin/Trajectories.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Trajectories.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Trajectories.md | Explicit |
| `Admin/Economics.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Economics.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Economics.md | Explicit |
| `Admin/Environmental_Constraints.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Environmental_Constraints.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Environmental_Constraints.md | Explicit |
| `Admin/Experiments.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Experiments.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Experiments.md | Explicit |
| Admin/Nothingness Theorem | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Nothingness%20Theorem | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Nothingness%20Theorem | Explicit |
| Admin/Computational Institutional Reasoning | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Computational%20Institutional%20Reasoning | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Computational%20Institutional%20Reasoning | Explicit |
| `Admin/Autonomy_Divergence_Protocol.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Autonomy_Divergence_Protocol.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Admin/Autonomy_Divergence_Protocol.md | Explicit |
| **Automation/ Layer** |  |  |  |
| `Automation/AUDIT_HARNESS.py` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/AUDIT_HARNESS.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/AUDIT_HARNESS.py | N/A (Script) |
| `Automation/audit_lib.py` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/audit_lib.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/audit_lib.py | N/A (Script) |
| `Automation/Colab_cold_session.py` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/Colab_cold_session.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/Colab_cold_session.py | N/A (Script) |
| `Automation/Colab_Integrity.py` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/Colab_Integrity.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/Colab_Integrity.py | N/A (Script) |
| `Automation/Colab_Launcher.py` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/Colab_Launcher.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/Colab_Launcher.py | N/A (Script) |
| `Automation/cold_session_bundler.py` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/cold_session_bundler.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/cold_session_bundler.py | N/A (Script) |
| `Automation/integrity_check.py` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/integrity_check.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/integrity_check.py | N/A (Script) |
| `Automation/parser.py` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Automation/parser.py | https://github.com/ksarith/LazarusForgeV0/blob/main/Automation/parser.py | N/A (Script) |
| **Architecture/ Layer** |  |  |  |
| `Architecture/Forge_flow.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Forge_flow.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Forge_flow.md | Explicit |
| `Architecture/Components.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Components.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Components.md | Explicit |
| `Architecture/Facilities.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Facilities.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Facilities.md | Explicit |
| `Architecture/Geck_forge_seed.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Geck_forge_seed.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Geck_forge_seed.md | Explicit |
| `Architecture/Engineering.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Engineering.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Engineering.md | Explicit |
| `Architecture/Precision.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Precision.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Precision.md | Explicit |
| `Architecture/Mechanical_Structures.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Mechanical_Structures.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Mechanical_Structures.md | Explicit |
| `Architecture/Thermal_Systems.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Thermal_Systems.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Thermal_Systems.md | Explicit |
| `Architecture/Friction_Dynamics.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Friction_Dynamics.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Friction_Dynamics.md | Explicit |
| `Architecture/Chemistry.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Chemistry.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Chemistry.md | Explicit |
| `Architecture/Cognitive_Frameworks.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Cognitive_Frameworks.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Cognitive_Frameworks.md | Explicit |
| `Architecture/Forge_Net.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Forge_Net.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Architecture/Forge_Net.md | Explicit |
| **Operations/ Layer** |  |  |  |
| `Operations/Gate_01_Intake.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_01_Intake.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_01_Intake.md | Explicit |
| `Operations/Gate_02_Triage.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_02_Triage.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_02_Triage.md | Explicit |
| `Operations/Gate_03_Reduction.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_03_Reduction.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_03_Reduction.md | Explicit |
| `Operations/Gate_04_Separation_Mechanical.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_04_Separation_Mechanical.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_04_Separation_Mechanical.md | Explicit |
| `Operations/Gate_05_Separation_Thermal.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_05_Separation_Thermal.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_05_Separation_Thermal.md | Explicit |
| `Operations/Gate_06_Fabrication.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_06_Fabrication.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_06_Fabrication.md | Explicit |
| `Operations/Gate_07_Utilization.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_07_Utilization.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Gate_07_Utilization.md | Explicit |
| `Operations/Electronics.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Electronics.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Electronics.md | Explicit |
| `Operations/Energy.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Energy.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Energy.md | Explicit |
| `Operations/Air_Scrubber.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Air_Scrubber.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Air_Scrubber.md | Explicit |
| `Operations/Plastics.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Plastics.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Plastics.md | Explicit |
| `Operations/Woodworking.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Woodworking.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Operations/Woodworking.md | Explicit |
| **Tests/ Layer** |  |  |  |
| `Tests/Support_Raft.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Support_Raft.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Support_Raft.md | Explicit |
| `Tests/Leviathan_testing.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Leviathan_testing.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Leviathan_testing.md | Explicit |
| `Tests/Living_Waters.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Living_Waters.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Living_Waters.md | Explicit |
| `Tests/Trophic_Forge.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Trophic_Forge.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Trophic_Forge.md | Explicit |
| `Tests/Solar_Descent.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Solar_Descent.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Solar_Descent.md | Explicit |
| `Tests/Cognitive_Salvage_Layer.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Cognitive_Salvage_Layer.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Cognitive_Salvage_Layer.md | Explicit |
| `Tests/Hydrologic_Resource_Cascade.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Hydrologic_Resource_Cascade.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Hydrologic_Resource_Cascade.md | Explicit |
| `Tests/Chaos_Dynamics.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Chaos_Dynamics.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Tests/Chaos_Dynamics.md | Explicit |
| **Challenges/ Layer** |  |  |  |
| `Challenges/Water.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Water.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Water.md | Explicit |
| `Challenges/Biofouling.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Biofouling.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Biofouling.md | Explicit |
| `Challenges/Waste.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Waste.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Waste.md | Explicit |
| `Challenges/Planned_Obsolescence.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Planned_Obsolescence.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Planned_Obsolescence.md | Explicit |
| `Challenges/Critical_Minerals.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Critical_Minerals.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Critical_Minerals.md | Explicit |
| `Challenges/Emergence.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Emergence.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Emergence.md | Explicit |
| `Challenges/Energy_Scarcity.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Energy_Scarcity.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Energy_Scarcity.md | Explicit — added 2026-07-12 |
| `Challenges/Return_To_Eden.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Return_To_Eden.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Return_To_Eden.md | Explicit |
| `Challenges/Closed_Loop_Feedstock.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Challenges/Closed_Loop_Feedstock.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Challenges/Closed_Loop_Feedstock.md | Explicit |
| **Archive/ Layer** |  |  |  |
| `Archive/README.md` † | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/README.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/README.md | Explicit |
| **Archive/Logs/ Layer** |  |  |  |
| `Archive/Logs/Unknowns_Changelog.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/Logs/Unknowns_Changelog.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/Logs/Unknowns_Changelog.md | N/A (History) |
| `Archive/Logs/Governance_Charter_Changelog.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/Logs/Governance_Charter_Changelog.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/Logs/Governance_Charter_Changelog.md | N/A (History) |
| `Archive/Logs/Forge_Audit_Kit_Changelog.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/Logs/Forge_Audit_Kit_Changelog.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/Logs/Forge_Audit_Kit_Changelog.md | N/A (History) |
| `Archive/Logs/Auditor_Protocols_Logs.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/Logs/Auditor_Protocols_Logs.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/Logs/Auditor_Protocols_Logs.md | N/A (History) |
| `Archive/Logs/AUDIT_HARNESS_CHANGELOG.md` | https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Archive/Logs/AUDIT_HARNESS_CHANGELOG.md | https://github.com/ksarith/LazarusForgeV0/blob/main/Archive/Logs/AUDIT_HARNESS_CHANGELOG.md | N/A (History) |
*Discovery.md Description Context: The foundational navigational directory and behavior scope boundary map for the active working repository layer. It anchors incoming multi-agent analysis runs and human code reviews, defining active document maturity gates, dependency maps, and evolutionary path tracking parameters without cluttering data extraction queries with long textual strings.*
## File Template Backlink Requirement
To prevent dead-ends and maintain rigorous structural provenance, every markdown documentation asset within this repository must explicitly mount this navigation anchor block inside its upper context/metadata parameters:
```markdown
---
## Navigation Anchors
* **Context Core:** https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md
* **Network Routing:** https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md
---

```
## Maintenance Protocol
Update this file whenever:
 * A new file is added to the repository
 * A file is renamed (update entry; old name moves to Discovery.md Rename Registry)
 * A file is retired to Archive/ (remove from active table; add Archive/ entry if needed)
Routing.md completeness is verified against Discovery.md structure map.
Discrepancies between the two are logged as pending corrections in Discovery.md.
**† Note on Archive/README.md basename collision:** `Archive/README.md` shares its basename with the root `README.md`. `parse_routing()` builds its registry by basename, first match wins — the root file is listed first in this table, so the short name `README.md` always resolves to it; `Archive/README.md` is only reachable by its full path, never by short name, even now that it's registered. This is a real, standing limitation, not a placeholder to be resolved by editing this file further — any tooling or agent needing `Archive/README.md` specifically should reference the full path.

**Note on non-extension Admin/ files:** Admin/Nothingness Theorem and Admin/Computational Institutional Reasoning are intentionally filed without .md extensions and contain spaces in their filenames (URL-encoded as %20 in raw/repo links). Nothingness Theorem is a philosophical substrate document (Admin/, intentionally functionless per its own doctrine); it carries a minimal Tier 0 File State sidecar sufficient for Phase 1 Ethical Anchor verification but is exempt from operational promotion gates. Computational Institutional Reasoning is the formal theoretical paper containing the axioms, theorems, and Verification Algebra that back CF-004, AP-006, and related epistemic-debt doctrine in Unknowns.md and Auditor_Protocols.md; it carries a full standard File State sidecar as of v0.16 (2026-06-30) and is subject to standard promotion gate tracking. Neither file carries a .md extension; both resolve via hardcoded ALIASES entries in Automation/AUDIT_HARNESS.py rather than through the dynamic _parse_routing() registry builder.


**2026-07-25 update:** Converted table URL structures from Markdown text hyperlinking ([Raw]/[Repo]) to bare active URLs across all entries. Added direct registration for new automation scripts (parser.py, cold_session_bundler.py, integrity_check.py, audit_lib.py, Colab_cold_session.py, Colab_Launcher.py, Colab_Integrity.py).

**2026-07-25 correction (same day):** The URL-format edit above dropped the backtick-quoting around every File Path / Name cell. `Automation/audit_lib.py`'s `parse_routing()` matches only backtick-quoted paths ending in `.md`/`.py` (see its docstring) — with the quoting gone, dynamic registry parsing returned zero entries, silently collapsing `AUDIT_HARNESS.py`'s `FILE_REGISTRY` down to just the `ALIASES` dict on every run. Confirmed by running `parse_routing()` directly against this file pre-fix (0 entries) and post-fix (77 entries). Backtick-quoting restored across all 77 rows; bare-URL columns from the earlier edit kept as-is since they don't affect parsing either way. Also fixed a malformed footnote (`** **...*`) below the table left over from the same edit. Recommend a `parse_routing()` smoke test become a standing pre-commit or first-cell check for this file going forward, given it has now broken silently twice.
