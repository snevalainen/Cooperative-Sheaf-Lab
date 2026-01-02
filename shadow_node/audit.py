import sys
import os

# Add current directory to path so we can import local modules
sys.path.append(os.getcwd())

from shadow_node.scraper import UniversalTranslator
from shadow_node.contract import OneDropContract

def run_pipeline(raw_text, source_label):
    print(f"\n--- INGESTING: {source_label} ---")
    
    # 1. OBSERVE (Scrape)
    node = UniversalTranslator()
    artifact_path = node.ingest(raw_text, source_label)
    print(f"✓ Observation saved: {artifact_path}")

    # 2. ORIENT (Validate)
    try:
        contract = OneDropContract.from_artifact(artifact_path)
        print(f"✓ ORIENTATION SUCCESSFUL (H0 Signal)")
        print(f"  > Quantity: {contract.alpha}")
        print(f"  > Time Friction: {contract.j_friction}")
        print("  > Status: VALID CONTRACT")
        return True
    except ValueError as e:
        print(f"✗ TOPOLOGICAL WASTE DETECTED (H1 Leak)")
        print(f"  > Reason: {e}")
        return False

if __name__ == "__main__":
    # Test Case 1: Clean Data
    run_pipeline(
        "Manifest A: 100 units. No delays.", 
        "TEST_CLEAN_01"
    )
    
    # Test Case 2: Dirty/Waste Data
    run_pipeline(
        "This is just a random chat log with no logistics data.", 
        "TEST_WASTE_01"
    )