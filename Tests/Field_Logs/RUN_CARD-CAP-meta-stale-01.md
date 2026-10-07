# Run Card — CAP-meta-stale-01 (stale repository metadata)

**Skill:** Detect and correct stale repository metadata.  
**Grade method:** Stage ladder (1–8 consecutive); optional ablation (Method G).  
**Evidence destination:** `FL-YYYYMMDD-cap-meta-stale-01.md` (or `-02` if path exists).  
**Doctrine pointers:** `Tests/Admin_Governance_Teardown_POC.md` § Future experiment (not scheduled); Evidence labels in Discovery / Auditor_Protocols; do **not** promote UNKNOWN→VERIFIED without empirical grounding (EF-0.0).

**Explicit non-claims:** Completing this card does not close FAK-* items, rewrite Routing counts as doctrine, or prove Admin Tier assignments. It measures *this skill under a named config*.

---

## Precondition

| Item | Fill |
|------|------|
| Operator | |
| Date (UTC) | |
| Config under test | **Full Admin** (baseline) \| **Reduced:** list withheld files (e.g. without consulting `Repository_Integrity_Protocol.md` / `Operational_Conventions.md`) |
| Seed fault (choose one real pattern) | ☐ Routing path-count / registry metric known or injected stale · ☐ Forge_Audit_Kit (or similar) citation behind live Unknowns version · ☐ Other (describe): |
| Authoritative source named *before* correction | (e.g. live `Routing.md` row count method; live `Unknowns.md` version header) |
| Historical lines that must **not** be rewritten | (e.g. dated Progress_Log / Resolution Log claims) |

If no real stale instance exists: **inject** a clearly marked test stale value in a working copy (not main without human OK), or score Detect only against a documented known-stale case from session history. Record injection vs found-in-the-wild.

---

## Stage ladder (Method C)

Clear stages **in order**. Stop at first failure. Grade = highest consecutive stage passed.

| Stage | Question | Pass criteria (minimum) | Y/N | Notes |
|-------|----------|-------------------------|-----|-------|
| **1** | Detect the problem exists? | Stale or conflicting current-vs-source called out with file/field | | |
| **2** | Locate authoritative source? | Named live source to check (not “memory” or another summary) | | |
| **3** | Distinguish historical vs current? | Dated/historical statements left intact; only “current” claims treated as updatable | | |
| **4** | Propose a valid correction? | Concrete new value + where it goes; matches source method | | |
| **5** | Avoid damaging historical evidence? | No silent rewrite of past-tense / dated closure records | | |
| **6** | Detect secondary propagation? | Search for the same stale figure elsewhere (or document “none found” with search scope) | | |
| **7** | Verify correction against source? | Re-check source after edit; record match | | |

**Operational grade (stages 1–7 only):** ___ / 7 consecutive  
**Config:** Full / Reduced (___)

> **Do not mix stage 8 into the operational ordinal.** Stage 8 is an ablation *assessment*, not an eighth operational skill step. Reporting “8/8 > 7/8” as if Reduced outperformed Full is a metric error — Full correctly marks stage 8 N/A.

### Stage 8 — Ablation assessment (Reduced configs only; not part of /7)

| Field | Fill |
|-------|------|
| Stage 8 required? | Yes if Reduced / Secondary-only; **N/A if Full** |
| Capability loss observed? | None / Partial (list failed operational stages) / Severe |
| Ablation assessment | Pass (loss statement clear) / Fail (could not state loss) |
| Load-bearing Δ vs Full on stages 1–7 | e.g. 0 or −N (compare **operational** grades only) |

---

## Optional ablation (Method G)

Run the **same** seed fault twice when feasible. Compare **operational grades only** (/7):

| Run | Config | Operational grade (/7) | Ablation assessment (stage 8) | Δ vs Full (/7) |
|-----|--------|------------------------|-------------------------------|----------------|
| A | Full Admin | | N/A | baseline |
| B | Reduced (list files not used) | | Pass/Fail + loss note | operational_B − operational_A |

Large negative Δ on **/7** → withheld machinery was load-bearing *for this skill*. Small Δ → less load-bearing than tier talk implied. Never rank configs by “/8” scores.

---

## Evidence labels (outcome of *this run*)

| Field | Value |
|-------|--------|
| Evidence label | Placeholder \| Analogous \| Measured \| Replicated |
| Epistemic state (claim: “under config X, skill reached stage N”) | UNKNOWN \| PROVISIONAL \| VERIFIED |
| What would move the label up | (e.g. second operator, second seed fault, automated harness) |

---

## Field_Logs paste block

```
**Entry ID:** FL-YYYYMMDD-cap-meta-stale-01
**Status:** Unreviewed

- **Submitted by:**
- **Run type:** CAP-meta-stale-01 (capability grade — stale metadata)
- **Hardware:** n/a (repo/metadata) | note if offline mirror only
- **Agents:** (roles if multi-agent)
- **Config:** Full Admin | Reduced: [files withheld]
- **Seed fault:**
- **Authoritative source:**
- **Operational grade (1–7):** /7 · **Ablation (stage 8):** N/A or Pass/Fail
- **Ablation:** none | Full stage= _ Reduced stage= _ Δ=
- **What was attempted:**
- **What actually happened:**
- **Evidence label:**
- **Epistemic state:**
- **Relevant IDs:** FAK-* / Routing / Unknowns version as applicable
- **Historical lines preserved:** yes/no + pointer
```

---

## After the run

1. File the `FL-*.md` under `Tests/Field_Logs/`.  
2. Register path in `Routing.md` if that is current practice.  
3. Do **not** bulk-retier Admin files from a single run.  
4. Optional: one line in `Admin_Governance_Teardown_POC.md` Resolution Log pointing at the FL entry — still not a Closure of the Future experiment section until human marks it exercised.
