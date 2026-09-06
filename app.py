
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import math

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="SolarSmart AI",
    page_icon="🌞",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🌞 SolarSmart AI")
st.subheader("Intelligent Solar System Recommendation")

st.write(
    "Enter your electricity consumption and basic site information "
    "to get a preliminary solar system recommendation."
)

# -----------------------------
# Inputs
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    monthly_consumption = st.number_input(
        "Monthly Electricity Consumption (kWh)",
        min_value=50.0,
        value=550.0,
        step=50.0
    )

    location = st.text_input(
        "Location",
        value="Lahore, Pakistan"
    )

    roof_area = st.number_input(
        "Available Roof Area (sq.ft)",
        min_value=50.0,
        value=500.0,
        step=50.0
    )

with col2:
    budget = st.number_input(
        "Budget (PKR)",
        min_value=0.0,
        value=700000.0,
        step=50000.0
    )

    system_type = st.selectbox(
        "System Type",
        ["On-Grid", "Off-Grid", "Hybrid"]
    )

    battery_required = st.selectbox(
        "Battery Required?",
        ["No", "Yes"]
    )

    backup_hours = st.number_input(
        "Required Backup Hours",
        min_value=0.0,
        value=4.0,
        step=1.0
    )

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("🔍 Analyze Solar System", type="primary"):
