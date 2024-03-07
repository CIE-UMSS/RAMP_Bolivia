#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:46:34 2024

@author: claudia

MTF
Tier 4 household
"""
from ramp.core.core import User

User_list = []

# Create new user classes
H = User("Tier 3", 1)
User_list.append(H)


# Create new appliances
H_indoor_bulb = H.Appliance(3, 5, 2, 240, 0.2, 10)
H_indoor_bulb.windows([1080, 1440], [0, 30], 0.35)

H_outdoor_bulb = H.Appliance(1, 13, 2, 120, 0.2, 10)
H_outdoor_bulb.windows([0, 330], [1170, 1440], 0.35)

H_TV = H.Appliance(1, 40, 3, 90, 0.2, 5) # 22 inch LED technology #CRT technology 15 inch: 60W, LED/LCD are more efficient: 15 inch, around 15W
H_TV.windows([750, 840], [1170, 1440], 0.35, [0, 30])

H_Radio = H.Appliance(1,36,2,120,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(2, 5, 2, 180, 0.2, 5)
H_Phone_charger.windows([1080, 1440], [420, 600], 0.35)

H_Blender = H.Appliance(1, 50, 3, 30, 0.1, 1, occasional_use=0.33)
H_Blender.windows([420, 480], [660, 750], 0.35, [1140, 1200])

H_Laptop = H.Appliance(H,1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)

H_Refrigerator = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
H_Refrigerator.windows([0, 1440], [0, 0])
H_Refrigerator.specific_cycle_1(200, 15, 5, 15) #intemedio
H_Refrigerator.specific_cycle_2(200, 10, 5, 20) #standard
H_Refrigerator.cycle_behaviour([330, 1139], [0, 0], [0, 329], [1140, 1440])

H_Iron = H.Appliance(1, 1000, 2, 10, 0.2, 1, occasional_use=0.15)
H_Iron.windows([420, 600], [1020, 1260], 0.35)

H_washing_machine = H.Appliance(1, 800, 2, 120, 0.1, 15, occasional_use=0.15)
H_washing_machine.windows([420, 600], [1020, 1260], 0.35)

if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
    )
    uc.initialize(peak_enlarge=0.15)

    Profiles_list = uc.generate_daily_load_profiles(flat=False)

    # post-processing
    from ramp.post_process import post_process as pp

    Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
        Profiles_list
    )
    pp.Profile_series_plot(
        Profiles_series
    )  # by default, profiles are plotted as a series
    
    if (
        len(Profiles_list) > 1
    ):  # if more than one daily profile is generated, also cloud plots are shown
        pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
        
    # this would be a new method using work of @mohammadamint
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'tier_4.csv')
