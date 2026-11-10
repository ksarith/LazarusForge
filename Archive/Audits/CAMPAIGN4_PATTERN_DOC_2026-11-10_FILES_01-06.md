# CAMPAIGN4_PATTERN_DOC_2026-11-10_FILES_01-06.md

**Campaign 4 cross-file pattern document, files 01–06 (Auditor_Protocols, Ethical_Constraints, Governance_Charter, Verification_Gates, File_Template, Canonical_Terms). Due at the five-to-eight-file mark per the kickoff convention; deposited alongside artifact 06.** Findings-only per PKC-020: this document aggregates already-deposited findings, advances nothing, and proposes no disposition — each pattern's remedy is the human's to rule.

## Pattern 1 — The 90-day Aging Rule is tripped repository-wide (systemic; four instances, two control cases)

- Instances: Auditor_Protocols.md 8 of 10 open entries (CAMPAIGN4_AUDIT_01 F3); Ethical_Constraints.md 3 of 7 open plus one near-trip (AUDIT_02 F-EC-2); Governance_Charter.md 13 of 13, 102–171 days (AUDIT_03 F-CH-4); Canonical_Terms.md 9 of 10, 112–139 days (AUDIT_06 F-CT-2). Aggregate: 33 of 38 open sidecar entries across the four tripping files are past the 90-day bar; the youngest tripped entry is 112 days old.
- Control cases: Verification_Gates.md (zero open unknowns — the rule cannot fire) and File_Template.md (no sidecar — the rule cannot fire). Neither is evidence of compliance; both are structural exemptions.
- Shape: the rule is never violated by commission — every instance is omission. Repository doctrine correctly forbids auditors from advancing Last Reviewed without a substantive review (findings-only per PKC-020), but no standing pass ever performs those reviews: the only entries that get refreshed are those caught by dedicated review passes (e.g. the Grok resolution-path reviews in Operations/, 2026-08-14/15; the X3 ruling annotations of 2026-10-28). The result is a monotonic aging clock that no scheduled mechanism resets.
- Interaction with the Cycle definition (CT-011): the Aging Rule's 90-day bar is Auditor_Protocols doctrine, deliberately much shorter than the one-calendar-year Cycle; the two do not conflict, and the Aging Rule's arithmetic is unaffected by the Cycle definition's propagation.
- Consolidated remedy option (already flagged at kickoff and in AUDIT_01/02; re-presented here as one ruling, not four): either authorize a batch Last-Reviewed refresh pass (re-read each tripped entry against current body state, advance only on genuine review, per the Ship_of_Theseus 2026-10-28 precedent), or amend the rule's remedy (e.g. make the trip a review-scheduling trigger rather than a per-file WARNING), or accept the aging as honest. One ruling covers all four instances and every future one.

## Pattern 2 — Relocation-repair-miss class (four instances, one corroborating instance)

The 2026-10-29/31 relocations (MAINT-29/30/31, the `<Letter>Logs/` homes; the 2026-08-09 Rename Registry migration) were repaired by fixing the fields and pointers named in findings, but never by grepping the corpus for every remaining occurrence of the old home. Instances:

1. Governance_Charter.md 2026-10-31 fix pass: repointed three File State fields, missed all body occurrences (AUDIT_03 F-CH-2 — four dangling pointers).
2. The same class in the Charter sidecar's own annotation (AUDIT_03 F-CH-1 context).
3. File_Template.md Update Procedure step 3: still routes rotation history to pre-relocation homes, never mentions the split triggers or the new homes (AUDIT_05 F-FT-1) — an operator-following-the-procedure defect, the most consequential shape.
4. Canonical_Terms.md: three passages still name `Discovery.md` as the Rename Registry's home four months after the 2026-08-09 migration, against its own two correct citations of `Archive/Rename_Registry.md` (AUDIT_06 F-CT-1).
- Corroborating (outside sweep scope): `Automation/audit_lib.py`'s LEGACY finding message still says "check Rename Registry in Discovery.md" — the stale home is baked into tooling output agents read.
- Remedy option: one corpus-wide grep sweep for the pre-relocation home strings (`Archive/Logs/` as a live-pointer target, `Discovery.md` + "Rename Registry" co-occurrence, `*_Changelog.md` routing language in procedures), each hit either repointed with a dated note or ruled historical per PKC-007. This is a mechanical, batch-eligible repair.

