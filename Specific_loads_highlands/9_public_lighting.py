# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:39:40 2021

@author: Clau

Paper: Energy sufficiency (SDEWES LA 2022)
User: Public lighting - LOWLANDS
"""

from core import User, np
User_list = []


#Definig users

PL = User("Public lighting ", 1)
User_list.append(PL)

#Appliances

PL_lamp_post = PL.Appliance(PL,1,40,2,310,0,300, 'yes', flat = 'yes')
PL_lamp_post.windows([0,362],[1082,1440],0.1)