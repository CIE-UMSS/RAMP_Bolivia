from core import User
import numpy as np
import pandas as pd

User_list = []

# === Load daily ambient temperatures from CSV ===
temp_file_path = "Data/Highlands_Daily_temp.csv" #!!!! CHANGE ---------------
df_temp = pd.read_csv(temp_file_path)
daily_ambient_temp = df_temp["Temperature"].values

coldest_day = int(np.argmin(daily_ambient_temp)) + 1

# === Physical parameters for water heating ===
cp_water = 4.18         # kJ/kg·K - specific heat of water
mass_flow = 0.05        # kg/s - water flow rate for a shower
target_temp = 40        # °C - desired hot water temperature

# === Calculate groundwater temperature ===
days = np.arange(1, 366)
groundwater_temp = daily_ambient_temp - 3 * np.cos((2 * np.pi / 365) * (days - coldest_day))

# === Thermal power required to heat water, per day (in watts) ===
power_profile_W = mass_flow * cp_water * (target_temp - groundwater_temp) * 1000

WH = User("Water Heating", 1)  # Create user with ID = 1
User_list.append(WH)

WH_shower = WH.Appliance(
    number=1,                # One shower per user
    power=power_profile_W,   # Daily power profile (365 values)
    num_windows=2,           # Two usage windows per day
    func_time=15,            # Each shower lasts 15 minutes
    func_cycle=3,
    occasional_use=1,        # Used daily (probability = 1)
    thermal_P_var=0.1        # 10% thermal power variability
)

# === Define time windows when the shower may be used ===
# Morning: 6:30–9:00 (390–540 minutes)
# Evening: 18:00–20:00 (1080–1200 minutes)
WH_shower.windows([390, 540], [1080, 1200], 0.35)


