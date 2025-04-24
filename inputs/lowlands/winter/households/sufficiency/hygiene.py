#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:06:09 2025

@author: claudia
"""

from ramp.core.core import User

User_list = []

HH = User("household hygiene", 1)
User_list.append(HH)

HH_shower = HH.add_appliance(1,5500,2,40,0.2,3, thermal_P_var = 0.3)
HH_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands