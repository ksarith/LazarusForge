# Chaos_Dynamics.md

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)
---

## File State

| Field            | Value                                                               |
|------------------|-----------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-07-05 — Claude added first Sandbox Log entries (SB-001–SB-004); no formal Skeptic/Auditor sign-off through Forge_Audit_Kit.md opening sequence yet |
| Auditor          | None formal yet — see Last Audit and Active Disputes                |
| Open Unknowns    | 0                                                                   |
| Active Disputes  | 1 (CD-DS-001, Resolved same session — see below)                    |
| Highest Risk     | Medium — gatekeeps the evidentiary pipeline feeding EN-001/EN-001a; misuse risk if sandbox output is cited past its Level ≤4 ceiling |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

*(per `Admin/Repository_Structure.md`)*

**This file DOES define:**
- Exploration/R&D processes, promotion/demotion gates, EN-005 resolution vehicle, feeder to EN-001a.

**This file DOES NOT define:**
- Cognition doctrine, entropy philosophy, or derating data.

**Folder:** Tests/.

---

## File Purpose

This file exists to give the repository a disciplined pipeline from informal exploration to physical evidence — protecting imaginative freedom (no idea needs pre-approval to be tried in the Sandbox) while enforcing evidentiary integrity (no Sandbox hypothesis can become an engineering claim without passing through physical Level 5/6 testing). Without this file, exploratory hypotheses like the four EN-001 material-category questions in §9 would have no home between "someone's idea" and "a formal EXP-ID," and there would be no institutional memory preventing the same dead end from being investigated twice.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | A two-cycle cap on inconclusive re-testing is the right balance between giving a hypothesis a fair second look and preventing unbounded consumption of physical material and operator/agent bandwidth | Judgment call made 2026-07-04 in response to Gemini's resource-exhaustion GAP finding; no data yet exists on whether two cycles is too few or too many in practice | Medium | First real Epistemic Block degradation occurs — review whether two cycles was sufficient |
| ASM-002 | The lightweight SB-### ID scheme (file-scoped, not repository-wide provenance) is sufficient for now, and the fuller UNK→HYP→EXP→EN-001a provenance chain ChatGPT proposed remains genuinely premature | Judgment call, 2026-07-04 — deliberately deferred rather than built ahead of real usage data | Medium | The Sandbox Log has processed enough real hypotheses that cross-linking friction becomes a practical problem |
| ASM-003 | The Sandbox → EXP-ID → feedback pattern used here will generalize cleanly to ME-001 (`Architecture/Mechanical_Structures.md`) if adopted there | Stated as "flagged for future consideration" (§8) — not yet tested against a second file's actual unknowns | Low | ME-001 pattern adoption is attempted and either confirms or breaks this assumption |

---

## Body

### 1. Purpose (Operational Summary)

Disciplined pipeline from informal exploration → physical evidence. Protects imaginative freedom while enforcing evidentiary integrity. See §7 for the governing Operational Invariant.

### 2. Hierarchy of Evidence

Sandbox ≤ Level 4 (hypotheses only). Promotion requires physical Level 5/6 work.

### 3. Exploration Phase (Sandbox)

Before starting new exploration, check the Sandbox Log (§9) for prior entries on the same or adjacent hypothesis — the log exists specifically to prevent repeated investigation of previously explored dead ends. If a matching Discarded or Deferred entry exists, review it before proceeding; do not silently duplicate it.

Outputs = engineering *questions*.
Every artifact terminates in: **Discarded** | **Deferred** | **Promoted** (→ EXP-ID proposal). All three dispositions are recorded in the Sandbox Log (§9) — none of them mean the artifact disappears.
No direct path to guidance, rules, or claims.

### 4. R&D Phase & EXP-ID Lifecycle

**EXP-ID minted at Promotion** (from Sandbox) or Intake. All physical material, data, and records reference this ID from the first step onward.

Pipeline (with ID stamped early):
**Intake (EXP-ID assigned)** → NDE → Sampling → Destructive Testing → Statistical Analysis → Derating Recommendations → Update `Admin/Experiments.md` + originating Sandbox record.

### 5. Promotion / Demotion & Feedback Loop

**Promotion:** Sandbox hypothesis → EXP-ID proposal → physical execution.

**Feedback Requirement (on EXP-ID completion):**
Update originating sandbox hypothesis (if any) with:
- **Confirmed**
- **Partially Confirmed**
- **Refuted**
- **Inconclusive**

