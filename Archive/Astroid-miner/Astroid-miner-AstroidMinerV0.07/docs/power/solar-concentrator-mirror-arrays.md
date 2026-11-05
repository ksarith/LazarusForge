# Solar Concentration Mirror Arrays

**Status:** Conceptual / technology-transfer candidate only
No design commitment, mass budget, or integration with any swarm subsystem exists yet.

**Provenance note:** This document summarizes secondhand technical analysis supplied by an external
collaborating model (not independently verified against primary literature by this repository's
audit process). Treat all figures below as reported claims, not validated engineering data, until
independently sourced.

---

## Purpose

Candidate technology for concentrating solar flux for high-temperature asteroid/regolith material
processing (staged volatile extraction, sintering, melting). Flagged as a technology-transfer
candidate from a companion terrestrial project ("Solar Descent"), which is out of scope for this
repository and not independently verified here.

## Main architectures (reported)

| Type | Focus | Typical concentration | Tracking | Space notes |
|------|-------|----------------------|----------|-------------|
| Parabolic dish | Point | 500–3000+ suns | Dual-axis | Highest optical efficiency; precise pointing required |
| Heliostat field + central receiver | Point (tower) | 500–3000 suns | Dual-axis per mirror | Scalable; secondary concentrators common |
| Parabolic trough | Line | 30–100 suns | Single-axis | Less relevant for extreme T |
| Linear Fresnel | Line | 10–50 suns | Single-axis | Mass/pointing advantages in some space concepts |
| Fresnel lens / micro-concentrator | Point or line | 10–100+ suns | Dual or none | Lightweight; space CPV heritage cited |
| Inflatable / thin-film membrane | Point | Variable | Dual-axis | Attractive for asteroid/spacecraft; shape control is the hard problem |

Theoretical limit: cannot exceed solar surface temperature (~5800 K) with passive concentration.
Practical high-end target: 1000–3000 K for materials processing.

## Space / asteroid relevance (reported use cases)

- Optical mining: lightweight concentrators focus sunlight on asteroid surface or contained
  feedstock to drive sublimation, outgassing, spalling, melting.
- Lunar articulating mirror arrays for regolith sintering/melting (>1000 suns, cited as analogue).
- Space factory concepts: primary + secondary mirrors delivering MW-class thermal power into a
  containment vessel, staged temperature bands for sequential volatile release.
- Secondary (non-imaging) concentrators to raise flux density and tolerate primary pointing error.

**Vacuum advantages (reported):** no atmospheric scattering/absorption, no mirror/molten-metal
oxidation, no need for pumps in staged volatile capture (ambient vacuum), 2.7 K background improves
heat-engine ΔT.

**Vacuum/space challenges (reported):** thermal cycling/distortion, radiation darkening of coatings,
micrometeoroid damage, adhesive/film outgassing, pointing/shape control of large lightweight optics,
heat rejection limited to radiation.

## Materials & coatings (reported)

- Silvered glass / protected silver on steel for secondaries.
- Aluminum, silver, or dielectric mirrors on thin films/membranes for primaries.
- Zerodur or low-CTE substrates for figure-critical applications.
- Liquid-metal mirrors or actively-cooled heat stops for extreme flux.

## Open questions for Astroid Miner (if this pathway is pursued)

1. Mass-specific concentration (kg optics per kW thermal delivered at target).
2. Optical survivability/lifetime under vacuum + radiation + dust.
3. Rigid dish vs. heliostat facets vs. inflatable membrane for primary concentration.
4. Beam termination: direct on regolith/asteroid, into a vessel, or via secondary optic /
   liquid-metal interface.

None of these are answered here. This document exists to record the concept and its source, not to
propose a design.
