# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:02:28 2021

@author: Clau
"""

'''
Paper: Energy sufficiency (SDEWES LA 2022)
User: School B - LOWLANDS
'''

from core import User, np
User_list = []

#Definig users

SB = User("School type B", 1)
User_list.append(SB)

#Appliances

SB_indoor_bulb = SB.Appliance(SB,12,7,2,120,0.25,30)
SB_indoor_bulb.windows([480,780],[840,1140],0.35)

SB_outdoor_bulb = SB.Appliance(SB,3,13,1,60,0.2,10)
SB_outdoor_bulb.windows([960,1080],[0,0],0.35)

SB_TV = SB.Appliance(SB,1,60,2,120,0.1,5, occasional_use = 0.5)
SB_TV.windows([480,780],[840,1140],0.2)

SB_radio = SB.Appliance(SB,3,4,2,120,0.1,5, occasional_use = 0.5)
SB_radio.windows([480,780],[840,1140],0.2)

SB_DVD = SB.Appliance(SB,2,8,2,120,0.1,5, occasional_use = 0.5)
SB_DVD.windows([480,780],[840,1140],0.2)

SB_Freezer = SB.Appliance(SB,1,200,1,1440,0,30, 'yes',3)
SB_Freezer.windows([0,1440])
SB_Freezer.specific_cycle_1(200,20,5,10)
SB_Freezer.specific_cycle_2(200,15,5,15)
SB_Freezer.specific_cycle_3(200,10,5,20)
SB_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

SB_PC = SB.Appliance(SB,1,50,2,210,0.1,10)
SB_PC.windows([480,780],[840,1140],0.35)

SB_Phone_charger = SB.Appliance(SB,3,2,2,180,0.2,5)
SB_Phone_charger.windows([480,780],[840,1140],0.35)