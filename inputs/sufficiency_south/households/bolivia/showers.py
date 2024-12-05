#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:58:04 2024

@author: claudia

Showers use in Bolivia 
8 minutes showers
"""
import pandas as pd

from ramp.core.core import User
User_list = []

#Defining users
H = User("household", 1)
User_list.append(H)
'''
#Lowlands
#Summer
H_shower = H.Appliance(1,4500,2,32,0.1,3, thermal_P_var = 0)
H_shower.windows([360,540],[1080,1260],0.2) 

#Fall
H_shower = H.Appliance(1,4500,2,32,0.1,3, thermal_P_var = 0.1)
H_shower.windows([360,540],[1080,1260],0.2) 

#Winter
H_shower = H.Appliance(1,4500,2,32,0.2,3, thermal_P_var = 0.2)
H_shower.windows([360,540],[1080,1260],0.2) 

#Spring
H_shower = H.Appliance(1,4500,2,32,0.1,3, thermal_P_var = 0)
H_shower.windows([360,540],[1080,1260],0.2) 

#Valleys
#Summer
H_shower = H.Appliance(1,4500,2,32,0.1,3, thermal_P_var = 0.1)
H_shower.windows([360,540],[1080,1260],0.2) 

#Fall
H_shower = H.Appliance(1,5500,2,32,0.1,3, thermal_P_var = 0.2)
H_shower.windows([360,540],[1080,1260],0.2)

#Winter
H_shower = H.Appliance(1,5500,2,32,0.2,3, thermal_P_var = 0.3)
H_shower.windows([360,540],[1080,1260],0.2) 

#Spring
H_shower = H.Appliance(1,4500,2,32,0.1,3, thermal_P_var = 0.1)
H_shower.windows([360,540],[1080,1260],0.2) 

#Highlands
#Summer
H_shower = H.Appliance(1,5500,2,32,0.1,3, thermal_P_var = 0.2)
H_shower.windows([360,540],[1080,1260],0.2) 

#Fall
H_shower = H.Appliance(1,5500,2,32,0.2,3, thermal_P_var = 0.3)
H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

#Winter

H_shower = H.Appliance(1,5500,2,32,0.2,3, thermal_P_var = 0.4)
H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands
'''
#Spring

H_shower = H.Appliance(1,5500,2,32,0.1,3, thermal_P_var = 0.2)
H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands


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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'shower_spring_HL_of.csv')