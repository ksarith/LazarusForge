# Mapping Memo: Gemini FN-001 / FN-005 Drafts → Live Forge_Net Doctrine

**Date:** 2026-09-07  
**Source drafts:** External Gemini specifications (FN-001 Data Validation; FN-005 Data Privacy and Access Control)  
**Target of truth:** `Architecture/Forge_Net.md` — §2.5 DV-001–006, §2.5.0 taxonomy, §6 PA-001–006, NI-1–8, §1.2 Offline Envelope  
**Purpose:** Clause-level disposition (keep / rewrite / reject). This memo does **not** amend Forge_Net and does **not** close FN-001 or FN-005.

**Governing rule:** Structure for both unknowns is already Provisional Spec. Remaining work is **calibration and implementation downstream**, not a parallel Architecture stack.

---

## 1. FN-005 (Privacy / Access) → PA-001–006

| Gemini clause | Live owner | Disposition | Notes |
|---------------|------------|-------------|-------|
| Three-tier taxonomy: Tier 0 / 1 / 2 | **PA-001** `private` / `cluster` / `public` | **Reject rename** | Same idea, different labels. Adopting Tier 0/1/2 creates dual doctrine. If ever renamed, do it as a Tracked terminology change, not a silent swap. |
| Tier 0 = coordinates, keys, raw sensors, local IDs | **PA-001** `private` scope examples | **Rewrite** | Keep *class* of examples; drop hard “loopback only / reject outbound serialization” as Architecture mandate — that is implementation (Automation / Security). |
| Tier 0 never leaves node | **PA-001** fail-closed; **NI-7** | **Keep (already covered)** | Align language to existing `private`; do not re-specify. |
| Tier 1 = surplus, capacity, trade handshakes | **PA-001** `cluster` + §3.2 resource sharing | **Rewrite** | Map examples under `cluster`; avoid “cryptographically proven capacity” as mandatory Architecture until Security selects mechanisms. |
| Tier 1 encrypted channels + rotating session IDs | Security_Protocols / SEC-* adjacency | **Reject in Forge_Net** | Valid *candidate* for Security implementation, not PA-* doctrine. |
| Tier 2 = public governance logs, KPIs | **PA-001** `public` | **Keep (already covered)** | Ensure no reverse link to `private` — already PA / NI-7. |
| Spatial grid obfuscation \(G \ge 10\) km | **PA-005** location precision | **Rewrite** | Keep *coarse centroid / reduced precision* principle. **Reject fixed 10 km** as settled Architecture number; leave Placeholder or Analogous candidate only. |
| 24h / 100-tx session key rotation | Security implementation | **Reject in Forge_Net** | Policy knob for a future security stack, not FN-005 closure. |
| Master public keys never in routine headers | Identity / Security design | **Rewrite as soft candidate** | Reasonable privacy posture; does not replace PA-003 anonymization scope rules. |
| Formal access predicate \(A(R,D,P)\) with Clearance, Auth_sig, RateLimit | **PA-002** | **Reject as written** | PA-002 = cluster membership + **node reliability** (§2.5.0). “Clearance tier” + single predicate reintroduces a unified trust/clearance score. |
| Rate limiting / \(R_{max}\) | Ops / Security | **Rewrite** | Optional implementation control; not required to close FN-005 structure. |
| Tier 0 leak → hard drop + isolate thread | Incident response | **Rewrite** | Intent aligns with Integrity_Incident_Log + Major/Constitutional ladder; do not prescribe thread isolation in Architecture. |
| Unauthenticated scan → firewall block | Security / host ops | **Reject in Forge_Net** | Host firewall policy is out of Architecture Scope Boundary. |
| Coordinate profiling → fuzz + “decay peer trust score” | **PA-005** + §2.5.0 | **Rewrite carefully** | Fuzz/coarse response OK as candidate. **Must not** decay *claim confidence*. If anything decays, it is **node reliability** only, and only under defined process — not a silent Goodhart lever. |
| Closure: static analysis + two-node sandbox | Residual path | **Rewrite** | Useful *evidence* for later implementation payment; FN-005 still needs **node-reliability threshold calibration**, not only tests. |

### FN-005 summary

| Keep | Rewrite | Reject |
|------|---------|--------|
| Three visibility *ideas* mapped to existing tiers | Examples, coarse location, incident *intent* | New Tier 0/1/2 names; mandatory crypto suite; fixed 10 km; formal Clearance predicate; firewall prescriptions; trust-score decay on claims |

**Does not close FN-005.** Residual remains: PA-002 **node-reliability** thresholds + any Battery/calibration items already noted in sidecar.

---

## 2. FN-001 (Validation) → DV-001–006

