# Non-Contact Handling of Conductive Non-Ferrous Material

**Status:** EXPLORATORY note. Literature-grounded, no design numbers, no model.
**Registry:** CONCEPT | EXPLORATORY | UNVALIDATED | N/A | UNPROVENANCED

## Why this matters

`zero-g-collection-anchoring.md` already lists eddy-current capture and sorting for metallic bodies, and `zero-g-fabrication.md` already lists induction heating with electromagnetic (EM) levitation. Two related questions are not covered:

1. Can a conductive **non-ferrous** piece be *attracted* (not just repelled) by an AC electromagnet, and is that useful for gentle handling in zero-g?
2. Once a melt is levitated, how is it **moved from furnace to casting site** without contact?

Both rest on the same physics (AC-induced eddy currents in a conductor), one in the solid state and one in the molten state, so they are kept in one note.

**Provenance:** The initial framing came from an AI-assistant discussion (Grok). Claims were then checked against the sources listed at the end. Claims that could not be checked are left out, not carried over.

**Evidence labels used below:**
`[SOURCED]` supported by a listed source · `[INFERENCE]` reasoning from the sources · `[PROPOSAL]` suggested work · `[OPEN]` unresolved

---

## 1. Attraction of non-ferrous conductors (the "Master Magnet")

### What is documented
- `[SOURCED]` Leonard R. Crow's write-up on electromagnets for attracting non-ferrous metals reports a first attracting magnet in 1940 and a much improved design in 1947. It describes attraction of copper, aluminum and silver, and of any metal of fair or good conductivity. The scan also indicates the magnet can be used to attract iron. (S1)
- `[SOURCED]` The design is an AC-driven electromagnet with shorted copper washers or a conductive ring fixed at the pole face. (S1, S3)
- `[SOURCED]` A 2024 Hackaday write-up of a modern build (a copper ring embedded in one end of a steel core, AC coil) describes the pull on copper and aluminum as weak, and compares it to a shaded-pole motor. (S3)
- `[SOURCED]` A hobbyist account of a separate variant describes two concentric coils fed 90° out of phase through a capacitor bank. This is anecdotal and shows that more than one drive scheme exists. (S5)

