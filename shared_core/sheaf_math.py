import math

def compute_integrity(truth_vector, reality_vector):
    """
    Normalizes inputs to create a universal 'Risk Index'.
    """
    # 1. Unpack Vectors
    # Truth: [Exp_Qty, 0, 0, 0]
    # Reality: [Act_Qty, Damage%, Delay_Days, Cost_Overrun]
    exp_qty = truth_vector[0] if truth_vector[0] > 0 else 1
    act_qty = reality_vector[0]
    
    # 2. Normalize Components (0.0 = Perfect, 1.0 = Total Failure)
    
    # Alpha Risk (Quantity Mismatch): |1000 - 500| / 1000 = 0.5 Risk
    alpha_risk = abs(exp_qty - act_qty) / exp_qty
    
    # I-Risk (Damage): Already 0.0-1.0 from Schema
    i_risk = reality_vector[1]
    
    # J-Risk (Time): Input is fraction of day. Cap risk at 1.0 (24 hours late)
    j_risk = min(1.0, reality_vector[2])
    
    # K-Risk (Money): Arbitrary cap for MVP (e.g. risk=1.0 if cost > 10% of deal)
    # We will keep K simple for now.
    k_risk = reality_vector[3]

    # 3. Compute Global Risk Index (Euclidean Norm of Risks)
    # Max possible distance in 4D unit cube is 2.
    raw_distance = math.sqrt(alpha_risk**2 + i_risk**2 + j_risk**2 + k_risk**2)
    risk_index = min(1.0, raw_distance) # Cap at 100% Risk
    
    # 4. Integrity Score (The "Health" Metric)
    integrity_pct = (1.0 - risk_index) * 100
    
    # 5. Financial Leakage (The "Bottom Line")
    # Alpha=0/unit, Time=k/day, Money=0k/contract
    alpha_loss = max(0, exp_qty - act_qty) * 10
    time_loss = reality_vector[2] * 1000
    money_loss = reality_vector[3] * 10000
    
    return {
        "risk_index": risk_index,        # 0.0 to 1.0 (Universal Metric)
        "integrity_pct": integrity_pct,  # 100% to 0% (Human Readable)
        "is_aligned": risk_index < 0.02, # 2% tolerance
        "leakage": alpha_loss + time_loss + money_loss,
        "components": {
            "qty_match": (1.0 - alpha_risk) * 100,
            "quality": (1.0 - i_risk) * 100,
            "punctuality": (1.0 - j_risk) * 100
        }
    }
