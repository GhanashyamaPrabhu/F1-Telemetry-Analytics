# F1 Telemetry Analytics

This project analyzes Formula 1 race telemetry and performance data using the FastF1 Python library.

The goal of this project is to explore motorsport data analytics and understand driver behavior using real Formula 1 telemetry data.

---

## Project Overview

Formula 1 cars generate large amounts of telemetry data during every lap. Engineers use this data to understand how drivers interact with the car and track.

This project uses the FastF1 API to download and analyze official Formula 1 timing and telemetry data.

The analysis includes:

- Race pace comparison
- Tire strategy visualization
- Driver telemetry comparison

---

## Features

### 1. Race Pace Analysis

This analysis compares lap times between drivers across an entire race session.

The visualization shows:

- Lap number vs lap time
- Performance consistency
- Tire degradation trends

Script used:

F1_analysis.py

---

### 2. Tire Strategy Visualization

This script analyzes the tire compounds used by drivers and how long each tire stint lasted.

The visualization shows:

- Tire compound used
- Stint lengths
- Strategy differences between drivers

Script used:

tire_visualization.py

---

### 3. Telemetry Comparison

Telemetry data is used to compare two drivers during their fastest laps.

The comparison includes:

- Speed vs distance
- Throttle input vs distance
- Brake application vs distance
- Gear selection vs distance

This type of analysis is commonly used by Formula 1 race engineers.

Script used:

telemetry_analysis.py

---

## Technologies Used

Python

Libraries used:

- FastF1
- Pandas
- Matplotlib
- NumPy

---

## Project Structure

F1-Telemetry-Analytics

F1_analysis.py  
telemetry_analysis.py  
tire_visualization.py  
README.md  
.gitignore  

---

## Installation

Clone the repository

git clone https://github.com/GhanashyamaPrabhu/F1-Telemetry-Analytics.git

Move into the project folder

cd F1-Telemetry-Analytics

Create a virtual environment

python -m venv f1_env

Activate the environment (Mac/Linux)

source f1_env/bin/activate

Install dependencies

pip install fastf1 pandas matplotlib numpy

---

## Running the Scripts

Race pace analysis

python F1_analysis.py

Telemetry comparison

python telemetry_analysis.py

Tire strategy visualization

python tire_visualization.py

---

## Future Improvements

Possible improvements to the project include:

- Track maps colored by speed
- Corner-by-corner lap time delta analysis
- Driver performance heatmaps
- Pit stop strategy analysis
- Interactive telemetry dashboards

---

## Motivation

Formula 1 provides one of the most interesting datasets in sports analytics.

This project explores how data science techniques can be used to analyze driver performance, race strategy, and telemetry data.

---

## Acknowledgments

Data provided using the FastF1 Python library.

FastF1 Documentation

https://theoehrly.github.io/Fast-F1/
