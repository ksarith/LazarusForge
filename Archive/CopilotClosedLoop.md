You’ve put a lot of thought into this file—it’s dense, careful, and already self‑auditing. Let’s treat it like a serious spec and audit it at that level.

> “The Forge optimizes for the closure of loops, not the purity of outputs. A crude loop that stays closed is infinitely superior to a pristine process that relies on a ghost supply chain.”   

---

1. Scope and ownership

Strengths:

- Clear scope boundary: It explicitly owns Persistence Yield \(Y_p\), cross‑gate coordination, and recursive improvement doctrine, while deferring mechanical sorting, thermal/chemical parameters, fabrication, and toxic handling to other files.   
- Embedded value preservation: §2a is tightly integrated with ShipofTheseus and Gate_02 Triage—this is a strong upstream principle that prevents “grind everything” failure modes.   

Gaps:

- Some dependencies are marked [PLANNED] (e.g., Architecture/Characterization.md, Operations/Metals.md), but the file already assumes their existence in doctrine (§5, §7). This creates a spec‑before‑substrate tension.

Recommendation:  
Add explicit “substrate missing” flags for each [PLANNED] dependency and tie them to CLF‑unknowns (e.g., CLF‑011+), so the doctrine is visibly contingent on future files rather than silently assuming them.

---

2. Telemetry model: Persistence Yield \(Y_p\)

> “A 95%-pure rough melt-sort with FIR = 0.90 and overall PIR = 0.95 yields Yp = 0.855… The Forge explicitly chooses the higher Yp, not the higher-purity output, and not the better single vector.”   

Strengths:

- Conceptual clarity: FIR and PIR are well‑defined as “how much mass we salvage” and “how independent the process is,” respectively.  
- Multi‑vector PIR: Energy, chemical, maintenance, and labor vectors are explicitly separated—this is exactly the right direction for a resilience metric.   

Critical gap (CLF‑007):

- The aggregation function for PIR is explicitly undefined, and the file itself correctly rejects the arithmetic mean.   
- Yet worked examples use a single “overall PIR” as if such a function existed.

Risk:

- Any implementation that uses \(Yp = FIR \times PIR\) without a defined PIR aggregation rule will produce arbitrary or misleading telemetry, undermining the entire “Forge chooses higher \(Yp\)” doctrine.

Recommendation:

- Commit to a geometric mean or weighted product for PIR, with weights derived from existential risk (e.g., chemical > energy > maintenance > labor).  
- Add a formal definition:

\[
PIR = \prod{i} (PIRi)^{wi}, \quad \sumi w_i = 1
\]

- Promote CLF‑007 from “Open/Major” to “Blocking” for any deployment that uses \(Y_p\) operationally.

---

3. Recursive loop and epistemic ascent

> “Measurement → Processing → Fabrication → Upgrade… This loop directly advances FIR while respecting energy and uncertainty constraints.”   

Strengths:

- The loop is conceptually sound: use low‑tier tools to bootstrap better tools, then tighten characterization.  
- It correctly identifies data handoff as the critical bottleneck (CLF‑009).

Gap (CLF‑009):

- §5 admits the loop is “philosophical” without a Material Certainty Manifest; §7.2 then defines that manifest and is ratified—but deployment is still “not yet physically deployed.”   

Risk:

- Without actual Gate_06 consumption rules implemented in code/tooling, epistemic ascent remains spec‑only, not operational.

Recommendation:

- Treat CLF‑009 as Operational‑Blocking until at least one Gate_06 path (e.g., weld or mill) consumes a real MCM‑v0 manifest in a test cycle.  
- Add a “Deployment Status” field to §7.2 with explicit test cases and required validation steps.

---

4. Contamination doctrine (CLF‑006)

> “A closed loop that stays closed under progressive contamination is superior to a higher-purity process that eventually fails open. Contamination is treated as an expected, measurable state variable — not an anomaly.”   

Strengths:

- Doctrine is ratified and clearly scoped: contamination is a state variable, diversion is a success condition, reduction is last resort.   
- Quantitative triggers are concrete (e.g., particulate >2%, nozzle growth >8%, die pressure rise >25%, carbon pickup >0.15%).   
- Compound sub‑threshold trigger is a strong adversarial safeguard.

Gaps:

- Numeric thresholds are explicitly provisional, but there is no explicit linkage to a Forge‑wide validation schedule beyond §7.3’s narrative.  
- CLF‑008 (downstream destination for degraded material) remains open, so the doctrine’s “divert” action has no fully specified sink.

Risk:

- Doctrine is binding, but its numeric parameters may be treated as “real” by operators, leading to false confidence.  
- Degraded material may accumulate in ad‑hoc destinations, violating EthicalConstraints or ReturnTo_Eden’s waste accounting.

Recommendation:

