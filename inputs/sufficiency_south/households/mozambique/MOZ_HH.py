#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:40:12 2024

@author: claudia

Household from Mozambique community with SUFFICIENCY REQUIREMENTS
SUMMER
"""

import pandas as pd

from ramp.core.core import User

User_list = []

H = User("households",1)
User_list.append(H)

'''
Energy Sufficiency
'''
#SUMMER

#Appliances

#Shelter and living conditions
#ilumination

# H_indoor_bulb = H.Appliance(4,7,3,360,0.2,10)
# H_indoor_bulb.windows([240,360],[1080,1440],0.35,[0,60])
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

# #thermal comfort
# H_Fan = H.Appliance(4,30,1,400,0.27,30)
# H_Fan.windows([540,1020],[0,0],0.35)

# #Nutrition

# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
# H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])

# #Water heating
# #Non electric

# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

#FALL

# H_indoor_bulb = H.Appliance(4,7,3,400,0.2,10)
# H_indoor_bulb.windows([360,420],[960,1440],0.35,[0,60])
         
# H_outdoor_bulb = H.Appliance(2,14,1,240,0.2,10)
# H_outdoor_bulb.windows([960,1380],[0,0],0.35)

# #thermal comfort
# H_Fan = H.Appliance(1,30,2,240,0.27,30)
# H_Fan.windows([600,980],[0,0],0.35)

# #Nutrition

# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
# H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])


# #Hygiene
# #Non electric

# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

# #WINTER

# #Shelter and living conditions
# #ilumination

# H_indoor_bulb = H.Appliance(4,7,3,400,0.2,10)
# H_indoor_bulb.windows([240,420],[960,1440],0.35,[0,60])
         
# H_outdoor_bulb = H.Appliance(2,14,1,160,0.2,10)
# H_outdoor_bulb.windows([960,1380],[0,0],0.35)

# #thermal comfort
# H_Fan = H.Appliance(1,30,1,120,0.27,30)
# H_Fan.windows([660,900],[0,0],0.35)

# #Nutrition

# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2) #Two cycles for cold season in ll
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [480, 1200], [0, 0], [0, 299], [1201, 1440])

# #Hygiene
# #NON ELECTRIC

# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

# #SPRING

#Shelter and living conditions
#ilumination

H_indoor_bulb = H.Appliance(4,7,3,360,0.2,10)
H_indoor_bulb.windows([240,360],[1080,1440],0.35,[0,60])
         
H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

#thermal comfort
H_Fan = H.Appliance(4,30,1,700,0.27,30)
H_Fan.windows([480,1260],[0,0],0.35)

#Nutrition

H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])

#Hygiene
#NON ELECTRIC

#ICT
H_TV = H.Appliance(1,30,2,120,0.1,5)
H_TV.windows([1080,1440],[0,60],0.35)

H_Radio = H.Appliance(1,36,2,120,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
H_Phone_charger.windows([1020,1440],[0,300],0.35)

H_Laptop = H.Appliance(1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)


if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
        #date_start="2022-01-01", date_end="2022-03-31" #SUMMER
        #date_start="2022-04-01", date_end="2022-06-30"  #FALL
        #date_start="2022-07-01", date_end="2022-09-30"  #WINTER
        date_start="2022-10-01", date_end="2022-12-31"  #SPRING
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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'MOZ_HH_spring.csv')