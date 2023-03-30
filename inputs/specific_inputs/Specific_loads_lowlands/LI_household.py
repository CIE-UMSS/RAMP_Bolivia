# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:59:29 2021

@author: Clau
"""

'''
Paper: Energy sufficiency (SDEWES LA 2022)
User: Low Income Household - LOWLANDS
'''

from core import User, np
User_list = []

#Defining users
H1 = User("low income household", 1) 
User_list.append(H1)
    
#Appliances
H1_indoor_bulb = H1.Appliance(H1,3,7,2,120,0.2,10)
H1_indoor_bulb.windows([1082,1440],[0,30],0.35)

H1_outdoor_bulb = H1.Appliance(H1,1,13,2,600,0.2,10)
H1_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H1_TV = H1.Appliance(H1,1,60,3,90,0.1,5)
H1_TV.windows([750,840],[1082,1440],0.35,[0,30])

H1_Antenna = H1.Appliance(H1,1,8,3,90,0.1,5)
H1_Antenna.windows([750,840],[1082,1440],0.35,[0,30])

H1_Phone_charger = H1.Appliance(H1,2,2,1,300,0.2,5)
H1_Phone_charger.windows([1080,1440],[0,0],0.35)

