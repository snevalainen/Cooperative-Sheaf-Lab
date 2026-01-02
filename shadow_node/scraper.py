import json
import re
import os
import time
import warnings
from datetime import datetime

# SILENCE PROTOCOL
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

try:
    import google.generativeai as genai
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False

class UniversalTranslator:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("GOOGLE_API_KEY")
        self.mode = "HYBRID" 
        
        if self.api_key and AI_AVAILABLE:
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-1.5-flash')
                print(">> [ShadowNode] AI Bridge Established.")
            except Exception:
                self.mode = "OFFLINE_REGEX"
                print(">> [ShadowNode] API Handshake Failed. Defaulting to REGEX.")
        else:
            self.mode = "OFFLINE_REGEX"
            print(">> [ShadowNode] Running in OFFLINE Mode (Regex Only).")

    def ingest(self, raw_input, source_label="manual_entry"):
        timestamp = datetime.now().isoformat()
        clean_text = self._sanitize_input(raw_input)
        
        payload = None
        if self.mode != "OFFLINE_REGEX":
            payload = self._map_via_ai(clean_text)

        # Fallback if AI failed or returned WASTE despite data potentially existing
        if not payload or payload.get("status") == "TOPOLOGICAL_WASTE":
            # Double check with Regex before giving up
            regex_payload = self._map_via_regex(clean_text)
            if regex_payload.get("status") != "TOPOLOGICAL_WASTE":
                payload = regex_payload
                print(f"   [Debug] AI missed it. Regex recovered signal.")
            elif not payload:
                payload = regex_payload

        payload["_meta"] = {
            "timestamp": timestamp,
            "source": source_label,
            "extraction_method": self.mode
        }
        
        return self._save_artifact(payload)

    def _sanitize_input(self, text):
        if not text: return ""
        return "".join(ch for ch in text if ch.isprintable() or ch in ['\n', '\t'])

    def _map_via_ai(self, text):
        prompt = f"""
        Extract strict JSON. 
        Rules:
        - "alpha": Integer (Look for 'units', 'qty', 'count', or raw numbers associated with cargo).
        - "j_friction": Float 0-1 (Delay in hours / 24.0).
        - "k_friction": Float 0-1 (Cost / 10000.0).
        Input: "{text}"
        Return ONLY JSON.
        """
        try:
            response = self.model.generate_content(prompt)
            clean = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(clean)
        except Exception:
            return None # Return None to trigger fallback

    def _map_via_regex(self, text):
        data = {"alpha": 0, "j_friction": 0.0, "k_friction": 0.0, "status": "SIGNAL"}
        
        # ALPHA MATCH: Handles "Qty: 100" AND "100 units"
        # Group 1: Leading (Qty: 100)
        # Group 2: Trailing (100 units)
        qty_match = re.search(r"(?:qty|quantity|units|count)\s*[:=]?\s*(\d+)|(\d+)\s*(?:units|qty|quantity|pcs)", text, re.IGNORECASE)
        if qty_match:
            val = qty_match.group(1) or qty_match.group(2)
            data["alpha"] = int(val)
        
        # J-FRICTION MATCH
        hours = re.search(r"(\d+)\s*hours?\s*(?:late|delay)", text, re.IGNORECASE)
        if hours: data["j_friction"] = min(1.0, int(hours.group(1)) / 24.0)

        # K-FRICTION MATCH
        cost = re.search(r"\$\s*([\d,]+)", text)
        if cost:
            val = float(cost.group(1).replace(",", ""))
            data["k_friction"] = min(1.0, val / 10000.0)

        if data["alpha"] == 0 and data["j_friction"] == 0 and data["k_friction"] == 0:
            return {"status": "TOPOLOGICAL_WASTE"}
            
        return data

    def _save_artifact(self, data):
        # Use Microseconds to avoid collision
        filename = f"shadow_node/artifact_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return filename