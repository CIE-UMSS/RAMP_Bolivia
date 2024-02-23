#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:40:12 2024

@author: claudia

Household from the lowlands with SUFFICIENCY REQUIREMENTS
"""
import pandas as pd

from core import User, np
User_list = []

#Defining users
H = User("household", 1)
User_list.append(H)

H_shower_P = pd.read_csv('TimeSeries/shower_P.csv')

#Appliances
H_indoor_bulb = H.Appliance(H,4,7,2,120,0.2,10)
H_indoor_bulb.windows([1082,1440],[0,30],0.35)
         
H_outdoor_bulb = H.Appliance(H,2,13,2,600,0.2,10)
H_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H_TV = H.Appliance(H,2,60,2,120,0.1,5)
H_TV.windows([1082,1440],[0,60],0.35)

H_Radio = H.Appliance(H,1,36,2,60,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(H,4,2,2,300,0.2,5)
H_Phone_charger.windows([1110,1440],[0,30],0.35)

H_Freezer = H.Appliance(H,1,200,1,1440,0,30, 'yes',3)
H_Freezer.windows([0,1440],[0,0])
H_Freezer.specific_cycle_1(200,20,5,10)
H_Freezer.specific_cycle_2(200,15,5,15)
H_Freezer.specific_cycle_3(200,10,5,20)
H_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

H_Fan = H.Appliance(H,1,30,1,220,0.27,60)
H_Fan.windows([720,1080],[0,0],0.35)

H_Laptop = H.Appliance(H,1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)

H_shower = H.AppHiance(H,1,H_shower_P,2,45,0.1,3, thermaH_P_var = 0.2, P_series=True)
H_shower.windows([390,540],[1080,1200],0.2) #Use thermal series from lowlands