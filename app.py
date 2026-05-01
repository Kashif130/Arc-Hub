import streamlit as st
import os

st.set_page_config(
    page_title="ArcOS Testnet Hub",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide all streamlit chrome
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    .stApp { margin: 0; padding: 0; background: #03080f; }
</style>
""", unsafe_allow_html=True)

# Read HTML file
html_path = os.path.join(os.path.dirname(__file__), "arc_app.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Use st.html (Streamlit 1.32+) instead of components.html
# st.html does NOT use iframe — renders directly in page
# This allows window.ethereum (MetaMask) to work
st.html(html_content)
