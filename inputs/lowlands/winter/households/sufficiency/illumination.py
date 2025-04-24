#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:01:59 2025

@author: claudia
"""

from ramp.core.core import User

User_list = []

HI = User("household illumination", 1)
User_list.append(HI)

HI_indoor_bulb = HI.add_appliance(4,7,3,360,0.2,10)
HI_indoor_bulb.windows([360,420],[1020,1440],0.35,[0,60])
         
HI_outdoor_bulb = HI.Appliance(2,14,1,240,0.2,10)
HI_outdoor_bulb.windows([1020,1380],[0,0],0.35)