import fastf1
import matplotlib.pyplot as plt
import os

# Create cache folder
if not os.path.exists("cache"):
    os.makedirs("cache")

fastf1.Cache.enable_cache("cache")

# Load session
session = fastf1.get_session(2024, 'Monaco', 'Q')
session.load()

# Fastest laps
ver_lap = session.laps.pick_driver('VER').pick_fastest()
ham_lap = session.laps.pick_driver('HAM').pick_fastest()

# Telemetry data
ver_tel = ver_lap.get_car_data().add_distance()
ham_tel = ham_lap.get_car_data().add_distance()

# Create 4 stacked plots
fig, ax = plt.subplots(4, 1, figsize=(12,10), sharex=True)

# SPEED
ax[0].plot(ver_tel['Distance'], ver_tel['Speed'], label="Verstappen")
ax[0].plot(ham_tel['Distance'], ham_tel['Speed'], label="Hamilton")
ax[0].set_ylabel("Speed (km/h)")
ax[0].set_title("Speed Comparison")
ax[0].legend()
ax[0].grid()

# THROTTLE
ax[1].plot(ver_tel['Distance'], ver_tel['Throttle'], label="Verstappen")
ax[1].plot(ham_tel['Distance'], ham_tel['Throttle'], label="Hamilton")
ax[1].set_ylabel("Throttle (%)")
ax[1].set_title("Throttle Application")
ax[1].grid()

# BRAKE
ax[2].plot(ver_tel['Distance'], ver_tel['Brake'], label="Verstappen")
ax[2].plot(ham_tel['Distance'], ham_tel['Brake'], label="Hamilton")
ax[2].set_ylabel("Brake")
ax[2].set_title("Brake Usage")
ax[2].grid()

# GEAR
ax[3].plot(ver_tel['Distance'], ver_tel['nGear'], label="Verstappen")
ax[3].plot(ham_tel['Distance'], ham_tel['nGear'], label="Hamilton")
ax[3].set_ylabel("Gear")
ax[3].set_xlabel("Distance (m)")
ax[3].set_title("Gear Selection")
ax[3].grid()

plt.suptitle("Telemetry Comparison — Verstappen vs Hamilton (Monaco Qualifying)")

plt.tight_layout()
plt.show()