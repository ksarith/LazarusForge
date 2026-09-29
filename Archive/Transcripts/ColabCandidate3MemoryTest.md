 ======================================================================
Candidate 3 — Transient Embedding Index
2026-09-29 10:52 UTC
======================================================================
  note: 4 candidate zips found; using the most recently modified:
    2026-09-29 01:17  /content/drive/MyDrive/LazarusForge-1_17_Alpha_unified.zip <-- selected
    2026-09-29 01:17  /content/drive/My Drive/LazarusForge-1_17_Alpha_unified.zip
    2026-07-28 01:11  /content/drive/MyDrive/LazarusForgeV0-0.99.31.zip
    2026-07-28 01:11  /content/drive/My Drive/LazarusForgeV0-0.99.31.zip
  (to force a different one, rename it, or delete the others, and re-run)
Repo root: /content/_extracted_repo/LazarusForge-1.17.Alpha

Collecting Corpus A (distilled) ...
  67 source slices
Collecting Corpus B (history) ...
  103 source slices

Building transient indexes ...
Loading weights: 100% 103/103 [00:00<00:00, 1595.87it/s]  Embedding 591 chunks for corpus_a_distilled ...
Batches: 100% 19/19 [01:16<00:00,  2.40s/it]  Index ready: corpus_a_distilled (591 chunks)
Loading weights: 100% 103/103 [00:00<00:00, 1800.12it/s]  Embedding 3444 chunks for corpus_b_history ...
Batches: 100% 108/108 [04:51<00:00,  1.27s/it]  Index ready: corpus_b_history (3444 chunks)

======================================================================
Running frozen queries
======================================================================

--- Query 1 [Decision history] ---
Q: Why does GMP-011's Genesis Phase holding clause anchor to Governance_Charter.md rather than to Governance_Migration_Protocol.md §VII.5?
  Corpus A top hit: Admin/Canonical_Terms.md
  Corpus B top hit: Admin/Ethical_Constraints.md

--- Query 2 [Decision history] ---
Q: Why was the CE-006 vessel design sketch integrated only after two rounds of correction rather than accepted on the first pass?
  Corpus A top hit: Admin/Resolution_Methodology.md
  Corpus B top hit: Architecture/Chemistry.md

--- Query 3 [Rejected reasoning] ---
Q: Why was the independent Grok/Copilot thread's GOV-008 registry patch to Governance_Charter.md rejected, and what was preserved from it instead?
  Corpus A top hit: Admin/Canonical_Terms.md
  Corpus B top hit: Admin/Governance_Migration_Protocol.md

--- Query 4 [Rejected reasoning] ---
Q: Why was the 2026-07-29 "CIR v2.0" bundle held as unratified draft material rather than applied alongside CIR-F02/CIR-F03?
  Corpus A top hit: Admin/CIR_Gov.md
  Corpus B top hit: Admin/Computational_Institutional_Reasoning.md

--- Query 5 [Unknown history] ---
Q: What was previously unresolved about ENV-007 and ENV-008, and how long had each sat unrevisited before being corrected?
  Corpus A top hit: Admin/Economics.md
  Corpus B top hit: Admin/Security_Protocols.md

--- Query 6 [Unknown history] ---
Q: What was GOV-008's status before the §VII.8 registry-schema extension, and did that extension change it?
  Corpus A top hit: Admin/Canonical_Terms.md
  Corpus B top hit: Admin/Governance_Migration_Protocol.md

--- Query 7 [Resolution history] ---
Q: How was the Support_Raft induction-loss discrepancy (12% laboratory vs. 20–40% real subsea conditions) resolved and logged?
  Corpus A top hit: Tests/Support_Raft.md
  Corpus B top hit: Tests/Support_Raft.md

--- Query 8 [Resolution history] ---
Q: How was RIP-002's "not yet implemented" status corrected, and what exactly was verified to justify the change?
  Corpus A top hit: Admin/Canonical_Terms.md
  Corpus B top hit: Admin/Progress_Log.md

--- Query 9 [Governance reasoning] ---
Q: Why was the Closed_Loop_Feedstock draft's "Resolved 2026-08-03" status claim rejected rather than accepted?
  Corpus A top hit: Admin/Auditor_Protocols.md
  Corpus B top hit: Admin/Progress_Log.md

--- Query 10 [Governance reasoning] ---
Q: Why does AP-033 (Rule 9) require confirmed governance-file access before a contribution can mark an unknown toward Resolved status?
  Corpus A top hit: Operations/Gate_02_Triage.md
  Corpus B top hit: Admin/Computational_Institutional_Reasoning.md

--- Query 11 [Technical reasoning] ---
Q: What led to CIR-F03's correction of Φ(n)'s trigger condition from S(n)=0 to S(n)≤ε, and why didn't the original CIR-F02 review catch it?
  Corpus A top hit: Admin/CIR_Gov.md
  Corpus B top hit: Admin/Computational_Institutional_Reasoning.md

--- Query 12 [Technical reasoning] ---
Q: Why was Architecture/Engineering.md's unknown-history safety factor corrected from 3× to 6×+?
  Corpus A top hit: Tests/Cognitive_Salvage_Layer.md
  Corpus B top hit: Architecture/Engineering.md

--- Query 13 [Cross-document reasoning] ---
Q: Beyond GMP-011, where else does the same failure pattern appear — an unratified section cited as though it supports the opposite of what it actually says?
  Corpus A top hit: Admin/Governance_Migration_Protocol.md
  Corpus B top hit: Admin/Governance_Migration_Protocol.md

--- Query 14 [Cross-document reasoning] ---
Q: How does CIR §4.3's Provenance Ceiling Gate relate to Auditor_Protocols.md's Institutional Provenance Labels, and where was that relationship first made explicit rather than merely implied?
  Corpus A top hit: Admin/Canonical_Terms.md
  Corpus B top hit: Admin/Computational_Institutional_Reasoning.md

Results written to /content/candidate3_results.json

Discarding transient indexes ...
Done. Indexes discarded. Markdown files remain the sole durable source.
======================================================================


Json.dumps 

