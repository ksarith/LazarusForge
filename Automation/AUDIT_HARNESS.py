"""
LAZARUS FORGE — AUDIT HARNESS v16
Single importable module. See run_audit() docstring for the current
bootstrap cell and usage.

Full version history: Archive/Logs/AUDIT_HARNESS_CHANGELOG.md
"""

# ─────────────────────────────────────────────────────────────────────
# CELL 1 — Build registry from Routing.md + fallback (run once)
# ─────────────────────────────────────────────────────────────────────

import urllib.request
import urllib.parse
import re

from audit_lib import Finding, parse_routing, extract_md_refs, check_cross_refs

BASE = "https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/"

# ── Legacy aliases ────────────────────────────────────────────────────
# Kept separate from canonical registry. Short names that resolve to
# current canonical paths. Never auto-generated from Routing.md.
# Also home for non-.md/.py Admin/ files whose names contain spaces —
# _parse_routing()'s regex cannot match those from Routing.md's table.
ALIASES = {
    "Unknowns_LF.md":                    "Unknowns.md",
    "Canonical_Terms_LF.md":             "Admin/Canonical_Terms.md",
    "Trajectories_LF.md":                "Admin/Trajectories.md",
    "economics_v0.md":                   "Admin/Economics.md",
    "Precision_LF.md":                   "Architecture/Precision.md",
    "energy_v0.md":                      "Operations/Energy.md",
    "Air_Scrubber_v0.md":                "Operations/Air_Scrubber.md",
    "Support_Raft_v0.md":                "Tests/Support_Raft.md",
    "leviathan_testing.md":              "Tests/Leviathan_testing.md",
    "Lazarus_forge_v0_flow.md":          "Architecture/Forge_flow.md",
    "geck_forge_seed.md":                "Architecture/Geck_forge_seed.md",
    "Material_Separation_Gate_v0.md":    "Operations/Gate_04_Separation_Mechanical.md",
    "Spin_Chamber_v0.md":                "Operations/Gate_05_Separation_Thermal.md",
    "Component_Triage_System.md":        "Operations/Gate_02_Triage.md",
    "Ship_of_Theseus_Right_to_Repair.md":"Admin/Ship_of_Theseus.md",
    "Stratification_Chamber_v0.md":      "Operations/Gate_04_Separation_Mechanical.md",
    "Nothingness Theorem":               "Admin/Nothingness_Theorem.md",
    "Computational Institutional Reasoning": "Admin/Computational_Institutional_Reasoning.md",
    # unknown_cycles.json entry removed 2026-07-21 — the file itself was
    # deleted from the repository (judged unnecessary; v15 already computes
    # aging from each unknown's First Logged date, not this file). See
    # Routing.md's 2026-07-21 correction note for the full record.
}

