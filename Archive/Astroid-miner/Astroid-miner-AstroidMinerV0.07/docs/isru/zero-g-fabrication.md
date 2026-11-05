Zero-G Fabrication

Purpose & Scope

This document defines conceptual and early-stage engineering approaches for manufacturing in microgravity (≈10⁻³–10⁻⁶ g) within the Leviathan self-replicating asteroid-mining architecture.

Fabrication is the hardest autonomy bottleneck: most terrestrial manufacturing implicitly relies on gravity for settling, containment, separation, and degassing. In zero-g:

Molten metals form spheres

Powders drift and contaminate

Bubbles do not rise

Small disturbances scatter material


The objective is not Earth-equivalent manufacturing, but robust, scalable, gravity-independent fabrication using asteroid-derived metals, silicates, and volatiles.

Priority outputs:

Structural wire, rods, tubes

Coils and conductors

Ceramic and SiC components

Weldable feedstock for higher-order assembly



---

1. Core Zero-G Fabrication Constraints

Material Behavior

Liquids: surface tension dominates → droplets, adhesion

Powders: float freely → dust clouds, sensor fouling

Gases: remain trapped → poor degassing, porosity


Containment & Shape Control

No natural settling or pressing

Artificial forces required: centrifugal, electromagnetic, pressure

Cross-contamination risk between metals, silicates, volatiles


Thermal Management

Heat rejection only by radiation or forced convection

Slow cooling without active quenching

High thermal cycling stress on tooling


Precision & Stability

Vibrations propagate easily in micro-g

Mining, spin systems, and propulsion must be isolated

Energy-intensive processes compete with limited power budgets



---

2. Foundational Design Principles

1. Containment precedes shaping
Material must be enclosed or field-controlled before melting or cutting.


2. Artificial gravity beats force application
Centrifugal acceleration replaces presses, molds, and gravity settling.


3. Field-based heating over contact heating
Induction and electromagnetic levitation minimize contamination.


4. Wire-first manufacturing
Continuous wire and filament production is the most flexible feedstock.


5. Welding is the primary manufacturing step
Complex geometry emerges from assembly, not casting.




---

3. Primary Fabrication Techniques

Technique	Role	Zero-G Mechanism	Strengths	Limitations	Leviathan Fit

Centrifugal Foundry / Spinning Chamber	Melting, casting, separation	Rotation (1–10 rpm) creates 0.1–1 g equivalent	Excellent containment; density separation	Mechanical complexity	Core fabrication “stomach”
Induction Heating + EM Levitation	Melting, purification	Eddy currents heat & levitate conductors	No crucible; high purity	Power-intensive	Dual-use with sorting
Spun Conical Ceramic Extrusion	Wire / filament	Centrifugal pressure extrudes melt	Continuous output	Cooling critical	Primary wire source
Plasma / Magnetic Quenching	Rapid solidification	Confined plasma sheath removes heat	Fast cooling; no contact	Gas & power demand	Preferred quench path
Radiative / Vacuum Cooling	Simple solidification	Radiation + cold sinks	Low complexity	Slow	Early bootstrap only
Laser / Optical Sintering	Ceramics, silicates	Focused laser fuses powder	Precision	Dust management	Secondary / later stage
Electroplating (spinning)	High-purity layers	Centrifugal electrolyte flow	Ultra-pure outputs	Electrolyte sourcing	Reserved for electronics
Welding (primary fabrication)	Assembly & repair	Laser / arc / induction	Highly versatile	Needs wire feedstock	Core fleet role



---

4. Quenching & Solidification Strategy

Solidification is the dominant failure mode for zero-g fabrication.

Preferred approaches:

Plasma-sheath quenching

Magnetically confined low-temperature plasma

Helium or argon convective heat removal

Minimal interaction with molten filament


Inert gas jet cooling

Pulsed argon/helium jets

Simple, scalable, controllable


Centrifugal thinning

Higher spin → thinner wire → faster radiative loss


Shadow / radiator extrusion

Extrude toward cold sinks or asteroid night side




---

5. Purity & Cross-Contamination Control

Selective induction heats metals, not silicates

Centrifugal separation stratifies melts by density

Multi-chamber processing sequence:

1. Melt + gross separation


2. Plasma or laser impurity removal


3. Levitation or electroplating for final purity



Non-useful residues routed to waste ejection systems



---

6. Validation Lineage & Precedents

NASA containerless processing & microgravity ISRU studies

International Space Station electromagnetic levitation & welding experiments

AstroForge & TransAstra concepts: induction vaporization and capture

Zero-g extrusion and welding tests in orbital and parabolic environments


These confirm that zero-g fabrication is difficult but tractable with the right assumptions.


---

7. Testing & Scale-Up Roadmap

1. Ground analogs

Spin rigs, plasma quenching, induction tests



2. Parabolic flights / drop towers

True micro-g extrusion and levitation



3. LEO prototypes

Small centrifugal + induction free-flyers



4. NEA demonstrations

Full collection → fabrication → welding loop





---

Summary

Zero-g fabrication is not Earth manufacturing without gravity — it is a different discipline entirely.

The Leviathan approach accepts this by:

Using spin instead of weight

Fields instead of molds

Wire instead of parts

Welding instead of casting


Once wire can be made reliably in space, everything else becomes assembly.


---

Next Steps

Notebook: zero_g_fabrication_sim.ipynb

Diagram: collection → centrifugal melt → quenched wire → spool → welder

Cross-links:

zero-g-collection-anchoring.md

docs/power/energy-scaling.md

Project map & raw links: 
https://github.com/ksarith/Lazarus-Forge-
[Lazarus Forge Discovery.md](https://raw.githubusercontent.com/ksarith/Lazarus-Forge-/main/Discovery.md)
Project map & raw links: 
https://github.com/ksarith/Astroid-miner
[Astroid-miner Discovery.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/Discovery.md)

