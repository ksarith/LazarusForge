# Admin_Governance_Teardown_POC.md

## Navigation Anchors
[README.md](../README.md) | [Discovery.md](../Discovery.md) | [Routing.md](../Routing.md) | [Admin/Repository_Structure.md](../Admin/Repository_Structure.md) | [Admin/Resolution_Methodology.md](../Admin/Resolution_Methodology.md)

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Spec Gates       | 0/6 — this is an analysis exercise, not a specification              |
| Open Unknowns    | 0 — this file identifies restructuring candidates, it does not itself resolve any Unknown |
| Owning Domain    | Tests/ (proof-of-concept / methodology exercise, not physical evidence) |
| Last Reviewed    | 2026-10-04                                                          |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES:**
- Classify every file in `Admin/` (33 files, ~1.76 MB as of 2026-10-04) against a stated minimality criterion, to identify what's load-bearing for a minimal governance proof-of-concept versus what's accumulated elaboration.
- Name specific, source-grounded restructuring candidates — consolidation, splitting, or relocation — with the reasoning that produced each one.
- Stay strictly observational and propositional. No file is modified, merged, or deprecated by this document.

**This file does NOT:**
- Constitute a ratified restructuring decision. Any action proposed here still requires the same process real changes to these files already require — and for Tier 1 Axiom content specifically, `Admin/Governance_Migration_Protocol.md`'s own amendment process, not a shortcut through this file.
- Duplicate or override any file's own Scope Boundary. Classifications here are read *from* those Scope Boundaries, not imposed on them.
- Assess Operations/, Architecture/, Challenges/, or Tests/ content. Scoped to `Admin/` only, per the question that prompted this file.

---

## File Purpose

The `Admin/` folder has grown to 33 files and ~1.76 MB without a single pass asking what's actually load-bearing. This file is that pass: a proof-of-concept teardown, sorting every file by an explicit minimality test rather than by impression, to surface genuine restructuring opportunities — and, as importantly, to show which files only *look* redundant until their Scope Boundaries are actually read side by side.

---

## Methodology

**The test, for each file:** *If a minimal Lazarus Forge proof-of-concept had to launch today — one human, no quorum, no hardware fleet — would the system lose something it cannot function without if this file didn't exist?*

Four tiers result:

- **Tier 0 — Constitutional core.** Defines the axioms, hard floors, and structural contract the rest of the system is built on. Removing it doesn't shrink the system, it ends it.
- **Tier 1 — Operational machinery.** Makes Tier 0 actually usable day to day — audit mechanics, naming, continuity tracking. Not founding doctrine, but the system can't run without it.
- **Tier 2 — Specialized/derived domains.** Real governance, narrower scope, dependent on Tier 0/1. A minimal POC can defer these without losing its defining character, though a full deployment needs them eventually.
- **Tier 3 — Theoretical superstructure.** Intellectually load-bearing for the project's identity, explicitly *not* operationally load-bearing by the files' own Status fields.
- **Tier 4 — Tooling/meta.** Prompts, schemas, templates for running the audit process itself — not doctrine content.

Classification was read from each file's own **Scope Boundary** (`**This file DOES/DOES NOT define**`) and **Status** field, not inferred from filename or guessed. Where a file had no standard Scope Boundary section, its actual header content was read directly instead (noted below).

---

## Classification Table

