# Admin_Governance_Teardown_POC.md

## Navigation Anchors
[README.md](../README.md) | [Discovery.md](../Discovery.md) | [Routing.md](../Routing.md) | [Admin/Repository_Structure.md](../Admin/Repository_Structure.md) | [Admin/Adm_Scope_Map.md](../Admin/Adm_Scope_Map.md) | [Admin/Resolution_Methodology.md](../Admin/Resolution_Methodology.md)

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Spec Gates       | 0/6 — this is an analysis exercise, not a specification              |
| Open Unknowns    | 0 — this file identifies restructuring candidates, it does not itself resolve any Unknown |
| Owning Domain    | Tests/ (proof-of-concept / methodology exercise, not physical evidence) |
| Last Reviewed    | 2026-10-04 — hypothesis-not-inventory line added to Scope Boundary; "Future experiment (not scheduled)" section added. Prior: recompute rule, Tier 2 deferral costs, GMP seam appendix, Tier 3/4 disposition options, link to Adm_Scope_Map load-bearing summary |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES:**
- Classify every file in `Admin/` (33 files, ~1.76 MB as of 2026-10-04) against a stated minimality criterion, to identify what's load-bearing for a minimal governance proof-of-concept versus what's accumulated elaboration.
- Name specific, source-grounded restructuring candidates — consolidation, splitting, or relocation — with the reasoning that produced each one.
- Record **deferral cost** for Tier 2 files (what named open work suffers if the file is treated as day-one optional).
- Sketch a possible **Governance_Migration_Protocol** internal seam (amendment vs Track A/B) without rewriting that file.
- Stay strictly observational and propositional. No file is modified, merged, or deprecated by this document.

**This file does NOT:**
- Constitute a ratified restructuring decision. Any action proposed here still requires the same process real changes to these files already require — and for Tier 1 Axiom content specifically, `Admin/Governance_Migration_Protocol.md`'s own amendment process, not a shortcut through this file.
- Duplicate or override any file's own Scope Boundary. Classifications here are read *from* those Scope Boundaries, not imposed on them.
- Assess Operations/, Architecture/, Challenges/, or Tests/ content. Scoped to `Admin/` only, per the question that prompted this file.
- Produce Field_Logs evidence or close any Unknown.
- Claim a demonstrated capability inventory. Tier assignments are **hypotheses about load-bearing structure**, read from each file's own Scope Boundary and Status field — not evidence that removing a file would actually produce the capability loss the tier implies. No component has been removed and tested. See "Future experiment (not scheduled)" below for what would actually close that gap.

**One-screen summary:** Tier 0–4 counts and navigation framing also live in `Admin/Adm_Scope_Map.md` § Load-bearing map. That section is a summary; **this file is the full table and findings**. If the two disagree, recompute from the classification table below and fix both.

---

## File Purpose

The `Admin/` folder has grown to 33 files and ~1.76 MB without a single pass asking what's actually load-bearing. This file is that pass: a proof-of-concept teardown, sorting every file by an explicit minimality test rather than by impression, to surface genuine restructuring opportunities — and, as importantly, to show which files only *look* redundant until their Scope Boundaries are actually read side by side.

It is an **instrument for filing decisions**, not a revolution. Prefer Field_Logs / Lane B evidence over expanding this analysis.

---

## Methodology

**The test, for each file:** *If a minimal Lazarus Forge proof-of-concept had to launch today — one human, no quorum, no hardware fleet — would the system lose something it cannot function without if this file didn't exist?*

Five tiers result:

- **Tier 0 — Constitutional core.** Defines the axioms, hard floors, and structural contract the rest of the system is built on. Removing it doesn't shrink the system, it ends it.
- **Tier 1 — Operational machinery.** Makes Tier 0 actually usable day to day — audit mechanics, naming, continuity tracking. Not founding doctrine, but the system can't run without it.
- **Tier 2 — Specialized/derived domains.** Real governance, narrower scope, dependent on Tier 0/1. A minimal POC can defer these without losing its *defining* character, though named open work (MAQT, physical runs, identity) often still needs them — see **Deferral costs** below.
- **Tier 3 — Theoretical superstructure.** Intellectually load-bearing for the project's identity, explicitly *not* operationally load-bearing by the files' own Status fields.
- **Tier 4 — Tooling/meta.** Prompts, schemas, templates for running the audit process itself — not doctrine content.

Classification was read from each file's own **Scope Boundary** (`**This file DOES/DOES NOT define**`) and **Status** field, not inferred from filename or guessed. Where a file had no standard Scope Boundary section, its actual header content was read directly instead.

### Recompute rule (mandatory for this file)

