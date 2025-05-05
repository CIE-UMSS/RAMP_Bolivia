from core import User
import numpy as np
import pandas as pd

User_list = []

# === Load daily ambient temperatures from CSV ===
temp_file_path = "Data/Lowlands_Daily_temp.csv" # !!!! CHANGE ---------------
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


WH_shower = WH.add_appliance(1,power_profile_W,2,15,0.1,3, thermal_p_var = 0.2, occasional_use=0.33)
WH_shower.windows([360,540],[1080,1260],0.2)




