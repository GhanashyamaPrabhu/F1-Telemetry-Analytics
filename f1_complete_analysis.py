import fastf1
import matplotlib.pyplot as plt
import os

# Create cache folder
if not os.path.exists("cache"):
    os.makedirs("cache")

fastf1.Cache.enable_cache("cache")

# Load race session
session = fastf1.get_session(2024, "Monaco", "R")
session.load()

laps = session.laps

driver1 = "VER"
driver2 = "HAM"

ver = laps.pick_drivers(driver1).dropna(subset=["LapTime"])
ham = laps.pick_drivers(driver2).dropna(subset=["LapTime"])

ver_times = ver["LapTime"].dt.total_seconds()
ham_times = ham["LapTime"].dt.total_seconds()

# -----------------------------
# Race Pace Comparison
# -----------------------------

plt.figure(figsize=(10,6))

plt.plot(ver["LapNumber"], ver_times, label="Verstappen")
plt.plot(ham["LapNumber"], ham_times, label="Hamilton")

plt.xlabel("Lap Number")
plt.ylabel("Lap Time (seconds)")
plt.title("Race Pace Comparison")
plt.legend()
plt.grid()

plt.show()

# -----------------------------
# Telemetry Comparison
# -----------------------------

ver_fast = laps.pick_drivers(driver1).pick_fastest()
ham_fast = laps.pick_drivers(driver2).pick_fastest()

ver_tel = ver_fast.get_car_data().add_distance()
ham_tel = ham_fast.get_car_data().add_distance()

fig, ax = plt.subplots(4,1, figsize=(12,10), sharex=True)

# Speed
ax[0].plot(ver_tel["Distance"], ver_tel["Speed"], label="VER")
ax[0].plot(ham_tel["Distance"], ham_tel["Speed"], label="HAM")
ax[0].set_ylabel("Speed")
ax[0].set_title("Speed Comparison")
ax[0].legend()

# Throttle
ax[1].plot(ver_tel["Distance"], ver_tel["Throttle"])
ax[1].plot(ham_tel["Distance"], ham_tel["Throttle"])
ax[1].set_ylabel("Throttle")

# Brake
ax[2].plot(ver_tel["Distance"], ver_tel["Brake"])
ax[2].plot(ham_tel["Distance"], ham_tel["Brake"])
ax[2].set_ylabel("Brake")

# Gear
ax[3].plot(ver_tel["Distance"], ver_tel["nGear"])
ax[3].plot(ham_tel["Distance"], ham_tel["nGear"])
ax[3].set_ylabel("Gear")
ax[3].set_xlabel("Distance")

plt.suptitle("Telemetry Comparison")

plt.show()

# -----------------------------
# Race Position Progression
# -----------------------------

plt.figure(figsize=(10,6))

plt.plot(ver["LapNumber"], ver["Position"], label="Verstappen")
plt.plot(ham["LapNumber"], ham["Position"], label="Hamilton")

plt.gca().invert_yaxis()

plt.xlabel("Lap Number")
plt.ylabel("Position")
plt.title("Race Position Progression")

plt.legend()
plt.grid()

plt.show()

# -----------------------------
# Track Map Colored by Speed
# -----------------------------

lap = laps.pick_drivers(driver1).pick_fastest()

telemetry = lap.get_car_data().add_distance()
pos = lap.get_pos_data()

data = telemetry.merge(pos, left_index=True, right_index=True)

plt.figure(figsize=(8,8))

plt.scatter(
    data["X"],
    data["Y"],
    c=data["Speed"],
    cmap="viridis",
    s=8
)

plt.colorbar(label="Speed (km/h)")
plt.title("Track Speed Map")

plt.axis("equal")

plt.show()
