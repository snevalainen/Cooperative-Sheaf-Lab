import streamlit as st
import json
import glob
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.sheaf_math import compute_integrity

st.set_page_config(page_title="PWP Command", page_icon="💀", layout="wide")
st.markdown("<style>.stApp { background-color: #000000; font-family: 'Consolas', monospace; } h1, h2, h3, p, div { color: #00ff00 !important; } .block-container { padding-top: 4rem; }</style>", unsafe_allow_html=True)

st.title("💀 COMMAND DECK // TIER 1")

# Sidebar: Context
with st.sidebar:
    st.header("CONTRACT CONSTRAINTS")
    contract_qty = st.number_input("Expected Qty", value=1000)

# Data Relay
files = glob.glob("data_relay/*.json")
if not files:
    st.warning("NO SIGNALS DETECTED")
    st.stop()

latest = max(files, key=os.path.getctime)
with open(latest, 'r') as f: data = json.load(f)

# Math Execution
reality = [data['alpha'], data['i_friction'], data['j_friction'], data['k_friction']]
metrics = compute_integrity([contract_qty, 0.0, 0.0, 0.0], reality)

# --- THE HEADLINE METRICS ---
c1, c2, c3 = st.columns(3)
c1.metric("DEAL INTEGRITY", f"{metrics['integrity_pct']:.1f}%")
c2.metric("RECOVERABLE VALUE", f"${metrics['leakage']:,.2f}")
c3.metric("RISK INDEX", f"{metrics['risk_index']:.3f}")

st.divider()

# --- THE COMPONENT BREAKDOWN (Plain English) ---
st.markdown("#### SIGNAL DIAGNOSTICS")
b1, b2, b3 = st.columns(3)
b1.progress(metrics['components']['qty_match'] / 100, text=f"QUANTITY MATCH: {metrics['components']['qty_match']:.1f}%")
b2.progress(metrics['components']['punctuality'] / 100, text=f"PUNCTUALITY: {metrics['components']['punctuality']:.1f}%")
b3.progress(metrics['components']['quality'] / 100, text=f"QUALITY: {metrics['components']['quality']:.1f}%")

st.divider()

if not metrics['is_aligned']:
    st.error("⚠️ CONTRACT BREACH DETECTED")
else:
    st.success("✅ CONTRACT FULFILLED")

st.caption(f"Signal Source: {data['id']}")
