# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:28:39 2022

@author: Clau

Uni-personal family - Lowlands
"""

import pandas as pd

from core import User, np
User_list = []

#Create new user classes

U = User("Unipersonal",1)
User_list.append(U)

U_shower_P = pd.read_csv('shower_P.csv')

#Appliances

U_indoor_bulb = U.Appliance(U,3,7,2,300,0.2,10)
U_indoor_bulb.windows([1170,1440],[0,30],0.35)

U_outdoor_bulb = U.Appliance(U,1,13,2,300,0.2,10)
U_outdoor_bulb.windows([0,330],[1170,1440],0.35)

U_Phone_charger = U.Appliance(U,1,6,2,60,0.2,15)
U_Phone_charger.windows([420,1440],[0,400],0.35)

U_Radio = U.Appliance(U,1,7,1,120,0.1,10)
U_Radio.windows([420,840],[0,0],0.35)

U_TV = U.Appliance(U,1,150,2,180,0.3,5)
U_TV.windows([720,900],[1170,1440],0.35)

U_Laptop = U.Appliance(U,1,100,1,120,0.3,30)
U_Laptop.windows([960,1200],[0,0],0.35)

U_TV_cable = U.Appliance(U,1,35,2,180,0.3,5)
U_TV_cable.windows([720,900],[1170,1440],0.35)

U_Stereo = U.Appliance(U,1,450,1,250,0.3,15, occasional_use = 0.2)
U_Stereo.windows([840,1320],[0,0],0.35)

U_Washing_machine = U.Appliance(U,1,800,2,60,0.3,30, occasional_use = 0.2)
U_Washing_machine.windows([480,720],[900,1200],0.35)

U_Microwave = U.Appliance(U,1,800,3,20,0.3,1, occasional_use = 0.2)
U_Microwave.windows([420,540],[720,900],0.3,[1080,1260])

U_water_pump = U.Appliance(U,1,250,2,30,0.3,15, occasional_use = 0.2)
U_water_pump.windows([420,720],[960,1260],0.35)

U_Freezer = U.Appliance(U,1,200,1,1440,0,30,'yes',3)
U_Freezer.windows([0,1440],[0,0])
U_Freezer.specific_cycle_1(200,20,5,10)
U_Freezer.specific_cycle_2(200,15,5,15)
U_Freezer.specific_cycle_3(200,10,5,20)
U_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

U_Telephone = U.Appliance(U,1,10,1,1440,0,30,'yes')
U_Telephone.windows([0,1440],[0,0])

U_Modem = U.Appliance(U,1,7,1,1440,0,60,'yes')
U_Modem.windows([0,1440],[0,0])

U_shower = U.Appliance(U,1,U_shower_P,2,15,0.1,3, thermal_P_var = 0.2, P_series=True, occasional_use = 0.6)
U_shower.windows([390,540],[1080,1200],0.2)

U_Air_Conditioner = U.Appliance(U,1,1000,2,120,0.2,15)
U_Air_Conditioner.windows([720,900],[1020,1260],0.35)