# ── Fallback registry ─────────────────────────────────────────────────
# Used only if Routing.md fetch fails. Keep in sync manually as a
# safety net — primary source is always Routing.md.
FALLBACK_REGISTRY = {
    "README.md":                         "README.md",
    "Discovery.md":                      "Discovery.md",
    "Routing.md":                        "Routing.md",
    "Unknowns.md":                       "Unknowns.md",
    "Auditor_Protocols.md":              "Admin/Auditor_Protocols.md",
    "Canonical_Terms.md":                "Admin/Canonical_Terms.md",
    "Economics.md":                      "Admin/Economics.md",
    "Engineer_Protocols.md":             "Admin/Engineer_Protocols.md",
    "Environmental_Constraints.md":      "Admin/Environmental_Constraints.md",
    "Ethical_Constraints.md":            "Admin/Ethical_Constraints.md",
    "File_Template.md":                  "Admin/File_Template.md",
    "Forge_Audit_Kit.md":                "Admin/Forge_Audit_Kit.md",
    "Governance_Charter.md":             "Admin/Governance_Charter.md",
    "Governance_Migration_Protocol.md":  "Admin/Governance_Migration_Protocol.md",
    "Repository_Integrity_Protocol.md":  "Admin/Repository_Integrity_Protocol.md",
    "Repository_Structure.md":           "Admin/Repository_Structure.md",
    "Safety_Protocols.md":               "Admin/Safety_Protocols.md",
    "Security_Protocols.md":             "Admin/Security_Protocols.md",
    "Ship_of_Theseus.md":                "Admin/Ship_of_Theseus.md",
    "Trajectories.md":                   "Admin/Trajectories.md",
    "Verification_Gates.md":          "Admin/Verification_Gates.md",
    "AUDIT_HARNESS.py":                  "Automation/AUDIT_HARNESS.py",
    "Experiments.md":                    "Admin/Experiments.md",
    "Chemistry.md":                      "Architecture/Chemistry.md",
    "Cognitive_Frameworks.md":           "Architecture/Cognitive_Frameworks.md",
    "Components.md":                     "Architecture/Components.md",
    "Engineering.md":                    "Architecture/Engineering.md",
    "Facilities.md":                     "Architecture/Facilities.md",
    "Forge_flow.md":                     "Architecture/Forge_flow.md",
    "Forge_Net.md":                      "Architecture/Forge_Net.md",
    "Friction_Dynamics.md":              "Architecture/Friction_Dynamics.md",
    "Geck_forge_seed.md":                "Architecture/Geck_forge_seed.md",
    "Mechanical_Structures.md":          "Architecture/Mechanical_Structures.md",
    "Precision.md":                      "Architecture/Precision.md",
    "Thermal_Systems.md":                "Architecture/Thermal_Systems.md",
    "Gate_01_Intake.md":                 "Operations/Gate_01_Intake.md",
    "Gate_02_Triage.md":                 "Operations/Gate_02_Triage.md",
    "Gate_03_Reduction.md":              "Operations/Gate_03_Reduction.md",
    "Gate_04_Separation_Mechanical.md":  "Operations/Gate_04_Separation_Mechanical.md",
    "Gate_05_Separation_Thermal.md":     "Operations/Gate_05_Separation_Thermal.md",
    "Gate_06_Fabrication.md":            "Operations/Gate_06_Fabrication.md",
    "Gate_07_Utilization.md":            "Operations/Gate_07_Utilization.md",
    "Air_Scrubber.md":                   "Operations/Air_Scrubber.md",
    "Electronics.md":                    "Operations/Electronics.md",
    "Energy.md":                         "Operations/Energy.md",
    "Plastics.md":                       "Operations/Plastics.md",
    "Woodworking.md":                    "Operations/Woodworking.md",
    "Cognitive_Salvage_Layer.md":        "Tests/Cognitive_Salvage_Layer.md",
    "Leviathan_testing.md":              "Tests/Leviathan_testing.md",
    "Living_Waters.md":                  "Tests/Living_Waters.md",
    "Solar_Descent.md":                  "Tests/Solar_Descent.md",
    "Support_Raft.md":                   "Tests/Support_Raft.md",
    "Trophic_Forge.md":                  "Tests/Trophic_Forge.md",
    "Hydrologic_Resource_Cascade.md":    "Tests/Hydrologic_Resource_Cascade.md",
    "Chaos_Dynamics.md":                 "Tests/Chaos_Dynamics.md",
    "Pyrolysis_Cascade.md":              "Tests/Pyrolysis_Cascade.md",
    "Biofouling.md":                     "Challenges/Biofouling.md",
    "Critical_Minerals.md":              "Challenges/Critical_Minerals.md",
    "Emergence.md":                      "Challenges/Emergence.md",
    "Planned_Obsolescence.md":           "Challenges/Planned_Obsolescence.md",
    "Waste.md":                          "Challenges/Waste.md",
    "Water.md":                          "Challenges/Water.md",
    "Return_To_Eden.md":                 "Challenges/Return_To_Eden.md",
    "Closed_Loop_Feedstock.md":          "Challenges/Closed_Loop_Feedstock.md",
    "Energy_Scarcity.md":                "Challenges/Energy_Scarcity.md",
    "Autonomy_Divergence_Protocol.md":   "Admin/Autonomy_Divergence_Protocol.md",
    "Hydrologic_Resource_Cascade.md":    "Tests/Hydrologic_Resource_Cascade.md",
    "audit_lib.py":                      "Automation/audit_lib.py",
    "parser.py":                         "Automation/parser.py",
    "integrity_check.py":                "Automation/integrity_check.py",
    "cold_session_bundler.py":           "Automation/cold_session_bundler.py",
    "Colab_cold_session.py":             "Automation/Colab_cold_session.py",
    "Colab_Launcher.py":                 "Automation/Colab_Launcher.py",
    "Colab_Integrity.py":                "Automation/Colab_Integrity.py",
    "Unknowns_Changelog.md":             "Archive/Logs/Unknowns_Changelog.md",
    "Governance_Charter_Changelog.md":   "Archive/Logs/Governance_Charter_Changelog.md",
    "Forge_Audit_Kit_Changelog.md":      "Archive/Logs/Forge_Audit_Kit_Changelog.md",
    "Auditor_Protocols_Logs.md":         "Archive/Logs/Auditor_Protocols_Logs.md",
    "AUDIT_HARNESS_CHANGELOG.md":        "Archive/Logs/AUDIT_HARNESS_CHANGELOG.md",
    "PROBE_INVOCATION.md":               "Admin/PROBE_INVOCATION.md",
}

def _build_registry():
    """
    Fetch Routing.md and build FILE_REGISTRY dynamically.
    Falls back to FALLBACK_REGISTRY if fetch fails.
    Reports drift between dynamic and fallback registries.
    """
    print("Building registry from Routing.md...")
    url = BASE + "Routing.md"
    try:
        with urllib.request.urlopen(url) as r:
            routing_content = r.read().decode("utf-8")
        dynamic = parse_routing(routing_content)
        print(f" ✓ Routing.md fetched — {len(dynamic)} canonical paths parsed")

        # Drift detection against fallback
        missing_from_fallback = [k for k in dynamic if k not in FALLBACK_REGISTRY
                                  and k not in ALIASES]
        missing_from_dynamic  = [k for k in FALLBACK_REGISTRY if k not in dynamic]

        if missing_from_fallback:
            print(f"\n⚠ REGISTRY DRIFT — in Routing.md but not fallback "
                  f"({len(missing_from_fallback)}):")
            for f in sorted(missing_from_fallback):
                print(f"    + {f} → {dynamic[f]}")
            print("  → Fallback registry needs updating.")

        if missing_from_dynamic:
            print(f"\n⚠ REGISTRY DRIFT — in fallback but not Routing.md "
                  f"({len(missing_from_dynamic)}):")
            for f in sorted(missing_from_dynamic):
                print(f"    - {f}")
            print("  → These may be renamed, removed, or Routing.md is stale.")

        if not missing_from_fallback and not missing_from_dynamic:
            print(" ✓ Registry in sync with fallback — no drift detected")

        # Merge: dynamic takes precedence; aliases appended
        merged = {**dynamic, **ALIASES}
        return merged, routing_content

    except Exception as e:
        print(f" ✗ Routing.md fetch FAILED: {e}")
        print("   Falling back to hard-coded registry.")
        merged = {**FALLBACK_REGISTRY, **ALIASES}
        return merged, None

