# MAIN DASHBOARD - app.py
import streamlit as st

# Page config
st.set_page_config(
    page_title="Ethiopia Financial Inclusion",
    page_icon="📈",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Select a page from the list below:")

# Main content
st.markdown('<h1 class="main-header"> Welcome to Ethiopia Financial Inclusion Dashboard</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.success("""
    ###  What's Available:
    
    1.  Overview - Key metrics and introduction
    2.  Trends - Historical analysis
    3.  Forecasts - Future predictions
    4.  Analysis - Interactive tools
    
    ###  How to Use:
    - Select pages from the sidebar
    - Interact with charts and filters
    - Download data as needed
    """)

with col2:
    st.info("""
    ###  The Data:
    - Account Ownership: 2011-2024
    - Mobile Money Growth
    - Digital Payment Trends
    - Forecasts: 2025-2027
    
    ###  Project Goal:
    Track Ethiopia's progress toward:
    - 60% account ownership by 2027
    - Increased digital payment usage
    - Financial inclusion for all
    """)

# Quick metrics
st.markdown("---")
st.subheader(" At a Glance")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Current Accounts", "49%", "+35% since 2011")
    
with m2:
    st.metric("Mobile Money", "64M", "Telebirr + M-Pesa")
    
with m3:
    st.metric("Digital Growth", "35%", "+30% since 2011")
    
with m4:
    st.metric("Target 2027", "60%", "11% to go")

# Footer
st.markdown("---")
st.caption("Dashboard created • Use sidebar to navigate")