# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:12:30 2021

@author: Clau
"""

from core import User, np
User_list = []

'''
Paper: Energy sufficiency, lowlands.
User: HIGHLANDS agro-productive unit
'''

#Definig users

LAU = User("Lowlands agro-productive unit", 1)
User_list.append(LAU)

#Appliances

LAU_grain_dryer = LAU.Appliance(LAU,1,9360,1,180,0.2,30,occasional_use = 0.33)
LAU_grain_dryer.windows([420,1080],[0,0],0.35)

LAU_grain_miller = LAU.Appliance(LAU,1,11700,1,180,0.2,15,occasional_use = 0.33)
LAU_grain_miller.windows([420,1080],[0,0],0.35)

LAU_water_pump = LAU.Appliance(LAU,1,1170,1,480,0.2,15,occasional_use = 0.33)
LAU_water_pump.windows([420,1140],[0,0],0.35)

LAU_wool_clipper = LAU.Appliance(LAU,1,350,1,60,0.2,15,occasional_use = 0.33)
LAU_wool_clipper.windows([390,540],[0,0],0.35)

