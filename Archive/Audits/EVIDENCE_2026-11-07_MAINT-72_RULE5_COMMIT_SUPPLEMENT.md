# COMMIT-EVIDENCE SUPPLEMENT — MAINT-72 (2026-11-07)

**Purpose:** the Rule 5 verification report deposited this pass (Class A intake 14; `Archive/Audits/EXTERNAL_REVIEW_2026-11-07_CLAUDE_RULE5_PACKET1_ECONOMICS_VERIFICATION.md`) states in its §3/N3 that the cited commits could not be opened from the evidence base (`LazarusForge-1.34.Alpha.zip` — tree only, no git history) and asks for `git show --stat` (or the GitHub commit pages) for the six shas — "that one input unblocks the V\* rows across all five packets." This deposit supplies it, fetched from the live GitHub repository's history.

**Authorship and standing:** Vibe (GLM 5.3, Mistral AI) — Architect line PRIMARY, Repo Custodian secondary; co-author mandate invoked; Class A intake 14 processing; non-independent Genesis Phase (Q-2 invoked), disclosed at maximum: this line authored the dispositions, the aggregates and the packets being verified. This supplement is custodian evidence supply for the human-named verifier's step and the human's disposition — it is not verification by the named verifier, fills no Verified-by cell, changes no Status line, and makes no disposition.

## 1. The six cited commits — verified via the GitHub API against live history

| Cited (as in the rows) | Full SHA | Author date (UTC) | Author | Commit message (verbatim) | Changes | Files |
|---|---|---|---|---|---|---|
| `eee122a6ce` | `eee122a6ce4f531557d5d69eb803c69d823a99a6` | 2026-10-28 19:42:55 | ksarith | Decision Brief 2026-10-28b passes: Canonical_Terms v0.12 — CT-007/ID-prefix registry ECN- rename narration reconciled to executed (2026-07-06), erroneous EC-008 citation corrected (AUDIT_19 F3), Highest Risk Low→High (X10 recompute); Ship_of_Theseus — Highest Risk Medium→High (AUDIT_18 F1), bare AP-012 qualified (F2), ST-001–004 Last Reviewed refreshed; Economics — Highest Risk Medium→High (AUDIT_19 F1), Lessons Learned §7 vocabulary fix (F2), ECN-001/002/004/005/006 Last Reviewed refreshed; Adm_Scope_Map — CT/Economics/Ship_of_Theseus Risk rows synced. No gates advanced. | +66 / −29 | 4: `Admin/Adm_Scope_Map.md`, `Admin/Canonical_Terms.md`, `Admin/Economics.md`, `Admin/Ship_of_Theseus.md` |
| `8eb2949601` | `8eb2949601a45d87a1ef00aec61209dcb1b2c53b` | 2026-10-28 17:41:13 | ksarith | Metrics_Scaffold: enact human-ratified AUDIT_17 F1-F3 — Verification Ref row (F1); template sections closed (F2: Scope Boundary, Assumptions, Lessons Learned, Active Disputes, Auditor Notes & Unknowns, Drift Indicators); Resolution Log folded to nested form (F3); Last Reviewed 2026-10-28 | +61 / −7 | 1: `Admin/Metrics_Scaffold.md` |
| `9f374e7b31` | `9f374e7b312bfd1d0c4afb294f05f50c152d11b6` | 2026-10-28 18:59:51 | ksarith | Security_Protocols: register SEC-013 reciprocal unknown (SoT ST-004; brief ID SEC-012->SEC-013 collision fix; supersedes never-logged SEC-013 reservation); Unknowns v5.72->v5.73 mirror; Unknowns_Changelog: late-migrated v5.72 + v5.73 entries | +32 / −4 | 3: `Admin/Security_Protocols.md`, `Archive/Logs/Unknowns_Changelog.md`, `Unknowns.md` |
| `5becc4d581` | `5becc4d581eb9d6ddf6149743a5e68e306df5b92` | 2026-10-29 17:43:20 | ksarith | X3 mechanical citation retrofit — Admin/ folder pass, Part 1/3 (PKC-003 qualified-citation rule; human-ruled Decision Brief 2026-10-29 item 4A; delegated line) | +75 / −70 | 4: `Admin/Canonical_Terms.md`, `Admin/Ethical_Constraints.md`, `Admin/Governance_Charter.md`, `Admin/Security_Protocols.md` |
| `2da669e28a` | `2da669e28a3fb118ad3ffa3c2d847e140d80bb9b` | 2026-10-28 19:21:43 | ksarith | AUDIT_10 F1 re-ruled: Challenges Problem-Statement Spec Gates N/A by subtype governs (supersedes same-day fee92b4 reconciliation); PKC-031 X2 sweep (CIR_Gov Binding Status, Unknowns GOV-021/CIR-GOV-001 rows); CIR_Gov Drift Indicators added (AUDIT_04 F3); Unknowns v5.74; duplicate v5.71 changelog entry removed | +30 / −17 | 4: `Admin/CIR_Gov.md`, `Admin/File_Template.md`, `Archive/Logs/Unknowns_Changelog.md`, `Unknowns.md` |
| `05bdb53912` | `05bdb53912240d2601f8236817c307451ff3a81f` | 2026-10-28 19:25:08 | ksarith | Wrapper Hygiene Batch (ratified 2026-10-28c): GC Scope Boundary lists Deployment Localization doctrine (AUDIT_01 F1) + Astroid-miner companion row to exists-state per owner ruling; GMP Scope Boundary lists Fork Reconciliation Track (AUDIT_02 F1); RS ownership narration reconciled to Charter state (AUDIT_12 F2) + PKC-011 Astroid-miner narration amendment; GC changelog entry | +28 / −12 | 4: `Admin/Governance_Charter.md`, `Admin/Governance_Migration_Protocol.md`, `Admin/Repository_Structure.md`, `Archive/Logs/Governance_Charter_Changelog.md` |

