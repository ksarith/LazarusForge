# CAMPAIGN4_AUDIT_11 — Admin/Autonomy_Divergence_Protocol.md

**Campaign:** Campaign 4 adversarial sweep of `Admin/` (34 files), artifact 11 of 34.
**Auditor:** Vibe (Repo Custodian line). **Date:** 2026-11-10.
**Base commit:** `e24e443d524d181ee1bdc15d414ebc2a781cb361` (LF main at compose).
**File:** `Admin/Autonomy_Divergence_Protocol.md` (ADP), 75,975 chars, 679 lines, fetched complete at the base commit. SHA-256 of the file as found: `1735df7e784f781ffd6ab9404433f9dad05631ab9eb13dbef27d4d53c1f40989`.
**Method:** full-text read plus live-source verification of every operative cross-reference, including direct checks against `Automation/audit_lib.py` and `Automation/AUDIT_HARNESS.py` v18 as fetched text, and against the in-repo Astroid-miner V0.07 snapshot.
**Findings-only per PKC-020:** this pass does not advance Last Audit, Last Reviewed, version, Status, Spec Gates, or unknown states, and does not modify the audited file. Conversion to audits of record is the human’s alone (MAINT-26 / AP-032).

---

## File State as found

| Field | Value as found |
|---|---|
| Status | Draft — PROPOSED NOT RATIFIED (Exploration-stage; Spec Gates and Governance ID tracked ahead of formal promotion, deliberately) |
| Body Stability | Transitional |
| Spec Gates | 6/6 (G5 PASS 2026-08-11 via direct execution of `Automation/audit_lib.py`’s `parse_routing`/`check_cross_refs`; “112 entries at time of verification” annotated as historical — see Routing.md path-count note 2026-10-03; ALIASES “18 entries, still current”) |
| First Logged | 2026-07-19 |
| Last Audit | 2026-10-29 (X3 mechanical citation retrofit, 8 bare colliding-prefix citations qualified) — 12 days before this pass |
| Open Unknowns | 1 (GOV-021c — multi-agent coordinated divergence, §12; deliberately held Open pending live evidence; GOV-021b Resolved 2026-08-11) |
| Active Disputes | 0 |
| Highest Risk | High (GOV-021c Risk High) |
| Ethical Anchor | canonical, exact |
| Governance ID | GOV-021 — “formally registered in `Archive/Logs/Governance_Charter_Changelog.md` 2026-07-27” (see F-ADP-1: wrong home) |

Sidecars: GOV-021b (Resolved 2026-08-11, Priority Major, Last Reviewed 2026-08-11) and GOV-021c (Open, Risk High, Priority Major, Blocking Yes, First Logged 2026-07-27, Last Reviewed 2026-08-15).

---

## Findings

### F-ADP-1 — WARNING — Wrong-home changelog citation in File State (Pattern 2, instance 9)

The File State Governance ID row (line 25) reads: “GOV-021 — formally registered in `Archive/Logs/Governance_Charter_Changelog.md` 2026-07-27”. That path does not exist (fetch fails: “path does not point to a file”). The changelog lives at `Admin/ALogs/Governance_Charter_Changelog.md` — relocated there 2026-07-23 per its own header, and the harness’s own registry (`FALLBACK_REGISTRY` in `Automation/AUDIT_HARNESS.py` v18) maps the file to the `Admin/ALogs/` path.

The registration the row describes is real: the GOV-021 sidecar in the correct `Admin/ALogs/` copy records First Logged 2026-07-19 “as a candidate ID, in `Admin/Autonomy_Divergence_Protocol.md`”, formally registered 2026-07-27, Last Reviewed 2026-07-27. The pointer is wrong, not the registration.