{
  "run_at": "2026-09-29T10:58:54.711775+00:00",
  "embed_model": "all-MiniLM-L6-v2",
  "top_k": 5,
  "repo_root": "/content/_extracted_repo/LazarusForge-1.17.Alpha",
  "source_zip": "LazarusForge-1_17_Alpha_unified.zip",
  "source_zip_sha256": "4106f1f70139ef9514372fdbf0f6b7e00f945847cf7c6eb996e6fccd01b28954",
  "md_file_count": 120,
  "queries": [
    {
      "id": 1,
      "class": "Decision history",
      "query": "Why does GMP-011's Genesis Phase holding clause anchor to Governance_Charter.md rather than to Governance_Migration_Protocol.md \u00a7VII.5?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": " GOV-018 closure (2026-08-23), alongside Governance Fork Reconciliation\nin `Admin/Governance_Charter.md` and the Fork Reconciliation Track in\n`Admin/Governance_Migration_Protocol.md`. No overlapping or competing\nterms found elsewhere in the repository at registration time; the nearest\nneighbors \u2014 \"active constitutional invariant\" (`Admin/Auditor_Protocols.md`)\nand \"constitutional state\" (`Admin/Security_Protocols.md`) \u2014 are used in\nnarrower rollback/recovery contexts and are not renamed or super"
        },
        {
          "rank": 2,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "gh       | Governance_Charter.md tier structure formally revised      |\n\n---\n\n## Conflict Resolution Doctrine\n\n**This section governs how terminology conflicts are resolved.**\n\nThree vocabulary sources exist in the repository:\n\n| Source                       | Authority Domain                                      |\n|------------------------------|-------------------------------------------------------|\n| `Architecture/Forge_flow.md` | Operational routing semantics; gate logic vocabulary  |\n| `Ad"
        },
        {
          "rank": 3,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "Lessons Learned",
          "text": "the actual gap \u2014 the existing rule was location-based (Tier 1 file vs. not) when the real distinguishing factor was constitutional impact | Generalizing an existing rule along its true axis is usually better than adding a parallel one for the case that doesn't fit \u2014 GMP-005 and GMP-009 were the same underlying gap, not two gaps | Replicated | No |\n| 2026-07-19 | Audit Review | Treating a human-directed approach (CE-006) as sufficiently settled for another file (CLF-004) to build on before indepe"
        },
        {
          "rank": 4,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "                 | Governance_Charter.md places Forge_flow.md in Tier 5; derived file cannot contradict constitutional source | No     |\n| 2026-05-27 | This file as primary ontology superseding Forge_flow.md                | Forge_flow.md is the operational routing authority; this file is the cross-file consistency enforcer | No          |\n\n---\n\n## Drift Indicators\n\nMandatory re-audit conditions for this document:\n\n- Conflict resolution doctrine removed or simplified to single-source authority\n-"
        },
        {
          "rank": 5,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "\ncommit history) is not automatically the constitutional surface. Defined\nand governed by Governance Fork Reconciliation in\n`Admin/Governance_Charter.md` (GOV-018).\n\n**Claimed Lineage**\nA governance lineage that asserts continuity with this repository's Tier 1\nconstitutional surface. Assertion alone; carries no legitimacy by itself.\nSee Recognized Lineage and Ratified Constitutional Lineage, below, for the\nstates a claim may progress to under the Fork Reconciliation Track\n(`Admin/Governance_Migr"
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Ethical_Constraints.md",
          "section": "full",
          "text": "Deliberately anchored to the Charter's Genesis Phase declaration rather than `Governance_Migration_Protocol.md` \u00a7VII.5: that section is part of \u00a7VII, headed \"Proposed, Not Ratified,\" and its own text states that nothing in \u00a7VII relaxes Genesis Phase rules \u2014 citing it as support for a clause that suspends future enforcement machinery during Genesis Phase would both rest on unratified text and invert what that text says. Same correction applied to GMP-011's holding clause, 2026-09-23.)*\n\n6. **Expl"
        },
        {
          "rank": 2,
          "source": "Admin/Progress_Log.md",
          "section": "full",
          "text": " Phase holding clauses initially cited `Governance_Migration_Protocol.md` \u00a7VII.5 as supporting authority \u2014 live text there says the opposite (nothing in unratified \u00a7VII relaxes Genesis Phase rules) and the holding clause's expiry condition was also narrower than actual Genesis Phase status (tied only to GOV-008 quorum, not any of the Charter's four exit pathways). Both corrected to anchor on the Charter's Genesis Phase declaration directly before ratification. Separately, `Admin/Metrics_Scaffold"
        },
        {
          "rank": 3,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "s in\n`Admin/Governance_Charter.md` v0.7 (2026-06-16) \u2014 GMP exists as executing\nresolution path but has not been audited against charter constraints. Full\nresolution pending GMP reaching Provisional Specification maturity.\nUnknowns.md v3.4 reflects corrected status.\n\n---\n\n### GMP-002 \u2014 Canonical Governance Ownership transfer not yet recorded in Charter\n\n| Field         | Value                                      |\n|---------------|--------------------------------------------|\n| Status        | O"
        },
        {
          "rank": 4,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "                                    |\n| Owner         | `Admin/Governance_Migration_Protocol.md`   |\n| First Logged  | 2026-06-05                                 |\n| Last Reviewed | 2026-06-19                                 |\n\n**Description:** This file is the intended resolution target for GOV-001\nin `Admin/Governance_Charter.md`. GOV-001 status needed updating.\n\n**Resolution:** GOV-001 status updated to In Progress in\n`Admin/Governance_Charter.md` v0.7 (2026-06-16) \u2014 GMP exists as executing\nr"
        },
        {
          "rank": 5,
          "source": "Unknowns.md",
          "section": "full",
          "text": "07a.*\n*GMP-005 and GMP-009 are Resolved as of 2026-07-17 (Track A/Track B redefined by constitutional impact rather than document location, merged as one gap) and do not appear in this active index per Size Management Rule 2 \u2014 see `Governance_Migration_Protocol.md`'s own sidecar and Resolution Log. `Governance_Charter.md`'s EDL draft was formally classified Track A under that resolution and remains PROPOSED, NOT RATIFIED. GOV-013 was classified Track A under the same resolution but has since bee"
        }
      ]
    },
    {
      "id": 2,
      "class": "Decision history",
      "query": "Why was the CE-006 vessel design sketch integrated only after two rounds of correction rather than accepted on the first pass?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/Resolution_Methodology.md",
          "section": "Lessons Learned",
          "text": "004/GR-003 or residual GF-007) |\n| 2026-08-15 | First applied case (WA-004/GR-003) | Ran the five-step order against a real Critical-priority pair | \u00a72's reuse check and \u00a73's verify-before-accept check together produced a better architectural result (two-outcome disposal model) than the originally-outlined flat category list would have | \u00a73 is not only a fabrication safeguard \u2014 verifying an upstream principle before building on it can surface a stronger structure than the thing being checked | A"
        },
        {
          "rank": 2,
          "source": "Operations/Gate_06_Fabrication.md",
          "section": "Lessons Learned",
          "text": "ecision instruments at bootstrap is correct doctrine \u2014 precision is seeded deliberately, not bootstrapped from nothing | Analogous | Yes \u2014 establish actual v0 precision ceiling during first operational fabrication cycle |\n| 2026-05-15 | Audit Review | Add-to-excess framed as workaround for imprecise forming | Add-to-excess is not a workaround \u2014 it is the correct philosophy for a system working with variable feedstock and inherently imprecise forming methods | The weld gets close. The mill finds "
        },
        {
          "rank": 3,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "ceholder; false-precision Measured claim                      | Placeholder \u2014 see GH-002 |\n| Jun 2026  | LayerMD structural template                              | Hallucinated framework; not consistent with File_Template.md               | No          |\n| Jun 2026  | Flat action_sequence array (v0.1)                        | Insufficient for kinematic replay and canonicalization                     | No          |\n| Jun 2026  | efficiency_delta single-dimension field (v0.1)           | Implied "
        },
        {
          "rank": 4,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": ": CSL-A06 added (simulation fidelity assumption was hidden);\n             fabrication failure modes added; NOVEL hard constraint added\n    Class 3: CANDIDATE_NOVEL intermediate status added; S2R delta trigger added\n- New unknowns: GH-007 through GH-011 (surfaced by multi-agent review)\n- Highest-risk finding: CSL-A06 \u2014 entire pipeline safety guarantee rests\n  on Stage 3 fidelity; assumption was implicit in v0.1\n\nDocument: Cognitive_Salvage_Layer.md (Exploration audit, 2026-06-24)\nAuditor: Synthes"
        },
        {
          "rank": 5,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "n-to-physical fidelity is low, promoted heuristics may pass Stage 3 while failing in physical execution. This assumption requires empirical validation before any heuristic reaches Operational Spec status.\n\n**CSL-A03 elaboration (Payment via Specification, added 2026-08-03 \u2014 human-directed, corrective merge from a Copilot/Grok exchange, see AP-033):** the expiry trigger above (\"Stage 3 validation pass on first physical anomaly\") elaborated as a concrete test: at the first physical anomaly that ge"
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Architecture/Chemistry.md",
          "section": "Resolution Log",
          "text": "e D is already sized for; (2) assumed AS-003's interlock\n  system was working infrastructure, when AS-003 is actually In Progress\n  and blocked on the Gate 4 Cold Verification Harness. Sent back for\n  revision; Grok's second pass made both gaps explicit design\n  requirements (combined thermal-sink sizing calculation; AS-003\n  calibration as a hard operating prerequisite, not assumed\n  infrastructure) rather than open points. Revised sketch verified and\n  integrated as CE-006's vessel-design arti"
        },
        {
          "rank": 2,
          "source": "Architecture/Chemistry.md",
          "section": "Resolution Log",
          "text": " points. Revised sketch verified and\n  integrated as CE-006's vessel-design artifact, closing item 1 of the\n  four-item Resolution Path at the conceptual/architectural level only \u2014\n  no vessel built, AS-003 uncalibrated, thermal-sink calculation not yet\n  performed. Also noted 316L stainless as already-approved (via Air_\n  Scrubber.md's Corrosion Isolation doctrine) for Stage D's own hull,\n  distinct from the anode/Cl\u2082-line materials rule. CE-006 moved to In\n  Progress alongside CE-005/CE-007, s"
        },
        {
          "rank": 3,
          "source": "Architecture/Chemistry.md",
          "section": "full",
          "text": "entration) depends on CE-006's own remaining hardware gap (sealed vessel design, actual Cl\u2082 generation rate) \u2014 this file cannot close ahead of CE-006's vessel-design item. Payment via Specification once CE-006's hardware exists and these doctrinal answers are calibrated against real flow/volume data.\n\n---\n\n### CE-008 \u2014 Dilution doctrine competency validation not established\n\n| Field | Value |\n|-------|-------|\n| Status | Open |\n| Risk | Medium |\n| Priority | Minor |\n| Type | Technical / Safety |"
        },
        {
          "rank": 4,
          "source": "Architecture/Chemistry.md",
          "section": "full",
          "text": " design now exists where none did before. It does not close it at the hardware level: no vessel has been built, AS-003 is not yet calibrated, and the combined thermal-sink calculation has not been performed. CE-006 moves to **In Progress** \u2014 this is architecture, not a finished system.\n\n**Spec-depth pass, 2026-08-15 (digital-only \u2014 no equipment exists yet to generate operational data; three of the four remaining quantification items are paper-closeable regardless, one is not):**\n\n*Generation-rat"
        },
        {
          "rank": 5,
          "source": "Architecture/Chemistry.md",
          "section": "File State",
          "text": ", CE-005 narrowed to In Progress, CE-006/CE-007 given quantitative scrubber chemistry and storage doctrine (Grok content, verified against source before adoption), human-directed, 2026-07-31; Claude \u2014 CE-006 vessel design sketch integrated after two rounds of correction (thermal-sink sizing, AS-003 prerequisite gate) verified against Air_Scrubber.md source; CE-006 moved Open \u2192 In Progress, human-directed, 2026-07-31 |\n| Open Unknowns    | 8                                                        "
        }
      ]
    },
    {
      "id": 3,
      "class": "Rejected reasoning",
      "query": "Why was the independent Grok/Copilot thread's GOV-008 registry patch to Governance_Charter.md rejected, and what was preserved from it instead?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": " GOV-018 closure (2026-08-23), alongside Governance Fork Reconciliation\nin `Admin/Governance_Charter.md` and the Fork Reconciliation Track in\n`Admin/Governance_Migration_Protocol.md`. No overlapping or competing\nterms found elsewhere in the repository at registration time; the nearest\nneighbors \u2014 \"active constitutional invariant\" (`Admin/Auditor_Protocols.md`)\nand \"constitutional state\" (`Admin/Security_Protocols.md`) \u2014 are used in\nnarrower rollback/recovery contexts and are not renamed or super"
        },
        {
          "rank": 2,
          "source": "Operations/Gate_02_Triage.md",
          "section": "Lessons Learned",
          "text": "common components | Strategic Recoverability added as second triage axis; four-tier classification system | Analogous  | Yes                 |\n| 2026-08-02 | Cross-agent draft review | Copilot drafted TIL/TAL/TCM/TMV as an already-binding constitutional extension | Wrote candidate architecture as though it were ratified: invented a \"Spec Gate: Constitutional\" category not present in `Admin/Verification_Gates.md`, and bound it into `Admin/CIR_Gov.md` despite that file's own Binding Status explici"
        },
        {
          "rank": 3,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "`Admin/Forge_Audit_Kit.md` both cite Verification_Gates.md's Gate 3/6\ndirectly (correctly, no rename needed there) \u2014 but any file that was\nactually citing Governance_Charter.md's now-renamed checkpoints under the\nold \"Gate N\" name would now be citing a term that no longer exists in that\nfile, silently breaking the reference rather than erroring visibly.\n\n**Resolution Path:** Payment via Specification \u2014 grep the repository for\n\"Gate 1\" through \"Gate 6\" outside `Admin/Verification_Gates.md` and\n`O"
        },
        {
          "rank": 4,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "-------------|--------------------------|\n| Status        | In Progress \u2014 Vehicle    |\n| Risk          | Medium                   |\n| Priority      | Major                    |\n| Type          | Governance               |\n| Blocking      | No                       |\n| Owner         | Admin/Canonical_Terms.md |\n| First Logged  | 2026-07-03               |\n| Last Reviewed | 2026-07-03               |\n\n**Description:** `Admin/Governance_Charter.md`'s \"Canonical Verification\nGates\" (Gate 1\u20136) was re"
        },
        {
          "rank": 5,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "conflicts with `Admin/Verification_Gates.md` on\n   Verification Gate definitions or document-promotion vocabulary,\n   Verification_Gates.md is authoritative. Log the conflict as an\n   Active Dispute here and initiate reconciliation. Added 2026-07-03 after\n   this file failed to catch a real divergence between Verification Gates\n   and Governance_Charter.md's (then-named) \"Canonical Verification Gates\"\n   because Verification_Gates.md was never registered as an authority\n   source \u2014 see GOV-011, "
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "Resolution Log",
          "text": "entionally left for a separate patch. Operating as Synthesizer, human-directed.\n- 2026-08-06: **\u00a7VII.8 added \u2014 Registry Data Model & Runtime Gate (Extension, Not Yet Ratified), reconciliation of an independent multi-agent thread against source.** An independent Grok/Copilot thread produced a full parallel GOV-008 definition, quorum checklist, registry spec, and escalation protocol without loading this section, `Unknowns.md`, or `CIR_Gov.md` \u00a78.2. Its patch to insert a second GOV-008 definition d"
        },
        {
          "rank": 2,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "a \u00a7VIII Evidence-Sufficiency Gate, integrated the same day into `Admin/Governance_Migration_Protocol.md`. Full Closure Event above: Grok proposed (with a self-produced Revision 1 addressing seven amendments requested by ChatGPT's prior Skeptic pass), Claude independently verified the revision against those seven amendments (Pass, ready for ratification), the Human Governing Authority ratified.\n\n**Residual:** GMP-010-R1 \u2014 mechanical harness flag for cross-references into non-Verified / Directed A"
        },
        {
          "rank": 3,
          "source": "Admin/Progress_Log.md",
          "section": "full",
          "text": "s campaign's full cycle earlier in the session.\n  Human-directed.\n\n### 2026-09-03 \u2014 Dual integrity repair after ChatGPT REVISE/G6-BLOCKED audits of Governance_Charter.md and Governance_Migration_Protocol.md\nGrok independently confirmed both ChatGPT audits (all primary findings held under source check). Applied surgical repairs only \u2014 no constitutional or migration architecture redesign:\n\n**Governance_Charter.md**\n- Added FROZEN markers to Tier 1 Axioms, Integrity Enforcement Architecture (GOV-00"
        },
        {
          "rank": 4,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "ly into `Governance_Charter.md` was **rejected** \u2014 `Unknowns.md`'s canonical GOV-008 entry already points here, and a second Charter-level definition would recreate the exact \"colliding local GOV-008\" incident this repository already logged and corrected 2026-07-28 (renamed to `CIR-001`). The thread's Model/Evidence Independence framing (\u00a72.1\u20132.2 of its draft) is also the repackaged-EQD drafting error this section's own opening paragraph warns against \u2014 advisory chat-session diversity is not gov"
        },
        {
          "rank": 5,
          "source": "Admin/Governance_Charter.md",
          "section": "Resolution Log",
          "text": "Full history: `Archive/Logs/Governance_Charter_Changelog.md` (relocated\nout of this file 2026-07-23 \u2014 every entry preserved verbatim, none\nedited or summarized in the move).\n\n**2026-08-11:** Pseudo-audit (Grok, same limits) \u2014 findings logged in\nsidecar changelog. Open Unknowns 20 match; GOV-003/005 Blocking Yes\ncorrect; GOV-015/018 Critical Priority left Blocking No (judgment calls).\nNo GOV-* closed. Spec Gates unchanged.\n\n**Version 0.10 (working) \u2014 2026-07-27.** GOV-021 formally registered\n(was"
        }
      ]
    },
    {
      "id": 4,
      "class": "Rejected reasoning",
      "query": "Why was the 2026-07-29 \"CIR v2.0\" bundle held as unratified draft material rather than applied alongside CIR-F02/CIR-F03?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/CIR_Gov.md",
          "section": "Lessons Learned",
          "text": "- CIR-GOV-002 (2026-08-18): a predicate comparing a composite quantity to its own multiplicative factor is circular regardless of the factor's value range \u2014 fix by defining an explicit pre-aggregate term that structurally excludes the tested factor, and check every occurrence of the old form across the file, not just the one a proposal was drafted against.\n\n---"
        },
        {
          "rank": 2,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "-004, GH-012, CSL-A03) gained genuinely\n  complementary elaboration \u2014 a canonicalization envelope constraint\n  for GH-004, a simpler baseline yield ratio alongside GH-012's\n  existing stratified metric, and a concrete \u0394_physical test for\n  CSL-A03's existing expiry trigger \u2014 all explicitly marked Placeholder\n  / Internally Derived, none changing Status or Open Unknowns. Four\n  entries (GH-007, GH-008, GH-009, GH-011) already had more specific,\n  better-grounded resolution paths than the proposal"
        },
        {
          "rank": 3,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "ployment cycle (fields: anomaly_class, total_submissions, feasible_count, yield_rate, reporting_period). Placeholder / Internally Derived \u2014 no numerical target asserted, no collection has occurred. This is a coarser, earlier-available companion metric, not a replacement for the stratified version above.\n\n*Surfaced by Gemini review, 2026-06-24.*\n\n---\n\n### GH-013 \u2014 Conceptual salvage artifact storage mechanism undefined\n\n| Field         | Value                            |\n|---------------|-------"
        },
        {
          "rank": 4,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "Lessons Learned",
          "text": "06) as sufficiently settled for another file (CLF-004) to build on before independent verification | The underlying mechanism was wrong; caught by chance two days later via an external model's flag and a manufacturer datasheet, not by any structural check this repository runs on itself | A directed approach and ratified doctrine carry different epistemic weight in principle, but nothing previously stopped a directed approach from being *treated* as load-bearing before it earned that weight \u2014 sil"
        },
        {
          "rank": 5,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": " already had more specific,\n  better-grounded resolution paths than the proposal series offered\n  (GH-007 and GH-008 already tie to the real `simulation_fidelity_\n  version`/`validated_on_machinery_revision` schema fields; GH-009\n  already defines Interaction Volume, more concrete than a generic\n  interaction matrix; GH-011 already specifies a pre-Stage-1 merge\n  pass) \u2014 the proposal's versions of these would have been a downgrade\n  if merged, so they weren't. CSL-A05's existing expiry trigger a"
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "File State",
          "text": "review nor its own \"no gate behavior changes\" claim caught. Verified directly against this file \u2014 not accepted from an unverified larger document set on the strength of its framing alone \u2014 since S(n)=0 became structurally unreachable the moment the floor patch landed, silently disabling the gate. A broader \"CIR v2.0\" proposal bundled alongside this same finding was not applied: it deletes elements of the ratified Definition 1 five-tuple without acknowledgment, introduces an unratified U(n) term "
        },
        {
          "rank": 2,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "full",
          "text": "view nor its own \"no gate behavior changes\" claim caught. Verified directly against this file \u2014 not accepted from an unverified larger document set on the strength of its framing alone \u2014 since S(n)=0 became structurally unreachable the moment the floor patch landed, silently disabling the gate. A broader \"CIR v2.0\" proposal bundled alongside this same finding was not applied: it deletes elements of the ratified Definition 1 five-tuple without acknowledgment, introduces an unratified U(n) term al"
        },
        {
          "rank": 3,
          "source": "Admin/CIR_Gov.md",
          "section": "Resolution Log",
          "text": "target inversion warning added inline. Also: Highest Risk raised Medium\u2192High, ASM-CIR-002 reframed from a confidence rating to a documented design-completeness gap (Checkpoints 2/4 have zero predicate coverage), Open Unknowns field corrected to describe CIR-GOV-001 (this file's own tracked item) rather than conflating it with the separately-owned GOV-008 dependency. Declined to integrate: worked micro-examples (3 test vectors) \u2014 genuinely useful but lower priority than the structural gaps above;"
        },
        {
          "rank": 4,
          "source": "Admin/Progress_Log.md",
          "section": "Resolution Log",
          "text": "is already properly dated within\n  RIP-001's own Resolution Log entry (2026-06-27), not free-floating\n  undated text \u2014 lower urgency than flagged. A parallel Gemini review\n  (Vector 1) repeated two already-resolved claims as new top-priority\n  work (CIR and Nothingness_Theorem missing Scope Boundary sections) \u2014\n  both checked and confirmed already present; not applied, since there\n  was nothing to apply. Human-directed.\n\n- 2026-08-11: **EC-002 (Anti-Weaponization pattern-matching mechanism)\n  re"
        },
        {
          "rank": 5,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "File State",
          "text": "patch discipline the 2026-07-29 rejected \"CIR v2.0\" bundle established as precedent. Human-directed. \u2014 v0.23, 2026-08-07 \u2014 \u00a74.6.2's Independence Predicate gained a port note: `Architecture/Cognitive_Frameworks.md` \u00a7IX.3 now has an equivalent disjunctive rule for the ordinal Confidence Labels, reusing this predicate and its CF-002 cross-reference unchanged rather than deriving new independence criteria \u2014 sound because the five labels are totally ordered, so the same min/max structure applies with"
        }
      ]
    },
    {
      "id": 5,
      "class": "Unknown history",
      "query": "What was previously unresolved about ENV-007 and ENV-008, and how long had each sat unrevisited before being corrected?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/Economics.md",
          "section": "Lessons Learned",
          "text": "| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |\n|------|---------------|----------------|-------------|------------------|------------|---------------------|\n| 2026-07-06 | Governance | CT-007 (Canonical_Terms.md) identified an `EC-` prefix collision between this file and `Ethical_Constraints.md` | Rename not yet executed | ECN-001 through ECN-005 (all five of this file's own EC- entries, including Resolved ECN-003) renamed from `EC-`"
        },
        {
          "rank": 2,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "ed* or *how it was derived*. These labels do not\nreplace, weaken, or alter the existing AP-006 confidence/provenance axes\nor the UNKNOWN / PROVISIONAL / VERIFIED epistemic states.\n\n| Label | Definition | Typical relationship to AP-006 axes | Notes / non-goals |\n|---|---|---|---|\n| **FACT** | Asserted as true independent of this repository's internal reasoning | Almost always Measured + Experimentally Verified or Operationally Hardened | External reality claims only. Repository-internal conclusio"
        },
        {
          "rank": 3,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "tration (joins GH-007 through GH-012 already outstanding there)\" \u2014 stale on arrival. GH-007 through GH-012 were already registered in `Unknowns.md` since v4.1 (2026-06-24), and GH-013 itself was registered the same day as this entry, per `Unknowns.md` v4.18. Nothing was actually outstanding.)*\n\n---\n\n- 2026-08-03: **Corrective merge \u2014 AP-033, human-directed.** A Copilot\n  proposal series, produced with no confirmed access to this file's\n  sidecar or `Admin/Auditor_Protocols.md`, declared 16 of th"
        },
        {
          "rank": 4,
          "source": "Admin/Economics.md",
          "section": "Lessons Learned",
          "text": "e of this file's own EC- entries, including Resolved ECN-003) renamed from `EC-` to `ECN-` to close the collision. CT-007's original write-up cited EC-008 as a sixth colliding ID \u2014 verified against this file directly: EC-008 does not exist here, that citation was in error. It also omitted EC-003 as a collision, likely because it is Resolved and drops out of Unknowns.md's active index \u2014 resolved status does not retire an ID from the shared namespace. | High \u2014 verified directly against source text"
        },
        {
          "rank": 5,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "d appears to be the erroneous claim, not the reverse. Any reference to an\n\"EC-00X\" unknown anywhere in the repository is now ambiguous without an\nexplicit file qualifier until this is fixed.\n\n**Why It Matters:** This is a live G5 (Cross-Reference Integrity) problem\nat the repository level, not a future risk to plan around. Every past and\nfuture reference to an EC-numbered unknown that doesn't name its owning\nfile explicitly is currently unreliable.\n\n**Resolution Path:** Economics.md's five colli"
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Security_Protocols.md",
          "section": "Resolution Log",
          "text": "ing change. Mirrored\n  in Unknowns.md's Active Index and cross-referenced from Electronics.md's\n  EL-006 entry. Human-directed.\n\n- 2026-09-10: **SEC-007b sidecar corrected \u2014 \"blocked pending SEC-007a\" had gone stale.** SEC-007a Ratified 2026-08-22; this sidecar's Blocking field, Resolution Path, and Last Reviewed date still described SEC-007b as waiting on it, three weeks after ratification. Grok's correction-grep flagged this; Claude verified the SEC-007a ratification date against its own FROZE"
        },
        {
          "rank": 2,
          "source": "Admin/Security_Protocols.md",
          "section": "Resolution Log",
          "text": "yet been split into SEC-007a/SEC-007b to match\n  `Unknowns.md` v4.4; PAT-001/PAT-002 are written against the split IDs\n  pending that reconciliation. Open Unknowns unchanged at 11 (EDL logs\n  decisions on existing unknowns; introduces no new ones itself).\n\n- **2026-07-02** \u2014 SEC-007 sidecar entry split into SEC-007a (constitutional\n  requirements, owning layer Admin) and SEC-007b (physical implementation,\n  owning layer Operations; blocked pending SEC-007a), closing the reconciliation\n  gap flag"
        },
        {
          "rank": 3,
          "source": "Unknowns.md",
          "section": "full",
          "text": "ors, EC-008's own explicit non-resolution); currently-covered (EL-006 admission-time wipe, non-integrable classes) vs. not-covered (ongoing attestation, runtime compromise detection) distinguished; open questions listed (minimum attestation required, behavior on missing/failed attestation, salvaged-sensor honest limitation, degraded-attestation residual). Scope fenced from EC-011 (permission-source vs. telemetry compromise), EL-006/SEC-007b (admission/constitutional trust vs. ongoing sensor hone"
        },
        {
          "rank": 4,
          "source": "Admin/Progress_Log.md",
          "section": "Resolution Log",
          "text": "5-04, EC-008/009\n  still read 2026-06-18, unchanged since the original registration despite\n  all being closed this session) \u2014 and one claim that no longer held: its\n  proposed fix for an ambiguous \"Open Unknowns: 8\" header assumed the\n  header didn't already distinguish substantively-open from\n  pending-ratification entries, but the parenthetical naming those six\n  items by name was already present from the prior correction pass.\n  Adopted the genuine fix (five dates corrected to 2026-08-22) an"
        },
        {
          "rank": 5,
          "source": "Admin/Security_Protocols.md",
          "section": "Resolution Log",
          "text": "agged this; Claude verified the SEC-007a ratification date against its own FROZEN marker and PAT-001's entry before fixing. Corrected all three live fields; the file's own historical Resolution Log entry describing the original 2026-07-02 split (accurate as of that date) left untouched. Mirrored in Unknowns.md's Active Index row. Human-directed.\n\n- 2026-08-10: **SEC-007a deferral trigger cross-linked (Claude review + Grok\n  apply).** Blocking remains No (constitutional item; no automated agent m"
        }
      ]
    },
    {
      "id": 6,
      "class": "Unknown history",
      "query": "What was GOV-008's status before the \u00a7VII.8 registry-schema extension, and did that extension change it?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": " GOV-018 closure (2026-08-23), alongside Governance Fork Reconciliation\nin `Admin/Governance_Charter.md` and the Fork Reconciliation Track in\n`Admin/Governance_Migration_Protocol.md`. No overlapping or competing\nterms found elsewhere in the repository at registration time; the nearest\nneighbors \u2014 \"active constitutional invariant\" (`Admin/Auditor_Protocols.md`)\nand \"constitutional state\" (`Admin/Security_Protocols.md`) \u2014 are used in\nnarrower rollback/recovery contexts and are not renamed or super"
        },
        {
          "rank": 2,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "Defined under GOV-018.\n\n**Ratified Constitutional Lineage**\nA lineage (or an explicit continued-fork arrangement) whose package has\nbeen ratified by the Human Governing Authority as the active constitutional\nsurface, or as an approved forked state. The terminal state in the Claimed\n\u2192 Recognized \u2192 Ratified progression. Defined under GOV-018.\n\n*Implementation status: all four terms registered as canonical vocabulary\nat GOV-018 closure (2026-08-23), alongside Governance Fork Reconciliation\nin `Admi"
        },
        {
          "rank": 3,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": " scope was\nAuditor_Protocols.md specifically, which is now closed.\n\n---\n\n### Resolution Log\n\n- 2026-09-23: **Claim-Type Labels registered (\u00a74).** Nine-label taxonomy\n  (FACT/MEASUREMENT/OBSERVATION/INFERENCE/ASSUMPTION/PROPOSAL/UNKNOWN/\n  DECISION/AUTHORIZATION) distinguishing claim *type* from AP-006's\n  existing confidence/provenance *axes*. Minimal shape only \u2014 definitions\n  plus a two-question usage rule, no retroactive relabeling of existing\n  content and no change to AP-006, EC-001, EC-008"
        },
        {
          "rank": 4,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "\n**Resolution Path:** Not yet defined. Candidate questions to resolve before a schema can be proposed: Does this warrant its own object type analogous to but structurally distinct from the Heuristic Object, or a different mechanism entirely (e.g., routing directly into `Unknowns.md` as a differently-flavored entry, or a dedicated companion file)? What replaces `validated_on_machinery_revision` as the artifact's \"is this still current\" check, given there's no machinery to revise against? Does Can"
        },
        {
          "rank": 5,
          "source": "Operations/Gate_02_Triage.md",
          "section": "Lessons Learned",
          "text": "common components | Strategic Recoverability added as second triage axis; four-tier classification system | Analogous  | Yes                 |\n| 2026-08-02 | Cross-agent draft review | Copilot drafted TIL/TAL/TCM/TMV as an already-binding constitutional extension | Wrote candidate architecture as though it were ratified: invented a \"Spec Gate: Constitutional\" category not present in `Admin/Verification_Gates.md`, and bound it into `Admin/CIR_Gov.md` despite that file's own Binding Status explici"
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "ven this section \u2014 if ratified \u2014 would itself be Tier-1-adjacent constitutional structure, not a routine Track A change. Do not treat drafting this section as itself satisfying any part of GOV-008.\n\n### VII.8 Registry Data Model & Runtime Gate (Extension, Not Yet Ratified)\n\n**Provenance and status:** an independent multi-agent thread (Grok/Copilot, 2026-08-06, human-directed) drafted a full parallel GOV-008 definition, checklist, registry spec, and escalation protocol \u2014 without ever loading this"
        },
        {
          "rank": 2,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "ed a full parallel GOV-008 definition, quorum checklist, registry spec, and escalation protocol without loading this section, `Unknowns.md`, or `CIR_Gov.md` \u00a78.2. Its patch to insert a second GOV-008 definition directly into `Governance_Charter.md` was rejected: `Unknowns.md`'s canonical entry already owns GOV-008 here, and a second Charter-level definition would recreate the \"colliding local GOV-008\" incident already corrected 2026-07-28. Its Model/Evidence Independence framing was identified a"
        },
        {
          "rank": 3,
          "source": "Archive/Logs/Governance_Charter_Changelog.md",
          "section": "Resolution Log",
          "text": " vs. the\n  architectural/hardware independence and enforcement substrate GOV-008\n  actually requires) is visible from this entry directly, not only from\n  EQD's side. No change to GOV-008's Status, Risk, or Resolution Path \u2014\n  this entry remains Open, unaffected in substance by EQD's existence.\n\n- 2026-07-23: **Sidecar and Resolution Log relocated to `Archive/Logs/Governance_Charter_Changelog.md`** (human-directed), matching the precedent set the same day by `Admin/Auditor_Protocols.md`'s reloca"
        },
        {
          "rank": 4,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "Resolution Log",
          "text": "entionally left for a separate patch. Operating as Synthesizer, human-directed.\n- 2026-08-06: **\u00a7VII.8 added \u2014 Registry Data Model & Runtime Gate (Extension, Not Yet Ratified), reconciliation of an independent multi-agent thread against source.** An independent Grok/Copilot thread produced a full parallel GOV-008 definition, quorum checklist, registry spec, and escalation protocol without loading this section, `Unknowns.md`, or `CIR_Gov.md` \u00a78.2. Its patch to insert a second GOV-008 definition d"
        },
        {
          "rank": 5,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "Resolution Log",
          "text": "y of it currently exists. No status change to\n  GOV-008 itself resulted from this pass; per the review's own fourth\n  recommendation, no progress on GOV-008 may be claimed until a real\n  second runtime exists. Operating as Synthesizer per\n  Auditor_Protocols.md v0.29, human-directed.\n\n- 2026-07-31: **v0.8 \u2014 \u00a7VII Bootstrap Quorum Doctrine added as a\n  candidate GOV-008 specification**, drafted from an external candidate\n  spec and refined after verifying its claims against GOV-008's actual\n  side"
        }
      ]
    },
    {
      "id": 7,
      "class": "Resolution history",
      "query": "How was the Support_Raft induction-loss discrepancy (12% laboratory vs. 20\u201340% real subsea conditions) resolved and logged?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Tests/Support_Raft.md",
          "section": "Lessons Learned",
          "text": "| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |\n|---|---|---|---|---|---|---|\n| May 2026 | Analogous data correction | Induction loss estimated at 12% | Laboratory-optimistic; real subsea conditions with seawater conductivity, alignment variance, and biofouling push losses to 20\u201340% | Always use field analog data for marine energy estimates, not laboratory figures | Analogous | Yes \u2014 pending SR-004 field-measured data |\n| May 2026 | A"
        },
        {
          "rank": 2,
          "source": "Operations/Air_Scrubber.md",
          "section": "Lessons Learned",
          "text": "| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |\n|------|---------------|----------------|-------------|------------------|------------|---------------------|\n| May 2026 | Modeling | Variant 4 marine claimed 10\u2013100 atm range with 20\u201350% power uplift | Physically untenable \u2014 isothermal compression to 100 atm requires massive work; 150W compressor cannot overcome hydrostatic pressure | Deep-sea compression is a separate power class. v0 m"
        },
        {
          "rank": 3,
          "source": "Operations/Gate_05_Separation_Thermal.md",
          "section": "Lessons Learned",
          "text": "| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |\n|------|---------------|----------------|-------------|------------------|------------|---------------------|\n| 2026-05-15 | Modeling | Back-of-envelope centrifugal pressure and hoop stress calculation for 400 RPM never-exceed at worst-case v0 geometry | Nothing failed \u2014 calculation ran cleanly | At 400 RPM, worst-case centrifugal pressure on the crucible wall is ~0.037 MPa, producing ~0"
        },
        {
          "rank": 4,
          "source": "Operations/Gate_07_Utilization.md",
          "section": "Lessons Learned",
          "text": "| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |\n|------|---------------|----------------|-------------|------------------|------------|---------------------|\n| 2026-05-19 | Audit Review | Utilization conceived as terminal stage \u2014 parts enter service and system moves on | Without feedback loop, fabrication becomes industrial output not adaptive learning. Precision ceiling stagnates, wire quality problems repeat, self-replication loop h"
        },
        {
          "rank": 5,
          "source": "Operations/Gate_06_Fabrication.md",
          "section": "Lessons Learned",
          "text": "e tracking | An untracked precision ceiling produces parts that appear correct but fail in service when actual ceiling is lower than assumed. Silent failure from overconfident tolerance claims is worse than acknowledged limitation | Precision ceiling is a first-class tracked metric, not a background assumption. It cannot exceed metrology capability. It must be documented honestly in fabrication records. Purchasing precision instruments at bootstrap is correct doctrine \u2014 precision is seeded delib"
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Tests/Support_Raft.md",
          "section": "full",
          "text": ") is a more reliable planning figure than the original laboratory estimate (12%) | Lessons Learned entry \u2014 laboratory figure was corrected against real subsea conditions (seawater conductivity, alignment variance, biofouling) | Medium \u2014 corrected once already, still Analogous rather than Measured | SR-004 (induction charging pad design) resolved with field-measured loss data |\n| ASM-005 | The Raft can be treated as replaceable-by-design without that undermining swarm reliability, provided a next"
        },
        {
          "rank": 2,
          "source": "Tests/Support_Raft.md",
          "section": "full",
          "text": "n submerged hull sections\n- Induction loss budget: 20\u201340% under real subsea conditions accounting for seawater conductivity, alignment variance, and biofouling (Estimated \u2014 corrected from laboratory-optimistic 12% per Lessons Learned)\n- Regional transmission loss: 5% (Analogous)\n\n---\n\n### Stasis Mode\n\nIf energy reserves fall below 20% of capacity:\n\n**Suspended (in order of shed):**\n1. Material Separation Gate \u2014 first non-essential load shed\n2. Data Tether and satellite uplink\n3. Docking charging"
        },
        {
          "rank": 3,
          "source": "Tests/Support_Raft.md",
          "section": "Resolution Log",
          "text": "\n| Date | Entry |\n|---|---|\n| 2026-05-04 | Induction loss estimate corrected from 12% (laboratory) to 20\u201340% (real subsea conditions). Logged in Lessons Learned. |\n| 2026-05-04 | Stasis Mode single-point-of-failure contradiction resolved \u2014 recovery beacon and passive mechanical recovery remain active regardless of energy state. |\n| 2026-05-06 | Cold storage rack concept added to Stasis Mode section \u2014 resolves dead-unit-clog contradiction identified by Gemini audit. |\n| 2026-05-06 | Foundational "
        },
        {
          "rank": 4,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "full",
          "text": "in TBD/Placeholder. Until SR-006 / SR-007 (and the Leviathan unit physical envelope dependency) resolve, Support_Raft contributes only the default $S = \\varepsilon$.\n\n**Security_Protocols contribution:** used only for the authenticity column \u2014 cryptographic logging \u2192 `cryptographic`; multi-party hardware confirmation / air-gapped attestation \u2192 `multi_party`. Hull-breach / remote-wipe patterns inform the \"stale\" freshness rule but do not themselves raise $S$.\n\n**Freshness Rule (Minimal):** a valu"
        },
        {
          "rank": 5,
          "source": "Tests/Support_Raft.md",
          "section": "full",
          "text": "Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |\n|---|---|---|---|---|---|---|\n| May 2026 | Analogous data correction | Induction loss estimated at 12% | Laboratory-optimistic; real subsea conditions with seawater conductivity, alignment variance, and biofouling push losses to 20\u201340% | Always use field analog data for marine energy estimates, not laboratory figures | Analogous | Yes \u2014 pending SR-004 field-measured data |\n| May 2026 | Architectural review | Stasis M"
        }
      ]
    },
    {
      "id": 8,
      "class": "Resolution history",
      "query": "How was RIP-002's \"not yet implemented\" status corrected, and what exactly was verified to justify the change?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": " unqualified \"Blocking\"\n  usage. CT-006 and CT-007 logged. Open Unknowns 4 \u2192 6.\n- 2026-06-24: v0.3 continued \u2014 HF-001 (Heuristic Failure) defined in Section 4\n  per proposal in `Tests/Cognitive_Salvage_Layer.md` v0.2. CT-008 logged to\n  track cross-file consistency of HF-001 vocabulary. Drift Indicators updated:\n  HF-001 consistency rule and unqualified Blocking guardrail rule added.\n  All Last Reviewed dates updated. Open Unknowns 6 \u2192 7.\n\n---\n\n## Relationship to Existing Documents\n\n- `Architect"
        },
        {
          "rank": 2,
          "source": "Admin/Resolution_Methodology.md",
          "section": "Lessons Learned",
          "text": "hes internal staleness as well as external fabrication; \u00a74's \"stop when paper is exhausted\" outcome should be stated explicitly | Analogous | After a fourth case, or after hardware data changes CE-006's remaining open set |\n| 2026-08-16 | Fourth applied case (GR-007) | Applied after GR-003 doctrine existed from an earlier methodology case | Category C's hollow \"pending GR-003\" citation became fillable; A\u2013C all paper-complete | Methodology compounds \u2014 filling one hollow citation unblocks the next"
        },
        {
          "rank": 3,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "ates.md\nregistered as fourth vocabulary authority source.\n\n**Changes from v0.2:**\n- Section 4: HF-001 (Heuristic Failure) defined as first-class failure class\n- Drift Indicators: HF-001 consistency rule added; unqualified Blocking\n  guardrail rule added\n- CT-008 logged: HF-001 canonicalization status tracking\n- All Last Reviewed dates updated to 2026-06-24\n- Open Unknowns: 6 \u2192 7\n- Version string updated to 0.3\n\n**What must remain constant:**\n\n**Forge_flow.md governs operational routing semantics"
        },
        {
          "rank": 4,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "Lessons Learned",
          "text": "06) as sufficiently settled for another file (CLF-004) to build on before independent verification | The underlying mechanism was wrong; caught by chance two days later via an external model's flag and a manufacturer datasheet, not by any structural check this repository runs on itself | A directed approach and ratified doctrine carry different epistemic weight in principle, but nothing previously stopped a directed approach from being *treated* as load-bearing before it earned that weight \u2014 sil"
        },
        {
          "rank": 5,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "Priority Demotion Doctrine defines\n  Operational Blocking and Epistemic Blocking subtypes\n- `Admin/Forge_Audit_Kit.md` \u2014 Tier 3; CT- sidecar prefix in Sidecar ID\n  Reference table\n- `Admin/File_Template.md` \u2014 standard file structure\n- `Discovery.md` \u2014 Rename Registry is the canonical filename resolution source\n- `Tests/Cognitive_Salvage_Layer.md` \u2014 source of HF-001 proposal; CT-008\n  tracks cross-file vocabulary consistency\n- `Operations/Gate_02_Triage.md` \u2014 CT-002 Blocking for that file's Spec "
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Progress_Log.md",
          "section": "Resolution Log",
          "text": "is already properly dated within\n  RIP-001's own Resolution Log entry (2026-06-27), not free-floating\n  undated text \u2014 lower urgency than flagged. A parallel Gemini review\n  (Vector 1) repeated two already-resolved claims as new top-priority\n  work (CIR and Nothingness_Theorem missing Scope Boundary sections) \u2014\n  both checked and confirmed already present; not applied, since there\n  was nothing to apply. Human-directed.\n\n- 2026-08-11: **EC-002 (Anti-Weaponization pattern-matching mechanism)\n  re"
        },
        {
          "rank": 2,
          "source": "Admin/Repository_Integrity_Protocol.md",
          "section": "Resolution Log",
          "text": "g that a stated \"clean\" result was not itself evidence of an actual line-by-line read. (6) New Lessons Learned row added documenting the RIP-008 correction as a general lesson about not inheriting a prior unknown's severity without re-checking whether the risk profile actually matches. Open Unknowns unchanged at 7 (RIP-008 resolved, RIP-009 added \u2014 net zero).\n- 2026-07-08: **v0.6 \u2014 Phase 0 (Manual Execution via Recurring Agent Audit) tier added; RIP-002 partially mitigated (human-directed).** Th"
        },
        {
          "rank": 3,
          "source": "Admin/Repository_Integrity_Protocol.md",
          "section": "full",
          "text": "cope) |\n\n#### 7. Closure statement\n\n*Lightweight Revision Anchors and Deletion Detection \u2014 Payment via Specification for **RIP-011** and **RIP-012**. Adopts forward-only anchors + mandatory comparison-when-baseline-exists; refuses memory-as-control and false full-history crypto. Drafted by Grok, 2026-09-05, against live \u00a7Version Preservation, \u00a7Resolution Logs Protected Element, and RIP-010 drill outcome. Claude ran an independent Skeptic pass same day: first flagged that the initial draft mislab"
        },
        {
          "rank": 4,
          "source": "Admin/Repository_Integrity_Protocol.md",
          "section": "full",
          "text": "in for detail and cross-module index entries. Closed 2026-09-03 following ChatGPT audit finding RIP-AUD-001 (this entry had been left Open with a resolution path that already described the fix as done \u2014 a semantic-state defect, not a substantive gap). The remaining residual \u2014 escalation timing, review cadence, and the human-operator/audit-lead distinction \u2014 is not a location problem and belongs entirely to RIP-007, which remains Open for that reason.\n\n---\n\n### RIP-004 \u2014 Constitutional violation "
        },
        {
          "rank": 5,
          "source": "Admin/Repository_Integrity_Protocol.md",
          "section": "Resolution Log",
          "text": "nfidence/Drift Trend report format added;\n  Protocol Validation subsection and RIP-010 logged; Status section v0.8\n  omission corrected (human-directed, external ideation reviewed).**\n  Reviewed four externally-authored proposals (ChatGPT/Grok) against this\n  file's actual current text before adopting anything. Two were rejected\n  outright: an incident-response SLA proposal reopened exactly the framing\n  RIP-008 was corrected away from (importing rigid cycle-bound timing onto\n  a risk that doesn"
        }
      ]
    },
    {
      "id": 9,
      "class": "Governance reasoning",
      "query": "Why was the Closed_Loop_Feedstock draft's \"Resolved 2026-08-03\" status claim rejected rather than accepted?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/Auditor_Protocols.md",
          "section": "Lessons Learned",
          "text": " Closed AP-004; Proposer (Grok) had already revised its own draft once (Revision 1, addressing a prior independent review's three findings) before the Closure Event was opened | Grok again correctly declined to self-verify the Closure Event, second consecutive instance of the same behavior | Independent review of a draft and independent verification of the resulting Closure Event are related but distinct passes \u2014 one producing amendments, the other clearing the event for ratification \u2014 and treat"
        },
        {
          "rank": 2,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "Lessons Learned",
          "text": "06) as sufficiently settled for another file (CLF-004) to build on before independent verification | The underlying mechanism was wrong; caught by chance two days later via an external model's flag and a manufacturer datasheet, not by any structural check this repository runs on itself | A directed approach and ratified doctrine carry different epistemic weight in principle, but nothing previously stopped a directed approach from being *treated* as load-bearing before it earned that weight \u2014 sil"
        },
        {
          "rank": 3,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "ciple (\"every idea is provisional feedstock...\") is recorded as provisional, not ratified doctrine. GH-013 registered for the storage/object-schema gap this subsection cannot resolve on its own \u2014 marked Blocking specifically for this subsection's advancement, not for the file as a whole. Open Unknowns 12 \u2192 13. *(Correction, 2026-07-19: this entry originally said \"Unknowns.md requires update: GH-013 global index registration (joins GH-007 through GH-012 already outstanding there)\" \u2014 stale on arri"
        },
        {
          "rank": 4,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "en a downgrade\n  if merged, so they weren't. CSL-A05's existing expiry trigger already\n  matched the proposal exactly (dependent on GH-003) \u2014 nothing to add.\n  Open Unknowns unchanged at 13. Status/Spec Gates unchanged\n  (Exploration, 1/6).\n\n## Abandoned Paths\n\n| Date      | Path                                                     | Why Abandoned                                                              | Reconsider? |\n|-----------|----------------------------------------------------------|--"
        },
        {
          "rank": 5,
          "source": "Admin/Resolution_Methodology.md",
          "section": "Lessons Learned",
          "text": "hes internal staleness as well as external fabrication; \u00a74's \"stop when paper is exhausted\" outcome should be stated explicitly | Analogous | After a fourth case, or after hardware data changes CE-006's remaining open set |\n| 2026-08-16 | Fourth applied case (GR-007) | Applied after GR-003 doctrine existed from an earlier methodology case | Category C's hollow \"pending GR-003\" citation became fillable; A\u2013C all paper-complete | Methodology compounds \u2014 filling one hollow citation unblocks the next"
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Progress_Log.md",
          "section": "full",
          "text": "t boundary appears to have swallowed both rather than just \u00a712.\n  Restored the full section verbatim, plus this entry, before doing\n  anything else with the upload. GOV-021c's own content was verified\n  separately and is being evaluated on its merits, unaffected by this\n  fix. Human-directed.\n\n- 2026-08-11: **First item ratified purely on documentation-completeness\n  grounds: CLF-010 (Closed_Loop_Feedstock.md \u00a74a).** Surveyed the whole\n  repo for genuinely ready-to-ratify items before picking th"
        },
        {
          "rank": 2,
          "source": "Admin/Progress_Log.md",
          "section": "Resolution Log",
          "text": "h the upload. GOV-021c's own content was verified\n  separately and is being evaluated on its merits, unaffected by this\n  fix. Human-directed.\n\n- 2026-08-11: **First item ratified purely on documentation-completeness\n  grounds: CLF-010 (Closed_Loop_Feedstock.md \u00a74a).** Surveyed the whole\n  repo for genuinely ready-to-ratify items before picking this one \u2014\n  checked CIR_Gov.md (explicitly sequenced behind GOV-008, which needs\n  physical hardware not yet available \u2014 correctly stays Proposed) and\n "
        },
        {
          "rank": 3,
          "source": "Challenges/Waste.md",
          "section": "Resolution Log",
          "text": " correction was also applied to this file's pre-existing BFR paragraph, which had carried the same \"validated\" overclaim since before this session. Added: an explicit training/demonstration standard (T1\u2013T6), a confirmatory lab-arrangement structure with a hard authority-boundary rule (lab result is evidence supplied to disposition authority, not itself an authorization), and a three-way residual classing distinguishing the epistemic/blocking residual (WA-002-R1, feedstock validation) from non-bl"
        },
        {
          "rank": 4,
          "source": "Operations/Gate_04_Separation_Mechanical.md",
          "section": "Resolution Log",
          "text": "o MG-*\n  closed.** Open Unknowns remain 8. Blocking status unchanged (all\n  No). Human-directed.\n- 2026-09-09: **MG-009 added** (provisional feedstock envelope table\n  drifted from Gate_03_Reduction.md's mirror table \u2014 found while\n  scoping FL-002 in Architecture/Forge_flow.md; logged rather than\n  fixed directly, closes automatically when FL-002 resolves). **Same\n  pass: merged a diverged duplicate Resolution Log section.** This\n  file had two copies of its Resolution Log \u2014 one positioned here,"
        },
        {
          "rank": 5,
          "source": "Challenges/Cha_Scope_Map.md",
          "section": "Resolution Log",
          "text": "- 2026-08-08: **File created \u2014 fourth folder in the Scope_Map rollout**,\n  following Admin/ (2026-08-07), Architecture/ and Operations/ (both\n  2026-08-08). All 9 Challenges/ files' subtype, Status, and full scope\n  content extracted directly from source. One extraction false-positive\n  (`Closed_Loop_Feedstock.md` appeared to have no Scope Boundary section\n  on first pass, due to this folder's numbered-heading convention) caught\n  and corrected before being stated as a finding \u2014 documented as a "
        }
      ]
    },
    {
      "id": 10,
      "class": "Governance reasoning",
      "query": "Why does AP-033 (Rule 9) require confirmed governance-file access before a contribution can mark an unknown toward Resolved status?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Operations/Gate_02_Triage.md",
          "section": "Lessons Learned",
          "text": " bound it into `Admin/CIR_Gov.md` despite that file's own Binding Status explicitly forbidding this | Cross-agent architectural drafts are useful but default to overclaiming operative status; every such draft needs to be checked against the actual gate/ratification state of every file it claims to extend, not just against plausibility | Analogous | Yes \u2014 recheck if \u00a7XII is ever promoted toward actual gate passage |\n\n---"
        },
        {
          "rank": 2,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "`Admin/Governance_Charter.md`'s \"Canonical Verification\nGates\" (Gate 1\u20136) was renamed to \"Enforcement Checkpoints\" (Checkpoint\n1\u20136) on 2026-07-03 to end a naming collision with this file's\n`Admin/Verification_Gates.md`-owned Verification Gate definition \u2014 see\nGOV-011. `Admin/Verification_Gates.md` also received a disambiguation\nnote confirming sole ownership of unqualified \"Gate\"/\"canonical\"\nterminology in its domain. CT-010 tracks whether every file that cites\n\"Gate 3,\" \"Gate 6,\" or similar in "
        },
        {
          "rank": 3,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "                 | Governance_Charter.md places Forge_flow.md in Tier 5; derived file cannot contradict constitutional source | No     |\n| 2026-05-27 | This file as primary ontology superseding Forge_flow.md                | Forge_flow.md is the operational routing authority; this file is the cross-file consistency enforcer | No          |\n\n---\n\n## Drift Indicators\n\nMandatory re-audit conditions for this document:\n\n- Conflict resolution doctrine removed or simplified to single-source authority\n-"
        },
        {
          "rank": 4,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "         | Governance / Technical   |\n| Blocking      | **Epistemic \u2014 see below** |\n| Owner         | Admin/Canonical_Terms.md |\n| First Logged  | 2026-06-23               |\n| Last Reviewed | 2026-07-05               |\n\n**Description:** No formal doctrine governs whether IDs may be reused after\nresolution, how ranges are reserved for new clusters, how collisions are\nhandled if two files claim the same prefix, or how multi-owner cross-module\nunknowns are numbered.\n\n**Escalation 2026-07-05 \u2014 this "
        },
        {
          "rank": 5,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "    |\n| Priority      | Major                            |\n| Type          | Governance                       |\n| Blocking      | Epistemic                        |\n| Owner         | Tests/Cognitive_Salvage_Layer.md |\n| First Logged  | 2026-06-24                       |\n| Last Reviewed | 2026-06-24                       |\n\n**Description:** NOVEL status requires a formal multi-dimensional threshold. No heuristic may receive NOVEL status until this resolves \u2014 enforced via CANDIDATE_NOVEL and hard "
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "File State",
          "text": ".16 header date, which is circumstantial at best. (5) A fifth issue, not raised by the prior audit: G3's \"blocked by AP-012/AP-016\" status directly contradicts `Admin/Auditor_Protocols.md` line 774, which records Gate 3 Clear as of 2026-08-03 \u2014 four days before this file's own v0.23 touch. Flagged inline at \u00a77.4 and in File State rather than resolved, since changing a Gate status is a call for this file's owner, not an editing pass. Human-directed.) \u2014 v0.25, 2026-08-18 \u2014 G3 contradiction resolve"
        },
        {
          "rank": 2,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "n Human Authority's ratification decisions as of this writing (checked\nagainst `Admin/Governance_Charter.md` and this file directly) \u2014 if such\nan obligation is adopted later, it must be reconciled with this design\nnote explicitly rather than silently overriding it. GMP-008 may later\naddress stalled Phase 1/2 proposals; it should not silently expire a\nPhase 3 item awaiting human ratification without explicit Human\nAuthority policy.\n\n### III.A.7 Explicit non-claims and residuals\n\n| Item | Disposit"
        },
        {
          "rank": 3,
          "source": "Archive/Logs/Auditor_Protocols_Logs.md",
          "section": "Resolution Log",
          "text": "This targets root cause (missing governance-file\n  access), not just the symptom \u2014 the underlying engineering in the\n  proposals was often reasonable, the failure was epistemic framing,\n  not incompetence. Merged the legitimate easy-set definitions into\n  `Tests/Cognitive_Salvage_Layer.md`'s sidecar as pure Payment via\n  Specification (see that file's own Resolution Log); did not merge\n  the medium or hard sets. Open Unknowns 14 \u2192 15 briefly, then AP-033\n  resolved same day like AP-031/AP-032 be"
        },
        {
          "rank": 4,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "full",
          "text": "6 header date, which is circumstantial at best. (5) A fifth issue, not raised by the prior audit: G3's \"blocked by AP-012/AP-016\" status directly contradicts `Admin/Auditor_Protocols.md` line 774, which records Gate 3 Clear as of 2026-08-03 \u2014 four days before this file's own v0.23 touch. Flagged inline at \u00a77.4 and in File State rather than resolved, since changing a Gate status is a call for this file's owner, not an editing pass. Human-directed.) \u2014 v0.25, 2026-08-18 \u2014 G3 contradiction resolved."
        },
        {
          "rank": 5,
          "source": "Archive/Logs/Auditor_Protocols_Logs.md",
          "section": "Resolution Log",
          "text": "is-enumerated the\n  unknown set itself (GH-005 omitted, a nonexistent \"GH-014\"\n  invented). A second agent (Grok), with confirmed access, correctly\n  diagnosed every violation unprompted and produced a clean,\n  properly-scoped rewrite. Added Rule 9 (Resolution Claims Require\n  Governance Access) generalizing Rule 8's file-level check to the\n  individual-unknown level; extended Fallacy Checklist item 4\n  accordingly. This targets root cause (missing governance-file\n  access), not just the symptom"
        }
      ]
    },
    {
      "id": 11,
      "class": "Technical reasoning",
      "query": "What led to CIR-F03's correction of \u03a6(n)'s trigger condition from S(n)=0 to S(n)\u2264\u03b5, and why didn't the original CIR-F02 review catch it?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/CIR_Gov.md",
          "section": "Lessons Learned",
          "text": "- CIR-GOV-002 (2026-08-18): a predicate comparing a composite quantity to its own multiplicative factor is circular regardless of the factor's value range \u2014 fix by defining an explicit pre-aggregate term that structurally excludes the tested factor, and check every occurrence of the old form across the file, not just the one a proposal was drafted against.\n\n---"
        },
        {
          "rank": 2,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "oes the sequence close off access to later joints?\n\n*Fail outcomes:* MATERIAL_FAILURE or HAZARDOUS_SEQUENCE.\n\n*S2R Delta trigger (GH-003 partial mitigation):* If physical execution of a promoted heuristic encounters more than a defined variance threshold in expected torque, resistance, or thermal profile, the heuristic is immediately demoted to UNSAFE quarantine and the simulation model is flagged for recalibration. The specific variance threshold is Placeholder pending first physical execution "
        },
        {
          "rank": 3,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "n-to-physical fidelity is low, promoted heuristics may pass Stage 3 while failing in physical execution. This assumption requires empirical validation before any heuristic reaches Operational Spec status.\n\n**CSL-A03 elaboration (Payment via Specification, added 2026-08-03 \u2014 human-directed, corrective merge from a Copilot/Grok exchange, see AP-033):** the expiry trigger above (\"Stage 3 validation pass on first physical anomaly\") elaborated as a concrete test: at the first physical anomaly that ge"
        },
        {
          "rank": 4,
          "source": "Admin/Governance_Charter.md",
          "section": "Lessons Learned",
          "text": "fter direct questioning of whether Gate_03 already articulated reversibility | Nothing failed in the first three; GOV-022's initial \"reject as redundant\" lean (from both Grok and ChatGPT) turned out wrong once source was actually checked | Redundancy requires one clear expression covering the ground \u2014 three independent reinventions of the same principle with zero cross-linking is the opposite finding, evidence of a missing index rather than existing coverage. A verifier reversing its own prior s"
        },
        {
          "rank": 5,
          "source": "Admin/Trajectories.md",
          "section": "Lessons Learned",
          "text": "----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|------------|---------------------|\n| May 2026 | Audit Review  | Exit conditions written without confidence labels         | Implied false precision \u2014 conditions read as verified targets         | All exit conditions labeled [Placeholder]; verification notes added                                               | Replicated | No   "
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "File State",
          "text": ", genuinely reachable). Copilot's \u00a77.3 citation also corrected \u2014 \"Agent Replacement Information Loss\" is a comparison-table row within \u00a77.3, not a section title in its own right; substance of that cross-check unaffected. Human-directed. \u2014 v0.20 \u2014 CIR-F03: \u03a6(n)'s trigger condition corrected from S(n)=0 to S(n)\u2264\u03b5, a direct follow-on consequence of CIR-F02's Coordinate Floor Constraint that neither the original CIR-F02 review nor its own \"no gate behavior changes\" claim caught. Verified directly ag"
        },
        {
          "rank": 2,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "full",
          "text": "genuinely reachable). Copilot's \u00a77.3 citation also corrected \u2014 \"Agent Replacement Information Loss\" is a comparison-table row within \u00a77.3, not a section title in its own right; substance of that cross-check unaffected. Human-directed. \u2014 v0.20 \u2014 CIR-F03: \u03a6(n)'s trigger condition corrected from S(n)=0 to S(n)\u2264\u03b5, a direct follow-on consequence of CIR-F02's Coordinate Floor Constraint that neither the original CIR-F02 review nor its own \"no gate behavior changes\" claim caught. Verified directly agai"
        },
        {
          "rank": 3,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "full",
          "text": " 2026-07-29, CIR-F03: this condition originally read $S(n)=0$; the \u00a74.2 Coordinate Floor Constraint (CIR-F02) means $S(n)$ can no longer reach exactly 0, so an unmodified $S(n)=0$ check would silently stop firing on every ungrounded physical claim. $\\le \\varepsilon$ rather than $= \\varepsilon$ additionally avoids a brittle exact-float-equality comparison.]*\n\n### 2. The Provenance Ceiling Gate $\\Psi(n)$\n\nThis operator scales the entire maturity space downward based on the origin category of the c"
        },
        {
          "rank": 4,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "full",
          "text": " or is explicitly placeholder in the cited files.**\n\n**Purpose & Scope.** $S(n)$ is the physical-grounding coordinate of a node's evidence vector $\\mathbf{V}(n)$. Per the Coordinate Floor Constraint (\u00a74.2) and the corrected $\\Phi(n)$ definition (CIR-F03):\n\n$$\nS(n) \\in [\\varepsilon, 1], \\qquad\n\\Phi(n) =\n\\begin{cases}\n0 & \\text{if } n \\in V_{\\text{phys}} \\text{ and } S(n) \\le \\varepsilon \\\\\n1 & \\text{otherwise}\n\\end{cases}\n$$\n\nThis schema answers three questions a Phase-2 harness must be able to a"
        },
        {
          "rank": 5,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "File State",
          "text": "-reference resolution) and zero \u03b3/\u03a6(n)/S(n)/CIR-001 references anywhere in the harness or its changelog \u2014 Phase-2 is genuinely unimplemented, not partially started. Schema is explicitly Draft/Not Ratified, does not close CIR-001, does not invent hardware or sensors, and correctly treats `Tests/Support_Raft.md`'s sensor surface as still TBD/Placeholder rather than usable. Checked for interaction with same-day edits to `Routing.md`, `Admin/Repository_Integrity_Protocol.md`, and `Admin/CIR_Gov.md` "
        }
      ]
    },
    {
      "id": 12,
      "class": "Technical reasoning",
      "query": "Why was Architecture/Engineering.md's unknown-history safety factor corrected from 3\u00d7 to 6\u00d7+?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "into architecture specification before `Operations/Leviathan.md` exists\n- Ethical Anchor field absent, altered, or not matching canonical string\n- validated_on_machinery_revision not updated when Forge machinery revision increments"
        },
        {
          "rank": 2,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "his still current\" check, given there's no machinery to revise against? Does Canonical_Terms.md need a new term for this artifact type, distinct from \"Heuristic\"? This is deliberately left open rather than guessed at \u2014 same posture this file already took with GH-011 (canonicalization) before that unknown had enough real usage to design against.\n\n---\n\n### Resolution Log\n\n- 2026-08-11: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates\n  left locked at 1/6. (1) Open Unknowns **13** = "
        },
        {
          "rank": 3,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": ": CSL-A06 added (simulation fidelity assumption was hidden);\n             fabrication failure modes added; NOVEL hard constraint added\n    Class 3: CANDIDATE_NOVEL intermediate status added; S2R delta trigger added\n- New unknowns: GH-007 through GH-011 (surfaced by multi-agent review)\n- Highest-risk finding: CSL-A06 \u2014 entire pipeline safety guarantee rests\n  on Stage 3 fidelity; assumption was implicit in v0.1\n\nDocument: Cognitive_Salvage_Layer.md (Exploration audit, 2026-06-24)\nAuditor: Synthes"
        },
        {
          "rank": 4,
          "source": "Admin/Resolution_Methodology.md",
          "section": "Lessons Learned",
          "text": "building on it can surface a stronger structure than the thing being checked | Analogous | After a second applied case in a different domain (chemistry/safety rather than waste/disposal) |\n| 2026-08-16 | Third applied case (CE-006) | Applied methodology in chemistry/safety domain after two prior cases | Top-of-entry Resolution Path had gone stale relative to its own body; paper surface assessed as exhausted | \u00a73 catches internal staleness as well as external fabrication; \u00a74's \"stop when paper is"
        },
        {
          "rank": 5,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "d, materially different six-item systems\n  sharing the same \"Gate N\" numbering \u2014 an undocumented divergence (GOV-011)\n  that existed in part because Verification_Gates.md was never registered\n  as a vocabulary authority source in this file's Conflict Resolution\n  Doctrine, despite being the file every document's `Spec Gates X/6` field\n  actually references. Fixed: Verification_Gates.md added as fourth\n  authority source (Resolution Rule 3 renumbered accordingly). New Section 4\n  entries: Verific"
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Architecture/Engineering.md",
          "section": "Resolution Log",
          "text": "d\n  `Architecture/Performance_Engineering.md` tagged `(planned)` per Discovery.md's\n  Fallacy 6 (Hallucinated Files) rule \u2014 none exist in Routing.md's canonical\n  registry. (4) \"Safe\" language tightened in \u00a71 (Fail Safe principle now\n  cross-references Safety_Protocols.md and specifies non-energetic/fail-passive\n  states) and \u00a77 (FMEA text no longer uses unbounded \"assumed safe\"). (5) \u00a77\n  gained a low-tech hazard detection sub-clause (witness marks, plumb lines,\n  tap-testing) addressing a gap "
        },
        {
          "rank": 2,
          "source": "Operations/Energy.md",
          "section": "Resolution Log",
          "text": "M-006 carried the assumption but nothing tracked the hardware realization itself; (3) the Safety Advisory's \"treat as structural specification\" phrasing revised to \"candidate architectural model\" \u2014 legitimate semantic-hygiene catch, since \"specification\" is a loaded term adjacent to the File State `Status` enum; (4) the bare \"Engineering.md\" cross-reference corrected to `Architecture/Engineering.md`, matching this repo's first-mention-full-path convention; (5) Voltage Ripple values in the Operat"
        },
        {
          "rank": 3,
          "source": "Operations/Gate_01_Intake.md",
          "section": "Resolution Log",
          "text": "to `Architecture/Facilities.md` FA-001\n  (PC-002). Section 2 operator safety cross-reference\n  updated to match.\n\n---"
        },
        {
          "rank": 4,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "car; the CE-006 canonical example's dates, mechanism, and \"found by chance via manufacturer datasheet\" account confirmed exactly against `Architecture/Chemistry.md`'s own record; the `Admin/Autonomy_Divergence_Protocol.md` \u00a74.2 cross-reference confirmed to exist and be correctly titled; the Resolution_Methodology Pattern 6/8 \"specification closure is not a de-escalation\" citation confirmed accurate and correctly followed (Risk/Priority unchanged, matching the GOV-003/PL-001/WA-002/GR-003 closure"
        },
        {
          "rank": 5,
          "source": "Architecture/Engineering.md",
          "section": "Resolution Log",
          "text": "corrected \u2014 \"doctrine triad\" framing replaced with explicit tier stack. Engineering.md is Tier 5 (Architecture), downstream of Ethical_Constraints.md (Tier 1) and Auditor_Protocols.md (Tier 2). Prior framing implied co-equal tier status with Tier 1 governance files, which is architecturally incorrect and creates a potential exploit path where engineering authority could be cited against a hard ethical floor. No body content changed. Eight findings actioned:\n  (1) Navigation Anchors, Upstream/Dow"
        }
      ]
    },
    {
      "id": 13,
      "class": "Cross-document reasoning",
      "query": "Beyond GMP-011, where else does the same failure pattern appear \u2014 an unratified section cited as though it supports the opposite of what it actually says?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "Lessons Learned",
          "text": "approach from being *treated* as load-bearing before it earned that weight \u2014 silence is not confirmation | Internally Derived | Yes |\n| 2026-07-19 | Governance Review | Resolving GMP-010 for honest error only, without considering deliberate subversion | The initial resolution path (check one primary source) is insufficient against an adversary who can plant or compromise a single source | Source diversity, not just source primacy, is required once an unknown's threat model includes deliberate ba"
        },
        {
          "rank": 2,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "Lessons Learned",
          "text": "the actual gap \u2014 the existing rule was location-based (Tier 1 file vs. not) when the real distinguishing factor was constitutional impact | Generalizing an existing rule along its true axis is usually better than adding a parallel one for the case that doesn't fit \u2014 GMP-005 and GMP-009 were the same underlying gap, not two gaps | Replicated | No |\n| 2026-07-19 | Audit Review | Treating a human-directed approach (CE-006) as sufficiently settled for another file (CLF-004) to build on before indepe"
        },
        {
          "rank": 3,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "ated proposal). Higher-tier provenance may warrant reduced consensus_run_count requirements in GH-002 resolution \u2014 the threshold should be stratified by trust tier, not uniform. Null until provenance trust tier doctrine is formally defined.\n\n`failure_modes_observed` \u2014 array populated from player constraint violations during simulation and from Stage 3 failure outcomes for paths that did not fully pass. Supports negative learning: a path that fails Stage 3 with a specific structural collapse mode"
        },
        {
          "rank": 4,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "-004, GH-012, CSL-A03) gained genuinely\n  complementary elaboration \u2014 a canonicalization envelope constraint\n  for GH-004, a simpler baseline yield ratio alongside GH-012's\n  existing stratified metric, and a concrete \u0394_physical test for\n  CSL-A03's existing expiry trigger \u2014 all explicitly marked Placeholder\n  / Internally Derived, none changing Status or Open Unknowns. Four\n  entries (GH-007, GH-008, GH-009, GH-011) already had more specific,\n  better-grounded resolution paths than the proposal"
        },
        {
          "rank": 5,
          "source": "Tests/Cognitive_Salvage_Layer.md",
          "section": "full",
          "text": "n-to-physical fidelity is low, promoted heuristics may pass Stage 3 while failing in physical execution. This assumption requires empirical validation before any heuristic reaches Operational Spec status.\n\n**CSL-A03 elaboration (Payment via Specification, added 2026-08-03 \u2014 human-directed, corrective merge from a Copilot/Grok exchange, see AP-033):** the expiry trigger above (\"Stage 3 validation pass on first physical anomaly\") elaborated as a concrete test: at the first physical anomaly that ge"
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "one thinks to do\n   it by hand.\n\n*Surfaced during a cross-repo epistemic-logic discussion (human-directed),\ngrounded in the CE-006 case as a real, not hypothetical, instance of the\nfailure mode. Logged rather than left as conversational insight, per human\ngoverning authority's direction that this is worth tracking formally.*\n\n**Closure Event (2026-08-30):**\n- **Unknown:** GMP-010\n- **Proposed status:** Resolved\n- **Payment type:** Specification\n- **Basis:** \u00a7VIII Evidence-Sufficiency Gate (`Admi"
        },
        {
          "rank": 2,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "ed rather than solved speculatively; a future unknown may be opened if the pattern recurs.\n\n**Risk and Priority fields on GMP-010 remain High / Major.** Specification closure is not a de-escalation (Resolution_Methodology Pattern 6 / 8).\n\n### VIII.5 Relationship to Existing Doctrine\n\n- Strengthens, does not replace, the provisional-status discipline already demonstrated in the recoverable CE-006 case.\n- Aligns with the evidence-diversity-over-raw-confidence principle in `Admin/Autonomy_Divergenc"
        },
        {
          "rank": 3,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "Resolution Log",
          "text": "overs uncertainty, not\n  disagreement after classification) and **GMP-012** (no rollback/repeal\n  doctrine for a ratified amendment that later proves harmful).\n  GMP-006/007/008 gained a shared consolidation note pointing at a\n  future amendment state machine \u2014 flagged, not designed, in this pass.\n  GMP-004 gained a cross-reference to existing GPG signing precedent\n  already established via `Admin/Repository_Integrity_Protocol.md`\n  RIP-001, as a lower-friction lead for `Admin/Security_Protocols"
        },
        {
          "rank": 4,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "ter than adding a parallel one for the case that doesn't fit \u2014 GMP-005 and GMP-009 were the same underlying gap, not two gaps | Replicated | No |\n| 2026-07-19 | Audit Review | Treating a human-directed approach (CE-006) as sufficiently settled for another file (CLF-004) to build on before independent verification | The underlying mechanism was wrong; caught by chance two days later via an external model's flag and a manufacturer datasheet, not by any structural check this repository runs on itse"
        },
        {
          "rank": 5,
          "source": "Admin/Governance_Migration_Protocol.md",
          "section": "full",
          "text": "** GMP-006\n- **Proposed status:** Resolved\n- **Payment type:** Specification\n- **Basis:** \u00a7III.A Track B Amendment Lifecycle \u2014 State Machine (`Admin/Governance_Migration_Protocol.md`, integrated 2026-08-31), summarized in the Proposed Resolution above. Two stale cross-references that would have contradicted this closure \u2014 an index line and a Drift Indicator entry, both still describing GMP-006 as pending \u2014 corrected in the same pass.\n- **Proposer:** Grok \u2014 Synthesizer, 2026-08-31. Drafted the or"
        }
      ]
    },
    {
      "id": 14,
      "class": "Cross-document reasoning",
      "query": "How does CIR \u00a74.3's Provenance Ceiling Gate relate to Auditor_Protocols.md's Institutional Provenance Labels, and where was that relationship first made explicit rather than merely implied?",
      "corpus_a": [
        {
          "rank": 1,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": " scope was\nAuditor_Protocols.md specifically, which is now closed.\n\n---\n\n### Resolution Log\n\n- 2026-09-23: **Claim-Type Labels registered (\u00a74).** Nine-label taxonomy\n  (FACT/MEASUREMENT/OBSERVATION/INFERENCE/ASSUMPTION/PROPOSAL/UNKNOWN/\n  DECISION/AUTHORIZATION) distinguishing claim *type* from AP-006's\n  existing confidence/provenance *axes*. Minimal shape only \u2014 definitions\n  plus a two-question usage rule, no retroactive relabeling of existing\n  content and no change to AP-006, EC-001, EC-008"
        },
        {
          "rank": 2,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "he exploration and the minimal definition block, 2026-09-23), Verifier\n(Claude, 2026-09-23 \u2014 Pass; the AP-006 tables, provenance ceiling rule,\nEF-0.3 Epistemic Ledger reference, and Auditor_Protocols Phase 3\ncitation all confirmed exact against source; no correction required).\nIndependence attestation: Grok (Proposer) and Claude (Verifier) are\ndifferent agent instances; Claude had no prior involvement drafting\nthis text. Human Ratification: Human Governing Authority, 2026-09-23.\nHuman-directed.*"
        },
        {
          "rank": 3,
          "source": "Admin/Governance_Charter.md",
          "section": "Lessons Learned",
          "text": "ctrine and enforcement layers must remain distinct                                      | Replicated | Yes                 |\n| 2026-05-23 | Audit Review  | Forge_Audit_Kit.md placed above Auditor_Protocols.md in tier hierarchy | Derived document outranked its source | A derived condensed reference cannot sit constitutionally above its source document. Tier ordering corrected. | Replicated | No |\n| 2026-05-23 | Modeling      | Axiom set mixing Protections and Prohibitions in single list | Structu"
        },
        {
          "rank": 4,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": "n/Verification_Gates.md                                      |\n| Last Audit       | 2026-09-23                                                          |\n| Auditor          | Claude \u2014 Claim-Type Labels registered under \u00a74 (Grok proposer, human-directed), 2026-09-23; prior: Claude \u2014 \"Disambiguation: Uses of 'Gate'\" section added (FL-012, human-directed), 2026-09-14; prior: Claude \u2014 four new terms registered (Active Constitutional Surface, Claimed/Recognized/Ratified Constitutional Lineage) at GOV"
        },
        {
          "rank": 5,
          "source": "Admin/Canonical_Terms.md",
          "section": "full",
          "text": ") \u2014 are used in\nnarrower rollback/recovery contexts and are not renamed or superseded by\nthis entry.*\n\n**Claim-Type Labels**\n\n**Status:** Ratified \u2014 Payment via Specification, 2026-09-23\n**Orthogonal to:** `Admin/Auditor_Protocols.md` \u00a7AP-006's two-axis system\n(Quantitative Confidence Labels + Institutional Provenance Labels).\n\nNine labels distinguishing *what kind of speech act* a statement is from\n*how well-supported* or *how it was derived*. These labels do not\nreplace, weaken, or alter the e"
        }
      ],
      "corpus_b": [
        {
          "rank": 1,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "full",
          "text": "rimentally Verified** | $P_{\\text{ceiling}} \\ge \\theta_p$ | $\\Psi(n) \\ge 1$; eligible for verified classification. |\n| **Operationally Hardened** | $P_{\\text{ceiling}} = 1.0$ | Full weighted potential unlocked. |\n\n**Identity with `Admin/Auditor_Protocols.md`'s Institutional Provenance Labels [Added 2026-08-07, first patch toward Confidence Algebra formalization]:** These four categories are not a CIR-local invention \u2014 they are, name for name, the Institutional Provenance Labels already defined i"
        },
        {
          "rank": 2,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "File State",
          "text": " `Routing.md`, `Admin/Repository_Integrity_Protocol.md`, and `Admin/CIR_Gov.md` (which has its own, separately-tracked $S(n)$/$\\Phi(n)$ symbols under CIR-GOV-002) \u2014 no overlap found; none of those files' edited passages reference this schema or CIR-001. Human-directed.) |\n| Active Trackers | CIR-001, CF-002, CF-004 |\n\n> **Provenance self-reference note:** This document's own Provenance Ceiling Gate (\\u03a8, Section 4.3) classifies its Truth Basis as *Internally Derived*, which bars it from self-"
        },
        {
          "rank": 3,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "full",
          "text": "Routing.md`, `Admin/Repository_Integrity_Protocol.md`, and `Admin/CIR_Gov.md` (which has its own, separately-tracked $S(n)$/$\\Phi(n)$ symbols under CIR-GOV-002) \u2014 no overlap found; none of those files' edited passages reference this schema or CIR-001. Human-directed.) |\n| Active Trackers | CIR-001, CF-002, CF-004 |\n\n> **Provenance self-reference note:** This document's own Provenance Ceiling Gate (\\u03a8, Section 4.3) classifies its Truth Basis as *Internally Derived*, which bars it from self-pr"
        },
        {
          "rank": 4,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "full",
          "text": "-07 \u2014 \u00a74.3's Provenance Ceiling Gate gained an identity note with `Admin/Auditor_Protocols.md`'s Institutional Provenance Labels: the four category names in this section's \u03a8(n) table were already identical to that file's, never previously stated as the same system. First surgical patch toward the \"Confidence Algebra\" formalization an external review (Grok) flagged as an open gap; companion patch in `Architecture/Cognitive_Frameworks.md` \u00a7IX.3 identifies the separate conjunction-operator relation"
        },
        {
          "rank": 5,
          "source": "Admin/Computational_Institutional_Reasoning.md",
          "section": "full",
          "text": "\u2014 they are, name for name, the Institutional Provenance Labels already defined in `Admin/Auditor_Protocols.md` \u00a7Evidence Classification and Institutional Truth Provenance Hierarchy (that section predates this one; AP-006, logged 2026-05-23). $\\Psi(n)$ is the algebraic implementation of that section's provenance ceiling rule (\"No internally-derived claim may be represented as VERIFIED regardless of internal coherence, agent consensus, or elegance\") \u2014 not a parallel or competing system. This was n"
        }
      ]
    }
  ]
}

