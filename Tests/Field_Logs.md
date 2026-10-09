# Field_Logs.md

## Navigation Anchors
[README.md](../README.md) | [Discovery.md](../Discovery.md) | [Routing.md](../Routing.md) | [CONTRIBUTING.md](../CONTRIBUTING.md) | [Hardware_Diversity_Ladder.md](../Admin/Hardware_Diversity_Ladder.md)

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Active — Index                                                      |
| Spec Gates       | N/A — this file is an index, not a specification                    |
| Open Unknowns    | 0                                                                    |
| Body Stability   | N/A                                                                  |
| Owning Domain    | Tests/                                                               |
| Last Reviewed    | 2026-10-03                                                          |
| Sidecar Link     | N/A                                                                  |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES:**
- Provide the submission format and format contract for real-world test runs — physical fabrication attempts, cross-agent sessions, hardware-diversity trials, or any activity that generates evidence this repository doesn't have yet.
- Serve as the index into `Tests/Field_Logs/` — one file per submission (see Restructure Note below). This file lists every entry; it does not contain entries itself.

**This file does NOT:**
- Resolve any Unknown, advance any Status, Spec Gate, or Body Stability field on its own. A field-log entry is raw evidence. Folding it into the doctrine it's relevant to — and updating that doctrine's own Resolution Log — is a separate, deliberate step, done after the entry is reviewed against source (see `Admin/Auditor_Protocols.md` Rule 6 and the fabrication-vigilance pattern logged there 2026-08-06).
- Require a fork, pull request, or GitHub account. See submission instructions below.
- Hold field/run evidence entries directly as of 2026-10-03 (see Restructure Note). `Archive/Transcripts/` is a separate, distinct bucket for raw AI session dumps — field/run evidence does not belong there; this file's entries live in `Tests/Field_Logs/` instead.

---

## Why This Exists

As of 2026-08-06, every physical-hardware and multi-agent-quorum unknown in this repository — `Hardware_Diversity_Ladder.md`'s Tier 1–3, `Admin/Governance_Migration_Protocol.md` §VII (GOV-008), the entire CSL hard-unknown set — is blocked on the same thing: nobody has actually run the hardware. This file exists so that when someone does, the result has somewhere honest to go, in a format the repository's existing audit discipline can actually use.

An unlabeled, undated claim is not evidence — it's a Placeholder as soon as it's written, per `Discovery.md`'s Evidence Classification doctrine. This template exists to prevent that outcome.

---

## Restructure Note (2026-10-03)

Entries used to be appended directly below, in this one shared file. That created a real collision risk for the exact low-friction, no-GitHub-account submission path this file promotes: two people editing the same file via the GitHub web editor without pulling latest first produces a conflicting commit. As of this date, entries are filed one-per-file instead — see **Submission Format** and **How to Submit** below for the current process. This file (the Scope Boundary, Submission Format, Evidence Classification tie, and the guidance sections below) is unchanged in purpose; only where entries physically live has changed.

---

## Submission Format

Each entry — human-run, agent-run, or mixed — gets its own file in `Tests/Field_Logs/`, named:

```
FL-YYYYMMDD-shortslug.md
```

If that exact filename already exists (two submissions same day, similar topic), append a disambiguator: `FL-YYYYMMDD-shortslug-2.md`, or use initials/time (`FL-YYYYMMDD-shortslug-jrs.md`). This is rare in a solo or small-team setting, but costs nothing to state up front.

File contents:

```
**Entry ID:** FL-YYYYMMDD-shortslug
**Status:** Unreviewed

### [YYYY-MM-DD] — [Short Title]

**Submitted by:** [name, handle, or "anonymous"]
**Run type:** [physical fabrication / cross-agent quorum trial / hardware-diversity test / other]
**Hardware involved:** [what ran where — see Hardware Independence Test in
  Hardware_Diversity_Ladder.md if claiming physical diversity; anti-spoofing
  checks apply — a container on one machine is not two hosts]
**Agents involved:** [which agent(s)/model(s), and whether they were given
  a role declaration per Admin/Forge_Audit_Kit.md before starting]
**What was attempted:** [plain description]
**What actually happened:** [results, including failures — a failed run
  logged honestly is worth more than a success claimed without detail]
**Evidence label:** [Measured / Replicated / Simulated / Analogous /
  Placeholder — per Discovery.md's Evidence Classification. Unlabeled
  entries are treated as Placeholder by default.]
**Relevant Unknown IDs:** [if this touches a known unknown — GU-005,
  EN-001, GOV-008, etc. — list them; if unsure, leave blank, a reviewer
  will cross-reference]
**Raw data / files:** [attach or link if applicable]
```

Entries don't need to be polished. A partial run, a failed test, or a single-host trial that didn't reach real hardware diversity are all worth logging — the pattern across attempts matters more than any single result, same principle as FRT's own logging doctrine in `Admin/Trajectories.md`.

**Status field values:** `Unreviewed` | `Reviewed — folded into [doctrine file]` | `Reviewed — no action`.

**Status ownership:** whoever folds an entry into doctrine (or explicitly closes it as no-action) updates **both** the entry file's Status line and this file's index row, in the same edit pass as the doctrine change — not as a follow-up. Same discipline as `Admin/Operational_Conventions.md` Convention 8. A mismatch between an entry file's Status and its index row is a drift indicator on this file.

---

## How to Submit (no GitHub experience required)

1. Fill out the format above for your run.
2. Send it — as a pasted message, a text file, or a zip with any raw data — through whatever channel you're already using to reach the project maintainer (e.g. the r/InnovativeAIChats thread, or directly).
3. If you're comfortable with GitHub: create a new file under `Tests/Field_Logs/` named per the convention above, or open an Issue with your entry pasted in. Neither is required. If you create the file directly, also add a row for it to the Index table below and register the new file's path in `Routing.md`, in the same commit/pull request — this keeps the index and the routing map from drifting out of sync with the actual files.

No fork is needed for this. Forking makes sense for parallel, divergent development — this repository's actual bottleneck right now isn't code review, it's getting real hardware and multi-agent runs logged at all. A fork would split that evidence across multiple trees instead of building one honest, cross-referenceable record. If the project reaches a point where multiple people are doing genuinely independent architecture work rather than submitting test evidence, that recommendation should be revisited — not before.

---

## Suggested Starter — Lowest Barrier to Entry

The two sections below ask for real hardware or multi-agent access, which most
readers won't have yet. If you have neither but want to contribute something
real: **pure Intake + safety screening on 5–10 household items you already
own.** No processing, no thermal work, no fabrication.

What it needs: a flashlight, a basic multimeter, a phone camera, gloves and
eye protection, and something to write notes in. About 1–2 hours. Prefer
items without unknown batteries or sealed electronics for a first run.

What to do: run each item through `Operations/Gate_01_Intake.md`'s safety
screening as written — hazard identification first (energetic, chemical,
biological, radiological per GI-002's discharge doctrine and GI-003's
detection guidance), then attempt identification and a preliminary parts
list, then tag with provenance. Don't process past Intake in this run — the
point is exercising the screening step itself, not producing recovered
material.

What's actually useful to log: not just "it worked" — how many items you
held vs. cleared and why, how much judgment call was involved on the
ambiguous ones, anything you almost missed. That's the data GI-002/GI-003
need and can't get from doctrine alone. A short, honest log of five ordinary
household items beats an ambitious run that never gets submitted.

---

If you're looking for the single most useful thing to attempt: **three physically separate computers, each running a different agent (different model family on each), attempting to establish the quorum `Admin/Governance_Migration_Protocol.md` §VII defines — while one or more of them actively proposes real doctrine improvements to this repository.**