Dating: the row was rewritten 2026-08-11 (the “stale registration note corrected” pass updated the File State Governance ID row and §2), i.e. four days after the 2026-07-23 relocation and four days after the 2026-07-27 registration — the path was already wrong when written. The Charter’s own 2026-10-31 repair (MAINT-29 relocation follow-up, preserved verbatim in the changelog) repointed the Charter’s identical `Archive/Logs/` → `Admin/ALogs/` pointers but did not sweep other files citing the old path; ADP’s Last Audit (2026-10-29) predates that repair by two days, so no later pass touched this row. Relocation-repair-miss (Pattern 2), instance 9 — same class as F-SP-1.

Scope of the error is one row: §2’s Status note (“registered in Charter sidecar 2026-07-27”) and the Cross-References row (“(Charter v0.10 changelog)”) carry no path and are clean.

**Suggested remedy (human queue):** single-path repoint in the File State Governance ID row to `Admin/ALogs/Governance_Charter_Changelog.md`.

### F-ADP-2 — WARNING — RIP-011 anchor fields absent from ADP’s Resolution Log

RIP-011’s ratified anchor rule requires `rl_entry_count_after` / `file_line_count_after` / `open_unknowns_after` fields on Resolution Log entries recording substantive revisions of Admin/ protocol files. Grep of `rl_entry_count_after` across ADP: 0 occurrences. The post-ratification RL entries are 2026-10-28 (AUDIT_20 F1–F6 enactment — substantive: wrapper reconciliation, sidecar tables added, Resolution Log restructured) and 2026-10-29 (X3 citation retrofit — citation-form-only, arguably non-substantive). At minimum the substantive 2026-10-28 entry carries no anchor fields and no logged exemption. Same class as F-GMP-2; folds into the queued human item (anchor-fields retrofit-or-exemption across the sweep’s findings).

### F-ADP-3 — NOTE — Aging Rule does not trip; near-trip disclosed (control case 4)

GOV-021c Last Reviewed 2026-08-15 = 87 days at 2026-11-10 — three days under the 90-day threshold. GOV-021b (Resolved 2026-08-11) is not subject. ADP is the campaign’s fourth Aging control case (after VG, FT, Safety). Disclosure: unless GOV-021c is reviewed on or before 2026-11-13, the entry trips the Aging Rule.

### F-ADP-4 — NOTE — Drift Indicators dormant; Compound Drift Rule not fired

All six indicators checked: §4/§6 modifications carry same-day RL entries; the 2026-08-15 live data point is graded in GOV-021c’s sidecar and RL; §12’s EC-001 mapping was cross-checked (2026-10-28 AUDIT_20 F4; ASM-004 verification); bare EC-/CF- citations — see F-ADP-5; the two “PROPOSED NOT RATIFIED” X2 instances are deliberately not migrated (PKC-031 migration-pending per the AUDIT_10 F5 ruling, recorded in the 2026-10-28 RL entry) — not a finding; Ethical Anchor and Navigation Anchors are canonical and unmodified.

### F-ADP-5 — NOTE — Bare-citation scan clean

The 2026-10-29 X3 pass qualified 8 bare colliding-prefix citations. The remaining unqualified ID mentions in operative text sit adjacent to a qualified path or under a qualified parent bullet (contextual qualification, consistent with the harness’s QUALIFY_WINDOW logic); sidecar definition rows and frozen RL history are exempt per audit_lib.py’s CT-007/PKC-003 rule. No new bare-citation instance; no remedy evidence point added.

---

## Clean verification (fabrication probes — all passed against live source)

