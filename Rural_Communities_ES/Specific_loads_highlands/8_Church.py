# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:41:40 2021

@author: Clau
"""

from core import User, np
User_list = []

'''
Paper: Energy sufficiency (SDEWES LA 2022)
User: Church - LOWLANDS
'''

#Definig users

CH = User("Church", 1)
User_list.append(CH)

#Church

CH_indoor_bulb = CH.Appliance(CH,10,26,1,210,0.2,60,'yes', flat = 'yes')
CH_indoor_bulb.windows([1200,1440],[0,0],0.1)

CH_outdoor_bulb = CH.Appliance(CH,7,26,1,240,0.2,60, 'yes', flat = 'yes')
CH_outdoor_bulb.windows([1200,1440],[0,0],0.1)

CH_speaker = CH.Appliance(CH,1,100,1,120,0.2,60, occasional_use=0.5)
CH_speaker.windows([1020,1260],[0,0],0.1)