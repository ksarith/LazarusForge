# Robotics.md — Mobile & Manipulator Systems (Salvage-Aware)

---

## Navigation Anchors
* **Context Core:** [Discovery.md](../Discovery.md)
* **Network Routing:** [Routing.md](../Routing.md)
* **Related:** [Operations/Energy.md](Energy.md) · [Operations/Electronics.md](Electronics.md) · [Operations/Automotive.md](Automotive.md) · [Operations/Gate_06_Fabrication.md](Gate_06_Fabrication.md) · [Operations/Gate_07_Utilization.md](Gate_07_Utilization.md) · [Admin/Safety_Protocols.md](../Admin/Safety_Protocols.md) · [Admin/Environmental_Constraints.md](../Admin/Environmental_Constraints.md) · [Admin/Ethical_Constraints.md](../Admin/Ethical_Constraints.md)

---

> ⚠️ **Operational Safety Advisory**
> Robots concentrate actuator force, pinch/crush hazards, stored electrical
> energy, and — when mobile — momentum in human-shared spaces. A system
> that "follows a path" can still injure at low speed. Salvaged arms,
> mobile bases, motor drivers, and vision modules may carry unknown
> firmware, missing safety interlocks, or mechanical wear that software
> demos do not reveal.
>
> No unsupervised operation in spaces occupied by people is authorized
> by this file. No claim of general-purpose autonomy, AGI embodiment, or
> replacement of human judgment is authorized by this file.
>
> Force-capable manipulators and mobile bases default to **power removed
> / mechanically restrained** until a human-authorized procedure for the
> specific platform exists. Collaborative ("cobot") labeling from a prior
> owner is not acceptance.

---

## File State

| Field            | Value |
|------------------|-------|
| Status           | **Proposed** |
| Body Stability   | Volatile |
| Spec Gates       | 0/6 |
| Verification Ref | Admin/Verification_Gates.md |
| Open Unknowns    | 8 (sidecar below; RB-002, RB-003 and RB-007 are Blocking for the stated physical work, the other 5 non-blocking; the three Blocking items also indexed in `Unknowns.md`) |
| Owner            | `Operations/Robotics.md` |
| Last Audit       | 2026-10-10 — v0 stub filed (Proposed). No physical robot work claimed. |
| Last Updated     | 2026-10-10 |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**Does:**

- Define the **Operations-layer** home for robotics in the Forge sense: mobile bases, manipulators, end-effectors, and their workshop integration — salvage intake, inspection, energy/electronics handoffs, and utilization limits.
- Name functional blocks and **hard safety floors** that later revisions must not silently weaken.
- Hold robotics-specific Unknowns and explicit non-claims.
- Interface to `Energy.md`, `Electronics.md`, `Automotive.md` (shared energy/rolling interfaces only), fabrication and utilization gates, and Admin safety / environmental / ethical constraints.

**Does not:**

- Define AGI, general autonomy, or "robot rights" doctrine → out of scope; human authority retained.
- Replace `Electronics.md` for MCU/firmware trust (EL-006 and related).
- Replace `Energy.md` for pack/bus design or site power budget.
- Replace `Automotive.md` for on-road vehicle systems; wheeled bases that are *not* road vehicles may share interfaces but not road-legal claims.
- Authorize unsupervised human-shared-space operation from this stub alone.
- Own full ROS/stack architecture as product documentation — only Forge operational constraints and evidence rules.

---

## File Purpose

Give the Forge a durable, honest place for **force- and motion-capable machines** without demo-driven overclaim. Prefer salvage, repair, bounded teleoperation, and supervised assists over greenfield "full autonomy" narratives. Every numeric force, speed, or endurance claim starts as **Placeholder** or **Analogous** until a Field_Log exists.

---

## Assumptions

1. Default envelope is a **controlled workshop cell** with clear human exclusion or supervised proximity rules — not public spaces.
2. Salvage platforms are **unsafe until inspected**; missing E-stops and altered firmware are expected failure modes.
3. Actuator force and pinch points dominate; perception ML does not reduce mechanical floors.
4. Autonomy features, if any, are **supervised tools**; governance weight and motion authority remain human.

---

## Body

### 1. Operating contexts (v0)

| Context | In scope for later work? | Notes |
|---------|--------------------------|-------|
| Static bench / powered-down inspection | Yes | Default envelope |
| Fixtured cell, human outside fence or known zone | Conditional | Procedure + interlocks required; not specified here |
| Supervised teleoperation in workshop | Conditional | Human in continuous control loop |
| Unsupervised operation with people present | **No** (this stub) | Non-claim |
| Public space / outdoor unattended mobile | **No** | Non-claim |
| Weaponized or coercion-capable configurations | **No** | Forbidden under Ethical_Constraints posture |

### 2. Hard safety floors (non-negotiable stubs)

These are **floors**, not a complete safety case. Weakening them requires human ratification and a Resolution Log entry.

