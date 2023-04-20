# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:57:23 2021

@author: Clau
"""

'''
Paper: Energy sufficiency (SDEWES LA 2022)
User: Irrigation Water for lowlands agroproductive zone
'''

from core import User, np
User_list = []

#Definig users

IW = User("Irrigation Water", 1)
User_list.append(IW)

#Appliances

IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)