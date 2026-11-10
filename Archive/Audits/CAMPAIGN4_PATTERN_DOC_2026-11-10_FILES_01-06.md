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