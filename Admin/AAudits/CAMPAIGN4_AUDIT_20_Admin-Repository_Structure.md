# CAMPAIGN4_AUDIT_20 — Admin/Repository_Structure.md (adversarial findings-only pseudo-audit)

**Campaign 4 sweep, artifact 20 of 34. Deposited 2026-11-10 under the kickoff's standing rules: findings-only per PKC-020 — this artifact advances no Last Audit, Last Reviewed, version, Status, Spec Gate, or unknown on any file; conversion to an audit of record is the human's alone (MAINT-26 / AP-032).** Seat: Vibe (GLM 5.3 Flash architecture). Adjacency disclosed: the file's own File State records four prior Vibe-line passes (2026-10-27, 2026-10-28, 2026-11-05, 2026-11-07); per the kickoff's standing disclosure, prior Vibe-line maintenance is treated as third-party content here, and this pass is itself non-independent with respect to it. First sweep pass executed after the MAINT-109 parallel-composition clobber repair; the canonical chain (kickoff addenda 1–18) verified intact at compose.

## File state as found (live fetch, LF main `03f15726`)

- `Admin/Repository_Structure.md` ("RS"), Status **Exploration**, Body Stability Transitional, Spec Gates 0/6, Open Unknowns 0, Active Disputes 0, Highest Risk Low — 37,588 chars / 617 lines, fetched complete, SHA-256 `f0f7ad1f5d5c85651a34d9bb8bea40964f6c59f57a63d838521b043ab77b619a`.
- No current version string anywhere in the file (same shape as the Security_Protocols/Safety_Protocols/Engineer_Protocols audits).
- Sidecar: in-file (`Auditor Notes & Unknowns`, Sidecar Link `#auditor-notes--unknowns`), three entries RS-001/002/003, all Resolved.

## Findings

