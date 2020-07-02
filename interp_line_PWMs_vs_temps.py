#!/usr/bin/env python3

"""
Interpolate a line through Peltier PWM vs. DS18B20 temperature readings.
"""

import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


df = pd.read_csv("data/PWMs_vs_temps.csv", names=["PWM", "temperature (C)"])

# Perform linear regression:
x = df["temperature (C)"]
y = df["PWM"]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Plot:
plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.xlabel("temperature (C)")
plt.ylabel("PWM value (from 8-bit res)")
plt.legend()
plt.text(2, 0, f"PWM value = {slope:.2f}*temperature + {intercept:.2f}")
plt.show()