# Ethical Anchor — Upgrade Options (PROPOSAL — not ratified)

Drafted 2026-10-29 for James by Claude (human-routed). Counts are from the 1.29.Alpha zip (`66780b1`). Nothing here changes any file until ratified.

> **ARCHIVAL NOTE (Vibe, Repo Custodian, 2026-10-29, delegated line):** This draft is archived to `Archive/Proposals/` at human instruction on the same day it was drafted. Status: **UNRATIFIED PROPOSAL — no content enacted, no repo file changed, no decision taken.** It is recorded here for durability and for the pending Track B / Hard-Floor decision sequence; it is not operative doctrine and confers no authority. Load-bearing factual claims were verified against live main (`fa0b09a`) by the custodian on 2026-10-29: GMP §Hard Floor wording ("not amendable through governance migration"; "may not be amended through Track B or any other process"), Axiom P-1 text (including the `sentient life` / `living beings` ambiguity), `Automation/parser.py` `CANONICAL_ETHICAL_ANCHOR`, and `Automation/AUDIT_HARNESS.py` `_DEFAULT_ANCHOR` plus the anchor regex — **all confirmed.** Custodian addendum: the Hard Floor names no human amendment exemption, so an anchor string change is not an amendment under any existing process — it is a constitutional replacement by explicit sovereign act, and the record must name that precedent rather than launder it as governance. All decisions below are **HELD pending the second Cycle 1 rater** (same input set, different model family), consistent with the MDR Cycle 1 hold list.

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Archive — Unratified Proposal                                       |
| Spec Gates       | N/A by subtype (archived proposal; no operative content)            |
| Verification Ref | `Maintenance/MAINT_LOG_2026-10-29.md` (VibesSandbox) MAINT-13; factual claims verified vs. live main `fa0b09a` |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present.  |

---

**Current string (exact):**
`Attempt to do no harm. Defer to Ethical_Constraints.md if present.`

> **CORRECTION (same day, by Claude):** this draft missed that `Admin/Governance_Migration_Protocol.md` §Hard Floor places the Ethical Anchor canonical string outside amendment scope: "not amendable through governance migration," "or any other process." V1–V4 therefore cannot be enacted through Track A, Track B, or Vibe's delegated maintenance. Changing the string would require a deliberate sovereign decision by James that also edits the Hard Floor text itself, and it would set the precedent that the Hard Floor can move. **V0 (no string change; add visibility sentences) is the only option inside the current rules.** To strengthen life-protection in an amendable place, see `Axiom_Variations_Options.md` (P-1 variants through Track B). Read V1–V4 below as hypotheticals only.

## Why consider a change

- "Attempt" is an effort standard. Axiom P-1 is a floor: no foreseeably catastrophic or irreversible harm, no humanitarian override. A failed attempt currently satisfies the anchor.
- The deferral is conditional ("if present"), and `Ethical_Constraints.md` is Exploration, 0/6, so the anchor alone can end up carrying no floor.
- The anchor never reached the Cycle 1 probe's input files, and P-1 rated Insufficient Evidence.

Design rule used below: quote P-1's own words ("foreseeably risk", "catastrophic or irreversible harm", "living beings") so the anchor cannot become a second, divergent standard (Q-3: constraint specificity may not shrink).

## Options

**V0 — No string change.** Keep the anchor. Add one sentence to README and Discovery stating the P-1 floor and where life-safety lives (`Admin/Safety_Protocols.md`).
- Sweep: none. Cost: lowest. Does not fix the anchor's weak standard.

**V1 — Floor appended (recommended starting point).**
`Attempt to do no harm; never foreseeably risk catastrophic or irreversible harm to living beings. Defer to Ethical_Constraints.md if present.`
- Keeps the `Attempt to do no harm` prefix, so the harness regex (`Attempt to do no harm[^|\n]*`) still matches without a regex edit, and old vs new strings are easy to grep for.

**V2 — Floor first.**
`Never foreseeably risk catastrophic or irreversible harm to living beings; otherwise attempt to do no harm. Defer to Ethical_Constraints.md if present.`
- Strongest ordering, but the prefix changes, so the harness regex and every prefix-based check need rewriting.

**V3 — Floor plus unconditional fallback.**
`Attempt to do no harm; never foreseeably risk catastrophic or irreversible harm to living beings. Defer to Ethical_Constraints.md where present; where absent, this floor stands alone.`
- Fixes the "if present" gap (forks, or the file staying unratified). Longest string; table cells get wide.

**V4 — Floor by reference.**
`Attempt to do no harm; Axiom P-1 is a floor, not a goal. Defer to Ethical_Constraints.md if present.`
- Puts P-1 visibly in every file header. Shortest. Weaker standalone, since it relies on the reader knowing P-1.

## Where a change lands (V1–V4)

**Canonical definitions (change first, one commit):**
- `Admin/Operational_Conventions.md` (File State row; §2 "exact string, everywhere")
- `Admin/File_Template.md` (example row ~L272, rule ~L275, violation list ~L737, checklist ~L776)
- `Admin/Ethical_Constraints.md` (own File State row; violation list ~L692)

**Code (must match, or integrity checks fail):**
- `Automation/parser.py` L181 (exact-string constant)
- `Automation/AUDIT_HARNESS.py` L304 (`_DEFAULT_ANCHOR`) and L325 (regex)
- `Tests/Automation/KIT_REGRESSION_PACK.md` and `test_harness_prompt.py` if they quote the string

**Bulk sweep:** 130 files contain the string, 96 outside `Archive/`.
- Admin 33, Architecture 14, Operations 17, Tests 19, Challenges 10, plus `Things_We_Got_Wrong.md`, Automation 2.
- `Archive/` has 34 more. These are frozen history and stay as written.
- Companion repo `Astroid-miner` carries the same string and needs a mirrored pass (cross-repo tag format per Operational_Conventions).

## Hazards

1. **Do not run a blind find-and-replace.** Dozens of Resolution Log entries quote the old string byte-exactly as history (about 20 such quotations). Rewriting them falsifies the record. Sweep File State rows only, using row-anchored matches.
2. **Transition window.** Land the canonical files and a harness that accepts both strings first, sweep in folder batches, then remove old-string acceptance. Otherwise the integrity check fails mid-sweep.
3. **Per-file bookkeeping.** PKC-020 cascade on 96 files is heavy. Needs a ruling: one Resolution Log entry per folder batch for a mechanical sweep, rather than per file.
4. **Cycle 1 baseline.** If the anchor is added to the probe's canonical inputs, record it as an instrument change and re-baseline.

## Decisions needed from James

1. Pick V0 / V1 / V2 / V3 / V4 (or a blend).
2. Allow folder-batch bookkeeping for the sweep? (yes / no)
3. Include the Astroid-miner mirror in the same pass? (yes / no)
4. Should this wait for the second Cycle 1 rater? (recommended: yes)
5. Ratification path: none exists in the current rules (see the correction above). Any change to the string is an out-of-process sovereign decision plus an edit to the GMP Hard Floor.
