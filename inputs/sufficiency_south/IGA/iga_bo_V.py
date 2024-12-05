#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:20:34 2024

@author: claudia

Milk production
"""

import pandas as pd

from ramp.core.core import User
User_list = []

MILK = User("Milk production", 1)			
User_list.append(MILK)

WS = User("Workshop", 2)
User_list.append(WS)

R = User("Restaurant", 5)
User_list.append(R)

GS = User("Grocery Store ", 5)
User_list.append(GS)

EB = User("Entertainment Business", 2)
User_list.append(EB)

#Appliances

		
                					
MILK_indoor_bulb = MILK.Appliance(2,7,2,120,0.2,10)
MILK_indoor_bulb.windows([1107,1440],[0,0],0.35)
        
MILK_outdoor_bulb = MILK.Appliance(1,13,2,600,0.2,10)                    
MILK_outdoor_bulb.windows([0,330],[1107,1440],0.35)     
    
MILK_cooler_tank = MILK.Appliance(1,4000,2,480,0.2,240)                    
MILK_cooler_tank.windows([360,600],[1080,1320],0.2)   	

MILK_milking_machine = MILK.Appliance(1,800,2,120,0.3,60, wd_we_type=0)
MILK_milking_machine.windows([300,480],[960,1080],0.3)			


#Workshop

WS_indoor_bulb = WS.Appliance(2,7,2,120,0.2,10, wd_we_type=0)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(1,5500,1,60,0.5,30, wd_we_type=0)
WS_welding_machine.windows([0,1440],[0,0],0.35)

WS_grinding_machine = WS.Appliance(1,750,1,480,0.2,60, wd_we_type=0)
WS_grinding_machine.windows([0,1440],[0,0],0.35)

WS_Radio = WS.Appliance(1,36,2,60,0.1,5, wd_we_type=0)
WS_Radio.windows([390,450],[1140,1260],0.35)

#Restaurant

R_indoor_bulb = R.Appliance(2,7,2,120,0.2,10)
R_indoor_bulb.windows([1107,1440],[0,30],0.35)

R_Blender = R.Appliance(1,350,2,20,0.375,5)
R_Blender.windows([420,480],[720,780],0.5)

R_freezer = R.Appliance(1,200,1,1440,0,30,'yes',2)
R_freezer.windows([0,1440],[0,0])
R_freezer.specific_cycle_1(5,15,200,15)
R_freezer.specific_cycle_2(5,20,200,10)
R_freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

#Grocery Store

GS_indoor_bulb = GS.Appliance(2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_Freezer = GS.Appliance(1,200,1,1440,0,30,'yes',2)
GS_Freezer.windows([0,1440],[0,0])
GS_Freezer.specific_cycle_1(5,15,200,15)
GS_Freezer.specific_cycle_2(5,20,200,10)
GS_Freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

GS_Radio = GS.Appliance(1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)

#entertainment bussiness

EB_indoor_bulb = EB.Appliance(2,7,2,120,0.2,10)
EB_indoor_bulb.windows([1107,1440],[0,30],0.35)

EB_outdoor_bulb = EB.Appliance(1,13,2,600,0.2,10)
EB_outdoor_bulb.windows([0,330],[1107,1440],0.35)

EB_Stereo = EB.Appliance(1,150,2,90,0.1,5, occasional_use = 0.33)
EB_Stereo.windows([480,780],[0,0],0.35)

EB_TV = EB.Appliance(1,60,2,120,0.1,5, occasional_use = 0.33)
EB_TV.windows([480,780],[840,1140],0.2)
    
EB_PC = EB.Appliance(1,50,2,210,0.1,10, occasional_use = 0.33)
EB_PC.windows([480,780],[840,1140],0.35)

EB_Freezer = EB.Appliance(1,200,1,1440,0,30,'yes',2)
EB_Freezer.windows([0,1440],[0,0])
EB_Freezer.specific_cycle_1(5,15,200,15)
EB_Freezer.specific_cycle_2(5,20,200,10)
EB_Freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
        date_start="2022-01-01", date_end="2022-12-31")
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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'IGA_BO_V.csv')