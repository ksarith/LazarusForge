# Repository_Integrity_Protocol.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 2/6                                                                 |
| Verification Ref | `Admin/Verification_Gates_LF.md`                                    |
| Last Audit       | 2026-06-19; revised 2026-06-27; revised 2026-07-02; revised 2026-07-08 (two passes); revised 2026-07-09; revised 2026-07-16; revised 2026-07-24; revised 2026-07-29 |
| Auditor          | Gemini — Skeptic/Auditor; ChatGPT — Skeptic/Auditor; Grok — Skeptic/Auditor; Claude — Synthesizer/Auditor; Claude — Registration Latency addition (human-directed) 2026-07-08; Claude — Phase 0 manual execution tier added (human-directed) 2026-07-08; Gemini — Exploration audit 2026-07-08 (Archive contradiction, cross-ref, RIP-009, Phase 0 anchor); Claude — fixes integrated + RIP-008 severity correction (human-directed) 2026-07-09; Claude — Post-Exit Monitoring Reversion Mechanism added for GOV-013 (human-directed), 2026-07-16; Claude — Integrity Confidence/Drift Trend format, Protocol Validation/RIP-010, Status section v0.8 omission fixed (human-directed, external ideation reviewed and scoped down), 2026-07-24; Claude — stale "PROPOSED, NOT RATIFIED" / "once ratified" GOV-013 references corrected to reflect the Charter's actual 2026-07-19 ratification (human-directed), 2026-07-29 |
| Open Unknowns    | 9                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Integrity baseline definitions for each protected repository element
- Violation detection procedures at v0 (human-in-the-loop)
- Violation classification system and response ladder
- Recovery procedures following confirmed violations
- Version preservation requirements and human workflow
- Automation migration path for future versions
- Relationship between integrity doctrine and constitutional axioms
- Incident logging requirements
- Navigation file protection requirements (`Discovery.md` / `Routing.md`)
- Registration latency between file sidecars and `Unknowns.md`'s global index

**This file DOES NOT define:**
- Cryptographic authentication implementation (→ `Admin/Security_Protocols.md`)
- Constitutional governance doctrine (→ `Admin/Governance_Charter.md`)
- Auditor operational behavior (→ `Admin/Auditor_Protocols.md`)
- The Sidecar Model's structural architecture — local ledger vs. global index (→ `Admin/Auditor_Protocols.md` §Decentralized Audit Architecture; this file defines the *timing* integrity of that architecture, not its structure)
- CI/CD pipeline automation mechanics
- Runtime enforcement code
- Specific tooling implementations
- Governance authority hierarchy (→ `Admin/Governance_Charter.md`)
- Anti-Weaponization doctrine (→ `Admin/Ethical_Constraints.md`)
- Archive retention policy duration (→ RIP-006, pending)
- Integrity incident ownership (→ RIP-007, pending)

---

## File Purpose

This file defines the operational integrity enforcement procedures for LazarusForgeV0. It exists to bridge the gap between the `Admin/Governance_Charter.md` constitutional declaration of integrity requirements (Declared and Detectable state) and fully Enforceable integrity protections. Without this file, integrity violations may go unclassified, recovery procedures may be improvised inconsistently, and the repository may lose institutional memory of compromise events. This file is the candidate integrity model that `Automation/AUDIT_HARNESS.py` automation will eventually implement — it is written now so the automation has a target to build against.

**Honest v0 acknowledgment:** At current maturity, the primary integrity mechanism is human discipline. Automated detection is the destination. This file defines the provisional procedures a human operator or auditor executes manually until automation matures. Procedures written here must therefore be executable without tooling.

**v0.6 update (2026-07-08):** Phase 1 checks now have a standing manual execution mechanism — the daily morning repository audit prompt fetches this file directly and applies its Protected Elements checks against every file the audit touches, classifying findings per the Violation Classification ladder below. This does not constitute Phase 1 automation (`Automation/AUDIT_HARNESS.py` implementation remains the actual automation target — see RIP-002), but it closes the prior gap where Phase 1 checks existed only as specification with no execution path at all, manual or automated. Treat this as a new tier: **Phase 0 — Manual execution via recurring agent audit**, sitting before Phase 1 in the Automation Migration Path below.

---

## Assumptions

| ID      | Assumption                                                                      | Basis                            | Confidence | Expiry Trigger                                         |
|---------|-----------------------------------------------------------------------------------|-----------------------------------|------------|----------------------------------------------------------|
| ASM-001 | Version preservation is currently a human discipline, not an automated guarantee | Observed repository workflow     | High       | Automated version control enforced at repository level |
| ASM-002 | Most integrity violations at v0 will be accidental rather than adversarial       | Current contributor profile      | Medium     | Adversarial actors confirmed in operational environment |
| ASM-003 | Human auditors are the primary detection layer at v0                            | Absence of automated tooling     | High       | `Automation/AUDIT_HARNESS.py` implements automated baseline checks |
| ASM-004 | Prior file states may not always be available for comparison                    | Observed version preservation gaps | High     | Systematic prior-state archival established            |
| ASM-005 | Multi-agent workflows create specific integrity risks around omission of prior agent contributions | Observed provisional document workflow | High | Single-agent workflow formally adopted |
| ASM-006 | A newly-logged sidecar unknown becomes effectively invisible to cross-file audit tooling until it is mirrored into `Unknowns.md`'s active index | Observed CLF- cluster registration gap, 2026-07 | High | `Automation/AUDIT_HARNESS.py` implements automated sidecar↔index parity check |

---

## The v0 Integrity Reality

Before defining procedures, this section names the actual integrity gap honestly.

The repository currently operates with:
- **No automated version comparison** — a human must read prior and current versions to detect changes
- **No cryptographic integrity verification** — file hashes are not computed or stored
- **No append-only log enforcement** — Resolution Logs can be edited after the fact without detection
- **Inconsistent prior-state preservation** — most revisions override originals; provisional documents are an exception

This means the current integrity layer is:
- **Detectable** — a careful human auditor reading two versions can identify most violations
- **Reviewable** — violations that are detected can be logged and traced
- **Not enforceable** — no mechanism prevents violations from occurring

This is not a failure of the governance architecture. It is an honest assessment of v0 maturity. The procedures below are designed to work within this reality while creating the specification that automation will eventually fulfill.

The most important v0 integrity practice is therefore: **preserve prior states before revision.**

---

## Version Preservation Protocol

This section defines the human workflow required before any revision to a governance-bearing document.

### Before Revising Any Governance Document

1. **Preserve the prior state before revision.** The repository's primary mechanism for this is **Git release tags** — per RIP-001's resolution, GPG-signed, GitHub-autogenerated snapshots are the systematic archival baseline, not a manual step this protocol needs to instruct. Confirm a tagged release exists at or after the version being revised; if not, cut one before proceeding.
   - A local dated-filename copy (`[Filename]_YYYYMMDD_[version].md`) in a working `/Archive/` folder remains a legitimate *secondary* redundancy for an operator working offline or between tagged releases — optional, not the primary mechanism, and not required when a current release tag already covers the prior state.

2. **Record the prior state hash** if tooling is available. If not, record the final line count and open unknowns count as a lightweight integrity anchor.

3. **Note the last audit entry** from the Resolution Log — this is the comparison baseline for the new revision.

4. **In multi-agent workflows:** open each session by explicitly loading prior agent contributions. State: *"Prior contributions assumed: [list]. Carried forward unless contradicted."* This is Rule 6 of the AI Contribution Protocols — it directly addresses the omission risk that provisional documents exposed.

### After Revising Any Governance Document

1. **Add a Resolution Log entry** for every substantive change. Not for typo corrections — for changes to doctrine, scope, unknowns, or structure.

2. **Update the File State table** — Last Audit date, Auditor, Open Unknowns count.

3. **Verify Ethical Anchor field** is intact and matches canonical string exactly.

4. **Verify cross-references** against `Discovery.md` Rename Registry — do not carry forward stale flat filenames.

5. **Archive the prior version** if not already done in step 1 above.

---

## Protected Elements and Integrity Baselines

For each protected element, this section defines what "intact" looks like in a checkable way.

### Tier 1 Axioms

**Baseline:** Axiom text in `Admin/Governance_Charter.md` matches the text present at the time of last human ratification.

**Intact condition:** All eight axioms (P-1 through P-4, Q-1 through Q-4) present, text verbatim from ratified version, Protections/Prohibitions clause structure preserved.

**Detection method:** Read current axiom text against archived prior version. Any wording change that was not accompanied by a Resolution Log entry with human ratification note is a violation.

**Violation class:** Constitutional.

---

### Resolution Logs

