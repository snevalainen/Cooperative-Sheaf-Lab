"""
MODULE: torsion_metrics.py
CONTEXT: THE ASYNC UPDATE PROBLEM (Latency as Torsion)

MATHEMATICAL AXIOMS (COHOMOLOGY):
This module quantifies the Operational Risk during the time lag between
a Manager's decision and a Driver's acknowledgment.

1. THE LATENCY INTERVAL (Delta t):
   Defined as the time between t_sent and t_ack.
   During this interval:
     x_M = "Route B"
     x_D = "Route A"

2. SHEAF TORSION (H^1):
   We measure the consistency of the edge e_MD (Manager-Driver) using the
   Coboundary Operator:
   delta^0(e_MD) = rho_M(x_M) - rho_D(x_D)
   
   Since rho_M != rho_D, delta^0 != 0.
   The system is in a state of Torsion (H^1 > 0).

3. THE CONVERGENCE CONDITION:
   The system only achieves Global Consensus (H^0) when the Driver ACKS.
   The "Ack" is the mathematical signal that the Cohomology Group H^1
   has collapsed to zero.

CONSTRAINT:
   The UI must visualize "Unacknowledged Messages" as "Active Torsion" (Red/Heat),
   not just "Pending." It is a measure of system instability.

REFERENCE:
   "The Shape of Agreement", Nevalainen (2025).
   Section 5: Economic Phase Shift (Consensus vs. Torsion).
"""

import math
from datetime import datetime

class TorsionMonitor:
    """
    Real-time calculator of H^1 metrics based on state divergence
    between nodes.
    """

    def calculate_h1_metric(self, manager_state: dict, driver_state: dict) -> float:
        """
        Computes the Coboundary Operator delta^0.
        Returns the magnitude of Torsion (0.0 = Consensus, >0.0 = Instability).
        """
        # 1. Extract Vectors (Simplified for MVP)
        # Assume states have a 'coordinate' (e.g., location index or route ID)
        v_manager = self._vectorize(manager_state)
        v_driver = self._vectorize(driver_state)

        # 2. Compute Difference (Coboundary)
        # delta^0 = x_M - x_D
        delta_sq = sum((m - d) ** 2 for m, d in zip(v_manager, v_driver))
        torsion_magnitude = math.sqrt(delta_sq)

        return torsion_magnitude

    def get_heat_color(self, torsion: float) -> str:
        """
        Maps Torsion magnitude to UI Heat (Red/Green).
        Constraints: Any Torsion > 0 is 'Active Risk'.
        """
        if torsion < 0.01:
            return "#00FF00" # GREEN (Consensus / Low Energy)
        elif torsion < 5.0:
            return "#FFA500" # ORANGE (Transitioning)
        else:
            return "#FF0000" # RED (Sheaf Fracture / High Energy)

    def _vectorize(self, state: dict) -> list:
        # Helper: Turn state dict into comparable vector
        # E.g., {'route_id': 105} -> [105.0]
        return [float(val) for val in state.values() if isinstance(val, (int, float))]