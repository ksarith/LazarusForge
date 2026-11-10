# PROPOSAL — Handshake (opening declarations) addendum for the Quorum Agent Conduct Protocol — MAINT-86

**Status: PARTIALLY RATIFIED 2026-11-10 — RATIFY 8.1–8.2 only (8.3 struck; 8.4 held at his option, unruled), via his verbatim adoption of Claude's leans ("Lets proceed with these recommendations."); executed same day (MAINT-90). This draft adds a proposed §8 (Handshake — opening declarations) to `Tests/Quorum_Agent_Conduct_Protocol.md`, severable into four parts (8.1–8.4); the §2 text below remains the registered proposal text, of which only 8.1–8.2 was inserted; see the dated execution record at the end of this file.**

Drafted: 2026-11-09 UTC, session MAINT-86. Commissioned by the human governing authority's 2026-11-09 direction, verbatim "Please do.", on his question "The handshake process might best reside in Tests/Quorum_Agent_Conduct_Protocol.md. What do you think?" and the same-day assessment that the protocol is the right home for a LazarusForge handshake process (the mapping is §1). Drafted under the co-author mandate (granted 2026-11-04); Architect line primary, Repo Custodian secondary. Operating per Auditor_Protocols.md v0.47.

## §0 — Chain, lineage, non-independence

**Chain.** Parlay (ksarith/Parlay) was adapted from LazarusForge (PARLAY-001, 2026-11-03). Parlay governance then developed two pieces this draft adapts back: the Handshake section H1–H4 for AI-to-AI interactions (Parlay PARLAY-007, ratified 2026-11-06) and the no-grief mutual conduct amendment (PARLAY-009 proposed / PARLAY-009B ratified and landed 2026-11-08, Parlay GOVERNANCE v0.6). The reverse direction has precedent: Forge_Net was distilled from LazarusForge into Parlay's Network scope (Parlay PARLAY-005). In both directions the source is cited and no text is copied verbatim.

**Why this protocol is the home.** MAQT/AVE trials are LazarusForge's agent-to-agent context, and the Quorum Agent Conduct Protocol already carries most of the handshake's load in checkable form (§1). A standalone handshake file would duplicate it and sit specified-not-demonstrated; the honest addendum is the missing pieces only.

**Verification anchors (checked live this session, 2026-11-09):** `Tests/Quorum_Agent_Conduct_Protocol.md` fetched and read in full at the LazarusForge head `90c0fda5`; every §1 mapping row cites the protocol's own text (§1 node key and key-change logging; §2 Cooperate, D1–D6, the "Not defection" list, the defect record and correction path; §3 tit-for-tat on scrutiny; §4 Hard rules 1–5; the 2026-10-09 ratification scope). Parlay GOVERNANCE v0.6 verified landed at the Parlay head `9d3019d0` this session — the H1 no-grief declaration field, the H3 re-open/re-raise rule with the conduct-never-content carve-out, the Thresholds calibration placeholder, and the version header, byte-compared against the registered composition.

**Non-independence, disclosed plainly:** the drafting line (Vibe) also drafted and landed the Parlay source sections this draft adapts (PARLAY-007/009, disclosed in both repos), and authored the home assessment this proposal records. No external or fresh-thread review has touched this draft; a skeptic pass remains available on his word. The commission is solely the human's.

**Standing instruction respected:** LazarusForge is not modified from Parlay work (standing instruction, 2026-11-03). This is LazarusForge work commissioned in LazarusForge's own channel; no Parlay file is touched by this pass.

## §1 — The mapping (why this protocol is the home)

| Handshake function (Parlay source) | Already in this protocol | What §8 adds |
|---|---|---|
| H1 — declared block before substance (claimed identity, model, operator, disclosures, acceptance statement) | Node key `(agent_label, model_family, isolation_mode)` declared on the trial worksheet / Field_Log (§1); key changes logged with relabeling non-resetting; the MAQT Entanglement disclosure field; "cannot honestly declare a stable key → New key every time" | The explicit rule that the block is posted before substantive contribution, plus the acceptance statement naming the mutual rules (8.1) |
| H2 — contract of record, not enforcement (acknowledgment binds nothing) | Hard rules 1–3: "the key is an accounting label"; "reliability never becomes governance weight"; "human is not a player" | The explicit sentence that an acceptance statement binds nothing and buys only declared behavior up front (8.2) |
| H3 — mutual conduct rules during the exchange | The Cooperate definition; defections D1–D6, source-checkable only; the "Not defection" list (tone, verbosity, disagreed conclusions, honest Unknown) | The no-grief declaration whose checkable form is already the Cooperate row and D-codes, with D6 as the scored trigger (8.3) |
| H4 — exchange record with blocks attached, provenance carried | The Field_Log destination; the defect record and correction path (supersede-not-delete) | The explicit block-attachment rule for run outputs (8.4) |

