# Automotive.md — Salvaged & Built Vehicle Systems

---

## Navigation Anchors
* **Context Core:** [Discovery.md](../Discovery.md)
* **Network Routing:** [Routing.md](../Routing.md)
* **Related:** [Operations/Energy.md](Energy.md) · [Operations/Electronics.md](Electronics.md) · [Operations/Gate_06_Fabrication.md](Gate_06_Fabrication.md) · [Operations/Gate_07_Utilization.md](Gate_07_Utilization.md) · [Admin/Safety_Protocols.md](../Admin/Safety_Protocols.md) · [Admin/Environmental_Constraints.md](../Admin/Environmental_Constraints.md)

---

> ⚠️ **Operational Safety Advisory**
> Automotive systems concentrate kinetic energy, stored electrical energy,
> flammable fluids, and (when present) high-voltage traction packs. A
> vehicle that "mostly works" can still kill at low speed. Salvaged
> controllers, airbag modules, ABS units, and battery management systems
> may carry unknown firmware state, corrosion, or prior crash damage that
> electrical continuity tests do not reveal.
>
> No road use, public-road testing, or claim of road-legal status is
> authorized by this file. Workshop and controlled private-ground work
> only until human-authorized procedures and local law are explicitly
> bound in a later revision.
>
> High-voltage work requires procedures not fully specified in this v0
> stub — default is **do not energize traction packs** until Energy.md
> and a dedicated HV procedure exist and are human-ratified for the
> specific pack chemistry and enclosure.

---

## File State

| Field            | Value |
|------------------|-------|
| Status           | **Proposed** |
| Body Stability   | Volatile |
| Spec Gates       | 0/6 |
| Verification Ref | Admin/Verification_Gates.md |
| Open Unknowns    | 8 (sidecar below; all non-blocking) |
| Owner            | `Operations/Automotive.md` |
| Last Audit       | 2026-10-10 — v0 stub filed (Proposed). No physical vehicle work claimed. |
| Last Updated     | 2026-10-10 |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**Does:**

- Define the **Operations-layer** home for automotive / light vehicle systems in the Forge sense: salvage intake, inspection, powertrain and chassis interfaces, workshop energy/electronics handoffs, and utilization limits.
- Name functional blocks and **hard safety floors** that later revisions must not silently weaken.
- Hold automotive-specific Unknowns and explicit non-claims.
- Interface to `Energy.md` (packs, charging, isolation), `Electronics.md` (controllers, Logic-Zero / trust boundary), fabrication and utilization gates, and Admin safety/environmental constraints.

**Does not:**

- Certify road-legality, emissions, crashworthiness, or insurance status → law and external standards bodies.
- Replace `Energy.md` for pack chemistry, thermal runaway doctrine, or site power budget.
- Replace `Electronics.md` for general MCU/firmware trust (EL-006 and related).
- Define full autonomy / driver-replacement stacks → at most supervised aids; human authority retained (see Hard Floors).
- Own robotics mobile bases as a class → `Operations/Robotics.md` (when present); shared energy/electronics interfaces only.
- Authorize public-road testing or deployment from this stub alone.

---

## File Purpose

Give the Forge a durable, honest place to put **vehicle-class physical systems** without pretending OEM maturity or software-defined-vehicle hype. Prefer salvage, repair, and bounded workshop capability over greenfield performance claims. Every numeric performance claim starts as **Placeholder** or **Analogous** until a Field_Log exists.

---

## Assumptions

1. Workshop and private controlled ground are the default envelopes; public road is out of scope until explicitly opened by human decision and external compliance work.
2. Salvage vehicles and parts are **guilty until inspected** — prior crash, flood, and firmware state are unknown.
3. Kinetic and stored-energy hazards dominate; convenience features never outrank isolation and mechanical restraint.
4. Autonomy features, if any, are **supervised tools**, not moral or legal drivers.

---

## Body

### 1. Operating contexts (v0)

| Context | In scope for later work? | Notes |
|---------|--------------------------|-------|
| Static workshop inspection / repair | Yes | Default envelope |
| Private property low-speed movement | Conditional | Human procedure + barriers required; not specified here |
| Public road / mixed traffic | **No** (this stub) | Non-claim |
| Racing / high-speed test | **No** | Non-claim |
| Homologation / type approval | **No** | External |