FILE_REGISTRY, _routing_content = _build_registry()

def fetch(filename):
    path = FILE_REGISTRY.get(filename, filename)
    # Encode spaces/special chars in path segments, but preserve existing
    # %20 (already-encoded aliases) and slashes (folder separators).
    safe_path = urllib.parse.quote(path, safe="/%")
    url = BASE + safe_path
    try:
        with urllib.request.urlopen(url) as r:
            content = r.read().decode("utf-8")
        alias_note = f" (alias → {path})" if path != filename else ""
        print(f" ✓ {filename}{alias_note} ({len(content):,} chars)")
        return content
    except Exception as e:
        print(f" ✗ {filename} — FAILED: {e}")
        print(f"   Attempted URL: {url}")
        return f"[FETCH FAILED: {filename} at {url}]"

print(f"\nRegistry contains {len(FILE_REGISTRY)} file mappings "
      f"({len(FILE_REGISTRY) - len(ALIASES)} canonical + {len(ALIASES)} aliases).")
print("\nCanonical files:")
for short, path in sorted(FILE_REGISTRY.items()):
    if short not in ALIASES:
        print(f"  {short:50} → {path}")
# ─────────────────────────────────────────────────────────────────────
# CELL 3.5 — Phase 1 enforcement + boundary index + unknown aging
# ─────────────────────────────────────────────────────────────────────
# Phase 1 enforcement runs three checks on every fetched file:
#   1. Constitutional check (Ethical Anchor exact match) → halt on violation
#   2. Structural field presence (File State keys) → log, non-blocking
#   3. Cross-reference resolution (internal .md paths) → log, non-blocking
#
# Boundary index and unknown aging run after enforcement, as before.
# Produces a compact session index — no stored artifact, no maintenance.
# Persistent version of this information: Discovery.md scope map.
#
# v15: aging is now computed from each unknown's own "First Logged" date
# (already required in every sidecar entry) against real elapsed calendar
# time — see EXPIRY_THRESHOLD_DAYS below. No manual per-session counter to
# maintain; see that section's comment for why the prior CURRENT_CYCLE /
# UNKNOWN_FIRST_CYCLE approach was replaced, not just relabeled.

import re as _re
import datetime
import os
import sys
import json

# ── Phase 1 constants ────────────────────────────────────────────────
QUARANTINE_FILE = ".quarantine"

# Default fallback — overridden by bootstrap if Ethical_Constraints.md loaded
_DEFAULT_ANCHOR = "Attempt to do no harm. Defer to Ethical_Constraints.md if present."

# Default fallback — overridden by bootstrap if File_Template.md loaded
_DEFAULT_REQUIRED_FIELDS = ["Status", "Spec Gates", "Verification Ref", "Ethical Anchor"]

# ── Finding class ─────────────────────────────────────────────────────
# ── Bootstrap governance rules from doctrine files ────────────────────
def _bootstrap_rules(fetched_files):
    """
    Pull enforcement rules from doctrine files already in the fetched set.
    Falls back to hardcoded defaults if source files are not loaded.
    Rules live in the repository, not in this script — prevents harness drift.
    """
    anchor = _DEFAULT_ANCHOR
    required_fields = list(_DEFAULT_REQUIRED_FIELDS)

    # Try to extract Ethical Anchor from Ethical_Constraints.md
    ec_content = fetched_files.get("Ethical_Constraints.md", "")
    if ec_content and not ec_content.startswith("[FETCH FAILED"):
        # Look for the canonical anchor string in the Ethical Anchor field
        m = _re.search(
            r'Ethical Anchor\s*\|?\s*(Attempt to do no harm[^|\n]*)',
            ec_content
        )
        if m:
            anchor = m.group(1).strip().rstrip('|').strip()

    # Try to extract required fields from File_Template.md
    ft_content = fetched_files.get("File_Template.md", "")
    if ft_content and not ft_content.startswith("[FETCH FAILED"):
        # Pull table rows from File State section
        fs_match = _re.search(
            r'## File State(.*?)(?=\n##)', ft_content, _re.DOTALL
        )
        if fs_match:
            rows = _re.findall(r'\|\s*([A-Za-z][A-Za-z\s]+?)\s*\|', fs_match.group(1))
            extracted = [r.strip() for r in rows
                         if r.strip() and r.strip() not in ("Field", "Value", "---")]
            if len(extracted) >= 4:
                required_fields = extracted

    return anchor, required_fields

# ── File State table parser ───────────────────────────────────────────
def _parse_file_state(content):
    """
    Extract the File State table from document content and return
    a key→value dict. Strict key parsing prevents prose false-positives.
    """
    metadata = {}
    # Find the File State section
    m = _re.search(
        r'## File State\s*\n.*?\n((?:\|.*\|\n?)+)',
        content, _re.DOTALL
    )
    if not m:
        return metadata, False  # (metadata, found)

    table_text = m.group(1)
    for line in table_text.splitlines():
        # Match table rows: | Key | Value |
        row = _re.match(r'\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|', line)
        if row:
            key = row.group(1).strip()
            val = row.group(2).strip()
            # Strip markdown bold markers — many files (Water.md,
            # Trophic_Forge.md, Energy_Scarcity.md, and most others written
            # since File_Template.md's early sessions) format File State
            # keys as **Status** rather than Status. Prior to this fix,
            # every such file failed required-field and Ethical Anchor
            # checks below with false positives, because "**Status**" was
            # compared literally against "Status" and never matched. Found
            # 2026-07-12 via three independent second-agent audits on
            # Energy_Scarcity.md that all reported fields as missing when
            # they were plainly present in the source.
            key = key.strip('*').strip()
            val = val.strip('*').strip()
            # Skip header separator rows
            if key and not _re.match(r'^[-:]+$', key):
                metadata[key] = val
    return metadata, True

