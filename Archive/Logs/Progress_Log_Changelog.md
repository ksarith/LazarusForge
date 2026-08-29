# Progress_Log_Changelog.md — Full History for Admin/Progress_Log.md

Split out 2026-08-09, following the precedent already established by `Unknowns_Changelog.md`, `AUDIT_HARNESS_CHANGELOG.md`, and `Forge_Audit_Kit_Changelog.md`. `Progress_Log.md` keeps the five most recent entries in full; this file holds every entry that's rotated out. No information is removed when an entry rotates — every entry below is preserved verbatim from `Progress_Log.md` at the time it moved.

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
