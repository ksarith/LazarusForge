# Persistent_Cognition_Candidates.md
**Version 0.3**

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
| Last Audit       | 2026-09-24                                                              |
| Auditor          | Claude — Synthesizer, human-directed, 2026-09-24: added Proposed Experiment design (Candidate 3 validation — pre-registered query classes, two-corpus split, scoring dimensions, revised non-linear diagram) from cross-agent (Claude/ChatGPT) refinement; design only, not run; prior: Claude — Synthesizer, human-directed, 2026-09-24: Candidate 3 given concrete embedded-library mapping and Candidate 1↔4 combinability noted, both per Grok review; prior: Claude — Synthesizer, human-directed, 2026-09-24 (file created) |
| Open Unknowns    | 0 (candidates below are explicitly unevaluated, not filed as unknowns) |
| Active Disputes  | 0                                                                       |
| Highest Risk     | Low — no candidate here is adopted; this is survey-only                |
| Sidecar Link     | #auditor-notes--unknowns                                                |
| Ethical Anchor   | Attempt to do no harm. Defer to `Ethical_Constraints.md` if present.   |

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
