# Repository_Structure.md — LazarusForgeV0

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-08-11                                                          |
| Auditor          | Claude — Automation/ formalized in Section II (external ChatGPT review finding, verified before applying), human-directed; prior: Grok — correction pass, 2026-08-09 |
| Open Unknowns    | 1                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Low                                                                 |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Canonical filename convention — the no-version-suffix rule and its rationale
- Folder assignment doctrine — decision rules for where new files belong
- Root file doctrine — what earns placement outside a folder
- File naming standard — casing, separators, word order
- Archive/ directory doctrine (resolves RIP-001 prerequisite)
- Cross-repo naming discipline
- Planned directory additions and their trigger conditions
- Forward-looking naming standard — new files created under this rule

**This file DOES NOT define:**
- File content standards (→ `Admin/File_Template.md`)
- Governance authority hierarchy (→ `Admin/Governance_Charter.md`)
- Navigation summaries or the current file map (→ `Discovery.md`)
- Rename Registry for historical corrections (→ `Archive/Rename_Registry.md`)
- Migration procedures for existing files (→
  `Admin/Governance_Migration_Protocol.md` Track A)
- Repository integrity enforcement (→
  `Admin/Repository_Integrity_Protocol.md`)

---

## File Purpose

This file defines how the LazarusForgeV0 repository is structured and
how new files are named and placed. Without it, folder assignment and
naming decisions are made by inference from existing patterns — which
works until it doesn't, and fails silently when contributors disagree
about which pattern applies.

The Rename Registry in `Archive/Rename_Registry.md` is the evidence that naming has
been inconsistent historically. This file exists so the Rename Registry
shrinks going forward rather than continuing to grow. It also resolves
RIP-001 (Archive/ directory not established) by defining the doctrine
for that directory, unblocking Repository_Integrity_Protocol.md's
prior-state preservation requirement.

**Ownership transfer:** The Governance_Charter.md Canonical Governance
Ownership table lists `Repository_Structure.md` as a planned canonical
target with no current owner. This file now owns repository structure
doctrine. Discovery.md retains ownership of the navigation map;
`Archive/Rename_Registry.md` owns the historical rename record — those are complementary, not overlapping.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | The six-folder structure (root, Admin/, Architecture/, Operations/, Tests/, Challenges/) is stable at v0 | Current repo state | High | New capability domain requires a folder not covered by existing structure |
| ASM-002 | Markdown (.md) remains the universal file format for all doctrine and specification files | Current tooling and workflow | High | Alternative format formally adopted |
| ASM-003 | The no-version-suffix rule applies to new files only — existing files are renamed opportunistically, not mandatorily | Rename Registry workload realism | High | Bulk rename pass formally scheduled |

---

## I. Filename Convention

### The No-Version-Suffix Rule

**Version suffixes do not belong in filenames.**

The `_v0`, `_v1`, `_LF` suffixes that appear in the Rename Registry
represent an earlier convention that has been systematically retired.
The pattern is now clear across the repository: Energy.md, not
energy_v0.md. Air_Scrubber.md, not Air_Scrubber_v0.md. Economics.md,
not economics_v0.md.

**Rationale:** Version state belongs in the File State block, not the
filename. A filename with a version suffix implies the versioned and
unversioned files coexist — which creates ambiguity about which is
canonical. The File State block (Status, Spec Gates, Last Audit) carries
all version information without polluting the filename.

**Rule:** All new files are created without version suffixes. Existing
files with version suffixes are renamed opportunistically during audit
passes using the Track A migration procedure in
`Admin/Governance_Migration_Protocol.md`. Renamed files are recorded
in the `Archive/Rename_Registry.md`.

### The No-Scope-Suffix Rule

Scope identifiers (`_LF`, `_forge`, `_v0`) in filenames are also
retired. They were useful when files existed outside the repository
context — they are redundant inside it. Every file in this repository
is a LazarusForge file by definition.

