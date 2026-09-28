# New-instance orientation: design notes, session transcript

**Filed 2026-09-28.** This is preserved reference/background discussion, not doctrine and not a body-text insertion. Produced by Claude (Synthesizer, human-directed) during the 1.17 Alpha review session, in response to the question of whether the current repository structure is good enough for a new instance to get oriented. The size and structure observations below were checked against the live 1.17 tree (file sizes, section positions, the bundler's docstring) before filing. The proposals are ideas only. Nothing here is selected, adopted, or ready for insertion, and no Unknown is filed from it.

---

## Part 1: What exists today

The orientation path, as observed in the 1.17 tree:

- `README.md` (landing page, specified-vs-demonstrated table)
- `Discovery.md` (about 49 KB; its Agent Orientation section, six points, sits around line 140, after Repository Role, Objectives, and Recent Governance Developments)
- `Routing.md` (about 40 KB; file registry)
- `Admin/Forge_Audit_Kit.md` (about 28 KB; mandatory session opening: load the kit, declare a role, run the Audit Opening Checklist)

Combined, roughly 118 KB, on the order of 30k tokens, before an instance does any work. That is comfortable for an agent able to load the whole tree and heavy for an agent with tight input limits.

Separately, `Automation/cold_session_bundler.py` implements AP-017's informational-independence requirement for audit sessions. It deliberately strips retrospective findings and evaluative metadata so an auditor is not primed. That is the opposite goal from orientation, and the repository currently has no written fork between the two.

## Part 2: Assessment

The structure is sound for an instance that can read a lot. The weak layer is the cheap first five minutes: the "read this before contributing" instruction sits behind roughly 130 lines of other content, and there is no compact current-state view short of Unknowns.md (about 107 KB) and Progress_Log.md (about 83 KB).

## Part 3: Ideas (none adopted)

1. **Start card, 4 KB or less.** The six Agent Orientation points compressed, the role declaration, where the live truth lives (Unknowns, Routing, Verification_Gates), and what not to touch. Linked first from README or Discovery.
2. **Role fork.** Contributors and synthesizers receive the state of play. Independent auditors receive only the raw bundle and no summaries, per AP-017. The card would say which path applies.
3. **Mechanical state digest.** Open-unknown counts, the latest Unknowns version headline, the last few Progress_Log titles, and a generated date. Derived by tooling, not hand-written, because Discovery.md point 6 says stated repo facts go stale. `Automation/integrity_check.py --health` already computes most of the counts. It must stay facts-only: `integrity_check.py` deliberately refuses to emit a readiness or governance-state badge, and a digest should keep that rule.
4. **Orientation test.** Give a cold instance only the start card plus the README and ask five pre-registered questions: where does X live, what is the live open thread, what is off-limits, which role must be declared, how is a claim verified. Score against source, with the design fixed before results, in the same style as the Candidate 3 pre-registration in `Tests/Persistent_Cognition_Candidates.md`.

## Part 4: Notes and caveats

- Small-context agents remain the binding constraint on any orientation design. The start card is the only item here that fits them.
- An orientation test run on an account with persistent memory enabled would be contaminated by Candidate 7's mechanism (see `Tests/Persistent_Cognition_Candidates.md`), so it should be run memory-off or with a "which layer answered" field.
- A digest and a start card are themselves stated repo facts. Both would need an owning file, a generated-date field, and a place in the Routing registry, or they become new sources of drift.
- Not investigated: whether an existing file already serves the start-card role, and how the bundler performs when used for orientation-adjacent sessions.
