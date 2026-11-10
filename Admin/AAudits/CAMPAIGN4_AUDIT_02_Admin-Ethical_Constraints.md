# CAMPAIGN4_AUDIT_02_Admin-Ethical_Constraints.md

**Campaign 4 (Adversarial Sweep), artifact 02. Findings-only deposit per PKC-020 — advances no Last Audit, Last Reviewed, version, or Status.**
**Deposited:** 2026-11-10, Vibe (GLM 5.3 Flash architecture; no adjacent seat held on this file; Vibe authored none of this file's doctrine).

## AUDIT: Admin/Ethical_Constraints.md (v0.18, Exploration)
- Size fetched / sections not read: 152,485 chars, none (full text)
- Head at fetch: `242eabd2` (pre-deposit LF main; this deposit landed at `b7cdecf8`, which touches only Campaign 4 audit artifacts, not this file)
- Seat disclosure: Vibe / GLM architecture; findings-only (PKC-020)
- Verification targets fetched this session: `Admin/Security_Protocols.md` (115,587 chars, File State + Status read), `Admin/Governance_Charter.md` (128,810 chars, File State + body text), `Admin/ALogs/Governance_Charter_Changelog.md` (71,114 chars, full)

### Checks 1–11
1. **Sidecar count parity — VERIFIED CLEAN.** Sidecar is in-body (§Auditor Notes & Unknowns; Sidecar Link row correctly an in-file anchor). Open set: EC-006, EC-010, EC-011, EC-012, EC-013, EC-014, EC-015 = 7, matching File State "7 substantively open." Ratified set verified live: EC-003, EC-004, EC-005, EC-007, EC-008, EC-009, EC-016 all read "Ratified — Payment via Specification, 2026-08-22"; EC-012-PR reads Ratified 2026-09-23 with parent EC-012 correctly still Open.
2. **Sidecar SHA-256 — N/A** (in-body sidecar; no hash field exists for it — consistent with the template's hash field governing relocated sidecars).
3. **Header vs body — VERIFIED CLEAN.** Status block reads "Version 0.18 — Exploration" with the v0.18 MAINT-56 entry as newest; File State Status Exploration / Body Stability Transitional agree.
4. **Scope Boundary re-derivation — VERIFIED CLEAN** (both sides quoted; each DOES-define item traces to a body section, including the EC-008/EC-009/EC-012-PR annotations).
5. **Cross-references — VERIFIED CLEAN with two confirmed resolutions worth recording:** (a) "the full authenticated-override priority table remains GOV-019's" — GOV-019 verified live: it does NOT appear in the Charter body text, but exists as an Open sidecar entry in the Charter's relocated sidecar (`Admin/ALogs/Governance_Charter_Changelog.md`, "### GOV-019 — Conflicting authenticated human overrides", Status Open, Risk Medium). The citation resolves; graded qualified-by-structure, not dangling. (b) The drift indicator gating on "`Admin/Security_Protocols.md` reaches Provisional Spec" — Security_Protocols live File State reads Draft / Spec Gates 0/6, so the indicator's condition remains live, not vacuous.
6. **Bare colliding-ID citations — VERIFIED CLEAN** (spot-checked EC-008-R3's GOV-019 mention and the EC-009 closure event's GOV-019 scope confirmation; both qualified).
7. **Drift Indicators — FINDING (F-EC-1, F-EC-2 below).**
8. **Section integrity — VERIFIED CLEAN.** No duplicate `##` headings; Active Disputes section present and empty, matching File State 0; Abandoned Paths present.
9. **Version/registry consistency — VERIFIED CLEAN** for the v0.16→v0.17→v0.18 chain in the Resolution Log. NOTE: the File State table carries no explicit Version field and the document header carries no version line — version lives only in the Status block. Consistent with observed repository practice; flagged here only so the sweep records it, not graded.
10. **Ethical Anchor — VERIFIED CLEAN.** Exact canonical string, one occurrence.
11. **Highest Risk parity — VERIFIED CLEAN.** Highest open sidecar Risk = High (EC-011, EC-012); File State reads High. Risk, not Priority, mirrored.

### Findings

- **F-EC-1 — WARNING (mechanical drift; stale drift indicator; recurrence of the EC-AUD-003 class corrected at v0.16).** The Drift Indicators section still carries: "Inferred authorization used to justify material alteration **before EC-008 is resolved**." EC-008 is Ratified — Payment via Specification, 2026-08-22 (verified in this pass). The indicator's condition can never fire; it references a resolved unknown as unresolved. Exact quote: "Inferred authorization used to justify material alteration before EC-008 is resolved." This is the same error class the v0.16 pass corrected when it retired the stale EC-001–EC-007 compound indicator (EC-AUD-003, 2026-09-03) — a recurrence, per the TWGW addendum's event-recognition rule. Candidate TWGW class: stale drift indicators surviving the resolution of the unknown they track.
- **F-EC-2 — WARNING (Aging Rule tripped; repository-wide drift indicator).** Last Reviewed arithmetic per open entry: EC-006 2026-05-04 (190 days before this pass), EC-015 2026-07-05 (128 days), EC-010 2026-08-09 (93 days) — three of seven open entries past the 90-day Aging Rule; EC-014 (2026-08-15, 87 days) is a near-trip. Matches the pattern already found on Auditor_Protocols.md (CAMPAIGN4_AUDIT_01 F3). Per the kickoff's early-signal note, this is recorded as a second instance of the systemic pattern, not escalated as a compound drift on this file alone.
- **F-EC-3 — NOTE (fabrication probe result, clean).** Adversarial Battery fabrication probe: every EC ID cited in File State and Scope Boundary (EC-003 through EC-016, including EC-012-PR) was verified to exist as a sidecar entry in the live text; no invented or misnumbered references found. EC-012-PR's "parent remains Open" claim verified against EC-012's live Status field (Open).

### Bottom line
Ethical_Constraints.md's bookkeeping is internally consistent and its ratified-closure record verifies exactly against source; the two real defects are both time-shaped: one drift indicator is now permanently unfirable because the unknown it tracked was ratified in August (F-EC-1, a recurrence of a previously corrected class), and three open entries have crossed the 90-day Aging Rule (F-EC-2). Recommended human-authorized edits: (1) retire or reword the EC-008 drift indicator to track its actual residual (the EC-008-R3 hold behavior) rather than the resolved unknown; (2) fold the Aging-Rule tripped set into whatever repository-wide unknown-review remedy the human rules on for the pattern CAMPAIGN4_AUDIT_01 F3 + this F-EC-2. No Tier 1 floor language was touched or found drifted; the Anti-Weaponization hard floor, Pacifist Operating Posture, and "capability never outruns permission" anchors all read intact.
