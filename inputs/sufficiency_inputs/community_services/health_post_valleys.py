# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:56:48 2021

@author: Clau
"""

'''
Health post - VALLEYS
'''

import pandas as pd


from ramp.core.core import User

User_list = []

#Defining users
HP = User("Health post", 1)
User_list.append(HP)

H_shower_P = pd.read_csv('shower_P_V.csv')


#Appliances

HP_indoor_bulb = HP.Appliance(12,7,2,690,0.2,10)
HP_indoor_bulb.windows([480,720],[870,1440],0.35)

HP_outdoor_bulb = HP.Appliance(1,13,2,500,0.2,10)
HP_outdoor_bulb.windows([0,342],[1140,1440],0.35)

HP_Phone_charger = HP.Appliance(5,2,2,300,0.2,5)
HP_Phone_charger.windows([480,720],[900,1440],0.35)

HP_TV = HP.Appliance(1,30,2,360,0.1,60)
HP_TV.windows([480,720],[780,1020],0.2)

HP_radio = HP.Appliance(1,40,2,360,0.3,60)
HP_radio.windows([480,720],[780,1020],0.35)

HP_PC = HP.Appliance(1,150,2,300,0.1,10)
HP_PC.windows([480,720],[1050,1440],0.35)

HP_printer = HP.Appliance(1,100,1,180,0.3,10)
HP_printer.windows([540,1020],[0,0],0.35)

HP_sterilizer_stove = HP.Appliance(1,600,2,120,0.3,30, occasional_use=0.33)
HP_sterilizer_stove.windows([480,720],[780,1020],0.35)

HP_needle_destroyer = HP.Appliance(1,70,1,60,0.3,10, occasional_use=0.33)
HP_needle_destroyer.windows([480,720],[0,0],0.35)

HP_water_pump = HP.Appliance(1,400,1,30,0.2,10)
HP_water_pump.windows([480,720],[0,0],0.35)

HP_Freezer = HP.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
HP_Freezer.windows([0, 1440], [0, 0])
HP_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
HP_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
HP_Freezer.cycle_behaviour(
    [330, 1139], [0, 0], [0, 329], [1140, 1440]
)

HP_shower = HP.Appliance(1,H_shower_P,2,10,0.1,3, thermal_P_var = 0.2, occasional_use=0.33)
HP_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'health_post_valleys.csv')