**Totals must be re-derived from the classification table by counting rows and summing the Size column per tier. Never trust a prior Totals line, a secondary summary (`Adm_Scope_Map` load-bearing map), or memory.**

Provenance: 2026-10-04 — Tier 1 and Tier 2 totals were wrong (7/245 and 14/653 stated; actual 6/330 and 15/667). The error propagated into `Adm_Scope_Map.md` until both were corrected from the table. Finding 3's “core size” claim was corrected the same day (12 files / ~857 KB, not 13 / ~772).

After any row add/remove/retier or size refresh: (1) recompute Totals, (2) update Finding 3 if 0+1 changed, (3) sync `Adm_Scope_Map.md` load-bearing map in the same session.

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

**Totals:** Tier 0: 6 files / 527 KB. Tier 1: 6 files / 330 KB. Tier 2: 15 files / 667 KB. Tier 3: 3 files / 166 KB. Tier 4: 3 files / 30 KB.  
**0+1 core:** 12 files / 857 KB.

*(Corrected 2026-10-04 — original Totals for Tiers 1 and 2 were arithmetic/counting errors (stated 7/245 and 14/653). Recomputed from table rows. Tiers 0, 3, and 4 were correct as originally stated.)*

---

## Deferral costs (Tier 2 only)

“Defer for minimal day-one POC” does **not** mean “ignore while running named programs.” Approximate cost if the file is absent or unread during that work:

| File | If deferred / ignored, what suffers |
|------|-------------------------------------|
| `Autonomy_Divergence_Protocol.md` | MAQT / peer divergence response; LT-007 framing (no sole-authority principle at protocol level) |
| `Governance_Migration_Protocol.md` | GOV-008 / §VII quorum work; Track A/B classification; axiom amendment path |
| `Security_Protocols.md` | Node identity, multi-sig, crypto mechanism claims; EL-006 adjacent trust language |
| `Safety_Protocols.md` | **Any physical run** (salvage, Logic-Zero bench, LE-0) — PPE and hazard classes |
| `Environmental_Constraints.md` | Site selection and environmental parameter claims |
| `Hardware_Diversity_Ladder.md` | MAQT Tier 2 scoring; anti-spoofing vs logical isolation |
| `Ship_of_Theseus.md` | LT-006 cognitive-grain / identity continuity; restoration authority claims |
| `Economics.md` | Procurement and surplus disposition decisions |
| `Engineer_Protocols.md` | Engineering procedure discipline for fabrication loops |
| `Trajectories.md` | v0→v5 / FRT roadmap alignment |
| `Metrics_Scaffold.md` | Lane C metric vocabulary (explicitly not a live dashboard) |
| `Integrity_Incident_Log.md` | Distinct incident intake vs Progress_Log / Field_Logs |
| `Forge_Audit_Kit.md` | Condensed audit ops; already Draft 0/6 — weak dependency until promoted |
| `Experiments.md` | PROVISIONAL → VERIFIED promotion path for falsification records |
| `Adm_Scope_Map.md` | Folder navigation only — low operational cost if Discovery/Routing stay current |

---

## Findings

**1. Tier 3 is the cleanest consolidation candidate, and it's larger than most Tier 0 files individually.** `Nothingness_Theorem.md`, `Computational_Institutional_Reasoning.md`, and `CIR_Gov.md` total 166 KB — more than `Governance_Charter.md` alone — and all three say, in their own Status fields, that they don't gate anything operational. A minimal POC loses zero operational capability by treating this trio as a single deferred "Theoretical Foundations" unit rather than three co-equal files sitting alongside the Charter. This doesn't mean deleting or devaluing the work — it means the *filing structure* currently implies these are as load-bearing as `Ethical_Constraints.md`, and their own text says they aren't.

**2. `Governance_Migration_Protocol.md` at 182 KB is the largest Admin/ file and is Tier 2, not Tier 0/1.** Its Scope Boundary and internal job mix rare-event Tier 1 Axiom amendment with common-event Track A/B migration mechanics. A split along that seam is suggested by structure, not imposed from outside — see **Appendix A**.

**3. Tiers 0 and 1 together are 12 files and ~857 KB — this is the actual load-bearing core.** *(Corrected 2026-10-04 with the Totals arithmetic fix: 6+6 files, 527+330 KB; prior 13/~772 inherited the Tier-1 miscount.)* Everything a minimal proof-of-concept needs to function (axioms, hard floors, the audit/promotion mechanism, naming, vocabulary, continuity tracking) lives here. That's well under half the folder's file count and under half its size — the other ~1 MB is Tier 2 specialization, Tier 3 theory, and Tier 4 tooling.