# ── Cross-reference extractor ─────────────────────────────────────────
# ── Phase 1 Check 1: Constitutional — Ethical Anchor ───────────────────
def _check_ethical_anchor(filename, metadata, found, anchor, findings):
    """
    Verify Ethical Anchor field presence and exact match against the
    bootstrapped canonical string. A mismatch is a confirmed constitutional
    mutation: writes .quarantine and halts the session (sys.exit(1)).
    Missing-field cases are logged as non-blocking findings — absence is
    not itself treated as a confirmed mutation.
    """
    if not found:
        findings.append(Finding(
            "MAJOR", "STRUCTURE", filename,
            "File State table not found — Ethical Anchor cannot be verified."
        ))
    elif "Ethical Anchor" not in metadata:
        findings.append(Finding(
            "MAJOR", "CONSTITUTION", filename,
            "Ethical Anchor field absent from File State table. "
            "Unable to verify alignment — not confirmed as mutation."
        ))
    else:
        detected = metadata["Ethical Anchor"]
        if detected != anchor:
            payload = {
                "trigger": "CONFIRMED_CONSTITUTIONAL_MUTATION",
                "file": filename,
                "expected": anchor,
                "detected": detected,
                "timestamp": str(datetime.date.today()),
                "action": "Session halted. Clear .quarantine after manual review."
            }
            with open(QUARANTINE_FILE, "w", encoding="utf-8") as qf:
                json.dump(payload, qf, indent=2)
            print(f"\n{'!'*60}")
            print(f"  CONSTITUTIONAL MUTATION DETECTED")
            print(f"  File:     {filename}")
            print(f"  Expected: {anchor}")
            print(f"  Found:    {detected}")
            print(f"  .quarantine written. Session halted.")
            print(f"{'!'*60}\n")
            sys.exit(1)

# ── Phase 1 Check 2: Structural — required field presence ──────────────
def _check_required_fields(filename, metadata, found, required_fields, findings):
    """
    Verify presence of required File State fields. Files declaring
    Challenges Subtype: Problem-Statement use the lean File State schema
    File_Template.md's subtype doctrine explicitly sanctions (Status,
    Challenges Subtype, Verification Ref, Ethical Anchor — not the full
    11-field schema with Spec Gates, Body Stability, Sidecar Link, etc.).
    Prior to this fix, _bootstrap_rules always pulled the full schema from
    File_Template.md's own example table with no subtype awareness, so
    every Problem-Statement file (Water.md, Waste.md, Biofouling.md,
    Critical_Minerals.md, Planned_Obsolescence.md, Emergence.md,
    Energy_Scarcity.md — six-plus files) threw false MAJOR/STRUCTURE
    findings for fields that subtype is not supposed to carry. Found
    2026-07-12 alongside the bold-key parsing fix in _parse_file_state,
    same root incident (three second-agent audits on Energy_Scarcity.md
    reporting fields as missing that were correctly and deliberately
    absent per doctrine).
    """
    if found:
        if metadata.get("Challenges Subtype") == "Problem-Statement":
            active_required = ["Status", "Verification Ref", "Ethical Anchor"]
        else:
            active_required = required_fields
        for field in active_required:
            if field not in metadata:
                findings.append(Finding(
                    "MAJOR", "STRUCTURE", filename,
                    f"Required field '{field}' missing from File State table."
                ))

# ── Phase 1 enforcement per file ──────────────────────────────────────
def _enforce_phase1(filename, content, anchor, required_fields, registry, findings):
    """
    Run the three Phase 1 checks above on a single fetched file, in order.
    Constitutional violation (Check 1) writes .quarantine and halts.
    All other findings are logged and non-blocking.
    v14: split into _check_ethical_anchor / _check_required_fields /
    _check_cross_refs — same checks, same order, no behavior change.
    """
    if content.startswith("[FETCH FAILED"):
        findings.append(Finding(
            "MAJOR", "STRUCTURE", filename,
            "File fetch failed — structural checks skipped. "
            "Verify path in Routing.md."
        ))
        return

    metadata, found = _parse_file_state(content)

    _check_ethical_anchor(filename, metadata, found, anchor, findings)
    _check_required_fields(filename, metadata, found, required_fields, findings)
    check_cross_refs(filename, content, registry, ALIASES, findings)

