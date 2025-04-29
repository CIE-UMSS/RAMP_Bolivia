#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 15:40:05 2025

@author: claudia
"""
from ramp.core.core import User

User_list = []

HSC = User("household space cooling", 1)
User_list.append(HSC)

HSC_Fan = HSC.Appliance(1,30,2,400,0.27,30)
HSC_Fan.windows([600,1200],[0,0],0.35)