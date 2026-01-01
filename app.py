import streamlit as st
import pandas as pd
import json
import time
import ingestor
import stitcher

# --- SHADOW CORE INTEGRATION ---
from private_core.pwp_core_engine import SecureEpochVault

# Initialize Sovereign Persistence
if 'vault' not in st.session_state:
    st.session_state.vault = SecureEpochVault("White_Piece_Live_Session")

# Page Configuration
st.set_page_config(page_title="The Stitching Layer", layout="wide")

st.title("The Stitching Layer: Control Center")
st.markdown("### Topology Status: **ACTIVE** (Real-Time Quaternionic Engine)")
st.divider()

# 1. The Drop Zone
col_main, col_metrics = st.columns([2, 1])

# --- LEFT COLUMN (Inputs) ---
with col_main:
    st.subheader("1. Define the Contract (Ground Truth)")
    expected_qty = st.number_input("Contracted Quantity (Alpha)", value=100)
    
    st.subheader("2. Ingest Reality (Restriction Map)")
    raw_input = st.text_area("Paste Logistics Report", height=100)
    
    # Initialize result variable to None so metrics check logic works
    result = None
    
    if st.button("Calculate Torsion"):
        if raw_input:
            with st.spinner("Analyzing..."):
                extracted_json = ingestor.extract_simplicial_data(raw_input)
                data = json.loads(extracted_json)
                
                # Dynamic Truth from the UI
                truth = [expected_qty, 0, 0, 0]
                
                # Reality from the AI
                reality = [
                    float(data.get('alpha', 0)), 
                    float(data.get('i_friction', 0)), 
                    float(data.get('j_friction', 0)), 
                    float(data.get('k_friction', 0))
                ]
                
                # Pass the 'vault' from session state into the stitcher
                result = stitcher.perform_handshake(truth, reality, "Live_Audit", vault=st.session_state.vault)
                
            st.write(f"### Result: {result['status']}")
            st.metric("Geometric Torsion", result['torsion'])
            st.json(data) # Show what the AI extracted

# --- RIGHT COLUMN (Metrics) ---
# This block is UN-INDENTED so it always runs
with col_metrics:
    st.subheader("Cohomology Metrics")
    
    # Check if a result exists from the button press
    if result:
        current_torsion = result['torsion']
        alignment_score = max(0.0, 100.0 - (current_torsion / 4.0))
        torsion_label = "High" if current_torsion > 10 else "Low"
        delta_val = f"-{round(current_torsion/10, 1)}%" if current_torsion > 0 else "0%"
    else:
        # Default state
        alignment_score = 100.0
        torsion_label = "None"
        delta_val = "0%"

    st.metric(label="Global Section Alignment (H0)", 
              value=f"{round(alignment_score, 1)}%", 
              delta=delta_val, 
              delta_color="inverse")
    
    st.metric(label="Calculated Torsion (H1)", value=torsion_label)
    st.caption("Monitoring real-time sheaf torsion via Quaternionic Engine.")

# --- BOTTOM SECTION (Diamond Table) ---
st.divider()
st.subheader("Diamond Complex Status")
st.info("The orchestrator is evaluating the consistency of the 4-node cycle.")

torsion_val = result['torsion'] if result else 0.0

diamond_data = [
    {"Edge": "A (Manufacturer) ➔ B (Logistics)", "Status": "ALIGNED", "Torsion": 0.0},
    {"Edge": "B (Logistics) ➔ C (Port)", "Status": "ALIGNED", "Torsion": 0.0},
    {"Edge": "C (Port) ➔ D (Buyer)", "Status": "MISALIGNED" if torsion_val > 0 else "ALIGNED", "Torsion": torsion_val},
    {"Edge": "D (Buyer) ➔ A (Manufacturer)", "Status": "MISALIGNED" if torsion_val > 0 else "ALIGNED", "Torsion": torsion_val * 1.05}
]

st.table(pd.DataFrame(diamond_data))

if torsion_val > 0:
    st.error(f"SYSTEMIC HOLE DETECTED: The cycle cannot close with a boundary error of {round(torsion_val * 1.05, 2)}.")

# --- SIDEBAR (Sovereign Security) ---
with st.sidebar:
    st.header("🛡️ Sovereign Security")
    
    # Display Current Epoch
    st.metric("Current Epoch", f"#{st.session_state.vault.epoch_id}")
    
    # Active Nodes Visualizer
    active_nodes = st.session_state.vault.active_nodes
    cols = st.columns(3)
    cols[0].write("🇺🇸" if "US" in active_nodes else "💀")
    cols[1].write("🇪🇺" if "EU" in active_nodes else "💀")
    cols[2].write("🇨🇳" if "CN" in active_nodes else "💀")
    
    st.divider()
    
    # The "Kill Switch" for Demo
    if "CN" in active_nodes:
        if st.button("Simulate CN Disconnect"):
            st.session_state.vault.heartbeat_check(failing_region="CN")
            st.rerun()
    else:
        st.error("Region CN Offline. Epoch Shifted.")
        if st.button("Reset Simulation"):
            del st.session_state.vault
            st.rerun()

    # Shadow Basis Inspector (Auditor View)
    with st.expander("View Shadow Basis (H1)"):
        current_basis = st.session_state.vault.synthesize_sheaf_laplacian()
        if current_basis:
            st.write(f"**Basis:** {current_basis}")
            st.write(f"**Public Norm:** {current_basis.norm():.4f}")
        else:
            st.error("Consensus Failure")

            # --- REPAIR SECTION ---
if torsion_val > 0:
    st.divider()
    st.subheader("🔧 Auto-Repair Protocol")
    
    # Call the new function
    repair_steps = stitcher.suggest_repair(truth, reality)
    
    # Display the prescriptions
    for step in repair_steps:
        st.warning(step, icon="⚠️")
        
    st.caption("These actions represent the 'Gradient Descent' required to restore H1 to 0.")