import fastf1
import matplotlib.pyplot as plt
import os

# create cache folder if it doesn't exist
if not os.path.exists("cache"):
    os.makedirs("cache")

fastf1.Cache.enable_cache('cache')

# Load session
session = fastf1.get_session(2024, 'Monaco', 'R')
session.load()

laps = session.laps

# select drivers
ver = laps.pick_driver('VER')
ham = laps.pick_driver('HAM')

# convert lap times to seconds
ver_lap_times = ver['LapTime'].dt.total_seconds()
ham_lap_times = ham['LapTime'].dt.total_seconds()

# plot
plt.figure(figsize=(10,6))

plt.plot(ver['LapNumber'], ver_lap_times,
         label='Max Verstappen', marker='o')

plt.plot(ham['LapNumber'], ham_lap_times,
         label='Lewis Hamilton', marker='o')

plt.xlabel('Lap Number')
plt.ylabel('Lap Time (seconds)')
plt.title('Race Pace Comparison: Verstappen vs Hamilton — Monaco 2024')
plt.legend()
plt.grid()

plt.show()