# ======================================================
# TIRE DEGRADATION ANALYSIS
# Model lap time increase due to tire wear
# ======================================================

import fastf1
import matplotlib.pyplot as plt
import numpy as np
import os

# ------------------------------
# Enable cache
# ------------------------------

if not os.path.exists("cache"):
    os.makedirs("cache")

fastf1.Cache.enable_cache("cache")

# ------------------------------
# Load session
# ------------------------------

session = fastf1.get_session(2024, "Monaco", "R")
session.load()

laps = session.laps

driver = "VER"

driver_laps = laps.pick_drivers(driver).dropna(subset=["LapTime"])

# ------------------------------
# Convert lap time to seconds
# ------------------------------

lap_numbers = driver_laps["LapNumber"]
lap_times = driver_laps["LapTime"].dt.total_seconds()

# ------------------------------
# Linear regression
# ------------------------------

coeff = np.polyfit(lap_numbers, lap_times, 1)
trend = np.poly1d(coeff)

# ------------------------------
# Plot degradation
# ------------------------------

plt.figure(figsize=(10,6))

plt.scatter(lap_numbers, lap_times, label="Actual Lap Times")

plt.plot(
    lap_numbers,
    trend(lap_numbers),
    color="red",
    label="Degradation Trend"
)

plt.xlabel("Lap Number")
plt.ylabel("Lap Time (seconds)")
plt.title("Tire Degradation Model")

plt.legend()
plt.grid()

plt.show()