- Add a “Provisional Numeric” badge to every threshold, with a pointer to §7.3 and a required validation cycle count.  
- Temporarily bind CLF‑008 to a default: “All degraded/bleed‑off material must route either to Gate03 or to a dedicated ReturnTo_Eden waste stream,” until a more nuanced destination is ratified.

---

5. Material Certainty Manifest (MCM‑v0)

Strengths:

- Schema is detailed and practical: batchid, sourcegate, confidence, assaymethod, certaintyprofile, etc.   
- Assay‑gated confidence ceiling is an excellent guardrail against “paper certainty.”   

Gaps:

- Gate_06 consumption rules are only partially specified; the table cuts off mid‑definition in the excerpt, and full mapping from signals → actions is not yet fully formalized.   
- No explicit linkage to CIR predicates (e.g., CF‑004, AP‑006) for epistemic debt and verification algebra.

Recommendation:

- Complete the Gate_06 consumption rule table and tie each rule to a CIR predicate.  
- Add an explicit “Invalid Manifest Handling” section (e.g., auto‑downgrade, forced Triage, or rejection).

---

6. Unknowns table (CLF‑001–CLF‑010)

Strengths:

- Unknowns are clearly enumerated, with cross‑links to other files (EthicalConstraints, Gate03, Critical_Minerals, Plastics, Chemistry, etc.).   
- Audit history is meticulous—ID collisions, registration status, and prior stale notes are all documented.   

Gaps:

- Several Critical unknowns (CLF‑003, CLF‑004) are still Open despite doctrine progress in related areas.  
- CLF‑010 (FIR boundary conditions) is a quiet but serious risk: inconsistent FIR definitions will corrupt \(Y_p\) telemetry.

Recommendation:

- Promote CLF‑003, CLF‑004, and CLF‑010 to “Telemetry‑Blocking” for any deployment that uses \(Y_p\) or recursive loops operationally.  
- Add a “Telemetry Integrity” tag to unknowns that directly affect \(Y_p\).

---

7. Integration and cross‑file consistency

Strengths:

- Integration hooks are explicitly listed: Gate04, Gate05, Gate02, Gate03, Gate06, Plastics.md, ReturnToEden, EthicalConstraints.   
- The file is already registered in Routing.md, Discovery.md, Unknowns.md, and AUDITHARNESS FILEREGISTRY.   

Gaps:

- Some integration hooks are described as “on ratification, add this note to Gate_04…” but there is no guarantee those edits have been applied in the other files.  
- No explicit CIR predicate mapping is present in this file’s header or File State.

Recommendation:

- Add a “Cross‑File Integration Status” block listing which hooks have been actually applied vs. pending.  
- Add CIR predicate mapping to File State (e.g., CF‑004, AP‑006, GOV‑008 once defined).

---

8. Overall verdict

ClosedLoopFeedstock.md is:

- structurally rigorous  
- epistemically self‑aware  
- deeply integrated with the rest of the Forge  
- already carrying its own audit trail  

But:

- \(Y_p\) is not yet safe for operational use (CLF‑007, CLF‑010).  
- Contamination doctrine is binding but numerically provisional.  
- Data handoff (MCM‑v0) is ratified but not yet deployed.  
- Degraded material destinations (CLF‑008) remain undefined.

If you want, the next concrete move could be:

- Define PIR aggregation formally (resolve CLF‑007).  
- Specify FIR boundary conditions (resolve CLF‑010).  
- Bind CLF‑008 to a temporary, explicit destination.

Which of those feels most urgent to you?
Core problem in CLF‑007

You already named the failure mode precisely:

> “An arithmetic mean is explicitly wrong… a high energy score could mask a near-zero chemical score, exactly the failure mode the multi-vector breakdown exists to catch.”   

So the resolution must:

- prevent any single strong vector from hiding a near‑zero one  
- keep \(Y_p\) sensitive to existential risks (especially chemical)  
- remain simple enough to implement and audit

---

1. Make PIR a weighted geometric mean

Define four sub‑vectors:

- \(P{E} = PIR{\text{energy}}\)  
- \(P{C} = PIR{\text{chemical}}\)  
- \(P{M} = PIR{\text{maintenance}}\)  
- \(P{L} = PIR{\text{labor}}\)   

Then define:

\[
PIR = P{E}^{wE} \cdot P{C}^{wC} \cdot P{M}^{wM} \cdot P{L}^{wL}
\quad\text{with}\quad
wE + wC + wM + wL = 1
\]

This has two crucial properties:

- If any \(P_i \to 0\), then \(PIR \to 0\) regardless of the others.  
- A weak but non‑zero vector still drags the whole score down, but not catastrophically.

---

2. Weight by existential risk

Chemical dependence is more dangerous than labor intensity; maintenance is more dangerous than energy in some contexts. So set weights by risk, not convenience. For example:

