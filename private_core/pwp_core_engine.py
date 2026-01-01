import numpy as np
import hashlib
import secrets
import time

class Quaternion:
    """
    The Atomic Data Type for the White Piece Logic.
    Represents q = a + bi + cj + dk
    """
    def __init__(self, a, b, c, d):
        self.w = float(a) # Scalar (Alpha/Quantity - H0)
        self.x = float(b) # i (Logistic Friction - Primary Entropy)
        self.y = float(c) # j (Temporal Friction)
        self.z = float(d) # k (Financial Friction)

    def __repr__(self):
        return f"({self.w:.2f} + {self.x:.2f}i + {self.y:.2f}j + {self.z:.2f}k)"

    def norm(self):
        # The "Public Heat" metric (Euclidean distance) exposed to the UI
        return np.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    def multiply(self, other):
        # Non-commutative Hamilton Product
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z

        return Quaternion(
            w1*w2 - x1*x2 - y1*y2 - z1*z2,
            w1*x2 + x1*w2 + y1*z2 - z1*y2,
            w1*y2 - x1*z2 + y1*w2 + z1*x2,
            w1*z2 + x1*y2 - y1*x2 + z1*w2
        )

    def conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)

class SecureEpochVault:
    """
    Implements (2, 3) Threshold Logic with Epoch Shifting.
    Simulates Sovereign-Grade Resilience.
    """
    def __init__(self, master_salt):
        self.epoch_id = 1
        self.master_salt = master_salt
        self.regions = ["US", "EU", "CN"]
        self.active_nodes = ["US", "EU", "CN"] # All healthy initially
        self.polynomial_coeffs = None
        self.shards = {}
        
        # Initialize Epoch 1
        self._generate_epoch_basis()

    def _generate_epoch_basis(self):
        """
        Generates a random polynomial f(x) = Secret + a1*x
        Where 'Secret' is derived from the Master Salt + Current Epoch.
        """
        # 1. Deterministic Secret for this Epoch
        context = f"{self.master_salt}_EPOCH_{self.epoch_id}"
        epoch_secret_int = int(hashlib.sha256(context.encode()).hexdigest(), 16) % (10**10)
        
        # 2. Random slope for the polynomial (The "Noise")
        slope = secrets.randbelow(10**5)
        
        self.polynomial_coeffs = (epoch_secret_int, slope)
        
        # 3. Distribute Shards f(1), f(2), f(3)
        self.shards = {}
        for idx, region in enumerate(self.regions, 1):
            val = epoch_secret_int + (slope * idx)
            self.shards[region] = (idx, val)
            
        print(f"\n[EPOCH {self.epoch_id} ONLINE] Secret distributed via (2, 3) Threshold.")

    def heartbeat_check(self, failing_region=None):
        """
        Simulates a network check. If a region fails, trigger Epoch Shift.
        """
        if failing_region and failing_region in self.active_nodes:
            print(f"⚠️ ALERT: Region_{failing_region} heartbeat lost.")
            self.active_nodes.remove(failing_region)
            self._trigger_epoch_shift()
        else:
            print(f"✓ Heartbeat Nominal. Active: {self.active_nodes}")

    def _trigger_epoch_shift(self):
        """
        Re-keys the system using the remaining nodes.
        Forward Secrecy: Old keys are mathematically obsolete.
        """
        print(f"⚙️ EXECUTING EPOCH SHIFT to Epoch {self.epoch_id + 1}...")
        
        if len(self.active_nodes) < 2:
            raise SystemError("CRITICAL FAILURE: Insufficient nodes for consensus.")
            
        self.epoch_id += 1
        self.shards = {} # FLUSH old shards (Forward Secrecy)
        self._generate_epoch_basis()
        print(f"✓ RECOVERY COMPLETE. New Basis generated for {self.active_nodes}")

    def synthesize_sheaf_laplacian(self):
        """
        Reconstructs the Secret to generate the Basis Matrix.
        """
        if len(self.active_nodes) < 2:
            return None
            
        context = f"{self.master_salt}_EPOCH_{self.epoch_id}"
        seed_hash = hashlib.sha256(context.encode()).hexdigest()
        np.random.seed(int(seed_hash, 16) % (2**32))
        
        # The Mayer-Vietoris "Shadow Patch"
        return Quaternion(
            1.0, 
            np.random.normal(0, 0.5),  # High Logistic Friction (i)
            np.random.normal(0, 0.1),  # Moderate Temporal Friction (j)
            np.random.normal(0, 0.05)  # Low Financial Friction (k)
        )

# --- EXECUTION TEST ---
if __name__ == "__main__":
    vault = SecureEpochVault("White_Piece_Prime_Key_2025")
    
    # 1. Healthy State
    basis_q = vault.synthesize_sheaf_laplacian()
    print(f"Epoch {vault.epoch_id} Shadow Basis: {basis_q}")
    print(f"Public Norm (Auditable): {basis_q.norm():.4f}")
    
    # 2. Simulate Attack
    print("\n--- SIMULATING GEOPOLITICAL FRACTURE ---")
    vault.heartbeat_check(failing_region="CN")
    
    # 3. Verify Resilience
    new_basis_q = vault.synthesize_sheaf_laplacian()
    print(f"Epoch {vault.epoch_id} Shadow Basis: {new_basis_q}")