import numpy as np
from engine import QuaternionicSection, calculate_torsion

def perform_handshake(party_a_data, party_b_data, shared_context, vault=None):
    """
    Simulates the Stitching Layer with Shadow Core Integration.
    It takes two local sections and verifies their agreement on a shared edge.
    
    Args:
        party_a_data (list): [Quantity, i_friction, j_friction, k_friction]
        party_b_data (list): [Quantity, i_friction, j_friction, k_friction]
        shared_context (str): Label for the edge.
        vault (SecureEpochVault, optional): The sovereign security core.
    """
    
    # 1. Standard Euclidean Difference (The "Public" View)
    # This calculates the raw distance between the vectors before Shadow distortion
    diff = np.array(party_a_data) - np.array(party_b_data)
    euclidean_torsion = np.linalg.norm(diff)
    
    # 2. Apply Shadow Patching (If Vault is Active)
    if vault:
        # Get the current Epoch's Hidden Basis
        shadow_q = vault.synthesize_sheaf_laplacian()
        
        # Check for Geopolitical Fracture (Consensus Failure)
        if shadow_q is None:
            return {
                "context": shared_context,
                "status": "FRACTURED",
                "torsion": 9999.0, # Infinite Friction
                "waste_stream_impact": "CRITICAL",
                "message": "CRITICAL: Consensus Layer Broken. Halt Logistics."
            }
            
        # The "Shadow Norm" - This simulates the internal friction
        # We multiply the raw torsion by the 'Logistics Entropy' (i component)
        # This makes the error 'sensitive' to the hidden basis state.
        # Formula: Torsion_Adjusted = Torsion_Raw * (1 + |i_friction|)
        entropy_factor = 1.0 + abs(shadow_q.x) 
        adjusted_torsion = euclidean_torsion * entropy_factor
        basis_id = f"Epoch_{vault.epoch_id}"
    else:
        # Fallback to legacy behavior if no vault is present
        adjusted_torsion = euclidean_torsion
        basis_id = "Legacy_Euclidean"

    # 3. The 'Certainty' Threshold
    is_aligned = adjusted_torsion < 0.01 
    
    return {
        "context": shared_context,
        "torsion": round(adjusted_torsion, 4),
        "status": "ALIGNED" if is_aligned else "MISALIGNED",
        "waste_stream_impact": "LOW" if is_aligned else "HIGH",
        "basis_used": basis_id
    }

def suggest_repair(truth, reality):
    """
    Calculates the 'Gradient of Repair' - the specific actions needed
    to zero out the Torsion.
    """
    # Unpack vectors: [Alpha, i, j, k]
    # Truth usually has 0 friction, Reality has observed friction
    qty_gap = truth[0] - reality[0]
    time_friction = reality[2] # j component
    cost_friction = reality[3] # k component
    
    recommendations = []
    
    # 1. Quantity Repair (Alpha)
    if abs(qty_gap) > 0:
        action = "Supplemental Shipment" if qty_gap > 0 else "Return Overstock"
        recommendations.append(f"📦 **Logistics:** Initiate {action} of {abs(qty_gap)} units.")
        
    # 2. Time Repair (j - Temporal)
    # If j_friction > 0.1, the loop is dragging temporally.
    if time_friction > 0.1:
        hours_to_recover = round(time_friction * 24.0, 1)
        recommendations.append(f"⏱️ **Timeline:** Expedite next leg by {hours_to_recover} hours to recover sync.")
        
    # 3. Cost Repair (k - Financial)
    if cost_friction > 0.1:
        # Arbitrary scaling: 0.1 friction = $1000 variance
        est_variance = round(cost_friction * 10000, 2)
        recommendations.append(f"💰 **Budget:** Authorize variance payment of ${est_variance}.")
        
    if not recommendations:
        return ["✅ System is Aligned. No repair needed."]
        
    return recommendations