**Exceptions:** The AUDIT_HARNESS.py script retains its name as a
functional identifier, not a scope tag. Scripts and non-markdown files
are not subject to this convention.

### Casing Standard

**PascalCase with underscores as word separators.**

Examples: `Forge_flow.md`, `Gate_02_Triage.md`, `Canonical_Terms.md`,
`Safety_Protocols.md`

Rules:
- First letter of each word is capitalized
- Words separated by underscores
- No spaces, no hyphens, no camelCase without underscores
- Acronyms treated as single words: `Air_Scrubber.md` not
  `Air_Scrubber.md`

**Accepted outlier:** `Forge_flow.md` uses lowercase `flow`. RS-002 closed
2026-08-09 as accepted exception — Rename Registry and the 2026-06-11
resolution log already treated this form as canonical. The lowercase is
not a precedent for new files.

### Numeric Prefixes in Gate Files

Gate files use zero-padded two-digit numeric prefixes for sort order:
`Gate_01_Intake.md`, `Gate_02_Triage.md`, through `Gate_07_Utilization.md`.

This convention applies only to sequential gate files in Operations/.
It does not generalize to other folders.

### File Extension

All doctrine, specification, and governance files use `.md` (Markdown).
Scripts use their native extension (`.py`). No other extensions are
currently in use. New file types require a RS-001 review before
introduction.

---

## II. Folder Assignment Doctrine

### The Six-Folder Structure Plus Automation/

```
Root                 — Navigation and cross-cutting files only
Admin/               — Governance, protocols, and doctrine
Architecture/        — System architecture and foundational logic
Operations/          — Physical modules and operational systems
Tests/               — Test frameworks and deployment platforms
Challenges/          — Problem layer: why these capabilities exist
Automation/          — Repository tooling; executable infrastructure
Archive/             — Prior states of governance-bearing documents
```

Automation/ is not a seventh content domain and does not compete with
the six above for file-placement purposes — see Rule 8 below. The
section name is retained for continuity with existing cross-references;
"Six-Folder Structure" refers to the six content-owning domains, with
Automation/ and Archive/ as infrastructure and history layers respectively.

### Decision Rules

When a new file is being placed, apply these rules in order:

**Rule 1 — Does it govern how the repository operates?**
If yes → Admin/. This includes protocols, governance documents,
audit frameworks, safety standards, and any file that sets rules
other files must follow.

**Rule 2 — Does it define foundational principles or system architecture
that other modules implement?**
If yes → Architecture/. This includes first-principles doctrine,
physical laws as Forge constraints, cognitive frameworks, and
network topology. Architecture/ files are referenced by Operations/
files, not the other way around.

**Rule 3 — Does it define a specific physical module, gate, or
operational subsystem?**
If yes → Operations/. Gate files, domain subsystems (Electronics,
Energy, Air_Scrubber), and material processing modules belong here.

**Rule 4 — Does it define a test environment, deployment platform,
or stress-testing framework?**
If yes → Tests/. Marine deployment, autonomous unit testing, and
validation platforms belong here.

**Rule 5 — Does it define a problem the Forge exists to address?**
If yes → Challenges/. These files define the why — water scarcity,
waste, planned obsolescence. They do not define solutions.

**Rule 6 — Does it span the entire repository and serve as a
navigation or cross-cutting reference?**
If yes → Root. Only a small number of files earn root placement
(see Section III).

**Rule 7 — Is it a prior state of a governance-bearing document?**
If yes → Archive/ (see Section V).

**Rule 8 — Is it an executable script implementing repository tooling
(audit, integrity-check, session-bootstrap, or similar automation),
or documentation describing only that script's own operation?**
If yes → Automation/. Automation/ is infrastructure, not a content
domain — it does not receive its own `*_Scope_Map.md`, and its
source of truth is the executable behavior of its scripts plus the
protocols (in Admin/) that specify what they must do. Doctrine that
happens to be about automation but sets rules other files must
follow still goes to Admin/ under Rule 1; only the implementation
artifacts themselves (the `.py` sources) go in Automation/.

