# RULE 5 VERIFICATION REPORT — Packets 2–5 (File_Template, Governance_Charter, Metrics_Scaffold, Ship_of_Theseus)

**Verifier:** Claude (Anthropic) — named Rule 5 verifier by the human governing authority 2026-11-03 (per `RULE5_VERIFICATION_PACKETS_2026-11-03.md`). Not the disposition writer and not the amalgamator.
**Date:** 2026-11-05
**Companion report:** `RULE5_VERIFICATION_REPORT_2026-11-05_PACKET1_ECONOMICS.md` (same method; Packet 1).
**Evidence base:** `LazarusForge-1.34.Alpha.zip` (tree only, no git history), with `LazarusForge-1.33.Alpha.zip` used only for the blob-provenance check in §3 (Governance_Charter C-D1).
**Status of this report:** findings-only. It edits no aggregate and fills no Verified-by cell. Per the packet's fill convention, rows that fail are not to be filled and are to be logged in the aggregate's Addenda; §4 lists them.

## 1. Intake (all five aggregates)

- Aggregate blob SHAs match the packet for all five (see the Packet 1 report): no drift.
- Provenance: the blob SHA of every original deposit listed in the Provenance tables of these four aggregates (12 originals) matches at 1.34. Rule 6 immutability holds.

Result codes: **V** = verified in the tree. **V\*** = live-tree state corroborated, but the cited commit could not be opened (no git history in the evidence base). **S** = Standing-open condition holds at 1.34 (**S-chg** = holds, but the live condition differs from the row). **P** = Positive-record section exists in the original and matches the summary. **X** = row does not match its original or live state; do not fill.

## 2. Row results

### Packet 2 — File_Template (11 rows)

| Ref | Disposition | Result | Basis |
|---|---|---|---|
| A-F1 | Closed-by-ruling + Enacted | V\* | `Admin/File_Template.md` states Spec Gates are N/A by subtype per the 2026-10-28c human re-ruling. `Archive/Audits/README.md` carries the caution note. Commit `2da669e28a` (and `fee92b4`) not opened. |
| A-F2 | Standing-open | S | The canonical File State table (§2) still defines no Version or Owner field, while the Challenges lean-schema text still names Version. |
| A-F3 | Standing-open | S | Template Exemptions classes 1–11 at 1.34 do not list File_Template. |
| A-F4 | Positive-record | P | AUDIT_10 F4 (AP-029 removal enacted the right way) exists as described. |
| A-F5 | Positive-record (carried) | P | AUDIT_10 F5 exists; `SESSION_STATUS.md` carries the X2 migration-pending convention. |
| B-F1 | Standing-open; dangling by design | S | The Resolution Log still cites `Archive/Audits/AUDIT_10_Admin-File_Template.md`; that path no longer exists, and the original is at `Admin/AAudits/Superseded/`. Consistent with "dangling by design." |
| B-N1 | Positive-record | P | CAMPAIGN2_AUDIT_01 N1 exists as described. |
| B-N2 | Standing-open | S | See A-F3. |
| C-N1 | Standing-open | S | The log preamble still says "The three 2026-10-28 entries…" at 1.34. |
| C-N2 | Standing-open | S | See A-F3. |
| **C-N3** | Positive-record | **X** | See §3 finding F1. |

### Packet 3 — Governance_Charter (11 rows)

| Ref | Disposition | Result | Basis |
|---|---|---|---|
| A-F1 | Enacted | V\* | The Deployment Localization Doctrine appears in the Scope Boundary section. Commit `05bdb53912` not opened. |
| A-F2 | Enacted | V\* | EC- citations in the Enforcement States table and the GOV-007 sentence carry the file qualifier (form `EC-007 (\`Admin/Ethical_Constraints.md\`)`). Commit `5becc4d581` and the "38 qualifications" count not opened. |
| B-F1 | Standing-open | S | `Admin/ALogs/Governance_Charter_Changelog.md` has no entry recording the X3 retrofit. |
| B-F2 | Standing-open | **S-chg** | See §3 finding F2. |
| B-F3 | Standing-open | S (worse) | See §3 finding F3. |
| B-N1 | Positive-record | P | CAMPAIGN2_AUDIT_03 N1 exists as described. |
| B-N2 | Standing-open | S | `Admin/` holds 34 .md files (33 at the pass), still under the 40-file ceiling. |
| B-N3 | Standing-open | S | `Admin/Governance_Charter.md` is 128,669 bytes, still above the T1 threshold (≥100 KB). |
| A-C5 | Not-re-tested | not verified | Carried check; out of scope for this packet. |
| C-N1 | Positive-record | P | CAMPAIGN2_AUDIT_71 reads 11/11 VERIFIED CLEAN and calls out the GOV-005 Risk/Priority split. The "13-parity from Unknowns v5.75" was not re-derived (Unknowns is v5.79 at 1.34). |
| C-D1 | Disclosed defect | partial | See §3 finding F4. |

