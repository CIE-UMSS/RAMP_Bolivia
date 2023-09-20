# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:12:30 2021

@author: Clau
"""

from core import User, np
User_list = []

'''
Paper: Energy sufficiency, lowlands.
User: Lowlands agro-productive unit
Flour_processing/grain processing
'''

#Definig users

LAU = User("Lowlands agro-productive unit", 1)
User_list.append(LAU)

#Appliances

# no need of a thresher because usally diesel is used as a fuel 

LAU_grain_dryer = LAU.Appliance(LAU,1,5000,1,180,0.2,30)
LAU_grain_dryer.windows([420,1080],[0,0],0.2)

LAU_grain_miller = LAU.Appliance(LAU,1,11700,1,180,0.2,30)
LAU_grain_miller.windows([420,1080],[0,0],0.2)

LAU_grain_toaster = LAU.Appliance(LAU,1,780,1,90,0.2,15)
LAU_grain_toaster.windows([420,1080],[0,0],0.2)

LAU_pump = LAU.Appliance(LAU,1,1700,2,60,0.2,10,occasional_use = 0.33)
LAU_pump.windows([420,720],[840,1020],0.35)