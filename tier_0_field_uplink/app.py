import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.schema import OneDropContract

st.set_page_config(page_title="PWP Uplink", page_icon="📡", layout="centered")
st.markdown("<style>.stApp { background-color: #1a1a1a; color: white; } .stButton>button { height: 4rem; font-size: 1.5rem; background-color: #00e676; color: black; font-weight: bold; width: 100%; }</style>", unsafe_allow_html=True)

st.title("📡 FIELD UPLINK")
with st.container(border=True):
    qty = st.number_input("Confirmed Quantity", min_value=0, value=500)
    delay = st.number_input("Delay (Hours)", min_value=0, value=0)
    dmg = st.number_input("Damaged Units", min_value=0, value=0)
    notes = st.text_input("Notes")

if st.button("🚀 TRANSMIT PACKET"):
    contract = OneDropContract(alpha=qty, i_friction=dmg/100.0, j_friction=delay, k_friction=0.0, notes=notes)
    with open(f"data_relay/packet_{contract.id}.json", "w") as f: f.write(contract.json())
    st.success("✅ PACKET SECURED")