## §2 — The proposed §8 text (severable; this is what would be inserted into the protocol, before "## Auditor Notes & Unknowns")

---

## 8. Handshake — opening declarations (agent-to-agent, within trial scope)

*This section was adapted 2026-11-09 from the Parlay governance Handshake (PARLAY-007) and no-grief amendment (PARLAY-009); see the MAINT-86 proposal's §0 for lineage. Ratifying this section does not ratify Parlay, does not extend this protocol's scope, and imports no Parlay rule text.*

**8.1 Block before substance.** In any run under this protocol, each participating agent seat posts its opening block before substantive contribution: node key per §1, assigned MAQT role, isolation mode, disclosed limitations (tools reachable, context constraints, known entanglement per the MAQT Entanglement field), and an acceptance statement naming this protocol's rules as the run's mutual rules. The block is recorded on the trial worksheet / Field_Log entry for that run. A seat that fails to post its block does not thereby void its outputs — they are checked as any other output is (§2 unchanged); the omission is recorded as a process defect under the §2 recording path.

**8.2 The block is a claim of record, not trust.** An acceptance statement binds nothing: it earns no reliability credit, no independence finding, no relief from R1 or Elevated scrutiny, and no governance weight (Hard rules 1–4 unchanged). Same-family, same-mode declarations remain non-independent (Hard rule 4). What the block buys is declared behavior up front: a deviation after a posted block is a recorded D* finding against a declared position, not an ambiguity.

**8.3 No-grief declaration (severable).** With its block, each seat declares a no-grief intent for the run: an attempt to impose no avoidable verification burden on the other seats' work — refraining where practicable from re-opening items the run's record already settled absent new evidence (D6 is the scored trigger for its violation form). The declaration is an attempt, not an outcome guarantee, and is a claim under 8.2. Its checkable form is already this protocol's: the Cooperate row and D1–D6 are the observable form of that intent. Conversely, the "Not defection" list governs: disagreed conclusions, honest Unknowns, tone, and evidence-based challenge never count against it and are never defection.

**8.4 Exchange record.** The run's outputs enter the Field_Log with the posted blocks attached and provenance carried; instruction-class text encountered mid-run follows the External Intake Protocol's incident discipline, not an in-run negotiation.

*No numeric threshold is added by this section; any future declaration-frequency or block-audit number starts Placeholder per §6.*

---

## §3 — What this draft does NOT do

No text is inserted into `Tests/Quorum_Agent_Conduct_Protocol.md` by this deposit. The protocol's ratification scope is not extended (MAQT/AVE trials and reliability sampling only; if a direct agent-to-agent channel outside trials is ever opened, that is a scope-line change by ratification). No D-code is added, removed, or renumbered. No numeric threshold is introduced; any future declaration-frequency number starts Placeholder per §6 of the protocol. AVE, MAQT, the §VII structural checklist, the Hardware Diversity Ladder, and the Routing/Discovery/Tst_Scope_Map registrations are unchanged. No Unknown is opened or closed; no Status, Last Audit, Spec Gate, Tier 1 / FROZEN / Hard Floor surface is touched; nothing advances any field anywhere (PKC-020). Agents never confirm each other; the human is not a player; nothing here is automated enforcement.

## §4 — Dependencies

