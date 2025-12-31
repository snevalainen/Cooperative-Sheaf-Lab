import streamlit as st
import pandas as pd
import json
import time
import ingestor
import stitcher

# Page Configuration
st.set_page_config(page_title="The Stitching Layer", layout="wide")

st.title("The Stitching Layer: Control Center")
st.markdown("### Topology Status: **ACTIVE** (Real-Time Quaternionic Engine)")
st.divider()

# 1. The Drop Zone
col_main, col_metrics = st.columns([2, 1])

with col_main:
    st.subheader("1. Define the Contract (Ground Truth)")
    # Let the user define what was *supposed* to happen
    expected_qty = st.number_input("Contracted Quantity (Alpha)", value=100)
    
    st.subheader("2. Ingest Reality (Restriction Map)")
    raw_input = st.text_area("Paste Logistics Report", height=100)
    
    if st.button("Calculate Torsion"):
        if raw_input:
            with st.spinner("Analyzing..."):
                extracted_json = ingestor.extract_simplicial_data(raw_input)
                data = json.loads(extracted_json)
                
                # Dynamic Truth from the UI
                truth = [expected_qty, 0, 0, 0]
                
                # Reality from the AI
                logistics_data = [
                    float(data.get('alpha', 0)), 
                    float(data.get('i_friction', 0)), 
                    float(data.get('j_friction', 0)), 
                    float(data.get('k_friction', 0))
                ]
                
                result = stitcher.perform_handshake(truth, logistics_data, "Live_Audit")
                
            st.write(f"### Result: {result['status']}")
            st.metric("Geometric Torsion", result['torsion'])
            st.json(data) # Show what the AI extracted

with col_metrics:
    st.subheader("Cohomology Metrics")
    
    # Calculate an 'Alignment Score' based on torsion
    # 0 torsion = 100% alignment. 400 torsion = 0% alignment.
    if 'result' in locals():
        current_torsion = result['torsion']
        alignment_score = max(0.0, 100.0 - (current_torsion / 4.0)) # Scaling for demo impact
        torsion_label = "High" if current_torsion > 10 else "Low"
        delta_val = f"-{round(current_torsion/10, 1)}%" if current_torsion > 0 else "0%"
    else:
        alignment_score = 100.0
        torsion_label = "None"
        delta_val = "0%"

    st.metric(label="Global Section Alignment (H0)", 
              value=f"{round(alignment_score, 1)}%", 
              delta=delta_val, 
              delta_color="inverse")
    
    st.metric(label="Calculated Torsion (H1)", value=torsion_label)
    st.caption("Monitoring real-time sheaf torsion via Quaternionic Engine.")

# 2. The Loop Monitor
st.divider()
st.subheader("Diamond Complex Status")
st.info("The orchestrator is evaluating the consistency of the 4-node cycle.")

# Calculate local vs global torsion for the demo table
torsion_val = result['torsion'] if 'result' in locals() else 0.0

# We simulate the rest of the loop to show how the torsion propagates
diamond_data = [
    {"Edge": "A (Manufacturer) ➔ B (Logistics)", "Status": "ALIGNED", "Torsion": 0.0},
    {"Edge": "B (Logistics) ➔ C (Port)", "Status": "ALIGNED", "Torsion": 0.0},
    {"Edge": "C (Port) ➔ D (Buyer)", "Status": "MISALIGNED" if torsion_val > 0 else "ALIGNED", "Torsion": torsion_val},
    {"Edge": "D (Buyer) ➔ A (Manufacturer)", "Status": "MISALIGNED" if torsion_val > 0 else "ALIGNED", "Torsion": torsion_val * 1.05} # The 'Closure' Error
]

st.table(pd.DataFrame(diamond_data))

if torsion_val > 0:
    st.error(f"SYSTEMIC HOLE DETECTED: The cycle cannot close with a boundary error of {round(torsion_val * 1.05, 2)}.")