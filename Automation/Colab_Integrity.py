import sys, subprocess, os

result = subprocess.run(
    ["git", "clone", "-q", "https://github.com/ksarith/LazarusForge.git", "/content/LazarusForge"],
    capture_output=True, text=True
)
if result.returncode != 0 and "already exists" not in result.stderr:
    print("CLONE FAILED:", result.stderr)
    raise SystemExit(1)

sys.path.append('/content/LazarusForge/Automation')
from integrity_check import run, print_summary

report = run("/content/LazarusForge")
print_summary(report)

# Optional: write full structured JSON alongside the summary
with open("/content/integrity_report.json", "w") as f:
    import json
    json.dump(report, f, indent=2)
print("\nFull report: /content/integrity_report.json — Files panel (left sidebar) to download.")
