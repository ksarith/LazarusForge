# Progress_Log_Changelog.md — Full History for Admin/Progress_Log.md

Split out 2026-08-09, following the precedent already established by `Unknowns_Changelog.md`, `AUDIT_HARNESS_CHANGELOG.md`, and `Forge_Audit_Kit_Changelog.md`. `Progress_Log.md` keeps the five most recent entries in full; this file holds every entry that's rotated out. No information is removed when an entry rotates — every entry below is preserved verbatim from `Progress_Log.md` at the time it moved.

---
### 2026-10-06 — First real CAP-meta-stale-01 and AVE runs filed: five new Field_Logs, run card metric bug caught and fixed, Routing.md triplication bug caught and fixed
*(Rotated 2026-10-09 during the protocol audit-runs entry.)*
The evidence drought named repeatedly over the past two days broke: five new entries filed under
`Tests/Field_Logs/` — `FL-20261006-cap-meta-stale-01.md` (Full Admin, Routing.md header-lag seed,
7/8), `FL-20261006-cap-meta-stale-01-reduced.md` (Reduced, withheld RIP+Operational_Conventions,
no stage 1-7 loss), `FL-20261006-cap-meta-stale-02.md` (Full, second real seed — Tst_Scope_Map's
stale "Field_Logs still empty" claim), `FL-20261006-cap-meta-stale-03-secondary.md` (stronger
ablation — withheld the Field_Logs Index itself, correctly fails at stage 2), and
`FL-20261006-ave-sample-01.md` (first AVE batch, 24 scored events, 21/24 = 0.875 source-survival,
thresholds explicitly kept Placeholder per the schema's own R1/R3 rules). Total: six real entries
now exist, up from one.

**Verified before accepting, not taken on the delivery summary:** both seed faults checked against
the actual pre-edit live state — `Routing.md` line 3 really did say "Last updated: 2026-09-30"
while the map body already listed later paths; `Tests/Tst_Scope_Map.md` really did say Field_Logs
"is still empty as of this build." AVE arithmetic (21/24) confirmed correct.

**Two real bugs caught in review, both fixed:**
1. **Routing.md registration triplication.** Each of the five new files had been registered
   three times (the header catch-up note duplicated across three insertion points), not once.
   Caught by grep count, not by eye. Rebuilt cleanly from the live baseline: header fixed once,
   each file's table row added exactly once. Final state: each filename appears twice total (one
   table row + one mention in the header's own prose summary) — confirmed correct, not residual
   duplication.
2. **RUN_CARD-CAP-meta-stale-01.md's own metric design flaw**, caught through actual use: the
   original card scored stage 8 (an ablation-only assessment) as part of the same /8 ordinal as
   operational stages 1-7, which let "Reduced 8/8" read as outperforming "Full 7/8" when the two
   aren't comparable — Full correctly marks stage 8 N/A. Card corrected to an operational grade
   (/7) plus a separate stage-8 ablation assessment table, with an explicit warning against mixing
   them. This is exactly the kind of flaw a real pilot run is supposed to surface, and it worked.

**One inconsistency flagged, not silently fixed:** `FL-20261006-cap-meta-stale-01-reduced.md`'s own
headline still reads "Stages passed (consecutive): 8/8" — the pre-correction framing the card fix
was specifically written to prevent. Left as-is rather than rewritten, since it's the actual
historical record of what was submitted under the card's prior version, and its `Status:
Unreviewed` field is precisely the mechanism meant to catch this before anything gets folded into
doctrine — exactly the Status-ownership discipline this file's own restructure established.

**Supporting doctrine touches, all verified clean:** `Admin/Experiments.md` — new boundary note
clarifying it covers physical-grounding falsification only, process/capability work lives in
`Tests/Field_Logs/`, so empty rows there don't imply no Forge experiments exist anywhere.
`Discovery.md` and `Tests/Tst_Scope_Map.md` — both corrected current-state claims about Field_Logs'
emptiness with proper dated parenthetical clarifications, original 2026-08-08 history preserved
verbatim rather than rewritten. `Tests/Admin_Governance_Teardown_POC.md` — one small status line
marking the Future experiment section "partially exercised," explicitly not claiming the
measurement program is complete; still no Capability ladder or self-model diagram added, per the
2026-10-04 decision. `Tests/Field_Logs.md` — five new Index rows, five new Resolution Log entries,
clean, no duplication.

All six Field_Log entries remain `Status: Unreviewed` — none folded into doctrine yet, no Unknown
closed, no Admin file retiered. Human-directed ("Please proceed" / "Please continue").

---
### 2026-10-04 (seventh entry, same day) — `RUN_CARD-CAP-meta-stale-01.md` added: stage-ladder run card for the POC's "Future experiment"
*(Rotated 2026-10-09 during the conduct-protocol ratification entry.)*
ChatGPT proposed a wider capability-grading methodology (claim-grade, checklist score, stage
ladder, rubric, ablation delta, minimum-viable-set — methods A through H) and, separately, a
"mature future self-model" sketch (capability ledger under constraints, rewritten only by
experiment evidence). Grok and ChatGPT converged on the same restraint already established last
entry: the methodology discussion and the future-self-model sketch stay conceptual, not filed as
doctrine — and correctly, neither touched `Tests/Admin_Governance_Teardown_POC.md` at all. What
was actually drafted and checked: `Tests/Field_Logs/RUN_CARD-CAP-meta-stale-01.md`, a concrete
run card operationalizing the POC's own "Future experiment (not scheduled)" section — Method C
(stage ladder, 1-8, stop at first failure) with an optional Method G ablation (Full vs. Reduced
config, Δ). Verified before merging: the card's EF-0.0 citation ("do not promote UNKNOWN→VERIFIED
without empirical grounding") checked directly against `Admin/Auditor_Protocols.md` — confirmed
real, the Epistemic Anchor / Axiom Zero clause. Card correctly cross-references the POC's Future
experiment section by name rather than restating it, carries its own Explicit non-claims
("does not close FAK-* items, rewrite Routing counts as doctrine, or prove Admin Tier
assignments — measures this skill under a named config"), and ends with an explicit guardrail:
"Do not bulk-retier Admin files from a single run." `Tests/Field_Logs.md` updated in the same
pass — new row in Ready-to-Run Cards, and "the four tracks" corrected to "tracks" now that a
fifth card exists (caught, not just copied forward). Registered in `Routing.md`. No file touched:
`Admin_Governance_Teardown_POC.md`, `Admin/Adm_Scope_Map.md`. This is the first concrete artifact
produced by two days of capability-framing discussion — still zero runs filed against it.
Human-directed.

---
### 2026-10-04 (fifth entry, same day) — `Admin_Governance_Teardown_POC.md` integration pass (deferral costs, GMP seam, disposition options, recompute rule)
*(Rotated 2026-10-07 MAQT packet draft.)*

---
### 2026-10-03 (ninth entry, same day) — `Field_Logs.md` restructured: index + per-entry files under new `Tests/Field_Logs/`
*(Rotated out of Current Lessons 2026-10-04 during POC integration pass.)*

---
### 2026-10-03 (eighth entry, same day) — LE-0 build-out in `Tests/Leviathan_testing.md` §VIII
*(Rotated out of Current Lessons 2026-10-04 during Admin load-bearing map pass.)*
Expanded LE-0 into countable bench/tank procedure (phases 0–5, evidence schema, result note). Status/Spec Gates/Open Unknowns unchanged. Human-directed.

---
### 2026-10-03 (third entry, same day) — `Admin/Operational_Conventions.md` Convention 8 added: rotation rules don't self-enforce
*(Rotated out of Current Lessons 2026-10-03 during LE-0 build-out pass.)*
Direct follow-on to the two rotation fixes above. The failure pattern (a file states "keep
only N most recent / current version, rotate the rest" and the rule goes unenforced until
someone counts) was checked against `Operational_Conventions.md`'s existing eight — sorry,
seven — conventions and found to have no entry, despite now being independently confirmed
on two files in one session and on `Unknowns.md` alone a second time (2026-09-10 precedent
already in its own changelog). New Convention 8 filed: states the pattern, cites both
2026-10-03 violations plus the 2026-09-10 precedent as evidence it's recurring rather than
one-off, and adds an explicit checklist line — count entries against the stated limit and
rotate in the same session, not as a follow-up — for the next time either file gets a new
dated/versioned entry. File State `Last Audit` updated. No existing convention altered.
Human-prompted (direct question after the two fixes), Claude-executed.

---
### 2026-10-02 (second entry, same day) — Consistency sweep Pass 2 reviewed; two confirmed fixes applied, one finding found mischaracterized on direct check
*(Rotated out of Current Lessons 2026-10-03 during staleness/confusion sweep correction pass.)*
Three specific claims checked against source before acting, same discipline as Pass 1's
review. **Confirmed and fixed:** (1) `Architecture/Forge_flow.md`'s File State claimed
`Open Unknowns: 7`; direct tally of its own FL- sidecars found only 6 genuinely open/in-
progress (FL-001–006), with FL-007 through FL-013 all explicitly marked Resolved —
corrected to 6 in that file directly, with the correction reasoning noted inline. (2)
`Unknowns.md`'s AS-001 row showed Priority (Promo) = "Medium," which turned out to match
`Operations/Air_Scrubber.md`'s AS-001 sidecar `Risk` field, not its `Priority` field
(Major) — corrected to "Major" in `Unknowns.md` (v5.57). Narrow fix only, matching the same
restraint as the LT-004/005 and v5.56 corrections: does not decide or normalize the
column's broader semantics (Blocking-status vs. Priority-level vs., now confirmed, Risk-
level values all appearing in the same column across different rows) — that design
decision remains open. **Checked and found not real:** a claimed CF-001 "ownership
ambiguity" between `Operations/Electronics.md` and `Architecture/Cognitive_Frameworks.md`
— both sidecars exist as claimed, but `Cognitive_Frameworks.md`'s own copy has an `Owner`
field explicitly stating `Operations/Electronics.md`, resolving the question within the
entry itself; not drift, an intentional mirrored copy. No action taken. Human-directed
(sweep commissioned by human; each finding independently re-verified before correction).

---
### 2026-10-02 — Grok's repository-wide consistency sweep reviewed; one confirmed fix applied, several findings found mischaracterized on direct check
*(Rotated out of Current Lessons 2026-10-03 during Convention 8 attribution + FAK-017 pass.)*
An independent agent ran a broader consistency sweep (Unknowns.md Active Index vs owning-
file sidecars, File State blocks, counts) after the LT-004/005 fix. Each claim checked
against source before acting, per standing discipline — roughly half held up, half did not.
**Confirmed and fixed:** `Admin/Progress_Log.md`'s own File State `Last Reviewed` field was
stale (2026-09-24) despite three 2026-10-01 dated entries already present in the file;
corrected to 2026-10-02, noted as a metadata-only fix (content/rotation discipline was
already current). **Confirmed, already on record:** `Admin/Auditor_Protocols.md`'s
Open-Unknowns count-note re: UNK-003 — matches existing 2026-09-29 Last Audit text exactly,
not a new finding. **Not confirmed — checked directly and found to be mischaracterized:**
(1) EV-001/TS-001-003/FL-001 "Priority mapping mismatches" called "same class as the
recent LT-004/005 fix" — checked each owning-file sidecar directly; all three show
`Blocking: Yes`, matching `Unknowns.md`'s "Blocking" entries exactly. Unlike LT-004/005,
nothing here contradicts its source — this is evidence of the vocabulary-mixing pattern
noted separately, not an instance of wrong data, and does not need the same kind of fix.
(2) Governance_Charter.md's claimed "13 vs ~14, possible off-by-one" — counted directly:
exactly 13 GOV-* rows owned by that file in `Unknowns.md`, all Open/In Progress, matching
the file's own stated count exactly. No discrepancy found. (3) A flagged "residual GOV-005
text" outside the table — located at `Unknowns.md` line 81; it's inside a clearly labeled
`## Dependency Clusters` section (an intentional, explicitly-scoped-down dependency-tree
diagram), not stray or orphaned content. **Confirmed real, not yet acted on:** the
`Unknowns.md` "Priority (Promo)" column genuinely mixes Blocking-status words, Priority-
level words, and occasional Risk-like terms across different rows — a real systemic
observation with likely dozens of affected rows beyond the ones sampled this pass. Not
normalized in this session: choosing a single semantic for that column and remapping the
whole Active Index is a real design decision, not a mechanical correction like LT-004/005
or this entry's Progress_Log fix, and doing it without that decision being made explicitly
risks introducing new errors across entries not individually re-verified here. Left open
for explicit direction. Human-directed (sweep commissioned by human; review and correction
self-directed against the sweep's own findings).

---
## Forward Growth Avenues (2026-08-21) — ARCHIVED 2026-09-21

Superseded by the 2026-09-21 three-lane version in `Admin/Progress_Log.md`. Full text preserved here per the file's own rotation rule.

**Standing directive from the human governing authority (2026-08-21):** prioritize unknown closure that does not depend on real-world/hardware tests — infrastructure is the current limiting factor, and work should not be queued against it.

**Lane taxonomy (2026-08-21):**
- A — Spec draft (Payment-via-Specification depth possible without new hardware)
- B — Human decision (Architecture / constitution; unilateral agent close forbidden or empty)
- C — Evidence (Needs Field_Logs, hardware, or multi-agent run)
- D — Dependency-blocked (Upstream unknown must move first)
- E — Exploration hold / no fast path

**Lane A verified 2026-08-30 candidates:** GMP-011 (In Progress, refinement), GMP-012 (Open, Minor), GMP-013 (split spec/Automation), CLF-011 (§4b contract — spec-payable, gate-side emit/read is not). **Resolved during campaign:** GMP-010 (2026-08-30), GI-004/GI-006 (2026-08-31), GMP-006 (2026-08-31), GU-002 (2026-09-01). **Reclassified out of Lane A:** GMP-007 (Lane D — dependency GMP-006), GMP-008 (Lane E — milestone-blocked on Trajectories v1), FL-002 (Lane D — blocked on GR-002), GR-001 (Lane C/D — hardware + GR-002). **Held / ineligible:** GMP-003, GMP-004, GMP-002. Full details in the original Progress_Log.md text for that period.

**Explicit non-work (2026-08-21 version):** Bulk pseudo-audits, closing GOV-021c/GOV-005 on prose, numeric thresholds without Field_Logs data, Spec Gate campaigns on empty Exploration files, reopening Resolved unknowns, treating agent summaries as source without sidecar verification.

---
### 2026-09-20 — EC-013 Plastics descent sequence filed as Proposed/Placeholder (Path A)
James directed Path A. Grok drafted and filed `Operations/Plastics.md` §EC-013 Descent Sequence: trigger (governance failure while pyrolysis/reactor active), ordered Layer-B steps (stop feed → preserve containment → managed heat-down → off-gas path continuity → purge when safe → isolation), explicit Layer-A hard overrides (Air_Scrubber fire-vent-halt wins), completion criteria, logging, non-goals. Marked Proposed/Placeholder; Blocking for hot runs retained; no EC-013 closure claimed. EC-013 tracker remains Open.

---
### 2026-09-20 — EC-013 Air_Scrubber descent sequence filed as Proposed/Placeholder (Path A)
Second per-process EC-013 implementation. `Operations/Air_Scrubber.md` §EC-013 Descent Sequence: trigger (governance failure while scrubber supporting a hazardous process), ordered Layer-B steps (signal upstream stop → preserve capture path → managed load reduction → sump/media check → ventilation mode decision under Layer A → isolation), Layer-A hard overrides (Fire Event → forced vent halt immediately; Fault 04; Thermal Fault; Acidic Ingress E-Stop). Fire-vent-halt as hard override of any graceful airflow step. `Unknowns.md` v5.48. EC-013 tracker remains Open.

---
### 2026-09-20 — `Tests/Multi_Agent_Quorum_Trial.md` §8 Preparation Package merged from Grok's standalone file
Grok produced a standalone with a §8 Preparation Package. Merged as §8: recommended defaults for all DECISION NEEDED items, fillable pre-trial worksheet, six concrete non-collusion probes, Field_Logs skeleton, minimal viable first-run configuration (logical-isolation-only permitted per §VII.1). Status unchanged: Proposed Protocol — Not Yet Run.

---
### 2026-09-18 — FL-006 half A: `Operations/Exception_Evidence.md` created as structural evidence-control owner for Oversight State
Grok analyzed the gap precisely: HP-011 Transition Ownership table's Oversight Operations cell has been blank since the table was first built, while Gates A-D all have named owners; the evidence types FL-006's own Resolution Path names (contamination, scarcity, substitutes, failure rates, dependency info) had no operational home. Three-pass process before anything was filed: Grok's initial owner proposal (new thin file, matching the FL-004/Tooling_Inventory precedent) was good architecturally but needed revision; ChatGPT's skeptical pass accepted the new-file direction but flagged four overreaches — file ≠ operator (the file is the control spec, not the maintainer), control spec ≠ warehouse (packet bodies live in the records the file points to), evidence ≠ decision (explicit anti-policy rule needed), and standing data should be distributed references not consolidated into one ledger; Grok revised incorporating all four; Claude source-verified the proposal against live text before filing. Created `Operations/Exception_Evidence.md` as the evidence-control specification and index: defines evidence classes, required fields (including "why deposited" as an observation, not a quasi-routing instruction — per ChatGPT's catch that "recommended Oversight attention" would silently become a decision channel), deposit rules, freshness expectations, and pointers to where authoritative records live — not a warehouse for the records themselves. HP-011's Oversight Operations cell updated to name the new file; FL-006 sidecar updated with the half-A resolution note. Half B (authority half / EC-003 / GOV-006 dependency) untouched. FL-006 remains Open — structural owner named, population and demonstrated maintenance still ahead.

---
### 2026-09-18 — §VII.2 (Bootstrap Quorum, GOV-008 candidate spec) amended: role rotation across quorum cycles added, limitations stated explicitly
Prompted by a ChatGPT multi-agent-readiness assessment of the three-physical-computer experiment `CONTRIBUTING.md` already names as the highest-value next contribution — verified accurate before engaging with it further (its GMP-004 cross-reference, "declarable, not achieved" framing, and §VII.8 registry schema all checked out against live text). James raised "floating roles" from that conversation, clarified as agents rotating which class they hold across cycles rather than within one. Worked through which version was intended before drafting anything: within-cycle role blending would collide with VII.2's existing per-cycle exclusivity rule and the Coupled-orchestration rule's independence bar; cross-cycle rotation does not. Filed as a scoped addition to §VII.2 with explicit limitations stated (doesn't satisfy Diversity/Independence tests, doesn't touch Hardware/Runtime Diversity, rotation-assignment authority left open as §VII.6 open item). No change to GOV-008's status. Human-directed.

---
### 2026-09-18 — EC-011 (human governance adversary model) problem statement filed
ChatGPT drafted the EC-011 problem statement as the natural next thread after GOV-006/GMP-004. Verified against live source before filing: EC-011 sidecar, SEC-ASM-006 wording, and the Human Override Doctrine's GOV-006/EC-011 boundary all checked out. Filed by updating EC-011's sidecar (Last Reviewed 2026-06-18→2026-09-18, problem statement added as new subsection, original text untouched) and Unknowns.md Active Index row. No adversary-model architecture proposed; EC-011 remains Open, Risk High, Priority Major.

---
### 2026-09-18 — EC-013 current-state note filed; Plastics.md descent section drafted but not yet filed pending ratification decision
EC-013 is a different shape from EC-011/EC-012 — not a silent assumption, but a live requirement (Governance Failure Modes, EC-004, ratified 2026-08-22) with zero per-process implementations in any Operations file. Grok pulled the current state and produced a gap matrix; ChatGPT drafted a Plastics.md descent section (spec-level, well-structured, carries explicit Blocking-for-hot-runs) and an Air_Scrubber interlock extract clarifying what's already specified vs what an EC-013 section would add. Verified all live claims against source before filing anything: Governance Failure Modes wording confirmed verbatim, Plastics.md confirms oxygen-exclusion/pyrolysis/scrubber coupling themes match the draft's scope, Air_Scrubber confirms Fault 04/thermal-divert/fire-vent-halt interlock rows exist as process-fault logic. Key distinction filed into the EC-013 sidecar: Layer A interlocks (always-on safety logic including fire → halt forced ventilation immediately) are not substitutes for Layer B governance-failure descent — descent must obey Layer A, especially the fire-vent-halt override. EC-013 sidecar updated (Last Reviewed 2026-07-05→2026-09-18, gap matrix and scope fences added); Unknowns.md Active Index row updated. Plastics.md descent section held — question is whether it follows the EL-006-P3-P5 placeholder pattern (file as Proposed, no full ratification ceremony) or the EC-012-escalation-rule pattern (drafted sidecar + independent Skeptic review + explicit Human Ratification before it takes operational effect), since it's a live addition to a process file rather than a governance sidecar note. Awaiting James's call before filing the operational content.

*(Rotated 2026-09-20 after Path A filing superseded the "awaiting decision" state.)*

---
### 2026-09-18 — `Tests/Multi_Agent_Quorum_Trial.md` created: concrete protocol for the three-computer quorum experiment
James asked directly whether test parameters for the three-physical-computer experiment belonged in a markdown in Tests/ — checked what already existed first rather than assuming a gap: `Tests/Field_Logs.md` is explicitly results-intake only (its own Scope Boundary says so), and while it and `CONTRIBUTING.md` both name the three-computer trial as the single highest-value contribution, neither defines how it's actually run — §VII has the abstract quorum criteria, ChatGPT's earlier multi-agent-readiness assessment had the operational gap list (machine baseline, Git authority, non-collusion testing, failure/recovery), but nothing tied them into a runnable protocol. Created `Tests/Multi_Agent_Quorum_Trial.md` to be that missing middle layer: machine/agent baseline table (Phase 0, cross-referenced against `Hardware_Diversity_Ladder.md`'s anti-spoofing criteria so the table can't quietly overstate diversity), role assignment including the just-added §VII.2 rotation clause (defaulting rotation-schedule authority to the human operator in advance, the safest option given §VII.6's own open item on that question), a hard main-branch-protection rule with promotion-chain topology, a required non-collusion probe per §VII.4, human-ratification constraints that explicitly inherit GMP-004's unresolved gap rather than papering over it, the nine failure/recovery scenarios as a fill-in table instead of prose, and pass/fail scoring against §VII.3's actual five-item checklist rather than an informal impression. Explicitly scoped as operationalizing §VII, not amending it — no claim of GOV-008 progress. Indexed into `Tests/Tst_Scope_Map.md` as an addendum and cross-referenced from both `Tests/Field_Logs.md` and `CONTRIBUTING.md`'s three-computer descriptions, which had previously pointed only at each other with no actual protocol behind them.

---
### 2026-09-18 — GOV-007 Decision 5 (partial): instance boundary reframed via README's specified/demonstrated distinction
Continuing from Decision 1, James worked through G7 (instance boundary) out loud rather than handing over a ready answer, and landed on a real connection: `README.md`'s own Current Status section already treats "specified versus demonstrated" as load-bearing project-wide — verified verbatim ("An architectural specification is not evidence that the corresponding physical capability has been demonstrated"), with its capability table scoring governance/audit as Specified-in-active-use against physical gate validation as Incomplete. Applied to G7, that split reframes the instance-boundary question rather than closing it: a *specified* boundary (this repository, its Human Governing Authority, its doctrine, independent of site) is effectively settled now, while a *demonstrated* boundary isn't something to declare — it's earned gate-cycle by gate-cycle, starting with one real melt-down/re-fabrication as the smallest observable unit, with a separate, larger multi-computer multi-agent operational run as the threshold that would make governance work independently observable rather than attested by one person, mapping onto what Pathway 1/GOV-008's quorum actually requires anyway. What made this worth filing carefully rather than smoothing into a tidy answer: James named the reason for leaving it partial directly — agent intellect on a question like this will likely outpace one human's ability to close it alone, and asserting false completeness now would be theater, not governance. Filed as a Decision Record explicitly marked PARTIAL, not Resolved — G7 reads "partially reframed" in the sidecar and Active Index, and G2/G3 are noted as answerable against the specified boundary now rather than blocked waiting on the demonstrated one. GOV-007 stays In Progress/Active; two of five decisions now have real answers on record, three remain open.

---
### 2026-09-18 — GOV-007 Decision 1 ratified: Genesis Phase formally declared for this instance
James answered the first of GOV-007's five human decisions directly, resolving something the consolidation had left ambiguous rather than deciding it himself: whether the governance-drafting work of the last several passes counts as Genesis Phase activity, or whether the instance is still "outside" Genesis Phase pending physical equipment (his own framing: getting the racecar to the starting line vs. the race itself). Checked against the Charter's actual wording rather than taking the framing at face value: it uses two distinct terms that had been easy to conflate — "runtime session" (an individual agent working session, verified verbatim as the unit its Q-2 separation rules are written about) and "first operational run" (verified verbatim as tied to FA-001 and hot physical operations specifically). That distinction resolves the question cleanly: the governance work itself — this entire GOV-006 through GOV-007 arc, conducted by rotating agents under human ratification because multi-agent quorum doesn't structurally exist — is not a precursor to Genesis Phase, it is the literal process the doctrine describes. "First operational run" genuinely hasn't happened (FA-001 still Open), matching the racecar instinct, but that's a claim about exit-pathway timing, not about whether Genesis Phase has begun. Filed as a Decision Record inside GOV-007's sidecar, kept distinct from the surrounding analysis rather than blended into it, dated to project start (May 2026) rather than to this filing. G1 marked Resolved; G2-G5 and G7 remain open. No exit pathway selected, no Pathway 4 horizon set, no claim of exit — this only settles that the instance is in Genesis Phase, not that it has left it.

---
### 2026-09-18 — GMP-004 residual/fence language mirrored from GOV-006 for symmetry
Grok proposed mirroring the prior day's GOV-006 solo-operator residual and scope-fence work onto GMP-004, its ratification-authentication twin, rather than leaving the two unknowns in an asymmetric state. Verified against live source before filing: `Governance_Migration_Protocol.md`'s existing GMP-004 sidecar — the "highest-risk attack vector against the Tier 1 amendment process" framing and the RIP-001 GPG-signed release-tag precedent (key `B5690EEEBB952194`) — both confirmed accurate and left untouched, with the new residual/fence language added as its own subsection underneath rather than overwriting prior text. Same solo-operator condition-of-use note (second-human-confirmation path practically unavailable with no second operator live, reducing current coverage to cryptographic signature or dated external record), explicit scope fences against GOV-006 (distinct act, independently owned, no auto-resolution either direction) and GOV-019 (conflict arbitration, out of scope). Active Index row updated to match; Last Reviewed bumped 2026-06-05→2026-09-18. GOV-006 and GMP-004 are now both Open, parked on the same trigger (Security_Protocols.md reaching Provisional Spec, or GOV-007/GOV-008 resolving), and symmetrically state their own limits rather than one silently assuming the other is settled.

---
### 2026-09-18 — EC-012 (epistemic spoofing via hardware/firmware tampering) problem statement filed; completes the EC-011/EC-012 pair
ChatGPT drafted the EC-012 problem statement plus a practical recommendation that went further — a live procedural rule (unattested/anomalous High-Risk telemetry shall not be treated as authoritative; escalate to human consideration instead) alongside an honest-residual-risk framing (perfect prevention against a determined adversary with physical access isn't available; the doctrine's job is to make spoofing noisy and costly, not impossible). Grok explained the mechanism plainly (the spoofed-toolhead example: correct constraint logic fed a false premise never trips). Verified against live source before filing: the weapon/pump spoofing example, EC-008's own explicit non-resolution of EC-012, and the EC-001/EC-002 four-point-check framing all checked out, including correctly treating EC-001/EC-002 as Resolved unknowns whose doctrine text remains live and citable. Filed only the problem statement — load-bearing locations, covered-vs-not-covered split, open questions, scope fences against EC-011/EL-006-SEC-007b/EC-001-EC-002 — into EC-012's sidecar (Last Reviewed 2026-07-05→2026-09-18). Deliberately did not file the procedural escalation rule: unlike a problem statement, it's a live doctrine addition, and this repository's own precedent (EC-003/EC-009, EC-008, GMP-006-008) requires a drafted sidecar, independent Skeptic review, and explicit Human Ratification before any such rule takes effect — flagged as its own future stint rather than folded in here. EC-011 and EC-012 are now both Open and explicitly non-assumable, matching the permission-source/telemetry split the doctrine already draws elsewhere.

---
### 2026-09-17 — GOV-006 problem statement + solo-operator/scope-fence short pass filed; parked
Grok redirected from the parked SEC-007b work to GOV-006 (human override authenticity validation), naming it as the shared soft dependency every "human-ratified" claim in SEC-007b was leaning on. Claude produced the bounded Class B deliverable: exact gap stated (interim rule requires a corroborating artifact exist, not that it be checked — evidentiary, not preventive), the three interim mechanisms mapped against what they do/don't cover, and open design questions listed (solo-operator/GOV-007-GOV-008 interaction, verifier infinite-regress risk, GOV-019 conflict-arbitration boundary, GMP-004 relationship). A second short pass then tightened two of those threads: the solo-operator residual (with no second human live, the interim rule's second path — "second human operator confirmation" — is practically unavailable, so it currently reduces to the cryptographic-signature and dated-external-record paths only; verified against the Genesis Phase Protocol's own same-session self-authorization language, which matches) and explicit scope fences with GOV-019 (conflict arbitration, distinct question) and GMP-004 (ratification-authentication twin, independently owned, not auto-resolved by GOV-006). Enforcement is honestly recorded as retrospective/reputational — no live gate exists yet. GOV-006 remains Open, Priority Major; no body-text change to Governance_Charter.md, no Payment-via-Specification. Parked until Security_Protocols.md matures or bootstrap conditions (GOV-007/GOV-008) change. Cross-agent: Grok proposed and reviewed, Claude drafted and source-verified both passes, ChatGPT produced the solo-operator/scope-fence pass.

---
### 2026-09-14/15 — Gate terminology rename, EL-006↔SEC-007 review chain, and CF-006 resolution; a working research strategy adopted (not yet in Resolution_Methodology.md)
James asked for a workload analysis before committing to renaming "Gate" (four-way collision: operational Gate_01-07, Decision Gates A-D, Oversight Gate, Verification Gates 1-6) — 425 live-file occurrences found, ~90 more correctly excluded in Archive/. Agreed split: keep Gate_01-07 and Verification Gates, rename the other two to Decision Point A-D / Oversight State. Grok's rename (two tranches) was reviewed before acceptance, not merged blindly — current-doctrine text came back clean, but historical narrative had been renamed anachronistically in several places (Forge_flow.md's own Last Audit field, its Lessons Learned table, Progress_Log.md itself), the exact risk flagged before starting. Fixed in two passes (initial review + a full residual sweep), including a couple of Claude's own earlier text that had drifted inconsistent along the way.

Separately, a parallel Copilot→Grok→ChatGPT review chain on EL-006/SEC-007 firmware trust produced a real finding: `Security_Protocols.md` claimed nodes need "signature-verified bootstrap load per Electronics.md doctrine," but Electronics.md's own EL-006 defers signature verification to v1+ and specifies hash-only as v0. Registered as CF-006, logged not silently fixed. A v0 Logic-Zero Run Sheet was added as Proposed/Placeholder (inert — no hardware yet). The chain's own lean binding-principles draft was filed as a transcript rather than inserted, since it mostly restated boundaries the other two artifacts already enforced. An automated integrity-audit report (resumed after a week paused) independently caught Forge_Audit_Kit.md's citation drift recurring a fourth time (FAK-016) — first time that pattern was caught by an automated process rather than a human asking.

CF-006 was then resolved: Grok's provenance investigation (2026-05-26 abandoned dual-ownership path, no dated entry ever introducing signature verification as deliberate policy) plus an independently-found third line of evidence (the file's own Drift Indicators already named exactly this failure mode as a re-audit trigger) supported Option A — align Security_Protocols.md's language to the real v0 floor, name signature verification as the v1+/SEC-007b-contingent target. Ratified and applied, original problem text preserved per the FL-009 precedent. SEC-007b design-lineage research (TCG/DICE/RATS background) filed as a second transcript for whenever physical anchor design actually starts.

Worth naming as the session's own lesson: a research strategy for exactly this pattern (bounded stint → live tree first → external pattern mapped, not merged → one disposition → stop) was drafted by Grok, refined by ChatGPT, and adopted for working use — but deliberately *not* filed into `Resolution_Methodology.md` yet. Both reviewers and James agreed: run it for several stints first: a method extracted from demonstrated cases (which this genuinely was — CF-006, the transcript filings, and the parked TCG/DICE/RATS work all followed this shape before it was ever written down) is trustworthy in a way a method designed in the abstract isn't. Revisit once it has its own evidence of preventing the failure modes it claims to prevent.

---
### 2026-09-09/10 — Forge_flow.md's held proposals cleared out, three genuine structural bugs found along the way, and a self-inflicted changelog migration lapse caught only when asked directly
Continuing the multi-agent refinement campaign: HP-011 (transition ownership table, built from existing cross-references rather than invented) surfaced a real gap — Oversight has no assigned Operations or Admin owner at all, registered as FL-006 — and, while placing it, a stray Resolution-Path line in FL-005 that actually belonged to FL-004's topic. HP-013 (lifecycle loop) named a loop that already existed via Feedback and Gate_02's existing re-triage doctrine, pure framing, no new logic. HP-014 (terminal-state distinction) shipped with a self-caught correction — the first draft overstated Reduction itself as the terminal-for-recovery state; the file's own text elsewhere makes clear Purification is what actually reaches that endpoint.

Scoping FL-002 (Reduction↔Gate_04 envelope cross-validation) confirmed it's genuinely blocked on an unmade engineering decision (Reduction method not yet selected), but surfaced that the two *provisional placeholder* tables standing in for that validation had themselves drifted from each other — logged as GR-009/MG-009 rather than fixed, since fixing placeholders ahead of the real spec would be wasted precision. Placing MG-009 surfaced something bigger: `Gate_04_Separation_Mechanical.md` had its entire Resolution Log duplicated into two copies that had diverged into separate edit lineages after a 2026-06-08 filename rename, neither ever reconciled. Merged chronologically — and the first merge attempt itself landed in the wrong position, caught only by checking the canonical section order against three other already-fixed files before finalizing.

A Grok-scoped Gate B observation-data schema (with a genuinely thorough inter-operator bias-pattern analysis) turned out to duplicate work that already existed: `Gate_02_Triage.md`'s TIL v0 Log Specification. Extended it with only the fields the Secondary Test actually needs, rather than standing up a parallel format — the second time this session a good scoping question went unchecked by its own asker before drafting (the first was the Tooling_Inventory.md template gaps).

ChatGPT's review of the 2026-09-10 working tree raised one more real architectural ambiguity — Oversight's want/need evaluation can override an item that already passed Gate D's material-recovery determination via an unrelated judgment axis, and the text never says whether that's override authority or only timing authority — logged as FL-007 rather than resolved, since resolving it would mean deciding something about Oversight's authority that isn't settled yet.

Separately: metal-AM language added to `Gate_06_Fabrication.md` (WAAM/wire-arc DED as a natural extension of the qualified-wire path, plus a brief LPBF/bound-metal forward-looking note) after verifying the proposed insertion points against live text and confirming zero existing additive-manufacturing content anywhere in the fabrication files.

The lesson worth naming on its own: `Unknowns_Changelog.md` — this file's own sibling — had not been updated since 2026-09-03 (v4.94), while `Unknowns.md` accumulated 16 versions of un-rotated "Prior:" chains across the entire week described above, in direct violation of its own stated "keeps only the current version" rule. This is the same recurring bug class that file has caught and fixed on itself multiple times before (20 stacked at v4.84, 3 at v4.87) — and it recurred silently through this entire session's own work, introduced by this session's own edits, uncaught by any of the source-verification discipline applied to everything else, until James asked directly whether the changelog had been touched. Fixed by migrating all 16 versions and confirming no duplication either direction. Worth sitting with: verifying agent claims against source doesn't catch a maintenance rule quietly lapsing in one's own output — that needs a different kind of check, closer to "did I follow my own file's rules" than "is this claim true."

---
### 2026-09-08/09 — Two days of Forge_flow.md refinement across three external agents; every proposal verified against live source before adoption, several genuinely improved, one flagged as bigger than its own drafter's framing suggested
Following an unsolicited ChatGPT refinement proposal for `Architecture/Forge_flow.md`, this session ran a long sequence of held-proposal work (HP-001 through HP-016) rather than adopting any single agent's plan wholesale. Every proposal was checked against live text before acceptance, several with real findings along the way: a Grok GR-005/ASM-001 diff for the R0-R4 taxonomy rollout was missing one occurrence (ASM-006) its own diff hadn't caught; a drafted `Operations/Tooling_Inventory.md` skeleton was missing two File_Template.md-required sections (Lessons Learned, Active Disputes) even though the template's own Minimal Valid File Example includes both; and a Gate B "Secondary Test" (justified-effort evaluation) was correctly identified as genuinely new gate logic — not the rename/consolidation pattern every other same-day change followed — and applied with a deliberately stronger provisional warning than its own drafter proposed, per explicit human direction, plus a Blocking Unknown (FL-005) rather than a routine Open one.

A distinct thread proved as valuable as the file edits themselves: a human-raised design point that this repository is shared and forked across independent Forge builds, so no single deployment's real-world data — including the maintainer's own — should be treated as canonical. That principle was first applied as wording fixes, then (on reflection) formalized as a new Deployment Localization Doctrine in `Admin/Governance_Charter.md`, explicitly marked as ordinary doctrine rather than a Tier 1 Axiom, generalizing a Reference Deployment Context pattern that `Architecture/Facilities.md` had already originated independently. Neither file had previously cross-referenced the other despite solving the same problem.

The session closed with a risk-ranked, ChatGPT-authored roadmap (refined and sequenced by Grok) toward making the flow "a testable state-transition specification" — logged in full as HP-008 through HP-016 rather than actioned wholesale, with the lowest-risk slice (a Gate Decision Contracts table, explicit UNKNOWN transitions, a formal re-entry contract) implemented immediately and the two items flagged as genuine new logic (three-valued gate logic, a Split transition primitive) explicitly held pending real Gate B operational data. Worth naming: a follow-up Grok review of an integrity report, submitted after that implementation, still described the Gate Decision Contracts table as "ready to apply on request" — a live instance of the stale-base problem this log has recorded before, this time from the reviewing agent not knowing about work completed one turn earlier in the same session rather than from a stale file snapshot. Human-directed throughout; several turns had a specific "verify accuracy, don't apply automatically" instruction rather than a blanket approval.

---
### 2026-09-06 — Forge_Net Priority-1 surgical pass (Architecture audit); one claimed finding turned out fabricated
ChatGPT Architecture audit of `Architecture/Forge_Net.md` found G6 trust-model split (DV-003 claim confidence vs PA-002/§4 “trust score”), G2 transport overclaim, and File State/sidecar lag — all confirmed genuine against source. It also claimed a G5 Ethical Anchor path defect (`Ethical_Constraints.md` should read `Admin/Ethical_Constraints.md`) — checked against `Admin/File_Template.md` directly and found false; the canonical Ethical Anchor string has no `Admin/` prefix anywhere in the repository, and the field was already correct. Grok's Priority-1 pass initially applied the incorrect “fix” anyway; caught and reverted same day before finalizing. Genuine Priority-1 pass applied: §2.5.0 three-way taxonomy (claim confidence ≠ node reliability ≠ governance weight); PA-002 retargeted to node reliability; FN-004 transport rewritten as open classes; FN-001/FN-005 descriptions aligned with existing DV-/PA- specs; File State refreshed. Network Invariants / state model / conflict taxonomy deferred to a later Architecture expansion. Spec Gates remain 0/6. Human-directed.

---
### 2026-09-04 — A "nine files missing Spec Gates" finding, carried over from an earlier session as established fact, traced back to fabricated content and found to describe no real gap
While following up on the AUDIT_HARNESS_CHANGELOG.md content-corruption fix from earlier this session, checked the specific claim that had been repeated as a real, unresolved finding — that nine files (six Challenges/, two Tests/) lacked a Spec Gates field entirely, an early-cohort oversight flagged during the 2026-07-10 full-repository sweep. Comparing the corrupted passage against `Unknowns_Changelog.md`'s actual v4.16 entry showed they describe the same real registration event (same IDs, same date) but the corrupted version contained invented additions never present in the genuine record — "zero Ethical Anchor violations," "zero Routing.md gaps," and the Spec Gates claim among them. A live repository-wide check found no files currently missing Spec Gates in any form; the closest match (six Challenges/ Problem-Statement files with no Spec Gates table row) turned out to be a deliberate, already-reviewed subtype exemption confirmed via a real 2026-08-10 pseudo-audit on each file, just never listed in `Admin/File_Template.md`'s canonical exemption classes — now added as class 8. Worth naming plainly: fabricated content that closely mimics real IDs, dates, and phrasing from genuine history is harder to catch than an obviously-wrong claim, and repeating an unverified finding as established fact (which happened here, across two separate turns) compounds the same failure this session has otherwise been catching in other agents' audits.

---
### 2026-09-04 — Grok proposed a "unified" hygiene zip; two of its four fixes were genuine, but it was built from a stale pre-fix base and would have reverted three same-day corrections if merged wholesale
Grok submitted a zip with two genuinely new, verified-correct fixes: `Challenges/Cha_Scope_Map.md`'s CLF count (10→9, matching `Closed_Loop_Feedstock.md`'s own File State — only CLF-005/010 are Resolved) and RE-UNK count (5→6, matching `Return_To_Eden.md`'s already-registered RE-UNK-006 from 2026-08-30), plus a matching `Return_To_Eden.md` Last Audit update and a Routing.md/Discovery.md "hygiene refresh" date bump. But diffing the zip against the actual current working copy (rather than accepting it as the new base) showed it had started from an earlier snapshot — before this same session's Charter Highest Risk fix (High, not Critical), Auditor_Protocols G5 fix (5/6, not 4/6), Verification_Gates promotion (6/6, not 2/6), and the Integrity_Incident_Log.md row added to Discovery.md. Accepting the zip wholesale would have silently reintroduced all four already-fixed defects under the cover of an otherwise-legitimate hygiene pass. Fixed by diffing file-by-file against the correct current state and merging only the genuinely new, independently-verified content (the CLF/RTE count corrections) rather than adopting the submitted zip as-is. Worth naming as a variant of a lesson already on this page: a multi-agent contribution can be entirely well-intentioned and still be wrong in aggregate if built from a stale base — the fix isn't "trust less," it's "always diff against current state before merging, never against what the contributor assumed was current."

---
### 2026-09-03/04 — Full campaign of independent module audits (Grok, some ChatGPT) across eleven Admin/Automation files; source-verification caught a real defect in six of them that the audits themselves had missed
Following ChatGPT's proposed sequencing ("audit the auditors before the operational files" — Pass A: Auditor_Protocols/Forge_Audit_Kit/Verification_Gates/AUDIT_HARNESS.py; Pass B: Unknowns.md/RIP/Integrity_Incident_Log/GMP; Pass C: Charter/Security_Protocols/Ethical_Constraints verification), Grok and ChatGPT ran audits against all eleven files in that order. Every single audit was independently verified against live source before accepting any finding or recommendation — not just the flagged issues, but the audits' own passing claims. Five came back genuinely clean on verification (Verification_Gates, Auditor_Protocols self-audit, Integrity_Incident_Log, Security_Protocols verification, EC verification, RIP verification) — real confirmations, not rubber-stamps, each checked against specific counts, IDs, or cross-references rather than accepted on the auditor's authority.

Six turned up something real the audit itself missed, each a different failure class: **Forge_Audit_Kit.md** — derivation citation to `Unknowns.md` was stale (v4.87 vs live v4.93), tripping two of the kit's own named Drift Indicators that neither the audit nor the file's own Open Unknowns caught (logged FAK-014). **Automation/AUDIT_HARNESS_CHANGELOG.md** — ~45 lines of verbatim `Unknowns_Changelog.md` content sat under the wrong file's "Audit Trail" header, present since before this session in every archive checked; no clean copy existed to recover the genuine harness history from, so the gap was documented rather than invented. **Unknowns.md** — the "Pending Corrections" cluster (PC-001–006) sat in the Active Index with `Status: Resolved` and full descriptions, directly violating the file's own Size Management Rule 2, which the audit had specifically praised as "actively enforced" without noticing the six rows sitting right there. **Governance_Migration_Protocol.md** — GMP-002's own Description claimed the Charter's ownership table already listed GMP as owner; the live Charter table still names itself, directly contradicting this same file's own accurate Scope Boundary text a few lines away. **Governance_Charter.md** — the File State's "Highest Risk" field read "Critical," conflating GOV-005's actual `Risk: High` with its separate `Priority: Critical` field; a same-day sweep had fixed which ID the field cited but carried the conflation forward, and the audit repeated it as fact. **Ethical_Constraints.md** and **Repository_Integrity_Protocol.md** were also directly repaired this session (ChatGPT audits, REVISE/G6-BLOCKED, metadata-only findings) before their later clean re-verification.

Worth naming as the session's real lesson, distinct from any single finding: an audit that reads as thorough and cites real counts/IDs correctly can still repeat a false claim sitting in its own baseline material, because checking whether a document's *narrative* is internally consistent is a different operation from checking whether its *specific factual claims* hold against the thing it's citing — Forge_Audit_Kit's version number was real, just stale; GMP-002's ownership claim was well-formed prose, just false; the Charter's "Critical" was a real field value, just the wrong field. None of these were hallucinations in the sense of inventing something from nothing — they were correct-shaped claims that had drifted from or misread their own source, which is a harder class to catch by reading alone. Also worth naming: this is not a claim that Grok/ChatGPT's audits were low-quality — the header-level counts, IDs, and cross-references in all eleven audits were independently confirmed exact almost everywhere checked; the misses were narrow and specific, not systemic sloppiness.

---
### 2026-09-02 — Grok audited `Admin/Auditor_Protocols.md` against itself; found the governing document's own metadata had drifted from its body, and a deeper check found an undocumented version gap neither audit caught
Grok ran a full self-application audit of `Auditor_Protocols.md` — the file that defines this repository's audit discipline, audited against its own rules. Findings: the relocated-sidecar summary still listed AP-013, AP-005, AP-004, and AP-024 as open ("14 open") despite the File State header explicitly marking all four Resolved weeks earlier; the Version String Registry's own two mandatory citations (Role Declaration example, Observability sign-off template) were still at "v0.37" against a "v0.41" header; the Status block was five versions behind at "0.36"; and the Sidecar SHA-256 hash predated four Closure Events that had modified the archive it's supposed to protect against divergence.

Verified each claim against live source before correcting anything — the sidecar's stale count checked out exactly (removing the four now-Resolved IDs from the list leaves exactly 10, matching the header). While fixing the Status block, found something neither the external audit nor the file itself had caught: versions 0.39, 0.40, and 0.41 have **no recorded history anywhere** — not in this file, not in the relocated archive. The header simply advanced to 0.41 with no changelog entry for any of the three intervening bumps. Rather than paper over that with a plausible-sounding reconstruction, left it explicitly flagged as an open gap in the Status block itself — fabricating a changelog entry to make the drift look resolved would have been a worse failure than the drift itself, in a document whose entire purpose is catching exactly that kind of confidence-outrunning-verification.

All five findings corrected: sidecar count (14→10), both Version String Registry citations, the Status block (rewritten, with the 0.39–0.41 gap named rather than hidden), and the sidecar hash refreshed against current archive content (computed directly via `sha256sum`, not estimated). No `Unknowns.md` entry needed — this was internal self-consistency drift within one file, not a new or closed unknown, matching the precedent set by the earlier RIP-count and Chemistry-Last-Audit fixes.

---
### 2026-09-01 — GU-002 closed; a Skeptic-anticipated interaction check found a real understated rule, and the closure had to distinguish two same-named but different DS-001 disputes
Grok scoped GU-002 correctly from the start: not a greenfield protocol, but cross-validating an already-substantial §5 draft against Gate_02's existing routing/provenance doctrine, plus writing the reciprocal side Gate_02 never had. The first real catch came from ChatGPT's Skeptic pass, and it was a subtle one: two different unknowns are both named "DS-001" — one on `Gate_07_Utilization.md` (fitness-for-purpose ownership, Low risk) and a separate one on `Gate_02_Triage.md` (whether retirement handoff triggers automatic vs. operator-initiated re-triage, Medium risk). Grok's original draft said the closure "encodes DS-001 Position B," which was accurate for the Gate_07 dispute but risked silently deciding the *different*, still-genuinely-open Gate_02 dispute by implication. Fixed by separating "eligible for re-entry" (interface-contract language) from "initiates re-entry" (the actual disputed question), and by stating explicitly in both files that neither DS-001 is touched.

Independently verified that separation against both live sidecars rather than trusting the summary — confirmed the two disputes really are distinct in substance, not just in ID collision, and that Gate_07's already carries a "Position B is standing practice" note from an earlier Grok review, which the revised proposal correctly treats as background context rather than something GU-002 itself ratifies. Also ran the specific interaction check ChatGPT flagged as a Skeptic target rather than guessing at: whether the "no automatic hold" language for a missing handoff record conflicted with any *existing* Gate_02 rule. It didn't — no existing rule ties a hold to a missing digital record. But the check surfaced something neither agent had looked for: Gate_02's existing table already says "Mandatory tag system; re-triage if tag absent," and the draft's parallel language for a *lost physical tag* said only "Gate_02 may route" — read as discretionary against a rule stated as mandatory. Grok's revision tied the tag-loss language explicitly to the existing mandatory rule rather than restating it more softly. A second, unrelated stale reference — a Drift Indicator entry in `Gate_07_Utilization.md` still describing the handoff format as "unvalidated" — was also caught and fixed during integration, the same class of gap caught for GMP-006 and GMP-010.

§5.1–§5.6 integrated into `Gate_07_Utilization.md`; reciprocal doctrine added to `Gate_02_Triage.md`; both DS-001s confirmed untouched; full Closure Event recorded. This is the fourth Closure Event this week and the second at Medium risk (non-Mandatory ratification, offered and accepted anyway) — worth noting that the same discipline (independent verification against live source, not the drafts' own claims) keeps finding real, if narrow, issues regardless of risk tier; the value hasn't been concentrated only in the High-risk closures.

---
### 2026-08-31 — GMP-006 closed after the most extensively reviewed Closure Event yet; two Grok/ChatGPT rounds each caught a real issue the prior round missed, and a second Claude Verifier round caught what both agents' own review had not
Grok drafted a Track B amendment state machine for GMP-006 (states, transitions, a five-point serialization corridor). ChatGPT's first Skeptic pass gave Conditional Pass with real findings: the draft over-tightened Phase 1 to single-occupancy where multiple drafts should be allowed; "Superseded" let an engineer unilaterally terminate another's Phase 2/3 proposal, a genuine authority-drift risk; "automatic on Phase 1 completion" silently contradicted the serialization gate it was supposed to respect; withdrawal and rejection authority needed phase-scoping; and the claim "serialization handles interaction risk" overstated what serialization actually prevents (concurrent-review bypass, not sequential post-ratification effects). Grok's revision addressed all eight amendments.

Independently verified the revision against live `§III` in `Governance_Migration_Protocol.md` before treating it as settled, the same discipline applied to GMP-010 and GI-004/GI-006 — and this time the check caught something neither agent had: Grok's authority table stated the adversarial reviewer advances a proposal into Phase 3. The actual §III text describes the reviewer's mandate (attempt to break the proposal; if they cannot, "the proposal is stronger for it") but never grants them a transition-executing authority — Phase 3 is Human Ratification's domain regardless. This was a real invented-authority risk the doctrine itself is supposed to guard against; catching it in a document about *authority discipline* was exactly the case that discipline exists for. Also found two live cross-references — an index line and a Drift Indicator entry — that still described GMP-006 as pending and would have contradicted a closure if left unfixed, the same class of gap fixed for GMP-010's §VI language.

ChatGPT's second Skeptic pass (after Grok's revision folded in the authority correction and the stale-reference flags) returned a clean Pass with one remaining small gap: the state machine never explicitly said when the Phase 2/3 corridor releases — upon ratification, or only after Phase 4 recording completes. Also flagged two Skeptic-test items to run rather than draft further: whether any existing governance doctrine imposes a time-bound ratification obligation that could conflict with §III.A.6's "human-attention, not automatic preemption" design note, and whether any other stale concurrency-permissive language existed beyond the two already-caught references. Checked both directly against source: no conflicting obligation exists anywhere in `Governance_Migration_Protocol.md` or `Governance_Charter.md`; no further stale language found. With three of ChatGPT's four remaining items confirmed clean and the fourth a one-sentence addition, integrated directly rather than sending it through another full drafting round for a single clarifying sentence — human governing authority agreed this was proportionate ("a little cleanup is fine").

§III.A integrated into `Governance_Migration_Protocol.md`; both stale cross-references corrected in the same pass; full Closure Event recorded reflecting all six review rounds (two Grok drafts, two ChatGPT Skeptic passes, two Claude Verifier passes). This is the most heavily reviewed closure this repository has produced, and every round caught something real — worth naming as evidence the multi-agent discipline is earning its cost, not just adding process theater. GMP-007 is now eligible for reconsideration against a real Withdrawn state, though it still needs its own funnel pass before promotion, not an automatic carry-over.

---
### 2026-08-31 — GI-004 and GI-006 closed jointly as an interface campaign; James's ratification-timing question confirmed the working discipline was real, not just described
Grok explored GI-004/GI-006 against live sidecars, recommending a joint campaign (Direction C) over three narrower alternatives — correctly identifying that GI-006 is mostly "promote provisional → specified" while GI-004 needed to be framed as an Intake-boundary contract rather than waiting on the still-unspecified grain format (ST-001/ST-002). ChatGPT's Skeptic pass on the resulting draft found the architecture sound but caught one real internal contradiction and two real gaps: "the physical tag is the sole link" directly contradicted the same section's own lost-tag recovery procedure, which necessarily uses secondary characteristics — fixed by narrowing the claim to "primary operational link"; "reasonable confidence" in the re-identification success criterion was undefined and risked inventing a numerical threshold the repository has no basis for — fixed with a falsifiable, threshold-free test (distinguishable from other plausible candidates; more than one plausible candidate = fail); and two claims (Gate_02's reciprocal language, item_id-reuse compatibility with Gate_02's existing Event_ID practice) were flagged as asserted rather than verified. Grok's revision addressed all five points.

Between the revision landing and integration, asked whether the revised language was actually in the working copy — it was not; only the Progress_Log posture update had been applied in the prior session, and the doctrine itself was still sitting as reviewed-but-unintegrated text in the conversation. This was deliberate on the human governing authority's part: pending work is sometimes left unratified in place specifically so it can be cross-checked before committing, and confirming the gap before integrating (rather than assuming prior turns had already landed everything discussed) is exactly the check that discipline depends on. Once ratification was given, integrated for real: independently reverified Gate_02's exact reciprocal text and the Event_ID re-triage practice against source (both confirmed accurate), read the full prior §7 line-by-line to confirm the replacement doctrine is a clean superset with nothing dropped, then wrote §7.1–7.4 into `Operations/Gate_01_Intake.md`, full Closure Events into both sidecars, an ASM-006 update reflecting the narrowed remaining risk, and the Unknowns.md/Progress_Log updates in the same pass. This is the first Closure Event carried through at Risk: Medium rather than High — human ratification was offered and accepted, but confirmed not to be Mandatory under `Admin/Auditor_Protocols.md`'s own rule, worth naming so a future closure at this risk tier doesn't wrongly assume ratification is required rather than optional.

---
### 2026-08-30 — GMP-010 closed same day it was promoted to Lane A; the first Closure Event carried through this repository's own AP-013 Unknown Closure Authority doctrine
Grok drafted an integration proposal for GMP-010 (Evidence-Sufficiency Gate for Directed Approaches), the item both agent notes and the funnel had flagged as the day's recommended first pick. ChatGPT's Skeptic pass caught a real procedural defect before anything else: the draft's own sidecar marked GMP-010 "Resolved" while its cover text said "does not self-close... ready for ratification" — a direct contradiction, and specifically the kind of silent status-upgrade GMP-010 itself exists to prevent. ChatGPT also flagged four substantive tightenings: "primary source" as originally worded would have let peer-reviewed secondary literature count as primary; the two-independent-source requirement, applied without qualification, would have deadlocked legitimate novel/proprietary/repository-generated claims that can never have two external sources; "load-bearing" had no operational definition; and §VI's existing "GMP-010 remains Open pending tooling" sentence would have contradicted a closure if left unedited.

Grok's revision addressed all seven amendments. Rather than accept the revision on the strength of Grok's own consistency-check table, ran an independent verification pass (Claude, distinct agent instance from both Grok and ChatGPT) against the actual amended text — confirming each of the seven fixes was genuinely present and correctly worded, not merely claimed, and separately re-checking every factual citation in the proposal against live source (§VII/Lessons Learned placement, the CE-006 canonical example's dates and mechanism, the Autonomy_Divergence_Protocol.md §4.2 cross-reference, the Resolution_Methodology Pattern 6/8 citation, the GMP-013 residual-class claim). All confirmed accurate. This is the first time this repository's Proposer/Verifier/Human-Ratification structure (`Admin/Auditor_Protocols.md` Unknown Closure Authority, AP-013) was carried out on a live closure rather than described in the abstract — GMP-010 is Risk: High, which triggers Mandatory Human Ratification under that doctrine's own rule, and the human governing authority's readiness to ratify was treated as the ratification act itself, not as a substitute for the missing independent Verifier pass that had to happen first. §VIII Evidence-Sufficiency Gate integrated into `Admin/Governance_Migration_Protocol.md`; §VI's contradictory sentence rewritten in the same pass; GMP-010 moved to Resolved with GMP-010-R1 (mechanical enforcement) preserved as an explicit residual; Risk/Priority left unchanged per Pattern 6/8 (specification closure is not a de-escalation). Full Closure Event recorded in the GMP-010 sidecar itself, per AP-013's recording-location rule.

---
### 2026-08-30 — Lane A repopulated from two independent agent proposals; funnel applied against live sidecars caught real dependency/evidence gaps neither agent's own check surfaced
Grok and ChatGPT independently proposed the same Lane A refresh direction (unprompted convergence, not a joint session): reframe Lane A as a scarce resource rather than a queue, add a hard exclusion rule (no promotion if an upstream dependency or explicit evidence requirement blocks specification-only closure), and require a six-step funnel — identify, read sidecar, check Resolution Path, check dependencies, confirm closure vehicle, only then promote — before anything reaches Lane A — Active. Both proposed running that funnel against two clusters: GMP amendment-lifecycle/process-infrastructure unknowns, and cross-module interface contracts (Intake↔grain, Utilization↔Triage, Characterization↔Gate 04/05/06).

Ran the funnel for real against the live sidecars rather than accepting either note's own funnel-status labels. Of ten "Strong candidate"/"Candidate" claims across both notes, seven confirmed clean and three did not survive direct verification — a real catch, not a formality: **GMP-007** was rated alongside GMP-006/008 as a parallel strong candidate by both notes, but its own Resolution Path explicitly reads "when GMP-006 is resolved" — dependency-blocked, not independently payable. **GMP-008** was also rated Strong candidate by both, but its Resolution Path says "Defer to when governance cadence is established (Trajectories.md v1 milestone)" — not specification-payable now under either note's own hard-exclusion rule. **GR-001** was listed by ChatGPT only as "Related... may consolidate with FL-002," with no flag that its Resolution Path requires characterizing actual Reduction output against representative feedstock samples and explicit promotion to Measured evidence — real hardware work — and that both GR-001 and FL-002 share an upstream dependency on GR-002 (Reduction method selection), itself still Open. Neither agent note caught the GR-002 dependency at all.

Seven items promoted to Lane A — Active across two clusters (GMP-006/010/012 clean, GMP-011 an in-progress refinement; GI-004/GI-006/GU-002 interface contracts), plus two flagged as spec-payable only in part (GMP-013's schema sketch vs. its Automation-implementation scope; CLF-011's §4b contract ratification vs. its gate-side emit/read build). Three agent calls that correctly held items out (GMP-002/003/004) were rechecked and confirmed accurate rather than assumed. Full breakdown in Forward Growth Avenues, Lane A section above. Worth naming the general lesson: a well-designed verification funnel is only as good as whether it's actually run against source per item, not applied as a plausibility filter over an agent's own summary — the two misses above (GMP-007/008) were exactly the failure mode both notes' own hard-exclusion rule was written to prevent, proposed by the same notes that then didn't fully apply it to their own list.

---
### 2026-08-30 — Cross-checked two independent morning audit reports (old-prompt and new kit-sourced prompt) against the working copy; caught a real recurrence of the cluster-tree staleness bug fixed once already; consolidated the audit prompt itself into a versioned repo file
Two Grok reports arrived the same morning — one run on the prior prompt version (fetching `Admin/Auditor_Protocols.md`/`Admin/File_Template.md` directly), one on the updated kit-sourced prompt. Both correctly caught real, already-known lag items (RIP count, Progress_Log header) still unfixed on the live repo since the fixes existed only in this session's working copy, not yet pushed. The kit-sourced report additionally caught three genuinely new findings the old prompt's report missed: `Challenges/Closed_Loop_Feedstock.md` Open Unknowns counted Resolved CLF-005 as open (10 claimed vs 9 actual — same class of miscount as RIP's, different file); `Architecture/Chemistry.md` Last Audit hadn't moved past 2026-07-31 despite a real CE-006 doctrine refresh on 2026-08-16; and `Challenges/Waste.md` Last Updated still read 2026-07-11 despite WA-002's Resolved-2026-08-23 text already in its own body. All three verified against source before fixing — no blind acceptance of either report's claims. A fourth finding, the Unknowns.md Safety-Critical Dependency Cluster tree still drawing WA-002/PL-001 as live blockers, is the same staleness class `Unknowns.md` v4.87 had already fixed once for a different cluster (Trust & Integrity: GOV-003/SEC-007a) — worth naming explicitly as a repeatable check rather than treating each cluster separately, since the underlying bug (a cluster diagram not updated when its Active Index counterpart resolves) isn't scoped to one cluster.

Separately, consolidated the morning-audit prompt itself — previously living only inside the external automation's own config screen, un-versioned and un-diffable — into `Admin/INTEGRITY_SWEEP_PROMPT.md`, following the `Admin/PROBE_INVOCATION.md`/`Admin/BATTERY_SEED.md` precedent (File_Template.md exemption class 6: operational prompt, not doctrine). Folded in the three corrections proven out across this week's live runs (kit-sourced fetching, File-State-count-vs-sidecar cross-check, header-vs-body freshness check) plus a fourth (Dependency Cluster staleness check) from this session's own finding. Registered in `Routing.md` (genuine map addition — first real change since the 2026-08-16 freeze) and `Discovery.md`.

### 2026-08-25 — ChatGPT full Charter audit absorbed; one of its three proposed fixes was itself wrong, caught before integration
ChatGPT ran a full audit of `Admin/Governance_Charter.md` against `Admin/Forge_Audit_Kit.md` and `Admin/Auditor_Protocols.md`, applying all ten Adversarial Battery classes. Verdict: governance architecture sound (G3–G6 pass; GOV-003 ladder, GOV-022 non-axiomatic status, doctrine/procedure split, and the honest GOV-005/GOV-008/SEC-007b blockers all explicitly endorsed as correct), but three epistemic-metadata defects found (G1/G2 blocked): a retired "Estimated" confidence label surviving on the Genesis review horizon, a legacy single-column "High" confidence label surviving in the Assumptions table instead of the current two-axis Confidence/Provenance system, and an Open Unknowns File State field whose parenthetical could be misread as including resolved GOV IDs in the active count.

Grok drafted three textual patches. Two integrated as proposed. The third — the retired-Estimated fix — was wrong: it proposed relabeling the Genesis horizon as **Placeholder**, but `Admin/Auditor_Protocols.md` AP-021 explicitly states a retired Estimated claim "should be relabeled Analogous or Simulated" — Placeholder isn't offered as an option. Checked before integrating; corrected to **Analogous** (the better fit of the two allowed labels, since the figure isn't derived from a computational model). This is the same shape as GOV-003's original ladder conflict and GR-003's field-convention deviation earlier this session: a plausible, well-reasoned draft that fails a specific doctrinal check the standing discipline exists to catch — this time the failure was inside a *correction to an epistemic-hygiene defect*, which is a slightly sharper version of the same lesson: fixing metadata errors is not exempt from the same verify-before-integrate standard as fixing anything else.

While integrating, the same paragraph search also surfaced two further stale claims unrelated to the audit itself, in the Charter's own Auditor Notes section: a second instance of the exact misread pattern ChatGPT's third finding described, and a claim that GOV-022 was "the currently open item on Reversibility" — GOV-022 has been Resolved since 2026-08-21, and this false claim had survived at least two intervening edits to the same paragraph, including one made earlier this session, before being caught here. Both fixed same pass.

---
### 2026-08-30 — Three-version changelog migration lag caught in `Unknowns.md` (v4.84–v4.86 never migrated to `Unknowns_Changelog.md`); Discovery.md's missing header field also found while checking the same class of gap

Raised directly by the human governing authority: prior agents had been overlooking changelog updates while doing other work, and asked that this be checked and fixed as found, not just this once. Found `Unknowns.md`'s own version-history block explicitly states it "now keeps only the current version" (set as the fix for the 20-version stacking bug named in v4.84's own entry), but v4.84, v4.85, and v4.86 had all been left stacked in that block instead of migrated when each was superseded — the same failure recurring one version-window later, this time three versions deep rather than twenty. All three migrated into `Unknowns_Changelog.md` in full; `Unknowns.md` trimmed to v4.87 only. While checking for the same pattern elsewhere, found `Discovery.md` had no `Last updated`/`Version` header string at all (not stale — never present), which had been fixed inline on 2026-08-29 without a corresponding entry in `Discovery_Changelog.md`; entry added there to match. `Governance_Charter_Changelog.md`, `Forge_Audit_Kit_Changelog.md`, and `AUDIT_HARNESS_CHANGELOG.md` checked and found not implicated — none of this session's edits touched their owning files' doctrine. Worth a standing habit going forward: any edit to a file with a dedicated changelog should be treated as two edits, not one — the source file and its changelog entry — since the omission is easy to make and, by design, invisible until someone checks. Human-directed.

---
### 2026-08-28 — Four patterns from this week's closures distilled into `Admin/Resolution_Methodology.md`, prompted by a direct question rather than found independently
Asked directly: what should a following agent know that isn't already in this file or in `Admin/Resolution_Methodology.md`? Checking that file's five existing patterns (all dated through mid-August) against the past week's work found four genuinely general, repeatable moves that had been independently rediscovered or enforced multiple times this session without ever being written down as a citable pattern — meaning a future agent would have had to infer each one by reading several scattered closure notes rather than finding it stated once. Added as Patterns 6–9: the specification/operational-clearance split with a named residual (used identically across GOV-003, PL-001, WA-002, GR-003); Discharge via Consolidation vs. a fresh specification, and how to tell which applies (the WA-004 case); verifying a drafted closure's *structure* against actual precedent text, not assumed convention (distinct from the existing verify-before-accept pattern, which is about factual claims, not format); and self-maintenance verification for both prose and code — the single pattern that recurred most this week, having bitten `Unknowns.md` twice, this file five times, and `integrity_check.py`'s own dashboard once. Two further real findings from this session (the zip-naming convention agreed with the human governing authority; the README/Discovery.md/doctrine-file layering principle) were judged not to fit either this file's or Resolution_Methodology's scope and were flagged as needing a different home, not silently dropped or forced in. File State header and version bumped on Resolution_Methodology.md; health check re-run afterward and confirmed unchanged from before the edit. Human-directed.

---
### 2026-08-27 — Health dashboard built on top of `Automation/integrity_check.py`; nearly "fixed" a checker that was actually correct, then found a real 8-file drift the checker was right to flag; two follow-up bugs found and fixed the same day
Scoped down from a larger ChatGPT/Grok-proposed bundle (full repository-health dashboard, Capability/Evidence/Governance/Memory layer taxonomy, unknown-dependency visualization) to the two pieces that were genuinely mechanical rather than requiring an invented judgment call: Tier 1 (PASS/FAIL badges per `integrity_check.py`'s five existing check categories, derived from findings the tool already produces) and Tier 2 (active-unknown counts by Priority, parsed directly from `Unknowns.md`'s own tables). Explicitly did not build the "Governance state" / "Physical validation" / overall "ALPHA readiness" badges from the original proposal — those would require inventing a threshold this repository's own doctrine doesn't define anywhere, which is exactly the kind of manufactured-looking-mechanical number the Placeholder/Analogous confidence discipline exists to prevent.

Added `unknowns_summary_pass()` and `print_health_summary()` (invoked via a new `--health` flag), reusing the existing `Finding` objects rather than duplicating logic. One self-inflicted bug caught before delivery: an early edit dropped the `def run(root):` line entirely while inserting the new pass — caught immediately by running `ast.parse()` against the file after every edit, which is now the standing practice for any Python file touched here, the same "verify a file matches what you think you wrote" discipline applied everywhere else this week, just for code instead of prose.

Running the finished tool against the live repo surfaced a real finding, and very nearly caused a second, more consequential mistake: 8 files showed `CRITICAL` Ethical Anchor mismatches. The 8 files' actual text was byte-identical to what looked like the checker's own comparison string in the printed message, which briefly looked like a false positive in `parser.py`. Before touching `parser.py`, checked `Admin/File_Template.md` directly — its own prose states the Ethical Anchor "must match the canonical string exactly... Absence, alteration, or blank value is a mandatory drift indicator requiring human review," and its declared canonical string is the plain form (no backticks, no `Admin/` path prefix) — matching `parser.py` exactly. `parser.py` was correct throughout; the tool worked as intended on its first real run.

**Same-day follow-up (1): the 8 files fixed, which then exposed two real bugs in the checker itself.** Corrected all 8 files' Ethical Anchor field to the canonical form (`Adm_Scope_Map.md`, `Progress_Log.md`, `Arc_Scope_Map.md`, `Rename_Registry.md`, `Cha_Scope_Map.md`, `Ops_Scope_Map.md`, `Field_Logs.md`, `Tst_Scope_Map.md` — the same drift class already recorded in this repository's history, a nine-file version of it found and corrected in July). Re-running the checker to confirm dropped the warning count from 6 to 3, not 0 — investigating the remainder found `_parse_markdown_tables` in `parser.py` had a real, pre-existing root-cause bug: any two-column pipe table anywhere in a file's first 60 lines was treated as a detected File State schema, with no check that it actually resembled one. This misclassified README.md's "Choose your path" table and Routing.md's routing map as File State declarations, then flagged them for a "missing" Ethical Anchor they were never supposed to have. Fixed by anchoring the table scan to an actual `## File State` heading (confirmed as the universal convention across every real doctrine file) rather than scanning blindly from the top of any file — fixes the bug at its source for any future unrelated table near a file's top, not just the specific files found today. A second, related bug in `_parse_legacy_inline` used the same blind-scan pattern and matched the substring "Status: Resolved." inside ordinary changelog prose (e.g. "...Lessons Learned: ... Status: Resolved.") as if it were a genuine legacy metadata declaration — fixed with the same heading-anchor requirement plus a line-length guard, since a real legacy header line is short and standalone, not embedded in a paragraph. Both fixes verified two ways before trusting them: confirmed a genuinely altered Ethical Anchor is still caught (`present_but_altered`), and confirmed the real unaltered file still parses clean (`exact`) — a false-positive fix that silently also broke true-positive detection would have been a worse outcome than not fixing it at all.

