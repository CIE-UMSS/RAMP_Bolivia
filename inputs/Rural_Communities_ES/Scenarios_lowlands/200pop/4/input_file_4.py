# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:30:09 2022

@author: pietr
"""


'''
Paper: Energy sufficiency (SDEWES LA 2022)
User: Irrigation Water for lowlands agroproductive zone
'''

from core import User, np
User_list = []

###### IGA's  AGRICULTURAL ######

#Definig users IRRIGATION WATER


IW = User("Irrigation Water", 4)
User_list.append(IW)

#Appliances

IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)

#Definig users

LAU = User("Lowlands agro-productive unit", 1)
User_list.append(LAU)

#Appliances

LAU_GD = LAU.Appliance(LAU,1,9360,1,180,0.2,30,occasional_use = 0.33)
LAU_GD.windows([420,1080],[0,0],0.35)

LAU_VW = LAU.Appliance(LAU,1,1170,1,480,0.2,15,occasional_use = 0.82)
LAU_VW.windows([420,1140],[0,0],0.35)

####Safe configuration 

LAU_BT = LAU.Appliance(LAU,1,370,1,700,0.2,180)
LAU_BT.windows([300,1440],[0,0],0.35)


###### IGA's NON AGRICULTURAL ######

#Definig users GROCERY STORE

GS = User("Grocery Store 1", 2)
User_list.append(GS)

#Appliances
GS_indoor_bulb = GS.Appliance(GS,2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(GS,1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_freezer = GS.Appliance(GS,1,200,1,1440,0,30,'yes',3)
GS_freezer.windows([0,1440],[0,0])
GS_freezer.specific_cycle_1(200,20,5,10)
GS_freezer.specific_cycle_2(200,15,5,15)
GS_freezer.specific_cycle_3(200,10,5,20)
GS_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

GS_Radio = GS.Appliance(GS,1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)

#Definig users RESTAURANT

R = User("Restaurant", 2)
User_list.append(R)

#Appliances

R_indoor_bulb = R.Appliance(R,2,7,2,120,0.2,10)
R_indoor_bulb.windows([1107,1440],[0,30],0.35)

R_Blender = R.Appliance(R,1,350,2,20,0.375,5)
R_Blender.windows([420,480],[720,780],0.5)

R_freezer = R.Appliance(R,1,200,1,1440,0,30,'yes',3)
R_freezer.windows([0,1440],[0,0])
R_freezer.specific_cycle_1(200,20,5,10)
R_freezer.specific_cycle_2(200,15,5,15)
R_freezer.specific_cycle_3(200,10,5,20)
R_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#Definig users

WS = User("Workshop", 1)
User_list.append(WS)

#Appliances

WS_indoor_bulb = WS.Appliance(WS,2,7,2,120,0.2,10)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(WS,1,5500,1,60,0.5,30, occasional_use = 0.3)
WS_welding_machine.windows([0,1440],[0,0],0.35)

WS_grinding_machine = WS.Appliance(WS,1,750,1,480,0.2,60, occasional_use = 0.3)
WS_grinding_machine.windows([0,1440],[0,0],0.35)

WS_Radio = WS.Appliance(WS,1,36,2,60,0.1,5)
WS_Radio.windows([390,450],[1140,1260],0.35)


#Definig users

EB = User("Entertainment Business", 1)
User_list.append(EB)

#Appliances

EB_indoor_bulb = EB.Appliance(EB,2,7,2,120,0.2,10)
EB_indoor_bulb.windows([1107,1440],[0,30],0.35)

EB_outdoor_bulb = EB.Appliance(EB,1,13,2,600,0.2,10)
EB_outdoor_bulb.windows([0,330],[1107,1440],0.35)


EB_Stereo = EB.Appliance(EB,1,150,2,90,0.1,5, occasional_use = 0.33)
EB_Stereo.windows([480,780],[0,0],0.35)

EB_TV = EB.Appliance(EB,1,60,2,120,0.1,5, occasional_use = 0.33)
EB_TV.windows([480,780],[840,1140],0.2)
    
EB_PC = EB.Appliance(EB,1,50,2,210,0.1,10, occasional_use = 0.33)
EB_PC.windows([480,780],[840,1140],0.35)

EB_freezer = EB.Appliance(EB,1,200,1,1440,0,30,'yes',3)
EB_freezer.windows([0,1440],[0,0])
EB_freezer.specific_cycle_1(200,20,5,10)
EB_freezer.specific_cycle_2(200,15,5,15)
EB_freezer.specific_cycle_3(200,10,5,20)
EB_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])
