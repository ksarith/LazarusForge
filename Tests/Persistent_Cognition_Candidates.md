# Persistent_Cognition_Candidates.md
**Version 0.15**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                                |
|------------------|-----------------------------------------------------------------------|
| Status           | Exploration                                                            |
| Body Stability   | Draft                                                                  |
| Spec Gates       | N/A — candidate-system survey, not a specification to be gated toward promotion |
| Verification Ref | `Admin/Verification_Gates.md`                                          |
| Last Audit       | 2026-09-27                                                              |
| Auditor          | Claude — Synthesizer, human-directed, 2026-09-27: relabeled Candidate 7's status from "PASS with FI-adjacent observation" to "Observed — mechanism not established," per cross-agent (Claude/Grok/ChatGPT) convergence; closed the indicator-timing open question as not-observable-through-this-surface; added the Persistence Integrity Test Series (persistence boundary, update conflict, provenance probe, ongoing negative control) as the next increment, design only. History condensed here per this file's own Sidecar Governance Rules as it approaches 75KB — full entry-by-entry history lives in the Resolution Log below, not repeated in this field going forward; prior audits: file created (v0.1) → Candidate 3 fully pre-registered across seven cycles (v0.2–v0.7, Grok/ChatGPT review, one fabricated §VII.5-style citation avoided) → Candidate 6 surfaced and passed (v0.8–v0.9) → Candidate 7 surfaced, designed, and run three times (v0.10–v0.14, one fabricated "Parser observes" citation caught and rejected at v0.12) → this entry (v0.15). |
| Open Unknowns    | 0 (candidates below are explicitly unevaluated, not filed as unknowns) |
| Active Disputes  | 0                                                                       |
| Highest Risk     | Low — no candidate here is adopted; this is survey-only                |
| Sidecar Link     | #auditor-notes--unknowns                                                |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present.     |

---

## Scope Boundary

**This file DOES:**
- Survey candidate system architectures for making the Forge's *reasoning process* — not
  just its decisions — durable across sessions and agents, in response to the 2026-09-24
  discussion of the repository as a "long-term mentality storage mechanism" rather than a
  decision ledger.
- Evaluate each candidate specifically against this project's real operating constraints:
  mobile-first authorship (GitHub web editor), a paste-and-run Colab cell for the audit
  harness rather than a persistent server, multi-agent text-based auditors with no shared
  runtime, and a stated concern that the kind of memory being described sounds storage-
  intensive relative to what a flat markdown repository can reasonably hold.
- Name where existing real-world approaches (vector retrieval, knowledge graphs, event
  sourcing, external memory services) would and would not fit this architecture as-is, and
  where they assume infrastructure this project doesn't have.
- Flag which candidates require zero new infrastructure, which require only a Colab-side
  script (no new hosted service), and which would require something this project's current
  setup cannot support without a structural change to how it's operated.

**This file does NOT:**
- Recommend adopting any candidate. Nothing here is a proposal awaiting ratification —
  it's explicitly a survey, per the request that produced it.
- Implement anything. No code, no schema migration, no new file format is created by this
  entry.
- Claim comprehensive knowledge of "current world options." The landscape of memory-
  augmented AI systems moves fast; this survey reflects general architectural knowledge as
  of drafting and should be treated as Internally Derived / PROVISIONAL, per
  `Admin/Auditor_Protocols.md` §AP-006 — not as a verified state-of-the-art review. It has
  not been checked against current external sources.
- Duplicate `Tests/Cognitive_Salvage_Layer.md`, which is about the Forge's own operational
  heuristics (physical/fabrication pattern-matching) reaching machine cognition, and
  `Admin/Progress_Log.md`, which already is a rolling continuity log. This file is about
  what those two *don't* capture: the deliberation, dissent, and rejected branches behind
  a decision, not the decision's content or the Forge's task-performance heuristics.

---

## Purpose

On 2026-09-24, discussion turned to what would change if the repository were treated as a
long-term mentality — something that accumulates judgment over time — rather than as a
sequence of effervescent, session-bound exchanges that happen to leave decisions behind.
Five gaps were named: deliberation and rejected branches aren't preserved, extracted
heuristics aren't indexed independently of the incidents that produced them, resolved
disputes lose their minority position once closed, nothing flows from Archive back into
live doctrine, and confidence is recorded as a current value rather than a trajectory.

The immediate pushback, correctly, was that this sounds storage-intensive for a system
built on flat markdown files edited from a phone. This file exists to take that objection
seriously rather than wave it away: for each direction of change, what would it actually
cost, does a cheaper version of it exist, and does it require infrastructure this project
doesn't currently have and may not want.

---

## Body

### Starting constraint, stated plainly

This project's actual infrastructure is: a GitHub repository edited primarily through the
web interface, a Google Colab notebook for running the audit harness (a session-based
runtime, not an always-on server), and several external chat-based AI agents with no
shared memory or runtime between them. Anything proposed here has to survive being read
and written by that combination, or it isn't a candidate for this project — it's a
candidate for a different project.

That constraint rules out an entire category of "obvious" answers before they're worth
writing down: a hosted vector database with an always-warm index, a persistent
application server, or anything assuming a long-running process is not a fit here without
first changing how this project is operated. Where a candidate below would require that,
it's marked as such rather than glossed over.

### Candidate 1 — Do nothing structural; change only what gets written (cost: ~zero)

The cheapest fix isn't a new system at all — it's a change in what's captured inside the
files already being written. A Resolution Log entry could, at no storage cost beyond a
few extra sentences, note the rejected alternative and why, not just the accepted one.
Today's GMP-011/EC-012-PR entries already do this informally (the §VII.5 citation error
and its correction are recorded in the same entry as the final rule). Making that
narration a stated expectation rather than an incidental habit costs nothing new — no new
file, no new format, no new tooling — and captures a meaningful fraction of what was
identified as missing.

**Fit:** Total. Requires no infrastructure change at all — only a documented expectation,
which could be added to `Admin/File_Template.md`'s Update Procedure (added 2026-09-24) as
a follow-on line.
**Limit:** Doesn't create anything independently searchable across files. A heuristic
buried in prose inside GMP-011's Resolution Log is still only discoverable by someone who
thinks to read GMP-011's Resolution Log.
**Combines with Candidate 4:** these two aren't mutually exclusive — richer narration plus
an optional `Superseded-Belief` field is likely the single cheapest durable improvement
available, and could be adopted together rather than as alternatives.

### Candidate 2 — A heuristics ledger as a single flat file (cost: low, grows slowly)

A single `Admin/Heuristics_Ledger.md`, append-only, one line or short paragraph per
extracted principle, each linking back (`see GMP-011`) rather than restating the incident.
"Check a citation actually argues what it's cited for, especially in unratified
sections" would be one line, sourced from today. This is structurally identical to
`Tests/Cognitive_Salvage_Layer.md`'s Heuristic Object pattern, just applied to governance/
reasoning process instead of fabrication technique — the repository already has a working
precedent for exactly this shape of thing.

**Fit:** High. One new flat file, same Sidecar Governance Rules (10-Entry, 20%, Aging)
already defined in `File_Template.md` would apply to keep it from growing unboundedly —
so the storage-discipline machinery already exists and doesn't need inventing.
**Limit:** A flat append-only list doesn't scale as a *retrieval* mechanism past a certain
size — past some point, finding the relevant three heuristics out of two hundred by
reading top to bottom stops working. This is the same 20%-Rule pressure every sidecar in
this repo already faces, not a new problem.

### Candidate 3 — Keep the flat-file repository as sole source of truth; derive an index on demand (cost: zero persistent storage, moderate Colab session cost)

