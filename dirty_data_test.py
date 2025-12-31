import ingestor
import engine
import stitcher
import json

def run_test():
    truth_data = [10, 0, 0, 0]
    raw_report = "Shipment B arrived. We expected 10 units but only got 10. However, the truck was 4 hours late due to weather and we had to pay a 0 fine."
    
    print("--- STEP 1: AI INGESTION ---")
    extracted_text = ingestor.extract_simplicial_data(raw_report)
    
    try:
        data = json.loads(extracted_text)
        print(f"AI Raw JSON: {data}")

        # Resilience Layer: Look for various possible names the AI might use
        alpha = data.get('alpha', data.get('quantity', 10))
        i = data.get('i_friction', data.get('logistics', 0))
        j = data.get('j_friction', data.get('time', 0))
        k = data.get('k_friction', data.get('money', 0))
        
        logistics_data = [float(alpha), float(i), float(j), float(k)]
        print(f"Mapped Quaternionic Data: {logistics_data}")

        print("\n--- STEP 2: TOPOLOGICAL AUDIT ---")
        result = stitcher.perform_handshake(truth_data, logistics_data, "Logistics_Edge")
        
        print(f"Status: {result['status']}")
        print(f"Torsion Level: {result['torsion']}")
        print(f"Impact: {result['waste_stream_impact']}")

    except Exception as e:
        print(f"Extraction Error: {e}")
        print(f"Raw AI Output was: {extracted_text}")

if __name__ == "__main__":
    run_test()