- **F-RS-1 WARNING (wrong-home audit-report citation; relocation-repair-miss, Pattern 2 instance 16):** the Resolution Log's 2026-10-28 pseudo-audit-ledger entry routes its report to `Archive/Audits/AUDIT_12_Admin-Repository_Structure.md`; the live report sits at `Admin/AAudits/AUDIT_12_Admin-Repository_Structure.md` (live listings probed at both homes: Archive/Audits/ holds no Repository_Structure report of any name). The entry predates the 2026-10-30 creation of `Admin/AAudits/` (MAINT-29), so the shape is the established relocation-repair-miss class — the report was moved into the per-folder audit home and this citation was never repointed. Same class as F-FAK-2 (instance 10) and F-EP-4 (instance 11); instance numbering continues the canonical count (15 through AUDIT_19).
- **F-RS-2 WARNING (stale operative Automation/ counts, two places; the "described in" half doubly stale):** §I's RS-001 retroactive-note table says "`.py` | `Automation/` (eleven files, described in `Automation/README.md`)" and RS-001's 2026-10-23 refresh says "`Automation/` now holds eleven `.py` files and one `.zip`" — the live directory holds **twelve** `.py` files plus one `.zip` (listing probed). Compounding: the live `Automation/README.md` table describes only **ten** of the twelve (`Candidate3_Transient_Index_Colab_hybrid.py` and `coverage_ledger_regen.py` appear in no README row), so the "described in `Automation/README.md`" half of the claim is stale against the README itself, not just the directory.
- **F-RS-3 WARNING (self-identical example voids the acronym rule's only demonstration; TWGW candidate):** §I Casing Standard, Rules list: "Acronyms treated as single words: `Air_Scrubber.md` not `Air_Scrubber.md`" — both strings are character-identical, so the example cannot demonstrate whatever contrast was intended (the non-underscored or differently-cased form one side was meant to carry is missing). A concrete defect in operative naming doctrine with a usable correction; flagged as a TWGW candidate per the 2026-11-07 addendum discipline.
- **F-RS-4 NOTE (MAINT-56-retired File State rows still carried; one-directional non-conformance):** the File State block carries the Last Audit and Auditor rows that File_Template's own amendment retired ("Amended 2026-11-04, MAINT-56: Last Audit and Auditor are retired fields"; Pattern A check C4 retired with them) — the same first half as F-FAK-1. The second half is absent here: Body Stability, Active Disputes and Highest Risk are all present and correctly filled. Cosmetic cell artifacts disclosed: the Last Audit cell opens "|2026-11-07" without the separator space, and a Prior chain carries a double space.
- **F-RS-5 NOTE (RS-001 pre-resolution residue under Resolved status; Pattern 5 shape):** RS-001's Description still asserts "The review procedure itself is not yet defined" and its Resolution Path still ends "Defer until a concrete case arises" — both describe the pre-2026-10-25 state and sit unannotated directly above the resolution narrative that supersedes them. Contrast the file's own PKC-023 annotation discipline applied elsewhere (§I, §VI); the residue here carries no dated marker.
- **F-RS-6 NOTE (bare colliding-ID citations, three-tier check):** "AUDIT_12 F2" appears twice (File Purpose and the Resolution Log's 2026-10-28 entry) with no home or epoch qualifier. AUDIT_12 is now a colliding ID across campaign numbering — this campaign's artifact 12 is `CAMPAIGN4_AUDIT_12` (Forge_Audit_Kit.md), and the cited report is the 2026-10-27 Repository_Structure pseudo-audit; a reader routing the bare ID from this file lands on the wrong artifact.
- **F-RS-7 NOTE (drift-indicator near-trip, retro-closed):** the file's own trigger "A new folder is created without a RS decision entry in this file" fired at creation for the per-folder Log/Audit subfolders — `Admin/ALogs/` and `Admin/AAudits/` (both 2026-10-30, MAINT-29) and the content folders' audit subfolders (`Operations/OAudits/`, `Architecture/RAudits/`, `Tests/TAudits/`, all live) — while RS's only related entry is the 2026-11-05 §II generic convention note (MAINT-63, human-ratified MAINT-62 §3.7). The generic note now covers the class and the placement was human-ratified, so this is disclosed as a near-trip closed retroactively, not an open violation.

**Aging Rule:** vacuous this pass — zero open unknowns (the tenth no-trip control case of the campaign; no new systemic instance). **Compound Drift Rule:** did not fire — none of the file's own listed indicators is in a firing state (F-RS-2/F-RS-3 are staleness/defect findings against the body, not the listed triggers; F-RS-7 is the retro-closed near-trip).

## Checks 1–11 record and fabrication probes

1. **Sidecar count parity:** File State Open Unknowns 0 = live recount of the in-file sidecar (three entries, all Resolved) = 0. Clean.
2. **Header vs body:** no version string claimed or present; nothing to reconcile. Clean.
3. **Log vs body:** the Resolution Log's 2026-10-28 claims verified live in the body (the ownership-reconciliation narration is in File Purpose; the §II subfolder-convention note is the 2026-11-05 MAINT-63 annotation). One citation defect: F-RS-1.
4. **Scope Boundary re-derivation:** all six DOES-NOT-DEFINE routing targets exist live (`Admin/File_Template.md`, `Admin/Governance_Charter.md`, `Discovery.md`, `Archive/Rename_Registry.md`, `Admin/Governance_Migration_Protocol.md`, `Admin/Repository_Integrity_Protocol.md`). Clean.
5. **Cross-references (existence + mirrored claims both directions):** Navigation anchors resolve (Discovery.md, Routing.md live at root). `Archive/Rename_Registry.md` live; its Forge_flow row matches RS-002's resolution claim in substance ("Forge_flow.md | Forge_flow.md | Architecture/ | Resolved — RS-002 2026-06-11 (accepted outlier; casing retained)"). `Architecture/Forge_flow.md` carries the 2026-06-11 RS-002 resolution log. `Unknowns.md`'s Repository Structure section excludes RS-001/002/003 per Size Management Rule 2 with Resolved dates matching the sidecar (2026-10-25 / 2026-08-09 / 2026-08-09). `Repository_Integrity_Protocol.md`'s RIP-001 is Resolved with the Git-release-tag primary mechanism, matching RS-003's account. File Purpose's ownership claim matches the Charter-listed canonical target as reconciled 2026-10-28. One failure: F-RS-1.
6. **Bare colliding-ID citations:** F-RS-6.
7. **Drift indicators incl. near-trips:** F-RS-7; none firing.
8. **Section integrity:** all eleven FT sections present in order (Navigation Anchors through Drift Indicators). Clean.
9. **Version/registry consistency:** Status Exploration and Body Stability Transitional are valid File_Template vocabulary; Spec Gates 0/6 consistent with Exploration status. Clean.
10. **Ethical Anchor exact string:** "Attempt to do no harm. Defer to Ethical_Constraints.md if present." — exact match against Ethical_Constraints.md's canonical row. Clean.
11. **Highest Risk parity (Risk, not Priority):** Low = max of the sidecar Risk column (Low/Low/Low); RS-003's Priority "Major" correctly not used. Clean.

**Fabrication probes (every cited path/ID verified live at `03f15726`):**

- Root table: the live root holds exactly the nine documented files (.gitignore, CONTRIBUTING.md, Discovery.md, LICENSE.md, NOTICE.md, README.md, Routing.md, Things_We_Got_Wrong.md, Unknowns.md) — 9/9, no undocumented root file; the root-count drift indicator does not fire.
- §I gate examples `Gate_01_Intake.md` through `Gate_07_Utilization.md`: all seven live in Operations/.
- Boundary-case exemplars: Facilities.md (Architecture/), Support_Raft.md (Tests/), Forge_flow.md (Architecture/) — all live as claimed.
- RS-001 retroactive-note table: `Automation/Candidate3_Colab_Hybrid.zip` live; `Archive/Astroid-miner/PROVENANCE.md` and `Astroid-miner-AstroidMinerV0.07/` live (the MAINT-71 annotation's claims hold); `Tests/Automation/test_harness_prompt.py` live; the import claims are true per `Automation/README.md` (audit_lib imported by harness and integrity checker; parser imported by the integrity checker); `Automation/Cold_session_manifest.py` fetched — JSON despite the `.py` extension, registered in Routing.md (RS claim true).
- Rule 8: Automation/ holds no `*_Scope_Map.md` (README only) — the rule holds live.
- FAILURES (recorded as findings): the F-RS-1 path does not exist; the F-RS-2 counts are false against the live listing and the live README.

**X10 index-parity, four sub-shapes:** recomputed clean (File State 0 = sidecar 0; Unknowns.md active-index exclusion per Size Management Rule 2 with matching dates; Highest Risk parity; no stale counts in the unknowns registry). **X11 wrapper-decay watch:** not a wrapper; N/A.

## Remedy queue additions (the human's alone; nothing executed)

- Repoint the F-RS-1 citation to `Admin/AAudits/AUDIT_12_Admin-Repository_Structure.md` (folds into the standing wrong-home-citation batch item).
- Refresh the F-RS-2 counts (twelve `.py`), and resolve the README description gap (describe `Candidate3_Transient_Index_Colab_hybrid.py` and `coverage_ledger_regen.py` in `Automation/README.md`, or soften RS's "described in" half).
- Correct the F-RS-3 example (TWGW candidate).
- F-RS-4 folds into the standing MAINT-56 retirement batch item.
- F-RS-5: add dated residue annotations per the file's own PKC-023 annotation discipline.
- F-RS-6: qualify both "AUDIT_12 F2" citations with the report's home and epoch.

## Verification block

- Audited file: `Admin/Repository_Structure.md` at LF main `03f15726e9245df8f62f460998eedeb2cef6a0d4` — 37,588 chars / 617 lines, fetched complete, SHA-256 `f0f7ad1f5d5c85651a34d9bb8bea40964f6c59f57a63d838521b043ab77b619a`.
- Key sources probed live at the same head: root, Admin/AAudits/, Automation/, Archive/, Archive/Astroid-miner/, Operations/, Architecture/, Tests/, Tests/Automation/ listings; Automation/README.md (8,043 chars) and Automation/Cold_session_manifest.py fetched; Archive/Rename_Registry.md, Architecture/Forge_flow.md, Unknowns.md, Routing.md, Discovery.md, Admin/File_Template.md, Admin/Ethical_Constraints.md, Admin/Repository_Integrity_Protocol.md fetched.
- Pre-compose head re-check (the MAINT-109 process remedy, first operational use): LF main verified at `03f15726` immediately before compose and re-verified immediately before push.
- This deposit is append-only; no audited-file field advanced.