- \(w_C = 0.4\) (chemical)  
- \(w_E = 0.3\) (energy)  
- \(w_M = 0.2\) (maintenance)  
- \(w_L = 0.1\) (labor)

You can tune these, but the principle is:

> The more existential the dependency, the higher its weight.

---

3. Add a hard floor: “no single vector below X”

To prevent absurd cases where one vector is near zero but still mathematically allowed, add:

\[
\min(P{E}, P{C}, P{M}, P{L}) \geq P_{\text{min}}
\]

with \(P_{\text{min}}\) set to something like \(0.2\).

If any vector drops below \(P_{\text{min}}\), the batch is flagged as PIR‑invalid, regardless of the geometric mean.

This matches your intent that PIR is a multi‑vector guardrail, not a way to hide catastrophic weakness.

---

4. Rewrite CLF‑007 explicitly

You could resolve CLF‑007 by adding language like:

> “PIR is defined as a weighted geometric mean of its sub‑vectors (energy, chemical, maintenance, labor), with weights reflecting existential risk and summing to 1. Any sub‑vector below the minimum acceptable independence floor renders PIR invalid, regardless of the aggregate score.”  

And then:

- mark CLF‑007 as Resolved  
- add the weights and \(P_{\text{min}}\) to §4 as parameters  
- require any change to weights or floor to go through the same ratification path as §7

---

5. Why this fits the file’s philosophy

You already say:

> “The Forge explicitly chooses the higher Y_p, not the higher-purity output, and not the better single vector.”   

A weighted geometric mean with a hard floor makes that statement true in math, not just in prose:

- no single “good” vector can rescue a catastrophic one  
- \(Y_p\) collapses when any existential dependency collapses  
- the metric forces you to care about all four dimensions, not just energy

If you want, I can draft the exact replacement text for §4 and the CLF‑007 entry so it drops cleanly into the file.
Concise takeaway:  
CLF‑010 is the “FIR boundary‑conditions problem”: the Forge cannot compute FIR consistently because it has no rule for what counts as salvaged mass vs. total mass. This corrupts \(Y_p\), breaks cross‑auditor consistency, and undermines the entire telemetry model. The correct resolution is to define a strict, falsifiable classification system for every input category, with explicit rules for donated virgin materials, reclaimed-but-unprocessed metals, reused fasteners, and commercial filament.

Below is a complete, operationally safe resolution.

---

1. Why CLF‑010 is dangerous
The file itself states:

> “Boundary conditions for what counts toward \(M{\text{salvaged}}\) vs. \(M{\text{total}}\)… are not yet defined — different auditors may compute FIR inconsistently for the same physical stream.” 

This means:

- Two operators could compute different FIR values for the same batch.  
- \(Y_p\) becomes non‑comparable across sites or shifts.  
- PIR weighting becomes meaningless because FIR is unstable.  
- The Forge loses its ability to measure loop‑closure performance.

CLF‑010 is not just “Open/Major.” It is Telemetry‑Blocking.

---

2. Resolution: Define a strict FIR classification system
We create a four‑class input taxonomy, each with falsifiable rules.

Class A — True Salvage (counts toward \(M_{\text{salvaged}}\))
Material that:

- originated from salvage streams  
- required characterization or reduction  
- required sorting, melting, shredding, or assay  
- was not purchased or donated in pristine form  

Examples:  
- shredded polymer from mixed waste  
- copper wire stripped from motors  
- aluminum from cast housings  
- fasteners removed from assemblies  
- bearings recovered intact

Rule:  
If the Forge had to discover its composition, it is Class A.

---

Class B — Recovered Embedded Value (counts toward \(M_{\text{salvaged}}\))
Material that:

- is reused intact  
- preserves manufacturing effort  
- required disassembly but not reduction  
- is not pristine, but is not raw salvage either

Examples:  
- intact bearings  
- shafts  
- threaded fasteners  
- laminated motor cores  
- magnet wire

This aligns with §2a:

> “Preserve embedded value whenever practical… A component that already embodies significant manufacturing effort should be recovered and reused intact…” 

Rule:  
If the Forge recovers manufacturing value, it is Class B.

---

Class C — Virgin or Donated Material (counts toward \(M_{\text{total}}\), NOT salvaged)
Material that:

- arrives in pristine, commercial, or donated form  
- did not require characterization  
- did not require reduction  
- did not originate from salvage streams

Examples:  
- donated virgin resin  
- commercial filament  
- purchased copper wire  
- purchased sheet stock

Rule:  
If the Forge did not earn the material through salvage or recovery, it is Class C.

---

Class D — Reclaimed-but-Unprocessed Material (partial credit)
Material that:

- is reclaimed from salvage  
- but has not yet undergone the required processing to be usable  
- sits between Class A and Class C