1. **X10 parity:** File State Open Unknowns 1 (GOV-021c) = sidecar section (GOV-021c Open; GOV-021b Resolved) = Unknowns index GOV-021 row (Vehicle/Open/Major; GOV-021c the sole open sub-unknown). Highest Risk High = GOV-021c High. Priorities match field-for-field (both sidecars Major). Active Disputes 0 = empty section.
2. **Astroid-miner convergence claims verified in-repo:** the V0.07 snapshot exists at `Archive/Astroid-miner/Astroid-miner-AstroidMinerV0.07/` (with PROVENANCE.md; the external companion repo also still exists). `docs/vision/rogue-unit-management.md` §1.3 Fleet Consensus Validation: “High-risk deviations require 80–99% fleet-wide agreement before corrective action is deployed / Ensures a single unit cannot make destructive decisions unilaterally” — exact, including the rationale ADP quotes. §2.2 Reversion/Safe Mode present with the limited-operational-mode language ADP describes. `docs/architecture/uranus-ejector-module.md` present. `docs/isru/zero-g-fabrication.md`: “Induction Heating + EM Levitation … No crucible; high purity” — exact. ADP’s `[Astroid-miner]` bracket citations name the external repo’s files (which exist); the snapshot additionally makes all three claims verifiable in-repo. The snapshot’s kebab-case filenames (`rogue-unit-management.md` etc.) differ from the external names — noted, not a defect: the citations target the external repo, and G5’s Astroid substring exemption in audit_lib.py (line 123) means they never trip the harness, consistent with the recorded 2026-08-11 tooling history.
3. **Auditor_Protocols.md (v0.47):** AP-013 Resolved 2026-08-19 and AP-008 Open confirmed; AP-012/AP-016 Resolved via Autonomous Graceful Degradation (Human Interaction Point Doctrine); the 9-entry open-AP list matches ADP’s characterizations.
4. **Cognitive_Frameworks.md:** CF-002 still an explicit Open unknown.
5. **Forge_Net.md:** FN-001 High/Blocking with minority-report-preservation / contradiction-logging / confidence-decay language as §12.1 characterizes it.
6. **Field_Logs:** the 2026-08-15 entry (`FL-20260815-gov021c-independence`) exists with the “Reviewed — folded into Admin/Autonomy_Divergence_Protocol.md” language.
7. **Governance_Charter.md:** P-4 (line 110) and Q-2 (line 120) FROZEN axioms present with the exact language ADP’s Constitutional Impact Statement quotes; GOV-021 registered in the Charter v0.10 changelog 2026-07-27 (line 1261 of the changelog).
8. **Routing.md:** the 2026-10-03 path-count note is present and the stale “112” figure is gone from the live table.
9. **GMP §VI:** Three Independence Dimensions (line 897), the full Outcome Taxonomy (lines 910–912), and the Minimum Quorum Matrix (line 888) all present as §12.2 reuses them.
10. **Tooling claims:** `Automation/audit_lib.py` contains `parse_routing` (line 54), `extract_md_refs` (line 78), `check_cross_refs` (line 107), and the Astroid substring exemption (line 123). `AUDIT_HARNESS.py` v18 `ALIASES` = exactly 18 entries — ADP’s “still current” claim verified.
11. **Spec Gates staleness handling:** the “112 entries at time of verification” figure is annotated as historical with a pointer to Routing.md’s note, and the annotation inside the historical 2026-08-11 third-pass entry is marked and backfill-dated (2026-10-23) — a clean instance of honest staleness marking, recorded here as such.

---

## Out of scope (recorded, not findings against ADP)

- The in-repo snapshot’s own Discovery links use the dead `Lazarus-Forge-` name — frozen archival record inside the V0.07 snapshot; the MAINT-56 repoint covered the Charter only. For any future Archive-snapshot pass.
- The snapshot’s 2026-07-19 convergence note states the then-shared Watch/Reversion exit-condition gap; that gap was resolved on the LF side 2026-08-11 (§6 four exit paths). The note is a dated historical record and ADP’s §6 text is explicitly time-qualified (“at the time this was open”) — consistent.
- Unknowns.md’s resolved-entry notes for GOV-021b were not examined beyond the GOV-021 row (Unknowns.md is its own sweep file, already audited at artifact 02).

---

*Findings-only deposit per PKC-020. Composed 2026-11-10 at base commit `e24e443d`. Auditor: Vibe (Repo Custodian line). No field of the audited file was advanced or modified by this pass.*