**Protocol (added 2026-09-18):** `Tests/Multi_Agent_Quorum_Trial.md` now defines the concrete machine baseline, role assignment, Git branch/promotion-authority model, required non-collusion probe, and pass/fail parameters for this run — run it under that protocol and log the result here rather than improvising the setup from this paragraph alone.

This is `Hardware_Diversity_Ladder.md` Tier 2 (Three-Host Architectural Diversity) attempted for real, not declared. It is also the first real evidence input `GOV-008` (still Open) has ever had a chance to receive. It will very likely fail to reach full quorum on the first attempt — that's fine and expected; a documented failure against Tier 2's actual requirements (distinct architectures, independent power, any-two-survive-loss-of-third) is exactly the kind of evidence this file exists to capture. Log it here regardless of outcome.

---

## Second-Highest-Value Run: Calibration Data for FN-001/FN-005

As of 2026-08-14, `Architecture/Forge_Net.md`'s data validation (DV-001–006) and data privacy (PA-001–006) Provisional Specs are both structurally complete — the remaining gap on both is the same one: numeric thresholds are Placeholder because no operational data has ever been generated to set them. A run doesn't need to be a full multi-forge network to produce this — it needs to generate contributions and conflicts a reviewer can measure. If attempting this, capture:

- **For DV-003 (confidence model):** observation count, source diversity (`independence_tag` values actually achieved — same_node / same_cluster / different_region / different_generation), and contradiction density for a batch of simulated or real contributions. Even a single-node dry run against a small seeded dataset is useful if it's honestly labeled Simulated, not Measured.
- **For DV-004 (conflict resolution):** at least one deliberately-induced conflicting contribution, to see whether minority-report preservation behaves as specified and what a reasonable "observation window" for a persisting contradiction actually looks like in practice.
- **For PA-002 (access control):** what trust-score range plausibly separates a new/unproven node from an established one, based on whatever contribution history the run produces — this doesn't need to be a final number, just a first real data point instead of an invented one.

Log this the same way as any other entry — **Evidence label** matters more here than usual, since the entire point is feeding a currently-Placeholder threshold with something honestly classified, not a confident guess dressed as data.

---

## Field-trial lifecycle stages

These stages describe **where a submission sits in the trial pipeline**. They do **not** replace Evidence Classification (`Measured` ≻ `Replicated` ≻ `Simulated` ≻ `Analogous` ≻ `Placeholder`). A submission always carries both: a lifecycle stage and an evidence-quality label.

| Stage | Meaning |
|-------|---------|
| **Submitted** | Entry accepted into this log; structure checked; claim not yet independently checked |
| **Reproducible** | Same procedure yields the same class of result on a second run or with a method clear enough to repeat |
| **Independently replicated** | Different operator or site; same claim survives |
| **Validated** | Folded into owning doctrine with an Evidence Classification update on the affected unknown or specification |

Examples of valid combinations: `Submitted` + `Measured`; `Independently replicated` + `Replicated`. Invalid: `Validated` + `Placeholder` (validation requires evidence quality above Placeholder).

**Failed trials are first-class.** A documented failure against real requirements is worth more than an unlabeled success claim. Prefer entries that name the claim tested, conditions, observed outcome, failure mode (if any), implication, and any Unknown affected.

## Ready-to-Run Cards

Procedure cards for tracks currently cleared to run — fill while running, file the result as a new `FL-YYYYMMDD-shortslug.md` entry per the Submission Format above. Cards are procedures, not entries, and don't get Index rows themselves.

