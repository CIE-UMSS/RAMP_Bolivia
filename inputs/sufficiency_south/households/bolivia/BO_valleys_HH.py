#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:44:49 2024

@author: claudia
"""

import pandas as pd

from ramp.core.core import User

User_list = []

H = User("household", 1)
User_list.append(H)

H_shower_P = pd.read_csv('shower_P_V.csv')

'''
SUFFICIENCY
'''

# #SUMMER
#Illumination
# H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
# H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

# #Thermal comfort
# #Not used in this part of the country

# #Cold storage
# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [330, 1139], [0, 0], [0, 329], [1140, 1440])

# #Hygiene
# #water heating
# #Use of gas for water heating

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
#Illumination
# H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
# H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([960,1380],[0,0],0.35)

# #Thermal comfort
# #Not used in this part of the country

# #Cold Storage
# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [330, 1139], [0, 0], [0, 329], [1140, 1440])

# #Hygiene
# #Water heating
# #Use of gas for this purpose

# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5) 
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

#WINTER

#Illumination
# H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
# H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([960,1380],[0,0],0.35)

# #Thermal comfort
# #Not used

# #Cold storage
# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [330, 1139], [0, 0], [0, 329], [1140, 1440])


# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5) 
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

#SPRING
# #Illumination
# H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
# H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

# #Thermal comfort
# #Not used in this part of the country

# #Cold storage
# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [330, 1139], [0, 0], [0, 329], [1140, 1440]
# )

# #Water heating
# #Use of gas for this purpose

# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5) 
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

'''
MODERN APPLIANCES
'''

#SUMMER
#Illumination
# H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
# H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

# #Thermal comfort
# #Not used in this part of the country

# #Cold storage
# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [330, 1139], [0, 0], [0, 329], [1140, 1440])

# #hygiene
# #water heating
# H_shower = H.Appliance(1,5500,2,40,0.1,3, thermal_P_var = 0.2)
# H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

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
#Illumination
# H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
# H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([960,1380],[0,0],0.35)

# #Thermal comfort
# #Not used in this part of the country

# #Cold Storage
# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [330, 1139], [0, 0], [0, 329], [1140, 1440])

# #Hygiene
# #Water heating
# H_shower = H.Appliance(1,5500,2,30,0.1,3, thermal_P_var = 0.3)
# H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

# # #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5) 
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

# #WINTER
#Illumination
# H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
# H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([960,1380],[0,0],0.35)

# #Thermal comfort
# #Not used

# #Cold storage
# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [330, 1139], [0, 0], [0, 329], [1140, 1440]
# )

# #Hygiene
# #water heating
# H_shower = H.Appliance(1,5500,2,30,0.2,3, thermal_P_var = 0.4)
# H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5) 
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

#SPRING

# #Illumination
# H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
# H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

# #Thermal comfort
# #Not used in this part of the country

# #Cold storage
# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [330, 1139], [0, 0], [0, 329], [1140, 1440]
# )

# #Water heating
H_shower = H.Appliance(1,5500,2,40,0.1,3, thermal_P_var = 0.2)
H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5) 
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
        #date_start="2022-01-01", date_end="2022-03-31" #SUMMER
        #date_start="2022-04-01", date_end="2022-06-30"  #FALL
        #date_start="2022-07-01", date_end="2022-09-30"  #WINTER
        date_start="2022-10-01", date_end="2022-12-31"  #SPRING"
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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'shower_spring_V.csv')