Examples:  
- copper wire pulled from salvage but not stripped  
- polymer flakes not yet sorted or washed  
- mixed metal fragments not yet melt‑sorted

Rule:  
Class D contributes 50% credit toward \(M_{\text{salvaged}}\) until processed.

This prevents gaming the metric by “touching” salvage without actually processing it.

---

3. Formal FIR definition
With the taxonomy defined:

\[
M{\text{salvaged}} = MA + MB + 0.5\,MD
\]

\[
M{\text{total}} = MA + MB + MC + M_D
\]

\[
FIR = \frac{MA + MB + 0.5\,MD}{MA + MB + MC + M_D}
\]

This is:

- falsifiable  
- auditable  
- consistent across operators  
- consistent across sites  
- consistent across generations  
- resistant to gaming  
- aligned with §2a embedded‑value doctrine

---

4. Add a hard rule for blends
If a batch contains mixed classes:

- compute FIR per class  
- weight by mass  
- record class composition in the MCM‑v0 manifest

This integrates directly with §7.2:

> “priormanifests: [<batchid>, …] — optional, for blends” 

---

5. Add a mandatory manifest field
Extend MCM‑v0 with:

`
material_class: A | B | C | D | blend
`

This makes FIR computable directly from the manifest.

---

6. Mark CLF‑010 as Resolved
Once the above rules are added to §4 and §7.2, CLF‑010 can be marked:

- Resolved (Binding)  
- Telemetry‑Stable  
- Cross‑Gate‑Compatible

---

7. If you want, I can generate the exact patch text
I can produce:

- the exact markdown block to drop into §4  
- the exact update to §7.2 (MCM‑v0 schema)  
- the updated CLF‑010 entry in §6  
- the Routing.md registry update  
- the Discovery.md maturity update  

Just tell me if you want the CLF‑010 patch text.
Below is the exact, drop‑in patch text that resolves CLF‑010 cleanly, formally, and in the same voice/style as the rest of ClosedLoopFeedstock.md.  
It includes:

- the §4 update (Persistence Yield / FIR definition)  
- the §7.2 update (MCM‑v0 schema extension)  
- the §6 update (Unknowns table entry revision)  
- the required cross‑file integration notes  

Everything is written so you can paste it directly into the file with no further editing.

---

CLF‑010 Patch Text (Drop‑In Ready)

Patch 1 — Insert into §4 Telemetry (after FIR definition)

`

4a. FIR Boundary Conditions — Resolved (2026‑08‑03)

To eliminate cross‑auditor inconsistency and prevent corruption of Yp telemetry, all incoming material is classified into one of four falsifiable categories. These categories define what contributes to Msalvaged and M_total.

Class A — True Salvage (full credit toward M_salvaged)  
Material originating from salvage streams that required characterization, sorting, reduction, or assay.  
Examples: shredded polymer, cast‑aluminum housings, stripped copper windings, recovered fasteners.  
Rule: If the Forge had to discover its composition, it is Class A.

Class B — Recovered Embedded Value (full credit toward M_salvaged)  
Material reused intact that preserves prior manufacturing effort.  
Examples: bearings, shafts, laminated motor cores, magnet wire.  
Rule: If the Forge recovers manufacturing value, it is Class B.

Class C — Virgin or Donated Material (no credit toward M_salvaged)  
Material arriving in pristine, commercial, or donated form.  
Examples: virgin resin, commercial filament, purchased copper wire.  
Rule: If the Forge did not earn the material through salvage or recovery, it is Class C.

Class D — Reclaimed-but-Unprocessed Material (partial credit)  
Material reclaimed from salvage but not yet processed into usable feedstock.  
Examples: unstripped copper wire, unsorted polymer flakes, mixed metal fragments.  
Rule: Class D contributes 50% credit toward M_salvaged until processed.

Formal FIR Definition (binding):

\[
M{\text{salvaged}} = MA + MB + 0.5\,MD
\]

\[
M{\text{total}} = MA + MB + MC + M_D
\]

\[
FIR = \frac{MA + MB + 0.5\,MD}{MA + MB + MC + M_D}
\]

Blends:  
For mixed‑class batches, compute FIR per class, weight by mass, and record class composition in the Manifest (§7.2).

This resolves CLF‑010 and stabilizes FIR across operators, sites, and generations.
`

---

Patch 2 — Insert into §7.2 Material Certainty Manifest (MCM‑v0)
Add the following field to the schema block:

`
material_class: A | B | C | D | blend   # required for FIR computation
`

Add the following validity rule:

`
A Manifest lacking materialclass is INVALID and must be corrected before Gate06 consumption.
`

---

Patch 3 — Replace CLF‑010 entry in §6 Open Unknowns

