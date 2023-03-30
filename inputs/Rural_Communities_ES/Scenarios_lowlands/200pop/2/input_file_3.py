# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:18:34 2022

@author: pietr
"""


from core import User, np
User_list = []

#Definig users

Public_lighting = User("Public lighting ", 7)
User_list.append(Public_lighting)

#Appliances

Public_lighting_lamp_post = Public_lighting.Appliance(Public_lighting,1,40,2,310,0,300, 'yes', flat = 'yes')
Public_lighting_lamp_post.windows([0,362],[1082,1440],0.1)

#Definig users

WSS = User("water supply system", 1)
User_list.append(WSS)

#Appliances

WSS_water_pump = WSS.Appliance(WSS,1,1700,2,60,0.2,10,occasional_use = 0.33)
WSS_water_pump.windows([420,720],[840,1020],0.35)
