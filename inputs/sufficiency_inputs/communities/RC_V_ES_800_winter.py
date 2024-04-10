#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:26:43 2024

@author: claudia

Rural Community from the VALLEYS with SUFFICIENCY REQUIREMENTS

Raqaypampa

Winter
"""

import pandas as pd

from core import User, np
User_list = []

H = User("household", 1)
User_list.append(H)

H = User("households",200)
User_list.append(H)

HP = User("hospital", 1)
User_list.append(HP)

SC = User("school", 1)
User_list.append(SC)

PL = User("public lighting", 1)
User_list.append(PL)

H_shower_P = pd.read_csv('shower_P_valleys.csv')

#Appliances
H_indoor_bulb = H.Appliance(4,14,3,400,0.2,10)
H_indoor_bulb.windows([360,420],[1020,1440],[0,60],0.35)
         
H_outdoor_bulb = H.Appliance(2,14,1,240,0.2,10)
H_outdoor_bulb.windows([1020,1380],[0,0],0.35)

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
    [330, 1139], [0, 0], [0, 329], [1140, 1440]
)

#H_Fan = H.Appliance(H,1,30,1,220,0.27,60, occasional_use=0.33)
#H_Fan.windows([720,1080],[0,0],0.35)

H_Laptop = H.Appliance(H,1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)

H_shower = H.AppHiance(1,H_shower_P,2,40,0.1,3, thermaH_P_var = 0.2)
H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from valleys

#Health Post

HP_indoor_bulb = HP.Appliance(12,7,2,630,0.1,10)
HP_indoor_bulb.windows([480,720],[870,1440],0.35)

HP_outdoor_bulb = HP.Appliance(1,13,2,690,0.2,10)
HP_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HP_Phone_charger = HP.Appliance(5,2,2,300,0.2,5)
HP_Phone_charger.windows([480,720],[900,1440],0.35)

HP_TV = HP.Appliance(1,150,2,360,0.1,60)
HP_TV.windows([480,720],[780,1020],0.2)

HP_radio = HP.Appliance(1,40,2,360,0.3,60)
HP_radio.windows([480,720],[780,1020],0.35)

HP_PC = HP.Appliance(1,200,2,300,0.1,10)
HP_PC.windows([480,720],[1050,1440],0.35)

HP_printer = HP.Appliance(1,100,1,60,0.3,10)
HP_printer.windows([540,1020],[0,0],0.35)

HP_sterilizer_stove = HP.Appliance(1,600,2,120,0.3,30, occasional_use=0.33)
HP_sterilizer_stove.windows([480,720],[780,1020],0.35)

HP_needle_destroyer = HP.Appliance(1,70,1,60,0.3,10, occasional_use=0.33)
HP_needle_destroyer.windows([480,720],[0,0],0.35)

HP_water_pump = HP.Appliance(1,400,1,30,0.2,10, occasional_use=0.33)
HP_water_pump.windows([480,720],[0,0],0.35)

H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour(
    [330, 1139], [0, 0], [0, 329], [1140, 1440]
)

H_shower = H.AppHiance(1,H_shower_P,2,40,0.1,3, thermaH_P_var = 0.2)
H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

#School
SC_indoor_bulb = SC.Appliance(27,7,1,60,0.2,10)
SC_indoor_bulb.windows([480,780],[0,0],0.35)

SC_outdoor_bulb = SC.Appliance(7,13,1,60,0.2,10)
SC_outdoor_bulb.windows([480,780],[0,0],0.35)

SC_TV = SC.Appliance(5,60,1,120,0.1,5, occasional_use = 0.5)
SC_TV.windows([480,780],[0,0],0.35)

SC_radio = SC.Appliance(24,4,1,120,0.1,5, occasional_use = 0.5)
SC_radio.windows([480,780],[0,0],0.35)

SC_DVD = SC.Appliance(2,8,1,120,0.1,5, occasional_use = 0.5)
SC_DVD.windows([480,780],[0,0],0.35)

H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour(
    [330, 1139], [0, 0], [0, 329], [1140, 1440]
)

SC_PC = SC.Appliance(25,50,1,210,0.1,10)
SC_PC.windows([480,780],[0,0],0.35)

SC_Phone_charger = SC.Appliance(5,2,1,180,0.2,5)
SC_Phone_charger.windows([480,780],[0,0],0.35)

SC_Printer = SC.Appliance(1,20,1,30,0.1,5)
SC_Printer.windows([480,780],[0,0],0.35)

SC_Stereo = SC.Appliance(1,150,1,90,0.1,5, occasional_use = 0.33)
SC_Stereo.windows([480,780],[0,0],0.35)

SC_data = SC.Appliance(1,420,1,60,0.1,5, occasional_use = 0.33)
SC_data.windows([480,780],[0,0],0.35)

#public lighting
PL_lamp_post = PL.Appliance(1,40,2,700,0,600, 'yes', flat = 'yes') #corregir el numero en funcion al numero de casas
PL_lamp_post.windows([0,420],[1110,1440],0.1)

#Income Generating Activities

#planta procesadora de trigo y sus derivados




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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'output_file_RC_V_winter.csv')