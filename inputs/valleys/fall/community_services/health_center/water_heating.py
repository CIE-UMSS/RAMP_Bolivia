from ramp.core.core import User
import numpy as np
import pandas as pd
import os

User_list = []

HCWH = User("Health Center Water Heating", 1)  # Create user with ID = 1
User_list.append(HCWH)

current_dir = os.path.dirname(__file__)  # /inputs/highlands/fall/households/sufficiency
project_root = os.path.abspath(os.path.join(current_dir, "..", "..", "..", "..", ".."))  # RAMP_Bolivia
csv_path = os.path.join(project_root, "data", "V_power_profile_water_heating.csv")
HCWH_shower_P = pd.read_csv(csv_path, sep=";", decimal=",")


WH_shower = HCWH.add_appliance(1,HCWH_shower_P,2,15,0.1,3, thermal_p_var = 0.2, occasional_use=0.33)
WH_shower.windows([360,540],[1080,1260],0.2)