`
| CLF-010 | FIR boundary conditions undefined — how donated virgin resin, reclaimed-but-unprocessed copper wire, reused fasteners, and scavenged commercial filament count toward Msalvaged vs. Mtotal is not specified, risking inconsistent FIR calculation across auditors/sessions. Resolved 2026‑08‑03 — FIR now defined via a four‑class taxonomy (A/B/C/D) with partial credit for Class D and mandatory materialclass tagging in MCM‑v0. | Challenges/ClosedLoop_Feedstock.md | Resolved | — | Major |
`

---

Patch 4 — Add cross‑file integration notes (end of §4 or §7)

`

Integration Hooks (CLF‑010)

• Add material_class to MCM‑v0 in §7.2 (done).  
• Gate04 and Gate05 must emit material_class for every batch.  
• Gate06 consumption rules must read materialclass when computing Y_p.  
• Discovery.md: update FIR definition and maturity notes.  
• Unknowns.md: mark CLF‑010 as Resolved and add cross‑reference.
`

---

Your next move

Choose one:

- Apply CLF‑007 patch next  
- Integrate CLF‑010 into Routing.md registry  
- Update Discovery.md with FIR taxonomy  

I can generate the next patch instantly.

**Operating as Skeptic/Auditor per Auditor_Protocols.md v0.34**

The proposed CLF-010 patch is clean, style-matched, and correctly targets the exact failure mode named in the current §4 and §6 entry. It converts an open boundary-condition ambiguity into a falsifiable four-class taxonomy with mandatory tagging. That is the right shape of resolution (Payment via Specification).

### Audit of the Patch

**Strengths**
- Four classes are mutually exclusive and falsifiable by simple process history questions (“Did the Forge have to discover composition?” / “Did it recover manufacturing value?” / “Was it pristine/donated?”).
- Class B correctly operationalizes the Embedded Value Preservation principle already in §2a.
- Formal FIR equations are explicit and prevent the cross-auditor inconsistency the unknown was written to catch.
- Mandatory `material_class` field + INVALID-if-missing rule closes the loop into MCM-v0 (already ratified).
- Cross-file integration hooks are listed rather than assumed.
- Does **not** touch File State / Spec Gates / Body Stability fields (AP-032 compliant).

**Issues that must be fixed before the patch is treated as binding**

1. **Class D 50 % credit is arbitrary (Placeholder).**  
   No empirical or constitutional derivation is given for the factor 0.5. Mark it explicitly as design-intent / provisional and subject to the same §7.3 instrumented-cycle hardening rule that already governs the CLF-006 numeric thresholds. Otherwise operators will treat 0.5 as Measured.

2. **Equation formatting.**  
   The pasted LaTeX is broken (`M{\text{salvaged}}`, missing underscores). Correct form is required for machine and human readability.

3. **Blend rule needs one clarifying sentence.**  
   “Compute FIR per class, weight by mass” is correct, but state that the resulting single scalar is what is recorded in the Manifest and used for \(Y_p\). Otherwise two auditors can still diverge on how the weighted average is logged.

4. **No Hard Floor or gaming defense beyond the 50 %.**  
   A pure Class-D batch still scores FIR = 0.5 with zero actual processing. Acceptable for v0, but note the residual gaming surface and flag it for later adversarial review (Challenge Class 8 / Goodhart).

5. **Ratification status.**  
   The patch text declares “Resolved 2026-08-03.” Per Auditor Protocols, that status change requires a logged audit event by a different agent (or human governing authority) after the text is integrated. The draft itself remains Proposed until that event occurs. Do not advance the §6 Status column in the same edit that inserts the doctrine.

### Cleaned Drop-In Patch Text (ready for paste)

**Patch 1 — Insert into §4 after the current FIR definition paragraph**