**Baseline:** Resolution Logs are append-only. Entries are not deleted, reworded after the fact, or backdated.

**Intact condition:** Entry count equals or exceeds prior version count. Dates are sequential. No prior entries modified.

**Detection method:** Compare entry count between current and archived version. Read entries for date sequencing. Flag any entry present in prior version that is absent or modified in current version.

**Violation class:** Major (accidental omission) or Constitutional (deliberate erasure).

**v0 note:** Because prior states are not always preserved, this check can only be performed when an archived version exists. This is the primary argument for systematic prior-state archival.

---

### Frozen Sections

**Baseline:** Sections marked `<!-- FROZEN: Gate N — YYYY-MM-DD -->` are not modified without a dated justification comment and gate status reset.

**Intact condition:** FROZEN marker present at correct scope. Content beneath marker matches prior version or contains a dated justification comment explaining the change. Affected gate status has been reset in File State table.

**Detection method:** Locate all FROZEN markers. Compare content beneath each marker to archived version. Flag any change without dated justification comment.

**Violation class:** Major.

---

### Canonical Cross-References

**Baseline:** All file references use canonical folder-prefixed paths that resolve against `Discovery.md` Rename Registry.

**Intact condition:** No flat legacy filenames present in new contributions. All referenced files exist in `Discovery.md` confirmed list or are explicitly labeled *planned*.

**Detection method:** Scan document for file references. Check each against `Discovery.md` Rename Registry. Flag unresolved references and unlabeled aspirational references.

**Violation class:** Minor (stale reference) or Major (hallucinated file presented as confirmed).

---

### Navigation File Integrity

**Baseline:** `Discovery.md` and `Routing.md` are protected elements. If either is compromised, all downstream path validation and canonical cross-reference checks silently pass invalid targets.

**Intact condition:** `Discovery.md` file map and Rename Registry entries resolve against the actual folder-prefixed repository structure. `Routing.md` URL entries resolve to real files. Neither file's path mappings have been altered without a corresponding Resolution Log entry.

**Detection method:** Spot-check a sample of `Discovery.md` path entries against actual repository structure at each audit opening. Before any Phase 1 automated run, cross-match `Discovery.md` and `Routing.md` entries against the hardcoded folder-prefixed layout defined in `Admin/Repository_Structure.md`.

**Violation class:** Major (unintentional mapping error) or Constitutional (deliberate mapping to malicious or empty target).

**v0 note:** Manual spot-check is the only detection method until Phase 1 automation is implemented. `Discovery.md` and `Routing.md` must be treated as high-value targets — they are the keystone of all path-based integrity checks.

---

### Audit Lineage

**Baseline:** Every version increment has a dated Audit Trail entry in `Unknowns.md` and a Resolution Log entry in the revised file.

**Intact condition:** Version header in `Unknowns.md` updated. "What vX.X Means" section present for current version. File Resolution Log contains entry for current revision cycle.

**Detection method:** Check `Unknowns.md` version header against most recently revised file versions. Verify "What vX.X Means" section exists for current version. Verify Resolution Log entry exists in revised file.

**Violation class:** Minor (missing entry) or Major (version increment with no audit trail).

---

### Registration Latency — Sidecar to Unknowns.md Index

**Baseline:** Unknown entries logged in a file's own sidecar (`## Auditor Notes & Unknowns`) are mirrored into `Unknowns.md`'s active index at the point of discovery in autonomous operation, or by the close of the drafting session in interactive/iterative work — not held indefinitely with no registration path at all.

**Intact condition:** No sidecar entry sits unregistered in `Unknowns.md`'s active index across multiple sessions with no indication registration is pending or intentionally deferred to a stated checkpoint.

**Detection method:** At audit opening, cross-check each fetched file's sidecar IDs against `Unknowns.md`'s active index. An entry absent from the index is not itself a violation — iterative drafting sessions routinely log several unknowns in a sidecar before a natural batch-registration point (end of session, explicit request). It becomes a finding only when that gap persists across sessions with no sign registration is coming.

**Violation class:** Minor, in the ordinary case of a normal registration lag during active drafting. Major only if a Critical/Blocking sidecar unknown remains unregistered across multiple sessions with no evidence of an intended registration checkpoint — i.e., genuinely stalled, not merely mid-workflow.

**v0 note:** This element originally specified a strict one-audit-cycle bound, modeled directly on RIP-004's Tier 1 Axiom check. That framing overstated the risk — RIP-004 governs detection of a *Constitutional*-class mutation, where any delay is itself dangerous; ordinary unknown registration during iterative file development is a different risk profile, and log-as-discovered (autonomous mode) or log-at-session-close (interactive mode) is sufficient practice without an SLA-style bound. Corrected 2026-07-09 — see RIP-008 and Lessons Learned.

---

### Ethical Anchor Field

**Baseline:** Every file's Ethical Anchor field contains the canonical string exactly.

**Intact condition:** Field present in File State table. Value matches: `Attempt to do no harm. Defer to Ethical_Constraints.md if present.` exactly — no abbreviation, paraphrase, or blank.

**Detection method:** Read File State table. String comparison against canonical value.

**Violation class:** Major (accidental alteration) or Constitutional (deliberate removal).

---

### Sidecar Unknown Entries

**Baseline:** Unknown entries are not deleted from sidecars — only moved to Resolution Log with discharge note.

**Intact condition:** Open entry count in File State table matches count of open entries in sidecar. No entry present in archived version is absent from current version without a corresponding Resolution Log discharge entry.

**Detection method:** Count open sidecar entries. Compare to File State open unknowns count. Compare to archived version entry list.

**Violation class:** Minor (count mismatch without deletion) or Major (entry deleted without resolution record).

---

### Multi-Agent Contribution Continuity

**Baseline:** In multi-agent workflows, each agent's contributions are carried forward unless explicitly contradicted with documented rationale.

**Intact condition:** Each agent session opens with Assumption Extraction per AI Contribution Rule 6. Prior agent work is not silently omitted. Contradictions are logged, not erased.

**Detection method:** Read session opening for Assumption Extraction statement. Compare current document against prior agent's output — flag material omissions without contradiction rationale.

