#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:11:28 2023

@author: claudia
Piedra Grande - Chuquisaca
"""

from ramp.core.core import User
User_list = []

H1 = User("low income household", 55) 
User_list.append(H1)

H2 = User("high income household", 2)
User_list.append(H2)

SB = User("School type B", 1)
User_list.append(SB)

PL = User("Public lighting ", 6)
User_list.append(PL)

GS = User("Grocery Store 1", 2)
User_list.append(GS)

R = User("Restaurant", 2)
User_list.append(R)

#Appliances
H1_indoor_bulb = H1.Appliance(H1,3,7,2,120,0.2,10)
H1_indoor_bulb.windows([1082,1440],[0,30],0.35)

H1_outdoor_bulb = H1.Appliance(H1,1,13,2,600,0.2,10)
H1_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H1_Radio = H1.Appliance(H1,1,36,2,60,0.1,5)
H1_Radio.windows([390,450],[1082,1260],0.35)

H1_TV = H1.Appliance(H1,1,60,3,90,0.1,5)
H1_TV.windows([750,840],[1082,1440],0.35)

H1_Phone_charger = H1.Appliance(H1,2,2,1,300,0.2,5)
H1_Phone_charger.windows([1080,1440],[0,0],0.35)

H2_indoor_bulb = H2.Appliance(H2,4,7,2,120,0.2,10)
H2_indoor_bulb.windows([1082,1440],[0,30],0.35)
         
H2_outdoor_bulb = H2.Appliance(H2,2,13,2,600,0.2,10)
H2_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H2_TV = H2.Appliance(H2,2,60,2,120,0.1,5)
H2_TV.windows([750,840],[1082,1440],0.35)

H2_DVD = H2.Appliance(H2,1,8,2,40,0.1,5,occasional_use = 0.3)
H2_DVD.windows([1082,1440],[0,0],0.35)

H2_Radio = H2.Appliance(H2,1,36,2,60,0.1,5)
H2_Radio.windows([390,450],[1082,1260],0.35)

H2_Phone_charger = H2.Appliance(H2,4,2,2,300,0.2,5)
H2_Phone_charger.windows([1110,1440],[0,0],0.35)

H2_Freezer = H2.Appliance(H2,1,200,1,1440,0,30,'yes',2)
H2_Freezer.windows([0,1440],[0,0])
H2_Freezer.specific_cycle_1(5,15,200,15)
H2_Freezer.specific_cycle_2(5,20,200,10)
H2_Freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

H2_Mixer = H2.Appliance(H2,1,50,3,30,0.1,1, occasional_use = 0.33)
H2_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

H2_Laptop = H2.Appliance(H2,1,70,1,90,0.3,30)
H2_Laptop.windows([960,1200],[0,0],0.35)

SB_indoor_bulb = SB.Appliance(SB,12,7,2,120,0.25,30)
SB_indoor_bulb.windows([480,780],[840,1140],0.35)

SB_outdoor_bulb = SB.Appliance(SB,3,13,1,60,0.2,10)
SB_outdoor_bulb.windows([960,1080],[0,0],0.35)

SB_TV = SB.Appliance(SB,1,60,2,120,0.1,5, occasional_use = 0.5)
SB_TV.windows([480,780],[840,1140],0.2)

SB_radio = SB.Appliance(SB,3,4,2,120,0.1,5, occasional_use = 0.5)
SB_radio.windows([480,780],[840,1140],0.2)

SB_DVD = SB.Appliance(SB,2,8,2,120,0.1,5, occasional_use = 0.5)
SB_DVD.windows([480,780],[840,1140],0.2)

SB_PC = SB.Appliance(SB,1,50,2,210,0.1,10)
SB_PC.windows([480,780],[840,1140],0.35)

SB_Phone_charger = SB.Appliance(SB,3,2,2,180,0.2,5)
SB_Phone_charger.windows([480,780],[840,1140],0.35)

PL_lamp_post = PL.Appliance(PL,1,40,2,310,0,300, 'yes', flat = 'yes')
PL_lamp_post.windows([0,362],[1082,1440],0.1)

GS_indoor_bulb = GS.Appliance(GS,2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(GS,1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_Freezer = GS.Appliance(GS,1,200,1,1440,0,30,'yes',2)
GS_Freezer.windows([0,1440],[0,0])
GS_Freezer.specific_cycle_1(5,15,200,15)
GS_Freezer.specific_cycle_2(5,20,200,10)
GS_Freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

GS_Radio = GS.Appliance(GS,1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)

R_indoor_bulb = R.Appliance(R,2,7,2,120,0.2,10)
R_indoor_bulb.windows([1107,1440],[0,30],0.35)

R_Blender = R.Appliance(R,1,350,2,20,0.375,5)
R_Blender.windows([420,480],[720,780],0.5)

R_freezer = R.Appliance(R,1,200,1,1440,0,30,'yes',2)
R_freezer.windows([0,1440],[0,0])
R_freezer.specific_cycle_1(5,15,200,15)
R_freezer.specific_cycle_2(5,20,200,10)
R_freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])