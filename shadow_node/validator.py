"""
MODULE: validator.py
CONTEXT: THE DIAMOND (Local Consistency Check)

MATHEMATICAL AXIOMS (SHEAF THEORY):
This module implements the detection of Sheaf Torsion (H^1 > 0) within a
Simplicial Complex K (The Diamond: Source -> Broker/Carrier -> Warehouse).

1. THE COMMUTATIVITY CONDITION:
   For the system to be in a state of Global Section (H^0, Consensus), the
   composition of Restriction Maps (rho) along divergent paths must be identical.
   
   Let x_S be the Source Data.
   Path alpha (Broker): x_B = rho_S_to_B(x_S)
   Path beta (Carrier): x_C = rho_S_to_C(x_S)
   
   The condition for consistency at the Warehouse (W) is:
   rho_B_to_W(x_B) == rho_C_to_W(x_C)

2. THE COBOUNDARY OPERATOR (delta):
   The local difference on the closing edges is defined as:
   delta^0 = rho_B_to_W(x_B) - rho_C_to_W(x_C)

3. THE FIRST COHOMOLOGY GROUP (H^1):
   If delta^0 != 0, the cycle represents a non-trivial element in H^1.
   [z] in H^1(K; F) = ker(delta^1) / im(delta^0)
   
   INTERPRETATION:
   A non-zero H^1 value is NOT a "bug." It is a Topological Feature representing
   Systemic Waste (Fraud, Error, or Phantom Inventory).
   The Validator must NOT "fix" the data. It must strictly measure the magnitude
   of the Torsion (||delta^0||).

REFERENCE:
   "The Shape of Agreement", Nevalainen (2025).
   Section 4: The Metric: Cohomology as Waste.
"""

from typing import List, Dict, Tuple, Any
import math

class SheafValidator:
    """
    The Enforcer of Topological Consistency.
    Calculates the Coboundary Operator on incoming data packets.
    """

    @staticmethod
    def compute_coboundary(vector_a: List[float], vector_b: List[float]) -> Dict[str, Any]:
        """
        Calculates delta^0 = vector_a - vector_b.
        
        Args:
            vector_a (List[float]): The 'Truth' or 'Source' vector (e.g., [Alpha, i, j, k]).
            vector_b (List[float]): The 'Observed' or 'Target' vector.
            
        Returns:
            Dict containing:
                - 'delta_vector': The component-wise difference.
                - 'torsion_magnitude': The Euclidean Norm (||delta^0||).
                - 'is_aligned': Boolean (True if torsion < epsilon).
        """
        # AXIOM CHECK: Vectors must be in the same fiber (same dimension)
        if len(vector_a) != len(vector_b):
            raise ValueError("Topological Mismatch: Fiber dimensions do not align.")

        # 1. Compute the Difference Vector (The Coboundary)
        delta_vector = [a - b for a, b in zip(vector_a, vector_b)]

        # 2. Compute the Magnitude (The Torsion Metric)
        # Using Euclidean Norm for the 'Shadow' approximation of the Quaternionic Norm
        torsion_magnitude = math.sqrt(sum(x**2 for x in delta_vector))

        # 3. Determine Consistency (H^0 vs H^1)
        # We allow a small epsilon for floating point arithmetic, but NOT for logic errors.
        epsilon = 1e-5
        is_aligned = torsion_magnitude < epsilon

        return {
            "delta_vector": delta_vector,
            "torsion_magnitude": torsion_magnitude,
            "status": "GLOBAL_SECTION_ALIGNED" if is_aligned else "TOPOLOGICAL_OBSTRUCTION_DETECTED",
            "h1_presence": not is_aligned
        }

    @staticmethod
    def audit_cycle(nodes: Dict[str, List[float]], edge_map: List[Tuple[str, str]]) -> List[Dict]:
        """
        Walks a Simplicial Complex (Graph) and computes torsion on every edge.
        """
        audit_log = []
        for u, v in edge_map:
            if u in nodes and v in nodes:
                result = SheafValidator.compute_coboundary(nodes[u], nodes[v])
                audit_log.append({
                    "edge": f"{u}->{v}",
                    "torsion": result['torsion_magnitude'],
                    "status": result['status']
                })
        return audit_log