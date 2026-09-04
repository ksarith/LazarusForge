# Forge_Audit_Kit.md — Version History

Full changelog for `Admin/Forge_Audit_Kit.md`, relocated out of the
kit's own body as of v1.10 (2026-07-14). Newest entries first. Add new
entries here, not back into the kit.

As of v1.11 (2026-07-14) this file also houses the kit's own sidecar
(Auditor Notes & Unknowns) and Adversarial Battery record, relocated out
of the kit body for the same reason as the changelog itself — the kit
is a working, frequently-versioned document, and its self-tracking
content was accumulating alongside the reference content it exists to
keep lean (see FAK-005). This is a deliberate, documented exception to
the Resolved Unknown Discharge Procedure's general rule that sidecar
entries live in the owning file — the owning file's condensed-reference
purpose is the reason for the exception, not a reason to apply it
elsewhere. Every other file in the repository keeps its sidecar in-body.

────────────────────────────────────────────────────────────────────

## Sidecar — Auditor Notes & Unknowns

**FAK-001** — Kit version maintenance trigger not formally owned. Maintenance trigger defined in How to Use. Status: Open — formal ownership assignment still needed.

**FAK-004** — Index triage policy (critical watch list, adopted v1.1) was never formally ratified. **Resolved (v1.10, human-directed):** approach superseded rather than ratified. Pre-loading an auditor with expected findings before it reads the target file undermines independent verification (EF-0.1: precedent and consensus are disqualified as evidence) — this is the same failure mode as agent-convergence-without-verification, just at the checklist-design level instead of the finding level. Resolution: critical watch list removed from the pre-audit checklist; `Unknowns.md` cross-referencing moved to Post-Audit Cross-Reference, performed only after independent findings are drafted. Lessons Learned: a checklist step can itself introduce the bias an audit is supposed to catch — worth auditing the audit process, not just its outputs. Status: Resolved — Discharge via Lessons Learned.

**FAK-005** — Character-count reduction pass at v1.3 reached ~16,950 chars; EF condensed reference and Audit Opening Checklist were ruled load-bearing, not bloat. Growth since — Resolution Log narrative, Auditor Notes narrative, and especially the critical watch list (FAK-004) — brought the kit to 35,112 chars by v1.9. **v1.10 pass:** Resolution Log externalized here; FAK-* entries trimmed to this kit's own Discharge Procedure format; critical watch list removed (FAK-004). Post-reduction count: ~25,100 chars in-kit (28% reduction from v1.9's 35,112). **v1.11:** sidecar and battery record also relocated here — see intro above. Status: Open — the 12,000-char ceiling parameter itself still hasn't been revisited; ceiling flag remains active as a Drift Indicator on the kit body.

**FAK-006** — Resolved Unknown Discharge Procedure canonized here at v1.4 from organically-emerged RIP-001 practice; per this kit's own Scope Boundary, full procedural doctrine belongs in `Admin/Auditor_Protocols.md`. Status: Open — condensed version live in the kit; full-doctrine migration to `Admin/Auditor_Protocols.md` still pending.

**FAK-007** — Critical watch summary went stale against `Unknowns.md` twice (v4.0→v4.5, then v4.9→v4.10) before being refreshed each time; full incident below in Version History. Resolution: refreshed 2026-07-05. Lessons Learned: a hand-maintained duplicate of another file's registry will recur as a staleness source regardless of refresh diligence — structurally superseded by FAK-004/v1.10, which removes the duplicate mechanism rather than re-committing to keep refreshing it. Status: Resolved.