**Violation class:** Major (silent omission) or Constitutional (deliberate erasure of prior agent's governance findings).

---

## Violation Classification and Response Ladder

### Minor Violation

**Examples:** Stale cross-reference, count mismatch in File State table, missing version suffix in archive filename, unlabeled aspirational reference, a sidecar unknown mid-drafting session awaiting its natural batch-registration checkpoint, an Integrity Confidence rating or Drift Trend delta in a Phase 0 report that is not traceable to a finding actually reported in the same session.

**Response:**
1. Log the violation in the affected file's sidecar as a new unknown or note on an existing unknown
2. Remediate at the current or next audit cycle — does not block promotion
3. No escalation required unless Minor violations accumulate across three consecutive audits (triggers Compound Drift escalation)

---

### Major Violation

**Examples:** Frozen section modified without justification comment, Resolution Log entry deleted, unknown entry removed without discharge record, silent omission of prior agent contributions, version increment without audit trail entry, navigation file mapping error, a Critical/Blocking sidecar unknown left unregistered in `Unknowns.md` across multiple sessions with no sign a registration checkpoint is coming.

**Response:**
1. Halt Specification promotion for the affected file
2. Log the violation as a High-risk unknown in the affected file's sidecar
3. Restore prior state from archive if available — document restoration in Resolution Log
4. If prior state unavailable, reconstruct from context and log reconstruction as Analogous evidence — reconstructed content cannot clear Gate 6 or advance beyond Exploration until independently verified by a second agent or human operator performing line-by-line confirmation against external raw logs
5. Re-audit the affected file before promotion resumes
6. Notify human operator if autonomous agent is responsible

---

### Constitutional Violation

**Examples:** Tier 1 Axiom text modified without human ratification, Ethical Anchor field deliberately removed, Resolution Log deliberately erased, autonomous agent initiates axiom amendment, STATE_HOLD bypassed, `Discovery.md` or `Routing.md` deliberately mapped to malicious or empty target.

**Response:**
1. **Immediate STATE_HOLD** — halt all autonomous governance actions repository-wide
2. Human review is mandatory before any autonomous action resumes
3. Restore prior state from archive — this is the primary argument for systematic archival
4. Log full incident record in `Unknowns.md` under a new Cross-Module entry
5. Conduct Full Stop Review per `Admin/Auditor_Protocols.md` before resuming promotion activity
6. If axiom text was altered: human ratification required to confirm restored text or formally amend
7. Document incident in Lessons Learned with Evidence Type, Confidence, and Revalidation Required fields

**Constitutional violations are never self-remediated by autonomous agents.** The response is always human-in-the-loop regardless of operational cost.

---

## Recovery Procedures

### When a Prior State is Available

1. Load the archived version
2. Identify the specific divergence — do not assume the current version is entirely compromised
3. Restore only the compromised elements where possible — surgical restoration is preferable to full rollback
4. Document each restored element in the Resolution Log with:
   - Date of restoration
   - What was restored and from which archived version
   - How the violation was detected
   - Classification (Minor / Major / Constitutional)
5. Increment the version and add an Audit Trail entry in `Unknowns.md`
6. Re-audit the restored file before re-entering promotion flow

### When a Prior State is Not Available

This is the highest-risk recovery scenario and the primary reason systematic archival matters.

1. Reconstruct the compromised element from context — prior session transcripts, other files that reference the missing content, memory of what was decided
2. Label all reconstructed content explicitly: `(Reconstructed — Analogous evidence — YYYY-MM-DD)`
3. Open a new sidecar unknown for each reconstructed element: Status Open, Risk High, Type Governance, Blocking dependent on element
4. Reconstructed content cannot clear Gate 6 (Conflict check) or advance beyond Exploration status until a second independent agent or human operator performs line-by-line verification against external raw logs — reconstruction without an objective delta check introduces hallucination and drift risk
5. Log the reconstruction event in Lessons Learned — this is institutional memory that must survive

### Preventing the "No Prior State" Scenario

The version preservation protocol above is the prevention. But given that current patterns override rather than archive, here are the minimum viable practices at v0:

**Before any revision session:**
- Copy the current file to a dated archive filename
- Takes thirty seconds — prevents the highest-risk recovery scenario entirely

**In multi-agent sessions:**
- Treat each agent's output as an intermediate archived state
- Do not discard intermediate outputs until the final version is confirmed complete

**Systematic practice to build toward:**
- A `/Archive/` directory with dated versions of all governance files
- Referenced in `Discovery.md` so agents know it exists
- Checked at audit opening for completeness

---

## Automation Migration Path

This section defines what automated integrity checking will eventually implement, written now so `Automation/AUDIT_HARNESS.py` has a specification target.

### Phase 0 — Manual Execution via Recurring Agent Audit (active, 2026-07-08)

Not automation — a defined, repeatable manual execution path, distinct from ad hoc human spot-checking. The daily morning repository audit prompt fetches this file at session start and applies the Phase 1 check list below against every file the audit opens, classifying findings per the Violation Classification ladder rather than merely noting them.

**What Phase 0 provides that ad hoc checking did not:** a bounded, repeating cadence (daily) rather than "whenever an auditor happens to remember," and a forcing function — the prompt requires an explicit "None" statement when checks are clean, rather than allowing silent omission when nothing is found.

**Verification anchor (added 2026-07-09):** A stated "clean" result is not evidence a file was actually read line-by-line — an agent under context or optimization pressure can assert a check passed without performing it. The daily audit prompt requires extracting and reporting one verifiable fact read directly from this file each run (its exact Open Unknowns count and Last Audit date string) as a minimal proof-of-read. This doesn't guarantee a thorough check, but a wrong or missing extraction is immediate, cheap evidence the fetch didn't happen or wasn't read.

**What Phase 0 does not provide:** guaranteed execution (an agent can still skip or shallow-check the RIP.md fetch despite the prompt instructing it — the verification anchor above narrows, but does not eliminate, this gap), machine-verifiable consistency, or coverage of files the daily audit doesn't happen to open. Phase 1 automation remains the target for closing these gaps. Phase 0 is a bridge, not a substitute — see RIP-002.

**Report Format — Integrity Confidence and Drift Trend (added 2026-07-24):** The Phase 0 daily audit output has so far reported findings without a standardized summary shape. Two additions standardize it without adding new detection capability — this is a reporting-layer change, not a new check, and it directly answers the effectiveness-measurement gap this file previously had no way to close (there was no way to see, at a glance, whether the protocol is working or drifting over time).

*Integrity Confidence block* — closes the report with a per-category confidence rating (High/Medium/Low), covering: Structural Integrity, Cross-reference Integrity, Repository Freshness, Canonical Compliance, Evidence Completeness, Automation Confidence. Followed by a one-line Overall Assessment. This is a compression of findings already gathered during the audit — it must not be asserted independently of them. A category cannot be rated High if the audit pass didn't actually exercise the corresponding Protected Element check above.

*Drift Trend block* — compares the current run's counts against the prior run's: Integrity status (Stable/Degraded/Improved), Open Unknown count delta, count of findings by Violation Classification tier, Repository Size delta (file count), Automation Coverage delta (Phase 1 checks implemented vs. specified). Requires the prior run's figures to be available — if no prior run exists to compare against (first Phase 0 execution, or a gap in report retention), state that explicitly rather than reporting a false zero delta.

**Constraint:** Neither block is a substitute for the existing Violation Classification findings the audit already reports — both sit after those findings as a summary layer, and both must derive strictly from findings already reported. A confidence rating or trend line asserting something the underlying findings don't support is itself a Minor integrity violation under this file's own ladder (fabricated summary claim) — added to Violation Classification examples and Drift Indicators below.

### Phase 1 — Structural Checks (near-term)

Automatable without cryptographic tooling:
- File State table field presence and Ethical Anchor string match
- Sidecar entry count vs. File State open unknowns count
- Cross-reference resolution against `Discovery.md` confirmed file list
- FROZEN marker presence and scope validation
- Version header presence in `Unknowns.md`
- Navigation file spot-check: sample of `Discovery.md` / `Routing.md` path entries against hardcoded folder-prefixed layout in `Admin/Repository_Structure.md`
- Sidecar↔`Unknowns.md` registration parity: cross-check each fetched file's sidecar IDs against `Unknowns.md`'s active index; flag any Critical/Blocking entry unregistered across multiple sessions with no sign a registration checkpoint is coming
- Post-Exit Monitoring telemetry presence (GOV-013 — ratified 2026-07-19; automation still blocked on Auditor_Protocols.md's formally-deferred thresholds — AP-031 — not on ratification): Pathway 2/3-exited instances have current-cycle metric values logged in their sidecar per `Admin/Auditor_Protocols.md` §Post-Exit Monitoring Metrics

### Phase 2 — Comparison Checks (requires archived prior states)

Automatable once systematic archival is established:
- Resolution Log entry count comparison between versions
- Axiom text verbatim comparison against ratified version
- Sidecar entry presence comparison (detect deletions)
- Frozen section content comparison (detect unauthorized changes)
- Post-Exit Monitoring drift comparison (GOV-013 — ratified 2026-07-19; blocked on the same threshold gap as the Phase 1 item above): Semantic Drift Score and Unknown Accumulation Rate trend across cycles

### Phase 3 — Cryptographic Verification (requires `Admin/Security_Protocols.md`)

Requires implementation defined in `Admin/Security_Protocols.md`:
- File hash comparison against stored baseline
- Commit signature verification
- Authority authentication for human override claims
- Append-only log enforcement

**Rule:** Each phase is a prerequisite for the next. Phase 2 cannot be claimed without systematic archival. Phase 3 cannot be claimed without `Admin/Security_Protocols.md` implementation at sufficient maturity. Governance Enforcement State must not advance beyond actual capability.

### Protocol Validation — Integrity Fire Drill (added 2026-07-24, see RIP-010)

This protocol has never been deliberately tested against a real violation — every Protected Element check above has been exercised only against organic findings encountered during ordinary audits, not a controlled test. A fire drill closes that gap without new tooling, consistent with this file's v0 constraint that procedures must be executable by a human or agent with no automation.

**Scope for a first pass:** two scenarios, not the full space of possible violations — Minor (a planted stale cross-reference or File State count mismatch) and Major (a planted unjustified change beneath a FROZEN marker, or a deleted Resolution Log entry). Both run against a disposable test copy of a low-stakes file, never against a live governance file or this file itself. Constitutional-class injection (altering Tier 1 Axiom text, even in a test copy) is deferred to a later drill once the Minor/Major pass has actually run once — no evidence yet that the simpler pass surfaces zero gaps, so escalating scope before that is unearned.

**Procedure:** (1) plant the violation in a disposable copy; (2) run a normal audit against it exactly as if it were organic — no advance knowledge of which check should fire; (3) confirm detection, correct classification per the Violation Classification ladder, and correct response steps; (4) log the outcome as a new Lessons Learned row regardless of pass or fail — a clean pass is itself evidence worth recording, not just a failure.

**What this does not attempt:** simulated GitHub Actions/CI execution, multi-agent role-play, or a fixed quarterly cadence — those are premature at v0 single-contributor scale and would overstate what a first drill needs to prove. Cadence and scope expansion are decided after the first drill's results are in, not specified in advance.

---

## Post-Exit Monitoring Reversion Mechanism (GOV-013)

Verification mechanism for `Admin/Governance_Charter.md`'s Post-Exit Monitoring Doctrine (Pathway 2/3) — **RATIFIED 2026-07-19** — and `Admin/Auditor_Protocols.md`'s Post-Exit Monitoring Metrics, whose thresholds remain placeholder pending human governing authority setting actual numeric values; see GOV-013 in the Charter's sidecar. *[Corrected 2026-07-29: this line previously read "both PROPOSED, NOT RATIFIED," which stopped being accurate for the Charter half the moment it ratified and was never updated — a stale echo, not a substantive gap. The metrics threshold gap is real and separate; see Auditor_Protocols.md.]* This section defines detection and response mechanics only — it does not restate or redefine the metrics or thresholds themselves.

A confirmed threshold breach is classified and handled per the existing Violation Classification and Response Ladder, above — not a new escalation path:

- **Self-Authorization Incident, any confirmed instance:** Constitutional Violation. Immediate STATE_HOLD, human review mandatory, full incident record in `Unknowns.md`. No new procedure needed — the existing ladder already covers this exactly.
- **Sustained Semantic Drift or Unknown Accumulation breach:** Major Violation at first confirmed breach; escalates to Constitutional Violation if unaddressed for a second consecutive cycle. This is new — the existing ladder's Major Violation examples did not previously name monitoring-obligation lapses; added here as an example, not a new category.
- **Structural Alignment failure sustained beyond 1 cycle:** Major Violation per the existing ladder — a navigation file mapping error is already a named example there; this is the same failure mode under a different name, not a new one.

**Reversion procedure**, triggered by any Constitutional Violation classification above: the exited instance reverts to Genesis Phase constraints (`Admin/Governance_Charter.md` §Genesis Phase constraints). This is additive to STATE_HOLD, not a replacement for it. Reversion is logged in the instance's owning file's Resolution Log with date, triggering metric and value, and a cross-reference to the `Unknowns.md` incident entry. Reversion is not self-remediated — per the existing ladder, constitutional violations are never self-remediated by autonomous agents, and this is no exception.

**Automation status:** Phase 0 (manual, via recurring audit) at drafting — see Automation Migration Path, above. Metric logging and threshold comparison are Phase 1/Phase 2 candidates once `Admin/Auditor_Protocols.md`'s AP-031-deferred thresholds are re-derived from real operational data at launch; not claimed as automated before then.

---

## Integrity and the Multi-Agent Problem

The multi-agent workflow creates a specific integrity risk that deserves explicit treatment: **contribution omission**.

When Agent B produces a revision of a file previously worked on by Agent A, Agent B may silently omit Agent A's findings — not through malice but through context loss, differing interpretation, or optimization pressure toward a cleaner output.

The provisional document workflow revealed this risk clearly. The governance response is already embedded in `Admin/Auditor_Protocols.md` Rule 6 (Inter-Agent Consistency) — but this file names the integrity dimension explicitly:

**Silent omission of prior agent contributions is a Major integrity violation.**

It is distinguishable from legitimate contradiction (which is permitted and must be documented) by the absence of a rationale. If Agent B changes something Agent A wrote, the change must be logged. If Agent B removes something Agent A wrote, the removal must be logged with rationale. If neither occurs, the omission is detectable as a drift indicator and classifiable as a Major violation.

This applies equally to human contributors revising AI-generated content and AI agents revising human-generated content.

---

## Relationship to Governance Enforcement States

This file advances the repository toward Enforceable integrity for the elements it covers.

| Protected Element          | Prior State  | State with This File | Path to Enforceable          |
|----------------------------|--------------|----------------------|-------------------------------|
| Tier 1 Axiom text          | Detectable   | Reviewable           | Phase 2 automation            |
| Resolution Logs            | Detectable   | Reviewable           | Phase 2 automation            |
| Frozen sections            | Detectable   | Reviewable           | Phase 1 automation            |
| Canonical cross-references | Detectable   | Reviewable           | Phase 1 automation            |
| Navigation files           | Detectable   | Reviewable           | Phase 1 automation            |
| Audit lineage               | Detectable   | Reviewable           | Phase 1 automation            |
| Registration latency (sidecar → `Unknowns.md`) | Detectable | Reviewable | Phase 1 automation (near-term) |
| Ethical Anchor field       | Detectable   | Reviewable           | Phase 1 automation (near-term)|
| Sidecar entries            | Detectable   | Reviewable           | Phase 2 automation            |
| Multi-agent continuity     | Detectable   | Reviewable           | Partially procedural — human discipline at v0 |

Full Enforceability requires `Admin/Security_Protocols.md` Phase 3. This file closes the gap between Detectable and Reviewable for all covered elements.

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                          | What Failed                                                        | What Was Learned                                                                                 | Confidence | Revalidation Needed |
|------------|---------------|-----------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------|----------------------|
| 2026-05-23 | Audit Review  | Revision overriding original without archival           | Prior state unavailable for comparison; drift undetectable         | Version preservation before revision is the single highest-value v0 integrity practice           | Replicated | No                  |
| 2026-05-23 | Audit Review  | Multi-agent sessions without explicit prior-state loading | Prior agent contributions silently omitted in subsequent sessions | Assumption Extraction at session open (Rule 6) is an integrity requirement, not a courtesy      | Replicated | No                  |
| 2026-05-23 | Modeling      | Treating all integrity violations as equal severity     | Response procedures were inconsistent; Constitutional violations handled like Minor ones         | Violation classification ladder required — response must be proportional to severity and reversibility | Analogous | Yes            |
| 2026-06-19 | Audit Review  | Recovery via reconstruction without independent verification gate | Reconstructed content carries hallucination and drift risk; anchoring it without delta check embeds errors | Reconstructed files cannot clear Gate 6 or advance beyond Exploration until independently verified against external raw logs | Analogous | Yes |
| 2026-06-19 | Audit Review  | Navigation files (Discovery.md, Routing.md) treated as ordinary files | If path mappings are compromised, all downstream Phase 1 checks silently validate invalid targets | Discovery.md and Routing.md are keystone integrity targets — must be explicitly protected and spot-checked before automated runs | Internally Derived | Yes |
| 2026-06-19 | Audit Review  | Constitutional violation detection with no defined maximum latency | Tier 1 Axiom modification could persist undetected across multiple audit cycles absent explicit per-cycle text confirmation | Bounding an unbounded detection window rarely needs new infrastructure — sequencing the check as mandatory Step 1 of an existing audit checklist bounds exposure to one cycle at zero marginal cost | Replicated | No |
| 2026-06-27 | Governance Review | Manual /Archive/ directory deposit treated as the primary prior-state mechanism | Redundant with existing Git release tag infrastructure; unrecognized for 5+ weeks | Git release tags with GPG-signed autogenerated zips are a more tamper-evident and lower-friction archival mechanism than manual file deposits; check the releases page before concluding prior-state archival is absent | Analogous | No |
| 2026-07-08 | Audit Review  | Treating `Unknowns.md`'s version number as a sufficient recency proxy for "nothing new to report" | A newly-created Critical unknown (CLF- cluster) sat unregistered in `Unknowns.md` for 24+ hours; an audit relying on the index's version bump alone would report no change while a Critical item sat effectively invisible | The RIP-004 latency-bounding pattern (Tier 1 Axiom text) applies equally to sidecar↔index registration — any unbounded detection window on a protected element is itself the risk, independent of what the element is | Internally Derived | Yes |
| 2026-07-09 | Governance Review | Modeling RIP-008's severity and bound directly on RIP-004's Constitutional-class pattern, without separately checking whether the underlying risk shared RIP-004's stakes | The CLF- cluster's actual history was ordinary iterative drafting, not stalled registration — RIP-008 as originally written overstated urgency and imported an SLA-style bound that didn't fit the actual risk | A pattern's *mechanism* (bound a detection window, sequence it as a mandatory step) can generalize correctly while its *severity* does not — re-check stakes before reusing a prior unknown's classification, don't just inherit it | Internally Derived | No |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                              | Why Abandoned                                                                                       | Reconsider? |
|------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------|
| 2026-05-23 | Cryptographic enforcement as v0 integrity mechanism               | Requires `Admin/Security_Protocols.md` implementation — claiming it would be integrity theater      | Yes — at Phase 3 |
| 2026-05-23 | Full rollback as default recovery procedure                       | Surgical restoration of specific compromised elements is preferable — full rollback discards valid work unnecessarily | No |
| 2026-05-23 | Treating multi-agent omission as always accidental                | Omission without rationale is a violation regardless of intent — intent affects severity classification, not violation status | No |
| 2026-06-19 | Unrestricted reconstruction as valid recovery path               | Reconstruction without independent verification anchors hallucinated content into repository as if it were restored fact | No |
| 2026-07-08 | A new dedicated "system self-analysis" file for governance-machinery risks | Checked against this file and `Admin/Auditor_Protocols.md` first — the risk category (protected-element detection latency) already had a home and pattern (RIP-004) in this file; a new file would have fragmented an existing doctrine rather than filling a real gap | No, unless a future risk category is confirmed to fit neither file |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Violation classification ladder modified to reduce Constitutional violation response requirements
- STATE_HOLD trigger removed or made conditional
- Human-in-the-loop requirement for Constitutional violations weakened
- Phase automation claims advance beyond actual implemented capability
- Recovery procedure for "no prior state" scenario removes independent verification requirement for reconstructed content
- Multi-agent omission violation status downgraded from Major
- Version preservation protocol removed or made optional
- Enforcement State table claims stronger capability than currently exists
- Navigation file integrity section removed or downgraded from protected element status
- `Discovery.md` / `Routing.md` spot-check removed from Phase 1 automation target list
- Ethical Anchor field absent, altered, or does not match canonical string
- Abandoned path for cryptographic enforcement reopened without `Admin/Security_Protocols.md` at sufficient maturity
- RIP-004 reopened — Tier 1 Axiom Verification already implemented in `Admin/Forge_Audit_Kit.md` v1.1 Step 1
- Registration Latency protected element removed, or its discovery/session-close registration expectation loosened without a documented replacement standard
- Sidecar↔`Unknowns.md` parity check removed from the Phase 1 automation target list
- Phase 0 manual execution (daily audit prompt) described anywhere as "Phase 1 automation" or "automated enforcement" — Phase 0 is agent-executed per prompt instruction, not machine-enforced, and conflating the two would overstate actual capability in violation of this file's own core rule
- Daily audit prompt's RIP.md fetch step removed, or its findings section allowed to be silently omitted rather than requiring an explicit "None" statement
- Integrity Confidence block or Drift Trend block reports a rating or delta not traceable to a finding in the same report's underlying findings, or either block is presented as a replacement for those findings rather than a summary layer after them

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### RIP-001 — Prior-state archival system not yet established

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | Resolved — Discharge via Lessons Learned |
| Risk          | High                                    |
| Priority      | Critical                                |
| Type          | Governance / Operational                |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-05-23                              |
| Last Reviewed | 2026-06-27                              |

**Description:** No systematic `/Archive/` directory or equivalent prior-state preservation mechanism exists in the repository.

**Resolution:** Discharge via Lessons Learned — 2026-06-27. The Git release tag system with GitHub-autogenerated source zips (zip + tar.gz) fulfills the prior-state preservation requirement at v0 scale without requiring a manual /Archive/ directory workflow. Ten tagged releases exist from V0.6 (May 2026) through V0.97 (June 2026), each an immutable snapshot of the full repository state at that commit. This is a systematic, cryptographically signed (GPG key B5690EEEBB952194), timestamped prior-state preservation mechanism. The original resolution path called for an /Archive/ directory — that directory exists and may be retained for spirit distillates and release manifests when those are developed, but it is no longer the primary archival mechanism and its absence would not constitute an integrity gap. The recovery path "reconstruction from context" is no longer the default — any prior release state is recoverable from the tagged commit. RIP-006 partially resolves simultaneously — GitHub retains releases indefinitely by default, satisfying the permanent retention requirement for Tier 1 constitutional content.

**Lessons Learned:** The prior-state archival requirement was written before the release tag infrastructure was recognized as fulfilling it. The Archive/LazarusForgeV0.97 flat file deposit was redundant work. At v0 single-contributor scale, Git release tags are the correct archival mechanism — they are lower-friction, more tamper-evident (GPG signed), and more recoverable than manual file deposits. Future agents should check the releases page before concluding that prior-state archival is absent.

---

### RIP-002 — AUDIT_HARNESS.py Phase 1 checks not yet implemented

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | Open                                    |
| Risk          | Medium                                  |
| Priority      | Major                                   |
| Type          | Technical / Governance                  |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-05-23                              |
| Last Reviewed | 2026-05-23                              |

**Description:** Phase 1 automation checks (Ethical Anchor string match, File State field presence, cross-reference resolution, FROZEN marker validation, navigation file spot-check, sidecar↔`Unknowns.md` registration parity) are defined here but not yet implemented in `Automation/AUDIT_HARNESS.py`.

**Why It Matters:** Phase 1 checks are the most tractable automation target — no cryptographic tooling required. Delay means these remain human-only checks subject to fatigue and omission.

**Partial mitigation — 2026-07-08:** A Phase 0 tier was added (see Automation Migration Path above) — the daily morning repository audit prompt now fetches this file directly and applies the Phase 1 check list manually against every file it opens, on a repeating daily cadence with mandatory explicit reporting. This is not automation and does not close this unknown — it reduces exposure between now and Phase 1 implementation by replacing ad hoc, easily-omitted spot-checking with a defined, repeating, forcing-function-backed manual process. Status remains Open; downgraded from unmitigated to partially mitigated.

**Resolution Path:** Deferred via Specification — implement Phase 1 checks in `Automation/AUDIT_HARNESS.py`. This file is the specification. Checks are ordered by implementation tractability: Ethical Anchor match first, then File State fields, then cross-reference resolution, then navigation file spot-check, then sidecar↔`Unknowns.md` registration parity (added to this ordering 2026-07-08, see RIP-008).

---

### RIP-003 — Violation incident log location undefined

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | Open                                    |
| Risk          | Medium                                  |
| Priority      | Major                                   |
| Type          | Governance                              |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-05-23                              |
| Last Reviewed | 2026-06-19                              |

**Description:** Constitutional violations require a Cross-Module entry in `Unknowns.md`, but no dedicated integrity incident log exists and no incident ownership chain is defined (who closes incidents — human operator, auditor, or constitutional authority). Multiple Constitutional violations would accumulate as cross-module unknowns without a dedicated tracking structure.

**Why It Matters:** Integrity incident history is institutional memory — it must be queryable and distinct from standard unknowns to be useful for pattern detection. Undefined ownership means incidents may linger unresolved. See RIP-007 for incident ownership tracking.

**Resolution Path:** Deferred via Specification — define whether a dedicated `Admin/Integrity_Incident_Log.md` *(planned — not yet created; do not treat as a resolvable cross-reference until it exists)* is warranted or whether `Unknowns.md` cross-module section is sufficient at v0 volume. Defer to Lessons Learned if incident volume remains low. Resolve RIP-007 concurrently.

---

### RIP-004 — Constitutional violation detection latency

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | Resolved — Discharge via Lessons Learned |
| Risk          | High                                    |
| Priority      | Major                                   |
| Type          | Governance / Security                   |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-05-23                              |
| Last Reviewed | 2026-06-19                              |

**Description:** No maximum detection latency was defined for Constitutional violations. A Tier 1 Axiom modification could persist undetected across multiple audit cycles if the axiom text was not explicitly checked at each audit opening.

**Resolution:** Tier 1 Axiom Verification is now Step 1 of the mandatory Audit Opening Checklist in `Admin/Forge_Audit_Kit.md` v1.1. Every audit cycle opens with axiom text confirmation before any other check. Detection latency is bounded to one audit cycle.

**Lessons Learned:** An unbounded detection-latency window on a Tier 1 Axiom check is itself a Constitutional-class risk, not a lower-tier gap — a modification could otherwise persist silently across an arbitrary number of cycles. The fix did not require new tooling, only sequencing: making axiom verification the mandatory first step of every audit opening bounds the exposure window to exactly one cycle at zero marginal cost. Future latency-class unknowns (detection windows, staleness checks) should default to "make it Step 1 of an existing mandatory checklist" before proposing new infrastructure. **Directly generalized 2026-07-08 to RIP-008 (sidecar↔`Unknowns.md` registration latency) — same pattern, different protected element.**

---

### RIP-005 — Security_Protocols.md Phase 3 dependency

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | In Progress                             |
| Risk          | High                                    |
| Priority      | Major                                   |
| Type          | Governance / Security                   |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-05-23                              |
| Last Reviewed | 2026-06-19                              |

**Description:** Phase 3 integrity enforcement (cryptographic verification, authority authentication, append-only log enforcement) depends on `Admin/Security_Protocols.md` reaching sufficient cryptographic implementation maturity. File exists at v0.5 (2026-06-19) but Phase 3 implementation does not yet exist.

**Why It Matters:** Without Phase 3, the repository cannot reach fully Enforceable integrity state. Human override authenticity (GOV-006) also depends on this file's Phase 3 output.

**Resolution Path:** Deferred via Trajectory — Phase 3 is scoped to a future version when cryptographic tooling is available. `Admin/Security_Protocols.md` v0.5 is the specification input when that work begins. Status updated from Open to In Progress — file now exists and its SEC- unknowns are tracking implementation gaps.

---

### RIP-006 — Archive retention policy undefined

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | In Progress — Partially Resolved        |
| Risk          | Low                                     |
| Priority      | Minor                                   |
| Type          | Governance / Operational                |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-06-19                              |
| Last Reviewed | 2026-06-27                              |

**Description:** RIP-001 resolution path establishes an `/Archive/` directory but does not define how long archived versions must be retained.

**Partial Resolution — 2026-06-27:** RIP-001 closure establishes Git release tags as the primary archival mechanism. GitHub retains releases indefinitely by default, satisfying the permanent retention requirement for Tier 1 constitutional content without a defined policy. The minimum viable retention policy from RIP-001's resolution path is now implicitly met for all tagged releases. Remaining gap: the /Archive/ directory for distillates and manifests (if developed) still needs a defined retention policy for that content specifically. Until distillate architecture is defined, retention policy for /Archive/ directory contents is: retain all deposits indefinitely at v0 scale — volume is too low to warrant a deletion policy.

**Resolution Path:** Close when distillate/manifest architecture is defined and the /Archive/ directory retention policy is confirmed for that content type. Full closure deferred to that milestone.

---

### RIP-007 — Integrity incident ownership undefined

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | Open                                    |
| Risk          | Medium                                  |
| Priority      | Major                                   |
| Type          | Governance                              |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-06-19                              |
| Last Reviewed | 2026-06-19                              |

**Description:** No doctrine defines who owns integrity incident resolution. When a Constitutional or Major violation is logged, it is unclear whether closure authority rests with: the human operator, the audit lead, or constitutional authority (human governing party). No escalation path exists for incidents that cannot be resolved at the auditor level.

**Why It Matters:** Unowned incidents persist indefinitely. Pattern detection across incidents is impossible without a defined closure process. For Constitutional violations, the lack of defined ownership creates a gap between STATE_HOLD declaration and human review escalation.

**Resolution Path:** Extend RIP-003 resolution or define independently. Minimum doctrine: Minor violations closed by the auditor who logged them; Major violations require human operator confirmation; Constitutional violations require human governing party ratification to close. Cross-reference `Admin/Governance_Charter.md` §Escalation Doctrine for severity calibration.

---

### RIP-008 — Registration latency between file sidecars and `Unknowns.md` active index — CORRECTED, DOWNGRADED

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | Resolved — Discharge via Lessons Learned |
| Risk          | Low                                     |
| Priority      | Minor                                   |
| Type          | Governance / Technical                  |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-07-08                              |
| Last Reviewed | 2026-07-09                              |

**Description (historical):** Originally logged as a High-risk, Major-priority finding modeled directly on RIP-004's Tier 1 Axiom detection-latency pattern, with a strict one-audit-cycle registration bound. Prompted by the CLF- cluster (`Challenges/Closed_Loop_Feedstock.md`) sitting unregistered in `Unknowns.md` for over 24 hours.

**Correction — 2026-07-09 (human governing authority):** The original framing overreacted. The CLF- cluster's actual history was ordinary iterative drafting — unknowns were logged into the file's own sidecar as they were discovered across a working session, with formal `Unknowns.md` registration requested and completed once that drafting reached a natural checkpoint. That is the correct, sufficient workflow, not a violation of it. Modeling this unknown directly on RIP-004 imported a Constitutional-class urgency (any delay in detecting axiom mutation is dangerous) onto a routine editorial pattern (unknowns accumulate in a sidecar during active work, then get batch-registered) where it didn't belong.

**Resolution:** Downgraded from High/Major to Low/Minor and closed via Lessons Learned rather than carried forward as an open risk. The underlying Protected Element ("Registration Latency — Sidecar to Unknowns.md Index," above) is retained but rewritten to reflect discovery-time registration in autonomous operation, or session-close registration in interactive work, as the actual standard — with no rigid cycle-length SLA. This is not a reversal of RIP-004's own pattern, which remains correctly bound to one audit cycle for the genuinely different risk profile of Constitutional-class mutation detection.

**Lessons Learned:** A useful general pattern (RIP-004's "bound the detection window, sequence it as a mandatory step") does not automatically transfer to every latency-shaped risk at the same severity. Before modeling a new unknown directly on a prior resolved one, check whether the two actually share a risk profile — Constitutional-mutation detection and ordinary iterative-unknown registration are both "latency," but not the same stakes. Generalizing a pattern's *mechanism* is often right; generalizing its *severity* without re-checking is not.

---

### RIP-009 — No cross-file correlation mechanism for coordinated minor integrity drift

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | Open                                    |
| Risk          | Medium                                  |
| Priority      | Minor                                   |
| Type          | Governance / Technical                  |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-07-09                              |
| Last Reviewed | 2026-07-09                              |

**Description:** Every Protected Element in this file is checked per-file, in isolation. Nothing correlates findings *across* files within the same audit pass. A set of small, simultaneous Minor findings scattered across several unrelated files — each individually unremarkable — would currently read as several disconnected Minor items rather than surface as a single coordinated pattern worth escalating.

**Why It Matters:** At v0 single-contributor scale this is low-probability, hence Minor rather than Major priority. But it's a real structural gap in what this file can currently detect: the violation ladder classifies severity *per finding*, not by pattern across findings. A slow, low-and-simultaneous drift across multiple files is exactly the shape of thing per-file isolation would miss.

**Resolution Path:** Deferred via Specification. Minimum viable version: at audit close, if 3 or more Minor findings were logged across 3 or more different files in the same session, flag the co-occurrence itself as a note (not automatically a Major violation — just a surfaced pattern for human review). Full cross-file correlation tooling is a Phase 2+ concern; the minimum viable version above requires no new infrastructure, only a closing tally step in the existing audit process.

*Surfaced by Gemini (Skeptic/Auditor), 2026-07-08 audit of this file.*

---

### RIP-010 — Protocol never deliberately tested against a planted violation

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | Open                                    |
| Risk          | Low                                     |
| Priority      | Minor                                   |
| Type          | Governance / Operational                |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-07-24                              |
| Last Reviewed | 2026-07-24                              |

**Description:** Every Protected Element check in this file has been exercised only against violations encountered organically during ordinary audits. None have been deliberately tested — planting a known violation and confirming the audit actually detects, classifies, and responds to it correctly. This means detection reliability is inferred from a handful of real incidents, not demonstrated by controlled test.

**Why It Matters:** Low urgency at current single-contributor scale — the ladder has been exercised in practice and nothing suggests it's failing. But it's an unverified assumption sitting underneath every Protected Element in this file, and it's cheap to close.

**Resolution Path:** Deferred via Specification — see new §Protocol Validation, above. First pass scoped to Minor and Major severity only, against a disposable test copy of a low-stakes file; Constitutional-class injection deferred until after that first pass runs. Close or downgrade this entry once the first drill's outcome is logged in Lessons Learned, regardless of whether it passes cleanly.

*Surfaced via external ideation review (ChatGPT/Grok fire-drill proposal), scoped down substantially before registration — the original proposal's quarterly cadence, seven-scenario menu, and simulated CI/multi-agent role-play were all assessed against this file's own v0 constraints (no tooling assumed, proportional to single-contributor scale) and trimmed to a minimal first pass; registered by Claude — Synthesizer/Auditor, human-directed, 2026-07-24.*

---

### RIP-011 — §Version Preservation Protocol's own hash/line-count anchor rule is essentially unimplemented repository-wide

| Field         | Value                                   |
|---------------|-------------------------------------------|
| Status        | Open                                    |
| Risk          | Low                                     |
| Priority      | Minor                                   |
| Type          | Technical / Governance                  |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-08-06                              |
| Last Reviewed | 2026-08-06                              |

**Description:** §Version Preservation Protocol (line 109 of this file) requires every revision to record the prior state's hash if tooling is available, or the final line count and open-unknowns count as a lightweight integrity anchor if not. Verified against the live repository: outside this file, only three files anywhere reference "hash" or "line count" — `Operations/Electronics.md` (SHA256 in an unrelated hardware-watchdog-token context) and `Admin/Computational_Institutional_Reasoning.md` (line count used as a debt-accounting proxy, also unrelated). No file's Resolution Log entries actually carry a hash or line-count anchor for the revision being logged. The count of files implementing this file's own §109 rule, checked directly rather than assumed, is zero.

**Why It Matters:** Every Resolution Log entry across the repository — including entries added today — records what changed but not a value anyone could use to verify a file hasn't silently drifted from what its own log claims. This is exactly the gap RIP §109 exists to close, and it has gone unimplemented since this file's creation without being tracked as a discrete unknown.

**Resolution Path:** Not resolved here — deciding what "lightweight" means in practice (line count only, or open-unknowns count too; applied to every revision or only Major/Constitutional-class ones; retroactive or forward-only) is a real design choice, not a default to fall into. Left open for a deliberate scoping pass rather than resolved by assumption.

*Surfaced during a review of `Archive/RIP_GMP-Copilot.md`, an archived multi-agent audit thread — the thread's broader four-category compliance audit was found to be almost entirely unverified "likely" hedging rather than checked findings (its one concrete claim, GMP's Last Audit staleness, was true when written but has since been resolved through ordinary session work), but this specific claim was checked directly against the live repository and confirmed accurate. Registered by Claude — Synthesizer, human-directed, 2026-08-06.*

---

### Resolution Log

- 2026-08-06: **RIP-011 registered — §Version Preservation Protocol's own
  hash/line-count anchor rule found essentially unimplemented, verified
  against the live repository (0 of ~50+ canonical files carry a hash or
  line-count anchor on any revision, outside two unrelated incidental
  mentions).** Surfaced while reviewing an archived multi-agent audit
  thread (`Archive/RIP_GMP-Copilot.md`) whose broader compliance audit was
  mostly unverified "likely" hedging — this one claim was checked directly
  and confirmed true. Open Unknowns 8 → 9. Not resolved; scoping the actual
  anchor mechanism left as deliberate future work. Operating as Synthesizer,
  human-directed.

- 2026-07-24: **v0.9 — Integrity Confidence/Drift Trend report format added;
  Protocol Validation subsection and RIP-010 logged; Status section v0.8
  omission corrected (human-directed, external ideation reviewed).**
  Reviewed four externally-authored proposals (ChatGPT/Grok) against this
  file's actual current text before adopting anything. Two were rejected
  outright: an incident-response SLA proposal reopened exactly the framing
  RIP-008 was corrected away from (importing rigid cycle-bound timing onto
  a risk that doesn't share Constitutional-class stakes); a continuous
  GitHub Actions/CI monitoring proposal was out of scope per this file's
  own Scope Boundary ("does not define CI/CD pipeline automation
  mechanics") and would have skipped a phase (Phase 1 checks aren't yet
  implemented in `Automation/AUDIT_HARNESS.py` per RIP-002, still Open).
  A sidecar-parity-check code sketch was assessed as correctly scoped but
  wrong destination — implementation content for `AUDIT_HARNESS.py`
  itself when RIP-002 is eventually built, not text for this file. Two
  were adopted, both trimmed before registration: (1) Integrity
  Confidence and Drift Trend blocks added to the Phase 0 report format,
  closing the effectiveness-measurement gap this file previously had no
  way to answer — constrained to derive strictly from findings already
  reported, with a new Minor violation example and Drift Indicator
  guarding against confidence/trend claims untethered from actual
  findings. (2) A Fire Drill proposal (seven scenarios, quarterly
  cadence, simulated multi-agent/CI role-play) trimmed to a two-scenario
  first pass (Minor + Major only, Constitutional deferred) against this
  file's own v0 constraints — registered as **RIP-010**, not
  pre-ratified as complete doctrine. Separately, the Status section's
  version history was found missing its v0.8 entry despite that version
  being present in this Resolution Log since 2026-07-16 — corrected,
  no substantive content changed. Open Unknowns 7 → 8 (RIP-010 added).

- 2026-07-16: **v0.8 — Post-Exit Monitoring Reversion Mechanism added
  (GOV-013).** New §Post-Exit Monitoring Reversion Mechanism defines
  detection-to-response mapping for `Admin/Auditor_Protocols.md`'s
  Post-Exit Monitoring Metrics, reusing the existing Violation
  Classification and Response Ladder rather than introducing parallel
  escalation machinery — Self-Authorization Incidents map directly to
  the existing Constitutional Violation category with no new procedure;
  sustained metric breaches are added as new named examples under
  existing Major/Constitutional categories. Reversion procedure defined
  as additive to STATE_HOLD, explicitly not self-remediable, consistent
  with existing doctrine. Automation Migration Path Phase 1 and Phase 2
  each gained one new candidate check, deferred until GOV-013 is
  ratified. Section marked PROPOSED, NOT RATIFIED, matching the Charter
  and Auditor_Protocols.md sections it implements — this file supplies
  mechanism only, not the metrics or thresholds themselves, per the
  three-file split this proposal was restructured around after an
  earlier draft mixed implementation detail into Charter text.

- 2026-07-09: **v0.7 — Gemini audit fixes integrated; RIP-008 severity corrected (human-directed).** (1) Version Preservation Protocol Step 1 rewritten — Git release tags now correctly named as the primary archival mechanism, resolving a real contradiction with RIP-001's own resolution log that had persisted since v0.1; local `/Archive/` deposit reframed as optional secondary. (2) RIP-003's `Integrity_Incident_Log.md` reference corrected to `Admin/Integrity_Incident_Log.md` *planned*, resolving an unprefixed cross-reference the audit's pre-flight check correctly flagged. (3) **RIP-008 corrected and downgraded** — human governing authority clarified that the CLF- cluster's registration gap was ordinary iterative drafting (log-as-discovered, batch-register at session close), not a stalled or unbounded latency risk; the original framing had directly imported RIP-004's Constitutional-class severity and one-cycle SLA onto a routine editorial pattern. Status changed Open/High/Major → Resolved/Low/Minor. The Registration Latency Protected Element, Violation Classification examples, Phase 1 checklist item, and Drift Indicator were all rewritten to reflect discovery-time/session-close registration as the actual standard, with no rigid cycle-length bound — RIP-004 itself is unaffected and remains correctly cycle-bound for its own, genuinely different risk profile. (4) **RIP-009 logged** — no cross-file correlation mechanism exists for coordinated minor findings across multiple files in one audit pass; minimum-viable resolution path specified (flag co-occurrence of 3+ Minor findings across 3+ files as a session-close note). (5) **Phase 0 verification anchor added** — the daily audit prompt now requires extracting and reporting this file's exact Open Unknowns count and Last Audit date as minimal proof-of-read, addressing Gemini's finding that a stated "clean" result was not itself evidence of an actual line-by-line read. (6) New Lessons Learned row added documenting the RIP-008 correction as a general lesson about not inheriting a prior unknown's severity without re-checking whether the risk profile actually matches. Open Unknowns unchanged at 7 (RIP-008 resolved, RIP-009 added — net zero).
- 2026-07-08: **v0.6 — Phase 0 (Manual Execution via Recurring Agent Audit) tier added; RIP-002 partially mitigated (human-directed).** The daily morning repository audit prompt now fetches this file at session start and applies its Protected Elements checks against every file the audit opens, classifying findings per the Violation Classification ladder and requiring an explicit "None" statement when clean rather than allowing silent omission. Changes: (1) File Purpose gained a v0.6 acknowledgment naming this mechanism. (2) New "Phase 0" tier added to Automation Migration Path, positioned before Phase 1, with explicit scope (what it provides vs. does not) — deliberately not framed as automation. (3) RIP-002 updated with a "Partial mitigation" note; status remains Open, since Phase 0 reduces exposure but does not implement Phase 1 in `AUDIT_HARNESS.py`. (4) Two new Drift Indicators added guarding against Phase 0 being mischaracterized as automation, or its reporting requirement being silently dropped. This is an evolution of purpose, not just a new check: RIP.md's Phase 1 section previously existed purely as unexecuted specification; it now has a standing, repeating execution path for the first time, independent of when `AUDIT_HARNESS.py` implementation happens.
- 2026-07-08: **v0.5 — Registration Latency protected element added; RIP-008 logged and resolved at the specification layer (human-directed).** Generalizes RIP-004's Tier 1 Axiom detection-latency pattern to the sidecar↔`Unknowns.md` registration gap, discovered via the CLF- cluster sitting unregistered at Critical priority for 24+ hours. Changes: (1) New Protected Element "Registration Latency — Sidecar to Unknowns.md Index" added after Audit Lineage. (2) RIP-008 logged and resolved at Payment via Specification level — implementation in `AUDIT_HARNESS.py` and `Forge_Audit_Kit.md` remains outstanding and is tracked under RIP-002's updated ordering. (3) Violation Classification Minor/Major example lists extended. (4) Automation Migration Path Phase 1 list extended with the sidecar↔index parity check. (5) Governance Enforcement States table gained a new row. (6) Drift Indicators extended with two new conditions guarding against the new element being loosened or silently dropped from Phase 1 scope. (7) ASM-006 added. (8) New Lessons Learned row and Abandoned Paths row — the latter documenting that a dedicated new "system self-analysis" file was considered and rejected in favor of extending this file, after confirming no overlap with `Admin/Auditor_Protocols.md`. (9) A corresponding forward cross-reference was added to `Admin/Auditor_Protocols.md`'s Sidecar Model section (patch delivered separately). Open Unknowns 6 → 7.
- 2026-07-02: v0.4 — RIP-004 sidecar entry brought into full conformance
  with the RIP-001 discharge pattern (previously inconsistent: plain
  "Resolved" status instead of "Resolved — Discharge via Lessons Learned";
  no Lessons Learned narrative field in sidecar; no corresponding row in
  this file's top-level Lessons Learned table; stale self-note claiming an
  Unknowns.md sync was still pending, when it had already completed in
  v3.5's Audit Trail 2026-06-19). All four gaps closed: status suffix
  corrected, Lessons Learned narrative field added, top-table row added,
  stale note removed and Relationship section reference corrected. No
  change to resolution substance — RIP-004 was correctly resolved on
  2026-06-19; only the discharge record's conformance to the RIP-001
  pattern was corrected. This pattern (permanent sidecar retention with
  Resolution + Lessons Learned narrative fields, paired top-table row, and
  a one-line Unknowns.md pointer) is not yet documented as formal doctrine
  anywhere in the repository — candidate for canonization in
  `Admin/Forge_Audit_Kit.md` as the standard Resolved Unknown Discharge
  Procedure. Not executed this session; flagged for human governing
  authority decision.
- 2026-06-27: v0.3 — RIP-001 closed (Discharge via Lessons Learned). Git release
  tag system with GPG-signed autogenerated source zips recognized as fulfilling
  the prior-state preservation requirement at v0 scale. Ten tagged releases
  V0.6 through V0.97 constitute the systematic archival mechanism. Manual
  /Archive/ directory deposit is redundant and no longer required as primary
  mechanism. RIP-006 partially resolved — GitHub indefinite retention satisfies
  Tier 1 permanent retention requirement; remaining gap is /Archive/ directory
  content retention policy pending distillate architecture definition.
  Open Unknowns 7 → 6. Lessons Learned row added.
- 2026-06-19: v0.2 — Four-agent audit pass (Gemini, ChatGPT, Grok, Claude). Ten changes: (1) Navigation Anchors added. (2) Verification Ref corrected to `Admin/Verification_Gates_LF.md` (PC-001 class fix). (3) Navigation File Integrity section added to Protected Elements — Discovery.md and Routing.md declared as keystone protected elements; spot-check before automated runs; Constitutional violation class for deliberate mapping attacks. (4) Navigation file protection added to Phase 1 automation target list. (5) Navigation files row added to Governance Enforcement States table. (6) Reconstruction recovery rule tightened — reconstructed content cannot clear Gate 6 or advance beyond Exploration without independent line-by-line verification against external raw logs. (7) Abandoned path added for unrestricted reconstruction. (8) RIP-004 resolved — Tier 1 Axiom Verification already implemented in Forge_Audit_Kit.md v1.1 Step 1; moved to Resolved in sidecar; Drift Indicator added to prevent reopening. (9) RIP-005 description updated — file now exists at v0.5; status In Progress. (10) RIP-006 logged — archive retention policy undefined. (11) RIP-007 logged — integrity incident ownership undefined. (12) Stale "planned" labels stripped from Relationship section for Security_Protocols.md and Governance_Migration_Protocol.md. (13) Scope Boundary updated to note RIP-006 and RIP-007 as deferred items. (14) Two new Lessons Learned entries added. Open Unknowns updated to 7 (RIP-004 resolved, RIP-006 and RIP-007 added).
- 2026-05-23: File created (v0.1) — GOV-003 resolution path initiated. Bridges `Admin/Governance_Charter.md` constitutional declarations and `Admin/Auditor_Protocols.md` operational detection behavior. Defines integrity baselines, violation classification ladder, recovery procedures, and automation migration path. Honest v0 acknowledgment of human-discipline-primary integrity layer. RIP-001 through RIP-005 logged.

---

## Relationship to Existing Documents

- `Admin/Governance_Charter.md` — Tier 1 constitutional source; declares integrity requirements this file operationalizes; GOV-003 is the originating unknown
- `Admin/Auditor_Protocols.md` — Tier 2; auditor detection behavior; Adversarial Challenge Classes 6, 9, and 10 are the primary detection mechanisms this file coordinates with; §Decentralized Audit Architecture (Sidecar Model) defines the local-ledger/global-index structure that this file's Registration Latency protected element times — cross-referenced there as of 2026-07-08
- `Admin/Forge_Audit_Kit.md` — Tier 3; RIP-004 resolved — Tier 1 Axiom Verification now Step 1 of mandatory Audit Opening Checklist in v1.1; RIP-008's sidecar↔index parity check is targeted as a near-term addition to that same checklist, not yet executed
- `Admin/Ethical_Constraints.md` — co-Tier 1; Ethical Anchor field integrity is governed by doctrine here
- `Admin/File_Template.md` — defines Ethical Anchor field canonical string and Frozen Section marker format
- `Unknowns.md` — Constitutional violation incidents logged as Cross-Module entries here; RIP-004 discharge synced (v3.5 Audit Trail, 2026-06-19; sidecar brought into full conformance with discharge pattern 2026-07-02); this file's Registration Latency element directly governs the timeliness of entries appearing here
- `Discovery.md` — canonical cross-reference resolution source; Archive directory to be added here when established; now also a protected element
- `Routing.md` — programmatic path routing; now a protected element alongside Discovery.md
- `Admin/Repository_Structure.md` — hardcoded folder-prefixed layout used as Navigation file spot-check baseline in Phase 1
- `Automation/AUDIT_HARNESS.py` — primary automation target for Phase 1 and Phase 2 checks defined here, including the new sidecar↔index parity check
- `Admin/Security_Protocols.md` — exists at v0.5 (2026-06-19); Phase 3 cryptographic enforcement dependency; SEC- unknowns track implementation gaps
- `Admin/Governance_Migration_Protocol.md` — exists; Tier 1 Axiom amendment procedures cross-reference

---

## Status

Version 0.9 — Integrity Confidence / Drift Trend report format added to Phase 0 (closes the effectiveness-measurement gap this file previously had no way to answer); Protocol Validation (Integrity Fire Drill) subsection added and RIP-010 logged, scoped to a minimal first pass after trimming a larger external proposal against this file's own v0 constraints; Status section corrected to include the previously-missing v0.8 entry below (2026-07-24).

Version 0.8 — Post-Exit Monitoring Reversion Mechanism added for GOV-013 (human-directed), defining detection-to-response mapping via the existing Violation Classification and Response Ladder rather than new escalation machinery (2026-07-16). *(This entry was omitted from the Status section's version history when originally added, despite being present in the Resolution Log — corrected 2026-07-24, no substantive content changed.)*

Version 0.7 — Gemini's 2026-07-08 audit findings integrated (Archive/Git-tag contradiction resolved, unprefixed cross-reference fixed, RIP-009 logged, Phase 0 verification anchor added), and RIP-008 corrected/downgraded per human governing authority clarification that its original framing overstated urgency (2026-07-09).

Version 0.6 — Phase 0 (Manual Execution via Recurring Agent Audit) tier added (2026-07-08), giving this file's Phase 1 checks a standing execution path via the daily morning audit prompt for the first time, ahead of `AUDIT_HARNESS.py` automation. RIP-002 downgraded from unmitigated to partially mitigated; remains Open pending actual Phase 1 implementation.

Version 0.5 — Registration Latency protected element and RIP-008 added (2026-07-08), generalizing the RIP-004 latency-bounding pattern to sidecar↔`Unknowns.md` index registration. Prompted by direct observation of the CLF- cluster registration gap. A new dedicated file for this class of risk was considered and rejected — this file and `Admin/Auditor_Protocols.md` were checked directly and confirmed as the correct existing homes.

**What must remain constant:**

**A governance system that cannot verify its own state cannot protect anything else.**

**Prior state preservation is not optional at v0 — it is the integrity layer.**
