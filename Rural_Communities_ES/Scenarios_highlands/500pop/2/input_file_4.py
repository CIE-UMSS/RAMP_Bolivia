# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:33:20 2022

@author: pietr
"""

'''
Paper: Energy sufficiency (SDEWES LA 2022)
User: High Income Household - HIGHLANDS
'''
from core import User, np
User_list = []

#Definig users

R = User("Restaurant", 5)
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

#Definig users
GS = User("Grocery Store 1", 6)
User_list.append(GS)

#Appliances
GS_indoor_bulb = GS.Appliance(GS,2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(GS,1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_Freezer = GS.Appliance(GS,1,200,1,1440,0,30,'yes',3)
GS_Freezer.windows([0,1440],[0,0])
GS_Freezer.specific_cycle_1(200,15,5,15)
GS_Freezer.specific_cycle_2(200,15,5,15)
GS_Freezer.specific_cycle_3(200,10,5,20)
GS_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

GS_Radio = GS.Appliance(GS,1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)