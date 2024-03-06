# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:16:23 2022

@author: Clau

Small family - Valleys
"""

import pandas as pd

from core import User, np
User_list = []

#Create new user classes

S = User("Small",1)
User_list.append(S)

S_shower_P = pd.read_csv('TimeSeries/shower_P.csv')

#Appliances

S_indoor_bulb = S.Appliance(S,5,7,2,300,0.2,10)
S_indoor_bulb.windows([1170,1440],[0,30],0.35)

S_outdoor_bulb = S.Appliance(S,2,13,2,300,0.2,10)
S_outdoor_bulb.windows([0,330],[1170,1440],0.35)

S_Phone_charger = S.Appliance(S,3,6,2,60,0.2,15)
S_Phone_charger.windows([420,1440],[0,400],0.35)

S_Radio = S.Appliance(S,1,7,1,120,0.1,10)
S_Radio.windows([420,840],[0,0],0.35)

S_TV = S.Appliance(S,1,150,2,240,0.3,5)
S_TV.windows([720,900],[1170,1440],0.35)

S_Laptop = S.Appliance(S,2,100,1,180,0.3,30)
S_Laptop.windows([960,1200],[0,0],0.35)

S_TV_cable = S.Appliance(S,1,35,2,240,0.3,5)
S_TV_cable.windows([720,900],[1170,1440],0.35)

S_Stereo = S.Appliance(S,1,450,1,250,0.3,15, occasional_use = 0.3)
S_Stereo.windows([840,1320],[0,0],0.35)

S_Washing_machine = S.Appliance(S,1,800,2,90,0.3,30, occasional_use = 0.3)
S_Washing_machine.windows([480,720],[900,1200],0.35)

S_Microwave = S.Appliance(S,1,800,3,30,0.3,1, occacional_use = 0.3)
S_Microwave.windows([420,540],[720,900],0.3,[1080,1260])

S_water_pump = S.Appliance(S,1,250,2,30,0.3,15, occasional_use = 0.7)
S_water_pump.windows([420,720],[960,1260],0.35)

S_Freezer = S.Appliance(S,1,200,1,1440,0,30,'yes',2)
S_Freezer.windows([0,1440],[0,0])
S_Freezer.specific_cycle_1(5,15,200,15)
S_Freezer.specific_cycle_2(5,20,200,10)
S_Freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

S_shower = S.Appliance(S,1,S_shower_P,2,30,0.1,3, thermal_P_var = 0.2, P_series=True)
S_shower.windows([390,540],[1080,1200],0.2)


