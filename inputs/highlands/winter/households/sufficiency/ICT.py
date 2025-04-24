#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 15:13:55 2025

@author: claudia
"""

from ramp.core.core import User

User_list = []

HICT = User("household ICT", 1)
User_list.append(HICT)

HICT_TV = HICT.add_ppliance(1,30,2,120,0.1,5) 
HICT_TV.windows([1080,1440],[0,60],0.35)

HICT_Radio = HICT.add_appliance(1,36,2,120,0.1,5)
HICT_Radio.windows([390,450],[1082,1260],0.35)

HICT_Phone_charger = HICT.add_appliance(4,5,2,120,0.2,10)
HICT_Phone_charger.windows([1020,1440],[0,300],0.35)

HICT_Laptop = HICT.add_appliance(1,70,1,90,0.3,30)
HICT_Laptop.windows([960,1200],[0,0],0.35)