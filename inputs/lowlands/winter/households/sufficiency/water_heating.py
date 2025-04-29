from ramp.core.core import User
import numpy as np
import pandas as pd

User_list = []

# === Load daily ambient temperatures from CSV ===
temp_file_path = "data/Lowands_Daily_temp.csv" # !!!! CHANGE ---------------
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

HH = User("household hygiene", 1)  # Create user with ID = 1
User_list.append(HH)

HH_shower = HH.add_appliance(1, power_profile_W, 2, 30, 0.2, 3, thermal_P_var = 0.4)
HH_shower.windows([360, 540], [1080, 1200], 0.2)