| Card | Track | Evidence destination |
|------|-------|----------------------|
| `Tests/Field_Logs/RUN_CARD-LaneB-LogicZero.md` | Lane B — EL-006 v0 Logic-Zero admission | `FL-YYYYMMDD-logiczero-<mcu-or-board>.md` |
| `Tests/Field_Logs/RUN_CARD-LaneB-SalvageID.md` | Lane B — Salvage vs. `Chemistry.md`/`Components.md` classes | `FL-YYYYMMDD-salvage-<slug>.md` |
| `Tests/Field_Logs/RUN_CARD-LE0-Candidate.md` | LT-003 — LE-0 Phase 0–5, Candidate A or B | `FL-YYYYMMDD-le0-candA.md` or `...-candB.md` |
| `Tests/Field_Logs/RUN_CARD-MAQT-Tier2.md` | MAQT — three physical hosts | `FL-YYYYMMDD-maqt-tier2.md` |
| `Tests/Field_Logs/MAQT_C1_SESSION_PACKET.md` | MAQT Cycle 1 session packet (roles, probes, EC-013 task) | use with results template |
| `Tests/Field_Logs/RUN_CARD-MAQT-C1-Results.md` | MAQT-1 results template (§VII.3 + capability dimensions + friction) | `FL-YYYYMMDD-maqt-c1-ec013.md` |

| `Tests/Field_Logs/RUN_CARD-CAP-meta-stale-01.md` | Capability grade — stale metadata (operational stages 1–7 + separate ablation assessment) | `FL-YYYYMMDD-cap-meta-stale-01.md` |

## Index

