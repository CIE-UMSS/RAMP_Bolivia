# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:28:30 2022

@author: pietr
"""
'''
Paper: Energy sufficiency, lowlands.
User: Low Income Household
'''

from core import User, np
User_list = []

###### COMMUNITY SERVICES ######

#Definig users

Public_lighting = User("Public lighting ", 26)
User_list.append(Public_lighting)

#Appliances

Public_lighting_lamp_post = Public_lighting.Appliance(Public_lighting,1,40,2,310,0,300, 'yes', flat = 'yes')
Public_lighting_lamp_post.windows([0,362],[1082,1440],0.1)


WSS = User("water supply system", 3)
User_list.append(WSS)

#Appliances

WSS_water_pump = WSS.Appliance(WSS,1,1700,2,60,0.2,10,occasional_use = 0.33)
WSS_water_pump.windows([420,720],[840,1020],0.35)