**4. The folder does not appear to have redundant/overlapping files once Scope Boundaries are actually compared — the "chaos" is scale, not duplication.** `Security_Protocols.md`, `Repository_Integrity_Protocol.md`, and `Auditor_Protocols.md` all touch "integrity" by name. Read together, their own DOES-NOT sections cleanly hand off: RIP owns violation *timing and classification*, Security owns *cryptographic mechanism*, Auditor_Protocols owns *epistemic foundation and role behavior*. Restructuring should be about **extraction and relocation** (Tier 3 grouping, optional GMP split), not hunting for duplicate content that doesn't appear to exist.

**5. Tier 4 (the three prompt/schema templates) arguably doesn't belong in `Admin/` conceptually** — tooling artifacts in the same sense as `Automation/` scripts (see `Operational_Conventions.md` Convention 6). Whether that argues for literal relocation or only shared understanding is a deliberate decision — see **Disposition options** below.

---

## Disposition options (Tier 3 and Tier 4 only — not executed)

Options for a future pass. Choosing one still requires normal change process; this table is not authorization.

| Target | Option A — Leave | Option B — Index | Option C — Relocate |
|--------|------------------|------------------|---------------------|
| **Tier 3** (CIR, CIR_Gov, Nothingness) | Stay as peer Admin files | Add “Theoretical foundations” index in Adm_Scope_Map / Discovery only | Move to e.g. `Admin/Theory/` or `Archive/Theory/` with Routing updates |
| **Tier 4** (BATTERY_SEED, INTEGRITY_SWEEP_PROMPT, PROBE_INVOCATION) | Stay in Admin/ | Mark as tooling in Adm_Scope_Map only | Move next to Automation/ or `Admin/Tooling/` with Convention 6-style Routing exemption if appropriate |

**Default until chosen:** Option A (leave). Prefer evidence work over disposition churn.

---

## Appendix A — GMP seam sketch (candidate only)

`Governance_Migration_Protocol.md` (~182 KB) appears to combine:

| Possible part | Role | Touch frequency |
|---------------|------|-----------------|
| **A — Axiom amendment** | How Tier 1 Axiom / Charter-level change is proposed, reviewed, ratified | Rare |
| **B — Track A/B migration mechanics** | Classification and migration machinery used in ordinary session work | Common |

**Not done here:** no new filenames, no content move, no claim that the live file’s headings already form a clean cut. A pilot would: (1) quote live section anchors that belong to A vs B, (2) propose two target files or two top-level parts inside GMP, (3) run through normal review — including anything GMP itself requires for structural change.

Until then, treat GMP as one Tier 2 file with an internal complexity warning.

---

## Future experiment (not scheduled)

**Status 2026-10-06:** Partially exercised — first Full and Reduced CAP-meta-stale-01 runs filed as `Tests/Field_Logs/FL-20261006-cap-meta-stale-01.md` and `FL-20261006-cap-meta-stale-01-reduced.md`. This section remains a design note, not a claim that the full measurement program is complete.

**Early evidence (2026-10-06, reviewed):** On the one skill tested (stale-metadata detection/correction) and one seed pair, the Reduced run — which withheld `Repository_Integrity_Protocol.md` and `Operational_Conventions.md` — showed **no operational capability loss** (7/7, matching Full). This is a single-run, single-agent, PROVISIONAL result per the entries' own epistemic state, not Replicated, and it says something about *this one skill and seed*, not about RIP or Operational_Conventions generally — both remain Tier 1 in the classification table above, which is about structural role (naming, continuity, audit mechanics for the whole repo), not about whether any one bounded skill happens to need them. A second ablation (`FL-20261006-cap-meta-stale-03-secondary.md`) tested withholding the Field_Logs Index itself instead, and that *did* block the skill at stage 2 — confirming the Index, not RIP/Operational_Conventions, is what this particular skill actually depends on. Treat this as the first real data point toward Finding 1's and Finding 4's claims, not as grounds to revise either.

A later, deliberately bounded version of this exercise could stop classifying documents and
start testing capability directly: pick one small, checkable skill, run it under progressively
reduced configurations of `Admin/`, and measure what actually breaks rather than inferring it
from a file's stated Scope Boundary. This is a candidate for a future Field_Log / LE-0-class
run design — **not implemented, not scheduled, and not a commitment** — listed here only so a
later session doesn't have to re-derive the idea from scratch.

**Candidate bounded skill:** "Detect and correct stale repository metadata" (the Routing.md
path-count and Forge_Audit_Kit.md citation-staleness pattern this session already hit five
times is a ready-made real example, not a hypothetical one).