### Mechanism (commonly given)
- `[SOURCED, forum-level]` A loose conductor on an AC magnet face is repelled (Lenz's law). This repulsion is the basis of eddy-current sorting. Washers fixed to the face carry induced currents in the same sense as the loose piece, so they attract it. (S4)
- Crow's own explanation is in the primary scan (S1) and should be preferred over the forum paraphrase if this note is revised.

### Limits
- `[SOURCED]` The pull is weak (S3).
- `[INFERENCE]` Force should fall quickly with distance and with particle size. This note does not quantify it.
- `[INFERENCE]` In vacuum, coil heat can only leave by radiation, so duty-cycling matters. AC drive also adds electromagnetic interference (EMI) in a dense swarm.
- `[INFERENCE]` Zero-g removes the need to fight weight, but residual accelerations (about 10⁻³ to 10⁻⁶ g, per `zero-g-fabrication.md`) and adhesion or dust forces still need a force budget before "weak is enough" can be claimed.

### Fit with Astroid-miner
- `[INFERENCE]` **Plausible:** gentle pickup, positioning and soft-docking of flat or bulk conductive product (sheet, plate, stock) and conductive fixtures, with little residual magnetism.
- `[INFERENCE]` **Not supported:** sorting loose regolith grains. Repulsion-based eddy-current separation is the established sorting method on Earth, and an attraction head would be weak on small irregular grains. A dual-mode sorting head would be speculation.
- `[OPEN]` Whether any handling task in the current architecture needs attraction at all, as opposed to repulsion or mechanical capture.

---

## 2. Furnace-to-casting transfer of a levitated melt

### What is known
- `[SOURCED]` Eddy currents induced in a conductive sample by a time-varying field both heat it and, through Lorentz forces, position it. Containerless EM levitation melting is established, including the ISS-EML facility on the International Space Station. (S6)
- `[SOURCED]` Positioning and heating are coupled in levitators: the heating field also stirs the melt, and combined AC and DC fields have been studied to stabilize levitated melts. (S7)

### What is open
- `[SOURCED]` Stewart et al. (arXiv:2511.02761, Nov 2025) describe controlled movement of molten metal from an induction furnace to a casting process as an unsolved step in microgravity. Their demonstration is closed-loop position control of semi-buoyant aluminum spheres in a lab, which is a preliminary step and not a molten transfer. (S2)
- `[INFERENCE]` Their setting is orbital debris recycling. Relevance to asteroid mining is by analogy.

### Gap in this repo
- `[INFERENCE]` A text search of the repo found EM levitation melting mentioned, but no treatment of how a levitated melt is moved to a mold or deposition site.
- `[INFERENCE]` The baseline fabrication path in `zero-g-fabrication.md` is collection → centrifugal melt → quenched wire → spool → welder. EM transfer would be an alternative or complement for a containerless route, not a requirement of the baseline.

### Modeling targets `[PROPOSAL]`
- Field strength, frequency and gradient needed to hold and translate a given melt mass against residual acceleration.
- Stability and fragmentation limits during acceleration.
- Inductive power versus radiative and evaporative losses (matters for high-vapor-pressure metals).
- Coil sequencing for a furnace-to-mold move.

### Validation path `[PROPOSAL]`
Start from published ISS-EML, drop-tower and parabolic-flight data. For ground work, follow the semi-buoyant solid-sphere approach in S2 before any molten work.

---

## 3. What this note does not claim

- No force, power or frequency numbers for either topic.
- Traveling-wave regolith excavators and eddy-current relative motion near spacecraft were raised in the source discussion and are **not verified**, so they are not included.
- The Master Magnet is not asserted to outperform existing magnetic handling concepts in the repo.

## 4. Open questions

1. Which handling steps in the current pipeline, if any, benefit from attraction?
2. Is a containerless route worth adding next to centrifugal melt and quench?
3. What is the smallest solid-sample experiment that would test the force-versus-distance behavior of S1/S3-style heads?

---

## Sources and verification status

| ID | Source | Status |
|----|--------|--------|
| S1 | L. R. Crow, *Electromagnets for Attracting Copper, Aluminum and Other Non-Ferrous Metals* (scanned copy on Scribd, https://www.scribd.com/document/376495229/Non-Ferrous-Magnet-pdf; date appears as 1951 on the scan) | Read via search excerpt only; full text not reviewed |
| S2 | Stewart et al., *Non-Contact Manipulation of Induced Magnetic Dipoles*, arXiv:2511.02761 (4 Nov 2025) | Excerpts reviewed; not read in full |
| S3 | Hackaday, "Sort Of Electromagnet Attracts Copper, Aluminum", 27 Mar 2024 (https://hackaday.com/2024/03/27/sort-of-electromagnet-attracts-copper-aluminum) | Excerpt reviewed. A commenter there recalls a 1956 Popular Electronics "Master Magnet" article; that is unverified and not relied on |
| S4 | Physics Forums and Mike Holt forum threads on attracting non-ferrous metals | Forum-level; mechanism explanation only |
| S5 | microship.com, "Master Magnet – 1963 Science Fair" | Anecdotal |
| S6 | npj Microgravity, doi:10.1038/s41526-023-00281-4 (ISS-EML context) | Excerpt reviewed; title not captured |
| S7 | JOM article, doi:10.1007/s11837-012-0417-y (modeling of levitated melts, AC/DC fields) | Excerpt reviewed; title not captured |

---

## Next Steps

- Open `[OPEN]` items above against the existing handling and fabrication docs.
- If pursued, add a small force-versus-distance and power-budget model under `src/astroid_miner/` with parameters declared in `parameters/`, and update the registry entry accordingly.

Cross-links:

- `zero-g-collection-anchoring.md`
- `zero-g-fabrication.md`
- `magnetic-drive.md`

Project map & raw links:
https://github.com/ksarith/Lazarus-Forge-
[Lazarus Forge Discovery.md](https://raw.githubusercontent.com/ksarith/Lazarus-Forge-/main/Discovery.md)
Project map & raw links:
https://github.com/ksarith/Astroid-miner
[Astroid-miner Discovery.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/Discovery.md)
