#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:58:37 2025

@author: claudia
"""

from ramp.core.core import User

User_list = []

HCS = User("household cold storage", 1)
User_list.append(HCS)

HCS_Freezer = HCS.add_appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
HCS_Freezer.windows([0, 1440], [0, 0])
HCS_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
HCS_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
HCS_Freezer.cycle_behaviour(
    [330, 1139], [0, 0], [0, 329], [1140, 1440])