## Pattern 3 — The GOV-022 missing-sidecar-record cluster (two MAJOR instances, one false verification record)

- AUDIT_03 F-CH-1 (MAJOR): GOV-022 has no sidecar record anywhere despite the Charter's File State claiming full Closure Events live in the sidecar Resolution Log.
- AUDIT_04 F-VG-1 (MAJOR): Progress_Log PKC-006's 2026-10-27 resolution record asserts the opposite ("every named closure event (…GOV-022) present with recorded Closure Events") and was git-verified false at both candidate states of the sidecar (`af611dcb` / `cad08771`: 21 GOV headings, zero GOV-022 occurrences).
- Shape: a record that never existed is attested twice — once by the owning file's File State, once by a verification record in a third file. The TWGW candidate flagged in AUDIT_04 (recorded verification contradicted by the named artifact) is the general class; this cluster is its load-bearing instance because GOV-022's resolution status is unknown.
- Remedy option: reconstruct from git history whether GOV-022 was ever resolved (the AUDIT_77-style provenance reconstruction used on Canonical_Terms' 0.13 bump is the in-corpus precedent), then either restore the Closure Event or correct the File State claim and the PKC-006 record with dated addenda.

## Pattern 4 — The self-application gap lineage (File_Template.md; fifth data point)

- Aggregate lineage A-F3 = B-N2 = C-N2 (Rule 5-verified 2026-11-07) plus AUDIT_05 F-FT-2 (fourth consecutive pass) and the Pattern-A facet (four substantive touches without migration). This document adds no new instance — File_Template was the fifth file examined and the gap held — but records that the lineage is now the campaign's longest-running single open item and that every remedy remains blocked on the same human ruling (add a self-exemption class, or migrate the file).

## Pattern 5 — Stale drift indicators and completion notes tracking resolved events (two instances)

- Ethical_Constraints.md F-EC-1: a drift indicator still reads "before EC-008 is resolved" for an unknown ratified 2026-08-22 (the EC-AUD-003 class recurrence).
- Canonical_Terms.md F-CT-4: a "history ends at v0.6" note contradicted by its own section's later blocks.
- Shape: wrapper text that conditions on an event keeps firing after the event. Distinct from Pattern 2 (wrong home) — this is wrong condition. Remedy option: batch-eligible; each fix is a dated deletion or rewording.

## Positive records worth preserving (the sweep's clean columns)

- Mirrored claims hold in both directions everywhere tested: CT-004↔SEC-005, CT-002↔TS-004, the Emergence.md File Purpose pointer, Forge_flow's Defined Terms local copy, the Kit's CT- registry row, Trajectories' CT-003/CT-007 v0→v1 rows.
- Automation-doctrine claims verified against script source, not descriptions: File_Template's header claims against `integrity_check.py`/`parser.py` (AUDIT_05); Canonical_Terms' `[ExternalRepo]` entry against `audit_lib.py` (AUDIT_06), including the convention's own recorded debugging history matching ADP's log.
- Count and parity recomputes: clean on VG (all values), FT (N/A structure), CT (10=10=10, Highest Risk, disputes, index parity including both In Progress — Vehicle rows).
- The X3 citation retrofit's qualifications are holding everywhere re-checked (AP, CT, ADP texts).

## Coverage note

Six of 34 Admin/ files done. The pattern document's due window (AUDIT_06–08) is satisfied at artifact 06; the next update is due in the AUDIT_11–14 window per the 5–8-file convention, or earlier if a new pattern earns its Xn registration (two instances required).

---

## Update 1 — 2026-11-10 (files 07–12; the AUDIT_11–14 due-window update)

Artifacts 07–12: Security_Protocols (07), Safety_Protocols (08), Repository_Integrity_Protocol (09), Governance_Migration_Protocol (10), Autonomy_Divergence_Protocol (11), Forge_Audit_Kit (12). This section aggregates already-deposited findings only; append-only; the text above is untouched.

**Pattern 1 (Aging Rule) — instances 5–7; control cases 3–4; one not-computable case:**

- Instance 5: Security_Protocols.md 9 of 11 open (AUDIT_07).
- Control case 3: Safety_Protocols.md clean (AUDIT_08).
- Instance 6: Repository_Integrity_Protocol.md 3 of 5 — RIP-005 144d, RIP-006 136d, RIP-009 124d (F-RIP-2).
- Instance 7: Governance_Migration_Protocol.md 2 of 4 — GMP-003 107d, GMP-013 107d (F-GMP-4). Running total: 47 of 60 open entries past the bar across the seven tripping files.
- Control case 4: Autonomy_Divergence_Protocol.md clean with a disclosed near-trip — GOV-021c at 87 days on 2026-11-10, trips 2026-11-13 if unreviewed (F-ADP-3).
- Not computable: Forge_Audit_Kit.md — its sidecar home carries zero Last Reviewed fields (F-FAK-3), a new shape for this pattern: the instrument that codifies Expiry Watch cannot run it on itself. Not counted as a control case; no aging instance claimed.

**Pattern 2 (relocation-repair-miss / wrong home) — instances 7–9:**

- Instance 7: F-RIP-1 — Unknowns’ Active Index RIP-005 row still pins “Security_Protocols.md … exists at v0.5”, the exact anchor the sidecar’s own 2026-09-03 correction removed; the repair missed the global index.
- Instance 8: F-GMP-3 — GMP’s Relationship section pins “Security_Protocols.md — exists at v0.5 (2026-06-19)” (the same formula), in a section the 2026-10-23 repair touched.
- Instance 9: F-ADP-1 — ADP’s File State Governance ID row cites the changelog’s pre-relocation home `Archive/Logs/Governance_Charter_Changelog.md` (relocated to `Admin/ALogs/` 2026-07-23; the registration it describes verified present there); the Charter’s own 2026-10-31 repoint repaired the Charter’s pointers but swept no other file.

**Bare-citation batch grep remedy — evidence points four and five (now five):**

- Fourth: F-RIP-5 (~7 bare path citations in operative/narrative text).
- Fifth: F-GMP-7 (~10 bare path citations, all targets resolving).
- ADP (artifact 11) scanned clean — the X3 qualifications are holding; no new point.

**Candidate new pattern (one instance; Xn requires two — not registered): repair-applied-to-the-mirror-not-the-owner.** F-FAK-1: VG-001’s resolution (2026-07-03) was corrected into Unknowns’ FAK-009 row on 2026-11-03 (MAINT-54) while the Kit’s own sidecar entry still asserts “VG-001 itself remains unresolved”. Distinct from Pattern 2 (wrong home) and Pattern 3 (stale condition): here a repair was propagated to the mirror but not to the owning record.

**Also recorded (single instances, not patterns):** F-FAK-4 (FAK-005’s Resolved row left in Unknowns’ Active Index contra Size Management Rule 2 / Discharge Procedure step 6 — closure substance verified); F-FAK-5 (the Kit’s own maintenance trigger fired: VG v0.8’s Gate 2 N/A definition post-dates the 2026-10-27 reconciliation; drift indicator in firing state, derivation solid); F-FAK-8 (the Cycle/CURRENT_CYCLE governance flag, open since 2026-07-14, still without its CT entry; harness session-based aging diverges from the ratified calendar-year Cycle).

**Positive records worth preserving (update 1):** the Kit’s changelog newest-first repair holds (v1.32 → v1.31 → v1.30 verified); the Kit’s “Intake Log entry 7” claim is exact (row 7 of 21); ADP’s three Astroid-miner convergence claims verify against the in-repo V0.07 snapshot (80–99% fleet consensus exact, §2.2 Reversion/Safe Mode, zero-g-fabrication induction heating + EM levitation); the Kit’s ID Reference and Scope Boundary targets all resolve (14/14 existence checks); the Kit’s token-ceiling note’s dated-measurement discipline is a clean staleness-marking instance.

**Coverage (update 1):** twelve of 34 Admin/ files done. The next update is due in the AUDIT_17–20 window per the 5–8-file convention, or earlier if a new pattern earns its Xn registration (two instances required — the mirror-repair candidate above is the one to watch).
