# Metrics_Scaffold.md — LazarusForge

## Navigation Anchors
[README.md](../README.md) | [Discovery.md](../Discovery.md) | [Routing.md](../Routing.md) | [Unknowns.md](../Unknowns.md) | [Admin/Progress_Log.md](Progress_Log.md)

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Active — Scaffold Only (no data collection required yet)            |
| Spec Gates       | N/A — this file defines a measurement taxonomy, not a specification |
| Open Unknowns    | 0                                                                     |
| Owning Domain    | Admin/                                                                |
| Last Reviewed    | 2026-09-24                                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present.   |

---

## Purpose

Created 2026-09-24 to close the Lane C ("Make it learn," per `Admin/Progress_Log.md`'s Forward Growth Avenues) gap between having a stated ambition — measure the Forge's own effectiveness — and having anywhere defined to put a measurement once one exists. Pure documentation. Every counter below starts empty; nothing here requires backfilling history or standing up new tooling.

**This file DOES:**
- Define what each Lane C metric counts, its unit, its start/stop or inclusion boundary, and its log location, precisely enough that two independent agents would count the same event the same way.
- State the minimum viable one-line record format for when a metric is first populated.

**This file does NOT:**
- Collect, compute, or report any data itself — it is a taxonomy, not a dashboard.
- Modify, extend, or depend on `Automation/AUDIT_HARNESS.py` or `Automation/integrity_check.py`. Those remain the integrity layer (cross-reference resolution, File State/Ethical Anchor enforcement, unknown aging, version-string drift); this file is the feedback/measurement layer. The two are orthogonal and neither reads the other.
- Duplicate `Unknowns.md`'s Active Index — Unknowns-opened/resolved counts already live there and in `Archive/Logs/Unknowns_Changelog.md`; this file only names them as governance metrics for completeness and points back rather than restating.
- Invent numeric targets, thresholds, or scoring. No metric here implies a pass/fail bar.
- Expand into knowledge-substrate work beyond the already-ratified Claim-Type Labels (`Admin/Canonical_Terms.md` §4) — a metric's own value is not itself claim-typed by this file.

---

## 1. Development metrics

| Metric | Definition | Unit | Start / Stop | Log location | Edge notes |
|--------|------------|------|--------------|--------------|------------|
| **Time-to-proposal** | Elapsed wall-clock from a clear, actionable question/task to the first reviewable proposal. | hours (or days if >24 h) | **Start:** first message/prompt that states the concrete question or deliverable. **Stop:** first artifact complete enough to enter review. | Progress_Log session entry or `Tests/Field_Logs.md` | Later revision time is excluded. Only the first proposal interval is counted even if later rejected. |
| **Review cycles per change** | Number of complete propose → review → (revise or reject) loops a single change undergoes before a terminal state. | integer count | One cycle ends on acceptance, rejection, or an acted-upon revision request. | Owning file's Resolution Log + optional Progress_Log summary | Multi-agent comments in one round = one cycle. Cosmetic-only edits do not start a new cycle. |
| **Rejected vs accepted** | Ratio of proposals that receive an explicit terminal reject decision to those that receive an explicit accept/ratify decision. | count / ratio | Only proposals that reach a formal decision are counted. | Progress_Log or a simple running table | Abandoned or still-open items are excluded. Partial acceptances count as accepted for the ratified portion. |
| **Contradictions / stale references discovered** | Genuine cross-file contradictions or references to non-existent/superseded content found during audits or normal work. | integer count | Counted when first identified and logged. | Progress_Log "Current Lessons" or audit notes | Tag "found & fixed same session" vs "found & left open." False positives later removed. |
| **Human intervention count per cycle** | Distinct occasions on which Human Governing Authority must act to unblock, override, ratify, or decide something agents could not resolve alone. | integer count | One intervention = one human decision or action event. | Progress_Log or MAQT §8.10 Collaboration Friction Log | Includes ratifications and escalations. Routine acknowledgements that add no new information are not counted. |
| **Agent-generated defects caught vs missed** | Defects introduced by an agent that were later detected, versus those that remained in committed text until a later session. | two counts + ratio | "Caught" = detected/corrected before or during next independent review. "Missed" = present in committed/shared artifact and found later. | Progress_Log or audit notes | Style preferences are not defects. Same-agent fixes inside one continuous drafting pass are not counted. |

## 2. Governance metrics (partially already live)

| Metric | Definition | Current home | Scaffold note |
|--------|------------|--------------|----------------|
| **Unknowns opened** | New entries added to the Active Index in `Unknowns.md`. | `Unknowns.md` + `Archive/Logs/Unknowns_Changelog.md` | Already exists; no change needed. |
| **Unknowns resolved** | Entries removed from the Active Index by any recognized Payment type. | `Unknowns.md` + `Archive/Logs/Unknowns_Changelog.md` | Already exists. |
| **Unknowns falsely closed & later caught** | Closures subsequently shown to have been premature, incomplete, or incorrect. | Progress_Log or owning-file Resolution Log | Log original closure date, discovery date, and corrective action. |
| **Policy/procedure conflicts discovered** | Cases in which two or more doctrines give incompatible instructions for the same situation. | Progress_Log or owning-file Resolution Log | Record the conflicting IDs and the disposition. |

## 3. Physical metrics (placeholder only)

- Predicted vs measured performance
- Material efficiency, failure rate, repairability

These remain empty until Lane B produces `Tests/Field_Logs.md` data. No further definition work required now.

## 4. Minimum viable record format

When any metric above is first populated, use a one-line entry:

```
YYYY-MM-DD | Metric-name | value | short context or link | actor
```

Example (illustrative only — not a real recorded measurement):
```
2026-09-24 | Time-to-proposal | 2.5 h | Lane C Metrics Scaffold draft | Grok
```

No dashboard, no automation, and no new unknown are required. The scaffold exists so the first real measurement has a defined place to land.

---

## Resolution Log

- 2026-09-24: **File created.** Lane C metrics scaffold — nine development/
  governance metric definitions plus a physical-metrics placeholder and a
  minimum viable one-line record format. Pure documentation; no data
  collection performed by this file. Explicitly orthogonal to
  `Automation/AUDIT_HARNESS.py` / `Automation/integrity_check.py` (verified:
  neither tool currently tracks any Lane C development metric, maintains
  running counters, or references Claim-Type Labels — confirmed by direct
  source check before filing, not assumed). Registered in `Routing.md`,
  `Discovery.md`, and `Admin/Adm_Scope_Map.md` same day. Proposer (Grok —
  initial scaffold, refined definitions, final ready-to-paste block, and
  the Automation/ orthogonality survey), Verifier (Claude — confirmed the
  Automation/ "what these tools do / do not do" claims directly against
  `AUDIT_HARNESS.py` and `integrity_check.py` source; no correction
  required). Human-directed.
