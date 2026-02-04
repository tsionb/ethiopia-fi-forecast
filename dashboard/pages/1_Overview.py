import streamlit as st
import pandas as pd
import plotly.express as px

st.title(" Overview")
st.markdown("### Key Metrics and Dashboard Introduction")

# Add overview content
col1, col2 = st.columns(2)

with col1:
    st.metric("Account Ownership", "49%", "+3%")
    st.metric("Digital Payments", "35%", "Growing")
    
with col2:
    st.metric("Mobile Money Users", "64M", "Telebirr + M-Pesa")
    st.metric("P2P vs ATM", "1.2x", "Digital > Cash")

st.info("""
This dashboard shows Ethiopia's financial inclusion progress.
Use the sidebar to navigate between sections.
""")