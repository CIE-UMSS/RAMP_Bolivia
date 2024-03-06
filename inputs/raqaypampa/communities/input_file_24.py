#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:43:29 2023

@author: claudia

Salvia Centro
"""

from core import User, np
User_list = []

#Users
HI = User("high income",5)
User_list.append(HI)

LI = User("low income",29)
User_list.append(LI)


#Appliances

#High consumption household

HI_indoor_bulb = HI.Appliance(HI,3,7,1,300,0.2,180)
HI_indoor_bulb.windows([1080,1440],[0,0],0.35)

HI_outdoor_bulb = HI.Appliance(HI,1,13,1,320,0.2,120)
HI_outdoor_bulb.windows([1100,1440],[0,0],0.35)

HI_Radio = HI.Appliance(HI,1,7,2,280,0.2,120)
HI_Radio.windows([420,708],[840,1020],0.35)

HI_TV = HI.Appliance(HI,1,60,2,120,0.2,60)
HI_TV.windows([840,1080],[1140,1440],0.35)

HI_Phone_charger = HI.Appliance(HI,2,5,3,240,0.2,95)
HI_Phone_charger.windows([421,660],[1190,1440],0.35,[0,420])

HI_Freezer = HI.Appliance(HI,1,200,1,1440,0,30,'yes',3)
HI_Freezer.windows([0,1440],[0,0])
HI_Freezer.specific_cycle_1(200,15,5,15)
HI_Freezer.specific_cycle_2(200,15,5,15)
HI_Freezer.specific_cycle_3(200,10,5,20)
HI_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])


#Low consumption household

HI_indoor_bulb = HI.Appliance(HI,2,7,1,300,0.2,180)
HI_indoor_bulb.windows([1080,1440],[0,0],0.35)

HI_outdoor_bulb = HI.Appliance(HI,1,13,1,320,0.2,120)
HI_outdoor_bulb.windows([1100,1440],[0,0],0.35)

HI_Radio = HI.Appliance(HI,1,7,2,280,0.2,120)
HI_Radio.windows([420,708],[840,1020],0.35)

HI_TV = HI.Appliance(HI,1,60,2,120,0.2,60)
HI_TV.windows([840,1080],[1140,1440],0.35)

HI_Phone_charger = HI.Appliance(HI,1,5,3,240,0.2,95)
HI_Phone_charger.windows([421,660],[1190,1440],0.35,[0,420])