| ID | Floor |
|----|--------|
| RF-1 | No unsupervised operation in human-occupied space from this file alone. |
| RF-2 | Force-capable axes: default **power removed** and **mechanically restrained** until platform procedure exists and is human-authorized. Support gravity or spring loads before removing power (RF-9). |
| RF-3 | E-stop and power isolation must be understandable and reachable by the human operator; software-only stop is not sufficient as the sole floor. |
| RF-4 | Pinch, crush, and stored-energy (gravity, spring, pneumatic) hazards are identified before power-up. |
| RF-5 | Salvaged motor drivers and controllers enter under Electronics trust rules; no "it homes" acceptance. |
| RF-6 | Perception or planning software does not relax RF-1–RF-5. |
| RF-7 | Human remains motion authority; robot output has **no governance weight**. |
| RF-8 | No integration path that converts the platform into a weapon or coercion tool (align Ethical_Constraints / anti-weaponization posture). |
| RF-9 | Before removing power or releasing a brake on any gravity-loaded or spring-loaded axis, the load is mechanically supported; power-down order is part of the platform procedure. |
| RF-10 | After power-off, stored electrical energy (drive bus capacitors) is verified discharged before hands-on work; waiting a fixed time is not verification. |
| RF-11 | The safety channel (E-stop, contactors, safety relays) is function-tested, not presumed from presence, before any powered motion; salvaged safety components are untrusted until tested. Reset after an E-stop must not restart motion; a deliberate restart action is required. |
| RF-12 | Other cell hazards are identified before power-up: hydraulic pressure (injection injury), laser or lidar emitters (eye safety), and mobile-base lithium packs (fire-capable; see EV-003 and `Operations/Energy.md`). |

### 3. Functional blocks (named; thresholds Placeholder)

| Block | Intent | Threshold / evidence status |
|-------|--------|-----------------------------|
| **A — Intake & identity** | Platform class, DOF, payload rating (claimed vs unknown), missing guards | Checklist **Placeholder** |
| **B — Mechanical structure** | Frame cracks, backlash, cable management, end-effector security | Criteria **Placeholder** |
| **C — Actuation & power train** | Motors, gearboxes, pneumatics/hydraulics leaks | Force/speed limits **Placeholder** |
| **D — Electrical & HV/LV buses** | Isolation, emergency power-down path | Defers partly to Energy.md; discharge verification per RF-10 |
| **E — Control & firmware** | Teach pendant / stack trust boundary | Defers to Electronics.md |
| **F — Sensing** | Encoders, limits, optional vision — honesty of telemetry | EC-012-related caution **Placeholder** |
| **G — Safety channel** | E-stop, light curtains, zone control (if any) | Presence **required** before unsupervised claims, and function-tested per RF-11; v0 forbids unsupervised |
| **H — Motion envelope** | Allowed modes: dead / teach / supervised auto | Default: dead + inspection only |
| **I — End-effector & task** | Gripper/tool change; task-specific hazards | Per-task **Placeholder** |
| **J — Utilization & retirement** | Cell integration vs donor parts; battery/hazmat | Gate_07 interface **Placeholder** |

### 4. Interfaces

| Upstream / peer | Relationship |
|-----------------|--------------|
| `Operations/Energy.md` | Mobile packs, bus voltage, isolation |
| `Operations/Electronics.md` | Controllers, firmware trust, EL-class rules |
| `Operations/Automotive.md` | Shared rolling/energy patterns only; no road claims |
| `Operations/Gate_06_Fabrication.md` | Mounts, guards, adapters |
| `Operations/Gate_07_Utilization.md` | In-service cell limits |
| `Admin/Safety_Protocols.md` | PPE, lockout, cell entry |
| `Admin/Environmental_Constraints.md` | Outdoor/dust/thermal envelopes |
| `Admin/Ethical_Constraints.md` | Anti-weaponization, human harm floors |
| `Tests/Field_Logs.md` | Any real power-up, teach, or motion evidence |

### 5. Explicit non-claims

- This file does **not** assert that any robot is safe for collaborative use.
- No Measured payload, repeatability, MTBF, or autonomy level is claimed.
- No AGI, general household robot, or unattended public mobile robot claim.
- Filing this stub does not open Spec Gates or close Unknowns.
- Robotics software success does not promote claim confidence or governance weight elsewhere in the Forge.

---

## Lessons Learned

*(None yet — no robotics Field_Logs under this file.)*

---

## Auditor Notes & Unknowns

