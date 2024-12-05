#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:02:53 2024

@author: claudia

Flour processing in the Bolivian Lowlands

The seasonal behaviour of quinoa and cereals must be taken into account for these pro-
cessing activities, and therefore these activities are only modelled during the harvest period,
which typically spans from July to October.
"""

import pandas as pd

from ramp.core.core import User
User_list = []

LAU = User("Flour_processing", 1)				
User_list.append(LAU)

GS = User("Grocery Store", 5)
User_list.append(GS)

WS = User("Workshop", 3)
User_list.append(WS)

EB = User("Entertainment Business", 3)
User_list.append(EB)

R = User("Restaurant", 5)
User_list.append(R)


#Appliances			
                				
LAU_grain_dryer = LAU.Appliance(1,5000,1,180,0.2,30, wd_we_type=0)				
LAU_grain_dryer.windows([420,1080],[0,0],0.2)				
                				
LAU_grain_miller = LAU.Appliance(1,18500,1,180,0.2,30, wd_we_type=0)				
LAU_grain_miller.windows([420,1080],[0,0],0.2)				
                				
LAU_grain_toaster = LAU.Appliance(1,780,1,90,0.2,15,wd_we_type=0)				
LAU_grain_toaster.windows([420,1080],[0,0],0.2)				
                				
LAU_pump = LAU.Appliance(1,1700,2,60,0.2,10,occasional_use = 0.33)				
LAU_pump.windows([420,720],[840,1020],0.35)	

#Grocery Store			

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

#workshop

WS_indoor_bulb = WS.Appliance(2,7,2,120,0.2,10, wd_we_type=0)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(1,5500,1,60,0.5,30, wd_we_type=0)
WS_welding_machine.windows([0,1440],[0,0],0.35)

WS_grinding_machine = WS.Appliance(1,750,1,480,0.2,60, wd_we_type=0)
WS_grinding_machine.windows([0,1440],[0,0],0.35)

WS_Radio = WS.Appliance(1,36,2,60,0.1,5, wd_we_type=0)
WS_Radio.windows([390,450],[1140,1260],0.35)

#Entertainment bussiness

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

EB_freezer = EB.Appliance(1,200,1,1440,0,30,'yes',3)
EB_freezer.windows([0,1440],[0,0])
EB_freezer.specific_cycle_1(200,20,5,10)
EB_freezer.specific_cycle_2(200,15,5,15)
EB_freezer.specific_cycle_3(200,10,5,20)
EB_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'IGA_BO_LL.csv')