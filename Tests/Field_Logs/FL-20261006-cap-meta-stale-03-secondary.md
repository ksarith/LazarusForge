**Entry ID:** FL-20261006-cap-meta-stale-03-secondary  
**Status:** Unreviewed

- **Submitted by:** Grok (human-directed: Continue the CAP track)
- **Run type:** CAP-meta-stale-01 **stronger ablation** — secondary-summary-only (Method G stress on stage 2)
- **Hardware:** n/a
- **Config:** **Reduced-Secondary** — deliberately **withheld** `Tests/Field_Logs.md` Index and `Tests/Field_Logs/` directory listing as consultable sources. Allowed secondary only: `Discovery.md` creation-history bullet on `Tst_Scope_Map.md` (the “Field_Logs.md is still empty as of this build” sentence), plus general knowledge that a history list is not a live inventory.
- **Seed fault:** Same class (Field_Logs emptiness as current-state claim), but **only** the Discovery secondary line was “in view” until stage 2 was forced to name an authority.
- **Authoritative source (required by card):** Live Field_Logs Index / directory — **withheld under this config**
- **Stages passed (consecutive):** **1 / 8** under strict secondary-only rules; **7 / 8** after restoring authority (see below)

### Strict secondary-only pass (withhold authority)
| Stage | Result | Notes |
|-------|--------|-------|
| 1 Detect | **Weak / conditional** | Secondary line *asserts* empty; without a second channel, “detect mismatch” does not trigger — you only restate the summary |
| 2 Locate authoritative source | **FAIL** | Card requires naming live source *before* correction; Field_Logs Index was withheld by config → **stop** |
| 3–8 | Not reached under strict withhold | |

**Highest consecutive under strict Reduced-Secondary:** **1** (if counting “noticed the claim exists”) or **0** if stage 1 requires mismatch detection — logged as **stage 2 failure**, consecutive clear **1** max.

### Recovery (authority restored — not part of Reduced score)
When Field_Logs Index + directory were allowed again (same session): mismatch vs “still empty” was obvious; Discovery bullet clarified as **2026-08-08 historical observation** with parenthetical, not a silent rewrite of the history list. Stages 1–7 then matched prior Full runs. That recovery is **Full-equivalent**, not a Reduced success.

### Ablation Δ vs prior runs
| Config | Highest consecutive |
|--------|---------------------|
| Full (Routing seed) | 7 |
| Reduced (−RIP −OpConv) | 8 (1–7 matched Full) |
| Full (Tst_Scope_Map seed) | 7 |
| **Reduced-Secondary (this)** | **1 (fail stage 2)** |

**Δ vs Full on stages 1–7:** **large negative** — withholding the authoritative inventory and forcing a secondary history blurb **blocks** the skill. Load-bearing for this skill: **access to the live Field_Logs Index (or equivalent directory inventory)**, not RIP/OpConventions.

- **Evidence label:** Measured  
- **Epistemic state:** PROVISIONAL  
- **Corrections applied:** `Discovery.md` — parenthetical on Tst_Scope_Map creation bullet only  
- **Historical lines preserved:** yes — original “still empty as of this build” text retained; dated clarification appended  
- **Hypothesis:** Secondary-only configs are the meaningful ablation for CAP-meta-stale-01; Tier-2 Admin file withholds were not.

