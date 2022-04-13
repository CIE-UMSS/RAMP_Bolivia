# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:28:41 2021

@author: Clau

Paper: Energy sufficiency (SDEWES LA 2022).
User: Restaurant - HIGHLANDS
"""

from core import User, np
User_list = []

#Definig users

R = User("Restaurant", 1)
User_list.append(R)

#Appliances

R_indoor_bulb = R.Appliance(R,2,7,2,120,0.2,10)
R_indoor_bulb.windows([1107,1440],[0,30],0.35)

R_Blender = R.Appliance(R,1,350,2,20,0.375,5)
R_Blender.windows([420,480],[720,780],0.5)

R_Freezer = R.Appliance(R,1,200,1,1440,0,30,'yes',3)
R_Freezer.windows([0,1440],[0,0])
R_Freezer.specific_cycle_1(200,15,5,15)
R_Freezer.specific_cycle_2(200,15,5,15)
R_Freezer.specific_cycle_3(200,10,5,20)
R_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])