**Mechanics:**
- Keep original hypothesis intact + append refutation/confirmation data (prevents re-exploration of dead ends).
- **Deferred-item reuse:** When a Deferred sandbox hypothesis is revisited, update its existing Sandbox Log entry (§9) in place — append the new activity and outcome — rather than creating a new entry. Mirrors `Unknowns.md`'s Reopened-status handling: revisiting isn't a fresh start, it's a continuation of the same record.
- **Inconclusive results:** Automatic trigger for a maximum of **two** re-test cycles with refined parameters. If the hypothesis remains unresolved after two cycles, it automatically degrades to an **Epistemic Block** — physical testing on that specific hypothesis halts, and the state is logged as a non-blocking entry in `Unknowns.md` (escalate to Critical only if the hypothesis is itself safety-relevant; routine inconclusive results do not inherit Critical severity by default). This cap exists to prevent unbounded consumption of physical material, fuel, and operator/agent bandwidth on a premise that has twice failed to resolve.
- Refuted hypotheses remain visible (with clear physical counter-evidence) for institutional memory.

### 6. Unknown Generation

New uncertainties exposed during exploration are logged as `Unknowns.md` entries following that file's standard registration procedure (owning-file sidecar first, index second). Verification still requires the full pipeline in §3–§5 regardless of how an uncertainty was surfaced.

A Discarded or Refuted sandbox hypothesis and a newly-registered Unknown are not mutually exclusive. A specific hypothesis can fail (and be logged Discarded/Refuted in the Sandbox Log, §9) while still surfacing a genuine, separate uncertainty worth tracking in `Unknowns.md` — e.g., a hypothesis about a specific joint geometry can be wrong while still revealing that no one knows how a whole material category behaves. Disposition in §9 and registration in `Unknowns.md` are independent events; neither implies the other.

### 7. Operational Invariant

> Exploration capacity shall never be constrained by current engineering certainty; however, engineering certainty shall never be increased by exploration alone.

### 8. Reconciliation & Cross-File Status

- **EN-005** (owning file: `Architecture/Engineering.md`) — this file establishes the general process framework EN-005 asked for. Status is held at **In Progress / Vehicle** in Engineering.md's own sidecar, *not* Resolved — full resolution requires a completed EXP-ID cycle producing a concrete Level 5/6 test definition for at least one component type. This file does not have standing to unilaterally close another file's unknown; Engineering.md's sidecar is the authoritative status, not this section.
- **EN-001 / EN-001a** (owning file: `Architecture/Engineering.md`) — this pipeline is the intended feeder for EN-001a's characterization data once that split is formally registered in `Unknowns.md`. As of 2026-07-05, SB-001 through SB-004 (§9) are the first real hypotheses registered against this pipeline, one per EN-001 material category — currently Deferred pending physical testing capability, not yet promoted to EXP-ID.
- Pattern reusable for **ME-001** (owning file: `Architecture/Mechanical_Structures.md`) — not yet adopted there; flagged for future consideration, not an active dependency.

### 9. Sandbox Log

Every sandbox artifact is recorded here at disposition — Discarded, Deferred, or Promoted — regardless of outcome. This is the mechanism that makes §3's "no direct path to guidance" doctrine compatible with institutional memory: exploration artifacts remain permanently discoverable after disposition, so no idea has to be investigated twice by someone who doesn't know it was already tried.