**When rules conflict:** Apply the most specific rule. A file that
is both architectural and operational belongs in Architecture/ if
it primarily sets doctrine that Operations/ implements, or in
Operations/ if it primarily specifies a physical module. When genuinely
ambiguous, default to the folder of its primary downstream consumers.
Document the reasoning in the file's own Scope Boundary.

### Boundary Cases by Folder

**Admin/ vs. Architecture/:** Admin/ governs contributors and
processes. Architecture/ governs the system being built. Safety_Protocols.md
is in Admin/ because it sets standards for contributors (operators).
Facilities.md is in Architecture/ because it defines physical
prerequisites for the system. When in doubt: who is the primary
audience — a contributor following a rule, or a system being built?

**Architecture/ vs. Operations/:** Architecture/ files are foundational
— they establish principles that multiple Operations/ files implement.
Operations/ files are specific — they define a particular module or gate.
A file that is cited by three or more Operations/ files as upstream
doctrine belongs in Architecture/. A file that owns one specific
physical process belongs in Operations/.

**Tests/ vs. Operations/:** Tests/ files define environments that
exist to stress-test and validate. Operations/ files define processes
that exist to produce output. Support_Raft.md is in Tests/ because
its primary purpose is as a testing and deployment platform, even
though it contains operational content.

**Challenges/ vs. everywhere else:** Challenges/ files define problems,
not solutions. If a file contains solution specifications, it belongs
elsewhere regardless of how it frames its purpose.

---

## III. Root File Doctrine

Root placement is reserved. Only files that meet all three criteria
belong at root:

1. **Cross-cutting scope** — the file is relevant to every folder
   and cannot be owned by any single folder without creating a
   misleading authority claim
2. **Navigation or index function** — the file helps contributors
   find other files or understand the repository as a whole
3. **No natural folder home** — placing the file in any folder
   would imply a scope restriction that doesn't exist

**Current root files and their justification:**

| File | Justification |
|------|---------------|
| `README.md` | Project overview — entry point for all contributors |
| `Discovery.md` | Navigation layer — spans all folders |
| `Unknowns.md` | Cross-module unknowns index — spans all folders |

**Files that do not belong at root:** Governance files belong in
Admin/ even if they feel foundational. Architecture files belong in
Architecture/ even if they feel universal. The temptation to place
important files at root because they feel significant is a placement
error — significance is not a root criterion.

---

## IV. Naming New Files

Before creating a new file, answer these questions in order:

**1. Does this file already exist under a different name?**
Check the `Archive/Rename_Registry.md` and the full file map.
Duplicate files with different names are a governance failure.

**2. What is the single most accurate noun for what this file owns?**
The filename should be that noun. Not a description of what it does —
the thing it is. `Facilities.md` not `Physical_Site_Requirements.md`.
`Economics.md` not `Economic_Model_v0.md`.

**3. Which folder does it belong in?**
Apply Section II decision rules. Document the reasoning if it required
judgment.

**4. Does the name conflict with any existing file across all folders?**
Filenames should be unique across the repository, not just within
a folder. `Gate_02_Triage.md` and a hypothetical `Triage.md` in
Architecture/ would create confusion even in different folders.

**5. Apply the naming standard:**
- PascalCase with underscores
- No version suffix
- No scope suffix
- Correct extension (.md for doctrine files)

---

## V. Archive/ Directory Doctrine

The Archive/ directory resolves RIP-001 in
`Admin/Repository_Integrity_Protocol.md` — the critical unknown that
prior-state preservation has no defined location.

### What Goes in Archive/

Prior states of governance-bearing documents saved before revision,
per the Version Preservation Protocol in Repository_Integrity_Protocol.md.

**Governance-bearing documents** are those whose modification carries
governance risk: Tier 1 and Tier 2 files (Governance_Charter.md,
Ethical_Constraints.md, Auditor_Protocols.md), and any file with
Specification status.

