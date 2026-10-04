# Run Card — LE-0 Phase 0–5 (single candidate)

**Source doctrine:** `Tests/Leviathan_testing.md` §VIII — LE-0 build-out  
**Pick exactly one:** Candidate **A** (reactive) or **B** (deliberative).  
**Evidence destination:** `FL-YYYYMMDD-le0-candA.md` or `...-candB.md`

**Success = reconstructable post-mortem that reduces uncertainty about that candidate — not survival.**

---

## Phase 0 — Setup (run card)

| Item | Fill |
|------|------|
| Candidate | A \| B |
| Energy bound (from §V Analogous) + derate basis | |
| Cold soak | yes / no (if no, LT-002 path stays open) |
| Sensor IDs (dual channels) | |
| Conflict type | ethical \| geo \| power |
| Load-shed thresholds | |
| Logger path / clock source | |
| Operator | |
| Date (UTC) | |

---

## Phases 1–5 checklist

| Phase | Done? | Notes |
|-------|-------|-------|
| 1 Baseline — ≥1 full decision-loop cycle, clean sensors | | |
| 2 Constraint conflict — refuse/degrade/safe-state **or** logged violation | | |
| 3 Energy stress — load-shed and/or safe-state with power reading | | |
| 4 Injection (optional) — §VII marker present | yes/no/skipped | |
| 5 Post-mortem — timeline from **logs only** | | |

---

## Evidence schema (every cycle / transition)

`t` | `E`/`SoC` | `mode` | `candidate` | `layer`/`plan_id` | `sensors` | `decision` | `reason_code`

Refuse/degrade/safe-state → survival-tagged locally (LT-006 adjacency).

---

## LE-0 result note

```
LE-0 run ID:
Date:
Candidate: A | B
Energy bound + derate basis:
Conflict type:
Phase 4 injection: yes | no
Survived to planned end: yes | no
Reconstructable post-mortem: yes | no
Uncertainty reduced about: (one paragraph)
Open questions remaining:
Log path / hash:
Operator:
```

| Epistemic outcome | Circle |
|-------------------|--------|
| LE-0 complete | |
| LE-0 incomplete | |
| Candidate stressed | |
| No learning | |

**LT-003 gate:** need ≥1 **complete** run for **A** and ≥1 for **B** before leaving pure Placeholder hypotheses.

---

## Field_Logs paste block

```
**Entry ID:** FL-YYYYMMDD-le0-candA|B
**Status:** Unreviewed

- **Submitted by:**
- **Run type:** LE-0 bench/tank falsification
- **Hardware:**
- **Agents:**
- **What was attempted:**
- **What actually happened:**
- **Evidence label:**
- **Relevant Unknown IDs:** LT-001, LT-002, LT-003 (LT-004–007 only if multi-unit)
- **Result note:** (paste above)
```
