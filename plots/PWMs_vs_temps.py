#!/usr/bin/env python3

"""
Interpolate a line through Peltier PWM vs. DS18B20 temperature readings.
"""

import matplotlib.pyplot as plt
import bokeh.palettes
from scipy import stats
import pandas as pd


def main():
    
    plt.style.use("ggplot")
    palette = bokeh.palettes.Paired[6]

    df = pd.read_csv("../data/PWMs_vs_temps.csv", 
                    names=["PWM", "temperature (C)"])

    # Perform linear regression:
    x = df["temperature (C)"]
    y = df["PWM"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    # Plot:
    plt.figure(num=None, figsize=(10, 7), dpi=100)
    plt.plot(x, y, 
            'o', 
            color=palette[4], 
            markersize=14, 
            alpha=0.8, 
            label='measured temperatures')
    plt.plot(x, intercept + slope*x, "--",
            color=palette[5], 
            alpha=0.9,
            linewidth=2, 
            label='fitted line')
    plt.xlabel("steady state temperature (C)") 
    plt.ylabel("PWM value (from 8-bit res)")
    plt.legend()
    plt.text(2, 10, f"PWM value = {slope:.2f} * temperature + {intercept:.2f}", fontsize=12)
    plt.savefig("PWMs_vs_temps.png")


if __name__ == "__main__":
    main()