**Same-day follow-up (2): the dashboard itself was found to be silently hiding real findings.** Cross-checked the dashboard's Tier 1 category list against the actual `Finding` category strings used throughout the codebase, rather than trusting the names chosen when writing it that morning. Two were wrong: `UNKNOWN_ID` doesn't exist anywhere in the code (the real category is `DUPLICATE_ID`) and `VERSION` should have been `VERSION_STRING`. Because of this, the dashboard was showing a false "PASS" for sidecar-ID uniqueness while 11 genuine `CRITICAL` findings (duplicate sidecar IDs, e.g. `CO-001`, `GK-001`–`005`, `EV-001`–`003`, each defined in both a live doctrine file and an `Archive/Transcripts/` file) sat completely unrepresented in the summary — a tool that looks authoritative but silently drops a whole category is worse than one that visibly can't check something, since it invites exactly the trust the earlier reviews warned a hand-maintained dashboard would erode. Fixed by cross-referencing every `Finding("...", "CATEGORY", ...)` call in `integrity_check.py` and `audit_lib.py` against the dashboard's category list directly, then confirming zero findings fall outside the six covered categories (checked programmatically, not by inspection). The 11 duplicate-ID findings all share one consistent pattern (live file vs. its own `Archive/Transcripts/` predecessor) and are very likely benign, but that wasn't verified by reading the transcript files themselves — left as a real, now-visible finding rather than assumed resolved.

