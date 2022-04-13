# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:50:31 2021

@author: Clau

Paper: Energy sufficiency (SDEWES LA 2022)
User: Coliseum - LOWLANDS
"""

from core import User, np
User_list = []


#Definig users

CO = User("Coliseum", 1)
User_list.append(CO)

#Appliances

CO_lights = CO.Appliance(CO, 10,150,2,310,0.1,300, 'yes', flat = 'yes')
CO_lights.windows([0,336],[1110,1440],0.2)