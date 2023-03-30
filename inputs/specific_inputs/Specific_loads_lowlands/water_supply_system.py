# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:08:08 2021

@author: Clau

Paper: Energy sufficiency (SDEWES LA 2022)
User: Public lighting - LOWLANDS
"""


from core import User, np
User_list = []


#Definig users

WSS = User("water supply system", 1)
User_list.append(WSS)

#Appliances

WSS_water_pump = WSS.Appliance(WSS,1,1700,2,60,0.2,10,occasional_use = 0.33)
WSS_water_pump.windows([420,720],[840,1020],0.35)
