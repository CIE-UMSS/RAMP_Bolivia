#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:24:16 2023

@author: claudia

Quimome, Beni
"""

from core import User, np
User_list = []

H1 = User("low income household", 172) 
User_list.append(H1)

H2 = User("high income household", 70)
User_list.append(H2)
    
SC = User("School type C", 1)
User_list.append(SC)

R = User("Restaurant", 6)
User_list.append(R)

GS = User("Grocery Store 1", 6)
User_list.append(GS)

IW = User("Irrigation Water", 1)
User_list.append(IW)

HP = User("Health post", 1)
User_list.append(HP)

WS = User("Workshop", 3)
User_list.append(WS)

PL = User("Public lighting ", 20)
User_list.append(PL)

EB = User("Entertainment Business", 1)
User_list.append(EB)

LAU = User("Lowlands agro-productive unit", 1)
User_list.append(LAU)
#Appliances

#low income households
H1_indoor_bulb = H1.Appliance(H1,3,7,2,120,0.2,10)
H1_indoor_bulb.windows([1082,1440],[0,30],0.35)

H1_outdoor_bulb = H1.Appliance(H1,1,13,2,600,0.2,10)
H1_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H1_TV = H1.Appliance(H1,1,60,3,90,0.1,5)
H1_TV.windows([750,840],[1082,1440],0.35)

H1_Antenna = H1.Appliance(H1,1,8,3,90,0.1,5)
H1_Antenna.windows([750,840],[1082,1440],0.35)

H1_Phone_charger = H1.Appliance(H1,2,2,1,300,0.2,5)
H1_Phone_charger.windows([1080,1440],[0,0],0.35)

#high income households

H2_indoor_bulb = H2.Appliance(H2,4,7,2,120,0.2,10)
H2_indoor_bulb.windows([1082,1440],[0,30],0.35)
         
H2_outdoor_bulb = H2.Appliance(H2,2,13,2,600,0.2,10)
H2_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H2_TV = H2.Appliance(H2,2,60,2,120,0.1,5)
H2_TV.windows([1082,1440],[0,60],0.35)

H2_DVD = H2.Appliance(H2,1,8,2,40,0.1,5)
H2_DVD.windows([1082,1440],[0,60],0.35)

H2_Antenna = H2.Appliance(H2,1,8,2,80,0.1,5)
H2_Antenna.windows([1082,1440],[0,60],0.35)

H2_Radio = H2.Appliance(H2,1,36,2,60,0.1,5)
H2_Radio.windows([390,450],[1082,1260],0.35)

H2_Phone_charger = H2.Appliance(H2,4,2,2,300,0.2,5)
H2_Phone_charger.windows([1110,1440],[0,30],0.35)

H2_Freezer = H2.Appliance(H2,1,200,1,1440,0,30, 'yes',3)
H2_Freezer.windows([0,1440],[0,0])
H2_Freezer.specific_cycle_1(200,20,5,10)
H2_Freezer.specific_cycle_2(200,15,5,15)
H2_Freezer.specific_cycle_3(200,10,5,20)
H2_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

H2_Mixer = H2.Appliance(H2,1,50,3,30,0.1,1, occasional_use = 0.33)
H2_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

H2_Fan = H2.Appliance(H2,1,30,1,220,0.27,60)
H2_Fan.windows([720,1080],[0,0],0.35)

H2_Laptop = H2.Appliance(H2,1,70,1,90,0.3,30)
H2_Laptop.windows([960,1200],[0,0],0.35)

#school B

SC_indoor_bulb = SC.Appliance(SC,27,7,1,60,0.2,10)
SC_indoor_bulb.windows([480,780],[0,0],0.35)

SC_outdoor_bulb = SC.Appliance(SC,7,13,1,60,0.2,10)
SC_outdoor_bulb.windows([480,780],[0,0],0.35)

SC_TV = SC.Appliance(SC,5,60,1,120,0.1,5, occasional_use = 0.5)
SC_TV.windows([480,780],[0,0],0.35)

SC_radio = SC.Appliance(SC,24,4,1,120,0.1,5, occasional_use = 0.5)
SC_radio.windows([480,780],[0,0],0.35)

SC_DVD = SC.Appliance(SC,2,8,1,120,0.1,5, occasional_use = 0.5)
SC_DVD.windows([480,780],[0,0],0.35)

SC_Freezer = SC.Appliance(SC,1,200,1,1440,0,30, 'yes',3)
SC_Freezer.windows([0,1440])
SC_Freezer.specific_cycle_1(200,20,5,10)
SC_Freezer.specific_cycle_2(200,15,5,15)
SC_Freezer.specific_cycle_3(200,10,5,20)
SC_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

SC_PC = SC.Appliance(SC,25,50,1,210,0.1,10)
SC_PC.windows([480,780],[0,0],0.35)

SC_Phone_charger = SC.Appliance(SC,5,2,1,180,0.2,5)
SC_Phone_charger.windows([480,780],[0,0],0.35)

SC_Printer = SC.Appliance(SC,1,20,1,30,0.1,5)
SC_Printer.windows([480,780],[0,0],0.35)

SC_Stereo = SC.Appliance(SC,1,150,1,90,0.1,5, occasional_use = 0.33)
SC_Stereo.windows([480,780],[0,0],0.35)

SC_data = SC.Appliance(SC,1,420,1,60,0.1,5, occasional_use = 0.33)
SC_data.windows([480,780],[0,0],0.35)

#restaurante

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

#Grocety store

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


IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)


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

HP_fan = HP.Appliance(HP,2,60,1,240,0.2,60)
HP_fan.windows([660,1080],[0,0],0.35)

HP_sterilizer_stove = HP.Appliance(HP,1,600,2,120,0.3,30, occasional_use=0.33)
HP_sterilizer_stove.windows([480,720],[780,1020],0.35)

HP_needle_destroyer = HP.Appliance(HP,1,70,1,60,0.3,10, occasional_use=0.33)
HP_needle_destroyer.windows([480,720],[0,0],0.35)

HP_water_pump = HP.Appliance(HP,1,400,1,30,0.2,10)
HP_water_pump.windows([480,720],[0,0],0.35)

HP_Fridge = HP.Appliance(HP,3,150,1,1440,0,30, 'yes',3)
HP_Fridge.windows([0,1440],[0,0])
HP_Fridge.specific_cycle_1(150,20,5,10)
HP_Fridge.specific_cycle_2(150,15,5,15)
HP_Fridge.specific_cycle_3(150,10,5,20)
HP_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

WS_indoor_bulb = WS.Appliance(WS,2,7,2,120,0.2,10)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(WS,1,5500,1,60,0.5,30, occasional_use = 0.3)
WS_welding_machine.windows([0,1440],[0,0],0.35)

WS_grinding_machine = WS.Appliance(WS,1,750,1,480,0.2,60, occasional_use = 0.3)
WS_grinding_machine.windows([0,1440],[0,0],0.35)

WS_Radio = WS.Appliance(WS,1,36,2,60,0.1,5)
WS_Radio.windows([390,450],[1140,1260],0.35)

PL_lamp_post = PL.Appliance(PL,1,40,2,310,0,300, 'yes', flat = 'yes')
PL_lamp_post.windows([0,362],[1082,1440],0.1)

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

LAU_grain_dryer = LAU.Appliance(LAU,1,5000,1,180,0.2,30)
LAU_grain_dryer.windows([420,1080],[0,0],0.2)

LAU_grain_miller = LAU.Appliance(LAU,1,11700,1,180,0.2,30)
LAU_grain_miller.windows([420,1080],[0,0],0.2)

LAU_grain_toaster = LAU.Appliance(LAU,1,780,1,90,0.2,15)
LAU_grain_toaster.windows([420,1080],[0,0],0.2)

LAU_pump = LAU.Appliance(LAU,1,1700,2,60,0.2,10,occasional_use = 0.33)
LAU_pump.windows([420,720],[840,1020],0.35)