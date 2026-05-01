import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ArcOS Testnet Hub",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
    .stApp { margin: 0; padding: 0; }
    iframe { width: 100% !important; border: none !important; }
</style>
""", unsafe_allow_html=True)

with open("arc_app.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=3500, scrolling=True)
