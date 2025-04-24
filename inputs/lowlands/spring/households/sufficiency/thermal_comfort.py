#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 15:48:39 2025

@author: claudia
"""

from ramp.core.core import User

User_list = []

HSC = User("household space cooling", 1)
User_list.append(HSC)

HSC_Fan = HSC.add_appliance(4,30,2,540,0.27,30)
HSC_Fan.windows([540,1200],[0,0],0.35)