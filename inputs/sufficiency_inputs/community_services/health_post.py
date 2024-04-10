# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:56:48 2021

@author: Clau
"""

'''
Paper: Energy sufficiency (SDEWES LA 2022)
User: Health Post - LOWLANDS
'''

from core import User, np
User_list = []

#Defining users
HP = User("Health post", 1)
User_list.append(HP)

#Appliances

HP_indoor_bulb = HP.Appliance(HP,12,7,2,690,0.2,10)
HP_indoor_bulb.windows([480,720],[870,1440],0.35)

HP_outdoor_bulb = HP.Appliance(HP,1,13,2,690,0.2,10)
HP_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HP_Phone_charger = HP.Appliance(HP,5,2,2,300,0.2,5)
HP_Phone_charger.windows([480,720],[900,1440],0.35)

HP_TV = HP.Appliance(HP,1,150,2,360,0.1,60)
HP_TV.windows([480,720],[780,1020],0.2)

HP_radio = HP.Appliance(HP,1,40,2,360,0.3,60)
HP_radio.windows([480,720],[780,1020],0.35)

HP_PC = HP.Appliance(HP,1,200,2,300,0.1,10)
HP_PC.windows([480,720],[1050,1440],0.35)

HP_printer = HP.Appliance(HP,1,100,1,60,0.3,10)
HP_printer.windows([540,1020],[0,0],0.35)

HP_sterilizer_stove = HP.Appliance(HP,1,600,2,120,0.3,30, occasional_use=0.33)
HP_sterilizer_stove.windows([480,720],[780,1020],0.35)

HP_needle_destroyer = HP.Appliance(HP,1,70,1,60,0.3,10, occasional_use=0.33)
HP_needle_destroyer.windows([480,720],[0,0],0.35)

HP_water_pump = HP.Appliance(HP,1,400,1,30,0.2,10)
HP_water_pump.windows([480,720],[0,0],0.35)

HP_Freezer = HP.Appliance(HP,1,200,1,1440,0,30,'yes',3)
HP_Freezer.windows([0,1440],[0,0])
HP_Freezer.specific_cycle_1(200,15,5,15)
HP_Freezer.specific_cycle_2(200,15,5,15)
HP_Freezer.specific_cycle_3(200,10,5,20)
HP_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

