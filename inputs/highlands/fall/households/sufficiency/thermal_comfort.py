#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 11:52:27 2025

@author: claudia
"""
from ramp.core.core import User

User_list = []

HTC= User("household thermal comfort", 1)
User_list.append(HTC)

HTC_heater = HTC.add_appliance(1,800,2,240,0.1,10, occasional_use = 0.66)
HTC_heater.windows([480,660],[1080,1200],0.35)