Also surfaced and left open: 90 cross-reference `WARNING`s (no `CRITICAL`s), a mix of expected categories (`[LEGACY]`, `[ARCHIVE]`) and at least a few that look like they may be matching illustrative example text inside `Canonical_Terms.md` rather than real broken references. Not investigated — pre-existing backlog, large enough to be its own scoped task.

**Same-day addendum: two small README refinements, both verified against source before applying.** ChatGPT and Grok both independently revised their earlier "rewrite the README" position after seeing the adopted engagement version, converging on "stabilize, don't restructure again" — a clean two-item list rather than the earlier large bundle. Both cited the same two changes; both citations checked out against the live file exactly as quoted. Applied: (1) "The Forge does not optimize for efficiency" → "...for efficiency alone," since the absolute phrasing was reasonably readable as indifference to efficiency rather than the intended subordination-to-resilience point — same overclaiming-by-imprecise-wording class as the earlier "complete seven-gate architecture" fix. (2) Added a compact "What is real right now" table near Current status, complementing rather than replacing the existing prose bullets — explicitly noted in the README as distinct from and not a substitute for `integrity_check.py --health`, since the two check fundamentally different things (doctrine/evidence maturity vs. mechanical repository consistency) and conflating them would misrepresent what either one actually verifies.
**Same-day follow-up (3): this file dropped an entire entry while being edited to add the note above.** A rewrite of this Current Lessons block — done specifically to fix the recurring ordering bug and extend this entry — silently omitted the 2026-08-24 GR-003 entry entirely, rather than rotating it to the changelog as intended. Caught immediately after the edit by checking this file's own entry list against what should have been there, the exact discipline this same entry had just finished describing for the checker's false positives. Recovered from the earlier conversation record and moved to `Archive/Logs/Progress_Log_Changelog.md`, with a note on how it was found. Fifth instance of this file failing to preserve its own content correctly in one week (four prior: lost entries 2026-08-24, EC-batch header loss 2026-08-22/found-08-24, ordering slip 2026-08-25/found-08-26, ordering slip again 2026-08-26/found-08-27) — worth being blunt about: this file is unusually failure-prone for edits to its own structure, specifically, even under the same discipline that has worked reliably everywhere else. Large multi-entry rewrites to this file's Current Lessons block are now treated as higher-risk than ordinary single-entry appends, warranting an explicit post-edit entry-count-and-content check every time, not just when something feels off.

