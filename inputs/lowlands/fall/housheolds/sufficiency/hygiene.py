#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 15:42:41 2025

@author: claudia
"""

from ramp.core.core import User

User_list = []

HH = User("household hygiene", 1)
User_list.append(HH)

HH_shower = HH.add_appliance(1,5500,2,40,0.1,3, thermal_P_var = 0.2)
HH_shower.windows([360,540],[1080,1260],0.2)