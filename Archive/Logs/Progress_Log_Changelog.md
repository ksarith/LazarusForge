# Progress_Log_Changelog.md — Full History for Admin/Progress_Log.md

Split out 2026-08-09, following the precedent already established by `Unknowns_Changelog.md`, `AUDIT_HARNESS_CHANGELOG.md`, and `Forge_Audit_Kit_Changelog.md`. `Progress_Log.md` keeps the five most recent entries in full; this file holds every entry that's rotated out. No information is removed when an entry rotates — every entry below is preserved verbatim from `Progress_Log.md` at the time it moved.

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
