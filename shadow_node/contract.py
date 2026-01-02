import json
from dataclasses import dataclass, asdict

@dataclass
class OneDropContract:
    """
    DIRECTIVE 01: THE SCHEMA
    Strictly typed container. 
    Any data that cannot be coerced here is TOPOLOGICAL WASTE.
    """
    alpha: int       # Quantity (Real)
    i_friction: float # Logistics Entropy (Imaginary i)
    j_friction: float # Temporal Delay (Imaginary j)
    k_friction: float # Financial Cost (Imaginary k)
    timestamp: str
    source_id: str

    @classmethod
    def from_artifact(cls, filepath):
        """
        Loads a JSON artifact and enforces the Schema.
        """
        with open(filepath, 'r') as f:
            data = json.load(f)

        # 1. Check for explicit Waste flag
        if data.get("status") == "TOPOLOGICAL_WASTE":
            raise ValueError("Artifact is flagged as WASTE.")

        # 2. Strict Type Coercion
        try:
            return cls(
                alpha=int(data['alpha']),
                i_friction=float(data.get('i_friction', 0.0)),
                j_friction=float(data.get('j_friction', 0.0)),
                k_friction=float(data.get('k_friction', 0.0)),
                timestamp=data['_meta']['timestamp'],
                source_id=data['_meta']['source']
            )
        except (KeyError, ValueError, TypeError) as e:
            raise ValueError(f"Schema Violation: {e}")

    def to_json(self):
        return json.dumps(asdict(self), indent=2)