Exploration and Draft files do not require archiving before revision —
their File State volatility is declared. However, archiving is
encouraged when a Draft file contains substantial Lessons Learned or
Resolution Log content that would be lost in a major restructure.

### Archive/ Naming Convention

Format: `[Filename]_YYYYMMDD_[version].md`

Examples:
- `Governance_Charter_20260602_v06.md`
- `Auditor_Protocols_20260523_v07.md`

The date is the date of archiving (before revision), not the date
of the file's last audit. The version matches the version noted in
the file's Resolution Log at the time of archiving.

### Archive/ is Not Navigation Space

Archive/ files do not appear in the Discovery.md file map. They are
not audited as active files. They exist for recovery and lineage
verification only. An auditor reading an Archive/ file to verify
prior state is the intended use case — not routine access.

### Archive/ Trigger Conditions

Archive before revision when:
- Any Tier 1 or Tier 2 file is being substantively revised
- Any file at Specification status is being revised
- A Track B migration (Tier 1 amendment) is being executed
- Repository_Integrity_Protocol.md Version Preservation Protocol
  requires it

### Discovery.md Update

When Archive/ is created as a physical directory, add it to the
Discovery.md repository structure map per the note in
Repository_Integrity_Protocol.md RIP-001. This file's existence
does not substitute for that update — the directory must exist
and be noted in Discovery.md before RIP-001 can be closed.

---

## VI. Cross-Repo Naming Discipline

The LazarusForge project spans three repositories with distinct roles:

| Repository | Role | Naming Convention |
|---|---|---|
| `LazarusForgeV0` | Active working repository — lean, operational, specification-oriented | This file's conventions apply |
| `Lazarus-Forge-` | Doctrine and philosophy companion | Separate governance — not subject to this file |
| `Astroid-miner` | Planned space-based extension — deferred to Leviathan milestone | Not yet active |

**Cross-repo rules:**
- Do not create files in LazarusForgeV0 that duplicate doctrine
  owned by Lazarus-Forge- without an explicit divergence reason logged
- Divergence between repos is a signal — log it, do not silently resolve it
- Astroid-miner does not inherit LazarusForgeV0 structure automatically —
  it will require its own Repository_Structure.md when activated

**The `V0` in LazarusForgeV0 is a repository name, not a file version
suffix.** The no-version-suffix rule applies to files within the
repository. It does not apply to the repository name itself, which
is a proper noun identifying a specific instantiation.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-06-05 | Audit Review | Version suffixes in filenames (_v0, _LF) | Created ambiguity about canonical file identity; required growing Rename Registry | Version state belongs in File State block, not filename. No-version-suffix rule adopted as forward doctrine. | Replicated | No |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### RS-001 — Non-markdown file type introduction procedure undefined

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Governance                     |
| Blocking      | No                             |
| Owner         | Admin/Repository_Structure.md  |
| First Logged  | 2026-06-05                     |
| Last Reviewed | 2026-06-05                     |

**Description:** Section I states that new file types require a RS-001
review before introduction. The review procedure itself is not yet
defined.

**Why It Matters:** AUDIT_HARNESS.py is currently the only non-markdown
file. If scripts, data files, or other formats are added, the naming
and placement convention may not apply cleanly.

**Resolution Path:** Payment via Specification — define minimum review
criteria when a non-markdown file type is first proposed. Likely a
lightweight Track A migration noting the new type, its folder
assignment, and its naming convention. Defer until a concrete case
arises.

---

### RS-002 — Forge_flow.md casing outlier not yet corrected

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Resolved — Accepted outlier    |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Housekeeping                   |
| Blocking      | No                             |
| Owner         | Admin/Repository_Structure.md  |
| First Logged  | 2026-06-05                     |
| Last Reviewed | 2026-08-09                     |
| Resolved      | 2026-08-09                     |

**Description:** `Forge_flow.md` uses lowercase `flow`, inconsistent with
the PascalCase standard in Section I.

