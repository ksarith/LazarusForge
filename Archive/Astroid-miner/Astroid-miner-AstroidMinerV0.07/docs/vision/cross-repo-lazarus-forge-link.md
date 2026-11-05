# Cross-Repository Relationship — Lazarus Forge (Solar Descent)

**Status:** Declared, dormant. Not an active integration.

**Provenance:** Verified directly against the uploaded `LazarusForgeV0-1Alpha12.zip` archive
(`Tests/Solar_Descent.md` and `Discovery.md`), not taken on the word of a secondhand summary.
This entry replaces an earlier draft in this repository that declined to register the claimed
link because the source repository wasn't available for verification at the time.

---

## What is actually declared, verified against source

`LazarusForgeV0/Discovery.md`, under "Cross-Repo Relationship":

> `Astroid-miner` — planned; activates when Leviathan deployment is underway.

`LazarusForgeV0/Tests/Solar_Descent.md`, under "Forward Reference — Asteroid Processing System":

> Solar Descent is the terrestrial validation stage for a space-based solar concentration and
> material processing architecture. Every unknown resolved here reduces risk in the Astroid-miner
> companion system. The relationship is explicit and directional: prove it underground first, then
> translate to vacuum.

> Repository Pointer: `Astroid-miner` companion repository. Activates when Leviathan deployment is
> underway per Discovery.md cross-repo relationship declaration. Solar Descent findings should be
> formally transferred to that repository at activation.

**The key qualifier both source files agree on: this link is explicitly dormant.** It activates at
a future milestone ("Leviathan deployment") that has not occurred. It is not a live technical
dependency, and nothing in this repository should currently be built assuming Solar Descent data
exists or is validated.

## Solar_Descent.md's own status (as audited in its source repository)

At time of verification: `Status: Exploration`, `Body Stability: Volatile`, `Spec Gates: 0/6`,
`Open Unknowns: 8` (including the two most load-bearing for any transfer — flux delivery (SD-UNK-001)
and achievable temperature (SD-UNK-002) — both `Open`, `Critical` priority, `Blocking: Yes`). No
Solar Descent test (SD-TEST-101 through SD-TEST-205) has produced empirical results yet; all
figures in that file are explicitly labeled proposed/unvalidated.

## Declared technology-transfer table (from Solar_Descent.md, reproduced for reference)

| Solar Descent element | Asteroid system equivalent (as declared in source) |
|---|---|
| SD-001 fiber optic downlink | Space-based fiber or mirror array routing solar flux to processing vessel |
| Underground chamber (sealed, inert atmosphere) | Asteroid processing vessel (vacuum) |
| Staged thermal cascade by temperature grade | Staged volatile extraction from asteroid body under solar heating |
| Stirling conversion (large thermal differential) | Stirling or equivalent, with 2.7K space background as cold sink |
| Spherical modular chamber geometry | Self-contained processing vessel, separable panel expansion |
| Vacuum pump integration (LW-001 synergy) | Vacuum capture of volatiles at staged temperatures |

Source also explicitly flags SD-001a (molten tin optical termination) as possibly more viable in
vacuum than underground — vacuum eliminates the oxidation problem that complicates it terrestrially.

## What this means for Astroid Miner today

- **Nothing is actionable yet.** The source file itself says findings "should be formally
  transferred... at activation" — activation hasn't happened.
- This repository's own `docs/terraforming/`, `docs/isru/`, and
  `docs/power/` concept documents (including `solar-concentrator-mirror-arrays.md` and
  `liquid-metal-rotating-mirrors.md`, V0.04) already independently cover similar territory
  (solar concentration, staged volatile capture, liquid-metal optics) without depending on this
  link. No content was changed in those files as a result of this verification.
- This entry exists so that if/when Leviathan deployment activates the link, a future
  audit knows where to look and what to check for updates, rather than reinventing the connection
  or accepting a future claim about it without re-verifying against the source repository at that
  time, the same way this entry was produced.

## What was deliberately not done

- No claims from `Solar_Descent.md`'s unvalidated ASM-* assumptions or projected temperature
  ranges were imported into this repository's own parameter files. Those remain that file's own
  UNVALIDATED, Low/Very-Low-confidence assumptions, not Astroid Miner data.
- No existing Astroid Miner document was rewritten to assume this link is live.
