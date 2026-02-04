import streamlit as st
import pandas as pd
import plotly.express as px

st.title(" Forecasts")
st.markdown("### Future Predictions")

# Forecast scenario selector
scenario = st.radio(
    "Select forecast scenario:",
    ["Base", "Optimistic", "Pessimistic"]
)

# Forecast data
forecast_data = pd.DataFrame({
    'Year': [2024, 2025, 2026, 2027],
    'Base': [49, 52, 55, 58],
    'Optimistic': [49, 54, 58, 62],
    'Pessimistic': [49, 50, 52, 54]
})

# Show selected scenario
selected_data = forecast_data[['Year', scenario]]
st.dataframe(selected_data)

# Chart
fig = px.line(
    forecast_data,
    x='Year',
    y=['Base', 'Optimistic', 'Pessimistic'],
    title='Forecast Scenarios',
    markers=True
)

st.plotly_chart(fig, use_container_width=True)