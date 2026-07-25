import sys, subprocess, json

result = subprocess.run(
    ["git", "clone", "-q", "https://github.com/ksarith/LazarusForgeV0.git", "/content/LazarusForgeV0"],
    capture_output=True, text=True
)
if result.returncode != 0 and "already exists" not in result.stderr:
    print("CLONE FAILED:", result.stderr)
    raise SystemExit(1)

sys.path.append('/content/LazarusForgeV0/Automation')
from cold_session_bundler import ColdSessionBundler

bundler = ColdSessionBundler("/content/LazarusForgeV0")
bundle = bundler.bundle(["Admin/Auditor_Protocols.md"])  # target file(s), explicit

print("=== MANIFEST (keep for your own records — never paste this to the auditor) ===")
print(json.dumps(bundle.manifest(), indent=2))

payload = bundle.render()
import os
if os.path.exists("/content/cold_session_payload.txt"):
    os.remove("/content/cold_session_payload.txt")
with open("/content/cold_session_payload.txt", "w") as f:
    f.write(payload)
print(f"\nPayload: {len(payload):,} chars — written to /content/cold_session_payload.txt")
print("Download via Files panel. Paste the ENTIRE file as the very first message")
print("to a brand-new chat session — nothing else before or after it, no framing of your own.")
