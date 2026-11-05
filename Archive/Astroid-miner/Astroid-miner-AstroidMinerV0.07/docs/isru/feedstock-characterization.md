# Feedstock Characterization & Materials Valuation Pipeline

Astroid-miner incorporates continuous and staged feedstock analysis to characterize raw materials prior to, during, and after processing. The goal is to maximize material value, optimize refining pathways, and provide early identification of commercially viable outputs.

Feedstock testing operates as a **decision-support system**, not a single-point gate, enabling adaptive refinement strategies while maintaining production throughput.

---

## Objectives

Feedstock characterization serves to:

- Identify elemental and alloy composition of mined material
- Detect valuable metals suitable for direct sale or minimal processing
- Guide refining, alloying, and thermal treatment strategies
- Correlate source material composition with downstream wire properties
- Build a long-term compositional map of the mined body

---

## Multi-Tier Feedstock Testing Strategy

To balance accuracy, power use, and system complexity, feedstock analysis is divided into tiers.

---

## Tier 1: Inline Spectral Screening (Low Cost, High Coverage)

### Purpose
Rapid, non-destructive identification of bulk elemental trends in incoming material.

### Methods
- Optical emission spectroscopy (OES)
- Laser-induced breakdown spectroscopy (LIBS)
- Broad-band reflectance or plasma spectra

### Capabilities
- Detects major elemental groups (Fe, Ni, Al, Cu, Mg, Si, etc.)
- Flags high-value or unusual compositions early
- Operates continuously with minimal sample prep

### Limitations
- Lower precision for trace elements
- Results are best treated as probabilistic, not definitive

Tier 1 data informs **routing decisions**, not final valuation.

---

## Tier 2: X-Ray Fluorescence (XRF) Composition Analysis

### Purpose
Elemental composition verification with higher accuracy.

### Methods
- Spot or batch XRF on processed feedstock or ingots
- Optional inline XRF where geometry allows

### Capabilities
- Accurate elemental percentages for metals and alloys
- Identification of sale-grade materials (e.g., Ni-Fe alloys, Cu-rich streams)
- Correlation of composition with resistance and mechanical properties

### Limitations
- Reduced sensitivity to light elements (e.g., H, C)
- Requires calibration and periodic validation

Tier 2 analysis supports **commercial classification** and **process optimization**.

---

## Tier 3: Targeted High-Value Analysis (Selective, Not Continuous)

### Purpose
Deep analysis of materials flagged as unusual or valuable by Tier 1 or Tier 2 systems.

### Methods (Optional / Deferred Capability)
- Mass spectrometry on micro-samples
- Neutron activation analysis (if infrastructure permits)
- Detailed crystallographic analysis (XRD-style methods)

### Capabilities
- Trace element detection
- Phase and compound identification
- Validation of rare or anomalous material streams

Tier 3 testing is applied sparingly to conserve energy and system wear.

---

## Integration With Production Decisions

Feedstock characterization directly informs:

- Refinement intensity (minimal processing vs. full separation)
- Alloy routing (structural, conductive, experimental)
- Wire production parameters
- Inline resistance anomaly expectations
- Commercial sale or storage prioritization

Materials exceeding defined purity or value thresholds may bypass wire production entirely and be routed to **sale-grade storage**.

---

## Feedback Loop With Inline Wire Testing

Electrical resistance anomalies detected downstream are correlated with upstream feedstock composition data to:

- Identify causative elements or impurity clusters
- Improve predictive models for exotic material formation
- Refine extraction and blending strategies

Over time, Astroid-miner learns which feedstock regions are statistically linked to desirable electrical or structural properties.

---

## Data Logging & Materials Atlas

All feedstock measurements are logged with:

- Spatial origin within the asteroid or source body
- Extraction timestamp
- Processing and thermal history
- Downstream material outcomes

This enables construction of a **materials-property atlas**, improving planning, valuation, and extraction efficiency over long mission durations.

---

## Commercial & Ethical Framing

Feedstock testing is designed to:

- Maximize material utilization
- Avoid speculative over-processing
- Enable transparent valuation of sale-grade materials
- Maintain production stability over anomaly chasing

High-value discoveries are treated as **opportunistic gains**, not operational dependencies.

---

## Deferred Expansion Notes

Future upgrades may include:
- Improved light-element detection (e.g., hydrogen presence)
- Enhanced phase identification for exotic alloys
- Cross-miner data sharing for comparative material learning

These capabilities are intentionally non-critical-path to ensure mission robustness.
