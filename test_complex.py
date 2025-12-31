import engine
import stitcher

# Manufacturer (Node A) says: "Contract is perfect" [Alpha=10, i=0, j=0, k=0]
node_a = [10, 0, 0, 0]

# Logistics (Node B) says: "There is a 3-unit delay in timing (j-friction)" [Alpha=10, i=0, j=3, k=0]
node_b = [10, 0, 3, 0]

print("--- SHAKE TEST: NODE A to NODE B ---")
result = stitcher.perform_handshake(node_a, node_b, "Shipment_Alpha")
print(f"Status: {result['status']}")
print(f"Torsion Level: {result['torsion']}")
print(f"Impact: {result['waste_stream_impact']}")