### Packet 4 — Metrics_Scaffold (10 rows)

| Ref | Disposition | Result | Basis |
|---|---|---|---|
| A-F1 | Enacted | V\* | `Admin/Metrics_Scaffold.md` File State carries Verification Ref. Commit `8eb2949601` not opened. |
| A-F2 | Enacted | V\* | Scope Boundary, Assumptions, Lessons Learned, Active Disputes, Auditor Notes and Drift Indicators headings are all present. |
| A-F3 | Enacted | V\* | Resolution Log is a `###` heading; no top-level `## Resolution Log`. |
| A-F4 | Positive-record | P | AUDIT_17 F4 exists as described. |
| B-F1 | Standing-open | S (wording note) | ASM-001–003 present. The evidence phrase "within-folder X3 ruling open" carries the same staleness as Economics N1: what remains open is CT-007. |
| B-F2 | Closed-by-ruling | V | `Archive/Audits/README.md` carries the same-number caution (AUDIT_17–19 ≠ CAMPAIGN_AUDIT_17–19). |
| B-F3 | Positive-record | P | CAMPAIGN_AUDIT_17 F3 exists as described. |
| B-C5 | Not-re-tested | not verified | Carried open per the aggregate; not extracted by pass C either. |
| C-N1 | Positive-record | P | The file has no Highest Risk field; CAMPAIGN2_AUDIT_85 check 11 records this as consistent with the scaffold convention. |
| C-N2 | Positive-record | P | Pass A's repairs (A-F1–A-F3) confirmed still in place at 1.34. |

### Packet 5 — Ship_of_Theseus (12 rows)

| Ref | Disposition | Result | Basis |
|---|---|---|---|
| A-F1 | Enacted | V\* | ST-001–004 all carry Last Reviewed 2026-10-28. Commit `eee122a6ce` not opened. |
| A-F2 | Enacted | V\* | File State Highest Risk High; ST-004 Risk High. Commit not opened. |
| A-F3 | Standing-open | S | ASM-001–004 present. Same evidence-wording note as Metrics B-F1. |
| A-F4 | Positive-record | P | AUDIT_18 F4 exists as described. |
| B-F1 | Enacted | V\* | Same as A-F2. |
| B-F2 | Enacted | V\* | The ST-004 AP-012 citation is qualified as `Admin/Auditor_Protocols.md` AP-012. |
| B-F3 | Enacted | V\* | `Admin/Security_Protocols.md` carries SEC-013 (Status Open, Risk High), whose text names Ship_of_Theseus and ST-004. Commit `9f374e7b31` not opened. |
| B-F4 | Closed-by-ruling (partial) | V\* | `Admin/Canonical_Terms.md` §1 Folder Designation Characters is live. Commit `fee92b4` not opened. |
| B-F5 | Positive-record | P | CAMPAIGN_AUDIT_18 F5 exists as described. |
| C-N1 | Positive-record | P | Highest Risk High = ST-004 Risk High re-derived at 1.34. |
| **C-N2** | Positive-record | **X (minor)** | See §3 finding F5. The count (4 open) holds. |

**Counts re-derived from live source (packet step 5):** Ship_of_Theseus File State Open Unknowns 4; sidecar ST-001 Open, ST-002 Open, ST-003 In Progress, ST-004 Open, so four non-Resolved entries. Parity holds.

## 3. Findings