| SB-ID | Date | Hypothesis (one line) | Disposition | Note |
|-------|------|------------------------|--------------|------|
| SB-001 | 2026-07-05 | Unknown-grade structural steel salvage, tested to yield/failure in tension and bending, will meet or exceed mild-steel-equivalent yield strength in ≥90% of samples drawn from typical Forge input streams (framing, angle stock, rebar-class material) | Deferred | From `Architecture/Engineering.md` EN-001. Would validate/tighten the interim 4× factor. Test sketch: minimum 10 samples across visually-distinct sources, tension test to failure, record yield/ultimate/elongation, compare against mild-steel baseline. Deferred pending confirmation of physical testing capability (tensile test rig or equivalent access) — see Engineering.md EN-001 Resolution Path. |
| SB-002 | 2026-07-05 | Unknown-alloy aluminum extrusion salvage shows yield-strength variance ≥3× across samples when grouped only by visual/magnetic sorting (i.e., confirms alloy series cannot be reliably distinguished without testing, justifying the 6× floor rather than a reduction) | Deferred | From `Architecture/Engineering.md` EN-001. This hypothesis, if confirmed, justifies keeping the 6× factor rather than lowering it — a valid and useful outcome either way. Test sketch: minimum 10 samples, hardness test (cheap proxy) cross-checked against tension test on a subsample, group by visual similarity, measure within-group variance. Deferred pending physical testing capability. |
| SB-003 | 2026-07-05 | Salvaged timber, screened first by moisture content (<19%) and visual/probe rot inspection, shows bending-strength variance narrow enough to support a factor below 5× for the screened subset (i.e., the mandatory inspection step in EN-001's table is doing most of the real risk reduction, and screened material may not need the full margin) | Deferred | From `Architecture/Engineering.md` EN-001. Test sketch: minimum 10 screened samples spanning at least 3 species, 3-point bend test to failure, compare variance within screened set against published unscreened-salvage variance. Deferred pending physical testing capability. |
| SB-004 | 2026-07-05 | A low-cost field identification protocol (magnet test + spark test + density/float test, per `Operations/Gate_02_Triage.md`) can correctly sort ≥95% of an unidentified scrap-metal sample set into steel/aluminum/other-with-caution categories without lab equipment | Deferred | From `Architecture/Engineering.md` EN-001's "unidentified material — barred until classified" row. If confirmed, this converts the current hard bar into a practical field-triage step rather than an indefinite block. Test sketch: assemble a mixed sample set of known-identity scrap, apply the three-test protocol blind, score against ground truth. Deferred pending physical testing capability. |

**Schema notes:**
- **SB-ID** — sequential (`SB-001`, `SB-002`, ...), scoped to this file only. This is a lightweight reference ID for cross-linking within the Sandbox Log and from Promoted entries to their resulting EXP-ID — it is not a repository-wide provenance chain. (A fuller UNK→HYP→EXP chain was proposed separately this session and deliberately deferred — see Resolution Log.)
- **Discarded** entries: hypothesis + one-line reason. No further tracking expected.
- **Deferred** entries: hypothesis + the specific condition that would justify revisiting it (not just "later"). Updated in place on reuse per §5's Deferred-item reuse rule — never duplicated.
- **Promoted** entries: hypothesis + the resulting EXP-ID. Full detail lives in `Admin/Experiments.md`; this row is a pointer, not a duplicate record.
- **Search-first duty:** per §3, check this table before starting new exploration on a hypothesis that might already have an entry.

**Size management — placeholder, not yet specified:** this table grows by design and will eventually need a compression or graduation trigger, similar to `Unknowns.md`'s 1,200-line rule or Engineering.md's EN-006 150-line split trigger. No specific threshold is set here — inventing one now, before any real growth data exists, would be the same "confidence without basis" problem flagged elsewhere this session. Revisit once the table has real entries to size against.



---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|---|---|---|---|---|---|---|
| — | — | — | — | No entries yet — no hypothesis has completed a full Sandbox → EXP-ID → feedback cycle | — | — |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status |
|----|-----------------|------------------------|------|--------|
| CD-DS-001 | Gate 5 and Gate 2 severity across three same-day independent audits (Gemini, Grok, ChatGPT) | Gemini: G5 **HOLD** (flat legacy cross-references), G2 conditional on an uncapped inconclusive-retest loop. Grok: both **Pass**, no issues raised — but Grok's stated basis for G5 ("uses canonical paths") did not match the file's actual text at time of audit. ChatGPT: G5 minor documentation-consistency note only; loop cap not raised. | Low | **Resolved 2026-07-04** — see below |

**Resolution (applying the Gate Scope vs. Promotion Readiness precedent established for SEC-DS-001, `Admin/Security_Protocols.md`):** G5 = Pass. The flat legacy paths (`Repository_Structure.md`, `Experiments.md`) resolve correctly through `AUDIT_HARNESS.py`'s ALIASES table — they were non-canonical phrasing, not broken references, so Gemini's HOLD overshoots; ChatGPT's calibration was closer. Corrected to canonical form in this revision regardless (§Scope Boundary, §4). G2 = Pass. No physical claim exists in this doctrine-only text for G2 to falsify — Gemini's resource-exhaustion concern is real but describes *future* execution-time behavior, not a present physical-plausibility violation. The missing cycle cap is treated as a now-closed non-blocking GAP (§5, this revision) rather than a gate failure. Grok's audit is noted as having stated a cross-reference claim inconsistent with the file's actual contents at the time — flagged for calibration, not treated as evidence either way.

---

## Auditor Notes & Unknowns

No unknowns are currently open under this file's own ownership. EN-001, EN-001a, and EN-005 are referenced in §8 but owned by `Architecture/Engineering.md` — see that file's sidecar for authoritative status. First unknowns native to this file are expected once a hypothesis completes a full Sandbox → EXP-ID → feedback cycle for the first time.

### Resolution Log

- 2026-08-11: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **0** — matches File State; no native
  unknowns until Sandbox → EXP-ID → feedback cycle completes (per file
  doctrine). (2) CD-DS-001 already **Resolved**. (3) No new unknowns
  registered; no Level-ceiling claims advanced. Human-directed.

- 2026-07-12: Template-skeleton backfill: converted embedded Scope Boundary to a standalone `##` section, added standalone File Purpose and Assumptions sections, wrapped the numbered §1–§9 body under a `## Body` header (demoted to `###`, retitled §1 to avoid duplicating the new File Purpose section), added standalone Lessons Learned and Active Disputes headers (the CD-DS-001 table previously had no owning header), and added Abandoned Paths and Drift Indicators. No numbered-section content, Sandbox Log entries, or dispute resolution text changed — preserves this file's mature §1–§9 doctrine intact, matching the precedent set by `Admin/Auditor_Protocols.md` (protocol files keep custom body structure inside the standard outer skeleton).

- 2026-07-05: **First real Sandbox Log entries — SB-001 through SB-004.**
  Four hypotheses registered, one per material category in
  `Architecture/Engineering.md` EN-001's new differentiated safety factor
  table (structural steel, aluminum, timber, unidentified-material field
  triage). All four logged **Deferred** — pending confirmation of physical
  destructive-testing capability, not yet promoted to EXP-ID or physically
  executed. This is the pipeline's first use since §9 was built 2026-07-04;
  everything in §9 prior to this was schema with zero entries. §8
  Reconciliation note updated to reflect it. No unknowns native to this
  file yet — per this file's own doctrine, that's expected until a
  hypothesis completes a full Sandbox → EXP-ID → feedback cycle, which
  hasn't happened yet.

- 2026-07-04 (second entry, same day): Added §9 Sandbox Log, implementing ChatGPT's
  "exploration artifacts remain permanently discoverable" suggestion. This exposed
  a real gap rather than being pure doctrine-polish: §3 already promised three
  dispositions (Discarded/Deferred/Promoted) but only Promoted artifacts had
  anywhere to go (an EXP-ID). Discarded and Deferred artifacts had no record at
  all prior to this entry. Added: the log table itself (schema only, zero
  entries — same "stub, absence isn't evidence of anything" posture Experiments.md
  already takes); a lightweight SB-### ID scoped to this file only (deliberately
  smaller than the fuller UNK→HYP→EXP→EN-001a provenance chain ChatGPT floated
  earlier this session — that remains deferred as premature infrastructure until
  the pipeline has processed at least one real hypothesis); a check-first
  instruction in §3; a Deferred-item-reuse rule in §5 (update in place, mirroring
  Unknowns.md's Reopened status rather than duplicating); and a one-sentence
  clarification in §6 that a hypothesis's disposition here and a separate
  Unknowns.md registration are independent events. Size-management trigger for
  the table is explicitly left unspecified pending real growth data, rather than
  guessing a threshold now.
- 2026-07-04: Full revision following three independent audits (Gemini, Grok, ChatGPT) run same day, before this patch. Canonical paths corrected (§Scope Boundary, §4). Inconclusive-retest loop bounded to two cycles with automatic Epistemic Block degradation (§5) — closes Gemini's resource-exhaustion GAP without adopting her G2-blocking severity. EN- prefix ownership made explicit inline (§8) rather than registering a new tracked unknown (CD-UNK-001 not adopted — Unknowns.md's Active Index already unambiguously owns this). §8's "EN-005 resolved here" language softened to explicitly defer to Engineering.md's sidecar (In Progress/Vehicle) rather than self-declaring closure — addresses Gemini's Resolved-Unknown-Discharge-Procedure contradiction finding. Duplicated Operational Invariant text (previously in both §1 and §7) trimmed to a single canonical location (§7), per Grok's and this session's prior note. Navigation Anchors block and File State table added — previously entirely absent. CD-DS-001 logged and resolved same session per the Active Disputes table above.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|---|---|---|---|
| 2026-07-04 | Fuller UNK→HYP→EXP→EN-001a repository-wide provenance chain (ChatGPT proposal) | Judged premature infrastructure — the pipeline hadn't processed a single real hypothesis yet at the time. Building a heavyweight chain ahead of real usage data risked guessing wrong about what cross-linking is actually needed. | Yes — once the Sandbox Log has enough real Promoted entries that the lightweight SB-### scheme starts creating cross-linking friction |
| 2026-07-04 | Self-declaring EN-005 Resolved from within this file | This file establishing the general process framework EN-005 asked for is necessary but not sufficient for EN-005's resolution — Engineering.md's own sidecar is the authoritative owner. Self-declaring closure would have violated ownership boundaries. | No — status changes belong in Engineering.md, not here |

---

## Drift Indicators

- Body treats a Sandbox hypothesis's disposition (§9) as equivalent to Unknowns.md registration, or vice versa — §6 explicitly holds these as independent events
- A hypothesis is promoted to EXP-ID without a Sandbox Log entry recording the promotion and resulting EXP-ID
- The two-cycle inconclusive-retest cap (§5) is exceeded without triggering Epistemic Block degradation
- This file declares another file's owned unknown (e.g., EN-001, EN-005) Resolved rather than deferring to that file's sidecar
- Sandbox Log entries accumulate without any size-management trigger being proposed once real growth data exists (currently deliberately unset — see Assumptions)
- Ethical Anchor field is absent, altered, or does not match the canonical string

---
*Last updated: 2026-07-12.*
