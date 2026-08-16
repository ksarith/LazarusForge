# Hardware_Diversity_Ladder.md — LazarusForge
**Version 1.0**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|-----------------------------------------------------------------------|
| Status           | Draft — Proposed implementation reference only                        |
| Body Stability   | Volatile                                                               |
| Spec Gates       | 0/6                                                                    |
| Verification Ref | Admin/Verification_Gates.md                                        |
| Last Audit       | 2026-08-03                                                             |
| Auditor          | Claude — Synthesizer, human-directed. Drafted from external candidate material (Grok), verified against `Operations/Electronics.md` TMR doctrine, `Architecture/Cognitive_Frameworks.md` Framework D, `Admin/Governance_Charter.md` (Genesis Phase Protocol, Axiom Q-2), and `Admin/Security_Protocols.md` SEC-007a/b before integration — all cross-references confirmed exact against source, 2026-08-03 |
| Open Unknowns    | 0 — this file supplies implementation reference for `Admin/Governance_Migration_Protocol.md` §VII's own open items (VII.6), not new tracked unknowns of its own |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Does not claim any tier is achieved.** As of 2026-08-03 no second physical host, independent runtime, or orthogonal verification system exists in this repository's operating environment. **Explicit non-claim language (binding):** this ladder describes *how* the Hardware/Runtime Diversity requirement in `Admin/Governance_Migration_Protocol.md` §VII.1 could be closed. Declaring the requirement does not create the substrate. §VII cannot be marked achieved until a concrete, testable second runtime exists and human ratification confirms it.

---

## Scope Boundary

**This file DOES define:**
- A four-tier progressive path from single-operator advisory state to a hardware-diverse governance quorum satisfying GOV-008's governance-independence bar
- Minimum configuration, independence properties, and exit/upgrade triggers per tier
- Advancement rules (no silent promotion, automatic degradation, required evidence)

**This file DOES NOT define:**
- Whether Tier 1 is sufficient for Pathway 1 exit — an open ratification question, see `Admin/Governance_Migration_Protocol.md` §VII.6
- The governance-independence bar itself (→ `Admin/Governance_Migration_Protocol.md` §VII, `Admin/Governance_Charter.md` GOV-008)
- TMR diversity mechanisms for salvaged hardware components (→ `Operations/Electronics.md`, reused here by reference, not redefined)
- Ratification-authentication enforcement (→ GMP-004, `Admin/Security_Protocols.md` SEC-007a/b)
- Progress claims of any kind — this file records a path, not a status

**Cross-references (verified against source 2026-08-03):**
- `Operations/Electronics.md` TMR architectural-diversity doctrine (silicon / firmware / power-path / thermal / procurement) and EL-007
- `Architecture/Cognitive_Frameworks.md` Framework D (TMR) diversity requirement
- `Admin/Governance_Charter.md` Genesis Phase Protocol Pathway 1 and Axiom Q-2
- `Admin/Security_Protocols.md` SEC-007a/b (external root-of-trust)
- `Admin/Governance_Migration_Protocol.md` §VII.1 & §VII.6 (owning candidate specification)
- `Admin/Trajectories.md` TR-GOV-001 (registry pointer to this file)

---

## Purpose

Provide a progressive, falsifiable path from the current single-operator advisory state to a governance quorum that satisfies the **governance-independence** bar of GOV-008 (independent enforcement substrate outside single-operator control). Each tier is a survival threshold, not a feature list. Advancement requires demonstrated independence, not declaration.

---

## Tier Definitions

