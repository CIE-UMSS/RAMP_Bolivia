#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 15:54:52 2025

@author: claudia
"""

from ramp.core.core import User

User_list = []

HI = User("household illumination", 1)
User_list.append(HI)

HI_indoor_bulb = HI.add_appliance(4,7,2,360,0.2,10)
HI_indoor_bulb.windows([300,420],[1020,1440],0.35)
         
HI_outdoor_bulb = HI.add_appliance(2,14,1,180,0.2,10)
HI_outdoor_bulb.windows([1140,1380],[0,0],0.35)