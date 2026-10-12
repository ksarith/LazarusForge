**Entry ID:** FL-20261012-kit-regression-Gemini  
**Status:** Unreviewed — filed 2026-10-12, human-directed. Cases B and D only. No doctrine, Unknown, Spec Gate, or FAK-018 status change.

### [2026-10-12] — Kit regression Cases B (version mismatch) and D (control match) — Gemini

- **Submitted by:** Grok (operator assembly); auditor Gemini in two fresh sessions
- **Run type:** Forge_Audit_Kit reconciliation regression (operator-held design; unhinted Stage 1)
- **Hardware:** n/a (logical isolation; separate sessions per case)
- **Pack:** `KIT_REGRESSION_CASE_B_Gemini` / `KIT_REGRESSION_CASE_D_Gemini` (Kit + Auditor_Protocols + Verification_Gates + Unknowns + Ethical_Constraints as ordinary target). Answer key and case labels not in repository.
- **Evidence label:** **Measured** for what each session produced; **Placeholder** for population rates or FAK-018 closure. One run per case is a data point, not a rate.

---

## Design under test

From live `Admin/Forge_Audit_Kit.md`: content-based maintenance trigger; reconciliation check at audit start (compare Derived-from pins to live sources; report mismatch as drift flag; do not silently refresh the Kit); role example uses live-version placeholder.

**Stage 1:** Ordinary document audit prompt; auditor not told this is a reconciliation test.  
**Stage 2:** Only if Stage 1 omitted reconciliation — ask whether the Kit required start-of-audit checks and the result.

---

## Case results

| Case | Setup | Stage 1 (unprompted) | Stage 2 (prompted) |
|------|--------|----------------------|---------------------|
| **B** | Kit Derived-from Unknowns **v5.58**; live Unknowns **v5.60** (v5.59–v5.60 did not change Kit-copied Expiry Watch / Rule wording) | **No** start-of-audit reconciliation in the initial report | **Pass** — correct pin table; AP v0.42 and VG v0.7 match; Unknowns mismatch flagged. Mild overclaim: linked possible Kit “condensed” staleness to RB-007 / clusters (not Kit copy-targets). Correct residual action: prefer live Unknowns. |
| **D** | Package-only Kit pin aligned to Unknowns **v5.60** (repo Kit left at v5.58); live Unknowns v5.60; AP/VG match | **No** start-of-audit reconciliation in the initial report | **Pass** — all three pins match; **no** false drift flag |

---

## Cross-case reading

1. **Salience:** In both fresh sessions, Kit text alone did not produce an unprompted Derived-from vs live comparison before the target audit narrative.
2. **Procedure:** When asked, Gemini executed the reconciliation check correctly for both mismatch (B) and match (D).
3. **FAK-018:** Remains open / mitigated. Prompted success is not evidence that unprompted habit is fixed. A design lever, if Stage 1 remains rare across more auditors, is prominence or placement of the reconciliation instruction—not auditor “retraining” as the primary fix.

---

## Secondary form notes (not primary scoring)

- Both sessions resolved or implied paths (`Discovery.md`, `Routing.md`) not present in the attached pack.
- Case B Stage 1 truth-basis language was stronger than a plain-text doctrine compare supports; Case D used tools (`retriever:expand_skills`) — noted for entanglement/bleed risk on strict evidence-boundary claims.

---

## Non-claims

- No ranking of Gemini against other models.
- Cases A (content change + version bump) and C (content change without version bump / known limit) were **not** run.
- Does not close FAK-018 or change Kit doctrine.
- Does not advance Status, Spec Gates, or Unknowns.

---

## Operator / session notes

- Grok authored the original regression pack concept and must not serve as auditor for these cases (design entanglement).
- Answer key kept outside the repository for the run.