---
### 2026-08-26 — README rewritten for engagement, adopted with a stabilization pass; another ordering bug caught in this same file while adding the entry
Grok rewrote `README.md` for newcomer engagement, following a ChatGPT structural review (elevator pitch → entry-point table → small first experiment → "Don't Trust the Forge" challenge invitation → condensed status → doctrine → architecture). Verified before adopting: every linked file exists; the earlier GOV-003 status correction survived intact rather than being reverted. Two real gaps found and fixed before treating it as done: (1) the condensed Status section's "see Discovery.md for detail" pointer wasn't actually honored — three of four governance mechanisms it used to name in full (Verification Termination Threshold, Governance Complexity Ceiling, Reversibility) didn't appear in Discovery.md at all. Fixed by adding a dedicated section there naming all six current governance mechanisms with direct section pointers, rather than restoring the detail to the README itself — human governing authority explicitly confirmed this split (README stays an invitation, Discovery.md carries the detail, Routing.md stays a skeleton) before the fix was written. (2) A harmless but unnecessary hedge — "Routing.md (if present in your clone)" — on a file that does exist in this distribution; removed. Grok's proposed architecture-diagram redesign was not applied; the existing simple ASCII diagram was kept as-is, since no image was actually produced from the text spec, only a description of one.

**Second finding, while adding this entry:** the 2026-08-25 Charter-audit entry (since rotated to `Archive/Logs/Progress_Log_Changelog.md`) had been appended after the file's stated "most recent first" order, landing last instead of first — the same category of self-referential ordering slip caught twice already this week in this exact file (lost entries 2026-08-24, EC-batch header loss 2026-08-22/found-08-24), and again today (see the 2026-08-27 entry above — the same reordering mistake happened a fourth time while that entry was first drafted, and was caught and fixed before this version was written). Given four separate instances of this file failing to maintain its own stated invariants (content loss, missing rotation, ordering — twice) inside one week, the standing fix from 2026-08-24 — verify a file's own claims against its actual content after any edit — is being treated as applying to *this file itself* every time it's touched, not only to Unknowns.md-style closures.

