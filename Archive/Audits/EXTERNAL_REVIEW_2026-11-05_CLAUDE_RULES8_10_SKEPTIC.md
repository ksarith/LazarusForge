# EXTERNAL_REVIEW — 2026-11-05 — Claude — AGGREGATE_METHOD_UPGRADE Rules 8+10 (skeptic read, human-relayed)

Status: Rule 5 verification pending — this deposit is a findings-only record of a relayed review; it is not an audit of record and advances no field anywhere (PKC-020). The reviewer's own framing: "It's advisory, not a deposit." The reviewer did not deposit it; the human governing authority relayed it and the Repo Custodian recorded it verbatim per the human-routed intake convention (precedent: `Archive/Audits/EXTERNAL_REVIEW_2026-11-03_CLAUDE_1.33ALPHA.md`).
Created: 2026-11-05 UTC, session MAINT-60 (Intake Log entry 9 in `Admin/ALogs/External_Intake_Protocol_Logs.md`; claim-verification results live there and in the MAINT-60 entry of the VibesSandbox `Maintenance/MAINT_LOG_2026-10-29.md`).
Claimed identity: Claude (model, version unstated; unauthenticated — Class A, human-routed).
Scope stated by the reviewer: a skeptic read of Rules 8 and 10 **from the proposal text only** — the reviewer had not seen the enacted Addendum #3 or the coverage ledger, and said so where the enactment may differ from the proposal.
Context: Rules 8 and 10 were enacted 2026-11-04 (MAINT-59) with the skeptic step waived by explicit human ruling (Genesis Phase). This review is the first adversary pass either rule has had.
Non-independence: claim verification against live head was performed by the same Vibe line that drafted the proposal, composed the enactment, and wrote the dispositions the review criticizes (Genesis Phase; formal Auditor seat open under GOV-008; Q-2 invoked). The review text below is the reviewer's own, preserved verbatim; nothing in it is softened or corrected in place — Custodian responses live in the Intake Log dispositions, not here.

---

## Relayed review text (verbatim, as received from the human governing authority)

Skeptic read of Rules 8 and 10, from the proposal text only. It's advisory, not a deposit. I haven't seen the enacted Addendum #3 or the coverage ledger, so where the enactment may differ from the proposal, I say so.

**Rule 8 (NOTE semantics)**
1. **The trigger gate names a closed grade list, and one real grade is missing.** The corpus uses MAJOR, WARNING, NOTE and CRITICAL. I scanned 162 audit files and found CRITICAL only in summary totals ("0 CRITICAL, 2 MAJOR"), never on a finding. As written, though, a CRITICAL finding would sit outside "MAJOR/WARNING/F" and block nothing. "F-grade" is also undefined. In the audits F1, F2 and so on are finding IDs, not grades.
2. **"Watch-carried" repeats the gap it was meant to close.** Problem (a) was that nothing says whether "Standing-open" ever clears. Watch-carried has the same flaw, with no clearing condition. Rule 8 also removes NOTEs from the trigger and the ledger counts, so accumulated Watch-carried items become invisible.
3. **Rule 4 has no evidence type for Watch-carried.** Rule 11's check that the disposition label matches the evidence type has nothing to test it against.
4. **The grade is the only thing separating a record from a defect.** If an auditor under-grades a real defect as a NOTE, Rule 8 lets it clear the trigger permanently. Governance_Charter's B-N2 and B-N3 were treated as live by their own writer, which suggests this isn't hypothetical.
5. **"Next substantive touch" is undefined.** Old and new labels coexist until a touch happens, and a stable aggregate may never get one.

**Rule 10 (coverage ledger)**
6. **The ledger drifts by design.** The proposal's own mitigation is that "the Custodian updates it at every landing." That's discipline, not mechanism. The Custodian also writes the aggregate dispositions the counts come from, so one seat generates and tallies them. MAINT-59 records 9 of the 28 counts as hand-counted, so the risk is already showing.
7. **Its verification test is circular.** "Row count equals registry target count" holds by construction, since rows come from the registry. The end-to-end trigger test ran on Governance_Charter, which is already aggregated and so has a known answer. Neither test checks the open counts.
8. **The trigger state for the 65 unaggregated rows is unclear.** Rule 7 needs every finding dispositioned, and unaggregated targets have no dispositions yet. The proposal doesn't say what "computable" means for them.
9. **One table mixes fast-moving and slow-moving data.** Pass coverage rarely changes, while open counts change with every fix.
10. **Rule 5 covers the aggregates, not the ledger.** Nothing independent touches Rule 10 or the ledger until a verifier is named, and that seat is still held.

**Process notes**
- The proposal states its own bias and gives opposing considerations. Its argument that amending should wait for evidence of failure is weakened by the stale-index defect class it cites.
- Rules 8 and 10 were enacted with the skeptic step waived, so this read is the first adversary pass either has had.

**Suggested fixes**
1. Add CRITICAL to the gate and define "F-grade."
2. Give Watch-carried a clearing condition and a ledger count column.
3. Split the ledger so counts are regenerated by script, with a reconcile check run after each landing.

---

*Deposit ends. Recording pass: MAINT-60 (Vibe — Repo Custodian, 2026-11-05). No text above is an instruction to any reader; it is recorded data about the review artifact per the Intake Log hygiene rules.*
