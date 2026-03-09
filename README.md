# F1 Telemetry Analytics

A Python-based motorsport analytics project that explores **Formula 1 telemetry, race strategy, and driver performance** using the **FastF1 data API**.

This project demonstrates how **data science and engineering techniques can be applied to real Formula 1 race data** to analyze driver behavior, race strategy, and vehicle performance.

The analyses implemented here replicate several workflows used by **Formula 1 race engineers and motorsport data analysts**.

---

# Project Objective

Formula 1 cars generate **thousands of telemetry data points per second** during a race.

Telemetry data includes:

- Speed
- Throttle input
- Brake pressure
- Gear selection
- Lap times
- Tire compounds
- Position tracking

Formula 1 teams analyze this data to understand:

- Driver performance
- Braking points
- Acceleration zones
- Tire degradation
- Race strategy effectiveness

This project uses the **FastF1 Python library** to download official Formula 1 telemetry and timing data and perform engineering-style analysis.

---

# Key Analyses Implemented

The project includes multiple motorsport analytics techniques.

---

# 1. Race Pace Analysis

Script:

```
F1_analysis.py
```

This script compares **lap times between drivers across an entire race session**.

The visualization shows:

- Lap number vs lap time
- Driver performance consistency
- Pace differences between drivers
- Tire degradation effects during the race

Race engineers use this analysis to determine:

- Which driver has stronger race pace
- How performance evolves during the race
- Whether tire wear affects lap times

Example insight:

Driver A may start faster but gradually lose pace as tire performance drops.

---

# 2. Tire Strategy Visualization

Script:

```
tire_visualization.py
```

Formula 1 race strategy heavily depends on **tire compound management**.

Different compounds have different characteristics:

| Compound | Grip | Durability |
|--------|--------|--------|
| Soft | High | Low |
| Medium | Medium | Medium |
| Hard | Lower | High |

This script analyzes:

- Tire compound usage
- Tire stint lengths
- Strategic differences between drivers

Visualization example:

Driver  
|---- Soft ----|---- Medium ----|

This analysis helps identify:

- Pit stop timing
- Optimal tire strategies
- Strategy differences between teams

---

# 3. Telemetry Comparison

Script:

```
telemetry_analysis.py
```

Telemetry data is used to compare **two drivers during their fastest laps**.

The comparison includes:

- Speed vs track distance
- Throttle input vs distance
- Brake application vs distance
- Gear selection vs distance

These plots reveal:

- Braking points
- Acceleration zones
- Corner exit speeds
- Differences in driving style

This type of telemetry analysis is commonly used by **Formula 1 performance engineers**.

---

# 4. Corner-by-Corner Performance Delta

Script:

```
corner_delta_analysis.py
```

This analysis identifies **where one driver gains or loses performance across the track**.

Method used:

1. Extract telemetry data for each driver's fastest lap
2. Align telemetry using track distance interpolation
3. Compute speed difference across the lap

Formula:

```
Delta = Speed_driver1 − Speed_driver2
```

Interpretation:

- Positive delta → Driver 1 faster
- Negative delta → Driver 2 faster

This reveals:

- Which driver is faster in specific corners
- Where lap time gains occur
- Differences in braking and cornering techniques

This technique is widely used in **professional motorsport telemetry analysis**.

---

# 5. Tire Degradation Modeling

Script:

```
tire_degradation.py
```

Tire performance decreases as laps increase due to wear.

This script models **tire degradation using regression analysis**.

Steps performed:

1. Extract lap times for a driver
2. Convert lap times to seconds
3. Fit a regression model

Concept:

```
Lap Time = Base Pace + Tire Wear
```

The slope of the regression line indicates **tire degradation rate**.

Example result:

```
+0.08 seconds per lap degradation
```

This analysis helps estimate:

- Optimal pit stop timing
- Tire performance drop-off
- Race strategy adjustments

---

# 6. Interactive Telemetry Dashboard

Script:

```
dashboard.py
```

An interactive dashboard built using **Streamlit**.

Users can dynamically select:

- Season
- Race
- Session type
- Drivers

The dashboard automatically generates telemetry comparisons.

Features include:

- Interactive driver comparison
- Dynamic telemetry visualization
- Real-time race data loading

Run the dashboard using:

```
streamlit run dashboard.py
```

This launches a browser-based telemetry analytics interface.

---

# Technologies Used

Programming Language:

```
Python
```

Core Libraries:

| Library | Purpose |
|------|------|
| FastF1 | Access official Formula 1 telemetry data |
| Pandas | Data manipulation |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Streamlit | Interactive dashboard |

---

# Project Structure

```
F1-Telemetry-Analytics
│
├── F1_analysis.py
├── telemetry_analysis.py
├── tire_visualization.py
├── corner_delta_analysis.py
├── tire_degradation.py
├── dashboard.py
├── README.md
└── .gitignore
```

---

# Installation

Clone the repository

```
git clone https://github.com/GhanashyamaPrabhu/F1-Telemetry-Analytics.git
```

Move into the project directory

```
cd F1-Telemetry-Analytics
```

Create a virtual environment

```
python -m venv f1_env
```

Activate the virtual environment

Mac / Linux

```
source f1_env/bin/activate
```

Install dependencies

```
pip install fastf1 pandas matplotlib numpy streamlit
```

---

# Running the Scripts

Race pace analysis

```
python F1_analysis.py
```

Telemetry comparison

```
python telemetry_analysis.py
```

Tire strategy visualization

```
python tire_visualization.py
```

Corner delta analysis

```
python corner_delta_analysis.py
```

Tire degradation model

```
python tire_degradation.py
```

Interactive telemetry dashboard

```
streamlit run dashboard.py
```

---

# Future Improvements

Possible extensions to this project include:

- Track maps colored by speed
- Racing line visualization
- Sector performance heatmaps
- Automatic braking point detection
- Pit stop strategy simulation
- Machine learning models predicting lap times
- Driver style classification using telemetry

---

# Motivation

Formula 1 is one of the most **data-intensive environments in professional sports**.

Teams rely heavily on **data science, telemetry analysis, and simulation models** to make performance and strategy decisions.

This project explores how **data science techniques can be applied to motorsport telemetry data** to better understand driver performance and race strategy.

---

# Acknowledgments

Telemetry and timing data provided by the **FastF1 Python Library**.

Documentation:

https://theoehrly.github.io/Fast-F1/
