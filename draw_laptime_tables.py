# importing the required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import fastf1
import fastf1.plotting

# Finding the data for the race we want to analyse
session = fastf1.get_session(2026, "Singaor", "R")
session.load()

""" laps = session.laps

# Select only the useful columns
lap_table = laps[['Driver', 'LapNumber', 'LapTime', 'Compound']]

# Sort by driver and lap number
lap_table = lap_table.sort_values(['Driver', 'LapNumber'])

print(lap_table)
 """