---

## Addendum: ChatGPT cross-check, verified against source (2026-09-29)

Preserved reference material, not doctrine. Above this line: the unmodified Colab console
output and `candidate3_results.json` from the first Candidate 3 run (2026-09-29,
`LazarusForge-1_17_Alpha_unified.zip`, sha256 `4106f1f7...b28954`). The results were also
shown to ChatGPT for an independent read. ChatGPT was working from the console log alone
(the JSON upload did not go through on that platform), which produced two content-level
errors this addendum documents, per the repository's cross-agent-verification-against-source
discipline (not agent convergence).

**Where ChatGPT's read was wrong, checked against the JSON text directly:**

- **Q1 (GMP-011 / §VII.5):** called `Admin/Ethical_Constraints.md` "a clearly poor top hit"
  on filename alone. The retrieved text is the exact correct answer, verbatim: "Deliberately
  anchored to the Charter's Genesis Phase declaration rather than
  Governance_Migration_Protocol.md §VII.5: that section is part of §VII, headed 'Proposed,
  Not Ratified'..." This is the strongest hit in the run, not a poor one.
- **Q9 (Closed_Loop_Feedstock "Resolved 2026-08-03" claim):** called `Admin/Progress_Log.md`
  "promising" on filename alone. The retrieved text is a different, later, real CLF-010
  ratification, not the rejected 2026-08-03 claim the query asks about. Checked against the
  live repository: the actual passage is at `Challenges/Closed_Loop_Feedstock.md` line ~565,
  inside a section the script does collect. Genuine miss, not a promising hit.
