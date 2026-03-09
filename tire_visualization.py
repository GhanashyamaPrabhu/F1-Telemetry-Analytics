import fastf1
import matplotlib.pyplot as plt

session = fastf1.get_session(2024, 'Monaco', 'R')
session.load()

driver = session.laps.pick_driver('VER')

stints = driver.groupby('Stint')

for stint, laps in stints:
    compound = laps['Compound'].iloc[0]
    plt.barh("VER", len(laps), left=laps['LapNumber'].min(), label=compound)

plt.xlabel("Lap Number")
plt.title("Tire Strategy – Verstappen")
plt.show()