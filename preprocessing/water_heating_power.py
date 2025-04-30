#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 10:00:19 2025

@author: claudia
"""

import pandas as pd
import numpy as np

# === Load daily ambient temperatures from CSV ===
temp_file_path = "data/Highlands_Daily_temp.csv" # !!!! CHANGE ---------------
df_temp = pd.read_csv(temp_file_path)
daily_ambient_temp = df_temp["Temperature"].values

daily_ambient_temp_K = daily_ambient_temp + 273.15
annual_mean_temp_K = np.mean(daily_ambient_temp_K)
coldest_day = int(np.argmin(daily_ambient_temp)) + 1

# === Physical parameters for water heating ===
cp_water = 4.18         # kJ/kg·K - specific heat of water
mass_flow = 0.08        # kg/s - water flow rate for a shower
target_temp = 40        # °C - desired hot water temperature

# === Calculate groundwater temperature ===
days = np.arange(1, 366)
groundwater_temp_K = daily_ambient_temp_K - 3 * np.cos((2 * np.pi / 365) * (days - coldest_day))
groundwater_temp_C = groundwater_temp_K - 273.15

# === Thermal power required to heat water, per day (in watts) ===
power_profile_W = mass_flow * cp_water * (target_temp - groundwater_temp_C) * 1000

#Save to CSV
power_profile_W.to_csv("power_profile.csv", header=["power_W"])