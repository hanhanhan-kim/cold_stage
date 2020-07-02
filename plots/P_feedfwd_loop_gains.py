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


plt.style.use("ggplot")
palette = bokeh.palettes.Paired[6]

csvs = sorted(glob.glob("../data/P_feedfwd_loop_gains/*.csv"))
dfs = [pd.read_csv(csv, names=["time", "temperature (C)"]) for csv in csvs]

for df, csv in zip(dfs, csvs):

    # Convert time string to datetime object:
    df["time"] =  pd.to_datetime(df["time"])
    
    # Plot:
    plt.figure(num=None, figsize=(10, 5))
    plt.plot(df["time"], df["temperature (C)"], color=palette[0], linewidth=3, label="measured temperatures")
    plt.axhline(y=17, color=palette[1], linestyle="--", alpha=0.8, label="setpoint (17 C)")
    plt.xlabel("time")
    plt.ylabel("temperature (C)")
    _, title = split(csv)
    title = title.replace("_", " ").replace(".csv", "")
    plt.title(f"{title} in P with feedforward control")
    fname = title.replace(" ", "_")
    plt.show()
    # plt.savefig(f"temps_vs_time_for_gains_of_P_feedfwd/temps_vs_time_for_{fname}.png")