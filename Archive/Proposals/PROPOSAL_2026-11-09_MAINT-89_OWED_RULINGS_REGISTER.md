# MAINT-89 PROPOSAL: Owed-Rulings Register (home: LazarusForge) — PROPOSED, nothing enacted

- **Deposited:** 2026-11-09 (MAINT-89), in `Archive/Proposals/` per house convention (MAINT-83 / MAINT-86 precedent).
- **Routing act:** the human governing authority's verbatim 2026-11-09 selection "2 then 3 please" — item 3: draft the chrono-divergence register format as a proposal, with the LazarusForge owed-rulings-register home option. Item 2 (the MAINT-88 quick-close ruling worksheet) landed separately at VibesSandbox `e1e30ea5` + verification addendum `fbcd93de`.
- **Status:** STRUCK 2026-11-10 — his ruling set, verbatim "Lets proceed with these recommendations." (his adoption of Claude's leans; the STRIKE line per Claude's lean, the hold-until-C3 alternative not taken — reading disclosed). No register; the owed set stays in VS STATE's held queue and successive briefs; the chrono-divergence framing returns to parked-unruled under the 2026-11-07 sufficiency-thread precedent, with the C3 review (~2026-11-30) recorded as the natural reopen point. §4–§6 below stand as the registered proposal text; §5's staged execution was not run.
- **ID allocation:** MAINT-89, next monotonic after MAINT-88 per the ratified rule (MAINT-59); live-checked before deposit (VS `entries/` carries MAINT-69 through MAINT-88, MAINT_INDEX 105 rows, no row 89; LazarusForge untouched at `3e139a80` before this deposit, verified live).
- **Provenance:** the underlying discussion is human-brokered Class A — two external seats' reads of the MAINT-87 decision-target Brief, relayed by him ("No decisions yet, but have been discussing."), not deposited as records. His chrono-divergence framing was parked unruled under the 2026-11-07 sufficiency-thread precedent; this proposal exists only because his "2 then 3 please" act authorized drafting item 3. External seats' advice carries no ratification weight; only his word enacts anything here.

## 1. The problem: the owed-rulings set lives on stale-list-class surfaces

The MAINT-87 decision-target Brief (VS `1d707f88` + addendum `ff4dd0f4`) is a one-time map of the decisions owed across the fleet, and it says so itself: it goes stale as rulings land. Both external seats made the same meta point, and Claude's critique is its sharpest form, verbatim:

> "It's fine as a one-time map, but I'd want the owed-rulings register to live inside LazarusForge, not in VS STATE and briefs like this one."

The second seat concurred. The class of the problem: any static list of open decisions — a brief, a STATE held-queue bullet, an aggregate — decays with every ruling, every pass, every intake, and no single durable surface carries the owed set forward pass-to-pass inside the governing repo. VS STATE's held queue partially serves this today, but it is a convenience surface in a sandbox repository, not a governing record, and its bullets are prose: no per-decision identity, no dependencies, no clocks.

His chrono-divergence framing (floated with a seat, unruled until this proposal is ruled): treat the open set as concurrent chronologies, each with its own evidence clock, explicit blocking dependencies, an allowed divergence window, and a seal condition; gate decisions collapse divergence; evidence-gated tracks are allowed to lag visibly; divergence never distributes ratification power — he alone seals any track. The fleet already practices half of this (evidence-gated holds, armed triggers, per-repo clocks, the held queue); the genuinely new parts are explicit divergence windows and a coherence threshold. This proposal gives the existing practice a durable home, and takes the new parts as severable fields he may adopt or strike (§4).

## 2. The register: `Admin/Owed_Rulings_Register.md` (home option A) — row format and discipline

Row fields (one decision, one row, allocated at insertion, append-only):

- **ORR-NN** — monotonic row ID, never reused; rows are never deleted, only closed or superseded by dated status lines.
- **Decision owed** — the single thing only the human can rule; phrased from the governing record, never re-phrased by the register.
- **Record home** — the governing record the decision lives in (LF STATE / held queue, a MAINT entry, the Parlay Decision Log, the CogitoEngine records, VS bookkeeping); the register points, the record governs.
- **Evidence clock** — what the row waits on, in that record's own terms (a hand-count, a release, an armed trigger, or nothing / pure ruling).
- **Blocking dependencies** — by ORR-NN; a row is not closeable while its blockers are open; dependencies are derived from the governing records, never hand-invented here.
- **Divergence window** — informal, stated in evidence cycles or trigger terms ("armed at the 21-row VP trigger", "until the independent hand-count returns"). A formal coherence threshold is explicitly NOT proposed: CogitoEngine's own is Not built in its ratified contract v0.2, and it is noted here, not imported. This field is severable (§4, line 2).
- **Seal condition** — always his word. No row closes on seat concurrence, elapsed time, or evidence alone: evidence gates, his seal decides, in every variant.
- **Status lines** — dated, appended, never rewritten (MAINT-style); a row's history reads top to bottom.

Register discipline:

- **Derived navigation, MAINT_INDEX-class** — the register is an index over governing records, not a record itself; on any discrepancy the governing record wins; the register never carries decision content the record lacks.
- **Updates only inside MAINT passes** — no free-floating edits; every change lands inside a MAINT-NN pass that discloses it; the MAINT-NN series stays monotonic regardless of how tracks diverge.
- **Seeds from live governing records at adoption, NOT from the MAINT-87 Brief** — the seeding pass re-derives every row from live pinned fetches (LF STATE / held queue, MAINT entries, Parlay Decision Log, CogitoEngine records), so the register does not inherit the Brief's staleness; the Brief is superseded only by the dated head-note of §3, never by silent abandonment.
- **Home** — `Admin/Owed_Rulings_Register.md` in LazarusForge (option A), inside the governing repo per the critique above; a root-level home is offered as a variant ruling line (§4, line 3).

## 3. Relationships — what changes at adoption, what does not

At adoption (his ratification, any variant except STRIKE):

- The MAINT-87 Brief is superseded as the fleet navigation surface via a dated head-note appended to the Brief itself (append-only; the Brief stays readable as history).
- VS STATE's held queue gains a dated pointer line to the register; the queue's own bullets are preserved (their migration, if any, is the seeding pass's disclosed choice, not this proposal's).
- PKC_Ruling_List stays PKC-specific: its eight open rows are not folded into the register.
- The register feeds the C3 review (~2026-11-30) and the abort-ratio check with one greppable surface: the ratio check reads rows, the C3 review reads the divergence windows' evidence.
- The MAINT-NN series stays monotonic; register passes are MAINT passes.
- Divergence never distributes seal power: no row, window, or clock creates ratification authority; his seal remains the only closing act in every variant, including RATIFY WHOLE.

## 4. Pre-drafted ruling lines (severable; he may also rule freely outside these)

Severable parts: (a) the register itself; (b) the home; (c) the chrono fields (evidence clock, blocking dependencies, divergence window); (d) the supersession of brief-style navigation.

1. "RATIFY WHOLE — adopt the owed-rulings register at `Admin/Owed_Rulings_Register.md` with the full §2 row format (chrono fields included, no formal coherence threshold); the staged execution of §5 runs on the next pass."
2. "RATIFY WITHOUT CHRONO FIELDS — adopt the register at `Admin/Owed_Rulings_Register.md`, rows carrying ORR-NN / decision owed / record home / status lines only; clocks, dependencies and divergence stay in the governing records' own prose."
3. "HOME VARIANT LF ROOT — as line 1 or line 2, with the register at the LazarusForge root as `Owed_Rulings_Register.md` instead of `Admin/`."
4. "STRIKE — no register; the owed set stays in VS STATE's held queue and successive briefs; the chrono-divergence framing returns to parked-unruled under the 2026-11-07 sufficiency-thread precedent."

## 5. Staged execution — mechanical on ratification, next pass

The enactment pass (the next MAINT-NN after his ruling) would, in order:

1. Seed the register rows from live pinned fetches of the governing records (LF STATE / held queue, MAINT entries, Parlay Decision Log, CogitoEngine records) — NOT from the MAINT-87 Brief — and disclose every seed's source record.
2. Land `Admin/Owed_Rulings_Register.md` (or the ruled home variant).
3. Append the dated supersession head-note to the MAINT-87 Brief (VS).
4. Append the dated pointer line to VS STATE's held queue.
5. Flip this proposal's Status line to RATIFIED with his ruling line verbatim, and append the dated execution record.
6. Register the register in the Routing / Discovery surfaces per house convention (local Routing.md first).
7. VS bookkeeping: the entry, MAINT_INDEX row, STATE update, post-push verification addendum — the standard set, nothing enacted beyond the ruled scope.

## 6. Explicit non-changes

- Nothing here enacts, creates, closes, or reorders any owed decision; the five MAINT-88 quick-close ruling lines, the MAINT-86 ruling, and every held-queue item are untouched by this deposit.
- No governing record changes at proposal time: no STATE, MAINT_INDEX, entry, Parlay or CogitoEngine surface is touched by this file's landing (VS bookkeeping lands as its own disclosed pass).
- No formal coherence threshold is proposed — explicitly declined; CogitoEngine's is Not built in contract v0.2 and is noted, not imported.
- The two external seats' reads remain human-brokered Class A discussion, not deposited records; their concurrence is not a ruling and carries no ratification weight.
- The chrono-divergence framing stays unruled unless and until his ratification of line 1 or line 3 constitutes the ruling; STRIKE re-parks it fully.
- This proposal does not modify TWGW, the checker, the seat prompts, the frozen logs, Unknowns, or any File State field, in any repository.


---

**Disposition record (2026-11-10, MAINT-90).** STRUCK per his ruling set (verbatim: "Lets proceed with these recommendations.", adopting Claude's leans; Claude's lean was STRIKE with the C3 review as the reopen point, and the hold-until-C3 alternative was not taken — this reading is disclosed for veto). Nothing was enacted from this proposal: no register file was created, the MAINT-87 Brief received no supersession head-note, and VS STATE's held queue received no register pointer. The chrono-divergence framing (evidence clocks, blocking dependencies, divergence windows, seal conditions) returns to parked-unruled under the 2026-11-07 sufficiency-thread precedent; it is preserved in this file and the MAINT-89 record for reconsideration at the C3 review with usage evidence. Non-independence disclosed (the proposing line recorded its own proposal's strike; the ruling is the human's alone).