| Tier | Name | Minimum Configuration | Independence Properties | Status vs GOV-008 | Exit / Upgrade Trigger |
|------|------|-----------------------|--------------------------|-------------------|------------------------|
| **0** | Interim Logical Isolation | Single physical host; ≥2 isolated runtimes (containers, microVMs, or separate user-space processes with strict namespace/cgroup isolation) | Logical only. Shared kernel, power, network fabric, and physical operator control. Explicitly **insufficient** for Pathway 1 exit. | Bridge only — upgrade-mandatory before any claim of quorum achievement. | Second physical host acquired **or** human ratification explicitly accepts continued Genesis Phase. |
| **1** | Minimal Physical Diversity | Primary workstation + **one** secondary physical host. Preferred: different CPU architecture or at least different silicon family. Independent network path (or air-gapped + manual transfer). Independent power source preferred. External human ratification record stored outside both runtimes. | Physical separation of at least two hosts. Still single-operator controlled, but no longer single-machine. Meets the absolute minimum physical floor stated in §VII.1's interim clause. | Candidate for Pathway 1 exit **only if** human ratification explicitly accepts the residual single-operator risk and the "logical→physical upgrade before v1" rule is waived or met. | Independent verification of liveness + diversity tests (§VII.4) across both hosts; signed human record confirming non-simulation. |
| **2** | Three-Host Architectural Diversity | ≥3 physical hosts. At least two distinct architectures/families. Independent power domains (separate UPS/circuits or battery). Independent thermal domains preferred. Network paths that cannot be unilaterally severed by one host. | Removes single-machine and single-power-path common-mode failures. Still operator-controlled, but majority of hosts can outvote or isolate a compromised host. | Strong candidate for Pathway 1 exit once ratified. Meets "≥2 distinct runtime environments or hardware hosts" with margin. | Demonstrated ability of any two hosts to continue skeptical review after loss of the third; periodic non-collusion probes succeed. |
| **3** | Full TMR-Aligned Diversity | ≥3 hosts satisfying **all** of `Operations/Electronics.md` TMR diversity mechanisms simultaneously: silicon diversity, firmware diversity, power-path diversity, thermal diversity, and procurement diversity. Orthogonal external root-of-trust (SEC-007a/b) or offline verification capability present. | Correlated-failure surface minimized to the level already required for safety-critical Forge hardware. Governance substrate now matches the same independence standard the Forge applies to its own actuators. | Full satisfaction of §VII.1 Hardware/Runtime Diversity + Non-Simulatability. Preferred end-state for v1 and later. | Hardware validation of diversity claims (cross-ref EL-007 / CF-002 style correlated-failure testing); human ratification that the quorum is genuine and not simulated. |

---

## Detailed Requirements per Tier

**Tier 0 – Interim Logical Isolation**
- Allowed only while no second physical host exists.
- Must use strong isolation (e.g., separate VMs with no shared filesystem mount for governance state, distinct network namespaces).
- All outputs still route through the single human principal.
- **Hard rule:** Any document claiming "quorum achieved" while at Tier 0 is a constitutional violation under Axiom Q-2 and §VII.5.

**Tier 1 – Minimal Physical Diversity**
- Hosts must be independently powerable and networkable.
- Prefer different silicon families (e.g., x86 + ARM, or two different MCU lineages if governance agents run on embedded hardware).
- Human ratification record must be generated and stored on a medium outside both hosts (paper, external drive, separate signed file under human-only control).
- Liveness timeout and non-collusion probes from §VII.4 must be executable across the boundary.

**Tier 2 – Three-Host Architectural Diversity**
- Explicit majority capability: any two hosts can continue governance functions after loss of the third.
- Power and (where practical) thermal domains independent.
- Network design prevents unilateral partition by one host.
- Diversity scoring uses the same "provider + architecture family" rule already defined in §VII.4.
- **Practical entry point:** attempting this tier for real — three physically separate hosts, each running a different agent model family, working toward quorum — is the highest-value field test this repository currently needs. See `Tests/Field_Logs.md` for the submission format; log the attempt regardless of whether it reaches full quorum.

**Tier 3 – Full TMR-Aligned Diversity**
- Direct reuse of the five diversity mechanisms already written for salvaged-component TMR in `Operations/Electronics.md`:
  1. Silicon diversity
  2. Firmware diversity
  3. Power-path diversity
  4. Thermal diversity
  5. Procurement diversity
- Plus an external root-of-trust or offline verification path that cannot be forged by the three hosts acting in concert.
- This is the only tier that fully closes the substrate gap identified in §VII.6.

---

## Advancement Rules