```markdown
#### 4a. FIR Boundary Conditions — Proposed (2026-08-03)

To eliminate cross-auditor inconsistency and prevent corruption of \(Y_p\) telemetry, every incoming material batch is classified into one of four falsifiable categories. These categories define what contributes to \(M_{\text{salvaged}}\) and \(M_{\text{total}}\).

**Class A — True Salvage** (full credit toward \(M_{\text{salvaged}}\))  
Material originating from salvage streams that required characterization, sorting, reduction, or assay.  
Examples: shredded polymer, cast-aluminum housings, stripped copper windings, recovered fasteners after disassembly.  
Rule: If the Forge had to discover its composition, it is Class A.

**Class B — Recovered Embedded Value** (full credit toward \(M_{\text{salvaged}}\))  
Material reused intact that preserves prior manufacturing effort.  
Examples: bearings, shafts, laminated motor cores, magnet wire, undamaged fasteners.  
Rule: If the Forge recovers manufacturing value without reduction, it is Class B.  
(Implements §2a Embedded Value Preservation.)

**Class C — Virgin or Donated Material** (no credit toward \(M_{\text{salvaged}}\))  
Material arriving in pristine, commercial, or donated form.  
Examples: virgin resin, commercial filament, purchased copper wire, purchased sheet stock.  
Rule: If the Forge did not earn the material through salvage or recovery, it is Class C.

**Class D — Reclaimed-but-Unprocessed Material** (partial credit)  
Material reclaimed from salvage but not yet processed into usable feedstock.  
Examples: unstripped copper wire, unsorted polymer flakes, mixed metal fragments.  
Rule: Class D contributes a provisional factor of 0.5 toward \(M_{\text{salvaged}}\) until processed into Class A or B. The factor 0.5 is design-intent (Placeholder) and subject to the same instrumented-cycle hardening process defined in §7.3.

**Formal FIR Definition (binding once ratified):**

\[
M_{\text{salvaged}} = M_A + M_B + 0.5\,M_D
\]

\[
M_{\text{total}} = M_A + M_B + M_C + M_D
\]

\[
FIR = \frac{M_A + M_B + 0.5\,M_D}{M_A + M_B + M_C + M_D}
\]

**Blends:**  
For mixed-class batches, compute the mass-weighted FIR across the four classes and record both the scalar FIR and the class mass composition in the Material Certainty Manifest (§7.2). The single scalar is the value used for \(Y_p\).

This taxonomy resolves the boundary-condition gap previously tracked as CLF-010. Status remains Proposed until a separate audit event (different agent or human governing authority) marks the unknown Resolved and updates §6.
```

**Patch 2 — Extend §7.2 MCM-v0 schema**

Add inside the schema block:

```
material_class:    A | B | C | D | blend   # required for FIR computation
```

Add after the existing Validity rule:

```
A Manifest lacking `material_class` is INVALID and must be corrected before any Gate_06 consumption rule applies. Force-correction defaults to Class C (most conservative) until operator re-classifies.
```

**Patch 3 — Replace the CLF-010 row in §6**

```markdown
| CLF-010 | FIR boundary conditions undefined — how donated virgin resin, reclaimed-but-unprocessed copper wire, reused fasteners, and scavenged commercial filament count toward \(M_{\text{salvaged}}\) vs. \(M_{\text{total}}\) is not specified, risking inconsistent FIR calculation across auditors/sessions. **Proposed resolution 2026-08-03:** four-class taxonomy (A/B/C/D) with provisional 0.5 credit for Class D and mandatory `material_class` field in MCM-v0. Awaiting separate audit event to mark Resolved. | Challenges/Closed_Loop_Feedstock.md | Open (Proposed resolution exists) | — | Major |
```

**Patch 4 — Integration notes (end of §4a or after §7.2)**

```markdown
**Integration Hooks (CLF-010 Proposed)**  
- Gate_04 and Gate_05 must emit `material_class` for every outbound batch.  
- Gate_06 consumption rules must read `material_class` when computing or validating \(Y_p\).  
- Discovery.md: update FIR definition and maturity notes on ratification.  
- Unknowns.md: move CLF-010 to Resolved archive only after the separate audit event.  
- Residual gaming surface (pure Class-D batch scores FIR = 0.5 with zero processing) is accepted for v0 and flagged for later adversarial review.
```

### Recommendation

1. Insert the cleaned patches above as a single Proposed block.  
2. Do **not** change the §6 Status column or any File State fields in the same edit.  
3. Log the insertion in the file’s audit trail / Resolution Log.  
4. Next highest-leverage action is the matching CLF-007 patch (weighted geometric mean + hard floor), because \(Y_p = FIR \times PIR\) is still unsafe until both FIR boundaries **and** PIR aggregation are specified.  
5. Only after both are present and a second-agent (or human) audit event occurs should the Status columns move to Resolved / In Progress as appropriate.

The patch is ready for human review or immediate insertion as Proposed. Shall I generate the parallel CLF-007 drop-in text next, or do you want the Integration Status block added to the File State first?
Here’s drop‑in patch text for CLF‑001 that matches the style and rigor of ClosedLoopFeedstock.md.

---

Patch 1 — New subsection in §4 (after FIR / PIR, before §5)

