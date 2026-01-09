"""
Legal Compliance Verifier
-------------------------

This script simulates a legal compliance endorsement module for smart contracts.
It checks contract metadata against basic compliance rules and outputs an endorsement flag.

Usage:
    python legal-verifier.py <path_to_metadata_file>
"""

import json
import sys
import os

def validate_legal(file_path: str) -> bool:
    """
    Simulates legal compliance validation.
    Expects a JSON file with keys: 'jurisdiction', 'transaction_type', 'parties'.
    Returns True if endorsement is granted.
    """
    if not os.path.exists(file_path):
        print("❌ Metadata file not found.")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    jurisdiction_ok = data.get("jurisdiction") in ["US", "EU", "BR"]
    transaction_ok = data.get("transaction_type") in ["payment", "supply_chain", "contractual_service"]
    parties_ok = all(p not in ["restricted_entity"] for p in data.get("parties", []))

    if jurisdiction_ok and transaction_ok and parties_ok:
        print("✔ Legal Compliance endorsement granted. Conditions validated.")
        return True
    else:
        print("⚠ Legal Compliance endorsement denied. Conditions not met.")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python legal-verifier.py <path_to_metadata_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    endorsed = validate_legal(file_path)

    if endorsed:
        print("✅ Endorsement flag set: legalEndorsed = true")
    else:
        print("❌ Endorsement flag set: legalEndorsed = false")
