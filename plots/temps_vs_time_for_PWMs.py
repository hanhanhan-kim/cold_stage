#!/usr/bin/env python3

"""
Generate timeseries plots of temperature readings from DS18B20 sensor, 
for each Peltier PWM duty cycle.
"""

import glob 
from os.path import split

import matplotlib.pyplot as plt
import bokeh.palettes
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

plt.style.use("ggplot")
colours = bokeh.palettes.Blues256[150::-15]

csvs = sorted(glob.glob("../data/feedforward_calibration/*.csv"))
dfs = [pd.read_csv(csv, names=["time", "temperature (C)"]) for csv in csvs]

for df, csv, colour in zip(dfs, csvs, colours):

    # Convert time string to datetime object:
    df["time"] =  pd.to_datetime(df["time"])
    
    # Plot:
    plt.figure(num=None, figsize=(10, 5))
    plt.plot(df["time"], df["temperature (C)"], color=colour, linewidth=3)
    plt.xlabel("time")
    plt.ylabel("temperature (C)")
    _, title = split(csv)
    title = title.replace("_", " ").replace(".csv", "").upper()
    plt.title(f"{title}")
    fname = title.replace(" ", "_")
    plt.savefig(f"temps_vs_time_for_{fname}.png")