**FAK-008** — Cross-agent Gate 3/G6 scoring dispute on `Security_Protocols.md`: gate execution-quality and open-unknown blocking are separate, independently required axes (see kit's Verification Gates section). Resolution: logged as Synthesizer-level resolution in `Security_Protocols.md` Active Disputes, 2026-07-02. Status: Resolved.

**FAK-009** — Gate scope clarification (FAK-008) was drafted while `Verification_Gates.md` was unavailable, so it cited `Admin/Auditor_Protocols.md` directly instead of the correct intermediate canonical layer — first concrete incident evidence for VG-001. Resolution: citation corrected once the file became available; checked independently consistent, no actual divergence. Lessons Learned: a derived file can cite the wrong layer of its own derivation chain even when the content stays correct — citation path and content correctness are different failure modes and both need checking. Status: Open (VG-001 itself remains unresolved in `Verification_Gates.md`; the kit's citation is corrected).

**FAK-010** — AI Contribution Rules' role-declaration template cited `Auditor_Protocols.md v0.14` while File State's derivation line read v0.20 — a self-caught breach of the kit's own Maintenance Trigger and Drift Indicator, surfaced by a Claude self-audit 2026-07-14 that explicitly declined to assign this an ID and left it to human ratification. Resolution: corrected 2026-07-14, same session. Lessons Learned: the kit's own version-string maintenance is enforced by chance discovery during unrelated audits, not by any structural check — see also the Cycle/CURRENT_CYCLE finding in the Adversarial Battery record below, which is the same enforcement-gap pattern at a larger scale. Status: Resolved.

**FAK-011** — No End-of-Life doctrine existed for the kit itself, despite the kit's own Fallacy Checklist item 8 requiring one for "every module spec." Surfaced by the same 2026-07-14 self-audit. Resolution: End-of-Life doctrine added to How to Use, 2026-07-14 (human-directed) — superseding the kit is a normal lifecycle event; final version is shelved for posterity as a study artifact, not deleted. Status: Resolved.

**FAK-012** — No sidecar entry recorded Adversarial Battery ever being applied to the kit itself (G3), despite Adversarial Priority Weighting plausibly requiring Full Battery given the kit's high Coupling and Governance Authority (every audit session routes through it). Surfaced by the same 2026-07-14 self-audit. Resolution: Battery run 2026-07-14 — see Adversarial Battery record below. Status: Resolved — battery applied; see that record for its own findings, which remain separately open where noted.

**FAK-013** — Five citations inside `Admin/Forge_Audit_Kit.md` (Sidecar Link field plus four body references) still pointed to `Archive/Logs/Forge_Audit_Kit_Changelog.md`, the pre-v1.10 location, despite this file's own intro stating the sidecar and changelog were relocated to `Archive/Logs/` at v1.10 (2026-07-14). Flagged as out-of-scope by Grok during a `Tests/Solar_Descent.md` audit, 2026-07-28 ("contains an unresolved reference... not escalated here"). Resolution: all five citations corrected to `Archive/Logs/Forge_Audit_Kit_Changelog.md`, 2026-07-28 (human-directed, in the same pass as the CIR-/GOV-008 rename below). Lessons Learned: a file can correctly document its own relocation in prose while its own self-citations still point at the old address — the intro note isn't self-enforcing. Status: Resolved.

**FAK-014** — Derivation citation to `Unknowns.md` went stale twice in the same way FAK-007 already documented once: v1.15 (2026-08-30) correctly refreshed the citation to the then-current v4.87, but `Unknowns.md` advanced to v4.93 on 2026-09-01 (GU-002 closure) — two days before a 2026-09-03 Grok audit that cleared Gates 5 and 6 without catching it. The kit's own Drift Indicators explicitly name this exact condition ("Derivation statement references a superseded version of... `Unknowns.md`"; "Expiry Watch not updated at `Unknowns.md` version increment") — both were live and untripped at audit time. Surfaced by Claude, source-verifying the Grok audit against `Unknowns.md`'s own header, 2026-09-03. Context: FAK-007's "Resolved" status assumed the problem was structurally fixed by removing the hand-maintained duplicate registry at v1.10 — this recurrence shows the *citation-currency* half of that problem (distinct from the duplicate-registry half) was never actually closed, just unobserved for seven version cycles. Separately, as of 2026-09-03 the kit is no longer being used in its original run-time-condensation role — audits are being performed by loading the full repository archive and prompting directly, bypassing the token-ceiling rationale (FAK-005) that justifies the kit's existence. Whether to formally retire the kit under its own End-of-Life doctrine, or keep it current as a reference despite reduced use, is a human decision — this entry doesn't presume one. Resolution: citation refreshed to `Unknowns.md` v4.93, 2026-09-03 (human-directed). Status: Open — citation corrected; the recurring-staleness pattern itself (citation currency has no structural check, same root cause FAK-010 already named) and the kit's ongoing role are both unresolved.

────────────────────────────────────────────────────────────────────

## Adversarial Battery Record

**2026-07-14 — First Battery application to `Forge_Audit_Kit.md` itself (FAK-012).** Applicable Red Teams selected by relevance — this is a governance/reference document, not a physical system, so Physics and Economic Red Teams were not applied. Auditor: Claude.

**Semantic Red Team:**
- The kit's existence as a condensed distillation of `Admin/Auditor_Protocols.md` is in structural tension with EF-0.1, which disqualifies agent consensus and precedent as evidence. An auditor who only ever loads the kit — which "How to Use" explicitly sanctions as the baseline for routine sessions — is relying on a secondary summary rather than independently verifying against primary source each time. "When this file contradicts a full source document, the full source document prevails" mitigates this for cases of detected conflict, but does nothing for cases where the kit is simply stale and nobody happens to load the source to notice (exactly what happened with the four separate staleness findings this session: Truth Provenance Labels, three derivation version strings, and the v0.14 role-declaration string). Not a defect to fix by editing text — a structural property of condensed references worth naming so it isn't mistaken for solved.

**Governance Red Team:**
- The kit grants itself binding block authority over Verification Gates without any structural mechanism ensuring its own gate table hasn't silently drifted from `Admin/Verification_Gates.md`. An auditor exercising a block based on the kit's wording is exercising real authority on a secondary source, with cross-check against the primary left entirely to auditor discretion.
- Self-amendment without external enforcement: the kit defines its own Discharge Procedure, Drift Indicators, and Maintenance Trigger, but nothing enforces compliance with them except a future auditor happening to notice — which is exactly how FAK-010 was caught this session, by chance, during an audit of the kit for an unrelated reason (Grok's `Governance_Charter.md` audit going wrong). A compliance mechanism that depends on incidental discovery is not a mechanism.

**Systems / Operational Red Team — MAJOR FINDING, confirmed against source, not hypothetical:**
`Admin/Canonical_Terms.md` §"Cycle (Governance / Audit Cycle)" ratifies Cycle = one calendar year by default (2026-07-05), and explicitly warns: *"'Audit cycles' here means Cycle — one calendar year by default, not one audit pass."* CT-011 (Resolved 2026-07-05) propagated this definition into `Admin/Auditor_Protocols.md`'s prose, and its own Resolution field explicitly states the broader sweep was never finished: *"the broader grep this entry called for... has not been performed yet; `Admin/Forge_Audit_Kit.md`'s Expiry Watch summaries specifically are still unchecked."* `AUDIT_HARNESS.py`'s own code was never checked either.

That check has now been run. `AUDIT_HARNESS.py` line 368: `CURRENT_CYCLE = 10   # ← update this each session` — incremented per session, not per calendar year. The repository is roughly 2.5 months old (earliest dated content 2026-05-07); ten "cycles" in that span is roughly one every one to two weeks. `EXPIRY_THRESHOLD = 2` therefore currently flags an unknown as overdue after roughly two to four weeks of session-based aging — not the ratified two-year default. GOV-001 through GOV-010 being reported as "at or past threshold" (Grok's audit, this session) is arithmetically consistent with the harness's own data, but the threshold it's consistent with is not the one `Canonical_Terms.md` ratifies. The kit's own Drift Indicators list already names this exact risk ("'Cycle'... conflated with 'audit pass'... see CT-011") — the indicator existed; nothing had actually walked it against the harness's executable code until this pass. Per CT-011's own instruction ("log a new entry rather than reopening this one"), this is flagged here for a new `Canonical_Terms.md` entry rather than resolved unilaterally — whether `CURRENT_CYCLE` should be redefined to track calendar time, `EXPIRY_THRESHOLD` recalibrated, or the harness variable renamed to something that doesn't collide with the ratified term (e.g. `CURRENT_SESSION`) is a governance call, not a mechanical fix.
- Separately: no documented fallback if `Forge_Audit_Kit.md` itself is unavailable mid-session (fetch failure, accidental deletion). The harness has graceful-degradation patterns for other fetch failures; the kit has none for itself.
- Separately: nothing structurally guarantees an auditor is using the current version of the kit rather than a stale cached copy from earlier in a long session — the exact failure class both Grok's `Governance_Charter.md` audit and FAK-010 fell into, from two different directions, in this same session.

**Malicious Actor Red Team:**
- The v1.10 Expiry Watch redesign (FAK-004) removes pre-loaded bias correctly, but introduces a trust-then-verify ordering: independent findings are drafted from the target file's own sidecar before Post-Audit Cross-Reference checks the file against `Unknowns.md`. A target file with an incomplete or manipulated sidecar would pass the file-scoped phase cleanly, with the gap only caught if Post-Audit Cross-Reference is actually performed with the same rigor as the main audit. Not a reason to reverse FAK-004 — pre-loading bias is the worse failure mode — but a reason Post-Audit Cross-Reference shouldn't be treated as optional or perfunctory.

**Synthesis:** One finding (Cycle/CURRENT_CYCLE) is severe and actionable, with a clear evidence chain back to CT-011's own deferred scope — recommend logging as a new `Canonical_Terms.md` entry. The Semantic and Governance Red Team findings describe structural properties of condensed/self-amending references rather than one-off defects — worth naming in doctrine (e.g. as a standing Drift Indicator or Fallacy Checklist note) rather than chasing as individual fixes. The Malicious Actor finding is a design tradeoff already made correctly (FAK-004), not a regression to undo.

────────────────────────────────────────────────────────────────────

## Version History

- 2026-08-30: **v1.15 — Derivation refresh, three versions stale.**
  `Admin/Auditor_Protocols.md` had drifted from v0.24 (this kit's citation)
  to v0.41 (actual current) — roughly 17 versions and five weeks of
  unreflected governance work, including AP-033 and AP-035. `Unknowns.md`
  had drifted from v4.21 to v4.87 — 66 versions. `Admin/Verification_Gates.md`
  checked and found unchanged at v0.7, no action needed there. Beyond the
  version strings themselves, checked AI Contribution Rules against the
  source's current rule list and found a real content gap, not just
  citation staleness: the kit only carried Rules 1–8; Rule 9 (AP-033,
  Resolution Claims Require Governance Access — no contribution may imply
  an unknown has advanced toward Resolved without confirmed sidecar
  access) and Rule 10 (AP-035, External Pseudo-Audit Scope and Logging
  Destination — pseudo-audits may not fabricate inventory claims, invent
  local ID prefixes, or generate a freestanding ledger as primary record)
  had been added to the source since v0.24 and never propagated here.
  Condensed versions of both added. Token ceiling note (`Admin/Auditor_Protocols.md`
  character count) updated from the stale v0.24 measurement (~157,000
  chars) to a fresh v0.41 measurement (~146,700 chars) — smaller despite
  more doctrine, since intervening passes trimmed duplicated version-history
  narrative elsewhere in that file while adding real rule content. Role
  declaration example string updated to cite v0.41. Open Unknowns count
  (5: FAK-001, FAK-005, FAK-006, FAK-009, plus the Cycle/CURRENT_CYCLE
  finding flagged for `Canonical_Terms.md`) checked against this file's
  own sidecar below and confirmed still accurate — no change needed there.
  Checked and left alone: this kit's own character count (23,727) remains
  well over its own 12,000 Drift Indicator ceiling — pre-existing, tracked
  as FAK-005 (Open since v1.3, ceiling parameter itself never revisited),
  not newly introduced by this pass and out of scope for a version-derivation
  refresh specifically. Prompted directly by the human governing authority
  after noticing prior agents have been inconsistent about keeping
  changelogs current alongside source-file edits generally — this kit's
  own derivation lag is itself a clean instance of exactly that pattern,
  caught only because it was checked directly against source rather than
  assumed current from its own header.

- 2026-07-28: **v1.14 — Governance Sidecar ID Reference gained a `CIR-`
  row** (`Admin/Computational Institutional Reasoning`), registered as
  part of renaming that file's colliding local "GOV-008" tracker to
  CIR-001 (see that file's own Resolution Log). FAK-013 also resolved
  in this pass — five stale `Archive/Logs/Forge_Audit_Kit_Changelog.md`
  citations corrected to this file's actual `Archive/Logs/` location.

- 2026-07-26: **v1.13 — Governing Principles gained a fifth line**
  ("Correct a flawed premise only when it threatens the task's outcome
  — not for its own sake"), naming explicitly what the existing
  "infinite audit recursion is a governance failure mode" line already
  gestured at without stating as a standalone principle. Sourced from
  a cross-agent (Grok/Gemini/ChatGPT) prompt-design discussion the human governing authority
  brought over from r/InnovativeAIChats; adapted rather than adopted
  wholesale — the same discussion's larger proposal (a four-tag
  evidence-provenance scheme) was declined for `Admin/Auditor_Protocols.md`
  as a fifth parallel vocabulary alongside Evidence Classification,
  EF-0.0's VERIFIED/PROVISIONAL/UNKNOWN, AP-024's H0–H5, and Forge_Net's
  DV-002 evidence_type enum — see that file's v0.29 Resolution Log.

- 2026-07-17: **v1.12 — Verification Gates section trimmed (Fallacy 5,
  flagged 2026-07-16, three turns outstanding).** Two of three dated
  paragraphs collapsed to a compact standing rule; full history preserved
  here rather than deleted.

  *Known source ambiguity (full text, removed from kit body):*
  `Admin/Auditor_Protocols.md`'s own Gate 3 status entry stated Gate 3
  "BLOCKED pending AP-012 and AP-016" in the same line as "Battery
  application is complete" — correct in substance (coverage complete,
  promotion blocked) but the phrasing blended the two axes this kit's
  Gate scope vs. promotion readiness note separates. Flagged as a
  legibility issue worth a wording pass, not a governance error. By
  2026-07-17 this was doubly stale: AP-012 and AP-016 have been Resolved
  since 2026-07-03, and `Admin/Auditor_Protocols.md` has moved through
  v0.17 → v0.24 since this note was written — the specific phrasing it
  described may no longer exist in the source at all. Removed rather
  than updated, since re-verifying decade-old phrasing against a since-
  heavily-revised file wasn't a good use of a trim pass; if the
  underlying legibility pattern recurs, it's now covered by the general
  "Gate 3 status is not permanent" rule that replaced this and the
  paragraph below.

  *Gate 3 note (full text, removed from kit body):* Battery coverage
  complete for `Admin/Auditor_Protocols.md` (v0.13). At least one Battery
  class per promotion cycle must be applied by an agent with no session
  context from the current audit cycle (AP-017). AP-012 and AP-016 — the
  two entries previously blocking promotion — are Resolved as of
  `Admin/Auditor_Protocols.md` v0.16 (2026-07-03, Payment via
  Specification). Gate 3 blocking status should be re-evaluated at next
  audit rather than assumed clear — a resolved blocker is not
  automatically a passed gate. The one durable principle in this
  paragraph (blockers can resolve without the gate itself having been
  re-checked) survives as the compact replacement rule; the v0.13/AP-012/
  AP-016-specific narrative around it does not need to keep being read by
  every future auditor of every future file this kit is used on.

  *Physical harness note: kept, not trimmed.* AP-010 is still Open as of
  2026-07-17 — this paragraph is a live, generally-applicable rule (Gate
  6 requires a test-harness cross-reference for documents with physical
  claims), not incident narrative, and doesn't share the other two
  paragraphs' problem of being tied to a specific resolved incident.

  Derivation versions also corrected while in this file: `Auditor_Protocols.md`
  v0.21 → v0.24, `Unknowns.md` v4.20 → v4.21 (both had drifted since this
  kit's 2026-07-14 Last Audit — three version bumps on the former, one on
  the latter, none previously caught).

────────────────────────────────────────────────────────────────────

- 2026-07-14: **v1.11 — Self-audit response + sidecar/battery relocation
  + First Battery.** A Claude self-audit of the v1.10 kit (source files
  unavailable that session, scope limited but honest about it — unlike
  the Grok audit of `Governance_Charter.md` earlier the same day)
  surfaced four real findings: a stale `v0.14` role-declaration string
  against a `v0.20` derivation (Finding 1); uneven reduction discipline
  in Verification Gates (Fallacy 5); no self-recorded Adversarial Battery
  application (G3); no End-of-Life doctrine for the kit itself despite
  the kit's own Fallacy Checklist item 8 requiring one (Fallacy 8). All
  four addressed: Finding 1 corrected; End-of-Life doctrine added to How
  to Use (human-directed — shelving for posterity as a study artifact,
  not deletion, on supersession); First Battery run against the kit
  (below); Verification Gates trim deferred, not yet done. Logged as
  FAK-010, FAK-011, FAK-012 respectively (FAK-010/011 Resolved same
  session; FAK-012 Resolved as "battery applied," its own findings
  tracked separately in the Battery record).

  Separately, human-directed: sidecar (Auditor Notes & Unknowns) and
  Adversarial Battery record relocated from the kit body into this file,
  extending the v1.10 rationale (working document, self-tracking content
  competing with reference content for the same space) one step further.
  Documented as a deliberate exception to the general in-body-sidecar
  rule, not a precedent for other files.

  The Battery's headline finding — `AUDIT_HARNESS.py`'s `CURRENT_CYCLE`
  incrementing per session against `Canonical_Terms.md`'s ratified
  one-calendar-year Cycle default — completes the sweep CT-011 explicitly
  left undone on 2026-07-05. Flagged for a new `Canonical_Terms.md` entry,
  not resolved here; see Battery record above for the full evidence chain.

────────────────────────────────────────────────────────────────────

- 2026-07-14: **v1.10 — Expiry Watch redesign (human-directed) + reduction
  pass + staleness correction.** Three changes, prompted by a Grok audit
  of `Governance_Charter.md` this session that inherited a stale DOC_STATUS
  assumption rather than checking the file's own File State table.

  *Expiry Watch redesign:* the "current critical watch" list (Audit
  Opening Checklist step 3) — a hand-curated duplicate of `Unknowns.md`'s
  Critical/Blocking table, refreshed piecemeal since v1.1 and the subject
  of FAK-004 (never formally ratified) and FAK-007 (went stale twice) —
  removed entirely. Rationale, human-directed: pre-loading an auditor with
  expected findings before it reads the target file undermines independent
  verification (EF-0.1 disqualifies precedent and consensus as evidence),
  and adds mental load pointed away from the file under audit. Expiry
  Watch is now file-scoped only — the target file's own sidecar, or the
  `AUDIT_HARNESS.py` boundary index if present. `Unknowns.md` registry
  cross-referencing moved to a new Post-Audit Cross-Reference section,
  performed only after independent findings are drafted from the file
  alone. FAK-004 and FAK-007 resolved as a consequence — the mechanism
  that could go stale no longer exists in the kit.

  *Reduction pass:* Resolution Log (this file's history, ~7,650 chars)
  externalized to `Archive/Logs/Forge_Audit_Kit_Changelog.md` — full history
  preserved verbatim below, add new entries there going forward, not back
  into the kit. Auditor Notes FAK-* entries trimmed to Status/Resolution/
  Lessons Learned per this kit's own Resolved Unknown Discharge Procedure
  (previously full incident narrative inline, much of it duplicating this
  Resolution Log's own entries for the same incidents — EF-0.5 applies to
  this kit same as any other document). Verification Gates section's
  process-note paragraph (2026-07-02 citation-routing incident, already
  covered by FAK-009 and the v1.6 entry below) removed from the kit,
  preserved here. FAK-005 updated with final character counts.

  *Staleness correction:* Truth Provenance Labels still listed the
  four-label system (Measured/Estimated/Analogous/Placeholder) retired by
  AP-021 on 2026-07-10 — corrected to the ratified five-label system
  (Measured/Replicated/Simulated/Analogous/Placeholder) with evidentiary
  thresholds. Verification Gates section gained a G2 evidentiary-backing
  note it had been missing since VG-002 activated the same day. Derived-
  from line corrected: `Auditor_Protocols.md` v0.18 → v0.20,
  `Verification_Gates.md` v0.4 → v0.7, `Unknowns.md` v4.10 → v4.20 —
  all three had drifted since this kit's 2026-07-05 Last Audit. A full
  content re-sync against everything that changed across those version
  gaps was not attempted this pass — flagged as separate follow-up work,
  not assumed complete.

────────────────────────────────────────────────────────────────────

- 2026-07-05: **v1.9 — FAK-007 Resolved: full critical watch refresh.**
  Derivation string corrected `Unknowns.md` v4.9 → v4.10 (a second
  staleness had accumulated since the 2026-07-02 fix) and
  `Admin/Auditor_Protocols.md` v0.16 → v0.18. Critical watch summary (Audit
  Opening Checklist step 3) rebuilt from live `Unknowns.md` v4.10 data
  rather than patched — added explicit note that this is a curated
  highlight, not the exhaustive Critical list, and pointed to
  `Unknowns.md`'s own cross-reference table for completeness rather than
  attempting to duplicate ~35 Critical entries here (consistent with
  FAK-005's character-ceiling constraint). GOV-011's 2026-07-05 resolution
  reflected, with an explicit flag that `Unknowns.md`'s own global index
  has not yet been updated to match — that sync is separate outstanding
  work. Surfaced and flagged inline, rather than silently perpetuated: the
  `EC-002` reference in the prior critical watch summary was ambiguous
  without a file qualifier — confirmed as an actual, already-occurred `EC-`
  prefix collision between `Ethical_Constraints.md` and `Economics.md`
  (five colliding IDs total), escalated as CT-007 in
  `Admin/Canonical_Terms.md` rather than resolved here (this file doesn't
  own that fix). Expiry Watch step text now cross-references
  `Admin/Canonical_Terms.md` §4's Cycle definition per CT-011, distinguishing
  audit pass from calendar cycle. New Drift Indicator added for
  cycle-vs-pass conflation.

- 2026-06-21: **v1.2** — Derivation string updated to `Admin/Auditor_Protocols.md` v0.8.1. Epistemic Foundation condensed reference added. Audit Opening Checklist restructured. AP-001–AP-007 Systemic Risk escalation added. Physical harness gate note added. Rule 8 added to AI Contribution Rules. Token ceiling note added.
- 2026-06-24: **v1.3** — Derivation strings updated to `Admin/Auditor_Protocols.md` v0.14 and `Unknowns.md` v4.0. Role declaration version string updated to v0.14. Human Interaction Point Doctrine added to Governing Principles. EF-0.2 L2 entry updated to reflect autonomous degradation doctrine. Active Unknowns section removed — replaced by critical watch summary integrated into Expiry Watch step. AP Systemic Risk escalation note updated: all seven entries carry resolution frameworks; AP-006 and AP-009 Resolved; AP-012 and AP-016 Critical. GH- prefix added to Governance Sidecar ID Reference. Operational Blocking / Epistemic Blocking added to Semantic Stability table. Gate 3 note updated with AP-017 independence requirement and current block status. AP-010 physical harness note updated. Token ceiling note updated to reflect v0.14 character count. FAK-005 remains Open — actual post-reduction count ~16,950; ceiling parameter needs revisiting, not the content. Reduction pass complete.
- 2026-06-27: **v1.3 patch** — Spec Gates (0/6) and Verification Ref (Admin/Verification_Gates.md) added to File State block. Phase 1 enforcement (AUDIT_HARNESS.py v11) flagged missing fields — all repository documents follow the same File State schema, no exceptions for meta documents.
- 2026-07-02: **v1.4** — Resolved Unknown Discharge Procedure section added, canonizing the RIP-001 pattern (permanent sidecar retention, Resolution + Lessons Learned narrative fields, matching top-table row, one-line Unknowns.md pointer — no centralized archive). Placed between Verification Gates and Sign-Off Format. Matching Drift Indicator added. FAK-006 logged — condensed version lives here per Scope Boundary; full doctrine migration to `Admin/Auditor_Protocols.md` still pending (file unavailable this session). Prompted by retroactive correction of RIP-004's discharge record, which had skipped the Lessons Learned narrative field and matching table row for six weeks despite being correctly resolved in substance.
- 2026-07-02: **v1.5** — Gate scope vs. promotion readiness clarification added to Verification Gates, sourced from `Admin/Auditor_Protocols.md` §Specification Promotion Rules and §Adversarial Audit Layer (file made available this session for the first time). Resolves the standing Grok/Gemini G3/G6 disagreement on `Admin/Security_Protocols.md`: gates test a document's own execution quality (check applied and documented, text non-contradictory); "open unknowns are non-blocking" is a separate, independently required promotion condition, not folded into G3 or G6. Flagged a legibility issue in the source: `Admin/Auditor_Protocols.md`'s own Gate 3 status entry blends "battery coverage complete" with "promotion blocked" in one line — correct in substance, ambiguous in phrasing. Gate 3 note rewritten to separate the two explicitly. `Unknowns.md` derivation string corrected from stale v4.0 to v4.5 (three missed maintenance-trigger updates). New Drift Indicator added for gate/promotion-status conflation. FAK-007 logged — critical watch summary still needs a full refresh against v4.0→v4.5 changes, not done this session. FAK-008 logged — dispute resolution recorded as Synthesizer-level, reversible, cross-referenced into `Admin/Security_Protocols.md` Active Disputes per `Admin/Auditor_Protocols.md` §Dispute Handling Protocol.
- 2026-07-02: **v1.6** — `Admin/Verification_Gates.md` reconciliation.
  Derivation line corrected to include it (was citing `Auditor_Protocols.md`
  only, skipping the intermediate canonical layer this kit's gate table is
  actually derived from). Gate scope vs. promotion readiness note's citation
  corrected to route through Verification_Gates.md §Gate 3/§Gate 6/
  §Promotion Requirements Summary; checked against it and confirmed
  independently consistent — no actual divergence, wrong citation path only.
  FAK-009 logged as the first concrete incident evidence for VG-001 (open
  since 2026-05-29, previously hypothetical risk). VG-001 remains Open —
  see Verification_Gates.md Resolution Log for the full record.
- 2026-07-02: **v1.7** — Derivation line was stale within the same session
  that fixed it: v1.6 cited `Verification_Gates.md v0.2` after that file
  had already been bumped to v0.3 in the same pass, and still cited
  `Unknowns.md v4.5` after Unknowns.md had moved to v4.6 then v4.7. Both
  corrected. Caught via a user-initiated live-repo check (Grok retrieval of
  File State fields across five files) following a file-management incident
  (accidental cloning, ~10% truncation of `Auditor_Protocols.md`, five
  duplicate `Unknowns.md` versions consolidated back to one). Check found
  no content loss — `Unknowns.md` confirmed v4.7, this file confirmed v1.6,
  `Security_Protocols.md` Open Unknowns confirmed at 12 (only possible if
  the SEC-007a/b split edit persisted) — but did catch this kit's own
  derivation-citation drift, a same-session recurrence of the exact pattern
  VG-001 and FAK-007 describe. Note: this check verified File State header
  fields only, not full body content (SEC-DS-001, EDL registry, RIP-004
  Lessons Learned fields, Discovery.md Objectives section unconfirmed by
  this pass).
- 2026-07-03: **v1.8** — Derivation line updated (`Auditor_Protocols.md`
  v0.14 → v0.16, `Verification_Gates.md` v0.3 → v0.4, `Unknowns.md`
  v4.7 → v4.9). Gate 3 note corrected: AP-012 and AP-016 Resolved as of
  `Auditor_Protocols.md` v0.16 (2026-07-03, Payment via Specification,
  full multi-agent specification text verified against original blocking
  conditions) — was still citing them as blocking. Critical watch summary
  partially corrected for the same reason (AP-012/AP-016 removed, RIP-001
  and SEC-007 updated to current split/resolved state); full v4.0→v4.9
  refresh still not done, FAK-007 remains open.