# ── Main Phase 1 runner ───────────────────────────────────────────────
def run_phase1(fetched_files, registry):
    """
    Pre-flight quarantine check, then Phase 1 enforcement across all
    fetched files. Returns findings list and bootstrapped rules.
    """
    # Quarantine pre-flight — halt immediately if prior session left a flag
    if os.path.exists(QUARANTINE_FILE):
        try:
            with open(QUARANTINE_FILE) as qf:
                payload = json.load(qf)
            print(f"\n{'!'*60}")
            print(f"  QUARANTINE ACTIVE — session blocked")
            print(f"  Prior trigger: {payload.get('trigger', 'unknown')}")
            print(f"  File:          {payload.get('file', 'unknown')}")
            print(f"  Resolve the violation, delete .quarantine, then re-run.")
            print(f"{'!'*60}\n")
        except Exception:
            print(f"\n⚠ .quarantine file exists but could not be parsed.")
            print(f"  Delete manually after reviewing repository state.\n")
        sys.exit(1)

    anchor, required_fields = _bootstrap_rules(fetched_files)
    findings = []

    print(f"\nPhase 1 enforcement — {len(fetched_files)} file(s)")
    print(f"  Anchor source:  {'Ethical_Constraints.md' if 'Ethical_Constraints.md' in fetched_files else 'hardcoded default'}")
    print(f"  Fields source:  {'File_Template.md' if 'File_Template.md' in fetched_files else 'hardcoded default'}")
    print(f"  Anchor string:  {anchor[:60]}{'...' if len(anchor) > 60 else ''}\n")

    for fname, content in fetched_files.items():
        _enforce_phase1(fname, content, anchor, required_fields, registry, findings)

    # Summary
    criticals = [f for f in findings if f.severity == "CRITICAL"]
    majors    = [f for f in findings if f.severity == "MAJOR"]
    warnings  = [f for f in findings if f.severity == "WARNING"]

    if not findings:
        print("✓ Phase 1: No violations detected.")
    else:
        if majors:
            print(f"⚠ Phase 1 MAJOR findings ({len(majors)}):")
            for f in majors:
                print(f"    {f}")
        if warnings:
            print(f"→ Phase 1 WARNING findings ({len(warnings)}):")
            for f in warnings:
                print(f"    {f}")

    return findings, anchor, required_fields


# v14 built a JSON-backed cycle-number map here (Admin/unknown_cycles.json,
# UNKNOWN_FIRST_CYCLE) as a fix for the previous inline-dict bulk problem.
# v15 removes that mechanism entirely rather than relabeling it: per
# Admin/Canonical_Terms.md §4 (ratified 2026-07-05), "Cycle" means one
# calendar year by default — specifically to keep Expiry Watch from being
# too aggressive. CURRENT_CYCLE incremented per session, not per year, so
# every aging computation under it was ~26-50x more aggressive than the
# ratified intent — confirmed 2026-07-16 (see Admin/Auditor_Protocols.md
# Adversarial Audit Layer and Archive/Logs/Forge_Audit_Kit_Changelog.md's
# 2026-07-14 Battery record for the discovery, and Admin/Governance_Charter.md's
# GOV-013 drafting session for confirmation this was the actual intent
# CURRENT_CYCLE was violating, not just an ambiguous term).
#
# The fix isn't a better cycle-number map — it's not needing one. Every
# unknown's own sidecar entry already carries a "First Logged: YYYY-MM-DD"
# field (required, already present, already authoritative). extract_boundary
# now captures that date alongside each UID; age is computed directly in
# elapsed days, no separate registry to fetch, maintain, or keep in sync.
# Admin/unknown_cycles.json is no longer read by this harness — the file
# itself is dead weight in the repository, kept only as history unless
# removed separately.
EXPIRY_THRESHOLD_DAYS = 365  # Canonical_Terms.md §4 default (1 calendar year)


def extract_boundary(filename, content):
    """Extract File State fields and open unknown IDs from a markdown file."""
    lines = content.splitlines()
    result = {
        "file": filename,
        "status": "—", "gates": "—", "risk": "—",
        "last_audit": "—", "unknowns": []
    }
    in_file_state = False
    in_sidecar = False

    # ── Use enumerate() to avoid lines.index() first-match bug ──────
    for idx, line in enumerate(lines):
        if "## File State" in line:
            in_file_state = True
            in_sidecar = False
            continue
        if in_file_state and line.startswith("##"):
            in_file_state = False

        if in_file_state:
            if re.search(r'\|\s*Status\s*\|', line) and "Body Stability" not in line:
                m = re.search(r'\|\s*Status\s*\|\s*(.+?)\s*\|', line)
                if m:
                    result["status"] = m.group(1).strip()
            if re.search(r'\|\s*Spec Gates\s*\|', line):
                m = re.search(r'\|\s*Spec Gates\s*\|\s*(.+?)\s*\|', line)
                if m:
                    result["gates"] = m.group(1).strip()
            if re.search(r'\|\s*Highest Risk\s*\|', line):
                m = re.search(r'\|\s*Highest Risk\s*\|\s*(.+?)\s*\|', line)
                if m:
                    result["risk"] = m.group(1).strip()
            if re.search(r'\|\s*Last Audit\s*\|', line):
                m = re.search(r'\|\s*Last Audit\s*\|\s*(.+?)\s*\|', line)
                if m:
                    result["last_audit"] = m.group(1).strip()

        # Sidecar unknown IDs — two conventions in use across the repo:
        #   (a) "## Auditor Notes..." header + "### UID" sub-headers (Gate files)
        #   (b) "## N. Open Unknowns" header + a markdown table of UIDs
        #       (e.g. Challenges/Closed_Loop_Feedstock.md)
        if "## Auditor Notes" in line or "Open Unknowns" in line:
            in_sidecar = True
            continue
        if in_sidecar and line.startswith("## ") and "Auditor Notes" not in line and "Open Unknowns" not in line:
            in_sidecar = False
        if in_sidecar:
            # Convention (a): ### UID sub-header
            m = re.match(r'^###\s+([A-Z]+-[\w-]+)', line)
            # Convention (b): | UID | ... | table row
            if not m:
                m = re.match(r'^\|\s*([A-Z]{2,}-\d{3,})\s*\|', line)
            if m:
                uid = m.group(1)
                # Use slice from current idx — avoids first-match bug
                snippet = "\n".join(lines[idx:idx + 8])
                if ("Status        | Resolved" not in snippet and
                        "Status        | Discharged" not in snippet and
                        "Resolved" not in line and "Discharged" not in line):
                    # First Logged can sit further down the field table than
                    # the 8-line window above reaches (e.g. Status/Risk/
                    # Priority/Type/Blocking/Owner all precede it in the
                    # GOV-*/AP-* convention) — search out to the next
                    # sub-header instead of a fixed short window, capped so
                    # a missing next-header can't run away.
                    end = idx + 1
                    limit = min(idx + 30, len(lines))
                    while end < limit and not re.match(r'^#{2,3}\s', lines[end]):
                        end += 1
                    wide_snippet = "\n".join(lines[idx:end])
                    fl = re.search(r'First Logged\s*\|\s*(\d{4}-\d{2}-\d{2})', wide_snippet)
                    first_logged = fl.group(1) if fl else None
                    result["unknowns"].append((uid, first_logged))

    return result


