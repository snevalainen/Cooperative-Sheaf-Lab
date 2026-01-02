import streamlit as st
import pandas as pd
import json
import os
import glob
from shadow_node.scraper import UniversalTranslator
from shadow_node.validator import SheafValidator
from shadow_node.action_handler import ActionHandler

# --- 1. TERMINAL CONFIGURATION ---
st.set_page_config(
    page_title="PWP // SHADOW NODE",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. PHOSPHOR CSS (Compact Mode) ---
st.markdown("""
<style>
    .stApp { background-color: #000000; font-family: 'Consolas', 'Courier New', monospace; }
    
    /* COMPACT VIEWPORT */
/* COMPACT VIEWPORT (Aggressive Padding) */
    .block-container { 
        padding-top: 6rem !important; /* Force content down below any browser header */
        padding-bottom: 1rem; 
        padding-left: 1rem; 
        padding-right: 1rem; 
    }    
    /* SCROLLBARS */
    ::-webkit-scrollbar { width: 8px; background: #000; }
    ::-webkit-scrollbar-thumb { background: #33ff00; }
    
    /* TEXT */
    p, h1, h2, h3, label, .stMarkdown, div { color: #33ff00 !important; font-family: 'Consolas', monospace; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stNumberInput>div>div>input { 
        background-color: #050505; color: #33ff00; border: 1px solid #33ff00; border-radius: 0px; 
    }
    
    /* BUTTONS */
    .stButton>button { 
        background-color: #000000; color: #33ff00; border: 2px solid #33ff00; 
        border-radius: 0px; font-weight: bold; text-transform: uppercase; width: 100%;
    }
    .stButton>button:hover { background-color: #33ff00; color: #000000; }
    
    /* METRICS */
    div[data-testid="stMetricValue"] { font-size: 1.1rem !important; color: #33ff00; }
    div[data-testid="stMetricLabel"] { font-size: 0.6rem !important; color: #00aa00; }
    
    code { background-color: #111; color: #00ff00; border: none; font-size: 0.8rem;}
</style>
""", unsafe_allow_html=True)

# --- 3. EXECUTION CORE ---
def main():
    st.markdown("### **PWP // SHADOW NODE v2.2 (COMPACT)**")

    # GRID SETUP (TIGHTER)
    q1, q2 = st.columns([1, 1])
    q3, q4 = st.columns([1, 1])

    # --- QUADRANT 1: INPUT ---
    with q1:
        # Reduced Height to 200px to fit screen
        with st.container(height=200, border=True):
            st.markdown("#### [1] INGESTION")
            tab_manual, tab_net = st.tabs(["MANUAL", "NETWORK"])
            
            with tab_manual:
                expected_qty = st.number_input("CONTRACT_QTY", value=1000, step=10)
                raw_text = st.text_area("RAW_DATA", height=60, value="INVOICE #99. Qty: 1000. Delay: 6h.")
                manual_trigger = st.button(">> AUDIT <<", key="btn_man")

            with tab_net:
                list_of_files = glob.glob('shadow_node/artifact_*.json')
                latest_file = max(list_of_files, key=os.path.getctime) if list_of_files else None
                
                if latest_file:
                    st.success(f"SIGNAL: {os.path.basename(latest_file)}")
                    if st.button(">> INGEST EDGE <<", key="btn_net"):
                        with open(latest_file, 'r') as f:
                            st.session_state.network_packet = json.load(f)
                            # Default manual trigger to allow logic flow
                            manual_trigger = True 
                else:
                    st.warning("NO SIGNAL")

    # --- QUADRANT 2: METRICS ---
    with q2:
        with st.container(height=200, border=True):
            st.markdown("#### [2] SHEAF METRICS")
            metrics_container = st.empty()
            if 'audit_results' not in st.session_state:
                metrics_container.info("WAITING...")
            else:
                render_metrics(metrics_container, st.session_state.audit_results)

    # --- LOGIC HANDLING ---
    if 'network_packet' in st.session_state:
        # Use a default 'expected' or one stored in session
        run_audit_logic(1000, data=st.session_state.network_packet)
        del st.session_state.network_packet
        st.rerun()
    elif manual_trigger:
        run_audit_logic(expected_qty, raw_text=raw_text)
        st.rerun()

    # --- QUADRANT 3: DATA ---
    with q3:
        with st.container(height=200, border=True):
            st.markdown("#### [3] ARTIFACT")
            if 'audit_results' in st.session_state:
                st.json(st.session_state.audit_results['full_packet'])
            else:
                st.markdown("`NO DATA`")

    # --- QUADRANT 4: ACTION ---
    with q4:
        with st.container(height=200, border=True):
            st.markdown("#### [4] SURGERY")
            if 'audit_results' in st.session_state:
                res = st.session_state.audit_results
                if res['torsion'] > 0:
                    st.error(f"⚠️ SURGERY REQUIRED")
                    st.markdown(f"**FLOW:** {res['action_status']}")
                    # Highlight the Cash Value
                    st.markdown(f"### **LEAKAGE: ${res['leakage_est']}**")
                else:
                    st.success("SYSTEM STABLE")
            else:
                st.markdown("`STATIONARY`")

# --- LOGIC HANDLERS ---
def render_metrics(container, res):
    m1, m2, m3 = container.columns(3)
    m1.metric("ALPHA", res['alpha'])
    m2.metric("TORSION", f"{res['torsion']:.2f}")
    m3.metric("FRICTION", f"{res['full_packet'].get('j_friction', 0):.2f}")
    
    if res['torsion'] > 0:
        container.markdown(f"**STATUS:** `OBSTRUCTION`")
    else:
        container.markdown(f"**STATUS:** `ALIGNED`")

def run_audit_logic(expected_qty, raw_text=None, data=None):
    if raw_text:
        node = UniversalTranslator()
        artifact_path = node.ingest(raw_text, "LIVE_DEMO")
        with open(artifact_path, 'r') as f:
            data = json.load(f)
    
    # Vectors
    vector_truth = [float(expected_qty), 0.0, 0.0, 0.0]
    vector_reality = [
        float(data.get('alpha', 0)),
        0.0,
        float(data.get('j_friction', 0)),
        float(data.get('k_friction', 0))
    ]
    
    audit = SheafValidator.compute_coboundary(vector_truth, vector_reality)
    
    # C. ACT (With Updated Math)
    handler = ActionHandler()
    if audit['h1_presence']:
        action_success = handler.execute_surgery("DRIVER", {"reroute": True})
        action_status = "ACTIVE" if action_success else "BLOCKED"
        
        # IMPROVED LEAKAGE FORMULA:
        # Cost of Time + Cost of Money + Cost of Missing Units ($10/unit arbitrary)
        alpha_loss = max(0, vector_truth[0] - vector_reality[0]) * 10 
        friction_loss = (vector_reality[2] * 1000) + (vector_reality[3] * 10000)
        leakage = alpha_loss + friction_loss
    else:
        action_status = "IDLE"
        leakage = 0.0
        
    st.session_state.audit_results = {
        "alpha": vector_reality[0],
        "torsion": audit['torsion_magnitude'],
        "status": audit['status'],
        "action_status": action_status,
        "leakage_est": round(leakage, 2),
        "full_packet": data
    }

if __name__ == "__main__":
    main()