**Resolution (2026-08-09):** Option A — accept current form as intentional
exception. Rename Registry already records `Forge_flow.md → Forge_flow.md
| Resolved — RS-002 2026-06-11`. The 2026-06-11 resolution log in
`Architecture/Forge_flow.md` treated the current casing as canonical.
Re-opening a rename would re-fight a settled historical decision for
negligible gain. Section I updated to "Accepted outlier." Not a precedent
for new files.

---

### RS-003 — Archive/ directory not yet physically created

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Resolved                       |
| Risk          | Low                            |
| Priority      | Major                          |
| Type          | Operational                    |
| Blocking      | No                             |
| Owner         | Admin/Repository_Structure.md  |
| First Logged  | 2026-06-05                     |
| Last Reviewed | 2026-08-09                     |
| Resolved      | 2026-08-09 (recognition of pre-existing state) |

**Description:** Section V defines Archive/ doctrine but the directory
does not yet exist in the repository. RIP-001 in
Repository_Integrity_Protocol.md remains open until the directory
exists and is noted in Discovery.md.

**Resolution (2026-08-09):** Archive/ has existed and been populated
for some time (chat distillates, Logs/, Rename_Registry.md, etc.).
Discovery.md structure map already includes it. RIP-001 itself was
closed earlier (2026-06-27) via the Git release-tag primary archival
mechanism. This entry's Status was left Open long after the physical
condition was satisfied — classic registration lag. Closed on
recognition; no new action required.

---

### Resolution Log

- 2026-08-09: **RS-002 closed — accepted outlier.** Keep `Forge_flow.md`
  casing. Rename Registry and 2026-06-11 Forge_flow resolution log already
  treated current form as canonical; re-fighting that for PascalCase purity
  is low-value. Section I updated. Not a precedent for new files.
  Human-directed.

- 2026-08-09: **RS-003 closed.** Archive/ directory has been present and
  populated (Logs/, Rename_Registry.md, multiple chat distillates) for
  an extended period; Discovery.md already maps it; RIP-001 was closed
  2026-06-27 on the Git-tag primary path. Status left Open purely by
  registration lag. Human-directed recognition pass.

- 2026-08-11: **Automation/ formalized in Section II — external
  (ChatGPT) review finding, verified before applying.** Section II's
  folder diagram and Decision Rules described only six folders and had
  no rule covering Automation/, despite it existing physically with 9
  scripts and already being treated as its own layer in both
  `Routing.md` ("Automation/ Layer" table) and `Discovery.md` (already
  called it "structurally different (scripts, not doctrine)" at the
  Tst_Scope_Map build, 2026-08-08 — this file was the one lagging, not
  Discovery.md or Routing.md). Added Automation/ to the folder diagram
  with an explanatory note, and a new Rule 8 stating it is
  infrastructure, not a seventh content domain — it gets no
  `*_Scope_Map.md`, and doctrine *about* automation still goes to
  Admin/ under Rule 1; only the `.py` implementation artifacts
  themselves go in Automation/. Human-directed.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-06-05 | Mandatory bulk rename of all existing version-suffixed files | Rename Registry workload is non-trivial and each rename requires downstream reference updates. Opportunistic renaming during audit passes achieves the same outcome without creating a large one-time correction burden. | No |
| 2026-06-05 | Placing Repository_Structure.md in root alongside Discovery.md | Structure doctrine governs contributors — it belongs in Admin/ with the other protocol files. Discovery.md is a navigation file; this file is a governance file. Same subject matter, different function. | No |

---

## Drift Indicators

*Standard drift indicators per `Admin/File_Template.md` apply. Additional
triggers specific to this file:*

- A new file is created with a version suffix without a logged exception
- A new file is created with a scope suffix (_LF, _forge) without a
  logged exception
- Forge_flow.md lowercase outlier is treated as a valid naming pattern
  in a new file
- Archive/ directory remains uncreated after a Tier 1 or Specification
  file is revised
- Root file count exceeds three without a documented root placement
  justification for each addition
- A new folder is created without a RS decision entry in this file
