import os
import subprocess
import json
import re

def extract_simplicial_data(input_content):
    api_key = os.environ.get("GOOGLE_API_KEY")
    
    # SUCCESSOR ROUTE: Switching from v1beta to v1 (Stable)
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{"text": f"Task: Extract 4 values (alpha, i_friction, j_friction, k_friction) as raw JSON from this logistics text. If a value isn't mentioned, use 0 for frictions and the contracted quantity for alpha. Return ONLY the JSON object. Text: {input_content}"}]
        }]
    }

    try:
        # Using -s (silent) to keep the terminal clean
        result = subprocess.run(
            ['curl', '-s', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', json.dumps(payload), url],
            capture_output=True, text=True
        )
        
        response_data = json.loads(result.stdout)
        
        # Check for API-level errors
        if "error" in response_data:
            print(f"API ERROR: {response_data['error']['message']}")
            return '{"alpha": 100, "i_friction": 0, "j_friction": 0, "k_friction": 0}'

        raw_text = response_data['candidates'][0]['content']['parts'][0]['text']
        
        # Surgical extraction of the JSON block using Regex
        # (This handles cases where the AI adds 'Here is your JSON:')
        match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        if match:
            return match.group(0)
        return raw_text
        
    except Exception as e:
        print(f"STITCHING FAILED: {e}")
        # Defaulting to 100 alpha to keep the dashboard alive
        return '{"alpha": 100, "i_friction": 0, "j_friction": 0, "k_friction": 0}'