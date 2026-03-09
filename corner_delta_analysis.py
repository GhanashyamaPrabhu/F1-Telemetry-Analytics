# ======================================================
# CORNER DELTA ANALYSIS
# Compare performance across track distance
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

session = fastf1.get_session(2024, "Monaco", "Q")
session.load()

driver1 = "VER"
driver2 = "HAM"

# ------------------------------
# Get fastest laps
# ------------------------------

lap1 = session.laps.pick_drivers(driver1).pick_fastest()
lap2 = session.laps.pick_drivers(driver2).pick_fastest()

tel1 = lap1.get_car_data().add_distance()
tel2 = lap2.get_car_data().add_distance()

# ------------------------------
# Interpolate speeds
# (align telemetry distance)
# ------------------------------

speed2_interp = np.interp(
    tel1["Distance"],
    tel2["Distance"],
    tel2["Speed"]
)

# speed delta
delta_speed = tel1["Speed"] - speed2_interp

# ------------------------------
# Plot delta
# ------------------------------

plt.figure(figsize=(12,6))

plt.plot(tel1["Distance"], delta_speed)

plt.axhline(0, linestyle="--")

plt.xlabel("Track Distance (m)")
plt.ylabel("Speed Delta (km/h)")
plt.title("Corner Performance Delta (VER vs HAM)")

plt.grid()

plt.show()