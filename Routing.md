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
| README.md | Raw | Repo | Explicit |
| Discovery.md * | Raw | Repo | Explicit |
| Routing.md | Raw | Repo | *Self-referential* |
| Unknowns.md | Raw | Repo | Explicit |
| **Admin/ Layer** |  |  |  |
| Admin/Governance_Charter.md | Raw | Repo | Explicit |
| Admin/Ethical_Constraints.md | Raw | Repo | Explicit |
| Admin/Auditor_Protocols.md | Raw | Repo | Explicit |
| Admin/Forge_Audit_Kit.md | Raw | Repo | Explicit |
| Admin/Verification_Gates_LF.md | Raw | Repo | Explicit |
| Admin/File_Template.md | Raw | Repo | Explicit |
| Admin/Canonical_Terms.md | Raw | Repo | Explicit |
| Admin/Engineer_Protocols.md | Raw | Repo | Explicit |
| Admin/Safety_Protocols.md | Raw | Repo | Explicit |
| Admin/Security_Protocols.md | Raw | Repo | Explicit |
| Admin/Repository_Integrity_Protocol.md | Raw | Repo | Explicit |
| Admin/Repository_Structure.md | Raw | Repo | Explicit |
| Admin/Governance_Migration_Protocol.md | Raw | Repo | Explicit |
| Admin/Ship_of_Theseus.md | Raw | Repo | Explicit |
| Admin/Trajectories.md | Raw | Repo | Explicit |
| Admin/Economics.md | Raw | Repo | Explicit |
| Admin/Environmental_Constraints.md | Raw | Repo | Explicit |
| Admin/Experiments.md | Raw | Repo | Explicit |
| Admin/Nothingness Theorem | Raw | Repo | Explicit |
| Admin/Computational Institutional Reasoning | Raw | Repo | Explicit |
| Admin/Autonomy_Divergence_Protocol.md | Raw | Repo | Explicit |
| **Automation/ Layer** |  |  |  |
| Automation/AUDIT_HARNESS.py | Raw | Repo | N/A (Script) |
| Automation/audit_lib.py | Raw | Repo | N/A (Script) |
| Automation/Colab_cold_session.py | Raw | Repo | N/A (Script) |
| Automation/Colab_Integrity.py | Raw | Repo | N/A (Script) |
| Automation/Colab_Launcher.py | Raw | Repo | N/A (Script) |
| Automation/cold_session_bundler.py | Raw | Repo | N/A (Script) |
| Automation/integrity_check.py | Raw | Repo | N/A (Script) |
| Automation/parser.py | Raw | Repo | N/A (Script) |
| **Architecture/ Layer** |  |  |  |
| Architecture/Forge_flow.md | Raw | Repo | Explicit |
| Architecture/Components.md | Raw | Repo | Explicit |
| Architecture/Facilities.md | Raw | Repo | Explicit |
| Architecture/Geck_forge_seed.md | Raw | Repo | Explicit |
| Architecture/Engineering.md | Raw | Repo | Explicit |
| Architecture/Precision.md | Raw | Repo | Explicit |
| Architecture/Mechanical_Structures.md | Raw | Repo | Explicit |
| Architecture/Thermal_Systems.md | Raw | Repo | Explicit |
| Architecture/Friction_Dynamics.md | Raw | Repo | Explicit |
| Architecture/Chemistry.md | Raw | Repo | Explicit |
| Architecture/Cognitive_Frameworks.md | Raw | Repo | Explicit |
| Architecture/Forge_Net.md | Raw | Repo | Explicit |
| **Operations/ Layer** |  |  |  |
| Operations/Gate_01_Intake.md | Raw | Repo | Explicit |
| Operations/Gate_02_Triage.md | Raw | Repo | Explicit |
| Operations/Gate_03_Reduction.md | Raw | Repo | Explicit |
| Operations/Gate_04_Separation_Mechanical.md | Raw | Repo | Explicit |
| Operations/Gate_05_Separation_Thermal.md | Raw | Repo | Explicit |
| Operations/Gate_06_Fabrication.md | Raw | Repo | Explicit |
| Operations/Gate_07_Utilization.md | Raw | Repo | Explicit |
| Operations/Electronics.md | Raw | Repo | Explicit |
| Operations/Energy.md | Raw | Repo | Explicit |
| Operations/Air_Scrubber.md | Raw | Repo | Explicit |
| Operations/Plastics.md | Raw | Repo | Explicit |
| Operations/Woodworking.md | Raw | Repo | Explicit |
| **Tests/ Layer** |  |  |  |
| Tests/Support_Raft.md | Raw | Repo | Explicit |
| Tests/Leviathan_testing.md | Raw | Repo | Explicit |
| Tests/Living_Waters.md | Raw | Repo | Explicit |
| Tests/Trophic_Forge.md | Raw | Repo | Explicit |
| Tests/Solar_Descent.md | Raw | Repo | Explicit |
| Tests/Cognitive_Salvage_Layer.md | Raw | Repo | Explicit |
| Tests/Hydrologic_Resource_Cascade.md | Raw | Repo | Explicit |
| Tests/Chaos_Dynamics.md | Raw | Repo | Explicit |
| **Challenges/ Layer** |  |  |  |
| Challenges/Water.md | Raw | Repo | Explicit |
| Challenges/Biofouling.md | Raw | Repo | Explicit |
| Challenges/Waste.md | Raw | Repo | Explicit |
| Challenges/Planned_Obsolescence.md | Raw | Repo | Explicit |
| Challenges/Critical_Minerals.md | Raw | Repo | Explicit |
| Challenges/Emergence.md | Raw | Repo | Explicit |
| Challenges/Energy_Scarcity.md | Raw | Repo | Explicit — added 2026-07-12 |
| Challenges/Return_To_Eden.md | Raw | Repo | Explicit |
| Challenges/Closed_Loop_Feedstock.md | Raw | Repo | Explicit |
| **Archive/Logs/ Layer** |  |  |  |
| Archive/Logs/Unknowns_Changelog.md | Raw | Repo | N/A (History) |
| Archive/Logs/Governance_Charter_Changelog.md | Raw | Repo | N/A (History) |
| Archive/Logs/Forge_Audit_Kit_Changelog.md | Raw | Repo | N/A (History) |
| Archive/Logs/Auditor_Protocols_Logs.md | Raw | Repo | N/A (History) |
| Archive/Logs/AUDIT_HARNESS_CHANGELOG.md | Raw | Repo | N/A (History) |
** **Discovery.md Description Context:** The foundational navigational directory and behavior scope boundary map for the active working repository layer. It anchors incoming multi-agent analysis runs and human code reviews, defining active document maturity gates, dependency maps, and evolutionary path tracking parameters without cluttering data extraction queries with long textual strings.*
## File Template Backlink Requirement
To prevent dead-ends and maintain rigorous structural provenance, every markdown documentation asset within this repository must explicitly mount this navigation anchor block inside its upper context/metadata parameters:
```markdown
---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)
---

```
## Maintenance Protocol
Update this file whenever:
 * A new file is added to the repository
 * A file is renamed (update entry; old name moves to Discovery.md Rename Registry)
 * A file is retired to Archive/ (remove from active table; add Archive/ entry if needed)
