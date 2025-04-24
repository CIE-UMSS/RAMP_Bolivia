#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:03:07 2025

@author: claudia
"""


from ramp.core.core import User

User_list = []

HCS = User("household cold storage", 1)
User_list.append(HCS)

HCS_Freezer = HCS.add_appliance(1, 200, 1, 1440, 0, 30, "yes", 2) #Two cycles for cold season in ll
HCS_Freezer.windows([0, 1440], [0, 0])
HCS_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
HCS_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
HCS_Freezer.cycle_behaviour([300, 1200], [0, 0], [0, 299], [1201, 1440])