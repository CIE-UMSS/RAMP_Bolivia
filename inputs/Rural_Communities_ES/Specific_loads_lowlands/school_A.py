# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:44:25 2021

@author: Clau
"""

'''
Paper: Energy sufficiency (SDEWES LA 2022)
User: School A
'''

from core import User, np
User_list = []

#Definig users

SA = User("School type A", 1)
User_list.append(SA)

#Appliances

SA_indoor_bulb = SA.Appliance(SA,6,7,2,120,0.25,30)
SA_indoor_bulb.windows([480,780],[840,1140],0.35)

SA_outdoor_bulb = SA.Appliance(SA,1,13,1,60,0.2,10)
SA_outdoor_bulb.windows([960,1080],[0,0],0.35)

SA_TV = SA.Appliance(SA,1,60,2,120,0.1,5, occasional_use = 0.5)
SA_TV.windows([480,780],[840,1140],0.2)

SA_radio = SA.Appliance(SA,3,4,2,120,0.1,5, occasional_use = 0.5)
SA_radio.windows([480,780],[840,1140],0.2)

SA_DVD = SA.Appliance(SA,1,8,2,120,0.1,5, occasional_use = 0.5)
SA_DVD.windows([480,780],[840,1140],0.2)