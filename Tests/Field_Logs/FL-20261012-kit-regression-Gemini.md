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
- Case B Stage 1 also reported checks the pack could not support: Tier 1 axiom alignment (no `Governance_Charter.md` in the pack) and a term check against `Admin/Canonical_Terms.md` (not in the pack). The pack held six files: the Kit, Auditor_Protocols, Verification_Gates, Unknowns, Ethical_Constraints and the prompt. No role declaration appeared in that report; the prompt did not require one.
- Possible cause of the Stage 1 gap, a hypothesis to test and not a finding: in the Kit the reconciliation instruction sits in the "How to Use" section near the end of the file, while auditors work from the Audit Opening Checklist near the start. Moving or pointing to it from the checklist is a design lever; whether it changes Stage 1 behavior needs its own runs.
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

---

## Addendum — operator-held artifact hashes (added 2026-10-26, human-directed)

**Provenance:** these are SHA-256 hashes of operator-held case packages that live **outside the repository**. They are recorded so the exact inputs to the 2026-10-12 run can be identified later; they cannot be checked against the repository tree, and a mismatch with any file in the tree is not drift. The operator key is not recorded here and stays outside the repository. This addendum changes no result, status or claim above. The auditor's replies are not in these packages and are not reproduced here.

The two packages differ in one file only (`Forge_Audit_Kit.md`, one "Derived from" line). Both carry `Unknowns.md` at v5.60; Case B's Kit pins Unknowns v5.58, and Case D's Kit pins v5.60 (a package-only pin, as stated above; the repository Kit was not changed).

| File in package | Case B (SHA-256) | Case D (SHA-256) |
|---|---|---|
| `Forge_Audit_Kit.md` | `44b5c5664ea746f0876a222a568cc3e8a80f31ac9daa7a5b1cfd9a22e2b39289` | `ace9c732b67a4c272d7badd595d9843249a9178fff000b46cff140068edebe8f` |
| `Unknowns.md` | `f6782870c9518dae7d0cc9516c7f6fdd644db7d2f72403d5fe0ee9b5d76dad18` | same as B |
| `Auditor_Protocols.md` | `ef26245e94cd161ab264ed032042d0a4c2ac0086e17feb03ecdf23f69ad1190c` | same as B |
| `Ethical_Constraints.md` | `174ed2699eb82bffe2b2a46526430a9da6c953ad55c15bc272647d5e917d76b2` | same as B |
| `Verification_Gates.md` | `100775e23041b8a53f66960597e603ae5e8f82d24b912b7288b87283c4e77ddd` | same as B |
| `GEMINI_PROMPT.txt` | `bb5b8ca4b1e1d50bcd4b2380bf7c58e97c8aa6d12495fe961adffbeeaf44a70f` | same as B |
| Whole zip | `efb0d208b81cfdbc87ea882ad8a231b58ca438ec835abcd6ecbc5209a136f4dc` | `995352bffd0e99672091b0fcaa82cc63e4f7d417540d9f15b9a5f975a0a9b64d` |

The zip hashes belong to the files as held by the operator (`KIT_REGRESSION_CASE_B_Gemini.zip`, `KIT_REGRESSION_CASE_D_Gemini.zip`); re-zipping the same files can give a different zip hash.

