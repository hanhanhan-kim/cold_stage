#!/usr/bin/env python3

"""
Compare measured temperatures vs setpoint of bang-bang control loop.
"""

import matplotlib.pyplot as plt
import bokeh.palettes
import pandas as pd


plt.style.use("ggplot")
palette = bokeh.palettes.Paired[6]

df = pd.read_csv("../data/bangbang_loop/setpoint_17c.csv", 
                 names=["time", "temperature (C)"])

df["time"] =  pd.to_datetime(df["time"])
    
# Plot:
plt.figure(num=None, figsize=(10, 5))
plt.plot(df["time"], df["temperature (C)"], 
         color=palette[0], 
         linewidth=3,
         label="measured temperatures")
plt.axhline(y=17, color=palette[1], linestyle="--", alpha=0.8, label="setpoint (17 C)")
plt.title("bang-bang control")
plt.xlabel("time")
plt.ylabel("temperature (C)")
plt.legend()
plt.show()