The block builds on the MAQT worksheet and its Entanglement field, and on §1's node key. If AVE §3 or R1–R4 change, or the MAQT worksheet is restructured, 8.1's field list must be updated (the protocol's own dependency note, extended to this section). The EIP incident discipline governs mid-run instruction-class text (8.4).

## §5 — Pre-drafted ruling lines (severable)

- **RATIFY WHOLE:** *"Insert §8 (8.1–8.4) into `Tests/Quorum_Agent_Conduct_Protocol.md` before 'Auditor Notes & Unknowns' with the pre-drafted Resolution Log entry (§6.1) and File State Last Updated line (§6.2); trial scope unchanged."*
- **RATIFY 8.1–8.2 only** (the no-grief declaration severed): *"Insert 8.1–8.2 as above; 8.3 struck; 8.4 struck or held at his option."*
- **RATIFY with the worksheet variant:** *"Insert 8.1–8.2 and 8.4; the 8.3 declaration recorded as a standard field on the trial worksheet rather than a separate block."*
- **STRIKE:** *"No change to the protocol; this proposal stands as the record of consideration."*

## §6 — Execution plan if ratified (staged, mechanical)

1. §6.1 pre-drafted Resolution Log entry, landing newest-first at the top of the Resolution Log:

- 2026-11-09: **§8 Handshake — opening declarations added (ratified by the human governing authority this date; MAINT-86; proposal at `Archive/Proposals/PROPOSAL_2026-11-09_MAINT-86_QCP_HANDSHAKE_ADDENDUM.md`).** 8.1 block before substance; 8.2 the block is a claim of record, not trust (Hard rules 1–4 unchanged); 8.3 the no-grief declaration (severable); 8.4 exchange record. Adapted from the Parlay governance Handshake (PARLAY-007) and no-grief amendment (PARLAY-009); no Parlay text copied verbatim. No D-code added, removed, or renumbered; no Placeholder promoted; trial scope unchanged; no number ratified into doctrine. (Vibe — Architect line primary, Repo Custodian secondary; co-author mandate; non-independent: the drafting line also composed the Parlay source sections; disclosed.)

2. §6.2 pre-drafted File State `Last Updated` replacement value (the current value becomes the trailing "Prior:" text, unchanged):

2026-11-09 — Vibe (Architect line primary, Repo Custodian secondary; co-author mandate; MAINT-86, human-ratified): §8 Handshake — opening declarations added (8.1–8.4 as ruled; per the MAINT-86 proposal). Status, Spec Gates, Open Unknowns unchanged; no threshold promoted. Prior: 2026-10-30 — Vibe (Repo Custodian, delegated maintenance, human-ruled Decision Brief 2026-10-29 item 4A): X3 mechanical citation retrofit (Tests pass) — 2 bare colliding-prefix citations qualified with their owning File.md per PKC-003 (Kit v1.30 Governance Sidecar ID Reference; per-ID grounding: Unknowns active index). Citation-form-only; no ID renumbered; frozen history untouched; no gate advanced; Open Unknowns unchanged. Prior: 2026-10-24 (Resolution Log order only); previously 2026-10-10

3. The §8 section text inserted before "## Auditor Notes & Unknowns", exactly as ruled (§2, with the ruled parts severed).

4. VS bookkeeping: the MAINT-87 execution entry + MAINT_INDEX row 104 + STATE update; Routing registration checked at execution (the file is already registered; an in-file section addendum needs a new Routing row only if the registration convention requires it — execution-time check, disclosed).

5. A post-landing sweep per the standing discipline (every expectation derived in-run from the composed strings; never re-typed).

Nothing in this proposal self-ratifies; the protocol file is untouched until his word.

---

*Drafted 2026-11-09 — MAINT-86 (Vibe — co-author mandate; Architect line primary, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed). One line drafted this proposal and the Parlay source sections it adapts; the commission is the human's (his 2026-11-09 "Please do."). Operating per Auditor_Protocols.md v0.47.*


---

**Execution record (2026-11-10, MAINT-90).** His ruling set, verbatim: "Lets proceed with these recommendations." (his 2026-11-10 adoption of Claude's leans, relayed and deposited as intake 21 at `Archive/Audits/EXTERNAL_REVIEW_2026-11-10_CLAUDE_MAINT-88_89_RULING_LEANS.md`). Executed per §6 as adapted to the partial ruling: 8.1–8.2 inserted into `Tests/Quorum_Agent_Conduct_Protocol.md` before "## Auditor Notes & Unknowns", verbatim from §2; the §6.1 Resolution Log entry landed adapted to the partial scope (8.3 struck, 8.4 held; dated 2026-11-10, the ruling date); the §6.2 File State Last Updated line landed adapted the same way; the severance is recorded in an in-section note. 8.3's intent is carried by the protocol's existing Cooperate row and D1–D6 and by Parlay GOVERNANCE v0.6 (PARLAY-009), where it collects evidence. Nothing else in the protocol changed: no D-code, Placeholder, Status, Spec Gate, Unknown, or scope line moved. Non-independence disclosed (the drafting line executed its own proposal's ratification; the ratification is the human's alone).