**Candidate measurement questions, for whoever designs the actual run:**
1. Can it detect the problem exists?
2. Can it locate the authoritative source to check against?
3. Can it distinguish historical/dated information from current information?
4. Can it propose a valid correction?
5. Can it avoid damaging historical evidence while correcting?
6. Can it detect secondary propagation (the same stale value repeated elsewhere)?
7. Can it verify its own correction against source, not just assert it?
8. Can it state what capability was lost when a given component was removed or unavailable?

Run this against the full `Admin/` set first as a baseline, then again under one or more
reduced configurations (e.g., without `Repository_Integrity_Protocol.md`, or without
`Operational_Conventions.md`). The result would be a genuine capability-loss measurement —
"these N questions failed, these M still passed" — rather than another tier label. That
distinction is the entire point of treating this as a future experiment and not a present
finding: nothing in this file has been tested that way yet.

---

## Explicit non-claims

- This file does not claim Tier 2 content is unimportant — only that it's deferrable for a *minimal* day-one POC character, which is a different claim from “safe to ignore during MAQT or physical runs.”
- This file does not propose specific target filenames, merge mechanics, or a migration sequence beyond the disposition option table and GMP seam sketch.
- The percentages and tier assignments reflect classification passes in one day; treat as a first cut under the recompute rule, not a finished audit.
- This file does not advance Spec Gates, close Unknowns, or replace Field_Logs evidence.

---

## Resolution Log

- 2026-10-06: Future experiment section marked **partially exercised** after CAP-meta-stale-01 Full + Reduced Field_Logs; no Spec Gates advanced; tiers remain hypotheses.

- 2026-10-06: **"Early evidence" note added** after the Future experiment section's status line,
  as part of a review pass on the day's six Field_Log entries. Scoped deliberately: states what
  the Reduced-vs-Full and Reduced-Secondary ablations showed for the one skill/seed tested,
  explicitly PROVISIONAL and single-run, and explicitly **not** grounds to change either RIP's
  or `Operational_Conventions.md`'s Tier 1 classification above. No table row, tier, or Totals
  figure changed by this entry. Human-directed.

- 2026-10-04 (second integration pass): ChatGPT reviewed the prior state and proposed a
  Capability 0–4 ladder (self-maintenance → self-model → controlled degradation →
  self-directed experimentation) framing this file as early capability decomposition.
  Grok assessed the review and recommended two small, instrument-scale integrations rather
  than the full ladder. Claude reviewed both, agreed with Grok's scope caution, and flagged
  one additional precision point not caught by either: ChatGPT's framing of the Tier 1/2
  arithmetic correction as "a miniature of Capability 1 self-maintenance" overstated what
  happened — a human-initiated, Grok-drafted recomputation that Claude verified and applied,
  not autonomous self-correction. That framing was deliberately **not** adopted, specifically
  because it would have been this file doing the exact thing it warns against two sections
  later: letting a hypothesis (autonomous self-maintenance) read as a demonstrated capability.
  Two integrations applied: (1) a "Future experiment (not scheduled)" section naming
  ChatGPT's 8-question bounded test for "detect and correct stale repository metadata" as an
  explicitly unimplemented candidate, tied to this session's own real stale-metadata pattern
  (Routing.md path counts, FAK citation staleness) rather than a hypothetical example;
  (2) one line added to Scope Boundary's DOES-NOT list stating tier assignments are
  hypotheses about load-bearing structure, not a demonstrated capability inventory. The
  FORGE SELF-MODEL diagram and the full Capability 0–4 ladder were explicitly not adopted as
  file content — named here as considered and declined, so a future session doesn't
  re-propose them without knowing that choice was already made deliberately. Human-directed.

---
- 2026-10-04 (integration pass): Added Methodology **recompute rule**; **Deferral costs** table for all Tier 2 files; **Disposition options** for Tier 3/4; **Appendix A** GMP seam sketch; navigation link to `Adm_Scope_Map` load-bearing map; File Purpose note that this is instrument not revolution. No Admin files merged, split, or deleted. Human-directed draft integration.

- 2026-10-04 (same day, follow-on): Finding 3 core-size claim corrected 13 files/~772 KB → **12 files/~857 KB** after Tier 1/2 Totals arithmetic fix (6+6, 527+330).

- 2026-10-04 (same day): Totals line corrected — Tier 1 7/245 → 6/330; Tier 2 14/653 → 15/667; dated note under Totals. Propagated correction to `Adm_Scope_Map.md` load-bearing map.

- 2026-10-04: File created. Direct response to a request to "tear down the repo into minimized components to rebuild into what must exist," scoped to `Admin/` governance files specifically after clarifying that physical G.E.C.K. teardown (already covered by `Architecture/Geck_forge_seed.md`) was not what was meant. All 33 `Admin/` files' own Scope Boundary and Status fields read directly before classifying — not inferred from filenames. Human-directed, Claude-authored.
