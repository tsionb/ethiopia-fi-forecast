import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Trends Analysis")
st.markdown("### Historical Trends and Patterns")

# Sample trend chart
trend_data = pd.DataFrame({
    'Year': [2011, 2014, 2017, 2021, 2024],
    'Account Ownership': [14, 22, 35, 46, 49],
    'Digital Payments': [5, 12, 22, 30, 35]
})

fig = px.line(
    trend_data,
    x='Year',
    y=['Account Ownership', 'Digital Payments'],
    title='Historical Trends',
    markers=True
)

st.plotly_chart(fig, use_container_width=True)