# ======================================================
# F1 TELEMETRY DASHBOARD
# Interactive Streamlit dashboard for telemetry analysis
# ======================================================

import streamlit as st
import fastf1
import matplotlib.pyplot as plt
import os

# ------------------------------
# Enable FastF1 cache
# ------------------------------

if not os.path.exists("cache"):
    os.makedirs("cache")

fastf1.Cache.enable_cache("cache")

# ------------------------------
# Dashboard Title
# ------------------------------

st.title("🏎️ F1 Telemetry Analytics Dashboard")

st.write("Compare telemetry data between two drivers.")

# ------------------------------
# User Inputs
# ------------------------------

year = st.selectbox("Season", [2023, 2024])
race = st.text_input("Race Name", "Monaco")
session_type = st.selectbox("Session", ["R", "Q", "FP1"])

driver1 = st.text_input("Driver 1", "VER")
driver2 = st.text_input("Driver 2", "HAM")

# ------------------------------
# Load Data Button
# ------------------------------

if st.button("Run Analysis"):

    st.write("Loading session data...")

    session = fastf1.get_session(year, race, session_type)
    session.load()

    # fastest laps
    lap1 = session.laps.pick_drivers(driver1).pick_fastest()
    lap2 = session.laps.pick_drivers(driver2).pick_fastest()

    tel1 = lap1.get_car_data().add_distance()
    tel2 = lap2.get_car_data().add_distance()

    # ------------------------------
    # Plot Speed Comparison
    # ------------------------------

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(tel1["Distance"], tel1["Speed"], label=driver1)
    ax.plot(tel2["Distance"], tel2["Speed"], label=driver2)

    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Speed (km/h)")
    ax.set_title("Telemetry Speed Comparison")

    ax.legend()
    ax.grid()

    st.pyplot(fig)

    st.success("Analysis Complete")