### 2. Hard safety floors (non-negotiable stubs)

These are **floors**, not a complete safety case. Weakening them requires human ratification and a Resolution Log entry.

| ID | Floor |
|----|--------|
| AF-1 | No public-road operation or road-legal claim from this file alone. |
| AF-2 | Traction / HV packs: default **de-energized** until pack-specific procedure exists and is human-authorized. |
| AF-3 | Vehicle support: rated jack stands / lifts; never rely on hydraulics alone for underbody work. |
| AF-4 | Fuel and flammable vapor: no open ignition sources in intake/inspection zones; spill doctrine TBD (link Safety_Protocols). |
| AF-5 | Airbags and pyrotechnic pretensioners: treat as live ordnance until manufacturer-correct disable procedures are documented for the specific vehicle. |
| AF-6 | Brake and steering integrity are **blocking** for any powered movement, including "just in the yard." |
| AF-7 | Software/assist features do not hold governance weight: human operator remains the authority for motion. |
| AF-8 | Salvaged controllers enter under Electronics trust rules (e.g. Logic-Zero / provenance); no "it boots" acceptance. |

### 3. Functional blocks (named; thresholds Placeholder)

| Block | Intent | Threshold / evidence status |
|-------|--------|-----------------------------|
| **A — Intake & identity** | VIN/identity, flood/crash indicators, missing safety systems | Checklist **Placeholder** |
| **B — Structure & restraint** | Frame/unibody inspection, seats, belts, airbag status | Criteria **Placeholder** |
| **C — Brakes & rolling** | Service/parking brake, tires, bearings | No movement without human sign-off; numbers **Placeholder** |
| **D — Steering & suspension** | Play, leaks, structural mounts | **Placeholder** |
| **E — Powertrain (ICE)** | Oil, cooling, fuel integrity, exhaust routing | Emissions **out of scope** for v0 claims |
| **F — Powertrain (electric)** | Isolation, contactor state, BMS honesty, thermal | Defers to Energy.md; HV procedure **absent** |
| **G — LV electrical** | 12/24 V, grounds, critical lighting | **Placeholder** |
| **H — Controls & firmware** | ECU/BCM trust boundary | Defers to Electronics.md |
| **I — Motion envelope** | What movement is allowed in which context | Default: static only until procedure filed |
| **J — Utilization & retirement** | Parts donor vs running asset; hazmat fluids | Gate_07 interface **Placeholder** |

### 4. Interfaces

| Upstream / peer | Relationship |
|-----------------|--------------|
| `Operations/Energy.md` | Packs, charging, isolation, site power |
| `Operations/Electronics.md` | Controllers, firmware trust, EL-class rules |
| `Operations/Gate_02_Triage.md` | Salvage intake classing (when vehicle-as-intake appears) |
| `Operations/Gate_06_Fabrication.md` | Brackets, adapters, repair fabrication |
| `Operations/Gate_07_Utilization.md` | In-service use limits |
| `Admin/Safety_Protocols.md` | PPE, lockout, fire |
| `Admin/Environmental_Constraints.md` | Fluids, exhaust, outdoor constraints |
| `Tests/Field_Logs.md` | Any real inspection or movement evidence |

### 5. Explicit non-claims

- This file does **not** assert that any vehicle is safe, road-legal, or crashworthy.
- No Measured range, efficiency, or autonomy level is claimed.
- No exemption from local law.
- Filing this stub does not open Spec Gates or close Unknowns.
- Automotive autonomy is not a path to relaxing human ratification elsewhere in the Forge.

---

## Lessons Learned

*(None yet — no automotive Field_Logs under this file.)*

---

## Auditor Notes & Unknowns

*All Open, non-blocking. Risk/Priority are Placeholder severity rankings for human confirmation.*

