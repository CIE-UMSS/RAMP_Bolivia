#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:06:53 2024

@author: claudia
"""

import pandas as pd

from ramp.core.core import User

User_list = []

HI = User("high income",1)
User_list.append(HI)

LI = User("low income",1)
User_list.append(LI)

#Appliances

#High consumption household


HI_indoor_bulb = HI.Appliance(3,7,1,300,0.2,10)
HI_indoor_bulb.windows([1080,1440],[0,0],0.35)

HI_outdoor_bulb = HI.Appliance(1,13,1,320,0.2,10)
HI_outdoor_bulb.windows([1100,1440],[0,0],0.35)

HI_Radio = HI.Appliance(1,7,2,280,0.2,120)
HI_Radio.windows([420,708],[840,1020],0.35)

HI_TV = HI.Appliance(1,60,2,120,0.2,60)
HI_TV.windows([840,1080],[1140,1440],0.35)

HI_Phone_charger = HI.Appliance(2,5,3,240,0.2,5)
HI_Phone_charger.windows([421,660],[1190,1440],0.35,[0,420])

HI_Freezer = HI.Appliance(1,200,1,1440,0,30,'yes',3)
HI_Freezer.windows([0,1440],[0,0])
HI_Freezer.specific_cycle_1(200,15,5,15)
HI_Freezer.specific_cycle_2(200,15,5,15)
HI_Freezer.specific_cycle_3(200,10,5,20)
HI_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

'''
#Low consumption household

HI_indoor_bulb = HI.Appliance(2,7,1,300,0.2,10)
HI_indoor_bulb.windows([1080,1440],[0,0],0.35)

HI_outdoor_bulb = HI.Appliance(1,13,1,320,0.2,10)
HI_outdoor_bulb.windows([1100,1440],[0,0],0.35)

HI_Radio = HI.Appliance(1,7,2,280,0.2,120)
HI_Radio.windows([420,708],[840,1020],0.35)

HI_TV = HI.Appliance(1,60,2,120,0.2,60)
HI_TV.windows([840,1080],[1140,1440],0.35)

HI_Phone_charger = HI.Appliance(1,5,3,240,0.2,5)
HI_Phone_charger.windows([421,660],[1190,1440],0.35,[0,420])
'''


if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
       date_start="2020-01-01", date_end="2020-12-31"
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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'high_cons_raq_grid.csv')