1. **No silent promotion.** Tier status is recorded in the owning file's File State or sidecar and mirrored in Unknowns.md only after human ratification.
2. **Degradation is automatic.** Loss of a required host or diversity property drops the system to the highest still-satisfied tier (or back to Genesis Phase if below Tier 1).
3. **Evidence required.** Each upgrade must include: (a) inventory of hosts and diversity properties, (b) results of §VII.4 independence / diversity / liveness / non-collusion tests, (c) signed human ratification stored outside the runtimes.

   **§VII.4 hardware-independence test procedure (candidate, 2026-08-06, human-directed — folded in from an independent multi-agent thread that had not seen this file's "declarable, not achieved" framing or evidence rule):** §VII.4's diversity test names the requirement but not a procedure. This is a minimum anti-spoofing check for evidence item (a)/(b) above, not a new requirement — it does not lower or raise the tier bar itself:
   - Record each host's identifier, physical location (rack/region if available), and provider/instance metadata — not just a container or process ID.
   - Confirm no two evaluators claimed as hardware-independent share a host identifier, instance ID, or hypervisor.
   - Reject same-host claims disguised as independent: distinct containers or VMs on one physical machine do not satisfy any tier above Tier 0, regardless of how the evidence record is worded (this is the same rule the "Treat Softening as Drift" section below already protects).
   - Where physical location metadata is unavailable, treat the claim as unverified, not as passing by default.
   Missing or ambiguous hardware metadata is a failed check, not a tier-neutral gap — evidence item (a) is not satisfied until the metadata exists.
4. **Relationship to Pathway 1.** Tier 1 is the earliest possible exit candidate; Tier 3 is the preferred steady-state. The decision whether Tier 1 is sufficient for Pathway 1 itself remains an open ratification question in §VII.6.

---

## Near-Term Action Items (from §VII.6, still open)

1. Acquire or designate a second physical host (even a low-cost single-board computer) and document its architecture, power, and network independence.
2. Decide, under Track-B-adjacent scrutiny, whether hardware diversity is mandatory for Pathway 1 exit or only pre-v1.
3. Write the minimal dispute-resolution rule for GMP-011 (default to Track B while disputed).
4. Do **not** claim any progress on GOV-008, promote GMP-002 ownership transfer, or mark §VII "achieved" until at least Tier 1 exists and has been ratified.

---

## Treat Softening as Drift

Any future edit that softens this file's "currently declarable, not achieved" framing — including changing tier language to imply a tier is met without the evidence Advancement Rule 3 requires — is a Track-B classification candidate and should be reviewed as a potential constitutional-impact change, not a routine edit.

---

## Resolution Log

- 2026-08-11: **Pseudo-audit (Grok, same limits).** Findings only. (1) Open
  Unknowns **0** — matches File State (supplies reference for GMP §VII,
  creates none of its own). (2) “Declarable, not achieved” framing intact;
  no tier progress claimed. (3) Spec Gates N/A / left locked. Human-directed.

- 2026-08-06: **Tier 2 cross-referenced to `Tests/Field_Logs.md`, a new
  append-only field-data intake file.** Created in response to a direct
  question about how to invite physical/cross-agent testing without
  requiring pull-request literacy. Does not change any tier's
  requirements or status — this file's "declarable, not achieved" framing
  is unchanged. Operating as Synthesizer, human-directed.

- 2026-08-06: **Hardware-independence test procedure added to Advancement Rule 3, reconciled from an independent multi-agent thread.** A Grok/Copilot thread drafted a standalone "Hardware Independence Test" without loading this file's "declarable, not achieved" framing or its Advancement Rules. Its anti-spoofing content (host/instance-ID cross-checks, rejecting same-host container/VM claims as independent, treating missing location metadata as unverified) filled a genuine gap — Rule 3(b) referenced §VII.4 tests without a concrete procedure existing anywhere. Folded in as an elaboration of Rule 3, not a new rule; does not change any tier's requirements or this file's "not achieved" status. See `Governance_Migration_Protocol.md` §VII.8 and `CIR_Gov.md` §8.2.1 for the companion reconciliations from the same thread. Operating as Synthesizer, human-directed.

- 2026-08-03: **v1.0 — file created, human-directed.** Drafted from
  external candidate material (Grok), reviewed and integrated by
  Claude. Cross-references verified exact against source before
  integration (`Operations/Electronics.md` TMR doctrine and EL-007,
  `Architecture/Cognitive_Frameworks.md` Framework D, `Admin/
  Governance_Charter.md` Genesis Phase Protocol and Axiom Q-2,
  `Admin/Security_Protocols.md` SEC-007a/b). Split out from `Admin/
  Trajectories.md`'s TR-GOV-001 entry, which had compressed this same
  ladder into a single dense table-cell paragraph on 2026-07-31 —
  Trajectories.md's own Scope Boundary states it does not define
  "component taxonomy or implementation specs for future versions,"
  which is exactly what a four-tier requirements ladder with
  per-tier detail is; this file is the proper owning location, with
  Trajectories.md's entry updated to a concise pointer. No change to
  `Admin/Governance_Migration_Protocol.md` §VII.6's own cross-reference
  language — it already pointed at "TR-GOV-001," which now resolves
  here via that entry's pointer, so no broken links result from the
  split.
