#!/usr/bin/env python3

"""
Generate timeseries plots of temperature readings from DS18B20 sensor, 
for each Peltier PWM duty cycle.
"""

import glob 
from os.path import split

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

csvs = sorted(glob.glob("data/feedforward_calibration/*.csv"))
dfs = [pd.read_csv(csv, names=["time", "temperature (C)"]) for csv in csvs]

for df, csv in zip(dfs, csvs):
    
    # Convert time string to datetime object:
    df["time"] =  pd.to_datetime(df["time"])
    
    # Plot:
    plt.figure(num=None, figsize=(12, 4), dpi=100, facecolor='w', edgecolor='k')
    plt.plot(df["time"], df["temperature (C)"])
    plt.xlabel("time")
    plt.ylabel("temperature (C)")
    _, title = split(csv)
    plt.title(f"{title}".replace("_", " ").replace(".csv", ""))
    plt.grid(True)
    plt.show()