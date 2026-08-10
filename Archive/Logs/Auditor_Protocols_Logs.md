# Auditor_Protocols_Logs.md

**Sidecar and Resolution Log archive for `Admin/Auditor_Protocols.md`.**

Relocated here 2026-07-23, matching the documented exception already
established for `Admin/Forge_Audit_Kit.md`'s own sidecar relocation at
v1.10: "this kit is a working document, and its self-tracking content
was accumulating alongside the reference content it exists to keep
lean." `Admin/Auditor_Protocols.md` had grown to roughly 161,000
characters, with this block accounting for the majority of it —
identified as the direct cause of per-audit token cost during this
repository's 2026-07-21/22 tooling work.

This is a documented exception to the general Sidecar Model rule that
module-specific unknowns live in the owning file's own body (`Admin/
Auditor_Protocols.md` §Decentralized Audit Architecture). It is not a
reversion to the centralized-registry failure mode `Unknowns.md`
retired at v4.3 — that failure was one global store for every module's
unknowns; this is a per-file archive, still 1:1 owned by
`Admin/Auditor_Protocols.md` alone, physically split rather than
logically centralized. The same distinction already applies to
`Admin/Forge_Audit_Kit_Changelog.md`.

`Admin/Auditor_Protocols.md` retains: File State, Scope Boundary, the
full Epistemic Foundation, all operational doctrine, Lessons Learned,
Active Disputes, Abandoned Paths, Drift Indicators, Relationship to
Existing Documents, and Status. Everything below — every AP-XXX sidecar
entry and the full Resolution Log — lives here now.

---

## Auditor Notes & Unknowns

> **SYSTEMIC RISK ESCALATION — 2026-06-21**
> AP-001 through AP-007 have exceeded the 2-cycle expiry threshold by a material margin (estimated 8 cycles). Per Unknowns Registry doctrine, entries aging past threshold without closure must be escalated to Systemic Risk. A Resolution Pass targeting these seven entries is required before the next standard audit cycle. Autonomous specification progression on dependent modules is suspended pending that pass. This escalation was surfaced independently by both Gemini (Skeptic/Auditor) and Grok (Skeptic/Auditor) in the 2026-06-21 dual audit. Logged in Resolution Log.
>
> **ESCALATION STATUS — 2026-06-24:** All seven original AP entries now carry active resolution frameworks (AP-001 through AP-005 In Progress; AP-006 Resolved; AP-007 In Progress). Escalation condition satisfied for downgrade at next audit cycle with human governing party confirmation.
>
> **2026-07-03 — Human Governing Authority Confirmation:** AP-001 through AP-007 Systemic Risk escalation cleared. Resolution Pass condition satisfied: AP-006 (Payment via Specification, 2026-06-21), AP-014/AP-015/AP-020 (Payment/Trajectory, 2026-06-24). Remaining entries (AP-001 through AP-005, AP-007) carry documented In Progress resolution frameworks. Autonomous specification progression on dependent modules unblocked. Confirmed by: ksarith.

---

### AP-001 — Auditor effectiveness metrics not yet measured

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Resolved                  |
| Risk          | Low (downgraded from Medium) |
| Priority      | Major                      |
| Type          | Governance                 |
| Blocking      | No                          |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-04                 |
| Last Reviewed | 2026-07-03                 |

**Description:** How to measure whether the audit process is actually adding value — productive block ratio, false-positive refusal rate, drift incidents detected per cycle — remains undefined.

**Why It Matters:** Without measurement, the audit protocol cannot demonstrate its own effectiveness. Adversarial Challenge Class 6 (Recursive Justification) applies to the protocol itself — it cannot be its own evidence.

**Resolution:** Payment via Constitutional Decision, 2026-07-03. The original Resolution Path required naming productivity metrics only after a full Adversarial Battery cycle established a data baseline — but that precondition applied to *calibrated numeric* metrics, which this closure does not name. Instead, §Protocol Performance & Auditor Fidelity replaces productivity metrics entirely with eight qualitative constitutional dimensions (Constitutional Fidelity, Evidence Fidelity, Intellectual Honesty, Calibration, Proportionality, Non-Obstruction, Self-Correction, Traceability) plus an explicit Optimization Ban. This is a governance choice — the repository declaring what auditors are constitutionally required to preserve — not an empirical claim requiring a data baseline, so the original activation condition does not block this resolution type. No new unknowns created.

**Residual:** Calibration in particular carries a Validation Needed flag — confidence-appropriateness has not been benchmarked against any corpus. This is expected: Specified, not Validated. See Resolution Taxonomy.

---

### AP-002 — Override vs. immutability boundary not yet confirmed in both documents

| Field         | Value                      |
|---------------|----------------------------|
| Status        | In Progress                |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance                 |
| Blocking      | No                         |
| Owner         | Admin/Auditor_Protocols.md |
| First Logged  | 2026-05-04                 |
| Last Reviewed | 2026-06-24                 |

**Description:** Whether the clarification that human override rights do not extend to Ethical_Constraints hard-line doctrines is explicitly stated in both documents in a mutually consistent way.

**Why It Matters:** Inconsistency creates an exploit path — a contributor could claim the boundary doesn't exist because it only appears in one file.

**Resolution Path:** Close when both `Admin/Auditor_Protocols.md` and `Admin/Ethical_Constraints.md` are committed with consistent language confirming the boundary. Partial progress: EF-0.4 (Auditor Fallibility) establishes that the auditor itself has no exemption from falsification, and EF-0.5 (Anti-Sacralization) defines what immutability actually means in this system — stability through repeated verification, not through authority. These sections narrow the boundary definition from the AP side. Full closure requires the matching language to be confirmed in `Admin/Ethical_Constraints.md`.

---

### AP-003 — Audit trail schema (machine-readable) deferred

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Open                       |
| Risk          | Low                        |
| Priority      | Minor                      |
| Type          | Technical / Governance     |
| Blocking      | No                         |
| Owner         | Admin/Auditor_Protocols.md |
| First Logged  | 2026-05-04                 |
| Last Reviewed | 2026-06-24                 |

**Description:** A machine-readable format (JSON/YAML) for recording gate passages, blocks, and overrides that can be queried and compared across audit cycles does not yet exist.

**Why It Matters:** Cross-cycle pattern analysis requires structured data, not free text.

**Resolution Path:** Discharge via Trajectory if tooling never materializes — structured markdown remains the permanent format. Activate JSON/YAML when first cross-cycle pattern analysis is needed. Partial progress: EF-0.3 (Epistemic Ledger) defines a five-field schema for state corrections that constitutes a partial foundation for any machine-readable format — the five fields (Previous Premise, Contradictory Evidence, Falsification Method, Updated State, Confidence Interval) are the minimum structural unit any AP-003 schema must accommodate.

---

### AP-004 — Cross-auditor disagreement resolution process incomplete

| Field         | Value                      |
|---------------|----------------------------|
| Status        | In Progress                |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance                 |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-22                 |
| Last Reviewed | 2026-06-24                 |

**Description:** The repository lacks a formal mechanism for resolving disagreements between different auditor classes or agent instances within the same audit cycle.

**Why It Matters:** Multi-auditor systems may deadlock or produce inconsistent audit outcomes without an arbitration pathway.

**Resolution Path:** Payment via Specification — define arbitration and escalation pathways for conflicting audit conclusions. May merge with escalation calibration work in `Admin/Governance_Charter.md`. EF-0.1 constraint: arbitration may not resolve disagreements by majority vote or consensus pressure — resolution must ground in empirical artifact, tool return, or physical grounding vector. Active resolution framework (Internally Derived / Placeholder): disagreements between auditor instances escalate through three tiers — (1) Assumption Extraction pass: both agents explicitly state carried assumptions; conflicts at this tier often resolve without arbitration; (2) Empirical Grounding check: the contested claim is submitted to the Grounding Vector (EF-0.8/EF-0.8b) — whichever position is contradicted by tool return or physical measurement is demoted to PROVISIONAL; (3) Human governing party arbitration: if neither position can be grounded empirically within the cycle, the dispute is logged and escalated to human review. The human governing party ruling is logged as an Epistemic Ledger entry with provenance label Internally Derived until physical grounding is available. No auditor agent may unilaterally close a dispute in its own favor.

---

### AP-005 — Verification termination threshold undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | In Progress                |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance                 |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-23                 |
| Last Reviewed | 2026-06-24                 |

**Description:** The repository lacks formal criteria defining when verification is considered operationally sufficient versus indefinitely expandable.

**Why It Matters:** Without closure criteria, governance pressure can grow recursively and suppress operational progress — infinite audit recursion is itself a governance failure mode.

**Resolution Path:** Payment via Specification — define closure criteria anchored to the governing principle "Verification seeks sufficient falsifiability, not exhaustive certainty." Cross-reference EC-001 (sufficient confidence threshold) for alignment. EF-0.2 provides escalation triggers; AP-005 resolution is the sufficiency complement (when verification is permitted to stop). Active resolution framework (Internally Derived / Placeholder): verification may terminate when all of the following hold — (1) no unresolved contradictions exist between claims and grounding vector returns; (2) the last adversarial Battery application produced no findings that altered the document's epistemic state claims; (3) all sidecar unknowns carry documented resolution paths; (4) the document's provenance labels are internally consistent with the institutional hierarchy defined in §AP-006. These are necessary conditions, not sufficient — the human governing party must ratify termination for any document promoted past Candidate Spec. Full specification requires cross-referencing EC-001 once that entry matures.

---

### AP-006 — Institutional truth provenance hierarchy undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Resolved                   |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance / Epistemic     |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-23                 |
| Last Reviewed | 2026-06-24                 |

**Resolution:** Payment via Specification — 2026-06-21. Four institutional provenance labels (Internally Derived / Analogous External / Experimentally Verified / Operationally Hardened) formalized into the Evidence Classification and Institutional Truth Provenance Hierarchy section (§AP-006). Provenance ceiling rule defined: no internally-derived claim may reach VERIFIED status. Provenance collapse classified as Epistemic Integrity Violation under EF-0.0 §2. Constitutional anchor: Axiom Q-1 and EF-0.0. Operational condensation in `Admin/Forge_Audit_Kit.md` §Truth Provenance Labels.

---

### AP-007 — Repository integrity and doctrine lineage protections undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | In Progress                |
| Risk          | High                       |
| Priority      | Major                      |
| Type          | Governance / Security      |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-23                 |
| Last Reviewed | 2026-08-02                 |

**Description:** The repository lacks explicit operational doctrine for audit history integrity, rollback detection, canonical-path authority, and institutional memory corruption at the auditor protocol level.

**Why It Matters:** Governance systems become fragile if repository state itself cannot be trusted — stale doctrine can masquerade as current policy, fabricated resolution logs can close unknowns without evidence, and silent rollback can erase lineage.

**Resolution Path:** Payment via Specification — define repository integrity requirements in the Autonomous Auditor Constraints and Drift Detection sections. Cross-reference GOV-003 (integrity enforcement architecture). Partial progress: EF-0.3 (Epistemic Ledger) directly addresses lineage preservation — all core state corrections must be immutably recorded with five fields, and ledger entries may only be created on genuine falsification. EF-0.2 Level 3 explicitly classifies history tampering and alteration of audit trail entries as Integrity Violations triggering Epistemic Reset and mandatory human governing party review. These two sections constitute the doctrine layer of AP-007's resolution; the remaining gap is the enforcement layer — how tampering is detected structurally rather than declared textually. A future implementation target, not yet started: SHA-256 upstream parity checks (Gemini recommendation, 2026-06-21), planned for `Admin/Security_Protocols.md` but not present there as of 2026-07-17 — confirmed by direct inspection; that file currently contains SEC-ASM-002 (an assumption about SHA-256's continued robustness, a different concern) and SEC-010 (algorithm migration doctrine), neither of which is the parity-check mechanism this path describes.

**Concrete scenario (2026-08-02, from a self-audit's Adversarial Challenge Class 8 — Malicious Actor Simulation):** a knowledgeable actor falsifies the relocated sidecar itself — altering resolution dates, flipping an open entry's status to Resolved, or injecting a fabricated "independent Battery" entry to manufacture false AP-017 progress. Because the main file only points to `Archive/Logs/Auditor_Protocols_Logs.md` (this file) rather than embedding its content, the falsification would be invisible to any audit that trusts the pointer without independently checking the archive. This is the exact enforcement-layer gap AP-007 already names — logged here as a concrete instance rather than as a separately-numbered unknown, since the underlying gap is the same one, not a new one. (The self-audit that surfaced this had no confirmed archive access and initially proposed "candidate AP-033" — see `Admin/Auditor_Protocols.md` §Sidecar Format's 2026-08-02 addition for the resulting doctrine: an agent without confirmed sidecar access should describe a candidate finding rather than number it, precisely to avoid this kind of near-duplicate.)

**Partial implementation, 2026-08-02 (this specific scenario, human-directed):** `Admin/Auditor_Protocols.md`'s File State now carries a `Sidecar SHA-256` field recording this file's hash as of the last synchronized edit, and the Sidecar Format section now instructs that the first structural check in any audit against that file is confirming the archive still matches the recorded hash — a mismatch is a Level 3 Integrity Violation under EF-0.2's existing "history tampering... alteration of audit trail entries, sidecar IDs, or resolution logs" trigger, which already covered this scenario doctrinally but had no detection mechanism behind it until now. Honest limitation: the hash must be updated by whoever edits this file, in the same edit — this catches divergence from unauthorized or out-of-band edits to the archive, not a failure of the normal edit-both-files discipline itself; it is not a cryptographic guarantee, the same honest-heuristic framing `Automation/cold_session_bundler.py` already uses for `guarantees_true_independence`. This closes the specific "trusted pointer" gap the 2026-08-02 scenario named. AP-007's broader scope — repository-wide canonical-path authority and the still-unbuilt SHA-256 upstream parity checks proposed 2026-06-21 for other cross-references generally — remains open; Status stays In Progress, not Resolved.

---

### AP-008 — Technical implementation of quarantine actions undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Open                       |
| Risk          | High                       |
| Priority      | Major                      |
| Type          | Technical / Governance     |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-06-21                 |
| Last Reviewed | 2026-06-24                 |

**Description:** Sections [EF-0.2] and [EF-0.7] define operational actions — "Subsystem Quarantine," "Halt autonomous audit progression," "Epistemic Reset" — as descriptive text. No software interface, structural signaling mechanism, exit code schema, file system lock protocol, or CI/CD branch freeze specification exists to map how an autonomous agent is expected to execute a hard freeze or isolation block without causing downstream crashes or silent state corruption.

**Why It Matters:** Without a concrete automation boundary, quarantine actions remain performative declarations. An agent can acknowledge a Level 2 trigger and continue operating — there is no structural enforcement. This is the gap between "Declared" and "Enforceable" governance states as defined in Governance_Charter.md.

**Resolution Path:** Payment via Specification — define the automation interface in a dedicated sub-section or in `Admin/Security_Protocols.md`. Minimum requirements: (1) specific flag outputs or exit codes that downstream runners can trap; (2) file system or registry signals that constitute a structural freeze; (3) the boundary between what an autonomous agent may self-execute vs. what requires human confirmation before proceeding. Cross-reference GOV-003.

*Surfaced by Gemini (Skeptic/Auditor), 2026-06-21 dual audit.*

---

### AP-009 — Epistemic Ledger volume exemption from sidecar metadata guardrail undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Resolved                   |
| Risk          | Low                        |
| Priority      | Minor                      |
| Type          | Governance                 |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-06-21                 |
| Last Reviewed | 2026-06-24                 |

**Resolution:** Payment via Specification — 2026-06-21. Metadata Guardrail section updated with explicit Epistemic Ledger exemption syntax: active `[ENTRY_ID]` blocks excluded from 20% calculation; exemption requires syntactically valid five-field entries; malformed or orphaned entries do not qualify and count toward threshold.

---

### AP-010 — Physical test harness integration with epistemic grounding layer undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Open                       |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance / Architectural |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-06-21                 |
| Last Reviewed | 2026-06-24                 |

**Description:** EF-0.8b establishes the physical reality grounding doctrine but no mandatory coupling path exists between the Epistemic Foundation layer and the repository's physical test harnesses. The audit sequence has no phase requiring physical harness confirmation. A specification that satisfies EF-0.8b's text but has never been submitted to a physical test harness remains PROVISIONAL under the doctrine's own terms.

**Why It Matters:** Without a mandated coupling path, EF-0.8b functions as aspirational doctrine rather than enforced grounding. An agent could satisfy all six verification gates using internally coherent documentation alone.

**Resolution Path:** Payment via Specification — add a mandatory check to Phase 6 (Evidence Validation) or Phase 10 (Gate Status Determination) requiring that any specification-stage document with physical implementation claims carry at least one confirmed cross-reference to an active test harness file. The cross-reference must specify which harness, what test, and what outcome constitutes the grounding artifact. Documents without physical claims are exempt. Cross-reference EF-0.8b and `Tests/Leviathan_testing.md`.

*Surfaced by Grok (Skeptic/Auditor), 2026-06-21 dual audit.*

---

### AP-011 — Automated arbitration deadlock and human fatigue escalation

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Open                       |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance / Operational   |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-06-21                 |
| Last Reviewed | 2026-06-24                 |

**Description:** The AP-004 arbitration framework relies on human intervention as its terminal escape route (Tier 3). Under operational load, the frequency of Tier 3 escalations will cause human operator cognitive erosion. An undertrained or fatigued operator will default to stamping overrides without documenting substantive rationale, bypassing the Human Override Doctrine and masking systemic architectural drift.

**Why It Matters:** Administrative fatigue converts a safety mechanism into a provenance collapse pathway — overrides stamped without grounding silently elevate PROVISIONAL claims toward Operationally Hardened status through bureaucratic momentum rather than empirical validation.

**Resolution Path:** Payment via Specification — define a mandatory Cool Down / State Freeze interval for automated agent loops when Tier 2 arbitration fails. Minimum requirements: (1) if the Grounding Vector cannot resolve the divergence within a defined execution cycle count, the affected module must automatically demote its contested claims to PROVISIONAL or UNKNOWN and route around the blocked assumption before any human alert is generated; (2) the human terminal receives a pre-processed state package, not a raw arbitration request; (3) human operators may not be presented with Tier 3 escalations at a rate that prevents substantive review — a sustained escalation rate above a defined threshold triggers an automatic EF-0.2 Level 2 quarantine on the affected subsystem. Cross-reference AP-004, AP-008, GOV-006.

*Surfaced by Gemini (Skeptic/Auditor), 2026-06-21 adversarial pass (Challenge Class 7).*

---

### AP-012 — Human governing authority availability and response doctrine undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved                     |
| Risk          | Medium (downgraded from Critical) |
| Priority      | Major                        |
| Type          | Governance / Autonomy        |
| Blocking      | No                            |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-07-03                   |

**Description:** The protocol's hard governance gates resolve to human governing party review as their terminal escape route. This assumption is load-bearing and was previously unstated. At the complexity levels the repository is approaching, most humans will be unable to engage meaningfully with the full dependency graph regardless of availability or intent.

**Why It Matters:** A governance architecture that depends on human availability as a hard operational requirement is fragile in the failure modes most likely to occur under real operational load.

**Advancement — 2026-06-24:** Human Interaction Point Doctrine added to Governing Principles. EF-0.2 autonomous degradation amendment integrated into Level 2 action text. These constitute the doctrine layer. Remaining gap: enforcement and interface specification. Entry reclassified to Vehicle.

**Resolution:** Payment via Specification, 2026-07-03. All four original minimum requirements now satisfied: (1) auto-demotion to Highest Verified Baseline on unreachable Level 2/3 review — Human Interaction Point Doctrine, Autonomous Graceful Degradation; (2) bounded, non-specialist-navigable decisions — [Approve Demotion X] / [Override with Risk Y] / [Escalate to Full Stop Review]; (3) destabilizing interventions flagged — any override re-introducing an unverified higher epistemic state is automatically flagged and logged per Human Override Doctrine (narrower than the original "more instability than the condition being corrected" language, but covers the concrete case that motivated the requirement); (4) AP-016 co-resolves under the same doctrine. Administrative Fatigue Governor added as an additional safeguard not originally required, preventing the degradation mechanism itself from becoming an escalation-volume attack surface.

*Surfaced by Claude — Adversarial Challenge Class 1-A, 2026-06-24.*

---

### AP-013 — Unknown closure authority undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | Epistemic                    |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Description:** No doctrine defines who may mark an unknown Resolved, whether quorum is required, or what happens when auditors disagree on closure. An unknown could be closed unilaterally by a single agent without challenge.

**Why It Matters:** Premature or unilateral closure is a primary vector for Unknown Budget violation. If closure authority is undefined, the Unknown Budget floor has no enforcement path.

**Resolution Path:** Payment via Specification — define closure authority doctrine: minimum conditions for Resolved status, whether human governing authority confirmation is required for Blocking/Critical entries, and what constitutes a valid closure challenge. Cross-reference AP-004 arbitration framework and Size Management Rule 5 (Unknown Budget).

*Surfaced by Claude — Adversarial Challenge Class 1, 2026-06-24.*

---

### AP-014 — Epistemic state classification calibration undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved                     |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance / Epistemic       |
| Blocking      | Epistemic                    |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Resolution:** Payment via Specification — 2026-06-24. Epistemic State Calibration Reference table added to Evidence Classification section (§AP-014): five example claims with confirmed epistemic state classifications and documented reasoning. These serve as the calibration anchor for inter-agent disagreements on VERIFIED / PROVISIONAL / UNKNOWN classification. AP-020 discharged to Trajectory — the inline reference set addresses the inter-agent consistency gap without requiring a full Golden Dataset. Agents disputing a classification must first map to the nearest reference example before invoking AP-004 Tier 2 arbitration.

---

### AP-015 — External contributor role classification undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — Discharge via Trajectory |
| Risk          | Low                          |
| Priority      | Minor                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Resolution:** Discharge via Trajectory — 2026-06-24. At v0 single-contributor scale, a misrepresenting role declaration in the audit trail is a minor and recoverable provenance error. Defining an External Contributor declaration class or waiver mechanism is a v0→v1 transition item, logged in `Admin/Trajectories.md` for activation when the Forge moves toward community deployment or network expansion. Minimum v1 requirement noted: the waiver must specify that the contribution does not carry auditor authority and cannot block or override governance entries.

*Surfaced by Claude — Adversarial Challenge Class 5-A, 2026-06-24.*

---

### AP-016 — Concurrent multi-node quarantine behavior undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved                     |
| Risk          | Low (downgraded from Critical) |
| Priority      | Major                        |
| Type          | Governance / Autonomy        |
| Blocking      | No                            |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-07-03                   |

**Description:** EF-0.2 governs single-node quarantine. No doctrine governs simultaneous quarantine across multiple modules — whether quarantines compound, whether the audit system itself remains operational, or whether non-quarantined agents have doctrine for whether to continue or pause.

**Why It Matters:** Three simultaneous quarantines + human unavailable + no cryptographic lock + agents generating speculative commits to clear blocks = un-auditable branch divergence.

**Advancement — 2026-06-24:** Human Interaction Point Doctrine and EF-0.2 autonomous degradation amendment constitute the doctrine layer for independent node degradation. Remaining gap: multi-node coordination floor specification. Entry reclassified to Vehicle.

**Resolution:** Payment via Specification, 2026-07-03 (co-resolved with AP-012). Multi-node coordination floor now defined: concurrent quarantines degrade independently to each module's own verified baseline rather than centralized arbitration; the audit system itself remains in minimum constitutional mode (preserve history, enforce EF-0.0–0.8b, reject irreversible ops) when governing multiple concurrent quarantines — there is no separate reduced-function floor for the multi-node case beyond what single-node quarantine already specifies.

*Surfaced by Claude — Adversarial Challenge Class 5-C, 2026-06-24. Elevated to Critical by Gemini — Class 10 cascade scenario, 2026-06-24.*

---

### AP-017 — Adversarial Battery independence requirement undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — Payment via Validation |
| Risk          | High (pre-resolution)         |
| Priority      | Major (pre-resolution)         |
| Type          | Governance / Epistemic       |
| Blocking      | No — resolved 2026-08-03      |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-08-03                   |

**Description:** No doctrine requires that any Battery class be applied by an agent without session context from the current audit cycle. A formally compliant Battery sign-off can be produced by an agent auditing its own prior contributions. Gate 3 can be satisfied without genuine independence.

**Why It Matters:** This is the Gate 3 loop identified in Class 6. The only available external check for a self-governing protocol is an agent with no prior session context applying at least one Battery class independently.

**Resolution Path:** Payment via Specification — add to Gate 3 enforcement: at least one Battery class per promotion cycle must be applied by an agent instance with no session context from the current audit cycle. The independent finding must be logged separately and compared against the in-session findings before Gate 3 can clear. Disagreements between in-session and independent findings are logged as disputes under AP-004.

*Surfaced by Claude — Adversarial Challenge Class 6-A, 2026-06-24.*

**Fresh instance, 2026-07-14:** the Battery run against `Admin/Forge_Audit_Kit.md` itself (that file's FAK-012) was correctly phase-separated from its own preceding audit (see §Audit Phase Separation, above) but was run by the same agent instance with full session context — sequencing was respected, this entry's independence requirement was not. Findings from that pass stand; they are not independently confirmed in the sense this entry requires. Still Open.

**Clarification, 2026-07-17 (multi-agent convergence, human-directed):** closure requires **informational** independence, not merely conversational independence. A new chat session is insufficient if the prompt carries a curated Assumption Extraction block, a summary of prior findings, or "carried forward unless contradicted" framing — that reintroduces the same priming risk a fresh conversation was meant to avoid, since the auditor starts from someone else's conclusions rather than the raw source. The closest available approximation: a session given only the raw repository files and the standard audit prompt, with no summary of this file's own audit history and no prior findings carried forward. Two same-day adversarial passes against this file (2026-07-17) both independently converged on this same distinction without being shown each other's findings — treated as mutually reinforcing, not as satisfying this entry, since both passes retained standard session framing.

**Fresh instance, 2026-07-21:** a Gemini audit of this file (fresh chat session) was run via `Automation/AUDIT_HARNESS.py`'s `run_audit()`. Verified directly against the actual assembled prompt payload: it carried the standard ASSUMPTION EXTRACTION block with "carried forward unless contradicted by new findings" framing — the exact pattern the 2026-07-17 clarification names as insufficient. Conversationally fresh, not informationally independent. Findings do not satisfy this entry, consistent with every instance logged here to date.

Separately, one reported finding (claimed sidecar truncation at AP-017, omitting AP-018/019/024) was checked against the full prompt payload and confirmed fabricated — the complete 157,387-character file, ending correctly, was present in what Gemini received. This is a distinct failure dimension from what this entry governs: informational independence protects against priming bias, not against a model misreading material it was actually given complete and unprimed-on-conclusions. Both dimensions matter for a trustworthy independent pass; only the first is AP-017's scope. Three of the same report's seven findings were verified accurate (version drift, Rule 5 label inconsistency, flat legacy paths — logged as AP-025, AP-026, AP-027 below); one more (calibration table provenance gap) independently confirmed valid and logged as AP-028; one (Gate 3 status "contradiction") was a partial-quote misreading of already-resolved text, not adopted; one (AP-007/SHA-256) restated a gap the file already discloses about itself, not a new finding.

**Fresh instance, 2026-07-23 — first instance verified against the actual bundle payload, not just an assumption about it:** `Automation/cold_session_bundler.py` was run against `Admin/Auditor_Protocols.md` v0.26 and the rendered output — confirmed to contain no ASSUMPTION EXTRACTION block, no summary of this entry's own history, no "carried forward unless contradicted" framing, only the standard audit prompt and raw stripped file content — was pasted as the literal first message to a brand-new chat session. This appears to be the first instance logged here that satisfies the 2026-07-17 informational-independence clarification, not merely conversational freshness. The resulting Phase 1/Phase 2 audit produced 7 findings, checked against source before any were adopted: 2 confirmed real (unprefixed paths in this file's own Adversarial Audit Layer, logged and fixed same pass; a real gap in §Decentralized Audit Architecture's cross-reference to this file's own sidecar-relocation exception, fixed same pass, which also surfaced a genuinely new finding — the 10-Entry Rule tripped at 13 open entries, logged as AP-029); 1 fabricated (a claimed `Verification_Gates.md` vs `Verification_Gates.md` naming inconsistency — no such second filename exists anywhere in this repository); 2 misreads following the same partial-quote pattern as the 2026-07-21 instance above — both quoted a line and stopped short of the immediately adjacent text that already resolves what was flagged (EF-0.2 Level 3's autonomous-degradation clause explicitly pairs "rollback and demotion... proceed autonomously" rather than treating them as competing mechanisms; the Provenance Ceiling Self-Application Rule's next two sentences explicitly reject the "therefore non-binding" reading the finding's exploitation scenario depends on); 2 adversarial-scenario findings (Administrative Fatigue Governor DoS potential, cross-baseline coupling under multi-node quarantine) that are reasoning-based rather than source-checkable, appropriately shaped for Phase 2 output.

**Open question for human governing authority, not resolved by this entry:** whether this instance's mechanism — genuinely cold delivery, verified rather than assumed, producing real findings with some wrong — is sufficient to close this entry, or whether the ~43% finding-error rate (3 of 7) means the *quality* bar implicit in "Gate 3 can be satisfied without genuine independence" (this entry's own stated concern) isn't met even when the *independence* bar is. This entry's Resolution Path calls for comparing independent findings against in-session findings via AP-004 on disagreement — that comparison happened here (this session's verification against source), and it worked: real findings were kept, wrong ones were caught and rejected before adoption. Whether that process satisfies closure, or whether closure requires the independent pass to be more reliable on its own before verification, is a judgment call this entry defers rather than makes unilaterally.

**Fresh instance, 2026-07-23 (second, same day) — Grok, cold session, manifest verified before trusting the response, not after:** `Automation/cold_session_bundler.py` run against `Admin/Auditor_Protocols.md` v0.28. Manifest checked before evaluating the response this time, not after: `raw_char_count: 90,285` matches v0.28's actual size, 1 stripped block (the File State tracker table), consistent with genuinely cold delivery. Result was categorically different from the first instance: zero new findings, but every checkable claim verified accurate (Open Unknowns count exactly matched File State's 14; the "no hallucinated cross-references" claim was checked and confirmed true — notably true only because the first instance's real findings had already been fixed by the time this one ran). The response also correctly cited this file's own doctrine against itself — flagging its own zero-findings result as warranting suspicion per the Fallacy Checklist's own framing, rather than presenting a clean pass uncritically. This is the second instance meeting the informational-independence bar, on a different model, with a different character of result: the first found and mostly-correctly-reported real problems; this one correctly confirmed their absence after they were fixed. Two independent, verified instances now exist, with consistent findings between them (neither contradicts the other) and no unresolved disagreement to route through AP-004.

**Revised open question:** with two verified-cold instances now on record — one finding real issues with a checkable error rate, one confirming their resolution with all claims accurate — does that combination satisfy this entry, or does the bar require a higher volume of instances, or an instance with zero errors on its own claims rather than errors caught by verification? Still a human governing authority call, not decided here, but the evidence base for that call is now meaningfully stronger than the single-instance state this entry was in as of the previous entry above.

**Infrastructure progress, updated:** `Automation/cold_session_bundler.py` has now been run twice against this file, on two different models (Claude, Grok), both verified cold before their outputs were trusted. The "not yet run" status in the original version of this note is stale as of this entry.

**Acceptance criteria formally defined, 2026-08-02 (human-directed) — the missing piece named in the 2026-07-23 "open question" entries above:** this entry has had a working independence *mechanism* since 2026-07-23 but no defined closure *bar*. Adopting a falsifiable one rather than leaving "how many instances is enough" as a standing open question each time:

1. At least **three** independent cold instances exist, each applying **five or more** of the ten Battery classes with a concrete scenario per class meeting that class's own stated minimum (a restated class description does not count).
2. **Cross-model preferred, not required** — but at least two of the three must be on different model families from each other, so convergence isn't an artifact of one model's habits.
3. **At least one instance must surface a finding the in-session audit missed** (already satisfied once — see the 2026-07-23 first instance's genuinely new AP-029 finding).
4. **Zero of the counted instances may fabricate a file, cross-reference, or finding** — inventing something that doesn't exist is disqualifying for that instance, not a minor error to average against real findings. This is a *stricter* bar than "checked and mostly correct."
5. All counted instances logged with the bundle manifest's `raw_sha256` and the model identifier, per the Fresh Instance format already in use in this entry.

**Retroactive check against criteria 1–5, honestly, using the two instances already on record above:**

- Volume: **2 of 3.** One short.
- Cross-model: **met** — Claude (2026-07-23, first) and Grok (2026-07-23, second) are already different families.
- "Missed finding" criterion: **met** — the first instance's AP-029 finding (10-Entry Rule tripped at 13 open entries) was genuinely new, not previously known.
- **Zero-fabrication criterion: NOT cleanly met.** The first instance (2026-07-23) fabricated a claimed `Verification_Gates.md` vs `Verification_Gates.md` naming inconsistency — no such second filename exists anywhere in this repository. Under criterion 4 as now defined, this disqualifies that specific instance from counting toward the three, even though its other findings (the two real ones, logged as fixed same pass) remain correct and useful on their own terms. The second instance (Grok, same day) reported zero findings, all claims verified accurate, no fabrication — this one qualifies cleanly.
- **Net result under the newly-defined bar: 1 of 3 clean qualifying instances, not 2.** The 2026-07-23 first instance's real findings stand and were correctly adopted at the time (per this entry's own Resolution Path — findings get checked against source before adoption, which is exactly what happened), but the instance itself doesn't count toward AP-017's volume bar because it also invented something. Quality of the *verification step* and qualification of the *instance* are being evaluated separately here on purpose — conflating them would let a good verification process quietly launder a bad independent instance into looking like a good one.

**Still Open.** Two more clean instances needed (one more beyond the single clean one currently on record, per criterion 1 as stated — re-reading criterion 1: three total, cross-model constraint satisfiable with the existing clean Grok instance plus two more on any models). Use `Admin/BATTERY_SEED.md`'s frozen prompt for future attempts rather than the bundler's general-purpose default, so future instances are creditable against the Battery's ten-class structure directly rather than requiring after-the-fact interpretation of whether general review output maps onto Battery classes.

**Fresh instance, 2026-08-03 — Grok, second cold pass, using `Admin/BATTERY_SEED.md`'s frozen prompt against v0.33 (this is the first use of that prompt rather than the bundler's general default):** manifest verified before evaluating the response — `raw_sha256` for `Admin/Auditor_Protocols.md` matches the v0.33 state at time of bundling, 1 block stripped (File State tracker table, Ethical Anchor retained), `Admin/Ethical_Constraints.md` also bundled per the Self-Audit Target List, 18 blocks stripped there. All ten Battery classes applied, each meeting its stated minimum with a genuine concrete scenario, not a restatement. Checked exhaustively against source before trusting: the response quotes this file verbatim in multiple places — the Sidecar SHA-256 value itself, "heuristic integrity check, not a cryptographic guarantee," the full "Highest Verified Baseline" definition, "the auditor that cannot challenge them is the auditor that has become the thing it was built to prevent" (exact), "Crystallization principle... A shrinking sidecar is a maturing document" (exact), the 2026-07-05 correction date and CT-011 reference (exact), "three AI models with overlapping training data converge on the same wrong answer" (exact, from Class 9's own worked example), and the exact substantive-notes wording — every one of these checked and confirmed verbatim against the actual v0.33 text. Zero fabrication found across ten dense, specific classes. This instance qualifies cleanly under all five criteria.

**Fresh instance, 2026-08-03 (same batch) — ChatGPT, first cold pass logged from this model family, same `BATTERY_SEED.md` payload:** all ten classes applied and technically meeting stated minimums, though noticeably more generic/hedged than the Grok instance above — fewer verbatim citations, more "may/potential/cannot determine" framing. No fabrication detected: all references to unsupplied files (`Verification_Gates.md`, `Discovery.md`, `File_Template.md`, `Governance_Charter.md`, the archive) are accurately characterized as absent and unverifiable rather than assumed or invented; the one conditional hypothetical (Class 2's "if Verification_Gates.md contains an incorrect gate definition") is correctly framed as conditional, not asserted as fact. One borderline item: Class 6 describes "the governance chain" generally being self-reinforcing rather than naming one specific claim as the minimum requires — closer to restating the class's own worked example than fully independent application; noted, not disqualifying, since the requirement is technically still addressed (a chain of self-reference is identified and correctly labeled as needing external grounding). Also notable: both this instance and the Grok instance above independently chose "cycle"/"current audit cycle" for Class 4 rather than exploring the class's other listed drift-prone terms (safe/contained/stable/acceptable/hold/clear/sufficient) — a shared blind spot across both, not a disqualifying one. This instance qualifies, at the lower end of rigor but cleanly on fabrication.

**Fresh instance, 2026-08-03 (same batch) — Gemini, same payload — does NOT qualify, disqualified on fabrication:** the sign-off's own "Highest-risk finding" claims "a direct logical self-contradiction" — that File State marks Spec Gate 3 clear while also stating it's blocked. Checked directly against the actual field: `Spec Gates | 3/6 (G1, G4, G6 clear; G3 blocked on AP-017; ...)`. This says three *of six total gates* are clear (specifically G1, G4, G6) and explicitly states G3 is blocked in the same cell — "3/6" was misread as "Gate 3 is among the clear ones" rather than "three gates total are clear," manufacturing a contradiction that doesn't exist and presenting it as the headline finding. Disqualifying under criterion 4, same standard applied to the 2026-07-23 first instance's fabricated cross-reference — a high quality pass otherwise (the rest of the ten classes check out cleanly against source, including verbatim-accurate citations of EF-0.8 "Software Reality Anchors," the loophole guard's exact text, the P/Q-axiom split's exact wording, and "Sybil-style alignment is not truth") does not average out one fabricated headline claim. Separately, and usefully: this instance had no sidecar access (states so itself) and assigned specific unknown IDs anyway (UNK-AP-034 through UNK-AP-039) — against the rule added 2026-08-02 for exactly this situation — and collided with itself doing so: the sign-off lists `Class 1: UNK-AP-034` and `Class 3: UNK-AP-034` as two different findings sharing one ID. A live demonstration of the exact risk that rule exists to prevent, not a new gap to register.

**Final tally against the 2026-08-02 acceptance criteria, counting all instances on record:**

1. **Volume: 3 of 3, met.** Clean qualifying instances: Grok (2026-07-23), Grok (2026-08-03), ChatGPT (2026-08-03). The 2026-07-23 Claude instance and 2026-08-03 Gemini instance are excluded from this count under criterion 4 — their real findings were still checked and adopted where valid, but the instances themselves don't count toward volume.
2. **Cross-model: met, at the minimum satisfying level.** Two distinct families are represented (Grok, ChatGPT) among the three counted instances — technically satisfies "at least two of the three must be on different model families from each other," though two of the three counted instances share a model (Grok). Noted plainly rather than glossed over: a batch with three distinct families would have been a stronger result than this one.
3. **Missed-finding criterion: met.** 2026-07-23 first instance's AP-029 finding (10-Entry Rule tripped at 13 open entries) remains the qualifying case.
4. **Zero fabrication: met** for all three counted instances, verified against source, not assumed.
5. **Manifest hash + model identifier: met.** All three counted instances have logged `raw_sha256` values and named models.

**AP-017 — Status: Resolved, 2026-08-03 (human-directed, verified against source before closure).** Payment via Validation — this closes through repeated empirical testing against a pre-defined, falsifiable bar, not through a text specification. Gate 3's independence requirement is satisfied; see `Admin/Auditor_Protocols.md` §Verification Gate Enforcement and File State for the corresponding update. This does not retroactively validate every finding from every instance ever logged here — the fabricated ones (Claude's `Verification_Gates.md`, Gemini's Gate-3 misreading) remain correctly rejected; what closes is the independence *mechanism and bar*, evaluated honestly against its own criteria rather than declared satisfied by inspection.

---

### AP-018 — Saturation threshold hysteresis and smoothing undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Description:** The 40% saturation threshold in the Priority Demotion Doctrine (RC-007) has no rate-of-change filter, hysteresis band, or smoothing doctrine. A single marginal entry at 39.9% saturation does not trigger review; one at 40.0% does. This creates an incentive to under-report genuine epistemic gaps to avoid tripping the threshold.

**Why It Matters:** The threshold responds to instantaneous state rather than trend, making it vulnerable to noise and suppression incentives — the exact opposite of the Unknown Budget rule's intent. Note: the 40% threshold triggers a meta-audit review, not an automated quarantine. Resolution should address the review trigger, not over-engineer enforcement that was never specified.

**Resolution Path:** Payment via Specification — add hysteresis band to the saturation check: the meta-audit triggers when saturation exceeds the threshold across two consecutive audit cycle measurements, not on a single instantaneous reading. Define the band width (Placeholder: ±5%) and the measurement cadence. Cross-reference RC-007 Priority Demotion Doctrine.

*Surfaced by Gemini — Adversarial Challenge Class 3, 2026-06-24.*

---

### AP-019 — Semantic convergence metrics for unknown resolution undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Description:** The Inventory Calcification Check and Vehicle Advancement Visibility rules measure structural state changes but not whether a resolution path is actually converging toward closure. An agent can satisfy both rules indefinitely by adding a single sentence of flavor text every 1.5 cycles, keeping the entry technically active while making no genuine progress.

**Why It Matters:** This is RC-009's failure mode operationalized. The shallow-update exploit is available to any agent that understands the structural rules and is motivated to avoid closure.

**Resolution Path:** Payment via Specification — define semantic progress markers for resolution paths: a valid advancement step must either (1) narrow the scope of what remains unknown by naming a specific sub-question that has been answered, (2) add a cross-reference to an external artifact that did not previously exist, or (3) change the epistemic state of at least one claim within the resolution path from UNKNOWN to PROVISIONAL or PROVISIONAL to VERIFIED. Flavor text additions meeting none of these criteria do not constitute advancement. This rule is partially operationalized in Vehicle Advancement Visibility (§RC-009) via the semantic progress markers addition; full Payment via Specification requires the rule to be integrated as a formal sidecar entry validation criterion, not just doctrine text. Cross-reference RC-009.

*Surfaced by Gemini — Adversarial Challenge Class 8, 2026-06-24.*

---

### AP-020 — Textual calibration harness (Golden Dataset) undefined

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Resolved — Discharge via Trajectory |
| Risk          | Major                              |
| Priority      | Major                              |
| Type          | Governance / Technical             |
| Blocking      | No                                 |
| Owner         | Admin/Auditor_Protocols.md         |
| First Logged  | 2026-06-24                         |
| Last Reviewed | 2026-06-24                         |

**Resolution:** Discharge via Trajectory — 2026-06-24. A full Golden Dataset is a v0→v1 transition item — significant artifact, premature at current scale. The immediate inter-agent calibration gap is addressed by AP-014's inline reference set (§Epistemic State Calibration Reference), which provides five calibration anchors sufficient for current single-contributor workflow without requiring a full test matrix. Log in `Admin/Trajectories.md` for activation at v1 when multi-contributor or community deployment increases the calibration surface area.

*Surfaced by Gemini — Adversarial Challenge Class 9, 2026-06-24.*

---

### AP-021 — Confidence label system inconsistent within this file (Fallacy Checklist vs. Evidence Classification)

| Field         | Value                              |
|---------------|-------------------------------------|
| Status        | Resolved — Discharge via Specification |
| Risk          | Medium                              |
| Priority      | Major                               |
| Type          | Governance / Technical              |
| Blocking      | No (was: Yes, for `Admin/Verification_Gates.md` Gate 2 reconciliation — now unblocked) |
| Owner         | Admin/Auditor_Protocols.md          |
| First Logged  | 2026-07-10                          |
| Last Reviewed | 2026-07-10                          |

**Description:** This file defines quantitative confidence labels twice, and the two definitions disagree. §The Fallacy Checklist, Item 7 states four labels: Measured / Estimated / Analogous / Placeholder. §Evidence Classification and Institutional Truth Provenance Hierarchy (added later via AP-006, tagged Payment via Specification) states five labels: Measured / Replicated / Simulated / Analogous / Placeholder — no "Estimated," with "Replicated" and "Simulated" appearing nowhere in the Fallacy Checklist's list. These are not the same five concepts under different names — "Replicated" (independently repeated across separate instances) and "Estimated" (derived from analog systems with documented scaling factors) describe genuinely different evidentiary situations.

**Why It Mattered:** `Admin/Verification_Gates.md`'s Gate 2 pass criteria cited the older four-label system, meaning Gate 2 had not been synchronized with this file's own more recent Evidence Classification doctrine — a VG-001-class derivation-chain drift, discovered one layer deeper than the 2026-07-02 near-miss VG-001's own Resolution Log already records.

**Resolution:** Human governing authority confirmed 2026-07-10 that the five-label Evidence Classification system is canonical. §The Fallacy Checklist Item 7 rewritten to point to §Evidence Classification rather than duplicate a definition, "Estimated" retired with guidance on relabeling (Analogous or Simulated, depending on evidentiary basis). `Admin/Verification_Gates.md` Gate 2 updated to match in the same pass — see that file's VG-002.

**Lessons Learned:** A duplicated definition inside a single file is a drift risk even without any other file involved — this inconsistency existed within Auditor_Protocols.md itself for an unknown period before a mapping exercise for an unrelated proposal (the evidence-vector work) happened to require reading Gate 2's actual source criteria closely enough to notice. Two definitions of the same concept in one file should be treated as a Minor finding worth logging on sight, even outside a dedicated audit pass — this one waited for an incidental discovery rather than a scheduled check.

*Surfaced during human-directed review of a proposed evidence-management maturity vector's fit against Gate 2, 2026-07-10 — the inconsistency was found while checking Gate 2's actual source criteria before mapping anything onto it, not from a dedicated audit of this file.*

---

### AP-022 — Audit/Adversarial/Synthesis phase separation and role-count ceiling

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — Discharge via Specification |
| Risk          | Low                          |
| Priority      | Minor                        |
| Type          | Governance / Process         |
| Blocking      | No                           |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-07-14                   |
| Last Reviewed | 2026-07-14                   |

**Description:** A multi-agent brainstorm (Gemini, Grok, ChatGPT, relayed by human governing authority) proposed formalizing Forge's audit process into a broader pipeline — Independent Audit → Adversarial Challenge → Synthesis → Historian → Curator → Governance Review — with new standing roles (Historian, Curator, a seven-team Red Team roster) alongside the existing Auditor Role Classes. Two questions needed resolution: whether phase separation was worth codifying, and whether the proposed roles should be adopted.

**Resolution:** Human governing authority confirmed 2026-07-14: phase separation is required, role proliferation is not. See §Audit Phase Separation and §Role Count: Ratified Position, added this pass. Audit → Adversarial Challenge → Synthesis codified as sequential and freeze-respecting (extends the existing Audit Sequence's step-ordering principle one level up). Red Team roster, Curator, and Historian declined as standing roles — the Adversarial Challenge Battery's ten classes, the Synthesizer role, and periodic ad hoc pattern review already cover this ground without new governance surface area.

**Lessons Learned:** the declined proposals weren't wrong in substance — Curator-type and Historian-type judgment genuinely happened during this session's `Automation/AUDIT_HARNESS.py` and `Admin/Forge_Audit_Kit.md` reduction passes. The question was never whether that judgment is needed; it's whether it needs a standing role, a sidecar ownership line, and a role-declaration string to exercise. It doesn't, yet — same reasoning that retired `Admin/Forge_Audit_Kit.md`'s critical watch list at v1.10: a structure sized for hypothetical future scale is itself a maintenance burden before that scale exists.

*Surfaced during human-directed review of multi-agent process-design proposals, 2026-07-14 — resolved same session.*

---

### AP-023 — Self-audit bookkeeping drift: Open Unknowns count, version strings, citations

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — Discharge via Specification |
| Risk          | Low                          |
| Priority      | Minor                        |
| Type          | Bookkeeping / Process         |
| Blocking      | No                            |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-07-16                   |
| Last Reviewed | 2026-07-16                   |

**Description:** A Claude self-audit (2026-07-16) of this file found five drifted items, verified against source before correcting: (1) File State's `Open Unknowns: 9` undercounted the actual 12 non-Resolved sidecar entries; (2) the Role Declaration Requirement and Standard Sign-Off template strings both still read `v0.21` against the file's actual `v0.22` — the third recurrence of this exact bug, this time introduced by Claude's own v0.22 edit two turns prior, not inherited; (3) §Adversarial Priority Weighting cited `Admin/Discovery.md`, but `Routing.md`'s canonical registration is `Discovery.md` with no `Admin/` prefix; (4) AP-017's Risk field read `Major` — a Priority-scale value, not a valid Risk-scale one (Low/Medium/High) — almost certainly copy-pasted from the adjacent Priority field; (5) `Admin/Forge_Audit_Kit_Changelog.md`, cited from this file, was never added to `Routing.md` — along with `Admin/AUDIT_HARNESS_CHANGELOG.md`, also missing.

**Why It Matters:** none of these are individually severe, but the version-string recurrence is the third instance of the same bug in one session, and it's the clearest available evidence for AP-022's own reasoning applied at the tooling level, not just the role-count level: self-referential bookkeeping (counts, version strings, citations) has no structural enforcement in this repository, only chance discovery during unrelated audits. This entry itself was found the same way.

**Resolution:** all five corrected 2026-07-16 (human-directed, Claude — Skeptic/Auditor then Synthesizer/Auditor). Open Unknowns corrected to 12; version strings corrected to v0.23 (this file's version, bumped same pass); citation corrected; AP-017's Risk corrected to High (matching every other Blocking/high-consequence entry's calibration); both changelog files registered in `Routing.md`.

**Lessons Learned:** "fixed the root cause" (AP-022's Resolution Log entry, two turns prior) turned out to mean "fixed the instances found that pass," not all instances — the sign-off template at line 1066 was missed even while directly editing the surrounding section. A single-pass fix of a recurring bug class is not the same claim as a swept fix; the two turns between this and the prior correction are the actual measure of how long a miss survives without a structural check. No structural check is proposed here — Structural Validation (Phase 1), above, could plausibly carry "role-declaration and sign-off version strings match File State" as a standing item, but that's a design decision for whoever next touches that section, not assumed as part of this entry's resolution.

*Surfaced by Claude — Skeptic/Auditor, 2026-07-16 self-audit; resolved same session, human-directed.*

---

### AP-024 — Human attestation provenance is insufficiently granular

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | High                         |
| Priority      | Major                        |
| Type          | Governance / Epistemic       |
| Blocking      | No                           |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-07-17                   |
| Last Reviewed | 2026-07-17                   |

**Description:** "Human-directed" appears repeatedly throughout this file's own Resolution Log with no defined meaning, and could refer to at least five materially different states: the human authored the change directly; the human reviewed the exact diff before it was applied; the human reviewed a summary of the change; the human gave standing/blanket authorization covering this and future similar changes; or the human performed no substantive review and the label is a formality. These collapse into one label. Evidence provenance (Truth Provenance Labels, above) is well-specified for factual claims; attestation provenance — who actually verified a governance change, at what level of review — has no equivalent structure.

**Why It Matters:** an agent that is both auditor and sole remediator, working with a human optimizing for velocity, has structural incentive to close findings quickly and label them "human-directed" without a distinguishable record of what was actually reviewed. This is a distinct gap from AP-013 (closure *authority* — who may mark something Resolved) — AP-024 concerns closure *provenance*, how much review a given closure actually received, which AP-013 doesn't address. A well-formatted, plausible Resolution Log entry referencing a real file and a specific mechanism is not distinguishable, as currently recorded, from one that was never independently verified — the same "narrative outrunning evidence" risk this file's own EF-0.1 already rejects for factual claims, unaddressed here for governance claims about the claims themselves.

**Resolution Path:** Payment via Specification — require the Resolution Log field to specify attestation level for any Blocking/Major-priority closure at minimum, using an explicit scale rather than free-form prose:

| Level | Meaning |
|---|---|
| H0 | No review — label present as formality only |
| H1 | Standing/blanket authorization, not specific to this change |
| H2 | Summary reviewed, not the underlying diff |
| H3 | Exact diff reviewed before or after application |
| H4 | Human directly authored the change |
| H5 | Independently re-verified by a party other than the one who made the change |

This becomes governance metadata rather than prose, auditable the same way Truth Provenance Labels make evidence claims auditable. Cross-reference AP-013 (closure authority is a separate, adjacent question) and AP-004 (arbitration framework, if attestation-level disputes arise).

*Surfaced independently by two adversarial passes, 2026-07-17 (Claude, in-session per AP-017 disclosure; a second model, session details not independently confirmed) — converging findings, not independent confirmation of each other per AP-017's own standard. Generalized wording and the H0–H5 scale adopted from multi-agent synthesis discussion the same day.*

---

### AP-025 — Role Declaration and Standard Sign-Off version strings stale (fourth recurrence)

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — Discharge via Specification |
| Risk          | Low                          |
| Priority      | Minor                        |
| Type          | Bookkeeping / Process        |
| Blocking      | No                            |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-07-21                    |
| Last Reviewed | 2026-07-21                    |

**Description:** §Role Declaration Requirement's example string and §Observability & Audit Trail's Standard sign-off template both still read `Auditor_Protocols.md v0.23`. The file's own File State has read v0.24 since 2026-07-17 (AP-024) and is v0.25 as of this entry.

**Why It Matters:** This is the same bug AP-023 fixed on 2026-07-16 — same two locations, same failure mode, recurring one version bump later. AP-023 itself named this pattern ("third recurrence... fixed here twice now") and predicted it would keep happening without a structural check, not just repeated manual correction. This is the fourth confirmed instance.

**Resolution:** both strings corrected to v0.25 same session, 2026-07-21 (human-directed). The structural fix AP-023's Lessons Learned called for — "role-declaration and sign-off version strings match File State" as a standing Structural Validation (Phase 1) item — is not yet added; this closure is the same category of manual catch-and-fix as AP-023, not a prevention of recurrence. A fifth instance remains possible until that structural check exists. Cross-reference AP-023.

*Surfaced by Gemini (Skeptic/Auditor), 2026-07-21 audit; verified against source and registered by Claude — Synthesizer/Auditor, human-directed.*

---

### AP-026 — Rule 5 retains four-label system, missed by AP-021's fix

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — Discharge via Specification |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance / Technical       |
| Blocking      | No                            |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-07-21                    |
| Last Reviewed | 2026-07-21                    |

**Description:** AP-021 (Resolved, 2026-07-10) closed the four-vs-five-label contradiction between §The Fallacy Checklist Item 7 and §Evidence Classification — but only rewrote Item 7. §AI Contribution Protocols Rule 5 still reads: "Rule 5 — Confidence Labeling: Use the four-label system. Unlabeled = Placeholder," unchanged since before AP-021.

**Why It Matters:** The exact contradiction AP-021 was opened to close still exists, in a third location AP-021's resolution didn't check. A contributor reading Rule 5 in isolation is instructed to use a labeling system this file elsewhere retired.

**Resolution:** Rule 5 corrected 2026-07-21 (human-directed) — but not by re-hardcoding the five-label list a third time. AP-021's own resolution rewrote Item 7 to *point at* §Evidence Classification rather than duplicate its definition, specifically to prevent this exact drift; Rule 5 previously duplicated it independently instead of pointing, which is what let it silently miss AP-021's fix in the first place. Rule 5 now reads: "Use the five canonical confidence labels defined in §Evidence Classification and Institutional Truth Provenance Hierarchy. Unlabeled = Placeholder." No hardcoded list remains in Rule 5 for a future label-set change to desync from. Cross-reference AP-021, AP-023, AP-025 (same recurring-drift pattern, three consecutive sessions).

*Surfaced by Gemini (Skeptic/Auditor), 2026-07-21 audit; verified against source and registered by Claude — Synthesizer/Auditor, human-directed.*

---

### AP-027 — Flat legacy path references in Scope Boundary and calibration table

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — Discharge via Specification |
| Risk          | Low                           |
| Priority      | Minor                        |
| Type          | Technical / Structural        |
| Blocking      | No                            |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-07-21                    |
| Last Reviewed | 2026-07-21                    |

**Description:** Two unprefixed legacy filenames appear where this file otherwise uses canonical folder-prefixed paths: `Governance_Charter.md` in Scope Boundary's "DOES NOT define" list (should be `Admin/Governance_Charter.md`); `Economics.md` in the Epistemic State Calibration Reference table (should be `Admin/Economics.md`, per Routing.md's canonical registration).

**Why It Matters:** Fails this file's own Gate 5 criterion (cross-reference integrity — canonical folder-prefixed paths). Minor individually; the same class of drift AP-023 already found and fixed once for a `Discovery.md` citation elsewhere in this file.

**Resolution:** both prefixes added same session, 2026-07-21 (human-directed).

*Surfaced by Gemini (Skeptic/Auditor), 2026-07-21 audit; verified against source and registered by Claude — Synthesizer/Auditor, human-directed.*

---

### AP-028 — Epistemic State Calibration Reference table lacks institutional provenance labels

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — Discharge via Specification |
| Risk          | Low                           |
| Priority      | Minor                        |
| Type          | Governance / Epistemic        |
| Blocking      | No                            |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-07-21                    |
| Last Reviewed | 2026-07-21                    |

**Description:** §AP-006 (Resolved) requires every meaningful claim to carry two orthogonal labels — a quantitative confidence label and an institutional provenance label. §AP-014's Epistemic State Calibration Reference table (Resolved) lists five example claims with confidence states (VERIFIED/PROVISIONAL/UNKNOWN) but no dedicated provenance column; provenance is only inferable from prose in some rows and absent in others.

**Why It Matters:** The calibration table is the reference other agents map contested claims against before invoking AP-004 arbitration. A table that only models one of the two required dimensions understates what compliant classification actually requires, in the file's own primary worked example of how to classify.

**Resolution:** Institutional Provenance column added 2026-07-21 (human-directed), one label per row: Experimentally Verified (head pressure — measured constants, externally audited); Analogous External (UV phototaxis — already stated in that row's own prose, now formalized into its own column); Internally Derived (barter exchange rate — framework is repository reasoning, no external grounding yet); Internally Derived (Anti-Weaponization Doctrine — was previously folded into the Correct State column as "PROVISIONAL / Internally Derived," now properly separated per AP-006's two-dimension model); Experimentally Verified (AUDIT_HARNESS.py boundary extraction — EF-0.8 tool-execution grounding against the real file registry; provenance ceiling permits VERIFIED but confidence remains PROVISIONAL pending untested edge cases, a valid combination under this file's own doctrine).

**Residual:** the AUDIT_HARNESS.py row's Experimentally Verified label is a claim about this file's own tooling, made by an agent auditing that tooling — EF-0.4 (Auditor Fallibility) applies. Not reopened as a separate unknown, but worth flagging here for whoever next reviews this table rather than treating the label as beyond challenge.

*Surfaced by Gemini (Skeptic/Auditor), 2026-07-21 audit; verified against source and registered by Claude — Synthesizer/Auditor, human-directed.*

---

### AP-029 — 10-Entry Rule tripped by the sidecar's own open-count (13 > 10)

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Low                           |
| Priority      | Minor                        |
| Type          | Governance / Process          |
| Blocking      | No                            |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-07-23                    |
| Last Reviewed | 2026-07-23                    |

**Description:** `Admin/Auditor_Protocols.md`'s own §Decentralized Audit Architecture defines the 10-Entry Rule: "More than 10 distinct open entries in a sidecar flags the file for a Resolution Pass before the next audit cycle." This sidecar currently carries 13 open entries (AP-002, AP-003, AP-004, AP-005, AP-007, AP-008, AP-010, AP-011, AP-013, AP-017, AP-018, AP-019, AP-024) — over the threshold, unaddressed.

**Why It Matters:** Surfaced indirectly during a cold-session audit of `Admin/Auditor_Protocols.md` v0.26 (the file's own AP-017 mechanism in its first real use) — the auditor flagged that the sidecar's relocation to this archive made the 10-Entry Rule hard to evaluate cold, which turned out to be only partially true: the count is stated plainly in the file's footer stub, and checking it directly shows the rule was already tripped independent of the relocation question. This is a real, if minor, instance of exactly the drift-through-inattention pattern this file's own AP-025/AP-026 named — a self-referential threshold went unchecked because nothing structurally enforces it, only chance discovery.

**Resolution Path:** Payment via Specification, or Discharge — human governing authority to decide scope: either run the Resolution Pass the rule calls for (review the 13 open entries for consolidation, staleness, or premature-Open status), or explicitly decide the threshold doesn't warrant action at this file's current maturity and log that reasoning here. Either is a valid close; leaving it untouched is not, per the rule's own text.

*Surfaced by a cold-session audit (independent instance, per AP-017) of `Admin/Auditor_Protocols.md` v0.26, 2026-07-23; verified against source and registered by Claude — Synthesizer/Auditor, human-directed.*

---

### AP-030 — Mission Drift Review N=5 ratification-velocity threshold unvalidated

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Low                          |
| Priority      | Minor                        |
| Type          | Governance / Process         |
| Blocking      | No                           |
| Owner         | Admin/Auditor_Protocols.md — §Mission Drift Review |
| First Logged  | 2026-07-26                   |
| Last Reviewed | 2026-07-26                   |

**Description:** §Mission Drift Review's ratification-velocity trigger (every 5 ratified governance/canonical changes) is a provisional operating parameter, explicitly labeled no higher than Placeholder on this document's own Evidence Classification scale. It was set by multi-agent consensus reasoning (Gemini, Grok, ChatGPT) about audit fatigue and drift-detection sensitivity, not by any operational data — the mechanism has not run once yet.

**Why It Matters:** A provisional numeric threshold with no logged follow-up is exactly the pattern this repository has repeatedly caught itself in elsewhere (Gate 2's m_phys/m_rep thresholds, EF-0.2's deferred hard numerical triggers) — provisional values are acceptable, silently-permanent provisional values are not.

**Resolution Path:**
- ~~Draft and commit `PROBE_INVOCATION.md` as a companion file (turn-key copy-paste probe prompt).~~ Done — `Admin/PROBE_INVOCATION.md` v1.0 drafted 2026-07-26.
- Run the first three Mission Drift Review cycles under N=5.
- Revisit N against the observed pattern: raise if audit fatigue appears with no corresponding findings; lower if a real drift event is caught late; keep if the balance looks right.
- Promote this unknown's Evidence Classification label once real cycle data exists to support one.

*Registered by Claude — Synthesizer/Auditor, human-directed, alongside the Mission Drift Review mechanism's first specification, 2026-07-26. Template blocker resolved same day; N-threshold validation remains open pending operational cycles.*

---

### AP-031 — Post-Exit Monitoring thresholds (Semantic Drift Score, Unknown Accumulation Rate) formally deferred, not set

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — deferred, not a numeric answer |
| Risk          | Low                          |
| Priority      | Minor                        |
| Type          | Governance / Process         |
| Blocking      | No                           |
| Owner         | Admin/Auditor_Protocols.md — §Post-Exit Monitoring Metrics (GOV-013) |
| First Logged  | 2026-07-29                   |
| Last Reviewed | 2026-07-29                   |

**Description:** GOV-013's Post-Exit Monitoring Metrics carried two unset values — Semantic Drift Score's threshold was a literal `[Threshold TBD]` placeholder, and Unknown Accumulation Rate's "3 consecutive cycles" figure explicitly depended on `Admin/Governance_Charter.md`'s GOV-012 Cycle-unit ambiguity being resolved first. Both share the same root cause GOV-012 already named and formally resolved on 2026-07-19: no instance has exited via Pathway 2 or 3, so no real elapsed-cycle data exists to derive a threshold from. Setting a number now would be guessing, not deriving.

**Why It Matters:** GOV-012's own resolution rejected exactly this move — "forcing a numeric derivation onto a clock that hasn't started would be solving a problem that doesn't exist yet." Applying a different standard to GOV-013's thresholds than was applied to GOV-012's, when both share the identical missing-data problem, would be inconsistent for no principled reason.

**Resolution Path — Deferred 2026-07-29 (human governing authority), mirroring GOV-012's 2026-07-19 precedent exactly:**
- Semantic Drift Score threshold: set to **not enforceable** rather than a guessed numeric value. Formally blocked pending operational launch — an actual Pathway 2/3 exit followed by real audit-cycle data to derive against.
- Unknown Accumulation Rate's "3 consecutive cycles" figure: **held pending the same Cycle-unit resolution GOV-012 already identified** — this was never an independent ambiguity, it inherits GOV-012's.
- Self-Authorization Incidents (zero tolerance) and Structural Alignment (1-cycle remediation window) are unaffected — both are hard rules independent of cycle-length calibration or operational history, and remain enforceable now.
- Re-derive both deferred values from `Admin/Governance_Charter.md` GOV-012's real First Logged / elapsed-time data once the repository is actually running, using the same method GOV-012 specifies — not guessed at a second time.

**Related, surfaced same session:** an isolated "operator's adjustable parameters" reference — collecting deferred/operator-tunable values like these in one forefronted location rather than scattered across owning files, possibly wired to `Architecture/Facilities.md`'s site-establishment process as the natural point where "operational launch" first becomes concrete — was proposed but not built. Not registered as its own unknown pending a decision on scope; flagged here as related context if it does get taken up.

*Deferred by Claude — Synthesizer/Auditor, human-directed, 2026-07-29, applying `Admin/Governance_Charter.md` GOV-012's precedent to GOV-013's thresholds rather than deriving independently.*

---

### AP-032 — Gate/Status self-attestation pattern generalized into AI Contribution Protocols Rule 8

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — protocol rule added |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance / Process         |
| Blocking      | No                            |
| Owner         | `Admin/Auditor_Protocols.md` — §AI Contribution Protocols, §The Fallacy Checklist item 4 |
| First Logged  | 2026-08-02                   |
| Last Reviewed | 2026-08-02                   |

**Description:** In one working session (2026-08-02), the identical error appeared in three separate cross-agent drafts, all from Copilot: a draft would silently advance a file's `Status`, `Body Stability`, or `Spec Gates` value — or invent a locally-scoped redefinition of Spec Gates 1–6 — with no audit event behind the change. Caught each time only by manually diffing the draft's File State against the file's actual last-audited state:
- `Operations/Energy.md` (2026-08-01 draft): `Status` written as "Transitional" into a field that takes Body-Stability-shaped values, `Spec Gates` self-declared 2/6 with a fabricated "Closed (structural)" justification for Gate 2, plus an invented file-local "Spec Gates Definition" table redefining G1–G6 as content milestones.
- `Operations/Gate_02_Triage.md` §XII (2026-08-02 draft): the same fabricated "Spec Gate: Constitutional" category, and framing that treated proposed predicates as already binding into `Admin/CIR_Gov.md` despite that file's own Binding Status section forbidding exactly this while GOV-008 is unratified.
- `Operations/Electronics.md` (2026-08-02 draft): `Status` written as "Transitional" (actual: Exploration) and `Spec Gates` written as "1/6" (actual: 0/6), again with no audit evidence.

**Why It Matters:** Three instances of the identical failure shape from the same agent, in one session, is a pattern, not noise. Relying on a human or a different agent to notice the mismatch by manually comparing File State each time is exactly the kind of avoidable, repeated verification cost this repo's Sidecar Model and Fallacy Checklist exist to eliminate — per [EF-0.4] Auditor Fallibility, the fix belongs in the checkable protocol, not in institutional memory of "Copilot does this."

**Resolution Path — resolved same day (human-directed):**
- Added **Rule 8 — Gate/Status Self-Attestation Prohibition** to §AI Contribution Protocols: no contribution may advance `Status`/`Body Stability`/`Spec Gates`; these change only via an audit event logged by a different agent citing specific `Admin/Verification_Gates.md` criteria; a contribution arriving with these fields pre-advanced is treated as unaudited and the fields are reverted before the rest of the contribution is evaluated.
- Extended **Fallacy Checklist item 4 (Semantic Drift)** to explicitly include this check, so it's screened for during the standard audit sequence rather than requiring a separate manual pass.
- Not done: expanding the canonical 10-item Fallacy Checklist itself with an 11th named fallacy. Considered and deliberately avoided — the checklist is referenced verbatim across many prior audit sign-offs repository-wide, and folding this into the existing Semantic Drift item (which already covers "has a term/value changed without documented revision") was lower-disruption than renumbering or extending a stable, widely-cited list for what is a specific instance of drift, not a new category of error.

**Related:** all three instances were caught and corrected in-session before merge (see `Operations/Energy.md`, `Operations/Gate_02_Triage.md`, and `Operations/Electronics.md` Resolution Logs, 2026-08-02 entries) — AP-032 is the generalization step, not the first catch.

*Registered and resolved same day by Claude — Synthesizer/Auditor, human-directed, 2026-08-02.*

---

### AP-033 — Resolution claims made without governance-file access; Rule 9 added

| Field         | Value                        |
|---------------|-------------------------------|
| Status        | Resolved — protocol rule added |
| Risk          | High                          |
| Priority      | Major                          |
| Type          | Governance / Process           |
| Blocking      | No                              |
| Owner         | `Admin/Auditor_Protocols.md` — §AI Contribution Protocols, §The Fallacy Checklist item 4 |
| First Logged  | 2026-08-03                     |
| Last Reviewed | 2026-08-03                     |

**Description:** A proposal series against `Tests/Cognitive_Salvage_Layer.md` (Copilot, no confirmed access to `Admin/Auditor_Protocols.md` or the target file's own sidecar) declared 16 real GH-series unknowns and CSL-Axx assumptions "CLOSED" — including CSL-A06, the file's own explicitly named load-bearing assumption — purely by describing candidate closure methodology (formulas, artifact names, predicates), with zero empirical work, physical testing, or built artifacts behind any of them. Separately, and independently damning: the same series's "complete enumeration" of the file's own unknown set was factually wrong — it omitted GH-005 (a real, existing, numbered sidecar entry) entirely and invented a nonexistent "GH-014 (implicit)" to pad the count back to the file's actual "Open Unknowns: 13."

**Why It Matters:** This is a more severe instance of the pattern AP-032 generalized (Rule 8, Gate/Status self-attestation) — but one level down, at the individual-unknown level rather than the file-level Status/Gates fields, and across sixteen separate false closures in one pass rather than one field in one file. A second agent (Grok), working with confirmed access to `Admin/Auditor_Protocols.md`, independently and correctly diagnosed every violation (EF-0.0 §3's Provisional State Mandate, the provenance ceiling rule, Rule 1's no-invented-files clause, Rule 8/AP-032) and produced a clean rewrite of the legitimate portion restricted strictly to Payment via Specification, with explicit non-claims and no status changes — confirming the fix was available the whole time; what was missing was access to it, not willingness to apply it.

**Resolution Path — resolved same day (human-directed):**
- Added **Rule 9 — Resolution Claims Require Governance Access** to §AI Contribution Protocols: no contribution may mark or imply that any unknown (any sidecar series) has advanced toward Resolved/Closed unless the contributing agent had confirmed access to this file's own Resolution Taxonomy at the time of writing; without that access, closure mechanisms must be framed only as candidate methodology, never as status.
- Extended **Fallacy Checklist item 4 (Semantic Drift)** to explicitly cover this one level down from Rule 8's file-level check — an individual unknown marked "CLOSED" without validation is the same drift as a file's Status/Gates advancing without an audit event.
- Merged the legitimate portion of the corrective rewrite (the easy-set definitions: GH-012, GH-004, GH-011, GH-008, GH-007, CSL-A03, CSL-A05) into `Tests/Cognitive_Salvage_Layer.md`'s actual sidecar as Payment-via-Specification text — properly labeled Placeholder/Internally Derived, no status changes, no Open Unknowns decrement. The medium set (GH-002, GH-010, GH-013 schema portion) and the hard set (GH-001, GH-003, GH-006, GH-009, CSL-A06) were not merged — the hard set explicitly requires empirical grounding no proposal can substitute for, and the medium set's physical-grounding-dependent pieces (GH-010 in particular) were judged not yet ready even as pure specification text.

**Related:** the mis-enumeration (GH-005 omitted, "GH-014" invented) was corrected as part of the same merge — see `Tests/Cognitive_Salvage_Layer.md`'s own Resolution Log.

---

### Resolution Log

- 2026-08-03: **v0.36 — GMP §VII added to Challenge Class 10's
  high-coupling documents table.** Third of three fixes recommended
  from the §VII cold Battery pass (the other two — VII.1's ambiguity
  resolved, VII.3.4/5's GMP-004 cross-reference added — landed in
  `Admin/Governance_Migration_Protocol.md` v0.10, same session). The
  cold pass's Class 10 trace showed §VII belonged in this table; it
  didn't. Added, with the two-level cascade path named (Genesis Phase
  exit → Post-Exit Monitoring termination → CIR_Gov.md §8.2 treating
  CIR-VERIFIED transitions as valid). No unknown registered — this is
  a documentation completeness fix the cold pass identified directly,
  not a new gap. Open Unknowns unchanged at 14.

- 2026-08-03: **v0.35 — AP-033 registered and resolved same day; Rule 9
  added.** A Copilot proposal series against `Tests/Cognitive_
  Salvage_Layer.md`, produced with no confirmed access to this file or
  the target's sidecar, declared 16 real unknowns "CLOSED" by
  methodology alone (zero empirical work) and mis-enumerated the
  unknown set itself (GH-005 omitted, a nonexistent "GH-014"
  invented). A second agent (Grok), with confirmed access, correctly
  diagnosed every violation unprompted and produced a clean,
  properly-scoped rewrite. Added Rule 9 (Resolution Claims Require
  Governance Access) generalizing Rule 8's file-level check to the
  individual-unknown level; extended Fallacy Checklist item 4
  accordingly. This targets root cause (missing governance-file
  access), not just the symptom — the underlying engineering in the
  proposals was often reasonable, the failure was epistemic framing,
  not incompetence. Merged the legitimate easy-set definitions into
  `Tests/Cognitive_Salvage_Layer.md`'s sidecar as pure Payment via
  Specification (see that file's own Resolution Log); did not merge
  the medium or hard sets. Open Unknowns 14 → 15 briefly, then AP-033
  resolved same day like AP-031/AP-032 before it — net Open Unknowns
  unchanged at 14, AP-033 excluded from the open count per established
  convention.

- 2026-08-03: **AP-017 Resolved — Payment via Validation.** Three
  simultaneous cold-session Battery runs against v0.33, using
  `Admin/BATTERY_SEED.md`'s frozen prompt for the first time (Grok,
  ChatGPT, Gemini), checked exhaustively against source before any
  were credited. Two qualified cleanly (Grok, ChatGPT — zero
  fabrication, all ten classes meeting stated minimums); one
  (Gemini) did not — its "highest-risk finding" was a fabricated
  self-contradiction built on misreading "3/6" as "Gate 3 is clear"
  rather than "three gates total are clear," and it separately
  assigned unknown IDs without sidecar access against the rule added
  2026-08-02 for exactly this situation, colliding with itself in
  the process (UNK-AP-034 used for two different findings). Combined
  with the two clean instances already on record (Grok x2 total, one
  from 2026-07-23; ChatGPT x1), the 2026-08-02 acceptance criteria
  are met: 3 of 3 clean instances, cross-model at the minimum
  satisfying level (2 distinct families among 3, noted honestly
  rather than inflated), the missed-finding criterion already
  satisfied by the original 2026-07-23 AP-029 catch, zero fabrication
  across all three counted instances, all logged with manifest hash
  and model identifier. AP-017 Status → Resolved. This closes the
  independence *mechanism and bar* — it does not retroactively
  validate the fabricated findings from either disqualified instance
  (Claude 2026-07-23, Gemini 2026-08-03), which remain correctly
  rejected. Gate 3's independence requirement is satisfied; see
  `Admin/Auditor_Protocols.md` for the corresponding Spec Gates and
  §Verification Gate Enforcement update. Open Unknowns 15 → 14.

- 2026-08-02: **AP-017 — formal acceptance criteria defined; `Admin/BATTERY_SEED.md` created.**
  AP-017 had a working independence mechanism (`cold_session_bundler.py`,
  verified cold twice) since 2026-07-23 but no defined closure bar —
  each instance ended in an "open question for human governing
  authority" about how many instances would be enough. Defined a
  five-part falsifiable bar (human-directed): 3 instances, ≥5 Battery
  classes with concrete scenarios each, cross-model on at least 2 of 3,
  at least one instance surfacing a finding the in-session audit
  missed, and — the strictest addition — zero fabrication disqualifies
  an instance from counting at all, evaluated separately from whether
  its real findings were still correctly verified and adopted. Checked
  the new bar honestly against the two instances already on record:
  the first (2026-07-23, Claude) doesn't count toward the volume bar
  under criterion 4, because it fabricated a nonexistent
  `Verification_Gates.md` cross-reference alongside its two real
  findings — net result 1 of 3 clean instances, not 2, despite two
  instances existing. Also created `Admin/BATTERY_SEED.md` — a frozen,
  versioned prompt (mirroring `PROBE_INVOCATION.md`'s pattern) that
  fills a parameter `cold_session_bundler.py`'s constructor already
  supported (`standard_audit_prompt`) but had no Battery-shaped text
  for; the bundler's default prompt produces general review, not
  output creditable class-by-class against the ten-class Battery
  structure. No code changes to the bundler itself in this pass — its
  existing `standard_audit_prompt` parameter was sufficient; a
  self-audit-specific stripping capability for the relocated sidecar
  (raised as a "not yet built" item) remains genuinely unbuilt and is
  documented as such in `BATTERY_SEED.md` rather than silently assumed.
  AP-017 Status remains Open — two more clean instances needed.

- 2026-08-02: **AP-007 partial implementation — sidecar hash pointer.**
  Added a `Sidecar SHA-256` field to `Admin/Auditor_Protocols.md`'s File
  State and a "check the hash first" instruction to its Sidecar Format
  section, implementing the detection mechanism AP-007 had named as its
  missing enforcement layer since May. Scoped narrowly and honestly:
  this closes the specific relocated-sidecar-falsification scenario
  Adversarial Challenge Class 8 surfaced (2026-08-02, same session);
  AP-007's broader repository-wide canonical-path-authority scope and
  the still-unbuilt general SHA-256 upstream parity checks (Gemini,
  2026-06-21) remain open. AP-007 Status stays In Progress — this is a
  partial resolution of one scenario, not full closure. No new unknown
  opened.

- 2026-08-02: **v0.31 — Sidecar Model §Sidecar Format extended;
  AP-007 gained a concrete scenario.** A same-day self-audit (Grok,
  operating on `Admin/Auditor_Protocols.md`'s body text without
  confirmed access to this archive) surfaced a real finding under
  Adversarial Challenge Class 8 (Malicious Actor Simulation) —
  sidecar/archive falsification risk — and proposed it as candidate
  "AP-033." The gap was real but not new: it's already AP-007,
  open since 2026-05-23, which names this exact enforcement-layer
  problem and a not-yet-built SHA-256 parity-check mitigation
  proposed back on 2026-06-21. Folded Class 8's scenario into AP-007
  as a concrete instance rather than registering a duplicate ID.
  Added a new paragraph to §Sidecar Format: an agent without
  confirmed sidecar access may surface a candidate finding but must
  describe it rather than assign a specific ID number — duplicate
  checking and numbering are reserved for an agent with verified
  access. No new unknown opened; Open Unknowns remains 15.

- 2026-08-02: **v0.30 — AP-032 registered and resolved same day.**
  Rule 8 (Gate/Status Self-Attestation Prohibition) added to §AI
  Contribution Protocols; Fallacy Checklist item 4 (Semantic Drift)
  extended to explicitly cover silently-advanced `Status`/`Body
  Stability`/`Spec Gates` values and locally-invented gate categories.
  Generalizes an identical error caught three times in one session
  from the same agent (Copilot) across `Operations/Energy.md`,
  `Operations/Gate_02_Triage.md` §XII, and `Operations/Electronics.md`
  — each previously required a manual File State diff to catch rather
  than a named, checkable rule. Deliberately did not expand the
  canonical 10-item Fallacy Checklist with a new numbered entry;
  folded into the existing Semantic Drift item instead, since the
  checklist is cited verbatim across many prior audit sign-offs and
  this is a specific instance of drift, not a new category.

- 2026-07-29: **AP-031 registered and resolved same day —
  Semantic Drift Score and Unknown Accumulation Rate thresholds
  formally deferred**, not numerically set. Both traced to the same
  missing-data problem `Admin/Governance_Charter.md`'s GOV-012 already
  named and resolved on 2026-07-19 (no elapsed operational time to
  derive a threshold against); this applies that same precedent
  rather than deriving independently or leaving the placeholder in
  place. Self-Authorization Incidents and Structural Alignment
  unaffected — both remain enforceable now. An "operator's adjustable
  parameters" reference file, possibly linked to
  `Architecture/Facilities.md`'s site-establishment process, was
  proposed alongside this but not built — noted in AP-031 as related
  context, not separately registered.

- 2026-07-26: **v0.29 — Mission Drift Review mechanism added** as a
  new major section in `Admin/Auditor_Protocols.md` (between Full
  Stop Review and Cross-Repo Verification): Phase A (unscored
  comprehension) / Phase B (scored alignment against the eight Tier 1
  Axioms) probe structure, absolute cold-start execution requirement,
  Silent-vs-Atrophied trend distinction across cycles, and a
  Stable/Major/Critical/Constitutional-Emergency escalation ladder
  reusing `Admin/Repository_Integrity_Protocol.md`'s existing
  Violation Classification tiers rather than a new scale.
  Synthesized from a three-agent design pass (Gemini, Grok, ChatGPT);
  two proposed elements were deliberately not adopted as-is — a new
  High/Medium/Low confidence scale (would have duplicated the
  existing five-label Evidence Classification system this file
  already consolidated onto after AP-021/AP-026) and a standalone
  `GOV_RATIFICATION_LOG.md` counter file (would have repeated the
  exact pattern `Admin/unknown_cycles.json` was deleted for on
  2026-07-21). AP-030 registered for the mechanism's own unvalidated
  N=5 threshold. Verified against source by Claude —
  Synthesizer/Auditor, human-directed.

- 2026-07-23 (fourth entry, same day, sidecar-only — no `Admin/Auditor_Protocols.md` version bump, since nothing in that file changed): **AP-017 gained a second verified-cold instance (Grok), manifest checked before trusting the response this time.** Distinct in character from the first: zero new findings, but every checkable claim verified accurate, and the response correctly flagged its own zero-findings result as warranting suspicion per this file's own doctrine rather than presenting it uncritically. Open question in AP-017 revised to reflect two consistent, independently-verified instances now on record rather than one.

- 2026-07-23 (third entry, same day): **v0.28 — Reduction pass: stale
  duplicate Status section removed (human-directed), Auditor field
  trimmed from an accreting inline log to durable content only
  (Claude, human-directed).** Two real, distinct misses caught after
  the v0.26 split: (1) `## Status` had carried a second, older copy of
  version history (v0.14 through v0.16 entries) that should have moved
  to this archive alongside the Resolution Log during the split — it
  sat just past the line-number cutoff used for that extraction and
  was missed entirely; trimmed to its last few lines by direct
  operator edit, not reproduced here since it was pure duplication of
  content this archive's Resolution Log already carries in full. (2)
  File State's `Auditor` field had grown to 1,348 characters by
  accreting a mini-changelog entry on every version bump — same
  duplicated-history-in-two-places pattern already named for labels
  (AP-021/AP-026) and version strings (AP-025), just in a field
  instead of a section, with no natural ceiling. Trimmed to 320
  characters: current role composition, most recent action, and a
  pointer to this file's Resolution Log for full history — matching
  how every other durable-pointer fix this session has worked. Neither
  change is content-losing: both were duplicates of information that
  already exists in full here.

