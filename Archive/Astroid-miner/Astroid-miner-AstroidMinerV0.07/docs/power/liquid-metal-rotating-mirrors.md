# Liquid Metal Rotating / Shaped Mirrors

**Status:** Conceptual / technology-transfer candidate only
No design commitment, mass budget, or integration with any swarm subsystem exists yet.

**Provenance note:** This document summarizes secondhand technical analysis supplied by an external
collaborating model (not independently verified against primary literature by this repository's
audit process). Treat all figures below as reported claims, not validated engineering data, until
independently sourced.

---

## Core principle (reported)

A liquid metal spun at constant angular velocity around a vertical axis forms a paraboloid under
gravity/centrifugal balance, usable as an optical reflector without grinding or polishing. Focal
length f = g / (2ω²) — faster spin gives shorter focal length. Basis of terrestrial liquid-mirror
telescopes (LMTs).

## Demonstrated systems (reported)

| System | Diameter | Metal | Notes |
|--------|----------|-------|-------|
| Large Zenith Telescope (Canada) | 6 m | Mercury | Decommissioned 2016 |
| International Liquid Mirror Telescope (India) | 4 m | Mercury | Reported operational |
| NASA Orbital Debris Observatory | 3 m | Mercury | Space-junk tracking |
| Lab/prototype work | 0.5–3.7 m | Mercury, gallium alloys | Diffraction-limited performance reported under controlled conditions |

## Candidate metals (reported)

| Metal / alloy | Melting point | Notes |
|---|---|---|
| Mercury | −39 °C | High reflectivity (~75–80%), long heritage; toxic, vapor pressure issues |
| Gallium | ~30 °C | Lower toxicity; oxidizes; lower reflectivity (~70% solidified) |
| Galinstan (Ga-In-Sn) | ~−19 °C | Liquid at room temp; oxidation management needed |
| Tin | 232 °C | Cheap, high boiling point; must stay molten; oxidation (dross) |
| Ionic liquids + metal film | Variable | Vacuum-stable, low vapor pressure; reflectivity depends on deposited film |

## Key limitations (reported, Earth-based)

1. Zenith-only pointing for classic spinning liquid mirrors.
2. Requires a stable gravitational field for the paraboloid to form.
3. Oxidation/contamination, especially tin and gallium in air.
4. Sensitive to rotation-rate jitter and vibration.

## Approaches to the pointing limitation (reported, research-stage)

- Magnetic actuation of ferrofluids/magnetic liquid metals for shape control independent of pure
  gravity/centrifugal balance.
- Electrowetting / electrocapillarity — voltage-controlled surface shape.
- Hybrid solid+liquid or wicking structures to stabilize the liquid film.
- Space/micro-g versions: spacecraft spin as artificial gravity, or surface-tension/magnetic shaping.

**Explicitly flagged as research/prototype stage** — no large flight-ready system reported to exist.

## Relevance to Astroid Miner (if this pathway is pursued)

- Vacuum eliminates oxidation of tin/gallium mirrors.
- Continuous solar availability removes terrestrial day/night thermal cycling.
- Low-mass, self-forming optics attractive where launch mass / in-situ fabrication matters.
- Magnetically-shaped or spin-shaped liquid-metal mirrors could avoid polishing large rigid mirrors
  in situ — unverified, no flight heritage reported.

## Status assessment

- Reported as mature for zenith-only terrestrial astronomy.
- Reported as experimental/research-stage for off-zenith or space use.
- No quantitative claims here should be treated as validated; this is a CONCEPT-tier placeholder for
  a possible future ENGINEERING-tier writeup, contingent on independent sourcing.