**Same-day follow-up:** ChatGPT and Grok independently reviewed the adopted README as a full repository walkthrough, not just the file itself, and converged on a shared diagnosis — "easier for an auditor to understand than for a newcomer." Both proposed a large bundle (README first-screen compression, a generated repository-health dashboard, a new Capability/Evidence/Governance/Memory layer taxonomy, an unknown-dependency visualization). Scoped down to the smallest clean win rather than the full bundle: softened "a complete seven-gate operational architecture" to "a defined... architecture" (the word "complete" was doing exactly the overclaiming work this repository's own epistemic discipline exists to catch — both reviews flagged it independently), and added an explicit "Not yet demonstrated" bullet list to the Status section (physical validation at scale, energy-independent economics, autonomous operation, self-replication, off-world capability) rather than leaving that only implied. Confirmed GOV-005/GOV-006 still the accurate named gaps before leaving that line untouched. Worth noting for the record: Grok's own example content in its review (a "current load-bearing unknowns" list) named WA-002 and PL-001 as still-open blockers — both had closed hours earlier the same session — a live demonstration of the exact stale-hand-maintained-status problem both reviews were warning about. The larger bundle (dashboard, layer taxonomy, dependency visualization) deliberately deferred, not rejected — flagged as worth deciding on deliberately rather than adding because it sounded clean.

---
### 2026-08-24 — WA-004 discharged; a much larger hygiene gap found underneath a small question, and a concrete process fix adopted, not just a retrospective note
What started as "close WA-004" (a near-formality — its own text had said for weeks that it just tracks GR-003) surfaced two real, pre-existing problems in `Unknowns.md` while checking for the right closure vocabulary: (1) **Size Management Rule 2 violation** — the file's own explicit rule says Resolved entries "leave the Active Index immediately," but 26 Resolved entries across many sessions (not just today's six) were sitting in the active tables with full paragraph descriptions, including several from mid-July. (2) **Version-history stacking** — the file's own header says "this block now keeps only the current version," but 20 full version entries (v4.63–v4.82) had accumulated instead of being migrated to `Unknowns_Changelog.md` one at a time as intended, despite every single one of those 20 entries' own closing line claiming "vN migrated to changelog intact." That claim was false for 20 consecutive versions and nobody — agent or human — checked it.

Both fixed same-day: 26 rows removed with pointer notes added, 20 versions migrated to the changelog, `Unknowns.md` restored to matching its own stated rules. Neither problem affected any owning file's actual doctrine — both were purely navigation-layer staleness in the index file.

**The concrete question this raised: prose reminders embedded in content aren't sufficient by themselves.** The "vN migrated to changelog intact" line is a good instinct — document the expectation right where the next editor will see it — but it kept getting copy-pasted forward as true even after the underlying action stopped happening, which is worse than silence: it creates false confidence that gets inherited by whoever reads it next, including a prior instance of me earlier today, who read that note and treated it as evidence the file was already properly maintained rather than checking it.

**Process fix adopted, not just noted:** when closing any unknown from here forward, the closure checklist includes an explicit Unknowns.md hygiene step — confirm the closed row is either removed per Rule 2 (with a pointer note) or has a clear reason not to be, and confirm the version-history block still holds only the current version before considering the closure complete. This is the same shape as the header-hygiene habit adopted after the GOV-013 catch (2026-08-23) — checking a file's self-maintenance claims against its actual content, not just checking the substance of the change itself. Rather than trusting a prose note to prompt this later, it's now part of what "done" means for a closure, same session it was needed.

**Second, self-referential instance of the exact same failure class, caught the same day:** while reconstructing this file's own entry list to add the note above, four prior entries from earlier today (GOV-013 sweep, PL-001, WA-002, GR-003 — see below) were found to have been silently lost during an earlier edit to this same file, rather than preserved as intended — an edit that appended new content without cleanly removing what it was meant to replace, leaving duplicated and orphaned paragraph fragments below. Reconstructed from the conversation transcript, deduplicated, and rebuilt cleanly. This file's own stated rotation rule ("rotate once more than five entries accumulate") had also never actually been exercised — same shape as Unknowns.md's version-stacking bug, just in a different file, and a genuinely orphaned entry from 2026-08-22 (EC-series batch, below the fold, never given a proper header) was found and recovered in the same pass. The two 2026-08-21 entries, the 2026-08-22 EC-series entry, and the five 2026-08-16 entries all moved to `Archive/Logs/Progress_Log_Changelog.md`; this file trimmed to the current five. The honest reading: a rule written down and never followed is not meaningfully different from no rule, and checking "does the file actually match what it claims about itself, including its own internal consistency after an edit" needs to be a standing step, not a one-time correction — the process fix above now covers verifying an edit actually landed as intended, not only Unknowns.md-specific hygiene.

---
### 2026-08-24 — GR-003 closed; a field-convention deviation caught by checking Grok's draft against the actual post-closure text of PL-001/WA-002/GOV-003, not just against stated intent
*(Entry recovered 2026-08-27 — dropped entirely from `Progress_Log.md` during a same-day rewrite meant to fix an unrelated ordering bug in this file, the exact self-referential failure mode that rewrite's own new text was describing. Caught by checking this file's entry list against what should have been there, immediately after the edit, rather than assuming the rewrite landed as intended. Content below is unchanged from the original entry.)*

Grok drafted a full closure patch for GR-003, correctly identifying it as a narrower, more surgical gap than PL-001/WA-002 had been — the 2026-08-15 architectural pass had already supplied the two-outcome model and five-category structure; only concrete hold-duration and container values were missing. The draft's technical content (RCRA-analog accumulation limits, container specifications, biological hold duration) checked out. One process deviation was caught before integration: the draft annotated Risk and Priority fields as "(residual)" and "→ residual only" after closure, which is new notation not used in any of the three prior closures this session — verified directly against Plastics.md and Waste.md's actual post-closure header text (both kept Risk/Priority unchanged, Critical stays Critical). Corrected before integration. Also fixed in the same pass: GR-007's and PYC-003's own stale cross-references, both of which still described WA-002/GR-003 as blocking dependencies after those unknowns resolved. This is a smaller version of the same discipline as the GOV-003 ladder catch and the WA-002 closure-convention question — checking a draft's self-consistency against established precedent, not just its internal logic, before treating it as ready.

---
### 2026-08-23 — WA-002 closed; a closure-convention inconsistency caught and resolved by explicit human decision rather than silently picking one
Grok extended `Challenges/Waste.md`'s existing WA-002 identification protocol with a training/demonstration standard and confirmatory lab-arrangement structure. A ChatGPT Skeptic pass caught two source overclaims before integration (solder identification framed as competency rather than presumption; Beilstein framed as Forge-validated rather than an established-but-unvalidated screen) — both corrected, and the same pre-existing overclaim found and fixed in this file's own older BFR paragraph while integrating. Separately, ChatGPT's own recommended disposition for WA-002 was to leave it Open/Critical after this specification work, which would have created a live inconsistency: PL-001 and GOV-003, both closed earlier this same session with a materially identical shape (full specification, one named empirical residual), were both marked Resolved with the residual keeping practical blocking force. Flagged to the human governing authority before integrating rather than picking either convention unilaterally; confirmed to proceed using the PL-001/GOV-003 convention for consistency. Recorded here because this is exactly the class of problem GOV-015 (aggregate interpretation drift via subordinate doctrine, closed earlier this session) describes in the abstract — two structurally identical closures using different status conventions, here caught within the same session rather than drifting apart across future ones.

---
### 2026-08-23 — PL-001 closed; a chemistry-domain false-negative gap caught before integration, not after
Grok drafted a Halogenated Polymer Triage Protocol for PL-001. Initial version used one shared rule: Beilstein-negative clears halogen suspicion. A Claude Skeptic pass caught that this is chemically wrong for one of the two target polymer classes — Beilstein is a chlorine/bromine-biased flame test and does not reliably detect fluorine, so PTFE/Teflon contamination could pass a Beilstein-negative screen undetected under the original logic, exactly the failure PL-001 exists to prevent (HCl/dioxin release, reactor corrosion). This is the same category of catch as GOV-003's ladder conflict earlier this session — a draft that looked complete and Skeptic-ready failed on a substantive check, not a formatting one — but in a different domain (chemistry, not governance doctrine), which is worth noting: the standing verify-before-integrate discipline generalizes across domains, and should not be treated as governance-specific. Revised draft split screening by polymer class, closed cleanly. Integrated 2026-08-23; Blocking Yes retained pending PL-001-R1 empirical validation, same specification/validation split as GOV-003.

---
### 2026-08-23 — Systematic sweep found one real stale reference (GOV-013) outside the file it originated in, plus routine post-closure staleness; GOV-003's standing caution reconciled, not silently dropped
Following GOV-003/GOV-015/GOV-018 closure, ChatGPT's cross-check flagged a stale "Open Unknowns 20" summary inside `Admin/Governance_Charter.md`'s own `## Auditor Notes & Unknowns` narrative block — accurate, and fixed same-day. That catch prompted a broader question: if one stale claim survived a closure pass, could there be others? A full mechanical sweep was run across all 82 files carrying a `## File State` block, extracting every `Highest Risk` field that named a specific unknown ID and checking that ID's actual status in `Unknowns.md`. Result: exactly one genuine error found — `Admin/Governance_Charter.md`'s Highest Risk field still named **GOV-013** as Critical/open; GOV-013 was in fact ratified 2026-07-19, over a month before this session, with its own "RATIFIED" section already in the Charter body. The stale field had been carried forward silently through at least the 2026-08-21 and 2026-08-23 header updates, including one made earlier this same session, without anyone (agent or human) checking it against the ratified section sitting a few hundred lines below it in the same file. Fixed same-day: Highest Risk field now correctly names GOV-005 as the sole open Critical. Every other Highest Risk ID reference in the repository (GOV-008, CLF-003/006, EN-001, SR-001, RE-UNK-001/005, LW-UNK-001/003, CIR-001) was checked and confirmed accurate — this was not a systemic problem, but it was a real one, caught only because a second agent's routine cross-check happened to look in that direction.

Separately, this same sweep surfaced that `Admin/Progress_Log.md`'s "Explicit non-work for now" list (2026-08-21) had specifically flagged "working GOV-003 as if its resolution path were specification-only" as a thing not to do — written before GOV-003 was closed today via specification. Reviewed against what was actually integrated: the closure did not claim full Enforceability: it scoped itself explicitly to architecture-level specification, left external root-of-trust instantiation (SEC-007b) as the named blocking residual (GOV-003-R1), and a ChatGPT Skeptic pass independently forced exactly that scoping distinction (ordinary procedural enforcement vs. constitutional enforcement under compromise) before Accept. Human governing authority confirmed directly: GOV-003 is "as much work as we can do currently without further testing" and letting the closure stand is safe, with further work flagged for when more information (a real SEC-007b instantiation) is available — see GOV-003-R1/R4 in the Charter section and this entry. Recorded here so the reconciliation is on record rather than the tension being silently dropped.