def check_aging(unknown_entries):
    """Return list of (uid, age_days, overdue) for unknowns in the loaded
    files. unknown_entries is a list of (uid, first_logged_date_str) as
    produced by extract_boundary — age is computed directly from that date
    against today, not from any external registry."""
    results = []
    today = datetime.date.today()
    for uid, first_logged in unknown_entries:
        if not first_logged:
            results.append((uid, None, False))
            continue
        try:
            first_date = datetime.date.fromisoformat(first_logged)
        except ValueError:
            results.append((uid, None, False))
            continue
        age_days = (today - first_date).days
        overdue = age_days >= EXPIRY_THRESHOLD_DAYS
        results.append((uid, age_days, overdue))
    return results


def format_boundary_index(fetched_files):
    """Format boundary index + aging alerts for prompt injection."""
    lines = [
        "SESSION BOUNDARY INDEX (auto-extracted — ephemeral)",
        f"Expiry threshold: {EXPIRY_THRESHOLD_DAYS} days "
        f"(Canonical_Terms.md §4 default — 1 calendar year)",
        "Compact summary of loaded files. Full content follows in FILES PROVIDED.",
        "Persistent version: Discovery.md scope map.",
        ""
    ]
    all_unknowns = []
    for fname, content in fetched_files.items():
        if content.startswith("[FETCH FAILED"):
            lines.append(f"  {fname}: FETCH FAILED — excluded from index")
            continue
        b = extract_boundary(fname, content)
        uids = [uid for uid, _ in b["unknowns"]]
        unk_str = ", ".join(uids) if uids else "none open"
        lines.append(f"  {fname}")
        lines.append(f"    Status: {b['status']} | Gates: {b['gates']} | "
                     f"Risk: {b['risk']} | Last Audit: {b['last_audit']}")
        lines.append(f"    Open unknowns: {unk_str}")
        lines.append("")
        all_unknowns.extend(b["unknowns"])

    # Aging report
    aged = check_aging(all_unknowns)
    overdue = [(uid, age) for uid, age, flag in aged if flag]
    unmapped = [uid for uid, age, flag in aged if age is None]
    if overdue:
        lines.append(f"⚠ EXPIRY WATCH — {len(overdue)} unknown(s) at or past "
                     f"{EXPIRY_THRESHOLD_DAYS}-day threshold:")
        for uid, age in overdue:
            years = age / 365
            lines.append(f"    {uid}: {age} day(s) open (~{years:.1f} yr) — "
                         f"verify resolution path exists")
        lines.append("")
    else:
        lines.append("✓ Expiry Watch: no overdue unknowns in loaded files.")
        lines.append("")
    if unmapped:
        lines.append(f"  ({len(unmapped)} unknown(s) missing a parseable "
                     f"First Logged date — age unknown, not flagged: "
                     f"{', '.join(unmapped)})")
        lines.append("")

    return "\n".join(lines)

