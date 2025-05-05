from ramp.core.core import User
import pandas as pd
import os

User_list = []

HWH = User("household water heating", 1)  # Create user with ID = 1
User_list.append(HWH)


current_dir = os.path.dirname(__file__)  # /inputs/highlands/fall/households/sufficiency
project_root = os.path.abspath(os.path.join(current_dir, "..", "..", "..", "..", ".."))  # RAMP_Bolivia
csv_path = os.path.join(project_root, "data", "HL_power_profile_water_heating.csv")


HH_shower_P = pd.read_csv(csv_path)


HWH_shower = HWH.add_appliance(1, HH_shower_P, 2, 30, 0.2, 3, thermal_p_var=0.4)
HWH_shower.windows([360, 540], [1080, 1200], 0.2)


