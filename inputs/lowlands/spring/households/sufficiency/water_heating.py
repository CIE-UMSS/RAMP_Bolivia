from ramp.core.core import User
import pandas as pd

User_list = []


HWH = User("household water heating", 1)  # Create user with ID = 1
User_list.append(HWH)

HH_shower_P = pd.read_csv("data/LL_power_profile_water_heating.csv")

HWH_shower = HWH.add_appliance(1, HH_shower_P, 2, 30, 0.2, 3, thermal_P_var = 0.4)
HWH_shower.windows([360, 540], [1080, 1200], 0.2)


