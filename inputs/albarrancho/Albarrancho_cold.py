# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:04:30 2021

@author: ClauLSS
"""

from core import User, np
User_list = []

'''
Dairy farming community - cold months (may-ago)
'''
#User classes definition

LMI = User("low middle income households",30)
User_list.append(LMI)

OF = User("Office",1)
User_list.append(OF)

PP = User("Poligeneration Plant",1)
User_list.append(PP)

MM = User("milking machine",15)
User_list.append(MM)

#Appliances definition
#Low-middle income households

LMI_indoor_bulb = LMI.Appliance(LMI,6,7,2,120,0.2,10)
LMI_indoor_bulb.windows([1069,1440],[0,30],0.35)

LMI_outdoor_bulb = LMI.Appliance(LMI,2,13,2,600,0.2,10)
LMI_outdoor_bulb.windows([0,330],[1069,1440],0.35)

LMI_Radio = LMI.Appliance(LMI,1,36,2,60,0.1,5)
LMI_Radio.windows([390,450],[1069,1260],0.35)

LMI_TV = LMI.Appliance(LMI,1,60,3,180,0.1,5)
LMI_TV.windows([720,900],[1069,1440],0.35,[0,60])

LMI_Phone_charger = LMI.Appliance(LMI,5,2,2,300,0.2,5)
LMI_Phone_charger.windows([1110,1440],[0,30],0.35)

LMI_Laptop = LMI.Appliance(LMI,1,70,1,90,0.3,30)
LMI_Laptop.windows([960,1200],[0,0])

LMI_Freezer = LMI.Appliance(LMI,1,200,1,1440,0,30,'yes',2)
LMI_Freezer.windows([0,1440],[0,0])
LMI_Freezer.specific_cycle_1(5,15,200,15)
LMI_Freezer.specific_cycle_2(5,20,200,10)
LMI_Freezer.cycle_behaviour([420,1139],[0,0],[0,419],[1140,1440])

LMI_Mixer = LMI.Appliance(LMI,1,50,3,30,0.1,1,occasional_use = 0.33)
LMI_Mixer.windows([420,480],[660,750],0.35,[1140,1200])

LMI_Water_pump = LMI.Appliance(LMI,1,250,2,60,0.3,10)
LMI_Water_pump.windows([420,450],[960,1020],0.3)


#Office

OF_indoor_bulb = OF.Appliance(OF,2,7,1,60,0.2,10)
OF_indoor_bulb.windows([480,780],[0,0],0.35)

OF_Phone_charger = OF.Appliance(OF,5,2,2,180,0.2,5)
OF_Phone_charger.windows([480,780],[0,0],0.35)

OF_PC = OF.Appliance(OF,1,50,2,210,0.1,10)
OF_PC.windows([480,780],[0,0],0.35)

OF_Printer = OF.Appliance(OF,1,20,2,30,0.1,5)
OF_Printer.windows([480,780],[0,0],0.35)


#Poligeneration Plant

PP_lighting = PP.Appliance(PP,8,100,2,690,0.2,240)
PP_lighting.windows([1080,1440],[0,420],0.2)

PP_control_system = PP.Appliance(PP,1,400,1,1440,0,30)
PP_control_system.windows([0,1440],[0,0])

PP_digester_pump = PP.Appliance(PP,1,500,2,720,0.1,60)
PP_digester_pump.windows([1140,1440],[0,540],0.2)

PP_agitator = PP.Appliance(PP,2,150,3,90,0.1,20)
PP_agitator.windows([0,60],[480,540],0.1,[960,1020])

PP_ARS = PP.Appliance(PP,1,200,3,540,0.1,60)
PP_ARS.windows([0,240],[660,960],0.1,[1320,1440])

PP_BDS = PP.Appliance(PP,1,500,3,540,0.1,60)
PP_BDS.windows([0,240],[660,960],0.1,[1320,1440])

PP_compressor = PP.Appliance(PP,1,1000,1,1440,0,60)
PP_compressor.windows([0,1440],[0,0])

#Milking machine

MM_milking_machine = MM.Appliance(MM,1,800,2,120,0.3,60)
MM_milking_machine.windows([300,480],[960,1080],0.3)

