#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:28:48 2024

@author: claudia

Household from the HIGHLANDS with SUFFICIENCY REQUIREMENTS
SUMMER
"""

import pandas as pd

from core import User, np
User_list = []

H = User("household", 1)
User_list.append(H)

H_shower_P = pd.read_csv('shower_P_HL.csv')

#Appliances
H_indoor_bulb = H.Appliance(4,14,2,300,0.2,10)
H_indoor_bulb.windows([1140,1440],[0,60],0.35)
         
H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

H_TV = H.Appliance(1,60,2,120,0.1,5)
H_TV.windows([1080,1440],[0,60],0.35)

H_Radio = H.Appliance(1,36,2,120,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
H_Phone_charger.windows([1020,1440],[0,300],0.35)

H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour(
    [490, 1079], [0, 0], [0, 419], [1080, 1440]
)

#H_Fan = H.Appliance(H,1,30,1,220,0.27,60, occasional_use=0.33)
#H_Fan.windows([720,1080],[0,0],0.35)

H_Laptop = H.Appliance(H,1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)

H_shower = H.AppHiance(1,H_shower_P,2,40,0.1,3, thermaH_P_var = 0.2)
H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from valleys

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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'output_file_HH_HL_summer.csv')