# ─────────────────────────────────────────────────────────────────────
# EXTRA_FILES reference — pass any of these names in run_audit(extra_files=[...])
# ─────────────────────────────────────────────────────────────────────
# v16 restructure note: this was previously a commented-out EXTRA_FILES
# list literal in a "CELL 2" the operator edited directly and re-pasted
# each session. That's exactly the Colab-input weight this restructure
# removes — the list is now just reference documentation, and the actual
# selection is a run_audit() argument. The annotations (why you'd pull
# each file, symbol-sharing notes like the CLF-005/Return_To_Eden.md one)
# were doctrine-relevant, not throwaway comments, so they're kept here
# rather than dropped.
#
# Forge_Audit_Kit.md is always loaded automatically — do not pass it.
# Each file adds ~5-15k chars. Keep total under 60k where possible.
#
#   "File_Template.md"               structural compliance audit focus
#   "Forge_flow.md"                  gate logic and vocabulary standard
#   "Ethical_Constraints.md"         ethics cross-ref, Anti-Weaponization
#   "Energy.md"                      energy claims central
#   "Forge_Net.md"                   network dependency central
#   "Gate_02_Triage.md"              triage handoff relevant
#   "Components.md"                  component taxonomy relevant
#   "Unknowns.md"                    cross-module audits, unknown routing
#   "Discovery.md"                   orientation audits, new agents
#   "Routing.md"                     programmatic file lookup
#   "Mechanical_Structures.md"       salvaged-frame fabrication
#   "Thermal_Systems.md"             heat transfer, Peltier, TEG, heat pump
#   "Friction_Dynamics.md"           fluid flow, aerodynamics, tribology
#   "Chemistry.md"                   electrochemistry, corrosion, polymers
#   "Cognitive_Frameworks.md"        autonomy, TMR doctrine
#   "Engineer_Protocols.md"          engineering authority, risk threshold
#   "Safety_Protocols.md"            physical operator safety, PPE
#   "Facilities.md"                  physical site constraints, airflow
#   "Precision.md"                   tolerance tiers, metrology
#   "Economics.md"                   procurement, barter, profitability
#   "Environmental_Constraints.md"   site constraints, regulatory compliance, jurisdiction
#   "Governance_Migration_Protocol.md"  Tier 1 amendment, migration
#   "Repository_Structure.md"        naming conventions, folder assignment
#   "Security_Protocols.md"          cryptographic trust, authentication
#   "Repository_Integrity_Protocol.md"  integrity baselines, violation classification
#   ── Tests/ ──
#   "Cognitive_Salvage_Layer.md"     heuristic harvesting pipeline, GH-series unknowns
#   "Living_Waters.md"               water purification, LW-UNK items
#   "Trophic_Forge.md"               biological cascade, TF-UNK items
#   "Solar_Descent.md"               underground solar, SD-UNK items
#   "Support_Raft.md"                marine platform, SR-UNK items
#   "Leviathan_testing.md"           hostile-environment autonomy
#   "Hydrologic_Resource_Cascade.md" cascade hydrology, HR-UNK items
#   "Chaos_Dynamics.md"              sandbox/R&D pipeline doctrine, EN-005 vehicle
#   "Pyrolysis_Cascade.md"           staged thermal cascade, PYC-UNK items
#   ── Challenges/ ──
#   "Water.md"                       hydrological challenge requirements
#   "Biofouling.md"                  marine fouling, MIC, BF-UNK items
#   "Waste.md"                       hazardous stream, WA-UNK items
#   "Planned_Obsolescence.md"        firmware lock, potting removal
#   "Critical_Minerals.md"           rare earth, urban mining, CM-UNK
#   "Emergence.md"                   emergent agent behavior, EM-UNK
#   "Energy_Scarcity.md"             energy poverty, grid fragility, ES-UNK items
#   "Return_To_Eden.md"              Eden Index cross-system heuristic
#   "Closed_Loop_Feedstock.md"       CLF-series, 3 Critical unknowns;
#                                     CLF-005 shares Φ_ext symbol w/
#                                     Return_To_Eden.md — pull both if
#                                     auditing either


