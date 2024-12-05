#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:30:57 2024

@author: claudia

Household from the HIGHLANDS with SUFFICIENCY REQUIREMENTS
SPRING
"""

import pandas as pd

from ramp.core.core import User

User_list = []

H = User("household", 1)
User_list.append(H)

H_shower_P = pd.read_csv('shower_P_HL.csv')

# #T1
# #Shelter and living conditions
# #Ilumination
# '''
H_indoor_bulb = H.Appliance(4,25,2,360,0.2,10)
H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
H_outdoor_bulb = H.Appliance(2,40,1,180,0.2,10)
H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

#Thermal comfort
# H_heater = H.Appliance(2,800,2,180,0.1,10, occasional_use = 0.33)
# H_heater.windows([480,660],[1080,1200],0.35)

# #Nutrition

# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [490, 1079], [0, 0], [0, 419], [1080, 1440]
# )

# H_Blender = H.Appliance(1, 50, 3, 30, 0.1, 1, occasional_use=0.33)
# H_Blender.windows([420, 480], [660, 750], 0.35, [1140, 1200])

# #Hygiene
# #H_shower = H.AppHiance(1,H_shower_P,2,40,0.1,3, thermaH_P_var = 0.2)
# #H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from valleys

# #ICT
# H_TV = H.Appliance(1,150,2,120,0.1,5) 
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_desktop = H.Appliance(1,150,1,120,0.3,30)
# H_desktop.windows([960,1200],[0,0],0.35)

#T2
#Shelter and living conditions
#Ilumination
'''
H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
H_outdoor_bulb.windows([1140,1380],[0,0],0.35)


#Nutrition

H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour(
    [490, 1079], [0, 0], [0, 419], [1080, 1440]
)

#H_Blender = H.Appliance(1, 50, 3, 30, 0.1, 1, occasional_use=0.33)
#H_Blender.windows([420, 480], [660, 750], 0.35, [1140, 1200])

#Hygiene
H_shower = H.Appliance(1,H_shower_P,2,20,0.1,3, thermal_P_var = 0.3)
H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

#H_water_pump = H.Appliance(1,625,1,15,0.2,5,occasional_use = 0.33)
#H_water_pump.windows([420,720],[0,0],0.35)

#H_washing_machine = H.Appliance(1, 800, 2, 120, 0.1, 15, occasional_use=0.15)
#H_washing_machine.windows([420, 600], [1020, 1260], 0.35)

#ICT
H_TV = H.Appliance(1,30,2,120,0.1,5) 
H_TV.windows([1080,1440],[0,60],0.35)

H_Radio = H.Appliance(1,36,2,120,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
H_Phone_charger.windows([1020,1440],[0,300],0.35)

H_Laptop = H.Appliance(1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)

'''


if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
        date_start="2020-10-01", date_end="2020-12-31"
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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'HH_BO_HL_spring_lighting_trad.csv')