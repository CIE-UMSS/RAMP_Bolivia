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
'''

#Definig users

LAU = User("Lowlands agro-productive unit", 1)
User_list.append(LAU)

#Appliances

LAU_GD = LAU.Appliance(LAU,1,9360,1,180,0.2,30,occasional_use = 0.33)
LAU_GD.windows([420,1080],[0,0],0.35)

LAU_VW = LAU.Appliance(LAU,1,1170,1,480,0.2,15,occasional_use = 0.82)
LAU_VW.windows([420,1140],[0,0],0.35)

LAU_BT = LAU.Appliance(LAU,1,370,2,900,0.2,180)
LAU_BT.windows([360,930],[1080,1440],0.35)