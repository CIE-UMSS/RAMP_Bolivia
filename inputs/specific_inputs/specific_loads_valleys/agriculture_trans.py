# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:12:30 2021

@author: Clau
"""

from core import User, np
User_list = []

'''
Paper: Energy sufficiency, lowlands.
User: Lowlands agro-productive unit
Dairy : milk production 
'''

#Definig users

MILK = User("Lowlands agro-productive unit", 1)
User_list.append(MILK)

#Appliances

MILK_indoor_bulb = MILK.Appliance(MILK,2,7,2,120,0.2,10)
MILK_indoor_bulb.windows([1107,1440],[0,0],0.35)
    
MILK_outdoor_bulb = MILK.Appliance(MILK,1,13,2,600,0.2,10)                    
MILK_outdoor_bulb.windows([0,330],[1107,1440],0.35)     

MILK_cooler_tank = MILK.Appliance(MILK,1,4000,2,480,0,240)                    
MILK_cooler_tank.windows([360,600],[1080,1320],0.2)   