- **Q10 (AP-033 Rule 9):** called the top hit "poor" and stopped there. Rank 3 in the same
  JSON (already collected; no re-run needed) is `Archive/Logs/Auditor_Protocols_Logs.md`,
  containing the literal Rule 9 text. Not a retrieval failure — a ranking one, which is
  exactly the distinction ChatGPT itself proposed checking for, just not applied here.
- **"Capture Top-5 instead of Top-1"** — already true of the run being reviewed. `top_k=5`
  was set from the first execution of the script; the gap was that only the console log
  (top-1 only) had been shared on that platform, not the JSON.

**Where ChatGPT's read held up, checked against the script:**

- **Corpus A membership for Q7/Q13** (its request to verify `Support_Raft.md` and
  `Governance_Migration_Protocol.md` were legitimately in the distilled corpus): confirmed
  against `Candidate3_Transient_Index_Colab.py`. Both carry a `## Lessons Learned` section,
  and Corpus A's collector sweeps every file in the repository for that section beyond its
  three-file fixed list. Working as designed, not an artifact.
- **Retrieval-relevance vs. historical-sufficiency as separate scoring dimensions** — sound,
  and the Q1/Q9 corrections above are a direct demonstration of why the distinction matters:
  a plausible filename is not the same as checked content.
- **Compare against ordinary repository routing/search as a baseline** — not yet done, and
  the one recommendation here that isn't already answered by data already in hand. Logged as
  the next open step.
- **"Candidate 3 as a candidate generator feeding existing routing, not a routing
  replacement"** — reasonable interpretation, consistent with `Architecture/Forge_flow.md`'s
  "Parser observes. It does not decide."

**Net effect on the Run 1 scoring already filed in `Tests/Persistent_Cognition_Candidates.md`
v0.16:** unchanged. That entry was written from direct JSON inspection, which already caught
the Q9 miss and the Q10 rank-3 hit this addendum re-derives; this cross-check corroborates
it rather than revising it. Filed here as a documented instance of the filename-plausibility
failure mode the experiment itself is designed to expose, this time in an auditor's read of
the results rather than in the retrieval system being audited.
