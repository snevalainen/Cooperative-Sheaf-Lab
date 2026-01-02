import streamlit as st
import time
import json
from shadow_node.scraper import UniversalTranslator

# --- MOBILE CONFIGURATION ---
st.set_page_config(
    page_title="PWP Driver",
    page_icon="🚚",
    layout="centered" # Mobile-friendly vertical layout
)

# --- CSS FOR MOBILE (BIG BUTTONS) ---
st.markdown("""
<style>
    .stApp { background-color: #1a1a1a; color: #ffffff; }
    .stButton>button { 
        height: 3rem; 
        font-size: 1.5rem; 
        background-color: #007bff; 
        color: white; 
        border-radius: 10px; 
        border: none;
    }
    .stTextArea>div>div>textarea { font-size: 1.2rem; }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🚚 DRIVER PORTAL")
    st.markdown("### UPLOAD PROOF OF DELIVERY")
    st.divider()

    # INPUT: SIMULATED CAMERA / FILE UPLOAD
    # For MVP, we use text, but in prod this is st.camera_input()
    raw_input = st.text_area("SCAN INVOICE / NOTES", height=150, placeholder="Type delay notes or scan doc...")

    if st.button("SUBMIT POD"):
        if raw_input:
            with st.spinner("UPLOADING TO SHADOW NODE..."):
                # 1. THE EDGE RESTRICTION MAP
                # The driver performs the scrape LOCALLY on the edge
                node = UniversalTranslator()
                artifact = node.ingest(raw_input, "DRIVER_MOBILE_APP")
                
                time.sleep(1) # Network simulation
                
            st.success("✅ POD UPLOADED")
            st.info(f"Artifact Hash: {artifact.split('/')[-1]}")
            st.markdown("---")
            st.caption("Manager has been notified of status change.")
        else:
            st.warning("Please enter data first.")

if __name__ == "__main__":
    main()