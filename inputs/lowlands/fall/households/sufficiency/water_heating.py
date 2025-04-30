#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 15:42:41 2025

@author: claudia
"""

from ramp.core.core import User
import pandas as pd

User_list = []

HWH = User("household water heating", 1)  # Create user with ID = 1
User_list.append(HWH)

HH_shower_P = pd.read_csv("data/LL_power_profile_water_heating.csv")

HWH_shower = HWH.add_appliance(1,5500,2,40,0.1,3, thermal_P_var = 0.2)
HWH_shower.windows([360,540],[1080,1260],0.2)