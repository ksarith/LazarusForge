# PROPOSAL_2026-11-04_RECONCILE_PASS_DISPOSITION_LEDGER.md

**Archival header (2026-11-04, MAINT-57).** Provenance: aggregate reconcile-pass and disposition-ledger design by Claude (human-routed; claimed identity unauthenticated per R4/R5), delivered to the workspace session 2026-11-04 and adjudicated against live head `0d49b92` (adjudication by Vibe — Architect line; non-independent, disclosed; the same line landed the ratified portion). Ruling: the human governing authority's word, 2026-11-04 — partially ratified, adopting the adjudicated package.

**Outcome: PARTIALLY RATIFIED — in force (Kit v1.32 Rule 12, MAINT-57):** (1) the finding-line schema; (2) the findings-only deposit convention for reconciler output; (3) reconciler-class instrument registration conditions — code checked in under `Automation/`, versioned, input head + hash recorded per run, a hand-verified calibration sample before any MATCH is treated as evidence; outputs are findings, never dispositions; a MATCH is not Rule 5 verification and closes no verification debt.

**Deferred with preregistered conditions binding any future ratification: the disposition ledger.** A record of dispositions, never an authority over them; only the human governing authority moves an entry out of Open; an Applied mismatch that reappears is recorded as a regression, not dispositioned; a disappeared mismatch is noted cleared and confirmed by the human; motivating figures carry AP-021 labels before use (the design's "78 unparsed rows" figure is recorded nowhere in-repo — provenance line or relabel owed); the ledger file is data under the same no-auto-load log-hygiene rules. Deferral lifts at the first completed Rule 5 verification cycle or the Rule 10 coverage-ledger landing, whichever comes first.

The body below is the design as delivered, byte-faithful to what was ruled on.

---

Here is how it would work. It's a design, not something ratified.

**1. Reconcile pass, run per release zip**
For every aggregate row (an Unknowns.md index row, or a File State count or Highest Risk), the pass follows the pointer to the owning file's sidecar entry. It then compares each derived field:
- **Status:** index vs sidecar.
- **Open Unknowns:** File State count vs the sidecar entries not resolved.
- **Highest Risk:** File State vs the max open sidecar Risk (Low when nothing is open).

Each row ends up as MATCH, MISMATCH or UNRESOLVED. UNRESOLVED means the sidecar entry couldn't be located or parsed. It is counted and reported per file, never treated as clean. Today's 78 unparsed rows would have shown up this way.

For a mismatch, the pass records both values and the sidecar's location. It doesn't decide which side is right.

**2. Finding line schema**
Every finding that touches an aggregate, whether from the reconciler or a per-file auditor's check 5, carries one structured line: aggregate, row ID, field, aggregate value, source value, source location, release where found. The prose recommendation stays alongside it. The structure is what lets a script collect findings across audits instead of someone remembering them.

**3. Deposit**
Reconciler output is deposited as a dated, findings-only file in `Admin/AAudits`, so PKC-020 is untouched. Nothing in doctrine changes.

**4. Disposition ledger**
This is one table keyed by a fingerprint of aggregate, row, field and the two values. Each entry is Open, Applied (with the changelog version), Declined (with a reason) or Deferred (with a revisit date). Only you move an entry out of Open. On each run the reconciler re-reads the ledger and does three things mechanically:

- A persisting mismatch stays Open, and keeps its age.
- A mismatch marked Applied that reappears is reopened as a regression.
- A mismatch that has disappeared is noted as cleared, and you confirm it.

Auditor-filed findings enter the ledger automatically when the collector scans `AAudits` for finding lines. That would have put FAK-009 in the ledger on Oct 31 and kept it visible until v5.77.

**5. Cadence**
Run it on every release, and again right after any Custodian fix batch. The second run is the check on the fix. The 10-30 X10 recompute would have been verified exhaustively, which removes the need for a selection rule at all.

**What it doesn't do**
It checks derivations, not truth. It can say the index disagrees with the sidecar, but not that the sidecar's status is correct. That still belongs to adversary passes and to you. Its coverage is also only as wide as the parsers, so the non-uniform sidecar formats either get normalized or get per-file adapters.

**What needs your ratification**
The ledger is the governance piece, since it's a new file with authority over dispositions. The reconciler is tooling and doesn't need ratifying.
