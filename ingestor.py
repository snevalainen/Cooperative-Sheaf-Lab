import google.generativeai as genai
import os
import json
import re
import time

# Configure the Bridge
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("Warning: No API Key found.")
else:
    genai.configure(api_key=api_key)

def extract_simplicial_data(raw_text):
    """
    Robust Extraction: Tries AI first, falls back to Regex if API fails.
    Upgraded to detect:
    1. Alpha (Quantity)
    2. J (Time - Hours)
    3. K (Money - USD)
    """
    try:
        # 1. Attempt AI Extraction (Stable Model)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Extract JSON: {{"alpha": (number), "i_friction": (0-1), "j_friction": (0-1), "k_friction": (0-1)}}
        From: "{raw_text}"
        Rules: 
        - "received 95" -> alpha 95.
        - "6 hours late" -> j_friction 0.25 (since 6/24 = 0.25).
        - "cost $500" -> k_friction 0.05 (since 500/10000 = 0.05).
        """
        
        try:
            response = model.generate_content(prompt)
            text = response.text.strip()
            if text.startswith("```"):
                text = re.sub(r"^```json|^```", "", text).strip()
                text = re.sub(r"```$", "", text).strip()
            return text
            
        except Exception:
            raise ValueError("AI Unreachable")

    except Exception:
        # 2. The "Regex Fallback" (Offline Mode)
        print("⚠️ AI Failed. Switching to Regex Fallback.")
        
        # A. Alpha (Quantity)
        alpha_val = 0
        qty_match = re.search(r"(?:received|delivered|qty|quantity)\s*[:=]?\s*(\d+)", raw_text, re.IGNORECASE)
        if qty_match:
            alpha_val = int(qty_match.group(1))
            
        # B. J Friction (Time)
        j_val = 0.0
        time_match = re.search(r"(\d+)\s*hours?\s*(?:late|delay)", raw_text, re.IGNORECASE)
        if time_match:
            hours = int(time_match.group(1))
            j_val = min(1.0, hours / 24.0)

        # C. K Friction (Money) - NEW LOGIC
        # Looks for "$X" or "X USD"
        k_val = 0.0
        cost_match = re.search(r"\$\s*([\d,]+)|([\d,]+)\s*USD", raw_text, re.IGNORECASE)
        if cost_match:
            # Extract number from either group and remove commas
            raw_cost = cost_match.group(1) or cost_match.group(2)
            cost = float(raw_cost.replace(",", ""))
            # Normalize: $10,000 = 1.0 friction
            k_val = min(1.0, cost / 10000.0)

        return json.dumps({
            "alpha": alpha_val, 
            "i_friction": 0, 
            "j_friction": round(j_val, 3), 
            "k_friction": round(k_val, 4), 
            "note": "Extracted via Offline Regex (Full Spectrum)"
        })