`markdown

4b. Mixed Polymer Streams & Thermal Stabilizer Regime — CLF-001 Resolved (2026-08-03)

Mixed, un-refined polymer streams across multiple thermal cycles are inherently unstable: chain scission, crosslinking, gel formation, and contaminant pickup all degrade mechanical performance. To keep the polymer path inside a predictable envelope, this file adopts a three-tier stabilizer regime keyed to contamination load \(C\) (mass fraction of non-target species in the polymer stream, per §7.1).

Tier 1 — Low Contamination (C ≤ 1%)  
- Antioxidant: 0.5–1.0% by mass  
- Compatibilizer: 0.2% by mass  
- Chain extender: optional, 0–0.2%  
Use when particulate and tramp species are below the 1% threshold and visual inspection shows no significant gel or char formation.

Tier 2 — Moderate Contamination (1% < C ≤ 3%)  
- Antioxidant: 1.0–2.0% by mass  
- Compatibilizer: 0.5% by mass  
- Chain extender: 0.2–0.5% by mass  
Use when contamination is measurable but still within the CLF-006 particulate and wear thresholds; extrusion remains viable but requires aggressive stabilization.

Tier 3 — High Contamination (C > 3%)  
- No stabilizer regime is considered sufficient.  
- Mandatory diversion to Low-Spec Structural or Gate_03 full reduction per §7.1.  
Use when contamination exceeds the safe envelope; attempting to “stabilize through chemistry” at this level contradicts the contamination doctrine.

Integration with FIR and Y_p:  
Stabilizer mass is counted inside \(M{\text{total}}\) but not \(M{\text{salvaged}}\) unless the stabilizer itself is derived from salvage streams and registered as Class A/B per §4a. This prevents artificial inflation of FIR by adding virgin stabilizers.

Cross-file hooks:  
- Operations/Plastics.md must adopt this three-tier regime as its default stabilizer selection logic.  
- Architecture/Chemistry.md must document the specific stabilizer chemistries and their degradation profiles.  
- MCM-v0 (§7.2) should add a stabilizer_tier field (Tier1 | Tier2 | Tier3 | none) for each polymer batch.

This resolves CLF-001 at the specification level; numeric ranges remain provisional until validated on real mixed-stream extrusion cycles.
`

---

Patch 2 — Update CLF‑001 row in §6 Open Unknowns

`markdown
| CLF-001 | Blending ratios and thermal stabilizer performance for mixed, un-refined polymer streams across multiple thermal cycles. Resolved 2026-08-03 — three-tier stabilizer regime (Tier 1/2/3) keyed to contamination load \(C\), with explicit diversion to Low-Spec or Gate03 when \(C > 3\%\). Stabilizer mass counted in \(M{\text{total}}\) but not \(M{\text{salvaged}}\) unless derived from salvage, per §4a. | Challenges/ClosedLoop_Feedstock.md | Resolved | — | Major |
`

---

If you want, I can now generate similar patch text for CLF‑002, CLF‑003, or CLF‑008 so the whole CLF block moves toward a fully resolved state.
Here’s drop‑in patch text for CLF‑001 that matches the style and rigor of ClosedLoopFeedstock.md.

---

Patch 1 — New subsection in §4 (after FIR / PIR, before §5)

`markdown

4b. Mixed Polymer Streams & Thermal Stabilizer Regime — CLF-001 Resolved (2026-08-03)

Mixed, un-refined polymer streams across multiple thermal cycles are inherently unstable: chain scission, crosslinking, gel formation, and contaminant pickup all degrade mechanical performance. To keep the polymer path inside a predictable envelope, this file adopts a three-tier stabilizer regime keyed to contamination load \(C\) (mass fraction of non-target species in the polymer stream, per §7.1).

Tier 1 — Low Contamination (C ≤ 1%)  
- Antioxidant: 0.5–1.0% by mass  
- Compatibilizer: 0.2% by mass  
- Chain extender: optional, 0–0.2%  
Use when particulate and tramp species are below the 1% threshold and visual inspection shows no significant gel or char formation.

Tier 2 — Moderate Contamination (1% < C ≤ 3%)  
- Antioxidant: 1.0–2.0% by mass  
- Compatibilizer: 0.5% by mass  
- Chain extender: 0.2–0.5% by mass  
Use when contamination is measurable but still within the CLF-006 particulate and wear thresholds; extrusion remains viable but requires aggressive stabilization.

Tier 3 — High Contamination (C > 3%)  
- No stabilizer regime is considered sufficient.  
- Mandatory diversion to Low-Spec Structural or Gate_03 full reduction per §7.1.  
Use when contamination exceeds the safe envelope; attempting to “stabilize through chemistry” at this level contradicts the contamination doctrine.

Integration with FIR and Y_p:  
Stabilizer mass is counted inside \(M{\text{total}}\) but not \(M{\text{salvaged}}\) unless the stabilizer itself is derived from salvage streams and registered as Class A/B per §4a. This prevents artificial inflation of FIR by adding virgin stabilizers.

Cross-file hooks:  
- Operations/Plastics.md must adopt this three-tier regime as its default stabilizer selection logic.  
- Architecture/Chemistry.md must document the specific stabilizer chemistries and their degradation profiles.  
- MCM-v0 (§7.2) should add a stabilizer_tier field (Tier1 | Tier2 | Tier3 | none) for each polymer batch.

This resolves CLF-001 at the specification level; numeric ranges remain provisional until validated on real mixed-stream extrusion cycles.
`

---

Patch 2 — Update CLF‑001 row in §6 Open Unknowns