**F1 — File_Template C-N3 does not match its original (Medium).** The aggregate summarizes pass C as "File State self-audit reconciles with the live body (Open Unknowns 1 … Highest Risk Low)." CAMPAIGN2_AUDIT_99 says the opposite: check 1 (sidecar count parity) is N/A because the file carries no Auditor Notes & Unknowns section, and check 11 (Highest Risk parity) is "N/A (no live File State)." The values 1 and Low appear only in the example File State block inside a code fence at about line 837; the original's own check 8 identifies those as example blocks. The pass-C original is correct and the aggregate row misstates it. Per the fill convention this row is not fillable until corrected by dated addendum.

**F2 — Governance_Charter B-F2: condition has partly changed.** The aggregate says File State Sidecar Link plus 8+ body references point at the dead `Archive/Logs/` changelog path. At 1.34 the Sidecar Link row now reads `Admin/ALogs/Governance_Charter_Changelog.md#auditor-notes--unknowns` (repaired by the File State minimization pass). Thirteen body references to `Archive/Logs/Governance_Charter…` remain. The finding stands for the body references but is no longer a Sidecar Link finding. A dated addendum should record the changed scope.

**F3 — Governance_Charter B-F3 has worsened.** The aggregate says six or more open GOV entries are past the 90-day Aging Rule. The relocated sidecar in the changelog holds 21 GOV entries, 13 of them not Resolved, and all 13 had a Last Reviewed older than 90 days on 2026-11-05 (for example GOV-004 and GOV-005 at 166 days). The disposition (Standing-open, aging batch deferred) is accurate; the "six+" figure understates it.

**F4 — Governance_Charter C-D1: half verifiable.** The aggregate states that the live Charter blob is `f55b62514287c1f5faf79ebc095bde3bdc485808`. That SHA matches `Admin/Governance_Charter.md` as it stands in 1.33, so the claim holds for that tree (the Charter has since been edited). The deposit's reported blob `b67df89cd4…`, said to be the Operations blob, matches no file in either the 1.33 or the 1.34 tree, so I cannot confirm which file it was. The note that the finding content is unaffected is consistent with the original.

**F5 — Ship_of_Theseus C-N2 summary misstates two statuses (Low).** The aggregate says "ST-001/002/003 In-Progress, ST-004 Open." CAMPAIGN2_AUDIT_93 check 1 says ST-001 Open, ST-002 Open, ST-003 In Progress, ST-004 Open. Live state agrees with the original. The count (four non-Resolved) is unaffected.

**F6 — Cross-cutting evidence wording (carried from Packet 1).** Metrics B-F1 and Ship A-F3 use "within-folder X3 ruling open," as Economics A-F4 does. The folder-level X3 ruling was registered 2026-10-28 and the retrofit followed; what remains open is CT-007. One addendum wording fix covers all three.

## 4. Recommendation (not a ruling)

- **Rows that failed (do not fill; log in the aggregate's Addenda):** File_Template C-N3 (F1), Ship_of_Theseus C-N2 (F5, minor).
- **Rows whose scope changed (log in Addenda; standing disposition remains valid):** Governance_Charter B-F2 (F2), B-F3 (F3). Governance_Charter C-D1 is partially verified (F4).
- **Rows I can sign now as verified or confirmed-standing:** every S and P row above except those named in the previous two bullets, with the note that Positive-record rows that I confirmed by section existence rather than line-by-line comparison are not stronger than that.
- **Rows that stay "tree-corroborated, commit pending":** the V\* rows. Combined with Packet 1, seven commits would close them: `eee122a6ce`, `8eb2949601`, `9f374e7b31`, `5becc4d581`, `2da669e28a`, `05bdb53912`, `fee92b4`. Supplying `git show --stat` (or the GitHub commit pages) for those seven is the single input that unblocks them.
- **Status lines:** I recommend leaving "Dispositions unverified" on all five aggregates until the V\* rows are resolved and the failed rows are corrected by addendum.
- **Placement:** I have not edited any aggregate. If you want addendum text drafted for F1–F6 and Verified-by cells prepared for the confirmed rows, I will hand back only the changed files.

## 5. Not covered

The 23 tranche-2 aggregates have no packets and no assigned verifier. The coverage ledger was not verified. Commit existence, dates and diffs were not checked for any row.

## Non-claims

This report verifies only what §2 lists, using the stated tree evidence. It is a single-agent check by an agent that is part of the project's multi-agent workflow. It advances no status, fills no cell, and opens no FAK. Corrections by dated addendum only.