| Gemini clause | Live owner | Disposition | Notes |
|---------------|------------|-------------|-------|
| Three-layer pipeline: Structural → Crypto → Epistemic | §2.5 validation list + DV-001–006 | **Rewrite** | Live pipeline is doctrinal (structural, consistency, source *process*, redundancy), not a crypto stack. Crypto is not Layer-2 of DV. |
| Layer 1 schema / type enforcement | **DV-001** | **Keep as class** | Schema version field is a good *candidate* under DV-001; do not mandate JSON/YAML or Repository_Structure as the schema home without check. |
| Mandatory UUIDv4, ISO timestamp, origin_node_id, schema_version | **DV-001 / DV-002** | **Rewrite** | Field *kinds* are compatible with provenance; specific formats/IDs are Placeholder until chosen once. |
| 2 MB payload cap; large assets out-of-band | Implementation / FN-004 bandwidth adjacency | **Rewrite** | Sensible *candidate* limit; not Architecture closure. |
| SHA-256 body hash must match header | Security / integrity implementation | **Reject as DV mandatory** | Optional integrity aid; DV-002 does not require a named hash algorithm. |
| Asymmetric signature required or socket drop | Security | **Reject as DV mandatory** | Identity and signing live outside DV confidence model; unsigned handling may be process policy later, not “immediate socket drop” in Architecture. |
| Parameter lineage to prior state hashes | **DV-002** provenance | **Rewrite** | Lineage *idea* fits DV-002; “genesis hash chain” is one possible design, not the only. |
| Physical reality bounds (non-negative mass, etc.) | Consistency class under §2.5 | **Keep as examples** | Good epistemic/operational bound *examples*; not a complete catalog. |
| Timestamp drift ±300 s → reject (replay) | Security / sync | **Rewrite** | Replay protection is real; fixed ±300 s is a candidate constant, not settled Architecture. |
| Formal \(V(P)=1\) iff schema ∧ crypto ∧ lineage ∧ bounds | DV package | **Reject as written** | Omits minority hold (DV-004), confidence-from-evidence (DV-003), rollback (DV-005), human escalation (DV-006). A pass/fail crypto gate is not the live model (“failed validation is a signal, not a rejection”). |
| Level 1 malformed → drop connection | Process | **Rewrite** | Structural fail may reject *ingest*; “drop connection” is transport policy. |
| Level 2 bad crypto → quarantine | **DV-005** adjacency | **Rewrite** | Quarantine aligns with DV-005 *intent* for suspect content; trigger should not be “only crypto.” |
| Level 3 bounds fail → “peer reputation decay” + human audit | **DV-004 / DV-006** + §2.5.0 | **Rewrite** | Human audit aligns with DV-006. Reputation decay = **node reliability** only, never claim-confidence multiplier. Prefer hold+log (DV-004) over silent score punishment as first response. |
| Closure: sandbox harness + &lt;15 ms on base hardware | Implementation SLA | **Reject as FN-001 closure criterion** | Performance budget is Ops/Automation; FN-001 residual is **threshold calibration**, not latency SLA. |

### FN-001 summary

| Keep | Rewrite | Reject |
|------|---------|--------|
| Schema/header field *kinds*; physical bound *examples*; quarantine/human-review *intent* | Pipeline framing without crypto-as-Layer-2; lineage as DV-002 option; replay window as candidate | Mandatory SHA-256/signing for Architecture DV; socket-drop crypto gate; formal V(P) that skips DV-003/004/005/006; 15 ms closure bar |

**Does not close FN-001.** Residual remains: consistency thresholds, decay intervals, anomaly signatures (shared with FN-003), post-Battery calibration.

---

## 3. Cross-cutting risks (both drafts)

1. **Trust collision relapse** — Any “peer score / clearance / trust decay” must be explicitly **node reliability** under §2.5.0, never a multiplier on DV-003 claim confidence.  
2. **Dual doctrine** — New tier names or parallel predicates without retiring PA/DV create the same class of bug Priority-1 fixed.  
3. **Scope Boundary breach** — Crypto suites, firewalls, socket policy, and latency SLAs belong to Security / Automation / Ops, not Forge_Net Architecture closure.  
4. **False closure** — Tests and formal predicates are evidence *later*; they do not replace the sidecars’ stated residuals.

---

## 4. Recommended use of the Gemini text

| Action | Recommendation |
|--------|----------------|
| Merge into `Forge_Net.md` body | **No** |
| Register as replacement FN-001/FN-005 specs | **No** |
| Mine for DV-001 field candidates / PA-005 coarseness examples | **Yes**, under ordinary review |
| Hand Security a “candidate controls” list (hash, session rotation, rate limit) | **Yes**, labeled non-binding |
| Next real Forge_Net work | Calibration notes or ASM/NI follow-through — not a Gemini import |

---

## 5. One-line verdicts

- **Gemini FN-005:** Parallel privacy stack; map to PA-*; reject rename and crypto mandates.  
- **Gemini FN-001:** Parallel validator stack; map field/bounds *ideas* to DV-*; reject crypto-as-Architecture-gate and score-as-confidence.  
- **Neither draft pays FN-001 or FN-005.** Structure remains as in live sidecars; calibration remains open.

*Memo only. No Unknowns status change. Human-directed mapping against Alpha 12 / live Forge_Net doctrine.*