| File | Size | Tier | One-line function (from its own Scope Boundary) |
|------|------|------|---------------------------------------------------|
| `Governance_Charter.md` | 124 KB | **0** | Tier 1 Axioms, constitutional hierarchy, governance precedence |
| `Ethical_Constraints.md` | 144 KB | **0** | Pre-action authorization, Anti-Weaponization hard floor, refusal doctrine |
| `Auditor_Protocols.md` | 150 KB | **0** | Epistemic Foundation (EF-0.0–0.8b), auditor roles, Sidecar Model, gate enforcement |
| `File_Template.md` | 41 KB | **0** | The structural contract every other file follows |
| `Repository_Structure.md` | 27 KB | **0** | Naming convention, folder/root placement doctrine |
| `Verification_Gates.md` | 41 KB | **0** | The six gates every specification must pass |
| `Repository_Integrity_Protocol.md` | 107 KB | **1** | Integrity baselines, violation classes, response ladder (the *timing* layer, not the structure — see its own cross-ref to Auditor_Protocols) |
| `Canonical_Terms.md` | 79 KB | **1** | Authoritative vocabulary, anti-drift term guardrails |
| `Resolution_Methodology.md` | 38 KB | **1** | Citable resolution patterns from real sessions — explicitly a reference, not a gate |
| `Operational_Conventions.md` | 13 KB | **1** | Convention catalog (no standard Scope Boundary — read directly; this is itself a Tier-1-appropriate example: small, citable, non-blocking) |
| `Progress_Log.md` | 84 KB | **1** | Rolling continuity record — explicitly *not* a duplicate of Unknowns.md or Resolution Logs |
| `Agent_Verification_Event.md` | 9 KB | **1** | AVE schema — Status: Candidate/Exploration, Volatile — process schema used across sessions |
| `Autonomy_Divergence_Protocol.md` | 65 KB | **2** | Response tiers for autonomy drift — Status: **Draft, PROPOSED NOT RATIFIED** |
| `Governance_Migration_Protocol.md` | 182 KB | **2** | Amendment procedure for Tier 1 Axioms — largest file in Admin/ by far |
| `Security_Protocols.md` | 106 KB | **2** | Cryptographic mechanisms, multi-sig override, node identity |
| `Safety_Protocols.md` | 29 KB | **2** | PPE, hazard classes, physical operator risk |
| `Environmental_Constraints.md` | 51 KB | **2** | Site/regional environmental parameters |
| `Hardware_Diversity_Ladder.md` | 15 KB | **2** | Four-tier hardware-diversity path to GOV-008's bar — explicitly "records a path, not a status" |
| `Ship_of_Theseus.md` | 27 KB | **2** | Identity-continuity doctrine (physical and AI) |
| `Economics.md` | 37 KB | **2** | Procurement, surplus disposition, barter doctrine |
| `Engineer_Protocols.md` | 38 KB | **2** | Engineering cognitive/procedural protocols |
| `Trajectories.md` | 35 KB | **2** | v0→v5 version roadmap, FRT doctrine |
| `Metrics_Scaffold.md` | 8 KB | **2** | Lane C metric taxonomy — explicitly "not a dashboard" |
| `Integrity_Incident_Log.md` | 6 KB | **2** | Append-only incident intake, distinct from Progress_Log and Field_Logs |
| `Forge_Audit_Kit.md` | 26 KB | **2** | Condensed audit operational reference (currently Draft, 0/6 — see FAK-017 and the open "role/retirement question" already on record) |
| `Experiments.md` | 8 KB | **2** | Falsification records — PROVISIONAL → VERIFIED promotion mechanism |
| `Adm_Scope_Map.md` | 34 KB | **2** | Admin/'s own per-file scope index (no standard Scope Boundary — it *is* the index) |
| `Computational_Institutional_Reasoning.md` | 83 KB | **3** | Formal algebra for institutional state — "a formal theoretical framework, not a ratified governance authority" |
| `CIR_Gov.md` | 51 KB | **3** | CIR's predicate-kernel packaging — "Proposed–Not-Ratified layer" |
| `Nothingness_Theorem.md` | 32 KB | **3** | Tier 0 *philosophically*, but explicitly "functionless by doctrine," exempt from Spec Gates, audited for internal consistency only |
| `BATTERY_SEED.md` | 8 KB | **4** | Draft seed/template for audit battery content |
| `INTEGRITY_SWEEP_PROMPT.md` | 12 KB | **4** | Draft — a literal prompt template for running integrity sweeps |
| `PROBE_INVOCATION.md` | 10 KB | **4** | Draft — a literal prompt template for probe invocation |

