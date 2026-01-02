from pydantic import BaseModel, Field, validator
from datetime import datetime
import uuid

class OneDropContract(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    source: str = "TIER_0_FIELD_UPLINK"
    alpha: float = Field(..., description="Quantity")
    i_friction: float = Field(0.0)
    j_friction: float = Field(0.0)
    k_friction: float = Field(0.0)
    notes: str = ""

    @validator('j_friction', pre=True)
    def normalize_time(cls, v):
        if isinstance(v, (int, float)) and v > 1.0: return min(1.0, float(v) / 24.0)
        return v
