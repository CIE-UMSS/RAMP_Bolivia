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
HC = User("Health post", 1)
User_list.append(HC)

H_shower_P = pd.read_csv('shower_P_V.csv')


#Appliances

HC_indoor_bulb = HC.Appliance(20,7,2,690,0.2,10)
HC_indoor_bulb.windows([480,720],[870,1440],0.35)

HC_outdoor_bulb = HC.Appliance(5,13,2,690,0.2,10)
HC_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HC_Phone_charger = HC.Appliance(5,2,2,300,0.2,5)
HC_Phone_charger.windows([480,720],[900,1440],0.35)

HC_TV = HC.Appliance(2,150,2,360,0.1,60)
HC_TV.windows([480,720],[780,1020],0.2)

HC_radio = HC.Appliance(5,40,2,360,0.3,60)
HC_radio.windows([480,720],[780,1020],0.35)

HC_PC = HC.Appliance(2,200,2,300,0.1,10)
HC_PC.windows([480,720],[1050,1440],0.35)

HC_printer = HC.Appliance(2,100,1,60,0.3,10)
HC_printer.windows([540,1020],[0,0],0.35)

HC_sterilizer_stove = HC.Appliance(3,600,2,120,0.3,30, occasional_use=0.33)
HC_sterilizer_stove.windows([480,720],[780,1020],0.35)

HC_needle_destroyer = HC.Appliance(1,70,1,60,0.3,10, occasional_use=0.33)
HC_needle_destroyer.windows([480,720],[0,0],0.35)

HC_water_pump = HC.Appliance(1,400,1,45,0.2,10)
HC_water_pump.windows([480,720],[0,0],0.35)

HC_Freezer = HC.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
HC_Freezer.windows([0, 1440], [0, 0])
HC_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
HC_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
HC_Freezer.cycle_behaviour([330, 1139], [0, 0], [0, 329], [1140, 1440])

HC_microscope = HC.Appliance(2,3,2,120,0.2,10, occasional_use=0.33)
HC_microscope.windows([480,720],[840,960],0.35)

HC_shower = HC.Appliance(1,H_shower_P,2,15,0.1,3, thermal_P_var = 0.2, occasional_use=0.33)
HC_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

HC_dental_compresor = HC.Appliance(2,500,2,60,0.15,10, occasional_use=0.33)
HC_dental_compresor.windows([480,720],[840,1260],0.35)

HC_centrifuge = HC.Appliance(2,100,1,60,0.15,10, occasional_use=0.33)
HC_centrifuge.windows([480,720],[0,0],0.35)

HC_serological_rotator = HC.Appliance(2,10,1,60,0.25,15, occasional_use=0.33)
HC_serological_rotator.windows([480,720],[0,0],0.35)

if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
        date_start="2020-01-01", date_end="2020-12-31")
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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'health_center_BO_V.csv')