*All Open. RB-002, RB-003 and RB-007 are Blocking for the physical work named in each entry (changed 2026-10-10 from non-blocking: the file's own floors already forbid that work until they are resolved; cf. the EL-005 correction in `Operations/Electronics.md`). The rest are non-blocking. Risk/Priority are Placeholder severity rankings for human confirmation.*

### RB-001 -- Platform intake checklist (DOF, payload unknown, guards, E-stop)

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Specification |
| Blocking | No |
| Owner | `Operations/Robotics.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** No filed intake checklist for salvage arms/bases vs complete unknown state.

**Resolution Path:** Draft checklist as Proposed; first Field_Log calibrates only, does not set a standard alone.

---

### RB-002 -- Power-down, restraint, and E-stop minimums before any powered motion

| Field | Value |
|---|---|
| Status | Open |
| Risk | High (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Safety |
| Blocking | Yes, scoped: first power-up of any force-capable axis -- changed from No 2026-10-10; RF-2/RF-3 already forbid it until resolved |
| Owner | `Operations/Robotics.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |
| Indexed | `Unknowns.md` > Operations -- Automotive & Robotics |

**Description:** Floors stated; platform-class procedures and test methods not filed.

**Resolution Path:** Per-class procedure; human authorization before first power-up Field_Log.

---

### RB-003 -- Force and speed caps for supervised workshop motion

| Field | Value |
|---|---|
| Status | Open |
| Risk | High (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Safety |
| Blocking | Yes, scoped: first powered motion, including supervised -- changed from No 2026-10-10; no motion without force and speed caps |
| Owner | `Operations/Robotics.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |
| Indexed | `Unknowns.md` > Operations -- Automotive & Robotics |

**Description:** No numeric caps; any later numbers start Placeholder until measured in cell.

**Resolution Path:** Conservative Proposed defaults → Field_Log → revise; never demo-driven.

---

### RB-004 -- Salvaged servo/driver acceptance vs Electronics trust doctrine

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Interface |
| Blocking | No |
| Owner | `Operations/Robotics.md` (joint with `Electronics.md`) |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** Cross-walk to Logic-Zero / provenance without a parallel trust stack.

**Resolution Path:** Explicit table in a later revision; no "it homes" acceptance rule.

---

### RB-005 -- Motion envelope states (dead / teach / supervised / forbidden)

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Governance |
| Blocking | No |
| Owner | `Operations/Robotics.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** Context table exists; transition rules and required human sign-off form do not.

**Resolution Path:** Small state machine + Field_Log fields before first non-dead work.

---

### RB-006 -- Telemetry honesty for limit switches and force/torque claims

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Epistemic |
| Blocking | No |
| Owner | `Operations/Robotics.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** Firmware-reported state is not ground truth (align EC-012 caution).

**Resolution Path:** Require independent check paths for safety-relevant sensors where feasible; document residual when not.

---

### RB-007 -- Human-shared space and "collaborative" labeling policy

| Field | Value |
|---|---|
| Status | Open |
| Risk | High (Placeholder) |
| Priority | Major (Placeholder) |
| Type | Safety / Governance |
| Blocking | Yes, scoped: any operation with people in the cell or space -- changed from No 2026-10-10; RF-1 already forbids it |
| Owner | `Operations/Robotics.md` |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |
| Indexed | `Unknowns.md` > Operations -- Automotive & Robotics |

**Description:** OEM cobot labels do not grant unsupervised presence; policy for supervised proximity TBD.

**Resolution Path:** Human decision + procedure; default remains exclusion or continuous supervision.

---

### RB-008 -- Boundary with Automotive (mobile bases vs on-road vehicles)

| Field | Value |
|---|---|
| Status | Open |
| Risk | Low (Placeholder) |
| Priority | Minor (Placeholder) |
| Type | Boundary |
| Blocking | No |
| Owner | `Operations/Robotics.md` (joint with `Automotive.md` AU-008) |
| First Logged | 2026-10-10 |
| Last Reviewed | 2026-10-10 |

**Description:** Shared energy/rolling interfaces without importing road-vehicle claims or vice versa.

**Resolution Path:** Short shared-interface note in both files once both stubs are registered.

---

## Abandoned Paths

*(None yet.)*

---

## Drift Indicators

- Any unsupervised human-shared-space claim without procedure + human ratification.
- Force/speed claims marked Measured without Field_Log.
- Controllers accepted on demo behavior without Electronics trust path.
- Weaponization-capable configuration described as in-scope.
- Spec Gate advance without body evidence.
- Open Unknowns count in File State disagreeing with sidecar.
- Any floor RF-1 to RF-12 weakened or dropped without ratification and a Resolution Log entry.
- Powered motion or people-present operation while its RB entry is still Blocking.

---

## Resolution Log

- 2026-10-10: **v0 Proposed stub filed.** Human-directed first iteration for an Operations-layer robotics domain: safety advisory, hard floors RF-1–RF-8, functional blocks A–J with Placeholder thresholds, interfaces to Energy/Electronics/Automotive/Gates/Admin, eight non-blocking Unknowns (RB-001–RB-008). No physical work claimed; no Spec Gate opens; unsupervised human-shared operation and AGI/embodiment hype explicitly out of scope. Registered 2026-10-10 in Routing.md, Ops_Scope_Map.md, and Discovery.md.
- 2026-10-10: **Safety review pass (human-directed).** Added floors RF-9 to RF-12 (support loads before power removal, verify discharge, function-test the safety channel and require deliberate restart after E-stop, hydraulic/laser/lithium hazards) and pointers from blocks D and G; RB-002, RB-003 and RB-007 changed to scoped Blocking. Floors only; no procedure or number added. All new items are Proposed/Placeholder.
- 2026-10-10: The three Blocking items are indexed in `Unknowns.md` v5.59 (Active Index cluster, Dependency Clusters block, Critical Watch). Index entries only; no change to the sidecar entries' substance.
