import os
import google.generativeai as genai

# Set your API Key in your terminal environment before running:
# export GOOGLE_API_KEY='your-actual-key-here'

def extract_simplicial_data(input_content):
    """
    Uses Gemini Flash to convert raw logistical documents into 
    a structured 0-simplex JSON object ready for the Quaternionic Engine.
    """
    
    # Check if API key is set
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return {"error": "API Key not found. Please set GOOGLE_API_KEY environment variable."}

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # The prompt explicitly asks for our 4 quaternionic dimensions (a, i, j, k)
    prompt = """
    Analyze this logistics document. Extract the following into a structured JSON format:
    1. entity_name: (The name of the company or node)
    2. alpha: (Contracted Quantity/Agreement - The REAL part 'a')
    3. i_friction: (Physical or Logistical discrepancy - The 'i' part)
    4. j_friction: (Temporal/Timing delays - The 'j' part)
    5. k_friction: (Financial/Cost overruns - The 'k' part)
    
    If a friction value is not explicitly mentioned as a discrepancy, set it to 0.
    Return ONLY the JSON.
    """
    
    response = model.generate_content([prompt, input_content])
    
    # Basic cleaning to ensure we only get the JSON string
    json_text = response.text.strip().replace('```json', '').replace('```', '')
    return json_text

# To test this later at your terminal, you can uncomment these lines:
# sample_text = "Invoice from Shipper-B: 100 units expected, 95 delivered, 2 days late, $50 surcharge."
# print(extract_simplicial_data(sample_text))