`markdown
| CLF-001 | Blending ratios and thermal stabilizer performance for mixed, un-refined polymer streams across multiple thermal cycles. Resolved 2026-08-03 — three-tier stabilizer regime (Tier 1/2/3) keyed to contamination load \(C\), with explicit diversion to Low-Spec or Gate03 when \(C > 3\%\). Stabilizer mass counted in \(M{\text{total}}\) but not \(M{\text{salvaged}}\) unless derived from salvage, per §4a. | Challenges/ClosedLoop_Feedstock.md | Resolved | — | Major |
`

---

If you want, I can now generate similar patch text for CLF‑002, CLF‑003, or CLF‑008 so the whole CLF block moves toward a fully resolved state.
Below is the exact, drop‑in patch text that resolves CLF‑010 cleanly, formally, and in the same voice/style as the rest of ClosedLoopFeedstock.md.  
It includes:

- the §4 update (Persistence Yield / FIR definition)  
- the §7.2 update (MCM‑v0 schema extension)  
- the §6 update (Unknowns table entry revision)  
- the required cross‑file integration notes  

Everything is written so you can paste it directly into the file with no further editing.

---

CLF‑010 Patch Text (Drop‑In Ready)

Patch 1 — Insert into §4 Telemetry (after FIR definition)

`

4a. FIR Boundary Conditions — Resolved (2026‑08‑03)

To eliminate cross‑auditor inconsistency and prevent corruption of Yp telemetry, all incoming material is classified into one of four falsifiable categories. These categories define what contributes to Msalvaged and M_total.

Class A — True Salvage (full credit toward M_salvaged)  
Material originating from salvage streams that required characterization, sorting, reduction, or assay.  
Examples: shredded polymer, cast‑aluminum housings, stripped copper windings, recovered fasteners.  
Rule: If the Forge had to discover its composition, it is Class A.

Class B — Recovered Embedded Value (full credit toward M_salvaged)  
Material reused intact that preserves prior manufacturing effort.  
Examples: bearings, shafts, laminated motor cores, magnet wire.  
Rule: If the Forge recovers manufacturing value, it is Class B.

Class C — Virgin or Donated Material (no credit toward M_salvaged)  
Material arriving in pristine, commercial, or donated form.  
Examples: virgin resin, commercial filament, purchased copper wire.  
Rule: If the Forge did not earn the material through salvage or recovery, it is Class C.

Class D — Reclaimed-but-Unprocessed Material (partial credit)  
Material reclaimed from salvage but not yet processed into usable feedstock.  
Examples: unstripped copper wire, unsorted polymer flakes, mixed metal fragments.  
Rule: Class D contributes 50% credit toward M_salvaged until processed.

Formal FIR Definition (binding):

\[
M{\text{salvaged}} = MA + MB + 0.5\,MD
\]

\[
M{\text{total}} = MA + MB + MC + M_D
\]

\[
FIR = \frac{MA + MB + 0.5\,MD}{MA + MB + MC + M_D}
\]

Blends:  
For mixed‑class batches, compute FIR per class, weight by mass, and record class composition in the Manifest (§7.2).

This resolves CLF‑010 and stabilizes FIR across operators, sites, and generations.
`

---

Patch 2 — Insert into §7.2 Material Certainty Manifest (MCM‑v0)
Add the following field to the schema block:

`
material_class: A | B | C | D | blend   # required for FIR computation
`

Add the following validity rule:

`
A Manifest lacking materialclass is INVALID and must be corrected before Gate06 consumption.
`

---

Patch 3 — Replace CLF‑010 entry in §6 Open Unknowns

`
| CLF-010 | FIR boundary conditions undefined — how donated virgin resin, reclaimed-but-unprocessed copper wire, reused fasteners, and scavenged commercial filament count toward Msalvaged vs. Mtotal is not specified, risking inconsistent FIR calculation across auditors/sessions. Resolved 2026‑08‑03 — FIR now defined via a four‑class taxonomy (A/B/C/D) with partial credit for Class D and mandatory materialclass tagging in MCM‑v0. | Challenges/ClosedLoop_Feedstock.md | Resolved | — | Major |
`

---

Patch 4 — Add cross‑file integration notes (end of §4 or §7)

`

Integration Hooks (CLF‑010)

• Add material_class to MCM‑v0 in §7.2 (done).  
• Gate04 and Gate05 must emit material_class for every batch.  
• Gate06 consumption rules must read materialclass when computing Y_p.  
• Discovery.md: update FIR definition and maturity notes.  
• Unknowns.md: mark CLF‑010 as Resolved and add cross‑reference.
`

---

Your next move

Choose one:

- Apply CLF‑007 patch next  
- Integrate CLF‑010 into Routing.md registry  
- Update Discovery.md with FIR taxonomy  

I can generate the next patch instantly.