**Totals:** Tier 0: 6 files / 527 KB. Tier 1: 7 files / 245 KB. Tier 2: 14 files / 653 KB. Tier 3: 3 files / 166 KB. Tier 4: 3 files / 30 KB.

---

## Findings

**1. Tier 3 is the cleanest consolidation candidate, and it's larger than most Tier 0 files individually.** `Nothingness_Theorem.md`, `Computational_Institutional_Reasoning.md`, and `CIR_Gov.md` total 166 KB — more than `Governance_Charter.md` alone — and all three say, in their own Status fields, that they don't gate anything operational. `Nothingness_Theorem.md` is explicitly "functionless by doctrine," CIR is explicitly "not a ratified governance authority," and CIR_Gov is explicitly a "Proposed–Not-Ratified layer." A minimal POC loses zero operational capability by treating this trio as a single deferred "Theoretical Foundations" unit rather than three co-equal files sitting alongside the Charter. This doesn't mean deleting or devaluing the work — it means the *filing structure* currently implies these are as load-bearing as `Ethical_Constraints.md`, and their own text says they aren't.

**2. `Governance_Migration_Protocol.md` at 182 KB is an outlier even among Tier 0/1 files, and its own Scope Boundary suggests why: it's trying to be both the rare-event amendment procedure (Tier 1 Axiom changes) and the common-event migration mechanics (Track A/B classification used far more often) in one file.** A split along that exact seam — the amendment process most sessions never touch, versus the Track A/B classification machinery that gets invoked regularly — is suggested by the file's own internal structure, not imposed from outside.

**3. Tiers 0 and 1 together are 13 files and ~772 KB — this is the actual load-bearing core.** Everything a minimal proof-of-concept needs to function (axioms, hard floors, the audit/promotion mechanism, naming, vocabulary, continuity tracking) lives here. That's well under half the folder's file count and well under half its size — the other ~1 MB is Tier 2 specialization, Tier 3 theory, and Tier 4 tooling, none of which a from-scratch POC needs on day one.

**4. The folder does not appear to have redundant/overlapping files once Scope Boundaries are actually compared — the "chaos" is scale, not duplication.** `Security_Protocols.md`, `Repository_Integrity_Protocol.md`, and `Auditor_Protocols.md` all touch "integrity" by name, which reads as overlap from the outside. Read together, their own DOES-NOT sections cleanly hand off to each other: RIP owns violation *timing and classification*, Security owns *cryptographic mechanism*, Auditor_Protocols owns *epistemic foundation and role behavior*. This is a real finding worth having, even though it's a non-finding in the "cut this" sense — it means restructuring should be about **extraction and relocation** (Tier 3 out, Governance_Migration_Protocol split), not about hunting for duplicate content that doesn't appear to exist.

**5. Tier 4 (the three prompt/schema templates) arguably doesn't belong in `Admin/` conceptually at all** — they're tooling artifacts in the same sense `Automation/`'s `.py` files are (see `Operational_Conventions.md` Convention 6, which already exempts `Automation/` scripts from `Routing.md` registration on exactly this reasoning). Whether that argues for literal relocation or just for a shared understanding that these three are a different kind of file is itself a decision worth making deliberately, not a given.

---

## Explicit non-claims

- This file does not claim Tier 2 content is unimportant — only that it's deferrable for a *minimal* POC, which is a different claim.
- This file does not propose specific target filenames, merge mechanics, or a migration sequence. That's the next step, if this framework holds up to scrutiny — not this document's job.
- The percentages and tier assignments above reflect one classification pass, done in one session. They should be treated as a first cut to react to, not a finished audit.

---

## Resolution Log

- 2026-10-04: File created. Direct response to a request to "tear down the repo into minimized
  components to rebuild into what must exist," scoped to `Admin/` governance files specifically
  after clarifying that physical G.E.C.K. teardown (already covered by
  `Architecture/Geck_forge_seed.md`) was not what was meant. All 33 `Admin/` files' own Scope
  Boundary and Status fields read directly before classifying — not inferred from filenames.
  Human-directed, Claude-authored.