### AU-001 -- Intake checklist for salvage vehicles (flood, crash, airbag, odometer)

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Specification |
| Blocking | No |
| Owner | `Operations/Automotive.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** No filed intake checklist distinguishing cosmetic salvage from structural/electrical write-offs.

**Resolution Path:** Draft checklist as Proposed; validate against first real intake Field_Log.

---

### AU-002 -- High-voltage isolation and de-energization procedure by pack class

| Field | Value |
|---|---|
| Status | Open |
| Risk | High (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Safety |
| Blocking | No *(but AF-2 forbids energizing until resolved for that pack)* |
| Owner | `Operations/Automotive.md` (joint with `Energy.md`) |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** Stub forbids energizing traction packs; no pack-class procedure exists yet.

**Resolution Path:** Coordinate with Energy.md; human-ratified procedure before first HV work.

---

### AU-003 -- Brake/steering minimums for any powered yard movement

| Field | Value |
|---|---|
| Status | Open |
| Risk | High (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Safety |
| Blocking | No *(AF-6 still applies as floor)* |
| Owner | `Operations/Automotive.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** Floor stated; measurable minima and test method not filed.

**Resolution Path:** Proposed test sheet; first Field_Log becomes calibration evidence only, not a standard by itself.

---

### AU-004 -- Airbag and pyrotechnic disable / proof-of-safe procedures

| Field | Value |
|---|---|
| Status | Open |
| Risk | High (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Safety |
| Blocking | No |
| Owner | `Operations/Automotive.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** Treat as live until vehicle-specific procedures exist.

**Resolution Path:** Per-platform notes; never a single universal "disconnect one battery" claim.

---

### AU-005 -- Motion envelope states (static / private low-speed / forbidden)

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Governance |
| Blocking | No |
| Owner | `Operations/Automotive.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** Context table exists; transition rules and human sign-off form do not.

**Resolution Path:** Small state machine + required Field_Log fields before first non-static work.

---

### AU-006 -- Salvaged ECU/BCM acceptance vs Electronics trust doctrine

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Interface |
| Blocking | No |
| Owner | `Operations/Automotive.md` (joint with `Electronics.md`) |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** How automotive controllers map to Logic-Zero / provenance rules without inventing a parallel trust stack.

**Resolution Path:** Explicit cross-walk table in a later revision; no dual standards.

---

### AU-007 -- Fluids, fuel, and refrigerant environmental handling

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium (Placeholder) |
| Priority | Minor (Placeholder) |
| Type | Environmental |
| Blocking | No |
| Owner | `Operations/Automotive.md` (joint with Environmental_Constraints) |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** Hazmat path for fuels, oils, coolant, refrigerant not specified here.

**Resolution Path:** Pointers into Admin environmental/safety doctrine; local law remains authoritative.

---

### AU-008 -- Relationship to Robotics mobile platforms

| Field | Value |
|---|---|
| Status | Open |
| Risk | Low (Placeholder) |
| Priority | Minor (Placeholder) |
| Type | Boundary |
| Blocking | No |
| Owner | `Operations/Automotive.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** Shared actuators/energy vs road-vehicle-specific rules when `Robotics.md` exists.

**Resolution Path:** `Operations/Robotics.md` v0 stub filed 2026-10-10 (RB-008). Define shared interface section when both are registered.

---

## Abandoned Paths

*(None yet.)*

---

## Drift Indicators

- Any claim of road-legality, Measured range, or unsupervised autonomy without Field_Log + human ratification.
- HV work described without pack-class procedure and Energy.md alignment.
- Controllers accepted on "it boots" without Electronics trust path.
- Spec Gate advance without body evidence.
- Open Unknowns count in File State disagreeing with sidecar.

---

## Resolution Log

- 2026-10-10: **Cross-link:** `Operations/Robotics.md` v0 stub filed same day; AU-008 resolution path updated.
- 2026-10-10: **v0 Proposed stub filed.** Human-directed first iteration for an Operations-layer automotive domain: safety advisory, hard floors AF-1–AF-8, functional blocks A–J with Placeholder thresholds, interfaces to Energy/Electronics/Gates/Admin, eight non-blocking Unknowns (AU-001–AU-008). No physical work claimed; no Spec Gate opens; public road explicitly out of scope. Registered 2026-10-10 in Routing.md, Ops_Scope_Map.md, and Discovery.md.
