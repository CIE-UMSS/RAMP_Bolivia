#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:27:18 2023

@author: claudia

Molinero
"""
from core import User, np
User_list = []

#Users

HI = User("high income",6)
User_list.append(HI)

LI = User("low income",33)
User_list.append(LI)

HP = User("health post",1)
User_list.append(HP)

SA = User("type A school",1)
User_list.append(SA)

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


#Health post

HP_indoor_bulb = HP.Appliance(HP,6,7,2,690,0.2,10)
HP_indoor_bulb.windows([480,720],[870,1440],0.35)

HP_outdoor_bulb = HP.Appliance(HP,2,13,2,690,0.2,10)
HP_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HP_Phone_charger = HP.Appliance(HP,2,2,2,300,0.2,5)
HP_Phone_charger.windows([480,720],[900,1440],0.35)

HP_TV = HP.Appliance(HP,1,150,2,360,0.1,60)
HP_TV.windows([480,720],[780,1020],0.2)

HP_radio = HP.Appliance(HP,1,40,2,360,0.3,60)
HP_radio.windows([480,720],[780,1020],0.35)

HP_PC = HP.Appliance(HP,1,200,2,300,0.1,10, occasional_use=0.3)
HP_PC.windows([480,720],[1050,1440],0.35)

HP_printer = HP.Appliance(HP,1,100,1,60,0.3,10, occasional_use=0.3)
HP_printer.windows([540,1020],[0,0],0.35)

HP_sterilizer_stove = HP.Appliance(HP,1,600,2,120,0.3,30, occasional_use=0.2)
HP_sterilizer_stove.windows([480,720],[780,1020],0.35)

HP_needle_destroyer = HP.Appliance(HP,1,70,1,60,0.3,10, occasional_use=0.2)
HP_needle_destroyer.windows([480,720],[0,0],0.35)

HP_water_pump = HP.Appliance(HP,1,400,1,30,0.2,10, occasional_use=0.5)
HP_water_pump.windows([480,720],[0,0],0.35)

HP_Freezer = HP.Appliance(HP,1,200,1,1440,0,30,'yes',3)
HP_Freezer.windows([0,1440],[0,0])
HP_Freezer.specific_cycle_1(200,15,5,15)
HP_Freezer.specific_cycle_2(200,15,5,15)
HP_Freezer.specific_cycle_3(200,10,5,20)
HP_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#Type A school

SA_indoor_bulb = SA.Appliance(SA,6,7,2,120,0.25,30)
SA_indoor_bulb.windows([480,780],[840,1140],0.35)

SA_outdoor_bulb = SA.Appliance(SA,1,13,1,60,0.2,10)
SA_outdoor_bulb.windows([960,1080],[0,0],0.35)

SA_TV = SA.Appliance(SA,1,60,2,120,0.1,5, occasional_use = 0.5)
SA_TV.windows([480,780],[840,1140],0.2)

SA_radio = SA.Appliance(SA,3,4,2,120,0.1,5, occasional_use = 0.5)
SA_radio.windows([480,780],[840,1140],0.2)

SA_DVD = SA.Appliance(SA,1,8,2,120,0.1,5, occasional_use = 0.5)
SA_DVD.windows([480,780],[840,1140],0.2)