Routing.md completeness is verified against Discovery.md structure map.
Discrepancies between the two are logged as pending corrections in Discovery.md.
**Note on non-extension Admin/ files:** Admin/Nothingness Theorem and Admin/Computational Institutional Reasoning are intentionally filed without .md extensions and contain spaces in their filenames (URL-encoded as %20 in raw/repo links). Nothingness Theorem is a philosophical substrate document (Admin/, intentionally functionless per its own doctrine); it carries a minimal Tier 0 File State sidecar sufficient for Phase 1 Ethical Anchor verification but is exempt from operational promotion gates. Computational Institutional Reasoning is the formal theoretical paper containing the axioms, theorems, and Verification Algebra that back CF-004, AP-006, and related epistemic-debt doctrine in Unknowns.md and Auditor_Protocols.md; it carries a full standard File State sidecar as of v0.16 (2026-06-30) and is subject to standard promotion gate tracking. Neither file carries a .md extension; both resolve via hardcoded ALIASES entries in Automation/AUDIT_HARNESS.py rather than through the dynamic _parse_routing() registry builder.
**2026-07-04 addition:** Tests/Chaos_Dynamics.md registered — created same date, resolution vehicle for EN-005 (see Architecture/Engineering.md sidecar and Discovery.md Scope Map for status caveats). Its Backlink Requirement is marked **Missing**, not Explicit — the file does not yet carry the mandatory Navigation Anchors block. This is the only row in this table currently in that state; treat as a standing pending correction until patched.
**2026-07-06 correction:** Challenges/Closed_Loop_Feedstock.md row's Repository URL was committed as a broken [Repo] link with no target — the only malformed link in this table. Corrected to a working link matching the standard pattern. File confirmed to carry the Navigation Anchors block (Backlink Requirement: Explicit) as of its v0.5.0 revision; cross-reference Unknowns.md v4.12 PC-005 for this file's remaining registration gaps in Discovery.md and Automation/AUDIT_HARNESS.py.
**2026-07-19 correction:** Unknowns_Changelog.md (split from Unknowns.md this date, full version history) and Admin/Autonomy_Divergence_Protocol.md (drafted this date, PROPOSED NOT RATIFIED — governance content, not yet ratified) registered. Unknowns_Changelog.md follows the Admin/AUDIT_HARNESS_CHANGELOG.md / Admin/Forge_Audit_Kit_Changelog.md precedent — N/A (History), no Discovery.md entry, matching how those two files were also left unregistered there. Admin/Autonomy_Divergence_Protocol.md is real content, not a changelog, and gets a full Discovery.md entry as well.
**2026-07-16 correction:** Admin/AUDIT_HARNESS_CHANGELOG.md and Admin/Forge_Audit_Kit_Changelog.md registered — both created 2026-07-14, actively cited from multiple files (Admin/Forge_Audit_Kit.md, Admin/Auditor_Protocols.md), never added here — surfaced by a self-audit of Admin/Auditor_Protocols.md, logged as that file's AP-023. Admin/unknown_cycles.json (also created 2026-07-14) is deliberately **not** registered here: Automation/AUDIT_HARNESS.py v15 (2026-07-16) removed the fetch call that used it — aging is now computed from each unknown's own First Logged date rather than a separate cycle-number map — so the file is orphaned, not a live cross-reference. Left in the repository as history per the same shelving convention as a retired kit version, not deleted.
**2026-07-21 correction:** AUDIT_HARNESS.py relocated from Admin/ to Automation/ — the new Automation/ subsystem's canonical home for repository tooling. Row above updated to match; the non-extension-files note above it was also citing the old Admin/-prefixed path for its ALIASES-resolution behavior and has been corrected. Discovery.md's structure-tree entry and the harness's own FALLBACK_REGISTRY self-reference ("AUDIT_HARNESS.py": "...") were updated in the same pass. Admin/AUDIT_HARNESS.py no longer exists as of this date — treat any remaining Admin/AUDIT_HARNESS.py citation elsewhere in the repository (roughly a dozen prose references in doctrine files, none of them live/resolved links) as stale until independently corrected; none of them affect this file's own registry parsing.
**2026-07-21 correction (unknown_cycles.json):** the 2026-07-16 note above said Admin/unknown_cycles.json was "left in the repository as history... not deleted." That has since changed — the file has been removed, judged unnecessary now that Automation/AUDIT_HARNESS.py v15 computes aging directly from each unknown's First Logged date rather than a separate cycle-number map. The 07-16 note is left above unedited as an accurate record of the decision at the time; this entry supersedes only its final clause. AUDIT_HARNESS.py's ALIASES entry for "unknown_cycles.json" should be removed as dead code pointing at a now-nonexistent file.
**2026-07-22 reorganization:** Reorganized repository changelogs and audit logs into a dedicated Archive/Logs/ layer to maintain core working layer cleanliness. Updated table entries for Unknowns_Changelog.md, Forge_Audit_Kit_Changelog.md, and AUDIT_HARNESS_CHANGELOG.md to reflect their new paths under Archive/Logs/. Registered newly created log archives Governance_Charter_Changelog.md and Auditor_Protocols_Logs.md.
**2026-07-25 addition:** Fully registered missing automation tools (parser.py, cold_session_bundler.py, integrity_check.py, audit_lib.py, Colab_cold_session.py, Colab_Launcher.py, Colab_Integrity.py) under the Automation/ section with active Raw and Repository URLs. Updated all Archive/Logs/ entries with explicit hyperlink text and target pairs.