**Cross-checks:**
- B-F3 cites "`eee122a6ce` (2026-10-28 19:42, same commit)" — the actual author date is 2026-10-28 19:42:55 UTC. MATCH.
- Each commit's message corroborates the row claims it is cited for: `eee122a6ce` names the CT-007/ID-prefix registry ECN- rename narration reconciliation (B-F3), the X10 Medium→High recomputes for Economics and Ship_of_Theseus (A-F1/B-F1, SoT A-F2/B-F1), the ECN- Last Reviewed refreshes (A-F2/B-F2) and the §7 Lessons Learned vocabulary fix (A-F3); `8eb2949601` enacts AUDIT_17 F1–F3 on Metrics_Scaffold (MS A-F1/A-F2/A-F3); `9f374e7b31` registers the SEC-013 reciprocal unknown (SoT B-F3); `5becc4d581` is the X3 retrofit Part 1/3 touching `Admin/Governance_Charter.md` (GC A-F2); `2da669e28a` re-rules AUDIT_10 F1 touching `Admin/File_Template.md` (FT A-F1); `05bdb53912` is the Wrapper Hygiene Batch naming "GC Scope Boundary lists Deployment Localization doctrine (AUDIT_01 F1)" (GC A-F1).
- All six commits are authored by the human account (ksarith) — the dispositions were executed under human ratification, consistent with the house flow the rows describe.

## 2. Aggregate intake re-verification at the live head (LF main, `a44d7a15` pre-landing)

All five tranche-1 aggregates' live blob SHAs match the packet table exactly — the packet evidence base is valid at the live head, not only at 1.34; no drift through the MAINT-63/70/71 landings; none of the five carries a §5 addendum (the 8 MAINT-63 addenda landed on tranche-2 aggregates only); all five still read "Dispositions unverified"; no Verified-by cell is filled on any.

| Aggregate | Live blob SHA at `a44d7a15` | Packet blob | Result |
|---|---|---|---|
| Economics | `3799c31fb289cec77b4f73c064a8b25c6b033353` | `3799c31f…` | MATCH |
| File_Template | `3d72b5c817ca86e033e35509c23b2b06e78605f0` | `3d72b5c8…` | MATCH |
| Governance_Charter | `0fa436287578ce4b3c3f8c3cc8ace6d80e50eee7` | `0fa43628…` | MATCH |
| Metrics_Scaffold | `068c81069545e479842492ba9e8a4831308d0526` | `068c8106…` | MATCH |
| Ship_of_Theseus | `c4177cd7274e868c7673e107fbda8e3dd6383424` | `c4177cd7…` | MATCH |

## 3. Rule 6 immutability re-verified at the live head

The three Economics originals' blob SHAs match the aggregate's Provenance table exactly at the live head: AUDIT_19 (8,062 bytes, `9ecea88e497bb55a5420d92a25d18e6196762131`) at `Admin/AAudits/Superseded/AUDIT_19_Admin-Economics.md`; CAMPAIGN_AUDIT_19 (11,334 bytes, `9d974dde688d0d0eba8c916ef2a7cc20c2dca9fb`) at `Admin/AAudits/Superseded/CAMPAIGN_AUDIT_19_Admin-Economics.md`; CAMPAIGN2_AUDIT_95 (2,943 bytes, `92255b0e9a386019c7b6b4270177558acbc72fb7`) at `Admin/AAudits/CAMPAIGN2_AUDIT_95_Admin-Economics.md`.

## 4. N1 / N2 corroboration at the live head

- CT-007 remains genuinely Open in `Unknowns.md` v5.79 (row: "ID namespace allocation doctrine undefined — narrower EC→ECN rename sub-issue resolved 2026-07-06; the broader namespace-allocation doctrine gap it was meant to cover remains genuinely Open").
- `Admin/Canonical_Terms.md` live header reads `**Version 0.14**`.
- The Economics A-F4 evidence cell reads "Within-folder X3 ruling open" verbatim.
- **Class finding recorded (no disposition made):** the same stale evidence phrase also appears in Ship_of_Theseus A-F3 and Metrics_Scaffold B-F1 — three aggregates carry it. Each is a dated-addendum candidate under Rule 6; dispositions are the human's.

## 5. Non-claims

This supplement verifies the existence, author dates, authors, full messages and per-file change counts of the six commits as served by the GitHub API at fetch (2026-11-07, live main); it does not open the patches line-by-line, does not fill any Verified-by cell, does not replace any Status line, opens no FAK, and makes no disposition. Per EIP R5, cross-model agreement is correlated evidence, not independence: the named verifier's own reading of this supplement — on the human's word — is what converts the V\* rows.

*Deposited 2026-11-07 — MAINT-72 (Vibe — Architect line PRIMARY, Repo Custodian secondary; co-author mandate invoked; Class A intake 14; non-independent Genesis Phase, disclosed). Findings-only; nothing self-advances.*
