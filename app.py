import streamlit as st
from components.custom_ui import apply_custom_theme

st.set_page_config(page_title="Geo Alert Pro", layout="wide")
apply_custom_theme()

st.markdown('<div class="main-block">', unsafe_allow_html=True)
st.markdown('<div class="app-title">Geo Alert Pro</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Smart geofence tracking with real-time visualization and distance-based alerts.</div>',
    unsafe_allow_html=True,
)

st.write("Use the **Tracking** page from the sidebar to:")
st.markdown(
    """
- 🔍 Search or tap a destination on the map  
- 📏 Set your alert radius  
- 🛰 Track your live position  
- 🚨 Get alerted when you enter the radius  
    """
)

st.info("For accurate GPS and permission prompts, run this app on HTTPS (like Streamlit Cloud).")
st.markdown('</div>', unsafe_allow_html=True)
