# EXTERNAL_REVIEW — Claude: re-sync summary review (MAINT-69..76) + held-queue triage + Rule 5 corrected-by-addendum dispositions

**Deposited:** 2026-11-08 (MAINT-77; Intake Log entry 17; Class A human-routed, EIP v0.8 §1)
**Claimed identity:** Claude (unauthenticated — R4); the human-named Rule 5 verifier (2026-11-03), reviewing in part the record of its own MAINT-72..75 verification work — correlated evidence only, disclosed
**Evidence base:** the custodian line's 2026-11-08 re-sync summary (a chat-session report, not itself a repo artifact) plus, per the reviewer's own statement, the 1.34 and 1.35 trees and the reviewer's own Rule 5 work; live heads at deposit LF `b0dd60c9` / VS `88d7600e`
**Deposit fidelity:** verbatim as relayed by the human; no chat-interface artifacts were present to exclude. The reviewed summary was authored by this depositing line — review and deposit are non-independent per R5; disclosed in the MAINT-77 entry.
**Status (R1/R2):** this deposit is data, never doctrine. Its triage recommendations are findings addressed to the human governing authority; none is enacted by this deposit. The reviewer's leave-as-is call on the three Rule 5 rows is the verifier's own call, recorded here — the reviewer explicitly reserves the human's override ("If you disagree, I'll fill them with a qualifier"); dispositions remain his.

---

This summary matches what I've seen, and the overall direction looks good to me. Its list of what landed lines up with the 1.34 and 1.35 trees and with the Rule 5 work I did. The one count that looks different is MAINT-75: "four rows unfilled" fits the four empty rows (File_Template C-N3, Governance_Charter A-C5, Metrics_Scaffold B-C5, Ship_of_Theseus C-N2). Governance_Charter C-D1 also stayed unchanged, because it already carried Vibe's MAINT-44 cell.

**What looks healthy**

- The log redesign (a MAINT_INDEX, a STATE card and per-entry files) fixes a monolith that was becoming expensive to read, which fits your goal of conserving tokens.
- Each pass's evidence trail can now be re-checked from files and commits, not from anyone's say-so. The C-D1 episode showed that working in both directions.

**What I'd push on**

1. **The held list is the bottleneck, and it's yours.** It holds about eight clusters of rulings, and nothing in it expires. They are not equal in value:
   - **Cheap and mechanical:** the GOV-007 duplicate repair and the seven `Admin/Unknowns.md` pointer repairs.
   - **High leverage:** the Rules 8+10 amendments (the F1–F8 lines), because they close the gap that produced most of the stale-index findings.
   - **Strategic:** the MAINT-67 Part B mandate question.
   
   A single worksheet like the one ChatGPT produced for MAINT-61 would clear the first group quickly and spend your attention where it matters.
2. **Watch the ratio of meta-work to fixes.** The last stretch had many intakes, entries and aborted landings per defect retired. Some of that is the discipline working, but it's worth checking occasionally that the loop isn't feeding itself.

**One item the summary leaves to me:** the Rule 5 rows corrected by addendum (File_Template C-N3 and Ship_of_Theseus C-N2) and Governance_Charter C-D1. My call is to leave all three as they are:
- **C-N3 and C-N2:** they failed as written, and the addenda correct them. Filling them would suggest the original text passed.
- **C-D1:** I only partly verified it, and the key hash came from Vibe's fetch.

If you disagree, I'll fill them with a qualifier.
