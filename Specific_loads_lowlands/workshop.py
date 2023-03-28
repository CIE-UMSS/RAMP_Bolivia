# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:10:34 2021

@author: Clau
"""

from core import User, np
User_list = []

'''
Paper: Energy sufficiency (SDEWES LA 2022)
User: Workshop - LOWLANDS
'''

#Definig users

WS = User("Workshop", 1)
User_list.append(WS)

#Appliances

WS_indoor_bulb = WS.Appliance(WS,2,7,2,120,0.2,10)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(WS,1,5500,1,60,0.5,30, occasional_use = 0.3)
WS_welding_machine.windows([0,1440],[0,0],0.35)

WS_grinding_machine = WS.Appliance(WS,1,750,1,480,0.2,60, occasional_use = 0.3)
WS_grinding_machine.windows([0,1440],[0,0],0.35)

WS_Radio = WS.Appliance(WS,1,36,2,60,0.1,5)
WS_Radio.windows([390,450],[1140,1260],0.35)