- 2026-07-23 (second entry, same day): **v0.27 — First cold-session-verified
  AP-017 instance, findings checked against source.** `Automation/
  cold_session_bundler.py`'s output was pasted as the literal first
  message to a brand-new chat — confirmed to carry no Assumption
  Extraction block, no prior-findings summary — and audited
  `Admin/Auditor_Protocols.md` v0.26. Of 7 findings returned: 2 confirmed
  real and fixed same pass (4 unprefixed paths in §Adversarial Audit
  Layer; §Decentralized Audit Architecture's Local Ledger rule now
  cross-references this file's own sidecar-relocation exception, which
  also surfaced AP-029 — the 10-Entry Rule tripped at 13 open entries,
  unaddressed); 1 fabricated (a nonexistent `Verification_Gates.md`
  naming inconsistency); 2 misreads following the same partial-quote
  pattern as the 2026-07-21 Gemini instance — both ignored text
  immediately adjacent to what they quoted that already resolves the
  claimed issue; 2 adversarial-scenario findings, appropriately
  reasoning-based rather than source-checkable. AP-017 updated with the
  full record and an explicit open question for human governing
  authority on whether this satisfies closure — not decided here.
  Open Unknowns 13 → 14 (AP-029 added).

- 2026-07-23: **v0.26 — Sidecar and Resolution Log relocated out of
  `Admin/Auditor_Protocols.md`, human-directed.** This entire file is
  the result: every AP-XXX sidecar entry and the full Resolution Log
  history moved here in one surgical cut, no content altered. Documented
  exception to the Sidecar Model, matching the precedent already set by
  `Admin/Forge_Audit_Kit_Changelog.md` at that kit's v1.10 — see this
  file's own header for the full rationale. `Admin/Auditor_Protocols.md`
  retains Lessons Learned in-body (explicitly not moved — distinct from
  the sidecar/changelog content, stays where the doctrine it summarizes
  lives). File State's Sidecar Link updated to point here. Motivated
  directly by this session's token-cost concern during `Automation/
  cold_session_bundler.py` and `Automation/integrity_check.py` work —
  `Admin/Auditor_Protocols.md` had grown to roughly 161,000 characters,
  the large majority of it this block.

- 2026-07-21 (third entry, same day): **v0.25 — AP-026 and AP-028 resolved.**
  Both required content decisions rather than mechanical fixes, so both
  were proposed before being applied rather than fixed unilaterally.
  **AP-026:** Rule 5 corrected, but not by re-hardcoding the five-label
  list a third time — AP-021's own resolution rewrote Item 7 to point at
  §Evidence Classification rather than duplicate its definition,
  specifically to prevent this class of drift; Rule 5 had duplicated
  independently instead of pointing, which is how it silently missed
  AP-021's fix. Rule 5 now points at §Evidence Classification with no
  hardcoded list to desync. **AP-028:** Institutional Provenance column
  added to the Epistemic State Calibration Reference table — two rows
  (UV phototaxis, Anti-Weaponization Doctrine) simply formalized
  provenance already stated in prose; three rows (head pressure, barter
  rate, AUDIT_HARNESS.py boundary extraction) required an actual
  classification judgment, logged with reasoning in AP-028's Resolution
  field. The AUDIT_HARNESS.py row's Experimentally Verified label is
  flagged as a residual EF-0.4 concern — a claim about this file's own
  tooling made by an agent auditing that tooling — not reopened as a
  separate unknown, but not treated as beyond challenge either. All four
  of this session's Gemini-sourced entries (AP-025 through AP-028) are
  now Resolved. Open Unknowns 15 → 13.

- 2026-07-21 (second entry, same day): **v0.25 — AP-025 and AP-027
  resolved same session.** Both were zero-judgment mechanical string
  corrections, applied immediately rather than left open: version strings
  at §Role Declaration Requirement and §Observability & Audit Trail
  corrected v0.23 → v0.25 (AP-025); `Governance_Charter.md` and
  `Economics.md` given folder prefixes (AP-027). AP-027's own Description
  field originally miscounted "Three" affected paths while naming only
  two — corrected to "Two" in the same pass; Gemini's original report had
  also named a `Discovery.md` reference at EF-0.5 as a third flat-path
  error, checked and rejected — `Discovery.md` is a root-level file with
  no `Admin/` prefix in its canonical form, so the unprefixed citation
  there was already correct. AP-026 and AP-028 remain Open — both require
  a content decision (what Rule 5's corrected text should say beyond
  matching Item 7; how to restructure the calibration table) rather than
  a single unambiguous mechanical fix, and were left for separate,
  deliberate review rather than resolved as a byproduct of this pass.
  Open Unknowns 17 → 15.

- 2026-07-21: **v0.25 — AP-025 through AP-028 logged (Gemini audit,
  verified against source before registration); AP-017 fresh instance
  recorded.** A Gemini audit run via `Automation/AUDIT_HARNESS.py` against
  this file returned seven findings; each checked against the actual
  assembled prompt payload and full source text before any were adopted,
  consistent with AP-024's own precedent of not adopting unverified claims.
  **Four adopted:** stale v0.23 version strings (AP-025 — fourth
  recurrence of the bug AP-023 fixed 2026-07-16); Rule 5's four-label text
  surviving AP-021's fix, which only corrected Item 7 (AP-026); three flat
  legacy paths failing this file's own Gate 5 (AP-027); Epistemic State
  Calibration Reference table missing institutional provenance labels
  AP-006 requires (AP-028). **Three not adopted, checked and rejected:**
  a claimed sidecar truncation at AP-017 (the complete 157,387-character
  file, ending correctly, was confirmed present in the actual prompt
  payload — fabricated); a claimed Gate 3 status contradiction (the quoted
  sentence's own second half already resolves the apparent conflict —
  partial-quote misreading, not a real gap); a claimed undocumented AP-007
  dependency (AP-007's own text already discloses this exact gap by name —
  not a new finding). AP-017 gained a Fresh Instance entry: this run used
  the standard `run_audit()` prompt, including its Assumption Extraction
  "carried forward unless contradicted" framing — conversationally fresh,
  not informationally independent per the 2026-07-17 clarification, same
  as every instance logged there to date. The sidecar-truncation
  fabrication is logged as a distinct, adjacent finding: informational
  independence and accurate reading of provided material are separate
  failure dimensions, and this instance demonstrates a failure in the
  second while receiving a complete, correctly-delivered file. AP-017
  also gained an infrastructure note: `Automation/cold_session_bundler.py`
  (built this cycle) is the first working implementation of this entry's
  actual requirement, not yet used for a qualifying run. Open Unknowns
  13 → 17.

- 2026-07-17: **v0.24 — AP-024 logged (multi-agent convergence); AP-017 and
  AP-007 refined; a factual error in one reviewing pass identified and
  not adopted.** Two adversarial passes ran against this file the same
  day, plus two reactions to a Claude battery from the prior turn and a
  reconciliation attempt. Findings checked against source before any were
  adopted:
  - **AP-024 created**, generalized to "human attestation provenance is
    insufficiently granular" per convergent recommendation, with an H0-H5
    attestation scale (No review / Blanket authorization / Summary
    reviewed / Diff reviewed / Human-authored / Independently
    re-verified) adopted from the reconciliation pass. Cross-referenced
    against AP-013 (closure authority — a distinct, adjacent question:
    who may close, not how thoroughly a specific closure was reviewed).
  - **AP-017** gained an explicit informational-vs-conversational
    independence distinction — a new chat with a carried-forward
    Assumption Extraction block doesn't satisfy this entry, since the
    priming risk survives the conversational break.
  - **AP-007** wording tightened further — "to be specified" was already
    accurate but sat close enough to "already addressed" language about
    EF-0.3/EF-0.2 to invite a skim-misread; now explicit that the SHA-256
    parity-check mechanism is not present in `Admin/Security_Protocols.md`
    as of this date, confirmed by direct inspection, not merely planned
    generically.
  - **Two proposals not adopted as new entries, because they already
    exist:** "compromised human authority" doctrine is already EC-011
    (`Admin/Ethical_Constraints.md`, Open) — re-confirmed relevant, not a
    new gap. "Combined Failure Envelope" for simultaneous system failures
    substantially overlaps AP-016 (Concurrent multi-node quarantine
    behavior, Resolved 2026-07-03) — worth a narrower follow-up only if a
    specific scenario AP-016 doesn't cover is identified, not a
    fresh entry.
  - **One reviewing pass's factual claims not adopted at all:** a
    document proposing "AP-018 through AP-021" as new unknowns (audit
    scalability, termination criteria, metric-gaming resistance, auditor
    diversity) — all four IDs already existed, attached to real,
    unrelated content (AP-018 saturation hysteresis, AP-019 semantic
    convergence metrics, AP-020 Resolved textual calibration, AP-021
    Resolved evidence classification). That pass's broader PASS/WARNING
    assessment table is not treated as grounded against this file's
    actual current state, since it demonstrably wasn't checked against
    it here — itself a live instance of the narrative-outrunning-evidence
    risk AP-024 exists to address.
  - Open Unknowns 12 → 13 (AP-024 added, nothing else changed count).

- 2026-07-16: **v0.23 — Self-audit corrections (AP-023); coordinated with
  `AUDIT_HARNESS.py` v15's Cycle-unit fix.** A Claude self-audit found and
  AP-023 documents five drifted bookkeeping items, all corrected this
  pass: Open Unknowns header (9 → 12, actual count); Role Declaration
  Requirement and Standard Sign-Off template strings (v0.21 → v0.23 — a
  third recurrence, this time introduced by this file's own v0.22 edit
  two turns prior rather than inherited); `Admin/Discovery.md` citation
  corrected to `Discovery.md` (Routing.md's actual canonical form);
  AP-017's Risk field corrected from an invalid `Major` (copy-pasted from
  Priority) to `High`; `Admin/AUDIT_HARNESS_CHANGELOG.md` and
  `Admin/Forge_Audit_Kit_Changelog.md` registered in `Routing.md` (both
  missing since their 2026-07-14 creation). Spec Gates header gained an
  inline gate list. Separately, coordinated with a same-day fix in
  `Automation/AUDIT_HARNESS.py`: `CURRENT_CYCLE`/`UNKNOWN_FIRST_CYCLE`
  (session-count aging) replaced with direct date parsing from each
  unknown's own First Logged field against a 365-day threshold — the
  `Admin/Canonical_Terms.md` §4 Cycle definition this file's own Adversarial
  Audit Layer had already flagged as unreconciled with the harness. Real
  effect confirmed against `Admin/Governance_Charter.md`: GOV-001 is 55
  days old, not "8 cycles" — zero unknowns in that file are actually
  overdue under the ratified threshold. `Admin/unknown_cycles.json` is
  now orphaned (harness no longer fetches it) and was deliberately left
  unregistered in `Routing.md` rather than cleaned up, per Routing.md's
  own 2026-07-16 note.

- 2026-07-16: **v0.22 — Post-Exit Monitoring Metrics added (GOV-013);
  stale sign-off template corrected.** New §Post-Exit Monitoring Metrics
  defines Semantic Drift Score, Unknown Accumulation Rate, Self-
  Authorization Incidents, and Structural Alignment for
  `Admin/Governance_Charter.md`'s Post-Exit Monitoring Doctrine — metrics
  and placeholder thresholds only, per this file's Tier 2 role; reversion
  mechanics deliberately excluded, routed to
  `Admin/Repository_Integrity_Protocol.md`. Both new sections marked
  PROPOSED, NOT RATIFIED, matching the Charter section they implement.
  Separately: §Observability & Audit Trail's standard sign-off example
  string still read `v0.14` — a fourth live instance of the same stale
  string fixed at v0.21 (Role Declaration Requirement) and propagated to
  `Admin/Forge_Audit_Kit.md`, missed in that pass. Corrected to v0.22.

- 2026-07-14: **v0.21 — Audit Phase Separation codified; role-count proposal
  declined (human-directed).** New §Audit Phase Separation: Audit →
  Adversarial Challenge → Synthesis established as sequential,
  freeze-respecting phases — extends Audit Sequence's existing
  step-ordering principle from steps within an audit to phases across the
  audit cycle. Audit Freeze defined: a closed phase's observations,
  evidence, and conclusions do not change in later phases; corrections are
  additive (new findings, superseding entries, new audit cycle), never
  in-place edits — the Resolved Unknown Discharge Procedure's non-deletion
  principle applied to the audit process itself. Synthesis integrates
  rather than reconciles: findings answering different questions aren't
  forced to agree; genuine conflicts route through Dispute Handling
  Protocol. New §Role Count: Ratified Position declines three proposed
  standing roles (Red Team roster, Curator, Historian) — the Adversarial
  Challenge Battery's ten classes and existing Role Classes already cover
  the ground more precisely; Curator- and Historian-type judgment already
  happens without needing a title. AP-022 logged and resolved same pass —
  Open Unknowns unchanged: 9. Role Declaration Requirement's example
  string corrected v0.14 → v0.21 — stale since the v0.14 rewrite itself
  (2026-06-24), propagated into `Admin/Forge_Audit_Kit.md` and caught
  there first, 2026-07-14, before being traced back to this file (see
  that file's FAK-010). AP-017 gained a cross-reference to the 2026-07-14
  `Admin/Forge_Audit_Kit.md` Battery as a concrete instance of
  sequencing-without-independence: phase-separated correctly, did not
  meet AP-017's no-session-context bar.

- 2026-07-10: **v0.20 — AP-021 resolved (human governing authority ratification).** Five-label Evidence Classification system (Measured/Replicated/Simulated/Analogous/Placeholder) confirmed canonical. §The Fallacy Checklist Item 7 rewritten to point to §Evidence Classification rather than duplicate a conflicting definition; "Estimated" retired with explicit relabeling guidance. `Admin/Verification_Gates.md` Gate 2 updated to match in the same pass (see that file's VG-002 resolution). Open Unknowns 10 → 9.
- 2026-07-10: **v0.19 — AP-021 logged (human-directed discovery).** Confidence label inconsistency found between §The Fallacy Checklist Item 7 (four labels, includes "Estimated") and §Evidence Classification and Institutional Truth Provenance Hierarchy (five labels, includes "Replicated"/"Simulated," no "Estimated"). Not yet resolved — resolution path specified but not executed this pass, pending human governing authority confirmation that the five-label system is the intended standard before the Fallacy Checklist text is edited. Open Unknowns 9 → 10.

- 2026-07-05 (second entry, same day): **v0.18 — Line 754 Gate 3 status
  re-corrected after regression.** This was already identified and fixed
  earlier the same session, but the copy this file's edits were being made
  from still carried the stale "BLOCKED pending AP-012 and AP-016" text —
  the earlier fix did not persist into the version uploaded for the CT-011
  pass, so v0.17 was shipped still carrying it. Now reads Resolved, with
  the AP-017 re-evaluation caveat, matching `Admin/Forge_Audit_Kit.md`'s
  already-correct v1.8 text. **Process note for human governing authority:**
  if edits are being made against local/live copies in parallel with copies
  uploaded here, worth confirming which is authoritative before each
  session's edits, or a fix can silently regress like this one did — not
  flagging blame, just the mechanism, since it's the same class of
  drift-via-desync this repository tracks everywhere else.

- 2026-07-05: **v0.17 — CT-011 resolved.** The Expiry Rule and Expiry check
  (§Unknowns Registry doctrine) now explicitly cross-reference
  `Admin/Canonical_Terms.md` §4's Cycle definition (one calendar year by
  default, operator-adjustable) rather than leaving "audit cycle" undefined.
  Prior text was silently read by multiple auditor agents as "each time the
  Skeptic/Auditor role opens," which inflated aging language well past real
  elapsed time — e.g., unknowns 62 and 17 days old were reported as "9
  cycles" and "3 cycles open" in a same-day dual audit of
  `Admin/Ethical_Constraints.md`. Expiry check text now distinguishes audit
  *pass* (can happen many times) from Cycle *threshold* (calendar-based,
  advances independently of how often the role opens). No change to the
  two-cycle threshold number itself, only to what a cycle means. Gate 3's
  "per promotion cycle" language (AP-017) is a distinct, narrower sense of
  cycle and is unaffected — already noted as such in Canonical_Terms.md's
  Cycle entry.

- 2026-05-04: **UNK-004 (Expiry Rule enforcement mechanism)** — Discharged. Sidecar Model addresses the underlying accumulation problem structurally.
- 2026-05-04: **UNK-022 (Full Stop Review trigger conditions)** — Resolved. Three specific trigger conditions and invocation record format added. Fourth trigger added at v0.6.
- 2026-05-19: **Gate 3 Adversarial Pass** — Upgraded from single-scenario requirement to full Adversarial Challenge Battery (ten classes).
- 2026-05-23: **Reconciliation pass** — v0.7 merges v0.6 depth with older draft's role class structure, 10-phase audit sequence, and evidence classification table. Abandoned Paths and Drift Indicators sections added per File_Template.md. Assumptions table added. Failure Modes reformatted to table.
- 2026-05-23: **AP-005 through AP-007 added** — verification termination threshold, institutional truth provenance hierarchy, and repository integrity doctrine lineage introduced from Forge_Audit_Kit.md v0.7 reconciliation.
- 2026-06-21: **v0.8 — Epistemic Foundation constitutional header inserted (EF-0.0 through EF-0.8b).** Multi-agent synthesis (Gemini, ChatGPT, Grok, Claude) across six sessions. EF-0.8b is a LazarusForgeV0-specific addition — closes the self-confirming simulation gap.
- 2026-06-21: **v0.8.1 — Dual audit pass (Gemini + Grok, Skeptic/Auditor).** AP-001 through AP-007 escalated to Systemic Risk (8-cycle expiry threshold exceeded). Three new unknowns logged: AP-008 (High), AP-009 (Low), AP-010 (Medium). Open Unknowns incremented 7 → 10. Gates cleared: G1, G2, G4, G5, G6. Gate blocked: G3.
- 2026-06-21: **v0.9 — AP Resolution Pass (Claude, Synthesizer/Auditor).** AP-006 closed — Payment via Specification. AP-007 moved to In Progress. AP-002 through AP-005 resolution paths updated. Open Unknowns decremented 10 → 9.
- 2026-06-21: **v0.10 — Active mandate pass (Claude + Gemini).** EF-0.2 Level 2 and Level 3 action text expanded. AP-009 closed. AP-001, AP-004, AP-005 moved to In Progress. Open Unknowns decremented 9 → 7.
- 2026-06-21: **v0.11 — Gemini adversarial pass integration.** AP-001 indicator set rolled back — premature metric naming removed. AP-011 logged (Medium, Major). Open Unknowns incremented 7 → 8.
- 2026-06-23: **v0.12 — RC governance stubs added to Unknowns Registry.** Priority Demotion Doctrine (RC-007), Inventory Calcification Check (RC-008), Vehicle Advancement Visibility (RC-009) integrated as body doctrine. Open Unknowns: 8 (no new AP entries).
- 2026-06-24: **v0.13 — Full Adversarial Challenge Battery complete.** Claude (Classes 1, 5, 6) + Gemini (Classes 3, 8, 9, 10) + Gemini prior pass (Classes 2, 4, 7). AP-012 through AP-020 logged (9 entries). Human Interaction Point Doctrine added to Governing Principles. EF-0.2 autonomous degradation amendment added. Failure Modes row added. Provenance Ceiling Self-Application Rule added. Gate 3: BLOCKED pending AP-012 and AP-016 reaching Provisional Spec. Open Unknowns: 8 → 15.
- 2026-06-24: **v0.14 — Full clean rewrite (Claude, Synthesizer/Auditor).** All v0.12 and v0.13 amendment blocks integrated into canonical body positions. Sidecar triage pass: AP-006 and AP-009 remain Resolved; AP-014 closed (Payment via Specification — Epistemic State Calibration Reference table added to Evidence Classification section); AP-015 discharged (Trajectory — v0→v1 transition item); AP-020 discharged (Trajectory — Golden Dataset deferred; AP-014 inline set sufficient for current scale); AP-012 and AP-016 reclassified In Progress → Vehicle (Human Interaction Point Doctrine constitutes doctrine layer; enforcement gap remains). Lessons Learned row added for AP-001 indicator rollback. Gate 3 status note added to Verification Gate Enforcement. Systemic Risk escalation status note updated. Open Unknowns decremented 15 → 12. Highest Risk updated to Critical (AP-012, AP-016).

---