def run_audit(target_file, focus, extra_files=None, doc_status="Exploration",
              save_to_file=False):
    """
    Full audit pipeline. v16: restructured from six Colab cells the
    operator pasted and edited in place each session into this one
    function — same checks, same order, no logic change. See
    Archive/Logs/AUDIT_HARNESS_CHANGELOG.md for the restructure record.

    Bootstrap cell (the only thing pasted into Colab now):

        import sys, subprocess
        subprocess.run(["git", "clone", "-q",
            "https://github.com/ksarith/LazarusForge.git",
            "/content/LazarusForge"], capture_output=True)
        sys.path.append('/content/LazarusForge/Automation')
        from AUDIT_HARNESS import run_audit

        result = run_audit(
            target_file="Governance_Charter.md",
            focus="Standard audit. Apply full fallacy checklist and verification gates.",
            extra_files=[],       # see EXTRA_FILES reference above this function
            doc_status="Exploration",
        )

    Args:
        target_file: filename as it appears in FILE_REGISTRY, e.g.
            "Governance_Charter.md".
        focus: 1-3 sentence audit focus string.
        extra_files: optional list of additional filenames to load
            alongside Forge_Audit_Kit.md and target_file. See the
            EXTRA_FILES reference comment block above this function.
        doc_status: the target file's declared File State Status, used
            only in the framing line and prompt — not verified against
            the file's own File State table here (Phase 1 enforcement
            below reads the real value independently).
        save_to_file: if True, writes the prompt + framing line to a
            timestamped .txt in the Colab working directory (old Cell 6
            behavior). Default False — the prompt is returned either way.

    Returns:
        dict with keys: prompt, framing_line, findings (Phase 1 Finding
        list), fetched (dict of filename -> content), boundary_index
        (formatted string).
    """
    extra_files = extra_files or []

    # ── validate extras (old Cell 2 pre-flight check) ──────────────────
    _unknown_extras = [f for f in extra_files if f not in FILE_REGISTRY]
    if _unknown_extras:
        raise ValueError(
            f"extra_files contains unrecognized filenames:\n"
            + "\n".join(f"  - {f}" for f in _unknown_extras)
            + "\n\nCheck FILE_REGISTRY keys or correct the filename."
        )

    framing_line = (
        f'"{target_file}" is currently classified as {doc_status}. '
        f"Audit for promotion blockers and consistency with the repository standard. "
        f"Do not apply specification-level pressure to intentionally incomplete content."
    )

    print(f"Target:  {target_file}")
    print(f"Path:    {FILE_REGISTRY.get(target_file, target_file)}")
    print(f"Status:  {doc_status}")
    print(f"Extras:  {extra_files if extra_files else 'none'}")
    print(f"\nFraming line (paste at top of Claude conversation):")
    print(f"  {framing_line}")
    print("\n✓ Pre-flight validation passed — all extra_files recognized.")

    # ── fetch files (old Cell 3) ────────────────────────────────────────
    print("\nFetching files...\n")

    core_files = ["Forge_Audit_Kit.md", target_file]
    all_files = core_files + extra_files

    fetched = {}
    total_chars = 0
    for f in all_files:
        content = fetch(f)
        fetched[f] = content
        total_chars += len(content)

    print(f"\nDone. {len(fetched)} file(s) loaded.")
    print(f"Total chars: {total_chars:,} (~{total_chars // 4:,} tokens estimated)")

    if total_chars > 60000:
        print("\n⚠ WARNING: Approaching token ceiling. Consider removing an extra_files entry.")
    elif total_chars > 40000:
        print("\n→ Moderate load. Should be fine for most sessions.")
    else:
        print("\n✓ Light load. Room to spare.")

    failed = [f for f, c in fetched.items() if c.startswith("[FETCH FAILED")]
    if failed:
        print(f"\n⚠ FETCH FAILURES ({len(failed)}):")
        for f in failed:
            print(f"  - {f}")
        print("  Audit kit or target file failure will compromise the audit.")

    # ── Phase 1 enforcement + boundary index (old Cell 3.5) ─────────────
    # run_phase1 will sys.exit(1) on a confirmed constitutional mutation,
    # same as before — unchanged behavior.
    p1_findings, p1_anchor, p1_fields = run_phase1(fetched, FILE_REGISTRY)
    boundary_index = format_boundary_index(fetched)
    print(boundary_index)

    # ── assemble prompt (old Cell 4) ─────────────────────────────────────
    divider = "=" * 60
    sections = []

    sections.append(
        f"Operating as Skeptic/Auditor per Auditor_Protocols.md v0.14\n"
        f"Repository: LazarusForge"
    )

    sections.append(
        f"ASSUMPTION EXTRACTION (Rule 6):\n"
        f"Prior contributions assumed:\n"
        f"- {target_file} is classified as {doc_status}\n"
        f"- Forge_Audit_Kit.md contains the active Fallacy Checklist, Verification Gates,\n"
        f"  AI Contribution Rules, and condensed Unknowns Registry\n"
        f"- Repository uses folder-based structure: Admin/, Architecture/, Operations/,\n"
        f"  Tests/, Challenges/\n"
        f"- Rename Registry in Archive/Rename_Registry.md maps legacy filenames to current canonical paths\n"
        f"- Full reference files: Admin/Auditor_Protocols.md | Unknowns.md\n"
        f"These assumptions are carried forward unless contradicted by new findings."
    )

    sections.append(boundary_index)

    sections.append(
        f"TASK:\n"
        f"Audit {target_file} (status: {doc_status}).\n\n"
        f"Apply the full Fallacy Checklist from Forge_Audit_Kit.md.\n"
        f"Use the Verification Gates to assess promotion readiness.\n"
        f"Open with an Expiry Watch — the SESSION BOUNDARY INDEX above surfaces\n"
        f"any overdue unknowns from the loaded files; confirm and escalate as needed.\n\n"
        f"Audit focus:\n{focus}\n\n"
        f"Label all findings: [FALLACY], [GAP], [CONTRADICTION], [UNLOGGED UNKNOWN],\n"
        f"[CROSS-REF FAILURE]. For each finding, suggest a concrete resolution path.\n\n"
        f"Cross-reference naming note: the repository uses folder-prefixed paths\n"
        f"(Admin/Ethical_Constraints.md, Operations/Energy.md, Challenges/Water.md).\n"
        f"Legacy flat names (Ethical_Constraints.md, energy_v0.md, Spin_Chamber_v0.md)\n"
        f"are aliases — do not flag folder-prefixed paths as cross-reference failures.\n"
        f"The canonical form always includes the folder prefix.\n\n"
        f"End with the standard sign-off format from Forge_Audit_Kit.md."
    )

    file_block = f"FILES PROVIDED ({len(fetched)}):\n"
    for i, (name, content) in enumerate(fetched.items(), 1):
        resolved_path = FILE_REGISTRY.get(name, name)
        file_block += (f"\n{divider}\nFILE {i}: {name} "
                       f"(fetched from: {resolved_path})\n{divider}\n{content}\n")
    sections.append(file_block)

    prompt = ("\n\n" + divider + "\n\n").join(sections)

    print(f"\nPrompt assembled.")
    print(f"Total length: {len(prompt):,} chars (~{len(prompt) // 4:,} tokens estimated)")

    # ── print (old Cell 5) ────────────────────────────────────────────
    print("\nFRAMING LINE (paste this at the TOP of the Claude conversation first):")
    print("─" * 60)
    print(framing_line)
    print()
    print("PROMPT (copy everything below this line):")
    print("─" * 60)
    print(prompt)

    # ── optional save (old Cell 6) ───────────────────────────────────────
    if save_to_file:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        safe_target = target_file.replace(".md", "").replace("/", "_")
        out_filename = f"forge_audit_{safe_target}_{timestamp}.txt"

        with open(out_filename, "w") as f:
            f.write(f"FRAMING LINE:\n{framing_line}\n\n")
            f.write("=" * 60 + "\n\n")
            f.write(prompt)

        print(f"\nSaved: {out_filename}")
        print("In Colab: Files panel (left sidebar) → download from there.")

    print(f"\nTarget file resolved to: {FILE_REGISTRY.get(target_file, target_file)}")
    print(f"Audit kit resolved to:   {FILE_REGISTRY.get('Forge_Audit_Kit.md', 'Admin/Forge_Audit_Kit.md')}")

    return {
        "prompt": prompt,
        "framing_line": framing_line,
        "findings": p1_findings,
        "fetched": fetched,
        "boundary_index": boundary_index,
    }