*(One row per file in `Tests/Field_Logs/`. Columns: ID, Date, Title, Status, Path — kept minimal and literal; no free-text notes column, so this table can't drift into a second body the way other tables in this repository have.)*

| ID | Date | Title | Status | Path |
|----|------|-------|--------|------|
| FL-20261009-protocol-audit-runs | 2026-10-09 | Audit runs on the conduct protocol — drafter-entangled audit plus three Gemini runs on a seeded copy (1 invalid-unreadable, 1 invalid-role-breach, 1 valid: 1 of 3 planted faults caught) plus a ChatGPT run on a second planted set (valid: 3 of 4 caught) | Unreviewed | `Tests/Field_Logs/FL-20261009-protocol-audit-runs.md` |
| FL-20261007-recharacterization-proposal | 2026-10-07 | Public recharacterization — README/CONTRIBUTING replaced, Things_We_Got_Wrong.md added — framing only | Reviewed — accepted and ratified | `Tests/Field_Logs/FL-20261007-recharacterization-proposal.md` |
| FL-20261006-ave-sample-01 | 2026-10-06 | AVE first batch — 24 scored events, source-survival 21/24=0.875; thresholds remain Placeholder | Reviewed — no action | `Tests/Field_Logs/FL-20261006-ave-sample-01.md` |
| FL-20261006-cap-meta-stale-03-secondary | 2026-10-06 | CAP-meta-stale-01 Reduced-Secondary — withhold Field_Logs authority; stage 2 fail (Δ large) | Reviewed — folded into `Discovery.md` | `Tests/Field_Logs/FL-20261006-cap-meta-stale-03-secondary.md` |
| FL-20261006-cap-meta-stale-02 | 2026-10-06 | CAP-meta-stale-01 seed2 — Tst_Scope_Map Field_Logs-empty current-state claims (stages 1–7) | Reviewed — folded into `Tst_Scope_Map.md`, `Discovery.md` | `Tests/Field_Logs/FL-20261006-cap-meta-stale-02.md` |
| FL-20261006-cap-meta-stale-01-reduced | 2026-10-06 | CAP-meta-stale-01 Reduced ablation — withhold RIP+OpConventions; 7/7 operational, ablation Pass | Reviewed — folded into POC, run card fix | `Tests/Field_Logs/FL-20261006-cap-meta-stale-01-reduced.md` |
| FL-20261006-cap-meta-stale-01 | 2026-10-06 | CAP-meta-stale-01 Full Admin — Routing.md Last-updated header lag vs map body (stages 1–7) | Reviewed — folded into `Routing.md`, POC | `Tests/Field_Logs/FL-20261006-cap-meta-stale-01.md` |
| FL-20260815-gov021c-independence | 2026-08-15 | Cross-agent independence dimensions exercised live (High-Risk Unknowns tier) — GOV-021c evidence | Reviewed — folded into `Admin/Autonomy_Divergence_Protocol.md` GOV-021c | `Tests/Field_Logs/FL-20260815-gov021c-independence.md` |

## Resolution Log

- 2026-10-09: **Protocol audit runs filed** — `FL-20261009-protocol-audit-runs.md`. Index row added. ChatGPT run added the same day. No threshold calibration; one run per auditor.
- 2026-10-07: **Recharacterization merge** — `FL-20261007-recharacterization-proposal.md` filed; root README/CONTRIBUTING replaced; `Things_We_Got_Wrong.md` added. Index row Unreviewed pending human ratification of public framing.

- 2026-10-07: **MAQT-C1 session packet + results template** added under `Tests/Field_Logs/` (human-directed draft from ChatGPT MAQT-1 assessment; does not execute Cycle 1).

- 2026-10-06: **Review pass on all five same-day entries.** `FL-ave-sample-01` → Reviewed — no
  action, per `Agent_Verification_Event.md`'s own "Where to log" rule (routine batches belong
  here, not in a doctrine edit). The two `cap-meta-stale-01` Full/Reduced entries and the
  `-02`/`-03-secondary` entries → Reviewed, folded into the corrections they'd already driven
  (`Routing.md`, `Tst_Scope_Map.md`, `Discovery.md`, the run card's own metric fix). One
  discrepancy caught and annotated, not silently rewritten: `-01-reduced`'s submitted headline
  read "8/8," the pre-correction framing the same-day card fix was written to prevent — a
  Reviewer note was added clarifying the corrected reading (7/7 operational + ablation Pass)
  without altering the original submitted figure. A short "Early evidence" note was added to
  `Tests/Admin_Governance_Teardown_POC.md`'s Future experiment section, explicitly scoped to
  the one skill/seed tested — not a basis for retiering RIP or Operational_Conventions.
  Human-directed ("Please continue").

- 2026-10-06: **AVE sample 01 filed** — `FL-20261006-ave-sample-01.md` (24 scored; survival 0.875; no threshold calibration).

- 2026-10-06: **CAP stronger ablation** — `FL-20261006-cap-meta-stale-03-secondary.md`. Secondary-only config fails stage 2; Discovery history bullet clarified.

- 2026-10-06: **CAP seed2 filed** — `FL-20261006-cap-meta-stale-02.md` (Tst_Scope_Map Field_Logs-empty staleness).

- 2026-10-06: **CAP-meta-stale-01 Reduced ablation filed** — `FL-20261006-cap-meta-stale-01-reduced.md`. Withheld RIP + Operational_Conventions; stages 1–8; no stage 1–7 loss vs Full.

- 2026-10-06: **CAP-meta-stale-01 first run filed** — `FL-20261006-cap-meta-stale-01.md`. Full Admin, stages 1–7/8 (Measured/PROVISIONAL). Seed: Routing.md Last-updated header lag. Index row added.

- 2026-10-03: **Restructured from single-file append-only log to index + per-entry files**, following a Claude/Grok collision-risk review requested after the web-editor submission path was identified as a real conflict risk once more than one contributor is active. `Field_Logs.md` retained as the Scope Boundary / Submission Format / Evidence Classification contract and now an Index into `Tests/Field_Logs/`; entries moved to one file per submission there, named `FL-YYYYMMDD-shortslug.md`. The sole existing Log Entry (GOV-021c, 2026-08-15) migrated verbatim as the pilot — `Tests/Field_Logs/FL-20260815-gov021c-independence.md`. New Status field (`Unreviewed` / `Reviewed — folded into [doctrine]` / `Reviewed — no action`) added to the entry-file template; ownership rule modeled directly on `Admin/Operational_Conventions.md` Convention 8 — whoever folds an entry into doctrine updates both the entry file's Status and this file's index row in the same pass. Explicit non-goal stated: `Archive/Transcripts/` remains for raw AI session dumps only; field/run evidence stays under `Tests/Field_Logs/`, not merged into Transcripts by habit. `README.md`, `CONTRIBUTING.md`, `Routing.md`, and `Discovery.md` references updated in the same pass (see those files' own Resolution Log / Progress_Log entries). Done while the project remains solo-operated, specifically to be ahead of the collision risk rather than discovering it after a second contributor's commit conflicts. Human-directed, Grok-drafted recommendation, Claude-verified against the live tree before applying.

- 2026-09-18: **Cross-referenced `Tests/Multi_Agent_Quorum_Trial.md`** into the
  Suggested Starter / three-computer section — that new file now defines the
  concrete machine baseline, role assignment, Git authority model, required
  non-collusion probe, and §VII.3 pass/fail scoring for the run this file
  had previously only described in two sentences. No change to this file's
  own Scope Boundary — it remains results-intake only; the new file is
  where the protocol itself lives. Human-directed, following a ChatGPT
  multi-agent-readiness assessment of the same experiment.
- 2026-08-17: **Suggested Starter section added — lowest-barrier entry point
  for contributors without hardware or multi-agent access.** The existing
  Highest-Value Run sections both assume resources most readers won't have.
  Added a pure Intake + safety screening starter (5–10 household items,
  minimal tooling) drawing on `Operations/Gate_01_Intake.md` GI-002/GI-003's
  own doctrine — the point is exercising the screening step and logging
  judgment-call data, not producing recovered material. Human-directed.

- 2026-08-15: **First real Log Entry added — GOV-021c cross-agent
  independence-dimension evidence.** Prior entries in this Resolution Log
  were about the file's own structure (Highest-Value Run sections); this is
  the file's first actual submitted Log Entry under the Submission Format.
  Documents a real cross-agent case from this session assessed honestly
  against `Admin/Governance_Migration_Protocol.md` §VI's Three Independence
  Dimensions — two met and traceable, one (role independence) named as not
  fully met rather than rounded up. See `Admin/Autonomy_Divergence_Protocol.md`
  GOV-021c for the corresponding status update; that unknown remains Open,
  this is one data point. Human-directed.

- 2026-08-14: **Second Highest-Value Run section added — FN-001/FN-005
  calibration data.** `Forge_Net.md`'s DV-001–006 and new PA-001–006
  Provisional Specs reached the same terminal state the same day
  (structure complete, only numeric thresholds Placeholder). This file's
  existing guidance only pointed at GOV-008/Hardware Diversity Tier 2;
  nothing told a contributor what data would actually calibrate DV-003
  or PA-002. Added a scoped second section specifying concretely what
  to capture (observation count/source diversity for DV-003, an induced
  conflict for DV-004, a plausible trust-score range for PA-002) so a
  field run produces usable calibration data rather than an unlabeled
  claim. Does not resolve FN-001, FN-005, or GOV-008 — this file creates
  no unknowns and resolves none on its own, per its own Scope Boundary.
  Open Unknowns unchanged (0). Human-directed.

- 2026-08-11: **Pseudo-audit (Grok, same limits).** Findings only. (1) Open
  Unknowns **0** — matches File State (intake log, creates none). (2) Spec
  Gates N/A (log, not specification). (3) Append-only intake discipline
  intact; no field entries yet (expected). (4) No unknowns closed or
  invented. Human-directed.

- 2026-08-06: **File created.** No physical or cross-agent field data has
  ever been logged against this repository's doctrine; this file exists
  to give that data a place to go that the existing audit discipline
  (Evidence Classification, RIP append-only rules, Auditor_Protocols
  fabrication vigilance) can act on. Created in response to a direct
  question about how to invite physical testing without requiring PR
  literacy. Cross-referenced from `CONTRIBUTING.md`. Operating as
  Synthesizer, human-directed.
