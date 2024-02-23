#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:23:50 2023

@author: claudia

Highlands

JUNUTA CONDOROCA - La Paz

"""

from core import User, np
User_list = []

#users

HI = User("high income",23)
User_list.append(HI)

LI = User("low income",394)
User_list.append(LI)

HC = User("health center",1)
User_list.append(HC)

SC = User("school type C",1)
User_list.append(SC)

PL = User("public lighting",42)
User_list.append(PL)

CH = User("church",1)
User_list.append(CH)

R = User("Restaurant", 13)
User_list.append(R)

CO = User("Coliseum", 1)
User_list.append(CO)

GS = User("Grocery Store 1", 15)
User_list.append(GS)

WSS = User("water supply system", 3)
User_list.append(WSS)

WS = User("Workshop", 5)
User_list.append(WS)

Quinoa = User("Lowlands agro-productive unit", 1)
User_list.append(Quinoa)

EB = User("Entertainment Business", 1)
User_list.append(EB)

IW = User("Irrigation Water", 1)
User_list.append(IW)

#Appliances

#high income households
HI_indoor_bulb = HI.Appliance(HI,4,7,2,120,0.2,10)
HI_indoor_bulb.windows([1082,1440],[0,30],0.35)
         
HI_outdoor_bulb = HI.Appliance(HI,2,13,2,600,0.2,10)
HI_outdoor_bulb.windows([0,330],[1082,1440],0.35)

HI_TV = HI.Appliance(HI,1,60,2,120,0.1,5)
HI_TV.windows([750,840],[1082,1440],0.35)

HI_DVD = HI.Appliance(HI,1,8,2,40,0.1,5)
HI_DVD.windows([750,840],[1082,1440],0.35)

HI_Radio = HI.Appliance(HI,1,36,2,60,0.1,5)
HI_Radio.windows([390,450],[1082,1260],0.35)

HI_Phone_charger = HI.Appliance(HI,4,2,2,300,0.2,5)
HI_Phone_charger.windows([1110,1440],[0,0],0.35)

HI_Freezer = HI.Appliance(HI,1,200,1,1440,0,30,'yes',3)
HI_Freezer.windows([0,1440],[0,0])
HI_Freezer.specific_cycle_1(200,15,5,15)
HI_Freezer.specific_cycle_2(200,15,5,15)
HI_Freezer.specific_cycle_3(200,10,5,20)
HI_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

HI_Mixer = HI.Appliance(HI,1,50,3,30,0.1,1, occasional_use = 0.33)
HI_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

HI_Iron = HI.Appliance(HI,1,1000,2,15,0.2,5,occasional_use =0.33)
HI_Iron.windows([420,480],[720,780],0.35)

HI_Laptop = HI.Appliance(HI,1,70,1,90,0.3,30)
HI_Laptop.windows([960,1200],[0,0],0.35)


#low income households

LI_indoor_bulb = LI.Appliance(LI,3,7,2,120,0.2,10)
LI_indoor_bulb.windows([1082,1440],[0,30],0.35)

LI_outdoor_bulb = LI.Appliance(LI,1,13,2,600,0.2,10)
LI_outdoor_bulb.windows([0,330],[1082,1440],0.35)

LI_TV = LI.Appliance(LI,1,60,2,90,0.1,5)
LI_TV.windows([750,840],[1082,1440],0.35)

LI_Radio = LI.Appliance(LI,1,36,2,60,0.1,5)
LI_Radio.windows([390,450],[1082,1260],0.35)

LI_Phone_charger = LI.Appliance(LI,2,2,1,300,0.2,5)
LI_Phone_charger.windows([1080,1440],[0,0],0.35)

#health center

HC_indoor_bulb = HC.Appliance(HC,20,7,2,690,0.2,10)
HC_indoor_bulb.windows([480,720],[870,1440],0.35)

HC_outdoor_bulb = HC.Appliance(HC,5,13,2,690,0.2,10)
HC_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HC_Phone_charger = HC.Appliance(HC,5,2,2,300,0.2,5)
HC_Phone_charger.windows([480,720],[900,1440],0.35)

HC_TV = HC.Appliance(HC,2,150,2,360,0.1,60)
HC_TV.windows([480,720],[780,1020],0.2)

HC_radio = HC.Appliance(HC,5,40,2,360,0.3,60)
HC_radio.windows([480,720],[780,1020],0.35)

HC_PC = HC.Appliance(HC,2,200,2,300,0.1,10)
HC_PC.windows([480,720],[1050,1440],0.35)

HC_printer = HC.Appliance(HC,2,100,1,60,0.3,10)
HC_printer.windows([540,1020],[0,0],0.35)

HC_sterilizer_stove = HC.Appliance(HC,3,600,2,120,0.3,30, occasional_use=0.33)
HC_sterilizer_stove.windows([480,720],[780,1020],0.35)

HC_needle_destroyer = HC.Appliance(HC,1,70,1,60,0.3,10, occasional_use=0.33)
HC_needle_destroyer.windows([480,720],[0,0],0.35)

HC_water_pump = HC.Appliance(HC,1,400,1,45,0.2,10)
HC_water_pump.windows([480,720],[0,0],0.35)

HC_Freezer = HC.Appliance(HC,3,200,1,1440,0,30,'yes',3)
HC_Freezer.windows([0,1440],[0,0])
HC_Freezer.specific_cycle_1(200,15,5,15)
HC_Freezer.specific_cycle_2(200,15,5,15)
HC_Freezer.specific_cycle_3(200,10,5,20)
HC_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

HC_microscope = HC.Appliance(HC,2,3,2,120,0.2,10, occasional_use=0.33)
HC_microscope.windows([480,720],[840,960],0.35)

HC_shower = HC.Appliance(HC,3,3000,2,60,0.1,15, occasional_use=0.33)
HC_shower.windows([360,720],[780,1400],0.35)

HC_heater = HC.Appliance(HC,2,1500,2,160,0.25,60, occasional_use=0.33)
HC_heater.windows([369,720],[1080,1260],0.35)

HC_dental_compresor = HC.Appliance(HC,2,500,2,60,0.15,10, occasional_use=0.33)
HC_dental_compresor.windows([480,720],[840,1260],0.35)

HC_centrifuge = HC.Appliance(HC,2,100,1,60,0.15,10, occasional_use=0.33)
HC_centrifuge.windows([480,720],[0,0],0.35)

HC_serological_rotator = HC.Appliance(HC,2,10,1,60,0.25,15, occasional_use=0.33)
HC_serological_rotator.windows([480,720],[0,0],0.35)

#school type c
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

SC_Freezer = SC.Appliance(SC,1,200,1,1440,0,30,'yes',3)
SC_Freezer.windows([0,1440],[0,0])
SC_Freezer.specific_cycle_1(200,15,5,15)
SC_Freezer.specific_cycle_2(200,15,5,15)
SC_Freezer.specific_cycle_3(200,10,5,20)
SC_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

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

#church

CH_indoor_bulb = CH.Appliance(CH,10,26,1,210,0.2,60,'yes', flat = 'yes')
CH_indoor_bulb.windows([1200,1440],[0,0],0.1)

CH_outdoor_bulb = CH.Appliance(CH,7,26,1,240,0.2,60, 'yes', flat = 'yes')
CH_outdoor_bulb.windows([1200,1440],[0,0],0.1)

CH_speaker = CH.Appliance(CH,1,100,1,120,0.2,60, occasional_use=0.5)
CH_speaker.windows([1020,1260],[0,0],0.1)

#public lighting

PL_lamp_post = PL.Appliance(PL,1,40,2,310,0,300, 'yes', flat = 'yes')
PL_lamp_post.windows([0,362],[1082,1440],0.1)

#coliseum
CO_lights = CO.Appliance(CO, 10,150,2,310,0.1,300, 'yes', flat = 'yes')
CO_lights.windows([0,336],[1110,1440],0.2)

#WSS

WSS_water_pump = WSS.Appliance(WSS,1,1700,2,60,0.2,10,occasional_use = 0.33)
WSS_water_pump.windows([420,720],[840,1020],0.35)

#restaurant

R_indoor_bulb = R.Appliance(R,2,7,2,120,0.2,10)
R_indoor_bulb.windows([1107,1440],[0,30],0.35)

R_Blender = R.Appliance(R,1,350,2,20,0.375,5)
R_Blender.windows([420,480],[720,780],0.5)

R_Freezer = R.Appliance(R,1,200,1,1440,0,30,'yes',3)
R_Freezer.windows([0,1440],[0,0])
R_Freezer.specific_cycle_1(200,20,5,15)
R_Freezer.specific_cycle_2(200,15,5,15)
R_Freezer.specific_cycle_3(200,10,5,20)
R_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#grocery store

GS_indoor_bulb = GS.Appliance(GS,2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(GS,1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_Freezer = GS.Appliance(GS,1,200,1,1440,0,30,'yes',3)
GS_Freezer.windows([0,1440],[0,0])
GS_Freezer.specific_cycle_1(200,15,5,15)
GS_Freezer.specific_cycle_2(200,15,5,15)
GS_Freezer.specific_cycle_3(200,10,5,20)
GS_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

GS_Radio = GS.Appliance(GS,1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)

#entertainment business
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

EB_Freezer = EB.Appliance(EB,1,200,1,1440,0,30,'yes',3)
EB_Freezer.windows([0,1440],[0,0])
EB_Freezer.specific_cycle_1(200,15,5,15)
EB_Freezer.specific_cycle_2(200,15,5,15)
EB_Freezer.specific_cycle_3(200,10,5,20)
EB_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#workshop

WS_indoor_bulb = WS.Appliance(WS,2,7,2,120,0.2,10)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(WS,1,5500,1,60,0.5,30, occasional_use = 0.3)
WS_welding_machine.windows([0,1440],[0,0],0.35)

WS_grinding_machine = WS.Appliance(WS,1,750,1,480,0.2,60, occasional_use = 0.3)
WS_grinding_machine.windows([0,1440],[0,0],0.35)

WS_Radio = WS.Appliance(WS,1,36,2,60,0.1,5)
WS_Radio.windows([0,930],[1140,1260],0.35)

#irrigation

IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)

#trnasformation
Quinoa_washing_machine = Quinoa.Appliance(Quinoa,1,1500,1,300,0.1,15)
Quinoa_washing_machine.windows([420,1080],[0,0],0.1) #  [7 to 18 ]
        
# Flour processing
LAU_grain_dryer = Quinoa.Appliance(Quinoa,1,5000,1,180,0.2,30)
LAU_grain_dryer.windows([420,1080],[0,0],0.2)

LAU_grain_miller = Quinoa.Appliance(Quinoa,1,11700,1,180,0.2,30)
LAU_grain_miller.windows([420,1080],[0,0],0.2)

LAU_grain_toaster = Quinoa.Appliance(Quinoa,1,780,1,90,0.2,15)
LAU_grain_toaster.windows([420,1080],[0,0],0.2)

# no need of a thresher because usally diesel is used as a fuel 