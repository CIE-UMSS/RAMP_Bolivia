#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:39:57 2024

@author: claudia

Carpentry workshop in a village in Kenya
"""

import pandas as pd

from ramp.core.core import User
User_list = []

CAR = User("Carpentry workshop", 3)			
User_list.append(CAR)

GS = User("Grocery Store ", 5)
User_list.append(GS)

CS = User("Copy Store ", 2)
User_list.append(CS)
#Appliances

#Quinoa washing			
   					
CAR_indoor_bulb = CAR.Appliance(4,7,2,120,0.2,10, wd_we_type=0)
CAR_indoor_bulb.windows([1107,1440],[0,0],0.35)
        
CAR_outdoor_bulb = CAR.Appliance(1,13,2,600,0.2,10, wd_we_type=0)                    
CAR_outdoor_bulb.windows([0,330],[1107,1440],0.35)     
    
CAR_planer = CAR.Appliance(2,1500,1,180,0.3,10, wd_we_type=0)                    
CAR_planer.windows([420, 1020],[0,0],0.35)   	

CAR_jigsaw = CAR.Appliance(2,650,1,180,0.3,10, wd_we_type=0)
CAR_jigsaw.windows([420, 1020],[0,0],0.35)			

CAR_cicular_saw = CAR.Appliance(2,1850,1,180,0.3,60, wd_we_type=0)
CAR_cicular_saw.windows([420, 1020],[0,0],0.35)	

CAR_drill = CAR.Appliance(1,450,1,60,0.3,5, wd_we_type=0)
CAR_drill.windows([420, 1020],[0,0],0.35)	

CAR_grinder = CAR.Appliance(1,1500,1,120,0.3,10, wd_we_type=0)
CAR_grinder.windows([420, 1020],[0,0],0.35)	

CAR_rotor = CAR.Appliance(1,1650,1,60,0.3,60, wd_we_type=0)
CAR_rotor.windows([420, 1020],[0,0],0.35)

#Grocery store

GS_indoor_bulb = GS.Appliance(2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_freezer = GS.Appliance(1,200,1,1440,0,30,'yes',3)
GS_freezer.windows([0,1440],[0,0])
GS_freezer.specific_cycle_1(200,20,5,10)
GS_freezer.specific_cycle_2(200,15,5,15)
GS_freezer.specific_cycle_3(200,10,5,20)
GS_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

GS_Radio = GS.Appliance(1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)

#Copy Store

CS_indoor_bulb = GS.Appliance(2,7,2,120,0.2,10, wd_we_type=0)
CS_indoor_bulb.windows([1107,1440],[0,30],0.35)

CS_outdoor_bulb = GS.Appliance(1,13,2,600,0.2,10, wd_we_type=0)
CS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

CS_freezer = GS.Appliance(1,200,1,1440,0,30,'yes',3)
CS_freezer.windows([0,1440],[0,0])
CS_freezer.specific_cycle_1(200,20,5,10)
CS_freezer.specific_cycle_2(200,15,5,15)
CS_freezer.specific_cycle_3(200,10,5,20)
CS_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

CS_Radio = CS.Appliance(1,36,2,60,0.1,5, wd_we_type=0)
CS_Radio.windows([390,450],[1140,1260],0.35)

CS_Laptop = CS.Appliance(1,70,1,180,0.3,30, wd_we_type=0)
CS_Laptop.windows([960,1200],[0,0],0.35)

CS_copy_machine = CS.Appliance(1,1200,1,420,0.3,30, wd_we_type=0)
CS_copy_machine.windows([420,1020],[0,0],0.35)

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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'IGA_KNY.csv')

