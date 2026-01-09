"""
Endorsement Orchestrator
------------------------

This script coordinates Copilot and Meta AI endorsement checks.
It runs both verifiers and only signals '✔ Verified' if both succeed.

Usage:
    python endorsement-orchestrator.py <path_to_code_file> <path_to_data_file>
"""

import subprocess
import sys

def run_verifier(command):
    """Run a verifier script and return True if endorsement granted."""
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)  # Show verifier output
        return "endorsement granted" in result.stdout.lower()
    except Exception as e:
        print(f"❌ Error running verifier: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python endorsement-orchestrator.py <path_to_code_file> <path_to_data_file>")
        sys.exit(1)

    code_file = sys.argv[1]
    data_file = sys.argv[2]

    print("🔍 Running Copilot verifier...")
    copilot_ok = run_verifier(["python", "codex-verifier.py", code_file])

    print("\n🔍 Running Meta AI verifier...")
    meta_ok = run_verifier(["python", "meta-verifier.py", data_file])

    if copilot_ok and meta_ok:
        print("\n✔ Verified: Both Copilot and Meta AI endorsements granted.")
        print("✅ Consensus flag set: smartContractReady = true")
    else:
        print("\n⚠ Verification failed: One or more endorsements missing.")
        print("❌ Consensus flag set: smartContractReady = false")