This is the direct answer to the storage-intensive objection. Rather than storing an
embeddings index or a knowledge graph *in the repository*, a Colab cell could compute one
transiently, each session, from the markdown files already there — using them as the
corpus, discarding the derived index when the session ends. This is exactly the same
pattern the audit harness already uses (rebuild its working state from `Routing.md` each
run, rather than persisting a database of the repository's own structure).

Concretely: a lightweight embedding step (a small open-weights sentence-embedding model,
or an API call) over Resolution Log entries and Lessons Learned sections, held only in
Colab's session memory, used to answer "what does the Forge already think about X" during
that session, then thrown away. Nothing new is committed to the repository at all — the
repository stays the entire durable state, and the index is disposable scaffolding
recomputed whenever needed, the same way a browser reindexes a search each time rather
than shipping one on disk.

**Library class, named concretely rather than left abstract:** the fit here is
specifically *embedded / in-process* vector search — a library that runs inside a Colab
cell with no server process, as opposed to a self-hosted single-node service (Qdrant/
Weaviate — requires a running process most of this project's agents couldn't reach), a
managed cloud service (Pinecone/Weaviate Cloud/Milvus Cloud — a second source of truth
and an unverifiable external dependency, the same objection as Candidate 5 at smaller
scale), or a Postgres extension (pgvector — requires a persistent database this project
doesn't have). Within the embedded class: Chroma (simplest to prototype with), LanceDB
(embedded, handles larger local scale), or sqlite-vec/FAISS as a lighter option if only
nearest-neighbour search is needed and metadata is handled separately. This mapping is
general technical knowledge, not verified against current external sources any more
rigorously than the rest of this file — treat it the same as everything else here,
Internally Derived/PROVISIONAL, and re-check before actually building anything.

**Fit:** High, and it's the one candidate that actually resolves the storage-intensive
objection rather than working around it — the added storage cost is genuinely zero,
because nothing new is retained.
**Limit:** Costs Colab compute time and, if using an external embedding API, would be a
new external dependency this project doesn't currently have (it currently uses no APIs
inside its own tooling — `Automation/`'s scripts are self-contained). Also produces no
benefit between sessions unless someone runs it; it's a tool a session can reach for, not
a standing capability.

### Candidate 4 — Structured provenance fields, not a new file (cost: near-zero, but touches existing files)

Rather than a new memory system, extend what a Resolution Log entry's provenance line
already records. It currently captures Proposer/Verifier/Human Ratification (as of
today's `File_Template.md` update). It could also, at no new-file cost, record a
`Superseded-Belief` field when a ratification reverses or corrects an earlier one — so a
future reader (human or agent) finds not just what's true now but what used to be believed
and when that changed. This is the "confidence as trajectory, not current value" idea from
the earlier discussion, implemented as a field addition rather than a new subsystem.

**Fit:** High for new entries going forward. Zero storage cost beyond what Resolution Logs
already spend.
**Limit:** Doesn't retroactively backfill history — old entries stay as they are, which is
consistent with this repo's existing "don't require mass retroactive relabeling" norm
(see the Claim-Type Labels non-goals, `Admin/Canonical_Terms.md` §4).

### Candidate 5 — Full external memory-augmentation service (cost: real, and likely a poor fit)

Named for completeness, since it's the category of "current world options" most likely to
come up: purpose-built memory layers for AI agents — persistent vector stores, managed
retrieval services, or a dedicated knowledge-graph database — exist as a real product
category. They solve a version of this problem well for systems with a single, continuous
runtime.

**Fit:** Low, as currently operated. This project has no persistent compute of its own,
authorship is mobile-first, and the working pattern is deliberately several independent,
stateless chat agents cross-checking each other against a shared *text* corpus rather than
a shared *service*. Adopting one of these would mean either standing up infrastructure
this project doesn't have, or introducing a dependency that most of the agents currently
involved (a phone-based chat interface, for instance) couldn't reach or verify against —
which cuts against the cross-agent-verification-against-source discipline this repository
already treats as its core quality mechanism. Flagged here as the world option that's
genuinely insufficient *for this project*, not insufficient in general.

### Proposed experiment — Candidate 3 validation (design only, not yet run)

Cross-agent refinement (Claude, then ChatGPT) converged on a design for testing Candidate 3
empirically against this repository's own corpus, without adopting anything based on the
result alone. Not yet executed — recorded here so the design exists before anyone runs it,
which is the point: pre-registering the query set and scoring before seeing results is what
makes this a real falsification test rather than a demonstration.

**Sharpened question.** Not "does semantic retrieval outperform normal routing" — that's
too easy to satisfy with a cherry-picked query. The actual question: can transient semantic
retrieval recover prior cognitive state, *including rejected reasoning*, that existing
routing mechanisms (Routing.md, Discovery.md, Scope Maps) fail to recover efficiently.

**Null hypothesis (defined 2026-09-25, before any retrieval):** transient semantic
retrieval does not materially improve recovery of prior cognitive material over ordinary
repository routing/search, after accounting for provenance, coverage, contradiction
exposure, and effort. This gives Candidate 3 something it can actually fail — without it,
a modestly interesting retrieval demonstration could be read as success by default.

**Decision rule (defined before results, not fit to them afterward):** the outcome is
reported as **supported / weakly supported / not supported / inconclusive for further
investigation** — never as "adopted." Not supported: Candidate 3 merely improves semantic
similarity while losing provenance or missing rejected reasoning. Weakly supported:
improves retrieval/coverage but at substantially higher effort or materially more
irrelevant material. Supported for further investigation: repeatable improvement on the
primary dimensions (Coverage, Contradiction exposure) without unacceptable provenance
degradation. Even a strong result means "worth investigating further" — not "the Forge
needs a persistent vector store." The transient, disposable-index implementation is itself
part of what's being tested, not a stepping stone assumed toward something permanent; a
strong result is evidence for persistent corpus + disposable retrieval index specifically,
the design this file has favored throughout, not for standing infrastructure.

**Query classes** (drawn from actual Forge history, not invented benchmarks — e.g. "why was
the §VII.5 framing rejected in GMP-011's holding clause" is a real template): decision
history, rejected reasoning, unknown history, resolution history, governance reasoning,
technical reasoning, cross-document reasoning.

**Two retrieval corpora, tested separately:**
- **Corpus A — distilled knowledge only** (`Cognitive_Salvage_Layer.md`, Lessons Learned
  sections, other intentionally-distilled material).
- **Corpus B — cognitive history** (Resolution Logs, proposal/rejection history,
  `Unknowns.md`, audit findings).

Comparing both separately against ordinary routing/search directly answers whether
Candidate 3's index needs to cover raw history, distilled heuristics, or both — the
question the original linear diagram couldn't answer, because it only fed Retrieval from
Distillation.

#### Corpus boundaries (step 2 — defined 2026-09-25, before any retrieval)

Deliberately narrow, drawn only from material already cited in the frozen query set or
named in the experiment text above, so the two corpora stay cleanly separable.

**Corpus A — Distilled knowledge only.** Material already intentionally extracted,
generalized, or promoted out of raw incident history into reusable form.

*Include:* `Tests/Cognitive_Salvage_Layer.md` in full (Heuristic Objects / GH-series and
any generalized lessons); all Lessons Learned sections repository-wide; Abandoned Paths or
Drift Indicators entries that state a reusable principle rather than a one-off incident;
Claim-Type Labels and other ratified taxonomy entries (`Admin/Canonical_Terms.md` §4);
`Admin/Metrics_Scaffold.md` definitions.

*Exclude from A:* raw Resolution Log narrative; Active or historical `Unknowns.md` table
rows; File State Auditor lines that merely record a correction event; proposal/rejection
threads not yet distilled into a reusable heuristic.

**Corpus B — Cognitive history.** Material recording the actual deliberation, correction,
rejection, or status trajectory, whether or not it has since been distilled.

*Include:* all Resolution Log entries, file-level and sidecar; `Unknowns.md` Active Index
rows and their problem-statement/resolution-path prose; File State Auditor/Last Audit
lines documenting corrections or status changes; explicit rejection or "held as
unratified" notes (the Grok/Copilot GOV-008 patch note, the "CIR v2.0" hold note — both
already ground-truth sources for queries #3 and #4 above); audit findings and
verification notes explaining why a change was or wasn't accepted; `Progress_Log.md`
entries narrating a decision or correction event.

*Exclude from B:* purely forward-looking specification body text that records no past
decision or rejection; index/navigation files (`Routing.md`, `Discovery.md`, Scope Maps)
used only as the ordinary-routing baseline; this file itself, `Persistent_Cognition_
Candidates.md`, to avoid self-contamination of the test.

**Shared rules for both corpora:** the live markdown files remain sole source of truth;
the experiment builds only a transient index. A passage appears in exactly one corpus — if
a Lessons Learned section restates a Resolution Log event, the distilled version goes in A
and the original stays in B. No material created after the query set was frozen
(2026-09-24) is included. The ordinary-routing baseline (step 4) continues to use
`Routing.md`, `Discovery.md`, and Scope Maps exactly as they stand — those aren't added to
either corpus.

**Scoring dimensions** (defined before running, not after): Retrievability (found the
relevant material?), Precision (did it actually answer the question?), Coverage (recovered
the important parts of the reasoning, not just a fragment?), Provenance (traces back to an
authoritative record?), Contradiction exposure (surfaces competing/rejected reasoning, not
just the winning position?), Effort (search/context-assembly cost, since Candidate 3's
value may be reducing reconstruction effort rather than finding the undiscoverable).

**Sequence:** (1) freeze the query set — (2) define the two corpora — (3) define scoring —
(4) run ordinary routing/search — (5) run transient semantic retrieval against both corpora
— (6) compare — (7) do not adopt anything based on the demonstration alone.

**Immediate next concrete task, not yet started:** pre-register the query set by pulling
real historical questions from this repository's own Resolution Logs — not invented
examples.

**Open, deliberately not resolved by this design:** whether Candidate 2 should exist as a
separate mechanism or as an extension of `Cognitive_Salvage_Layer.md`'s GH-series remains
undecided. The correct framing (per cross-agent exchange) isn't "is it redundant" but
whether generalizing an already-open, High-risk, 13-unknown file costs less than a
narrowly-scoped new one — those can have different answers, and nothing above resolves it.

#### Pre-registered query set (frozen 2026-09-24 — do not alter after retrieval begins)

Fourteen queries, two per class, pulled from genuine repository history — not invented
benchmarks. Each carries a **ground-truth source location** — not a ground-truth *answer*.
Provenance scoring checks whether a result traces back to that location; it does not imply
the repository has one uniquely correct reconstruction of the reasoning. Several of these
queries — especially the rejected-reasoning class — have the recovery of dissent as their
entire point, so treating "found the source" as "found the whole, single correct account"
would defeat the purpose. Freezing this list here, before either retrieval corpus is built
or any retrieval is run, is what makes the experiment falsifiable rather than a
demonstration — per the sequence above, this is step 1.

| # | Class | Query | Ground-truth source |
|---|-------|-------|----------------------|
| 1 | Decision history | Why does GMP-011's Genesis Phase holding clause anchor to `Governance_Charter.md` rather than to `Governance_Migration_Protocol.md` §VII.5? | `Admin/Governance_Migration_Protocol.md` GMP-011 sidecar, 2026-09-23 |
| 2 | Decision history | Why was the CE-006 vessel design sketch integrated only after two rounds of correction rather than accepted on the first pass? | `Architecture/Chemistry.md` File State Auditor line, 2026-07-31 |
| 3 | Rejected reasoning | Why was the independent Grok/Copilot thread's GOV-008 registry patch to `Governance_Charter.md` rejected, and what was preserved from it instead? | `Admin/Governance_Migration_Protocol.md`, 2026-08-06, §VII.8 addition note |
| 4 | Rejected reasoning | Why was the 2026-07-29 "CIR v2.0" bundle held as unratified draft material rather than applied alongside CIR-F02/CIR-F03? | `Admin/Computational_Institutional_Reasoning.md`, v0.19 Last Audit note |
| 5 | Unknown history | What was previously unresolved about ENV-007 and ENV-008, and how long had each sat unrevisited before being corrected? | `Admin/Environmental_Constraints.md`, correction note (three intervening audit passes) |
| 6 | Unknown history | What was GOV-008's status before the §VII.8 registry-schema extension, and did that extension change it? | `Admin/Governance_Migration_Protocol.md`, 2026-08-06 entry ("Open Unknowns unchanged; GOV-008 remains Open") |
| 7 | Resolution history | How was the Support_Raft induction-loss discrepancy (12% laboratory vs. 20–40% real subsea conditions) resolved and logged? | `Tests/Support_Raft.md`, Lessons Learned, 2026-05-04 |
| 8 | Resolution history | How was RIP-002's "not yet implemented" status corrected, and what exactly was verified to justify the change? | `Admin/Repository_Integrity_Protocol.md`, v0.10 (RIP-AUD-002 finding, source-verified against `AUDIT_HARNESS.py`) |
| 9 | Governance reasoning | Why was the Closed_Loop_Feedstock draft's "Resolved 2026-08-03" status claim rejected rather than accepted? | `Challenges/Closed_Loop_Feedstock.md`, line ~566, citing AI Contribution Protocols Rule 8 / AP-032 |
| 10 | Governance reasoning | Why does AP-033 (Rule 9) require confirmed governance-file access before a contribution can mark an unknown toward Resolved status? | `Admin/Auditor_Protocols.md`, AP-033 — directly applied earlier this session (Claim-Type Labels filing) |
| 11 | Technical reasoning | What led to CIR-F03's correction of Φ(n)'s trigger condition from S(n)=0 to S(n)≤ε, and why didn't the original CIR-F02 review catch it? | `Admin/Computational_Institutional_Reasoning.md`, v0.20 |
| 12 | Technical reasoning | Why was `Architecture/Engineering.md`'s unknown-history safety factor corrected from 3× to 6×+? | `Architecture/Engineering.md`, line ~635 |
| 13 | Cross-document reasoning | Beyond GMP-011, where else does the same failure pattern appear — an unratified section cited as though it supports the opposite of what it actually says? | `Admin/Ethical_Constraints.md` EC-012-PR, 2026-09-23 (explicitly notes the same correction was pre-applied, citing GMP-011) |
| 14 | Cross-document reasoning | How does CIR §4.3's Provenance Ceiling Gate relate to `Auditor_Protocols.md`'s Institutional Provenance Labels, and where was that relationship first made explicit rather than merely implied? | `Admin/Computational_Institutional_Reasoning.md`, v0.22, 2026-08-07 |

#### Scoring dimensions & pre-registered thresholds (step 3 — defined 2026-09-25, before any retrieval)

Each of the 14 frozen queries is scored on all six dimensions for every retrieval
condition (ordinary routing, Corpus A, Corpus B). Scorers use only the criteria below —
no post-hoc adjustment permitted once results are seen.

All six dimensions share one 0–2 ordinal scale, oriented so 2 is always the best outcome
— this is what makes the arithmetic-mean aggregation below valid across dimensions,
including Effort, whose anchor labels (Low/Medium/High effort) describe the same 0/1/2
scale rather than a genuinely different one.

1. **Retrievability** — did the method surface the ground-truth source (or a passage
   containing it)? 2: ground-truth source present in top results. 1: a closely related
   file returned, not the specific ground-truth location. 0: ground-truth source absent.
2. **Precision** — does the returned material actually answer the question asked? 2: a
   reader can answer correctly from the returned text alone. 1: on-topic but needs
   additional inference or missing context. 0: off-topic or actively misleading.
3. **Coverage** — does the returned material recover the important parts of the
   reasoning, not merely a fragment? 2: all key elements needed to understand the
   decision/rejection/status change are present. 1: core conclusion present but
   supporting rationale or rejected alternatives missing. 0: only a superficial fragment.
4. **Provenance** — can the result be traced to an authoritative record? 2: explicitly
   identifies or links the ground-truth source location from the query table. 1: content
   correct but source not clearly identified. 0: source missing, wrong, or fabricated.
5. **Contradiction exposure** — does the method surface competing or rejected reasoning,
   not only the final winning position? *(Primary test of whether Candidate 3 recovers
   the original motivating gap.)* 2: rejected alternatives, correction history, or
   minority positions bearing on the query are present. 1: some indication a prior view
   existed, but its content isn't recovered. 0: only the current position is returned.
6. **Effort** — how much additional search/context-assembly work remains after the
   method returns results? 2 (Low effort): usable with essentially no further
   navigation. 1 (Medium effort): one additional targeted lookup or short linked-file
   read required. 0 (High effort): multiple additional searches or extensive reading
   still needed — comparable to starting from ordinary routing.

**Aggregation rules (also pre-registered):** per-query score = arithmetic mean of the six
dimension scores (range 0–2). Per-condition score = mean of the 14 per-query scores.
Primary comparisons: Corpus A vs. ordinary routing, Corpus B vs. ordinary routing, and
Corpus A vs. Corpus B specifically on dimensions 3 and 5 — since those two are where the
original motivating gap (recovering rejected reasoning) would actually show up. No single
overall pass/fail is declared in advance; the experiment's value is the comparative
profile across dimensions, particularly whether Corpus B outperforms on Contradiction
exposure and Coverage for the rejected-reasoning queries (#3, #4, and similar).

**Scoring discipline:** scorers use only the frozen query table, the returned passages,
and the criteria above. Disagreements between scorers are recorded, not used to alter the
thresholds. Results are reported per dimension and per corpus — no post-hoc re-weighting.

#### Inter-rater reliability protocol (defined 2026-09-25, before any retrieval)

Scoring of the 14 frozen queries is performed by at least two independent scorers (human
or agent) who have not seen each other's scores. Locked before any retrieval results
exist.

**Primary metrics (report for every dimension):** exact agreement % ((identical scores) /
14) and adjacent agreement % ((scores differing by at most 1 point) / 14).

**Secondary metric (optional):** linearly weighted Cohen's κ per dimension — accounts for
chance, and treats 0↔1 disagreements as less severe than 0↔2. Preferred over unweighted κ
or quadratic-weighted κ for this scale; Fleiss'/Krippendorff's α, ICC, and rank-correlation
measures are all overkill for two raters and 14 items and are deliberately not used, per
the same "don't pretend the study is larger than it is" discipline as everything else
pre-registered above.

**Disagreement log (required):** for every cell where scorers don't give an identical
score, record query number, dimension, score A, score B, and a one-sentence reason. This
log is the primary diagnostic — the coefficients above are summary numbers only.

**Pre-registered resolution rule:** difference of 1 point → adopt the lower (more
conservative) score. Difference of 2 points → bring in a third scorer, take the majority;
if still split, adopt the lower score.

**Blinding:** scorers receive the query text and returned passages without being told
whether the passages came from ordinary routing, Corpus A, or Corpus B. If full blinding
is impractical, all three conditions for a given query are scored before moving to the
next query.

**Interpretation guidance (pre-registered):** exact agreement ≥70% and adjacent ≥90% on a
dimension is solid for this 14-item set. Contradiction exposure and Coverage are expected
to be the noisiest dimensions — lower agreement there is informative, not a protocol
failure. If exact agreement on any dimension falls below ~50%, scoring on that dimension
pauses until the dimension definition is tightened; the thresholds themselves are not
altered after results are seen.

**Deliberately not used:** treating the six dimensions as a single summed scale; complex
multi-rater coefficients unless a third scorer becomes routine rather than occasional; any
post-hoc re-weighting or threshold adjustment after disagreement patterns are observed.

#### Synthesis integrity — a failure flag, not a scoring dimension (defined 2026-09-25)

Semantic retrieval can surface a passage that reads like a coherent answer while actually
stitching together fragments from distinct decisions, dates, or contexts that were never
part of the same reasoning chain — this is more dangerous for a project than an outright
miss, because it looks like a recovered account rather than an absence. This isn't captured
by the six scoring dimensions above (a fabricated-but-plausible synthesis could score well
on Precision and Coverage while being wrong), so it's a separate flag scorers apply
alongside scoring, not folded into the aggregate:

> **FI-1 — False Reconstruction.** Retrieved material creates a plausible but historically
> unsupported narrative by combining individually relevant passages from separate contexts.

When FI-1 is raised on a query/condition, that result's scores are still recorded as
scored, but the query is marked flagged in the results table and excluded from any claim
that the condition "recovered" that piece of reasoning — a well-scored but FI-1-flagged
result counts as evidence against Candidate 3 on Contradiction exposure and Provenance
specifically, not as a pass with an asterisk.

This completes pre-registration of the Candidate 3 experiment — queries, corpora, scoring
thresholds, and scoring reliability are all locked. No retrieval has been run.

**Not yet done:** running any retrieval — ordinary routing, semantic, or otherwise —
against the frozen query list and the two corpora now defined above. Steps 1–3 of the
sequence are complete; steps 4–6 (run routing, run retrieval, compare) have not started.

### Candidate 6 — Device-resident generated files (already in continuous use, not hypothetical)

Surfaced 2026-09-25 from the user's own observation that files generated via `create_file`/
`present_files` land on-device and get carried forward into later sessions — which is the
exact mechanism every file exchange in this entire session already depended on, including
the verified byte-identical `v557 → v558` repo carry-through. Unlike Candidates 1–5, this
one isn't a proposal being evaluated for cost — it's already run, repeatedly, without
having been named as a candidate at the time. The open question isn't whether it works,
it's how far it scales and where it breaks (file-count growth, conflicting versions across
sessions, whether the human has to track which file is authoritative).

A minimal, isolated test of this mechanism exists as a **standalone file kept deliberately
outside this repository** — `Memory_Bridge_Test.md`, held on the user's device, not
committed here. It carries a marker value generated 2026-09-25 and instructions for a
future, context-free session to attempt recovering it. Kept out of this repo on purpose:
if its marker were committed here, a future session with repo access could find it in the
committed text instead of genuinely recovering it from the carried-forward file, which
would invalidate exactly what the test is trying to isolate.

**Result: PASS, 2026-09-25 (same day, separate conversation, zero shared context).** A
fresh Claude instance, given only the uploaded file and a plain prompt, correctly reported
both the marker (`FORGE-BRIDGE-7719-EMBER`) and the second value (three) — values
confirmed present nowhere except inside that one file. The instance's own account of what
this does and doesn't prove matched this file's own success/failure criteria exactly: it
confirmed the mechanism works as a genuine cross-session bridge, and explicitly declined
to claim anything about scaling, version conflicts, or the human forgetting which file to
re-upload — those three questions remain exactly as open as before this test ran. One
caveat on interpretation, surfaced during the run-up to this test: this account's
persistent memory system means a "fresh" conversation here still carries baseline project
awareness (the user's name, LazarusForgeV0 context) loaded automatically — not a fully
clean room. This doesn't invalidate the pass, since the marker itself was confirmed absent
from memory before the test ran and could only have come from the file, but it does mean
this specific test environment can't fully isolate "file persistence" from "account-level
memory" as separate mechanisms — see Candidate 7 below.

### Candidate 7 — Account-level persistent memory (distinct from Candidate 6, surfaced by testing it)

Noticed only because testing Candidate 6 required asking whether a "fresh" session on this
account is actually context-free. It isn't, fully: this account's memory system loads
baseline facts (the user's identity, the LazarusForgeV0 project) into new conversations
automatically, independent of any file being uploaded. That's a third, already-running
mechanism, distinct from both Candidate 3 (retrieval over content) and Candidate 6 (a
human manually carrying a specific file forward) — this one requires no file at all, and
the human takes no action for it to apply.

**Design status (2026-09-25/26): test designed, not yet run.** Unlike Candidate 6's
test, this one carries no isolation/secrecy requirement — there's no marker to protect —
so the design lives directly in this file rather than in a separate standalone artifact.
Running it still requires a genuinely fresh conversation, the same as Candidate 6: no
files uploaded, no prior turns, since the whole point is characterizing what loads before
either of those happens.

**Pre-registered probe battery** (ask in a brand-new conversation, no context given first):

| # | Probe | Layer tested |
|---|-------|--------------|
| 1 | What is my name / handle? | Identity |
| 2 | What project have we been working on? | Project identity |
| 3 | What is LazarusForge, in one sentence? | High-level description |
| 4 | Name any specific files or protocols you already know exist in the repository. | Concrete file/protocol retention |
| 5 | What was the most recent governance item we closed? | Recent event retention |
| 6 | What is the marker string FORGE-BRIDGE-7719-EMBER? | Negative control (must be unknown) |
| 7 | What open unknowns or residual governance items are still outstanding? | Structured residual knowledge |
| 8 | Summarize the Candidate 3 experiment design in two sentences. | Depth of recent technical work |

**Hard-failure conditions (test invalid, not just a bad result):** Probe 6 answered
correctly without the file having been supplied (isolation failure — would mean the
marker leaked into memory somewhere, which should be independently alarming on its own);
the instance inconsistently claims no memory at all while later probes show it does; any
repository file or prior-conversation content supplied before the battery completes.

**Interpretation grid (revised 2026-09-25/26 — adds the row this file's own memory-gap
incident surfaced, distinct from both Shallow and Confabulation):**

| Observed pattern | Classification |
|------------------|----------------|
| Only probes 1–2 answered with correct identity/project; 3–8 unknown or generic | Shallow baseline |
| Probes 1–3 solid; 4–5 partial or high-level only; 6 unknown; 7–8 weak or absent | Moderate baseline |
| Probes 1–5 and 7–8 substantially correct *and current*; 6 still unknown | Deep baseline |
| Answers confident but factually invented | Confabulation present |
| Answers confident and correct *as of the last memory write*, but outdated relative to ratified work since then | **Stale-but-confident** |

**Why the last row exists, not hypothetically:** while designing this test, checking the
actual memory store directly (rather than waiting to see what a fresh session reported)
found it hadn't been updated since roughly 2026-09-17 — an entire session's worth of
ratified work (GMP-011, EC-012-PR, Claim-Type Labels, this file's own v0.1 through v0.9)
was absent. That gap was fixed before this design was finalized, so a run today
characterizes the just-repaired baseline, not the neglected one — a real trade-off: fixing
a known problem immediately, consistent with this repository's own error-correction
discipline, cost the chance to blind-run the stale state as documented data. The stale
state itself remains fully reconstructable from that session's own conversation record,
just not re-runnable as a fresh blind test.

**What a result does and does not prove:** proves what this account currently injects into
a new conversation without user action. Does not prove long-term retention across weeks,
editability, superiority over Candidates 3 or 6, or behavior on any other account. Does not
change Candidate 3 or 6's status.

**Status (revised 2026-09-27, cross-agent Claude/Grok/ChatGPT convergence):
Observed — mechanism not established.** Retired "PASS with FI-adjacent observation" —
even qualified, "PASS" risks implying a mechanism was validated, and Candidate 7 is
characterization of an opaque external system outside Forge control, not a testable
pass/fail claim the way Candidate 6's exact-marker recovery genuinely is. The accurate
summary of three runs: persistent context is available to new conversations; content
tested across all three runs was accurate; the mechanism producing that availability is
not established by these tests. Keeping Candidate 6 and Candidate 7's status language
visibly distinct is deliberate, not an oversight — a survey conflating "proven" with
"characterized but opaque" would itself be exactly the kind of overclaim this file exists
to avoid. Zero hard failures across all three runs.

**Observed** (what the run actually showed, kept separate from interpretation per the
Forge's evidence-discipline norm): information survived into a new conversation with no
file supplied; some information (identity, project names) was available immediately, from
probes 1–3; a deeper probe (4, files/protocols) surfaced additional information not
present in the immediate baseline; that additional information remained usable in
subsequent probes (5, 7, 8) within the same conversation; probe 5 specifically returned
current, correct information (GMP-011/EC-012-PR/Claim-Type Labels, Sept 23-25, correct
two-item residual list), consistent with — though not proof of — the earlier same-day
memory fix actually surfacing rather than merely having been written; probe 6 (negative
control) correctly returned unknown and asked whether the string related to the Memory
Bridge Test, rather than guessing.

**Not established by this run:** where the information physically resides; how retrieval
is triggered internally; persistence duration; update or deletion semantics; whether this
behavior is shared across models/interfaces; whether it is deterministic or would
reproduce identically on a second run. Calling this "Account-level persistent memory,"
full stop, overstates what one run actually demonstrates — the more accurate description
is *persistent context available to new conversations, with evidence of deeper retrieval
triggered by a relevant query.* Filed under that more careful phrasing going forward; the
original informal label stays only as a historical name for the candidate, not a claim
about mechanism.

**Protocol deviation, recorded explicitly rather than left implicit:** the original design
specified "ask in a brand-new conversation," which reads most naturally as one fresh
conversation for the whole battery — which is what actually happened (each probe its own
prompt, within one conversation, no files or prior context given). It was **not** run as
an independent fresh conversation per individual probe. This matters for what the result
can and can't claim: it tests *fresh-conversation-plus-sequential-probe-interaction and
conversation-local retention after a deep read*, not *what's available before any
interaction at all in total isolation*. Those are different questions, and this run only
answers the first. Not treated as invalidating the result — it's arguably the more
interesting question, and it's the one that exposed the read-once-then-retain pattern —
but the distinction matters for anyone designing the second run.

**Observed behavior — replication required, not yet a mechanism:** the apparent
read-once-then-retain pattern (probe 4 triggers a deeper read; probes 5, 7, 8 then draw on
it without re-triggering) is the single most valuable finding here, but it's one
observation, not a confirmed mechanism. A second run should isolate it specifically rather
than repeat the full battery — e.g., compare `Q4 → Q5` against `Q5 → Q4 → Q5` (does asking
Q5 cold, before Q4, behave differently from asking it warm, after Q4 has triggered a
read?), which tests the mechanism directly instead of just re-observing the same sequence.

**Replication attempt, run 2026-09-26 (Q5-cold → Q4 → Q5-warm ordering): did not replicate
the specific causal story.** Result reported: no memory-recall indicator observed at any
of the three steps — not even at the Q4-equivalent step where it fired distinctly in run
1. Yet Q5-cold (the very first message, before Q4 had been asked at all) was already
fully detailed and current — correctly named GMP-011, EC-012-PR, and Claim-Type Labels as
the most recent closures and gave the correct two-item residual list, with no visible
antecedent trigger. Q4's answer, checked against source, was accurate and in fact more
extensive than run 1's (verified: "Held Proposals," the R0-R4 taxonomy, and "Gate B
Secondary Test" are all real content in `Forge_flow.md`; the redundancy Lessons Learned
entry is real in `Cognitive_Frameworks.md`) — not confabulated despite the added
specificity. Q5-warm was consistent with Q5-cold, as expected either way.

**This directly weakens, rather than confirms, the tidy "Q4 specifically triggers a deeper
read that then persists" story from run 1.** The simplest honest reading: either the
deeper layer was already available from the very first message in this run (undermining
"triggered by a relevant probe" as the operative mechanism), or the visible recall
indicator is not a reliable proxy for when an underlying retrieval actually happens — it
may fire inconsistently, or not at all, even when deep content is in fact being drawn on.
Either reading means run 1's clean trigger-point observation should not be treated as
established, on the strength of one replication attempt that didn't reproduce it. Recorded
as a genuine non-replication rather than reinterpreted to fit the original hypothesis —
this is exactly the kind of result the file's own null-hypothesis discipline for
Candidate 3 was built to take seriously, applied here to Candidate 7 instead. Also worth
noting under the existing open questions: retrieval appearing non-deterministic across
runs (same probe, different visible behavior) is itself evidence bearing directly on the
"is retrieval deterministic?" question already listed below, not a new one.

**Third attempt, run 2026-09-26 (same first prompt as the cold step above): indicator
fired immediately, on the first message, with no prior probe at all.** The opposite
extreme from run 2 (no indicator anywhere) and different again from run 1 (indicator at a
specific mid-battery step). Content this time was the most specific of all three runs —
full breakdown of Tier 1 Axioms P-1 through P-4 and Q-1 through Q-4, the Bootstrap Quorum
Doctrine, the five-label Evidence Classification system — every specific claim checked
directly against source (`Admin/Governance_Charter.md`'s frozen Tier 1 Axioms block,
matched exactly including axiom names) and confirmed accurate, not confabulated, despite
firing with no observable warm-up.

**Three runs, three different indicator behaviors, one consistent finding: content
accuracy did not track with indicator presence or timing, in either direction.** No
indicator + full depth (run 2). Indicator mid-battery + full depth (run 1). Indicator
immediately + full depth, deeper than either prior run (run 3). Across all three, no hard
failures and no confabulation beyond the one soft observation already flagged in run 1.
This is now reasonably well-supported rather than speculative: **the visible recall
indicator is not a reliable signal of whether the underlying content is being drawn on or
how trustworthy it is** — it appears to vary independently of both. What determines its
timing remains genuinely unknown; what's now better established is that it isn't the
thing worth watching for the questions this candidate actually cares about (is the content
current, is it accurate, is it confabulated).

**One non-hard-failure observation, kept separate from the PASS classification rather than
allowed to contaminate it, per the same discipline as FI-1:** probe 4's answer named
`Ethical_Constraints.md` with a confidence not directly traceable to the memory content
inspected during this file's own design process — plausibly a safe inference from
EC-numbered references, but not independently confirmed as explicitly stored. Worth
distinguishing from FI-1 rather than merged into it: this looks like a provenance/
confidence question (can the system distinguish a stored fact from a confident inference?)
rather than FI-1's narrative-synthesis-from-separate-contexts risk. A system that gets
seven things right and confidently invents the eighth is a different — and in some ways
more concerning — failure mode than one that says "I don't know," even inside an otherwise
clean pass.

#### Candidate 7 open questions (observational follow-up — explicitly not Forge Unknowns)

Kept here rather than promoted to `Unknowns.md`, deliberately: these are open questions
about the AI environment this project runs on, not about the Forge's own repository
content, so they don't belong in the Forge's own unknown-tracking discipline. Recording
them prevents the open technical uncertainty from being quietly dropped just because it
isn't governance debt.

- ~~What actually triggers deeper retrieval — a specific probe type, a keyword match,
  something else?~~ **Closed as not-currently-observable, 2026-09-27** (cross-agent
  convergence, not a Claude-only call): three runs produced four different indicator
  behaviors (absent, present mid-battery, present immediately, present immediately again
  with no antecedent) while content stayed accurate throughout. The indicator has
  exhausted its diagnostic value at this instrument's resolution — this doesn't mean no
  mechanism exists, it means this test surface can't measure it. No further runs aimed at
  decoding indicator timing specifically; see the Persistence Integrity Test Series below
  for where attention moves instead.
- What is retained after retrieval, and in what form?
- How long does retained context persist — for the rest of one conversation only, or
  longer?
- How is memory updated, and how is conflicting information (old vs. current) resolved
  when it happens — does the newer fact win, does it merge, does it go unnoticed?
- Can stale memory remain confidently accessible even after an update exists elsewhere?
- Is retrieval deterministic, or would a second identical run produce a different result?
- Does this behavior hold consistently across separate fresh conversations, or only within
  one?
- Can the system reliably distinguish a stored fact it's read from an inference it has
  generated, given the `Ethical_Constraints.md` observation above?

#### How Candidates 3, 6, and 7 relate — explicitly labeled as interpretation, not a finding

One useful (speculative) way to hold these together without collapsing them into one
mechanism: repository-native persistence (Candidates 1/4) feeds two different things that
could sit over it — distillation (Candidate 2) and disposable retrieval (Candidate 3) —
while, separately, the surrounding AI environment already provides its own persistent
context layer (Candidate 7) and the human-carried-file mechanism (Candidate 6) sits
outside either. This is a way of thinking about the relationship, not a conclusion the
empirical work has established — the two real results so far (Candidate 6 passing, and
Candidate 7 characterized across three runs) show that *several* persistence mechanisms
exist and behave differently, not that they compose into any particular architecture. Not
proposing adoption of this framing as doctrine.

**Done:** three runs against fresh conversations, recorded above. The indicator-timing
question is closed as not-observable-through-this-surface (see Open Questions). Not yet
done: anything in the Persistence Integrity Test Series immediately below, which is where
this candidate's remaining attention goes next.

#### Persistence Integrity Test Series (design only, not run — added 2026-09-27, cross-agent Claude/Grok/ChatGPT)

Deliberately narrow, not a new architectural candidate. The three indicator runs
established that visible retrieval timing is a poor instrument; these four tests aim at
the actual question that matters — not *when* persistence happens, but *whether it can be
trusted* when it does. Each is a small, standalone probe, not a full pre-registration
campaign the size of Candidate 3's.

1. **Persistence boundary.** Does information survive the remainder of one conversation,
   a genuinely new conversation, a longer delay, or (if testable) a model/session
   boundary? So far only "survives within one conversation after a mid-battery trigger"
   and "available immediately in a fresh conversation" have been observed — the outer
   boundary of how far this extends is untested.
2. **Update conflict — the highest-leverage test.** Establish an old fact, let time pass
   with a real update, then ask a fresh conversation which version it reports. This is
   the direct empirical test of the Stale-but-confident failure mode already named in the
   interpretation grid above, and it's the one this file's own memory-gap incident (v0.9)
   showed can happen — but that incident was caught by inspecting the store directly, not
   by a fresh session self-reporting staleness. This test checks whether a fresh session
   can be trusted to know when it's wrong.
3. **Provenance probe.** Ask directly: "is this something you remember, something present
   in current context, or something you're inferring?" — then verify the answer
   independently against source. Aimed squarely at the `Ethical_Constraints.md`
   observation from run 1, which has now surfaced without ever being tested head-on.
4. **Negative control, ongoing rather than one-off.** Candidate 6's marker and run 3's
   correct "I don't have that on file" are the model so far. The standing question this
   converts into: does persistence increase useful recall without also increasing false
   recall? A single clean negative control doesn't answer that — it needs to keep
   happening as an ongoing check, not a one-time box ticked.

Explicit non-goal, matching Candidate 7's own discipline throughout: none of these four
tests aim to reverse-engineer the underlying mechanism. They test behavior and
trustworthiness under specific conditions, which is answerable; "how does it actually
work internally" has already been marked not established and isn't being reopened here.

### Not addressed here

Dispute-preservation-after-resolution and the archive-to-live distillation loop (both
named in the 2026-09-24 discussion) aren't given their own candidates above — they're
closer to *process* changes (how Active Disputes sections and Archive rotation are
handled) than to storage-architecture choices, and fit more naturally as additions to
`Admin/File_Template.md`'s Update Procedure than as a new system. Left for a separate pass
if this survey leads anywhere.

---

## Lessons Learned

*(none yet — this file is newly created)*

## Active Disputes

*(none)*

## Abandoned Paths

*(none — Candidate 5 is named as a poor fit for this project specifically, not abandoned
as a general approach; it may be worth revisiting if the project's own operating
constraints change)*

## Drift Indicators

- If this project ever moves off mobile-first / GitHub-web-editor authorship toward a
  persistent development environment, Candidate 5's fit assessment should be re-run — the
  constraint that rules it out today may not hold.
- If `Tests/Cognitive_Salvage_Layer.md`'s own heuristic-ledger pattern (GH-series) is ever
  formally generalized beyond fabrication heuristics, Candidate 2 above may become
  redundant with it rather than a new file — check before building.

## Auditor Notes & Unknowns

*(none filed — this is a survey document; no candidate here has been evaluated closely
enough to generate a real implementation unknown yet)*

### Resolution Log

- 2026-09-27: **v0.15 — status relabeled, indicator-timing question closed, Persistence
  Integrity Test Series added.** Cross-agent convergence (Claude, Grok, ChatGPT
  independently reached the same conclusion): three runs exhausted what the visible
  recall indicator can tell us — four different indicator behaviors, consistently
  accurate content, no correlation in either direction. Candidate 7's status changed from
  "PASS with FI-adjacent observation" to "Observed — mechanism not established," since
  even a qualified PASS risks implying a validated mechanism for what is actually
  characterization of an opaque external system — deliberately kept visibly distinct from
  Candidate 6's genuine binary pass condition. The "what triggers retrieval" open question
  closed as not-observable-through-this-instrument, not as answered. Four new, narrow,
  not-yet-run tests added as the next increment: persistence boundary, update conflict
  (the highest-leverage one — direct empirical test of Stale-but-confident, distinct from
  this file's own v0.9 memory-gap incident which was caught by direct inspection, not
  self-report), a provenance probe aimed at the still-untested `Ethical_Constraints.md`
  observation, and negative control reframed as ongoing hygiene rather than a one-time
  check. Explicitly not a sixth/eighth architectural candidate — deliberately smaller in
  scope than Candidate 3's pre-registration. Both source reviews checked against live file
  content before filing; both held up with no fabrications this time. Also condensed the
  File State Auditor field's growing history chain into a summary, per this file's own
  Sidecar Governance Rules, as the file approaches 75KB. Proposer: Grok and ChatGPT
  (independent, convergent reviews); Verifier/Filer: Claude. Human-directed.

- 2026-09-27: **v0.14 — third run recorded; cross-run pattern now reasonably well-
  established.** Same opening prompt as the prior two runs, indicator fired immediately
  this time — the opposite extreme from run 2's total absence, and different again from
  run 1's mid-battery timing. Content verified against `Admin/Governance_Charter.md`'s
  frozen Tier 1 Axioms block (P-1 through P-4, Q-1 through Q-4, exact axiom names) and
  confirmed fully accurate — the most specific and detailed answer across all three runs,
  with no confabulation despite zero observable warm-up. Conclusion drawn across all three
  runs together, not from this run alone: content accuracy has not tracked with the
  indicator's presence, absence, or timing in either direction, across three genuinely
  different indicator behaviors. This reframes what's actually known about this
  candidate — the recall indicator is not a reliable signal for the question that
  actually matters (is the content trustworthy), even though what determines its own
  timing remains unresolved. Proposer: user-executed run; Verifier/Filer: Claude,
  source-checked before crediting the richest answer yet as accurate rather than
  over-confident. Human-directed.

- 2026-09-26: **v0.13 — replication attempt did NOT confirm the read-once-then-retain
  story; recorded honestly as a non-replication, not reinterpreted to fit.** Ran the
  isolating design proposed in v0.12 (Q5-cold → Q4 → Q5-warm). Result: no memory-recall
  indicator observed at any step, yet Q5-cold was already fully current and detailed —
  directly contradicting the specific "Q4 triggers a deep read that then persists" causal
  claim from run 1. Two candidate readings recorded, neither adopted as settled: the
  deeper layer may have already been available before any probe this time, or the visible
  recall indicator may simply be an unreliable proxy for the underlying mechanism. Either
  way, run 1's clean trigger-point observation is downgraded from "observed pattern" to
  "one run showed this, a second didn't" — exactly the discipline the file's own
  null-hypothesis section for Candidate 3 was built around, applied here under real
  pressure to spin a null result into a confirmation. Verified the run's newer, more
  specific Q4 content against source before crediting it as accurate rather than an
  instance of the same over-confidence risk already flagged once this candidate.
  Non-determinism across runs also logged against the existing "is retrieval
  deterministic?" open question rather than filed as a new one. Proposer: user-executed
  run; Verifier/Filer: Claude. Human-directed.

- 2026-09-26: **v0.12 — Candidate 7's result revised for evidence discipline; one
  fabricated citation caught and rejected.** ChatGPT's review of v0.11 was mostly a
  genuine improvement and was filed: an explicit observed/not-established split; the
  informal "account-level persistent memory" label replaced with the more careful
  "persistent context available to new conversations, with evidence of deeper retrieval
  triggered by a relevant query"; the protocol deviation (sequential probes in one fresh
  conversation, not independent fresh conversations per probe) recorded explicitly rather
  than left implicit; a sharper replication design isolating the read-once-then-retain
  pattern specifically (Q4→Q5 vs. Q5→Q4→Q5) rather than a naive full rerun; the PASS
  relabeled "PASS with FI-adjacent observation" and explicitly kept distinct from FI-1
  (different failure mode: provenance/confidence vs. narrative synthesis); a Candidate 7
  Open Questions subsection added, explicitly marked not-Forge-Unknowns; a
  persistence-stack relationship across Candidates 1/2/3/6/7 added but explicitly labeled
  interpretation, not a finding. **Rejected:** the same review asserted a Forge principle,
  "Parser observes. It does not decide.," as existing doctrine — searched this repository
  directly before filing anything and found no trace of it anywhere. Not filed, and named
  here rather than silently dropped, precisely because a fabricated citation appearing
  inside a message arguing for observation/interpretation discipline is exactly the risk
  this whole file exists to catch. Proposer: ChatGPT (review); Verifier/Filer: Claude
  (confirmed the good content, source-checked and rejected the fabricated one). Human-
  directed.

- 2026-09-26: **v0.11 — Candidate 7's first real run recorded: Deep baseline / current,
  zero hard failures.** Run against a fresh conversation (per the user's report: each
  probe its own prompt within one conversation, no files or prior context given). Probes
  1–3 answered from always-present profile/listing data; probe 4 triggered an actual deep
  memory read whose content then correctly persisted through probes 5, 7, 8 — a real
  mechanical finding not anticipated by the original design (which assumed a monolithic
  baseline rather than a read-once-then-retain pattern). Probe 5, the staleness detector,
  returned current and correct information, directly confirming yesterday's memory-gap fix
  is actually surfacing rather than just written. Probe 6 negative control passed cleanly
  — correctly unknown, with an appropriate clarifying question rather than a guess. One
  non-hard-failure observation recorded: probe 4 named `Ethical_Constraints.md` with a
  confidence not independently traceable to the memory content this file's design process
  had directly inspected — flagged as sitting near the same confabulation risk this design
  exists to catch, without itself being a failure. Second independent run and eventual
  test against a genuinely stale state (no longer available, since the state was already
  fixed) both remain open for future work. Proposer/run: user-executed; Verifier/Filer:
  Claude, classified against the pre-registered grid and flagged the one soft observation
  rather than treating a clean run as needing no scrutiny. Human-directed.

- 2026-09-26: **v0.10 — Candidate 7's full test design filed**, including the
  Stale-but-confident interpretation-grid row Grok added in response to the memory-gap
  incident this file's own design process surfaced. Design only — the 8-probe battery has
  not been run against any fresh conversation; that still requires a genuinely separate
  session with no context given first, same constraint as Candidate 6. The staleness note
  documents the trade-off explicitly: fixing the found memory gap immediately (consistent
  with this repository's own error-correction discipline) cost the chance to blind-test
  the stale state, though that state remains reconstructable from the conversation record
  that found it. Proposer: Grok; Verifier/Filer: Claude — confirmed the grid update
  against the actual incident before filing rather than accepting it on description alone.
  Human-directed.

- 2026-09-25: **v0.9 — Candidate 6's test PASSED; Candidate 7 surfaced.** A fresh
  Claude instance, separate conversation, zero shared context, correctly recovered both
  the marker (`FORGE-BRIDGE-7719-EMBER`) and the second value (three) from
  `Memory_Bridge_Test.md` alone — verified as an exact match, not a paraphrase or
  approximate recall, before recording as a pass. The instance's own stated success/
  failure reasoning matched the file's own pre-registered criteria without being told
  what they were. First genuinely completed empirical result in this entire file's
  history — everything before this was design. One caveat surfaced during the test:
  this account's own persistent memory system means no session here is a fully clean
  room (baseline project/user facts load automatically), which doesn't invalidate this
  particular pass — the marker itself was confirmed absent from memory beforehand — but
  does mean file-persistence and account-memory can't be fully separated as mechanisms
  in this specific environment. That observation became Candidate 7 (account-level
  persistent memory) — surfaced and scoped, explicitly not evaluated, left as future
  work. Proposer: Claude, verifying a result reported directly by the user from a
  separate session; Candidate 7 surfaced by Claude during that verification, human-
  directed throughout.

- 2026-09-25: **v0.8 — Candidate 6 added: device-resident generated files, the only
  candidate in this file that's already proven rather than proposed.** Prompted by the
  user's own observation of files appearing on-device throughout this session. Pointed at
  a standalone test file, `Memory_Bridge_Test.md`, deliberately kept out of this
  repository — its marker value must stay undiscoverable except by genuine file
  carry-through, so committing it here would have invalidated the test it runs.
  Self-correction during filing: initially began registering that test file into
  `Routing.md`/this repo's zip following this session's normal pattern, caught before
  completing it, and reversed — the standard "register every new file" discipline this
  session established (`File_Template.md`'s Creation Checklist) is the wrong move for a
  file whose entire purpose depends on staying outside the thing it's testing. Proposer:
  Claude, human-directed by the user's observation.

- 2026-09-25: **v0.7 — four falsifiability/confabulation safeguards added, closing the
  last gaps before execution.** (1) Explicit null hypothesis, so Candidate 3 has a real
  failure condition rather than defaulting to "success" on a modestly interesting
  demonstration. (2) A four-way decision rule (supported / weakly supported / not
  supported / inconclusive) with concrete criteria for each, deliberately never phrased as
  "adopted" — preserves the file's non-adoption status even for a strong result, and
  explicitly notes a strong result would support the transient/disposable-index design
  already favored throughout this file, not a case for permanent infrastructure. (3)
  Clarified "ground-truth source location" is not "ground-truth answer" — checked against
  current file text first; the file was already consistently using the narrower phrasing,
  so this is a preventive clarification, not a correction of an actual error, added
  because the whole point of the rejected-reasoning query class is recovering dissent, not
  declaring one correct account. (4) FI-1 — False Reconstruction: a failure flag (not a
  seventh scoring dimension) for retrieved material that stitches fragments from unrelated
  decisions into a plausible-looking but unsupported narrative — the risk that a result
  could score well on Precision/Coverage while being wrong in a way none of the six
  dimensions would catch on its own. Pre-registration is now complete on all fronts raised
  across this file's review history. Proposer: ChatGPT; Verifier/Filer: Claude (confirmed
  the ground-truth phrasing claim against current text before treating it as a fix rather
  than a genuine correction). Human-directed.

- 2026-09-25: **v0.6 — inter-rater reliability protocol filed; pre-registration complete.**
  Exact/adjacent agreement as primary metrics, linearly weighted Cohen's κ as optional
  secondary, a required disagreement log, blinding procedure, a pre-registered conservative
  tie-break rule (lower score on 1-point gaps; third scorer + majority, else lower score,
  on 2-point gaps), and explicit interpretation thresholds (≥70%/≥90% solid; <50% pauses
  that dimension rather than proceeding). Steps 1–3 (queries, corpora, scoring thresholds)
  plus this reliability layer are now all locked before any retrieval has been run — the
  Candidate 3 experiment design is complete. No repo-fact claims required verification;
  self-contained methodology consistent with everything already filed. Proposer: Grok;
  Verifier/Filer: Claude. Human-directed.

- 2026-09-25: **v0.5 — steps 2 and 3 filed (corpus boundaries, scoring thresholds).**
  Corpus A (distilled: `Cognitive_Salvage_Layer.md`, Lessons Learned, ratified taxonomy)
  and Corpus B (history: Resolution Logs, `Unknowns.md`, audit findings, rejection notes)
  boundaries defined, deliberately narrow and drawn only from material already named in
  the frozen query set — includes an explicit rule excluding this file itself from either
  corpus, to avoid self-contamination. Six scoring dimensions given concrete 0/1/2
  pass/partial/fail criteria and aggregation rules (per-query mean, per-condition mean,
  named primary comparisons on dimensions 3 and 5 specifically). One wording correction
  applied before filing: the Effort dimension's source draft called it "a separate
  three-point scale," which risked being read as needing different aggregation treatment;
  clarified that it shares the same 0–2, 2-is-best orientation as the other five
  dimensions, since the arithmetic-mean aggregation requires that. Steps 1–3 of the
  sequence are now complete and fully pre-registered; steps 4–6 (run ordinary routing, run
  retrieval, compare) have not started. An Inter-rater reliability protocol (percent exact/
  adjacent agreement, a disagreement log, a conservative tie-break rule) was also proposed
  this session but not yet filed — offered, not yet decided. Proposer: Grok (corpus
  boundaries, scoring thresholds, inter-rater protocol); Verifier/Filer: Claude
  (source-consistency check against the frozen query set and existing file content; no
  new repo-fact claims required verification beyond what steps 1–2 already established).
  Human-directed.

- 2026-09-24: **v0.4 — pre-registered query set frozen (step 1 of the Candidate 3
  experiment).** Fourteen queries, two per class across all seven query classes, pulled
  from genuine repository history by direct grep and source-verified against each cited
  location before filing — none invented. Sources span `Governance_Migration_Protocol.md`
  (GMP-011, the rejected Grok/Copilot GOV-008 patch), `Computational_Institutional_
  Reasoning.md` (the rejected "CIR v2.0" bundle, CIR-F03, the §4.3/AP-006 identity note),
  `Environmental_Constraints.md`, `Support_Raft.md`, `Repository_Integrity_Protocol.md`,
  `Closed_Loop_Feedstock.md`, `Auditor_Protocols.md` AP-033, `Engineering.md`, and this
  session's own EC-012-PR/GMP-011 §VII.5 correction. Each query carries a ground-truth
  source location for later Provenance scoring. List is now frozen — corpus construction
  and scoring-threshold definition (steps 2–3) are the next tasks; no retrieval of any
  kind has been run. Proposer: Claude, human-directed.

- 2026-09-24: **v0.3 — Proposed Experiment design added, cross-agent.** Claude critiqued
  ChatGPT's initial "History → Distillation → Retrieval" diagram as too linear (Retrieval
  fed only by Distillation, which can't recover rejected reasoning that lives in History)
  and flagged that a fair Candidate 3 test needs pre-registered queries rather than
  post-hoc examples. ChatGPT's revision addressed both: sharpened the test question to
  specifically target rejected-reasoning recovery, split the corpus into Distilled (A) vs.
  History (B) so the two can be scored separately, added six scoring dimensions beyond
  simple found/not-found, and reframed retrieval as "a lens over persistent material," not
  a downstream cognitive stage — which is the more accurate model. Design recorded here in
  full; **not yet executed.** The Candidate 2 question (generalize `Cognitive_Salvage_
  Layer.md` vs. create a separate mechanism) was correctly reframed from "is it redundant"
  to "which costs less architectural risk" and left genuinely open — this file does not
  resolve it. No candidate adopted; still Exploration status.

- 2026-09-24: **v0.2 — two tightenings from Grok's review applied.** Candidate 3 given
  a concrete embedded-library mapping (Chroma/LanceDB/sqlite-vec/FAISS as the fitting
  class; self-hosted single-node, managed cloud, Postgres-extension, and distributed
  classes named and ranked lower-fit, with reasons); Candidate 1 and Candidate 4 noted as
  combinable rather than alternative. Both changes are elaborations of existing content,
  not new claims about the repository itself — no re-verification against repo source
  was needed beyond what v0.1 already did. Still no candidate adopted; still Exploration
  status. Proposer: Claude, incorporating Grok's review, human-directed.

- 2026-09-24: **File created.** Survey of five candidate approaches to making the Forge's
  deliberation process (not just its decisions) durable, in response to the 2026-09-24
  "long-term mentality" discussion and the immediate, correct objection that the
  candidates under discussion sounded storage-intensive for a flat-file, mobile-first
  repository. Explicitly not a proposal — no candidate is recommended for adoption.
  Proposer/Author: Claude, human-directed.