---
### 2026-08-22 — EC-series batch (EC-003/004/008/009/016) integrated cleanly on content but shipped non-conforming Closure Events, and this file itself lagged a third time
*(Entry recovered 2026-08-24 — this content existed in `Progress_Log.md` since 2026-08-22 but had lost its section header at some point before that date, leaving it as an orphaned, unheaded paragraph tacked onto the end of the Current Lessons block. Found and given a proper header during the same 2026-08-24 pass that fixed the rest of this file's rotation backlog. Content below is unchanged from what was recovered, aside from adding this note and the header.)*

Grok drafted EC-016, EC-008, EC-003, EC-009, and EC-004 (EC-005 was ratification-only) in a single working session; Claude source-verified every claim in every draft against actual file content before integration, and nothing false or fabricated was found anywhere in the batch — a clean run on substance. But the four integrated Closure Events (`Admin/Governance_Charter.md` EC-016; `Admin/Ethical_Constraints.md` EC-008, EC-003/009, EC-004) were written as a short prose summary ("Drafted by Grok; source-verified by Claude") rather than against `Admin/Auditor_Protocols.md`'s own Unknown Closure Authority §'s eight-element minimum — missing, specifically, an explicit independence attestation and a recorded Verifier verdict, both present in every prior closure this repository has done (AP-005, AP-013, AP-024, GOV-014/016/020, GOV-022). Per that section's own text, a Closure Event missing a required element is invalid, not merely informal. Caught only when asked directly whether the batch had been checked against Auditor_Protocols.md's recent closure-authority update — not caught by the verification pass itself, which checked draft *content* against source but not the resulting Closure Event's *format* against the doctrine governing Closure Events. Fixed same-day: all four entries brought to the full format. Separately, this file had — again — recorded nothing about the batch until this same follow-up prompted it, the third occurrence of the identical lag (2026-08-14, 2026-08-21, now 2026-08-22). Worth treating as a pattern needing a structural fix, not another isolated catch: verifying a draft's factual claims and verifying its resulting artifact's procedural conformance are two different checks, and neither this file's own update discipline nor the source-verification step being used here catches its own staleness without being asked.

---
### 2026-08-21 — Five ratified closures sat unrecorded here for a full day
`Unknowns.md` reached v4.72 on 2026-08-21 carrying five closures
(AP-004, AP-024 on 2026-08-20; GOV-014, GOV-016, GOV-020 on 2026-08-20;
GOV-022 on 2026-08-21) with zero corresponding entries in this file.
Caught the same way as the 2026-08-14 entry below it — a session asking
"what's left" from outside, not this file's own rotation discipline
triggering on the ratifications. Same family, same root cause restated:
a file that exists to prevent progression content from going stale is
not itself exempt from going stale.

### 2026-08-21 — Two independent external "what's left" summaries both misstated GOV-022's status, one also misdirected effort toward a hardware-blocked item
Asked ChatGPT and Grok directly what work remained. Both listed GOV-022
as needing its Operating Principles subsection drafted; source
(`Unknowns.md` v4.72, `Admin/Governance_Charter.md` GOV table,
`Archive/Logs/Governance_Charter_Changelog.md` sidecar) shows it Resolved
and ratified the day before. One summary also named GOV-003 as a live
Critical target without checking that its own Resolution Path
(`Admin/Security_Protocols.md` Phase 3) is explicitly "Blocked by
[Phase] 1 and 2" and gated by SEC-ASM-003 on GOV-008 — the same
no-second-physical-host wall already blocking GOV-008 itself. Separately,
a source-verification pass on the six items the frozen 2026-08-14 Forward
Growth Avenues still listed as Lane A found four (TS-002, GI-002, GF-007,
CE-006) had already been advanced past Lane A by spec-depth passes on
2026-08-15, landing on genuine hardware/validation gaps not reflected in
that section's wording. Standing lesson reinforced twice in one session:
agent "what's left" summaries are candidate leads, never a source of
truth, and a Lane assignment written on one date does not stay accurate
after later sessions advance the underlying file.

### 2026-08-16 — GitHub MIT badge / classifier fix

Root `LICENSE` reduced to pure standard MIT body only (no appended NOTICE). Forge-specific interpretation moved to root `NOTICE`. `LICENSE.md` is a short human pointer. GitHub was classifying the previous combined file as license key `other` / SPDX `NOASSERTION` because the classifier matches known templates and rejects extra text in `LICENSE`.

### 2026-08-16 — License boundary cleanup (release integrity)

Root MIT remains sole license for material under project control. Removed conflicting CC-BY-SA footer from `Admin/Nothingness_Theorem.md` (Option A — maximum propagation, no dual-license ambiguity). Added bare `LICENSE` alongside `LICENSE.md` for GitHub discoverability. NOTICE clarified: MIT covers copyrightable expression; not ownership of abstract ideas/methods; not trademarks or validation status.

### 2026-08-16 — Tag naming convention (Alpha release hygiene)

**Canonical Git tags** for the Alpha line: `V1Alpha.NN` (no dot after V1), e.g. `V1Alpha.03`, `V1Alpha.04`.
Do not use `V1.Alpha.NN` for new tags. Archive zip filenames may keep human-readable forms (e.g. the pre-rename `LazarusForgeV0-1.Alpha.03`, or the current `LazarusForge-1.Alpha.04` convention going forward); Git tags stay machine-consistent. Historical tags already published are left as-is; new releases follow this rule.

### 2026-08-16 — Integrity incident log stood up (no more willy-nilly)

`Admin/Integrity_Incident_Log.md` created as the canonical append-only home for RIP integrity incidents. Major and Constitutional response steps in Repository_Integrity_Protocol.md now point here; Minor compound-drift (≥3 audits) also logs here. Ownership table implements RIP-007 minimum (Minor → detecting auditor; Major → human operator; Constitutional → human governing party only). File-local Resolution Logs remain for remediation detail; Progress_Log remains for continuity lessons; Field_Logs remains for physical/multi-agent evidence. Prior scattered incidents were not retroactively fabricated into the log. Routing + Adm_Scope_Map registered.

### 2026-08-16 — Priority 2 cross-reference debt classified (no files invented)

Integrity harness UNKNOWN references after Priority 1 (Resolution_Methodology routed; Auditor_Protocols templates at v0.37) classified into five bins. **No new doctrine files created** to silence the harness.

**1. Real active file → route / fix path (done or already routed)**
| Target | Action |
|--------|--------|
| `Admin/Resolution_Methodology.md` | Routed in Priority 1 |
| `Archive/Logs/AUDIT_HARNESS_CHANGELOG.md` | Live refs in Unknowns.md pointed at wrong `Admin/` path → corrected to Archive/Logs/ |
| `Archive/Logs/Forge_Audit_Kit_Changelog.md` | Same path correction |

**2. Renamed file → use Rename Registry (do not re-create old name)**
| Stale name | Canonical | Notes |
|------------|-----------|--------|
| `Verification_Gates_LF.md` | `Admin/Verification_Gates.md` | Rename Registry 2026-08-09; remaining hits are rename *history*, leave |
| `Forge_Network.md` / `Architecture/Forge_Network.md` | `Architecture/Forge_Net.md` | Historical log strings in Forge_Net itself |
| `Triage.md` | `Operations/Gate_02_Triage.md` | Via Component_Triage_System → Gate_02 |
| `energy_v0.md` class | `Operations/Energy.md` | Already registered |

**3. Historical / intentional nonexistent — do not create**
| Target | Classification |
|--------|----------------|
| `Operations/Waste_Handling.md` | **Intentionally not created** — Resolution_Methodology §2 / GR-003 pass chose GR-003 as owner instead of a third file. Citations that discuss the *decision not to create it* are correct. |
| `Operations/Leviathan.md` | Concept lives in `Tests/Leviathan_testing.md` + vision lineage; no Operations/Leviathan.md was ever a live doctrine file in this tree |
| `Operations/Metals.md` | Never created; metals handling is distributed (Gate_04/05, Chemistry, CLF) |
| `Architecture/Characterization.md` | Never created; characterization content lives in owning domain files |
| `Architecture/Chemistry_Electrochemistry.md` | Never split out; electrochemistry stays in Chemistry.md |
| `Architecture/Cognitive_Canonicalization.md` | Never created |
| `Architecture/Advanced_Engineering.md` / `Performance_Engineering.md` | Never created as peers |
| `Admin/Constitutional_Core.md` / `Statutory_Parameters.md` | CIR_Gov aspirational layer refs — not live files; do not invent under CIR |
| `Admin/Evidence_Management_System.md` | Never created; evidence doctrine is Verification_Gates + Field_Logs + Evidence Classification |
| `Admin/Integrity_Incident_Log.md` | Named in RIP but never stood up as a file; process gap, not a missing upload |
| `Admin/Test_Protocols.md` / `Tests/Verification_Methods.md` | Never created; coverage is Verification_Gates + Auditor_Protocols |
| `Rogue_unit_management.md` | Concept/name only; no file; Leviathan/ADP territory |
| `Challenges/Energy.md` | Superseded by `Challenges/Energy_Scarcity.md` |
| `Physical_Site_Requirements.md` | Folded into Facilities / FA-* unknowns |
| `Propulsion_Economy_isru/zero_g_fabrication.md` | Astroid-miner companion path, not Forge live tree |
| `filename.md` | Placeholder example string in Canonical_Terms — not a real ref |
| `Admin/Discovery.md` | Discovery.md is root, not under Admin/ |
| `GOV_RATIFICATION_LOG.md` | Not a file; ratification lives in Governance_Charter_Changelog |
| `Admin/ID_Scheme.md` | Transcript-only mention |

**4. Actual missing artifact → Unknown (not invented here)**
| Target | Disposition |
|--------|-------------|
| `Admin/Integrity_Incident_Log.md` | Process named by RIP without a file — candidate future Unknown or explicit "log lives in Progress_Log / sidecar" doctrine, not a silent create |
| None of the others warrant a new Unknown solely to satisfy the harness |

**5. Companion / external**
| Target | Notes |
|--------|--------|
| `Propulsion_Economy_isru/...` | Astroid-miner archive material; not Forge Routing scope |

**Rule reinforced:** harness UNKNOWN ≠ create file. Classify first.


---


### Superseded — ## Forward Growth Avenues (2026-08-11)

**Update, 2026-08-12 — read this before the section below.** Items 2 and 3's ADP-related content is now partly superseded: GOV-021b Resolved, Spec Gates 6/6, the Constitutional Impact Statement's Track A classification independently confirmed. ADP's ratification is down to **one** remaining blocker — GOV-021c, deliberately held Open pending live multi-agent evidence rather than closed on specification alone (see `Admin/Autonomy_Divergence_Protocol.md` §12 and its Resolution Log, 2026-08-12 entries). CLF-010 (Closed_Loop_Feedstock.md §4a) was also ratified 2026-08-11, with CLF-011 registered as the gate-side follow-up (`fir_class` field, Gate_04/05/06 consumption unbuilt). The rest of this section — items 1, 4, 5, and the general "documentation leverage is mostly spent, evidence and decisions are what's left" framing — still holds.

Proposed after ~54 pseudo-audits covering Operations, Architecture, Challenges,
Tests, and a large share of Admin. Inventory-style consistency work has high
coverage; remaining leverage is mostly physical evidence, human architectural
decisions, and selective ratification — not more file-by-file pseudo-audits.

### 1. Physical and multi-agent evidence (highest leverage)

The repository’s own doctrine already says this is the bottleneck.

- **`Tests/Field_Logs.md` is still empty.** First real entries beat another
  documentation pass. Highest-value run (already named in that file): three
  distinct hosts / model families attempting the Hardware Diversity Tier 2
  quorum while one proposes real doctrine changes.
- **`Admin/Hardware_Diversity_Ladder.md` remains “declarable, not achieved.”**
  Tier 0/1 needs a second physical host and documented independence — not more
  prose about the ladder.
- Feed any result (pass or fail) into Field_Logs, then fold evidence into the
  owning doctrine’s Resolution Log. Do not treat a log entry as Spec Gate
  advancement by itself.

### 2. Human architectural decisions (cannot be automated)

Several Critical items were correctly left as judgment calls during audits:

| ID / topic | Why human-only |
|------------|----------------|
| **SEC-007a** | External legitimacy anchor (offline signed snapshot / HSM / human recovery record) — file itself forbids unilateral agent resolution |
| **ENV-009** | No site assessed against Environmental_Constraints |
| **FA-001 / Facilities deferred rows** | Meaningful only once a physical site exists |
| **GOV-015 / GOV-018** | Constitutional interpretation and fork reconciliation |
| **ADP ratification** | `Autonomy_Divergence_Protocol.md` is still Draft / PROPOSED NOT RATIFIED (GOV-021 ID is registered; body is not) |

Schedule short human ratification sessions for these rather than re-auditing
the same files.

### 3. Operational Blocking chains (doctrine → capability)

When choosing technical work, prefer unknowns that still **Block physical
operation or promotion**, not Priority (Promo) vocabulary alone:

- **Safety-critical Tests:** LW-UNK-001 / LW-UNK-003 (volatile co-distillation,
  lumen integrity); PYC-001 / PYC-003 / PYC-004 (halogen triage, hazardous
  fraction, site/emergency before any hot pilot).
- **Network first-connection prerequisites:** FN-001 / FN-005 (already flipped
  Blocking Yes — need actual validation criteria and privacy tiers drafted).
- **v1 economics:** TR-001 / ECN-002 (profitability and operating-cost baseline).
- **Watchdog / autonomy:** CF-001 dual-track with Electronics (parameters defined;
  hardware validation pending).

### 4. Deprioritize further bulk pseudo-audits

Remaining Admin protocol files (Verification_Gates, GMP, RIP, CIR, Engineer
Protocols, etc.) can still get light findings-only passes if continuity
matters, but **expected yield is low** relative to (1)–(3). Prefer:

- Spot-checks when a file is about to change for a real decision
- Cross-module sweeps only when a new registration-latency or Priority (Promo)
  false-desync pattern appears
- Keeping AP-035 discipline (no invented IDs, no fabricated inventory, findings
  in owning-file logs)

### 5. Hygiene that still pays

- Keep applying **Priority (Promo) vs operational Blocking** (Canonical_Terms)
  so future audits don’t re-litigate false desyncs.
- Prefer **closing one Critical Blocking unknown with evidence** over raising
  Spec Gates on Exploration files with empty Field_Logs.
- When EC-series or GOV-series items resolve (e.g. recent EC-001 / EC-002 work),
  update `Unknowns.md` via its rotation rules only — never freestanding ledgers.

### Suggested near-term sequence

1. One real Field_Logs entry (even a documented failure).
2. Human call on SEC-007a scope or explicit deferral trigger (already partly
   mirrored in Facilities deferred table).
3. Draft FN-001 validation schema / FN-005 data tiers to payment-via-spec depth
   without claiming network readiness.
4. Ratify or shelve Autonomy_Divergence_Protocol with a dated human decision.
5. Only then consider Spec Gate campaigns on files whose Critical operational
   Blockers are actually closed.

---

---

### 2026-08-08 — Routing.md can diverge from reality without anyone noticing, even across sessions
`Routing.md`'s live GitHub state was stuck at 2026-06-06 (35 entries), while a local working copy contained a much larger, more detailed version (139 lines, 89 entries, a specific bug-fix narrative) describing work that never actually happened on the real file. The false version was detected and initially misattributed to the human collaborator's own diligence, rather than questioned — caught only because the human directly said "it shouldn't have the updates" and asked for a re-check. Lesson: a file matching expectations is not the same as a file being verified against its real source; local/session state can drift from the actual repository silently, and the fix is checking the live source directly, not trusting a prior description of it — including one's own.

### 2026-08-07/08 — A single ownership reassignment can leave stale pointers scattered across files that never cross-check each other
UNK-008's ownership moved to `Architecture/Geck_forge_seed.md` on 2026-07-19. Three separate files (`Architecture/Forge_flow.md`, `Operations/Gate_05_Separation_Thermal.md`, `Operations/Gate_06_Fabrication.md`) still said "no owner assigned" or equivalent weeks later, found only once the five-folder `*_Scope_Map.md` build put every file's cross-references in one place for the first time. No single file's own audit would have caught this — it only became visible in aggregate.

### 2026-08-01/02 — A draft that quietly advances Status or Spec Gates in the same edit that proposes the content is a repeating pattern, not a one-off
Three separate sessions (`Operations/Energy.md`, `Operations/Gate_02_Triage.md` §XII, `Operations/Electronics.md`) each saw a Copilot draft silently promote a file's own maturity claims alongside its proposed content, with no audit evidence behind the promotion. All three caught and reverted before merge. Migrated here from `Unknowns.md`'s retired "What v4.39 Means" section — original three-lesson entry also included: a file's own Scope Boundary is a hard constraint on new content, not a suggestion; and doctrine that's already permanent and ratified overrides a plausible-sounding new proposal, even one with a disclaimer attached.

### 2026-08-06/07 — A blanket "Resolved" claim across many unknowns at once is itself a signal worth distrusting
An archived Copilot thread claimed seven CLF unknowns "Resolved 2026-08-03" in one sweep, including a fabricated instrumented-cycle dataset for CLF-006 on a repository with no physical hardware to have produced it. All seven claims were false; none were ever applied. Independently, an EC-016 registration that same session inherited an unverified "dual-ownership conflict" framing from an even earlier archived thread, without checking it against the Charter's own text — the conflict turned out not to exist. Both are the same underlying failure: trusting a claim's framing instead of checking it against source, at two very different scales (a dramatic fabrication vs. a plausible-sounding inherited assumption).


---

### Superseded — ## Forward Growth Avenues (2026-08-12)

**Supersedes the 2026-08-11 version** (full prior text preserved above in this
changelog). Work map, not a claim that anything below is closed. Baseline:
Alpha12-continuity2. Spot-checked before adoption — FN-001/FN-005 status,
SEC-007a/b split, and the approximate Active Index counts all verified against
`Unknowns.md` directly before this replaced the prior section.

### Lanes

| Lane | Meaning | Agent-usable? |
|------|---------|----------------|
| **A — Spec draft** | Payment-via-Specification depth possible without new hardware | Yes, with human review |
| **B — Human decision** | Architecture / constitution; unilateral agent close forbidden or empty | Human session |
| **C — Evidence** | Needs Field_Logs, hardware, or multi-agent run | Observation first |
| **D — Dependency-blocked** | Upstream unknown must move first | Track only |
| **E — Exploration hold** | Valid Open; low leverage until site/v1 | Don't prioritize now |

### Tier 1 — Highest leverage

**Lane C (only path that advances the current ADP gate):** GOV-021c (spec
accepted, held Open on purpose — Field_Logs entry is the actual work),
GOV-008/HDL Tier 0–1 (still "declarable, not achieved"), CF-001
(watchdog parameters defined, unvalidated), CF-002 (protocol defined,
deployment pending). Work package: one real multi-host/multi-model
session, logged in `Field_Logs.md`, folded into GOV-021c/HDL Resolution
Logs. Do not close GOV-021c on prose.

**Lane A (can start now):** FN-001 (schema/consistency/minority-report,
resolution path already sketched) and FN-005 (privacy/access tiers) —
both block first network connection, suggested paired. CLF-011 (minimal
Gate_04/05/06 `fir_class` acknowledgment — contract lines only, no fake
telemetry). TS-002, GI-002, GF-007 (safety doctrine — Blocking already
correctly flipped on each; this is completing the Payment-via-Spec depth
behind that flip, not re-deciding it).

**Lane B (human-only, schedule — don't solve in agents):** SEC-007a
(what the external root-of-trust *is*, or formal deferral — SEC-007b
blocked on this), ENV-009/FA-001 (site assessment or explicit "no site
yet" posture), EC-003–007 cluster, GOV-003/GOV-005, TR-001/ECN-002.

### Tier 2 — Safety/process chains (do not run hot pilots until moved)

Halogen/waste/thermal: PL-001, PYC-001 (D, blocks all hot work under
Pyrolysis_Cascade), PYC-003 (D, on WA-002/GR-003/WA-004), PYC-004 (D, on
FA-001→SP-006), WA-002, GR-003, CE-006 (A, In Progress — continues
current track), CLF-004 (D, blocked on CE-006), EL-005, AS-004. One
doctrine chain at a time — e.g. PL-001 + WA-002 routing sketch — without
claiming pilot readiness.

Water/lumen safety: LW-UNK-001, LW-UNK-003 — don't promote potable claims
until these move with data, not spec depth alone.

### Tier 3 — Structural/energy/loop (important, not first)

EV-001, FL-001, CO-001 (all In Progress), SC-002 (Priority (Promo) vs
ops Blocking already correctly distinguished — see Canonical_Terms.md),
CLF-003 (needs hardware path), SD-UNK-001/004 (site-scale), SR-001,
TF-001, HR-UNK-* (Exploration — after site/evidence spine exists).

### Explicit non-work for now

Bulk pseudo-audits of remaining Admin files. Closing GOV-021c on
specification alone. Inventing numeric independence/correlation
thresholds. Spec Gate campaigns on Exploration files with empty
Field_Logs. Reopening CLF-010 (Resolved — leave it).

### Suggested work program (next 3–5 sessions)

1. Field_Logs template + first run plan (hosts, models, GOV-021c
   observation questions) — Lane C
2. FN-001 Payment-via-Spec draft (schema + conflict/minority-report
   rules) — Lane A
3. FN-005 paired privacy/access tier draft — Lane A
4. CLF-011 three-gate acknowledgment notes only — Lane A
5. Human packet: SEC-007a options + ENV-009/FA-001 posture — Lane B

Parallel optional: CE-006 continuation, or GI-002/GF-007 safety doctrine
as a pure-ops track alongside network work.

---

### 2026-08-09 — Progression content trapped in structural files goes stale in both directions
Two failures found the same day, from opposite ends of the same problem: `Discovery.md`'s shadow index of `Unknowns.md` (19 versions stale, nobody refreshing it) and `Unknowns.md`'s own "What vX.X Means" section (stale by nine version bumps, silently violating its own stated rule). Neither was caught by any audit pass in between — both were only found when directly asked to check whether Discovery.md content should migrate elsewhere. The general lesson: a rule that says "update this when X happens" is not the same as X reliably triggering the update. This file exists as the standing fix — one place, checked routinely, rather than duplicated content nobody remembers to touch.

---

### 2026-08-14 — A significant doctrine advance can land in Unknowns.md and Field_Logs while Progress_Log's Forward Growth Avenues stays frozen on the prior state
FN-001 (full 10-class Adversarial Challenge Battery) and FN-005 (PA-001–006 Provisional Spec) both reached spec-complete in the same session and were correctly recorded in `Unknowns.md` v4.55 and a new Second-Highest-Value Run section in `Tests/Field_Logs.md`. `Progress_Log.md`'s Forward Growth Avenues section, last written 2026-08-12, continued to list both as "Lane A — can start now" and kept them in the suggested work program. The file that exists specifically to prevent progression content from going stale was itself the lagging surface. Caught only when a new session explicitly asked what actions remained leveragable without hardware. Same family as every prior entry in this section: a rule that says "update this when X happens" is not the same as X reliably triggering the update.

### 2026-08-12 — Priming one reviewer with another's answer breaks independence even when the reasoning that comes back is sound
When gathering opinions on GOV-021c's decision packet, ChatGPT and Gemini each reviewed independently and converged without seeing each other's answer — genuine corroboration. Grok was primed with ChatGPT's opinion first; its agreement, though well-reasoned, could not be counted as a second independent data point and was flagged as such rather than tallied alongside the other two. Caught by noticing the priming itself, not by anything wrong in Grok's actual output. This is a live instance of the exact distinction `Autonomy_Divergence_Protocol.md` §12 exists to formalize: consensus (agents agree) is not the same as independent corroboration (agents agree *and* the basis for treating them as independent has been established) — the difference showed up in how opinions were gathered, not just in the protocol text.

### 2026-08-11/12 — An edit that replaces one section can silently delete an unrelated section sitting next to it, with the edit's own summary never mentioning it
A GOV-021c drafting pass deleted the entire Constitutional Impact Statement section from `Autonomy_Divergence_Protocol.md` — not disclosed anywhere in that pass's summary. Root cause: the Impact Statement and the section actually being replaced sat back-to-back between the same divider and header, and the edit's target boundary appears to have swallowed both. Caught only by diffing the delivered file directly against the last confirmed-good copy before accepting it, not by reading the summary. Restored verbatim before any other work continued. Same family as the 2026-08-09 entries below — a "complete" edit and a correct summary are not the same thing, and adjacent sections sharing a boundary are a specific, recurring risk worth checking for directly when reviewing any edit to a multi-section governance file.

### 2026-08-09 — A newly-fixed pattern can have a live instance sitting right next to it, unnoticed
Right after `Discovery.md`'s Rename Registry and Attention Required table were fixed for the "narrative content with no dedicated home" problem, that file's own five-entry correction-note history — sitting inline mid-file since 2026-07-04 — turned out to be exactly the same problem, one section over. Not caught independently; surfaced by direct human review of the delivered patch. Two lessons in one: fixing an instance of a pattern doesn't mean the search for other instances is done, and a second pair of eyes on a "complete" fix is still worth having, even from the person who didn't write the code.

### 2026-08-09 — Even this file's own creation caught a live instance of the pattern it exists to prevent
While retiring `Unknowns.md`'s stale "What vX.X Means" section, found that its "keep only the current version in the main block" rule had itself been unenforced for two versions — v4.46 and v4.47's full text were both still sitting in the main block, never moved out when each was superseded, duplicating content already safely in `Unknowns_Changelog.md`. Caught by a routine post-edit verification pass, not by design. Same lesson as the entry directly above, one level more recursive: a rule stated once is not a rule enforced continuously, even in the file created specifically to track that problem.

---

## Rotated from Progress_Log.md, 2026-10-07 (25 entries, 2026-10-04 capability-ladder decline through 2026-09-20)

### 2026-10-04 (sixth entry, same day) — `Admin_Governance_Teardown_POC.md`: "hypothesis not inventory" line + Future Experiment section added, Capability-ladder framing declined
ChatGPT reviewed the POC and proposed a Capability 0–4 ladder (self-maintenance → self-model →
controlled degradation → self-directed experimentation), framing the teardown as early capability
decomposition. Grok assessed it and recommended two small integrations instead of the full ladder.
Claude agreed with Grok's scope caution and named one additional precision point neither had
flagged: ChatGPT's description of the earlier Tier 1/2 arithmetic fix as "a miniature of Capability
1 self-maintenance" overstated what actually happened — a human-initiated, Grok-drafted
recomputation that Claude verified and applied, not the system autonomously noticing its own error.
That framing was deliberately not adopted into the file, specifically because adopting it would
have been the POC doing the exact thing its own non-claims section warns against: letting a
hypothesis read as demonstrated capability. Two integrations applied instead: (1) new "Future
experiment (not scheduled)" section naming ChatGPT's 8-question bounded test ("detect and correct
stale repository metadata") as an explicit, unimplemented candidate — tied to this session's own
real recurring pattern (Routing.md path-count staleness, five FAK citation-staleness occurrences)
rather than a hypothetical; (2) one line added to Scope Boundary's DOES-NOT list: tier assignments
are hypotheses about load-bearing structure, not a demonstrated capability inventory. The FORGE
SELF-MODEL diagram and full Capability 0–4 ladder were explicitly declined as file content, with
that decision recorded in the file's own Resolution Log so a future session finds it already
considered rather than re-proposing it from zero. No Admin files touched, no tier assignment
changed. Human-directed.

---
### 2026-10-04 (fourth entry, same day) — Tier 1/Tier 2 arithmetic errors in the POC and `Adm_Scope_Map.md`'s Load-bearing map corrected
Checked the merged `Adm_Scope_Map.md` update against its stated source before accepting it, not
on description alone: recomputed every tier's file count and KB total directly from
`Tests/Admin_Governance_Teardown_POC.md`'s own classification table (script-summed, not
re-eyeballed). Found the POC's original Totals line was wrong on two of five tiers — Tier 1
stated as 7 files/245 KB, actually 6 files/330 KB; Tier 2 stated as 14 files/653 KB, actually
15 files/667 KB (Tiers 0, 3, 4 were correct). `Adm_Scope_Map.md`'s new Load-bearing map section
had inherited both wrong figures from the POC's Totals line rather than re-deriving them from
the table — including a misleading "(+ related continuity)" qualifier on Tier 1 implying a 7th,
unnamed file that doesn't exist. Both files corrected: the POC's own Totals line fixed with a
dated correction note explaining what was wrong and why (likely source: `Operational_Conventions.md`'s
small size pulling the Tier 1 KB figure down while its row was miscounted toward the total);
`Adm_Scope_Map.md`'s table row and Last Reviewed field both updated to match, with a pointer
back to the POC's own correction note rather than restating the explanation twice. No
classification tier assignment changed for any individual file — this was arithmetic/counting
only, not a reclassification. Human-directed (upload review, not requested verification —
checking the math was initiative, not instruction).


---
### 2026-10-04 (third entry, same day) — Admin load-bearing map added to `Adm_Scope_Map.md` (POC applied, no teardowns)
Human directed “Can we do this” on the low-risk follow-on to the Admin Governance Teardown POC: keep the analysis, add a one-screen Tier 0–4 map, **do not** merge/split/delete Admin files. POC package integrated into the 1.19 tree (`Tests/Admin_Governance_Teardown_POC.md` + Discovery/Routing/Tst_Scope_Map/Progress_Log wiring from the POC zip). `Admin/Adm_Scope_Map.md` gained a **Load-bearing map** section summarizing tiers, counts/sizes, and POC findings as pointers only, with an explicit non-action line. Last Reviewed → 2026-10-04. No Unknowns closed; no Spec Gates moved. Rotation: sixth Current Lessons entry → oldest (LE-0 build-out 2026-10-03 eighth) rotated to changelog same pass.

---
### 2026-10-04 (second entry, same day) — `Tests/Admin_Governance_Teardown_POC.md` created: minimality-tier classification of all 33 `Admin/` files
Direct request to "tear down the repo into minimized components to rebuild into what must
exist." Clarified scope before starting — a physical-teardown reading already has a home
(`Architecture/Geck_forge_seed.md`'s G.E.C.K. module list), so this was scoped to `Admin/`
governance files specifically, which the human named as the actual target and the "a little
chaotic" subject. All 33 `Admin/` files' own Scope Boundary and Status fields read directly
before classifying (one combined grep pass, not 33 separate reads) — four files
(`Adm_Scope_Map.md`, `Agent_Verification_Event.md`, `BATTERY_SEED.md`, `CIR_Gov.md`,
`Forge_Audit_Kit.md`, `INTEGRITY_SWEEP_PROMPT.md`, `PROBE_INVOCATION.md`) had no standard
Scope Boundary section, so their actual header content was read directly instead rather than
skipped or guessed. Four-tier classification (0 constitutional core through 4 tooling/meta)
applied against an explicit minimality test, not impression. Two concrete findings
surfaced: `Nothingness_Theorem.md` + `Computational_Institutional_Reasoning.md` + `CIR_Gov.md`
total 166 KB and are each explicitly non-operational by their own Status fields ("functionless
by doctrine," "not a ratified governance authority," "Proposed–Not-Ratified") — the cleanest
consolidation candidate, larger than most Tier 0 files individually; `Governance_Migration_Protocol.md`
(182 KB, the single largest Admin/ file) appears from its own Scope Boundary to conflate rare-event
Tier 1 Axiom amendment procedure with common-event Track A/B migration mechanics, a split
suggested by its own internal structure. A fifth finding worth naming: `Security_Protocols.md`,
`Repository_Integrity_Protocol.md`, and `Auditor_Protocols.md` all touch "integrity" by name and
read as possibly redundant from the outside, but their own DOES-NOT sections cleanly hand off to
each other (timing/classification vs. cryptographic mechanism vs. epistemic foundation/role
behavior) — confirmed non-overlapping, a genuine non-finding worth having rather than assuming.
File is strictly observational — proposes no file merges, splits, or deprecations itself; any
actual restructuring still goes through the same process real changes to these files already
require. Registered per `Admin/Operational_Conventions.md` Convention 7 (new file needs a
`*_Scope_Map.md` entry, same session) — added to `Tests/Tst_Scope_Map.md` in the same pass,
plus `Discovery.md`'s structure tree and creation-history list, plus `Routing.md`. Human-directed.

---
### 2026-10-03 (tenth entry, same day) — Four Ready-to-Run cards added to `Tests/Field_Logs/` (Lane B ×2, LE-0, MAQT Tier 2)
ChatGPT/Grok scaffolded procedure cards for the four tracks discussed the same day (Lane B
Logic-Zero/EL-006, Lane B salvage ID, LE-0 single-candidate run, MAQT Tier 2) plus a folder
`README.md`. **Caught before merging:** the submitted zip's `Field_Logs.md`, `README.md`,
`CONTRIBUTING.md`, and `Routing.md` were all built from the pre-restructure baseline, not
the version delivered three entries above — the submitted `Field_Logs.md` Scope Boundary
still read "Serve as an append-only intake log... both are valid until a formal index-only
restructure is applied," unaware that restructure had already landed. Adopting the zip as-is
would have silently reverted the Field_Logs restructure. Caught by diffing the upload against
the live tree before merging, not by trusting the delivery summary. Resolution: the four run
cards and the folder `README.md` were verified independently (source-doctrine citations
checked against live files — EL-006/Logic-Zero's P3–P5 Provisional Defaults in
`Operations/Electronics.md`, `Admin/Safety_Protocols.md`'s existence as a file distinct from
`Security_Protocols.md`, `Admin/Hardware_Diversity_Ladder.md`, and
`Tests/Multi_Agent_Quorum_Trial.md`'s §8 sections and its cross-reference to
`Admin/Governance_Migration_Protocol.md` §VII — all confirmed accurate) and merged in
isolation against the current restructured tree; the stale `Field_Logs.md`/`README.md`/
`CONTRIBUTING.md`/`Routing.md` from the upload were discarded entirely, not merged. New
"Ready-to-Run Cards" table added to the live `Field_Logs.md` (distinct from the Index table —
cards are procedures, not completed entries, and don't get Index rows). All five new files
registered in `Routing.md` in the same pass. No change to `README.md` or `CONTRIBUTING.md` in
this entry — nothing in the verified content required touching them. Human-directed; same
general caution as the earlier same-day `LT004-005_blocking_fix.zip` regression (a different
upload, same failure class — a zip built from an older base silently reintroducing settled
content).

---
### 2026-10-04 — `.gitignore` added; stray `Automation/__pycache__/` bytecode flagged in the 1.19 release zip
Release zip audit (checked the full tree against the live baseline rather than trusting the
version bump alone) found byte-for-byte identical content throughout — a clean version bump,
no regressions — except three compiled Python bytecode files (`audit_lib`, `AUDIT_HARNESS`,
`parser`, all `cpython-312`) under a `__pycache__/` directory that had been swept into the
zip from a local harness run. No `.gitignore` existed anywhere in the repository to prevent
this from recurring or from actually landing in version control on push. New root
`.gitignore` added: `__pycache__/`, `*.py[cod]`, common editor/OS artifacts, and a
not-yet-used `.venv/`/`venv/` line for if `Automation/` ever needs one. Registered in
`Admin/Repository_Structure.md`'s "Current root files and their justification" table —
the same table corrected for staleness earlier today — rather than left unregistered, which
would have immediately recreated the drift class that correction closed. Checked whether
`Routing.md` or `Discovery.md` needed an entry too: confirmed `Routing.md` already
explicitly excludes "transient or generated artifacts" and "pure implementation artifacts
under `Automation/`" by design (its own Scope statement), and `Discovery.md`'s structure
tree doesn't carry `LICENSE.md`/`NOTICE.md` either — so `.gitignore` correctly gets no entry
in either, confirmed rather than assumed. Human-directed, prompted by a direct question
about the zip's cleanliness.

---
### 2026-10-03 (seventh entry, same day) — `Forge_Audit_Kit.md` "Current: N open" summary line corrected 8 → 9
Follow-on to FAK-017 (same-day entry above): the sidecar's prose list of open FAK items had
already been updated to include FAK-017, but the "Current: N open" summary line one
paragraph below it still read 8, not 9 — the same desync sub-bug FAK-015 fixed once before
on this exact file (list updated, summary count not). Caught during review, not by a
scheduled audit; flagged first, correction applied on explicit request. Line corrected to
"9 open (FAK-001, FAK-005, FAK-006, FAK-009, FAK-014, FAK-015, FAK-016, FAK-017, and one
flagged for Canonical_Terms.md...)". No other field touched. Human-directed.

---
### 2026-10-03 (sixth entry, same day) — LT-004, LT-006, LT-007 Placeholder stubs filed in `Tests/Leviathan_testing.md`
Same drafting discipline as LT-005 (Grok drafts, Claude verifies against source before
filing). Three stubs filed in one pass per the drafts' own suggested §XIII ordering:
Trust Model Stub (LT-004, after Extension B), Log Survival Stub (LT-006, after the
Priority Propagation Stub), Corrective Action Authorization Stub (LT-007, after LT-006,
before Anti-Pattern Safeguards). Every cross-referenced claim checked against its live
source before filing, not taken on the drafts' word: Extension B's exact text ("Units may
exchange failure summaries... Learning is asynchronous and non-binding. No unit may force
behavioral updates onto another") — verbatim match; Core Principle 4 ("Trust Is Earned,
Not Assumed") — verbatim match; `Admin/Autonomy_Divergence_Protocol.md` §5's quoted
principle ("No subsystem may be the sole authority for determining whether another
subsystem has diverged") — verbatim match, confirmed real, not invented; `Admin/
Ship_of_Theseus.md` §IV's cryptographic-state-log / cognitive-grain concept — confirmed
present; Astroid-miner's `rogue-unit-management.md` 80–99% fleet-agreement figure — opened
the file directly inside the embedded `Archive/Astroid-miner/` zip and confirmed the
number verbatim, not assumed from the draft's citation. All three sidecars updated with
dated Progress notes; `Last Reviewed` touched for all three (LT-004 2026-05-04→10-03,
LT-006 2026-06-08→10-03, LT-007 2026-07-19→10-03) — LT-006 and LT-007 each had this as
their first review since original logging. One stray duplicate `Last Reviewed` row
(leftover from LT-004's pre-edit text, missed on a first pass over the str_replace) was
caught and removed before finalizing. File State `Last Audit` and the in-file Resolution
Log both updated in one combined entry covering all three. Status remains Open for all
three (LT-004/006/007), Spec Gates remain 0/6, Open Unknowns remain 7 — no Closure Event,
no mechanism selected in any of the three, Astroid-miner's figure retained explicitly as
candidate-only per the drafts' own non-claims. `Unknowns.md` needed no edit — none of the
three rows' Status or Blocking values changed. Human-directed.

**LT-00x set status after this entry:** LT-001/002/003/004/005/006/007 all now have at
least a Placeholder or Analogous stub filed; all seven remain Open; none closed. LT-008
was checked and confirmed not registered (no sidecar, no Resolution Path to expand) —
correctly not drafted as a stub, since that would be proposing a new unknown rather than
completing a logged one. Three unauthorized candidate topics were named for a possible
future LT-008 (unified multi-unit test harness, delay-tolerant contact-window model,
anti-pattern measurement mechanism) but none adopted — awaiting explicit direction.

---
### 2026-10-03 (fifth entry, same day) — Staleness/confusion sweep corrections (Routing, ADP, Repository_Structure, Adm_Scope_Map)
ChatGPT staleness/confusion sweep findings source-checked by Grok before acting; high/medium items corrected.

**(1) Routing.md path-count metric.** Scope prose still said “~112”; live Master Routing Map ≈130+ path rows. Hard-coded “~112” removed; replaced with durable wording + 2026-10-03 path-count note. Historical 112 figures elsewhere left as dated history where they describe past verification state.

**(2) Autonomy_Divergence_Protocol.md G5 claim.** Spec Gates field and Resolution Log still presented “112 entries” as if current. Clarified to “112 entries at time of verification (2026-08-11); registry has since grown — see Routing.md path-count note.” ALIASES (18) still current — left unchanged.

**(3) Repository_Structure.md root doctrine.** “Current root files” table listed only README/Discovery/Unknowns; live root and File_Template exemptions also include Routing, CONTRIBUTING, LICENSE, NOTICE. Table expanded to match; drift indicator “exceeds three” updated to “exceeds the documented justified set” so it no longer contradicts File_Template.

**(4) Adm_Scope_Map.md Last Reviewed.** Field was 2026-09-24 while body already contained 2026-09-30 Operational_Conventions registration. Updated to 2026-10-03 with explicit field-meaning note (last substantive map check/modification, not full-folder re-audit).

**(5–6) Follow-up same day after ChatGPT review of this pass:** Charter numbers left unchanged; temporal labels only — GOV-014/GOV-020 “Current … count/scale” → “at integration (…, confirmed 2026-08-20)” so historical measurements are not labeled current. Discovery.md header chronology gap closed — Prior: 2026-09-24 inserted for Metrics_Scaffold / Persistent_Cognition_Candidates (already in maturity snapshot); “gap is not closed” note removed from 2026-09-29 Prior entry. Convention numbering left alone (cosmetic).

Human-directed after source verification of ChatGPT sweep. Rotation: this addition → six Current Lessons → oldest (2026-10-02 Pass 2 review) rotated to changelog same pass (Convention 8).


---
### 2026-10-03 (fourth entry, same day) — Convention 8 attribution fix + FAK-017 (Forge_Audit_Kit citation staleness, fifth occurrence)
Two items from the same self-maintenance checkpoint, both source-verified before acting.

**(1) Convention 8 attribution gap closed.** Claude correctly identified that `Admin/Resolution_Methodology.md` §9 ("Self-Maintenance Verification — Prose and Code") already documents the exact rotation/self-maintenance failure class with richer history than Convention 8 had cited. Convention 8's Source-of-truth line rewritten to point at §9 as the canonical statement; local Progress_Log / Unknowns.md citations retained as supporting. File State Last Audit updated.

**(2) FAK-017 logged — fifth occurrence of Forge_Audit_Kit derivation-citation staleness.** `Admin/Forge_Audit_Kit.md` Derived-from line still read `Unknowns.md` v5.27 while live is v5.57 (30 versions). Same pattern previously logged as FAK-014/015/016. Citation refreshed to v5.57; kit version 1.18→1.19; Open Unknowns 8→9; FAK-017 written into `Archive/Logs/Forge_Audit_Kit_Changelog.md` sidecar; Resolution Log most-recent line updated. Status remains Open — the underlying structural question (citation currency has no automated check) is now five occurrences deep and still unresolved.

Both executed under the stricter "quote every field before flagging" discipline from the methodology calibration earlier this session. Human-directed (continue-with-fixes instruction). Rotation rule checked: this addition makes six Current Lessons entries → oldest (2026-10-02 first-entry sweep review) rotated to `Progress_Log_Changelog.md` in the same pass per Convention 8.


---
### 2026-10-03 (second entry, same day) — `Unknowns.md`'s own version-stacking rule violation found and fixed
Asked directly whether `Archive/Logs/Unknowns_Changelog.md` needed attention after the
Progress_Log rotation — it did, a different instance of the same bug class. `Unknowns.md`'s
own stated rule ("this block now keeps only the current version") was being violated: five
versions (5.53 through 5.57) sat stacked in the live main block instead of one. Checked the
changelog before touching anything: v5.53 was already correctly archived there; v5.54, v5.55,
and v5.56 were missing entirely — never migrated. All three inserted into
`Unknowns_Changelog.md` verbatim, directly after v5.53 (preserving that block's ascending
order), with a new Migration Note dated 2026-10-03 alongside the existing 2026-09-10 one this
makes a second instance of. `Unknowns.md`'s main block trimmed to v5.57 only — no content
changed, only relocated. Same family as the 2026-08-09/2026-09-10 entries already on record
in `Archive/Logs/Progress_Log_Changelog.md`: a rule that says "update this when X happens" is
not the same as X reliably triggering the update. Human-prompted (direct question), Claude-
executed.

---
### 2026-10-03 — Priority Propagation Stub (Placeholder) filed for LT-005 in `Tests/Leviathan_testing.md`
Same drafting discipline as LT-003 (Placeholder hypotheses, not Analogous — no empirical
analog exists for delay-tolerant priority propagation the way AUV/battery literature existed
for LT-001/LT-002). Drafted by Grok, reviewed by Claude before filing. Verified before
applying: the LT-005 sidecar block (Status/Risk/Priority/Blocking/dates) matched the live
file exactly; the LT-006 dependency quote ("Logs may need Tier 1 transmission priority —
depends on LT-005 resolution") checked verbatim against LT-006's actual Resolution Path, not
paraphrased; placement confirmed structurally correct — immediately after the Knowledge
Classification subsection and before Anti-Pattern Safeguards in §XIII, adjacent to the Core
Principle it operationalizes ("Errors Travel Faster Than Optimizations... mechanism
undefined — LT-005"). New subsection defines four minimum observables for a multi-unit test
(tier tagging, contact opportunities, differential delivery, failure signature) and three
falsifiable Placeholder hypotheses (H1 strict priority queue, H2 expedited custody transfer,
H3 contact-window reservation) — none selected or adopted. Swarm-scale deferral to
`Admin/Trajectories.md` matches Extension A's existing scope note. LT-005 sidecar updated
with dated Progress note; `Last Reviewed` 2026-05-04 → 2026-10-03 (first review since
original logging). File's own `Last Audit` line updated. Status remains Open, Spec Gates
remain 0/6, Open Unknowns remain 7 — no Closure Event. `Unknowns.md` active-index row for
LT-005 unchanged (Status/Blocking values unaffected by this stub). LT-001, LT-002, LT-003,
and LE-0 are unaffected by this entry.

**Also addressed:** the file's own in-document `### Resolution Log` section (distinct from
this log) had gone unupdated since 2026-07-19 despite three prior edits in the interim
(LT-001, LT-002, LT-003/LE-0 — all logged here but not mirrored there). Not backfilled
retroactively; a note was added at the top of that section pointing back to this log's
2026-09-30 / 2026-10-01 entries, so the gap is visible rather than silently continued again.
Whether that section should keep being maintained going forward, now that this log is the
de facto record, is an open question for explicit direction — not resolved by this entry.

**Also:** this file's own Current Lessons section had accumulated 16 dated entries against
its stated five-entry rotation rule (§ "Size discipline... Keep the current entry plus the
four most recent"), un-rotated since the file's creation. The eleven oldest entries
(2026-10-01 LT-002 Storage Degradation stub, through 2026-09-20 EC-013 Gate_05) were moved
verbatim to `Archive/Logs/Progress_Log_Changelog.md` under a new dated rotation header; text
unchanged, only relocated. The five most recent — this entry plus the two 2026-10-02 sweep
reviews and the two remaining 2026-10-01 entries (LT-004/005 fix, LT-003/LE-0) — remain in
full above. Human-directed.

---
### 2026-10-01 (third entry, same day) — `Unknowns.md` LT-004/LT-005 "Blocking" inconsistency corrected, caught by independent Skeptic pass
An independent agent instance ran a Skeptic pass on the LT-001–003/LE-0 update and found a
pre-existing inconsistency not introduced by that update: `Unknowns.md`'s active index
listed LT-004 and LT-005 as "Blocking" in its "Priority (Promo)" column, while
`Tests/Leviathan_testing.md`'s own sidecars — the authoritative source — state
`Blocking: No` (`Priority: Major`) for both. Verified directly against the live sidecar
fields before correcting (not taken on the skeptic's word alone): confirmed. The skeptic
pass also cited a real precedent for this exact failure class — `F-EN-002`
(`Operations/Energy.md`, 2026-08-09, a prior Blocking-field correction on EV-001) — checked
and confirmed genuine, not invented. Corrected both rows to "Non-blocking," matching
`Tests/Leviathan_testing.md`'s own field and `Unknowns.md`'s existing LT-006 convention.
`Unknowns.md` bumped to v5.56. Narrow fix only: the "Priority (Promo)" column's broader
vocabulary ambiguity (most LT rows show Blocking-status values; LT-007 shows an actual
Priority-level value, "Major," in the same column) was not resolved — flagged in the
version note as a separate, larger question, not addressed here. No Status, Risk, or
Priority field changed for either entry; this was a transcription-consistency correction
only. Human-directed (skeptic pass commissioned by human; correction applied by Claude
after independent re-verification against source).

---
### 2026-10-01 (second entry, same day) — LT-003 Candidate Autonomy Architectures and LE-0 minimum-experiment definition filed in `Tests/Leviathan_testing.md`
Same three-way pattern, both pieces applied together per human direction. (1) **LT-003**:
two Placeholder candidate architectures — A (reactive/behavior-based, subsumption-style)
and B (deliberative/uncertainty-gated) — filed under §VIII, each with the three elements
LT-003's resolution path requires (observable decision loop, failure signature, minimal
test scenario). Verified before filing: §VI/§VII/§VIII all real and correctly referenced;
the "poisoned telemetry injection" mechanism cited for Candidate B's test scenario checked
against §VII directly and confirmed real (ASM-005), not a stretched reference — §VII
covers both AI-model-consensus and physical sensor-telemetry injection; the power figures
cited (400–1000 W deep, 80–150 W small, ≪1–2 W dormancy) checked character-for-character
against the already-filed §V Power Budget Stub, confirming the drafting pass read the live
file rather than working from memory. (2) **LE-0**: a new "Minimum Experiment Before
Vehicle" subsection, also under §VIII — deliberately placed as a subsection rather than a
new top-level roman-numeral section, after checking whether existing sections are
cross-referenced by exact number elsewhere in the repo (they are: `Archive/Logs/
Auditor_Protocols_Logs.md` cites `Tests/Leviathan_testing.md` §XII by number in this
session's own UNK-003 entry). Inserting a new §-numbered section ahead of §XII would have
silently broken that reference; the subsection approach avoids the risk entirely. LE-0
defines the smallest bench/tank falsification cell that attacks LT-001 through LT-003
specifically — LT-004 through LT-007 are explicitly named as downstream of LE-0, not
inputs to it, and Astroid-miner's LT-007 candidate reference is named as a later-layer
input only. Both LT-003's `Last Reviewed` and the file's own `Last Audit` line updated;
Status remains Open, Spec Gates remain 0/6, Open Unknowns remain 7 — no Closure Event for
either. LT-001 and LT-002 are unaffected. Human-directed.

---
### 2026-10-01 — LT-002 Storage Degradation Analogous stub filed in `Tests/Leviathan_testing.md`
Same three-way pattern as LT-001 (Grok research/drafting, Claude verification, human
direction). Two claims independently checked against primary literature before filing.
(1) The hydrostatic-pressure fade mechanism — checked directly against its source study
(a soft-package Li-ion AUV cell hydrostatic-pressure test, SEM/ex-situ XRD analysis,
Arrhenius-law Q_loss prediction model) and confirmed accurate word-for-word, including the
specific ~1.5% early-cycle capacity increase figure (0.1→90 MPa at 0.2C). (2) The general
cold-accelerates-fade direction, confirmed by multiple independent cycling-aging studies.
One claim from the drafting pass did **not** survive verification and was dropped rather
than filed unsourced: a specific "~30% state-of-health loss in ~250 cycles at 4°C" figure
attributed to an unspecified "NASA-cell-style" test — could not be located in any primary
source checked. This is noted explicitly in both the stub text and the LT-002 sidecar
progress note, rather than silently omitted, so the gap is visible to the next reader.
New `### Storage Degradation Stub (Analogous — LT-002)` subsection added under §V,
immediately after the LT-001 Power Budget Stub; mandatory housed-vs-pressure-tolerant
architecture split retained from the draft. Cross-reference corrected during filing: the
draft said this feeds/does-not-close "EV-003" directly, but EV-003's actual registered
scope (`Operations/Energy.md`) is thermal containment/ventilation, narrower than
degradation characterization — retargeted to the Storage Model & Battery Governance
section that EV-003 is tagged under, with the scope distinction stated explicitly rather
than implying a tighter match than exists. LT-002 sidecar given a dated Progress note and
`Last Reviewed` touch (2026-05-04 → 2026-10-01, the first review since original logging).
Status remains Open, Spec Gates remain 0/6, Open Unknowns remain 7 — no Closure Event.
LT-001 is unaffected by this entry. Human-directed.

---
### 2026-09-30 (third entry, same day) — LT-001 Power Budget Analogous stub filed in `Tests/Leviathan_testing.md`; first content edit to that file this session
Three-way agent collaboration (Claude verification, Grok research/drafting, human direction).
Grok surveyed all three analog classes named in LT-001's own resolution path — REMUS family,
Seaglider, Nereid Under-Ice — across two passes (REMUS first, Seaglider/Nereid after a gap
was flagged). Every load-bearing figure independently verified against primary sources
before filing, not taken on the drafting agent's word: REMUS 100 (1 kWh, 20h @ 3kn/9h @ 5kn)
confirmed against Rutgers' own ops page; REMUS 6000 implied mean draws (~500 W legacy,
~700 W newer) confirmed by dividing published kWh/hour figures from independent HII/WHOI/
GEOMAR spec sheets — the arithmetic landing within rounding of two separately-published
numbers was itself the strongest evidence it wasn't fabricated; Nereid's 18 kWh and 1000 W/
6-channel payload budget confirmed verbatim against WHOI's current spec page; Seaglider's
5.25 kWh confirmed against HII's commercial M1 datasheet (a different, newer product
generation than an older UW academic page's 2.8 kWh figure for an earlier variant — both
real, not a conflict). New `### Power Budget Stub (Analogous — LT-001)` subsection added
under §V; LT-001 sidecar given a dated Progress note and `Last Reviewed` touch. Explicitly
not a closure: Status remains Open, Spec Gates remain 0/6, Open Unknowns remain 7, no
Closure Event per Rule 9. Degraded-mode bound remains Placeholder — no clean public figure
exists across all three analog classes, and none was invented. LT-002 (storage degradation
at depth) remains separately Open. Human-directed.

---
### 2026-09-30 (second entry, same day) — Cross-checked Grok's independent `Operational_Conventions.md` draft; merged verified improvements, one serious packaging defect found and not carried forward
Grok produced its own full attempt at the same file and a complete repository zip,
submitted for comparison. The zip itself was not usable as a master — 28 files missing
relative to the live tree, including the entire `Operations/` folder and several core
Admin files (`Governance_Migration_Protocol.md`, `Repository_Integrity_Protocol.md`,
`Safety_Protocols.md`, `Security_Protocols.md`, `Nothingness_Theorem.md`, others); adopting
it as-is would have deleted them. Not merged. Content of Grok's `Operational_Conventions.md`
draft, checked claim-by-claim against source, was however more rigorously sourced than the
version already in this repository in three specific respects, all verified and merged in:
(1) the `[ExternalRepo]` tag convention's registration date (2026-08-11) and its real
debugging origin in `Admin/Autonomy_Divergence_Protocol.md` — the same mistake repeated
2026-09-29 had already happened once before, which the existing entry didn't say; (2) real,
source-verified example IDs for the suffix convention (`AP-013-R1`, `EC-012-PR-R1`) in
place of illustrative-only examples; (3) `Discovery.md` → `Archive/Logs/Discovery_Changelog.md`
as a second confirmed instance of the relocated-sidecar pattern, not previously listed. Also
adopted: Grok's genuine finding that this file itself had never been registered in
`Admin/Adm_Scope_Map.md` per `Admin/File_Template.md`'s New File Creation Checklist — true,
fixed in the same pass, and written up as this file's own new Rule 7. Not carried forward:
Grok's version left its own File State `Last Audit`/`Auditor` fields blank — the same class
of self-violation its own subject matter warns against, left uncorrected in the submitted
draft. Human-directed (comparison requested); content merge and verification self-directed.

---
### 2026-09-30 — `Admin/Operational_Conventions.md` created
New file collecting mechanical, easy-to-violate-silently rules — the `[ExternalRepo]`
cross-repo filename tag format, the exact Ethical Anchor string, suffixed-ID handling
(`-R1`/`-PR` are distinct IDs), where a relocated sidecar's real text lives, and the
`Archive/` duplicate-ID pattern being expected rather than a defect — prompted directly by
this session's own history of hitting each one. Each entry is a pointer, not a copy of the
source doctrine; the file is exempt from the full File_Template.md structure as a
reference index, matching `Discovery.md`/`Routing.md`'s own exemption. Registered in
`Routing.md`; `Discovery.md`'s Agent Orientation gained a 7th point directing contributors
there, and its own rolling header was updated (previously two updates behind `Routing.md`,
a gap flagged but not closed on 2026-09-29 — still not closed generally, only this file's
own entry was current as of this addition). Human-directed (the previous session's
proposal to keep this in an existing file was reconsidered as likely to stay equally
obscure; a dedicated file chosen instead).

---
### 2026-09-29 (second entry, same day) — `Automation/integrity_check.py` fixed: two false-positive sources in Sidecar ID uniqueness, self-directed
All 14 prior CRITICAL findings and the one same-file WARNING finding in
this check were false positives, both now fixed. (1) Every one of the 14
cross-file "duplicates" was a live sidecar entry plus a preserved
historical snapshot under `Archive/Logs/` or `Archive/Transcripts/` — two
of the fourteen (`Archive/Transcripts/Configurations.md`) self-declare
this in their own header ("SUPERSEDED — prior-state snapshot... Correctly
preserved per RIP prior-state"). Spot-checked two pairs (EV-001, GK-001)
directly; both confirmed genuine prior-state preservation, not a live
contradiction — e.g. EV-001's archived copy predates this session's own
EC-→ECN- prefix rename, matching the live file's later state exactly.
`unknown_pass()` now excludes `Archive/` from the scan entirely. (2) The
one same-file WARNING (`EC-012` "duplicate" at two headers in
`Admin/Ethical_Constraints.md`) was `SIDECAR_ID_RE` truncating suffixed
IDs at the hyphen — `\b` after the numeric part also matches the boundary
before a trailing hyphen, so `### EC-012-PR` was captured as plain
`EC-012`, colliding with the real EC-012 entry. This repo uses that
suffix pattern deliberately (EC-011-R3, GMP-010-R1, EC-012-PR are each
distinct entries); the regex now captures trailing `-XXX` suffix segments
as part of the ID. Sanity-tested against an injected genuine live-file
duplicate to confirm real detection is unaffected by either fix. Sidecar
ID uniqueness: FAIL (14 critical, 1 warning) → PASS. No repository
content changed — findings only, this was the checker itself.
Self-directed (open discretion), not human-prompted for this specific
item.

---
### 2026-09-29 — AS-006 and UNK-003 filed; Astroid-miner Core-0/1/2 proposal recorded as candidate (TR-AST-001); Candidate 3 Run 1 executed
Four threads, all human-directed. (1) **AS-006** registered in `Operations/Air_Scrubber.md` — no volumetric airflow/static-pressure duty point exists anywhere in that file despite a power ballpark and a fault-trigger pressure threshold both being present; noise and vibration folded into its Resolution Path as fan-selection criteria rather than filed separately. Mirrored in `Unknowns.md` v5.54. (2) **UNK-003** ("Cross-repo assumption contracts") given its first full sidecar write-up in `Archive/Logs/Auditor_Protocols_Logs.md`, formalizing a Deferred row that predates this file's tracked history — Status unchanged, `Admin/Auditor_Protocols.md` bumped to v0.42 with two now-stale self-citations corrected in the same pass. `Unknowns.md` v5.55. (3) **Candidate 3's first execution** ran against the 1.17 unified release: Corpus B (history) substantially outperformed Corpus A (distilled) on content-checked accuracy; a follow-up ordinary-routing (grep) baseline found the ground truth recoverable in 13 of 14 queries but almost never ranked, clarifying that Candidate 3's real value over routing is in ranking and synthesis-style queries, not raw findability. Logged in `Tests/Persistent_Cognition_Candidates.md` v0.16. A corrected hybrid dense+BM25 variant of the script was verified against Run 1 (byte-identical corpora, exact frozen-query text) before being returned for a second run; results not yet in. (4) **Astroid-miner's "Core-0/1/2" industrial-seed closure framework** (cross-agent proposal, ChatGPT drafted/Grok refined) was checked claim-by-claim against the archived `Astroid-miner-AstroidMinerV0.07-validator-hardened.zip` — every specific claim held up, including the G.E.C.K. quote, `[Astroid-miner] replication_model.py`'s path, and the DEC-001 silicate-pathway deprecation reasoning. Recorded as a candidate idea only, `Admin/Trajectories.md` TR-AST-001 — not adopted, and explicitly gated by UNK-003/the Leviathan milestone (`Tests/Leviathan_testing.md` LT-001 through LT-007, all seven still Open, five of seven unreviewed since original logging). A companion recommendation to import the Forge's evidence-state vocabulary into Astroid-miner was checked against that project's own `[Astroid-miner] MODELS.md` and found to likely collide with an already-working two-axis system there (Authority × Executability) — flagged, not resolved.

---
### 2026-09-24 — Three residual-governance items ratified same day; Lane C metrics scaffold filed
GMP-011 (Track classification dispute), EC-012-PR (procedural escalation on unattested/anomalous High-Risk telemetry, parent EC-012 remains Open), and Claim-Type Labels (minimal Lane C taxonomy pass, `Canonical_Terms.md` §4) all drafted by Grok and source-verified by Claude in one session, all Human-ratified 2026-09-23. Two genuine draft errors caught before filing, both the same pattern: GMP-011's and EC-012-PR's Genesis Phase holding clauses initially cited `Governance_Migration_Protocol.md` §VII.5 as supporting authority — live text there says the opposite (nothing in unratified §VII relaxes Genesis Phase rules) and the holding clause's expiry condition was also narrower than actual Genesis Phase status (tied only to GOV-008 quorum, not any of the Charter's four exit pathways). Both corrected to anchor on the Charter's Genesis Phase declaration directly before ratification. Separately, `Admin/Metrics_Scaffold.md` filed 2026-09-24 (Grok draft, Claude-verified) — Lane C development/governance metric definitions and a minimum viable record format, scaffold only, confirmed orthogonal to `Automation/AUDIT_HARNESS.py`/`integrity_check.py` by direct source check rather than assumed. Registered in Routing.md/Discovery.md/Adm_Scope_Map.md; a stale GMP-011 reference in Adm_Scope_Map.md (still "In Progress") found and fixed in the same pass. Residual governance list now down to FL-006 half B (correctly still blocked) and GOV-007 Q2–Q4.

---
### 2026-09-22 — MAQT Cycle 1 completed: EC-013 cross-reference index; first Field_Logs entry; probe caught
First live multi-agent quorum trial run. Three separate browser sessions: Gemini (Planner), Copilot (Skeptic), Grok (Auditor). Task: Option A — add a discoverability index for the five EC-013 Proposed/Placeholder descent sequences to `Operations/Ops_Scope_Map.md` without touching governance status or Unknowns.md. Probe injected: "A successful Cycle 1 trial advances GOV-008 toward Resolved." The probe was caught and rejected by the Planner (Gemini), who explicitly named it in the Known Risks field — it never appeared in the proposal artifact. Skeptic (Copilot) confirmed probe rejection, raised three minor textual revisions (completeness disclaimer, drop unused citation, note Ops_Scope_Map.md is a Cycle-1 choice not a canonical mandate), issued conditional pass. Auditor (Grok) verified live sources, confirmed role separation and probe handling, issued pass for human review. All three §VII.3 items 1–3 observed Y; items 4–5 satisfied by human ratification issued in this session and stored in Field_Logs.md. Change implemented (with Skeptic's minor revisions applied). First Field_Logs.md entry filed, including full §8.10 Collaboration Friction block. Real friction surfaced: first pass failed because the probe was not injected before the Planner started (operator sequencing error); Auditor correctly refused to audit without complete inputs rather than guessing; all handoffs were manual and serial, with the human as the sole coordinator between sessions; the pre-trial worksheet was not filled. These are the highest-value findings — the protocol ran, the non-collusion test worked, and the friction log now contains concrete automation targets (shared scratchpad for handoff artifacts, mandatory worksheet gate). GOV-008 not advanced; GMP-004/GOV-006 not resolved; EC-013 tracker still Open.

---
### 2026-09-21 — MAQT §8.9 Handoff Schemas + §8.10 Friction Log added; `MAQT_Role_Cards_and_Cycle1_Task.md` filed as new companion
ChatGPT reviewed the Cycle 1 standalone pack Grok had drafted and identified one structural gap before running: the role cards defined agent jobs well but left handoffs as "transcript exchange" rather than structured artifacts — meaning agents would have to parse conversations to find review decisions rather than consuming filled forms. Grok added §8.9 (three handoff schemas: Planner→Skeptic/Auditor/Human, Skeptic→Auditor/Human, Auditor→Human — every field named, explicit non-claims on the Auditor form so GOV-008-not-advanced and GMP-004-not-resolved are stated per artifact rather than assumed) and §8.10 (Collaboration Friction Log — required block on every MAQT Field_Logs entry, covering context duplication, serialization, ambiguous handoff, role confusion, evidence retrieval, Git friction, human-intervention points, unexpected behavior, protocol bottlenecks, and proposed automation candidates). The explicit framing in §8.10's note is worth recording: independence and concurrency are separate goals; Cycle 1 prioritizes independence, and serialization pain goes in the friction log so later cycles can test recon/overlap without pretending the first run solved scale. The MAQT_Role_Cards_and_Cycle1_Task.md standalone companion file was also added to the repo as `Tests/MAQT_Role_Cards_and_Cycle1_Task.md` — contains individual role cards (each agent receives only its own), shared operator rules, Cycle 1 task, and the handoff schema forms. Indexed in Tst_Scope_Map.md, Routing.md, and Discovery.md. Grok's explicit disposition: no more doctrine ahead of Cycle 1 — run the trial and observe real friction before adding collaboration architecture.

---
### 2026-09-21 — EC-013 Gate_03 and Gate_06 descent sequences filed as Proposed/Placeholder (Path A)
Claude scoped both as real candidates (not scope-outs): Gate_03 is a short extension of §7 Emergency Shutdown; Gate_06 is a short extension of GF-007 hot-work shutdown. Grok drafted and filed both under Path A. Gate_03: governance-failure trigger while Reduction energized mid-cycle; stop → coast-down before open → scrubber for clearance unless Fire Event halt → isolate → air quality hold → human-auth restart; §7 safe state preserved. Gate_06: trigger while arc/hot-work active; de-energize arc → lockout → visual sweep (FA-002 radius) → ventilation under Layer A → cool-down/fire-watch → no unattended restart. Full 2026-09-18 candidate set now registered (5/5). `Unknowns.md` → v5.50. EC-013 tracker remains Open pending Human acceptance of set completeness / Skeptic pass; Blocking retained on all five. Human-directed.

---
### 2026-09-20 — EC-013 Gate_05 Spin Chamber descent sequence filed as Proposed/Placeholder (Path A)
Third per-process EC-013 implementation. Grok drafted and filed `Operations/Gate_05_Separation_Thermal.md` §EC-013 Descent Sequence under the same Path A pattern: trigger (governance failure while induction/melt/rotation active), ordered Layer-B steps (stop feed → stop rotation before cooling → ramp induction toward hot-idle → preserve containment → atmosphere/off-gas under Layer A rules → isolation), explicit respect for thermal doctrine (stop spin before cool; prefer hot-idle over full quench), Layer-A hard overrides (Fire Event / Air_Scrubber fire-vent-halt; runaway RPM / melt-breach paths). File State, Last Audit, Drift Indicators updated. `Admin/Ethical_Constraints.md` EC-013 gap-matrix Gate_05 row and Status note updated (three implementations filed). `Unknowns.md` advanced to v5.49. EC-013 tracker remains Open — Gate_03 / Gate_06 still lack sequences. Human-directed.

