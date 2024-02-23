# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:16:36 2021

@author: Claudia
"""

#Demand Scenario Creator

import numpy as np
import pandas as pd
from core import User, np
User_list = []

class community:
    
    def __init__(self, Alt, P, PPH, PR, Dist):
        self.Altitude = Alt
        self.Population = P
        self.People_per_household = PPH 
        self.Poverty_rate = PR
        self.Distance_from_other_comm = Dist

Alt = int(input("Altitude:")) #altitudeMasl
P = int(input("Population:")) #Population
PPH = int(input("Population per household:"))  #PeoplePerHousehold
PR = float(input("Poverty rate:")) #PovertyRate
Dist = int(input("Distance from the nearest bigger community:")) #DistanceFromAnotherCommunity(hours)


LI = int(round(P/PPH)*PR) #Low Income Household
HI = round(P/PPH) - LI #High Income Household
if (Alt < 2000): #Lowlands households
    H1 = User("low income", LI) 
    User_list.append(H1)
    H2 = User("high income", HI)
    User_list.append(H2)
else: #highlands housegolds
    H3 = User("low income", LI)
    User_list.append(H3)
    H4 = User("high income", HI)
    User_list.append(H4)

    #Health facilities

if (P < 500):
    if (Dist < 2):
        pass
    else:
        HP = User("Health post", 1)
        User_list.append(HP)
    
elif (500 < P <1000):
    HP = User("Health post", 1)
    User_list.append(HP)
else:
    HC = User("Health center", 1)
    User_list.append(HC)

    #Schools

if (P < 100):
    if (Dist < 1):
       pass
    else:
        S1 = User("School type 1", 1)
        User_list.append(S1)
elif (100 < P < 500):
    S2 = User("School type 2", 1)
    User_list.append(S2)
else:
    S3 = User("School type 3", 1)
    User_list.append(S3)

    #Public lighting

PL = round(P/30)
Public_lighting = User("Public lighting ", PL)
User_list.append(Public_lighting)

#Potable water system

if (P<200):
    pass
else: 
    PW = User("Potable water system", 1)
    User_list.append(PW)

#IGAs
 
#Commerce (Grocery Stores, Restaurants, Entertainmet bussiness, Workshops)

if (Alt > 2000)  :
    R1 = round(P/75)
    R = User("Restaurant 1", R1)
    User_list.append(R)
    GS1 = round(P/65)
    GS = User("Grocery Store 1", GS1)
    User_list.append(GS)
    EB1 = round(P/250)
    EB = User("Entertainment bussiness", EB1)
    User_list.append(EB)
    WS1 = round(P/85)
    WS = User("Workshop 1", WS1)
    User_list.append(WS)
else:
    R2 = round(P/70)
    R = User("Restaurant 2", R2)
    User_list.append(R)
    GS2 = round(P/350)
    GS = User("Grocery Store 2", GS2)
    User_list.append(GS)
    EB2 = round(P/150)
    EB = User("Entertainment bussiness 2", EB2)
    User_list.append(EB)
    WS2 = round(P/80)
    WS = User("Workshop 2", WS2)
    User_list.append(WS)

#Agriculture 

if (Alt > 3000): #Highlands
    Agroproductive_units_1 = round(P/85)
    APU1 = User("Agroproductive Unit 1", Agroproductive_units_1)
    User_list.append(APU1)
elif (Alt > 2000): #Valleys
    Agroproductive_units_2 = round(P/65)
    APU2 = User("Agroproductive Unit 2", Agroproductive_units_2)
    User_list.append(APU2)
else: #Lowlands (Chaco, Tropical lowlands, Amazonia)
    Agroproductive_units_3 = round(P/50)
    APU3 = User("Agroproductive Unit 3", Agroproductive_units_3)
    User_list.append(APU3)

#Defining appliances    
#Residential sector

if (Alt < 2000): #Lowlands households   

    #low income
    H1_indoor_bulb = H1.Appliance(H1,3,7,2,120,0.2,10)
    H1_indoor_bulb.windows([1082,1440],[0,30],0.35)

    H1_outdoor_bulb = H1.Appliance(H1,1,13,2,600,0.2,10)
    H1_outdoor_bulb.windows([0,330],[1082,1440],0.35)

    H1_TV = H1.Appliance(H1,1,60,3,90,0.1,5)
    H1_TV.windows([750,840],[1082,1440],0.35,[0,30])

    H1_Antenna = H1.Appliance(H1,1,8,3,90,0.1,5)
    H1_Antenna.windows([750,840],[1082,1440],0.35,[0,30])

    H1_Phone_charger = H1.Appliance(H1,2,2,1,300,0.2,5)
    H1_Phone_charger.windows([1080,1440],[0,0],0.35)

    #High income

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

    H2_Freezer = H2.Appliance(H2,1,200,1,1440,0,30, 'yes',2)
    H2_Freezer.windows([0,1440],[0,0])
    H2_Freezer.specific_cycle_1(5,15,200,15)
    H2_Freezer.specific_cycle_2(200,10,5,20)
    H2_Freezer.cycle_behaviour([480,1200],[0,0],[0,479],[1201,1440])

    H2_Mixer = H2.Appliance(H2,1,50,3,30,0.1,1, occasional_use = 0.33)
    H2_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

    H2_Fan = H2.Appliance(H2,1,171,1,220,0.27,60)
    H2_Fan.windows([720,1080],[0,0])

    H2_Laptop = H2.Appliance(H2,1,70,1,90,0.3,30)
    H2_Laptop.windows([960,1200],[0,0])

else:  #highlands households

    #low income
    H3_indoor_bulb = H3.Appliance(H3,3,7,2,287,0.4,124)
    H3_indoor_bulb.windows([1153,1440],[0,300],0.5)

    H3_outdoor_bulb = H3.Appliance(H3,1,13,1,243,0.3,71)
    H3_outdoor_bulb.windows([1197,1440],[0,0])

    H3_Radio = H3.Appliance(H3,1,7,2,160,0.3,49)
    H3_Radio.windows([480,840],[841,1200],0.5)

    H3_TV = H3.Appliance(H3,1,100,3,250,0.3,74)
    H3_TV.windows([1170,1420],[551,1169],0.3,[300,550])

    H3_Phone_charger = H3.Appliance(H3,2,5,3,200,0.4,82)
    H3_Phone_charger.windows([1020,1440],[0,420],0.3,[720,1019])

    H3_Freezer = H3.Appliance(H3,2,200,1,1440,0,30,'yes',3)
    H3_Freezer.windows([0,1440],[0,0])
    H3_Freezer.specific_cycle_1(200,20,5,10)
    H3_Freezer.specific_cycle_2(200,15,5,15)
    H3_Freezer.specific_cycle_3(200,10,5,20)
    H3_Freezer.cycle_behaviour([0,0],[0,0],[480,1200],[0,0],[0,299],[1201,1440])

    H3_Iron = H3.Appliance(H3,1,1000,2,22.5,0.5,10,occasional_use =0.03)
    H3_Iron.windows([420,480],[720,780],0.5)

    H3_Water_pump = H3.Appliance(H3,1,250,2,37.5,0.47,17.5)
    H3_Water_pump.windows([420,450],[960,1020],0.5)

    #High income
    
    H4_indoor_bulb = H4.Appliance(H4,4,7,2,287,0.4,124)
    H4_indoor_bulb.windows([1153,1440],[0,300],0.5)

    H4_outdoor_bulb = H4.Appliance(H4,2,13,1,243,0.3,71)
    H4_outdoor_bulb.windows([1197,1440],[0,0])

    H4_Radio = H4.Appliance(H4,1,7,2,160,0.3,49)
    H4_Radio.windows([480,840],[841,1200],0.5)

    H4_TV = H4.Appliance(H4,1,100,3,250,0.3,74)
    H4_TV.windows([1170,1420],[551,1169],0.3,[300,550])

    H4_Phone_charger = H4.Appliance(H4,4,5,3,200,0.4,82)
    H4_Phone_charger.windows([1020,1440],[0,420],0.3,[720,1019])

    H4_Freezer = H4.Appliance(H4,2,200,1,1440,0,30,'yes',3)
    H4_Freezer.windows([0,1440],[0,0])
    H4_Freezer.specific_cycle_1(200,20,5,10)
    H4_Freezer.specific_cycle_2(200,15,5,15)
    H4_Freezer.specific_cycle_3(200,10,5,20)
    H4_Freezer.cycle_behaviour([0,0],[0,0],[480,1200],[0,0],[0,299],[1201,1440])

    H4_Blender = H4.Appliance(H4,1,350,2,20,0.375,7.5)
    H4_Blender.windows([900,1020],[420,600],0.5)

    H4_Iron = H4.Appliance(H4,1,1000,2,22.5,0.5,10,occasional_use =0.03)
    H4_Iron.windows([420,480],[720,780],0.5)

    H4_Water_pump = H4.Appliance(H4,1,250,2,37.5,0.47,17.5)
    H4_Water_pump.windows([420,450],[960,1020],0.5)

#Health facilities

if (P < 500):
    if (Dist > 2):
        HP_indoor_bulb = HP.Appliance(HP,12,7,2,690,0.2,10)
        HP_indoor_bulb.windows([480,720],[870,1440],0.35)

        HP_outdoor_bulb = HP.Appliance(HP,1,13,2,690,0.2,10)
        HP_outdoor_bulb.windows([0,342],[1037,1440],0.35)

        HP_Phone_charger = HP.Appliance(HP,8,2,2,300,0.2,5)
        HP_Phone_charger.windows([480,720],[900,1440],0.35)

        HP_TV = HP.Appliance(HP,1,150,2,360,0.1,60)
        HP_TV.windows([480,720],[780,1020],0.2)

        HP_radio = HP.Appliance(HP,1,40,2,360,0.3,60)
        HP_radio.windows([480,720],[780,1020],0.2)

        HP_PC = HP.Appliance(HP,1,200,2,300,0.1,10)
        HP_PC.windows([480,720],[1050,1440],0.35)

        HP_printer = HP.Appliance(HP,1,100,1,60,0.3,10)
        HP_printer.windows([540,1020],[0,0])

        HP_fan = HP.Appliance(HP,2,60,1,240,0.2,60)
        HP_fan.windows([660,960],[0,0])

        HP_sterilizer_stove = HP.Appliance(HP,1,600,2,120,0.3,30)
        HP_sterilizer_stove.windows([540,600],[900,960],)

        HP_needle_destroyer = HP.Appliance(HP,1,70,1,60,0.2,10)
        HP_needle_destroyer.windows([540,600],[0,0])

        HP_water_pump = HP.Appliance(HP,1,400,1,30,0.2,10)
        HP_water_pump.windows([480,510],[0,0])

        HP_Fridge = HP.Appliance(HP,1,150,1,1440,0,30, 'yes',3)
        HP_Fridge.windows([0,1440],[0,0])
        HP_Fridge.specific_cycle_1(150,20,5,10)
        HP_Fridge.specific_cycle_2(150,15,5,15)
        HP_Fridge.specific_cycle_3(150,10,5,20)
        HP_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

        HP_Fridge2 = HP.Appliance(HP,1,150,1,1440,0,30, 'yes',3)
        HP_Fridge2.windows([0,1440],[0,0])
        HP_Fridge2.specific_cycle_1(150,20,5,10)
        HP_Fridge2.specific_cycle_2(150,15,5,15)
        HP_Fridge2.specific_cycle_3(150,10,5,20)
        HP_Fridge2.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,299],[1201,1440])

        HP_Fridge3 = HP.Appliance(HP,1,150,1,1440,0.1,30, 'yes',3)
        HP_Fridge3.windows([0,1440],[0,0])
        HP_Fridge3.specific_cycle_1(150,20,5,10)
        HP_Fridge3.specific_cycle_2(150,15,5,15)
        HP_Fridge3.specific_cycle_3(150,10,5,20)
        HP_Fridge3.cycle_behaviour([580,1200],[0,0],[420,479],[0,0],[0,419],[1201,1440])
    else:
        pass
        
elif (500 < P <1000):
    HP_indoor_bulb = HP.Appliance(HP,12,7,2,690,0.2,10)
    HP_indoor_bulb.windows([480,720],[870,1440],0.35)

    HP_outdoor_bulb = HP.Appliance(HP,1,13,2,690,0.2,10)
    HP_outdoor_bulb.windows([0,342],[1037,1440],0.35)

    HP_Phone_charger = HP.Appliance(HP,8,2,2,300,0.2,5)
    HP_Phone_charger.windows([480,720],[900,1440],0.35)

    HP_TV = HP.Appliance(HP,1,150,2,360,0.1,60)
    HP_TV.windows([480,720],[780,1020],0.2)

    HP_radio = HP.Appliance(HP,1,40,2,360,0.3,60)
    HP_radio.windows([480,720],[780,1020],0.2)

    HP_PC = HP.Appliance(HP,1,200,2,300,0.1,10)
    HP_PC.windows([480,720],[1050,1440],0.35)

    HP_printer = HP.Appliance(HP,1,100,1,60,0.3,10)
    HP_printer.windows([540,1020])

    HP_fan = HP.Appliance(HP,2,60,1,240,0.2,60)
    HP_fan.windows([660,960])

    HP_sterilizer_stove = HP.Appliance(HP,1,600,2,120,0.3,30)
    HP_sterilizer_stove.windows([540,600],[900,960],0.3)

    HP_needle_destroyer = HP.Appliance(HP,1,70,1,60,0.2,10)
    HP_needle_destroyer.windows([540,600])

    HP_water_pump = HP.Appliance(HP,1,400,1,30,0.2,10)
    HP_water_pump.windows([480,510])

    HP_Fridge = HP.Appliance(HP,1,150,1,1440,0,30, 'yes',3)
    HP_Fridge.windows([0,1440],[0,0])
    HP_Fridge.specific_cycle_1(150,20,5,10)
    HP_Fridge.specific_cycle_2(150,15,5,15)
    HP_Fridge.specific_cycle_3(150,10,5,20)
    HP_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

    HP_Fridge2 = HP.Appliance(HP,1,150,1,1440,0,30, 'yes',3)
    HP_Fridge2.windows([0,1440],[0,0])
    HP_Fridge2.specific_cycle_1(150,20,5,10)
    HP_Fridge2.specific_cycle_2(150,15,5,15)
    HP_Fridge2.specific_cycle_3(150,10,5,20)
    HP_Fridge2.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,299],[1201,1440])

    HP_Fridge3 = HP.Appliance(HP,1,150,1,1440,0.1,30, 'yes',3)
    HP_Fridge3.windows([0,1440],[0,0])
    HP_Fridge3.specific_cycle_1(150,20,5,10)
    HP_Fridge3.specific_cycle_2(150,15,5,15)
    HP_Fridge3.specific_cycle_3(150,10,5,20)
    HP_Fridge3.cycle_behaviour([580,1200],[0,0],[420,479],[0,0],[0,419],[1201,1440])
else:
    HC_indoor_bulb = HC.Appliance(HC,20,7,2,690,0.2,10)
    HC_indoor_bulb.windows([480,720],[870,1440],0.35)

    HC_outdoor_bulb = HC.Appliance(HC,5,13,2,690,0.2,10)
    HC_outdoor_bulb.windows([0,342],[1037,1440],0.35)

    HC_Phone_charger = HC.Appliance(HC,5,2,2,300,0.2,5)
    HC_Phone_charger.windows([480,720],[900,1440],0.35)

    HC_TV = HC.Appliance(HC,2,150,2,360,0.1,60)
    HC_TV.windows([480,720],[780,1020],0.2)

    HC_radio = HC.Appliance(HC,5,40,2,360,0.3,60)
    HC_radio.windows([480,720],[780,1020],0.2)

    HC_PC = HC.Appliance(HC,2,200,2,300,0.1,10)
    HC_PC.windows([480,720],[1050,1440],0.35)

    HC_printer = HC.Appliance(HC,2,100,1,60,0.3,10)
    HC_printer.windows([540,1020],[0,0])

    HC_fan = HC.Appliance(HC,2,60,1,240,0.2,60)
    HC_fan.windows([660,960],[0,0])

    HC_sterilizer_stove = HC.Appliance(HC,3,600,2,120,0.3,30)
    HC_sterilizer_stove.windows([540,600],[900,960],0.35)

    HC_needle_destroyer = HC.Appliance(HC,1,70,1,60,0.2,10)
    HC_needle_destroyer.windows([540,600],[0,0],0.35)

    HC_water_pump = HC.Appliance(HC,1,400,1,30,0.2,10)
    HC_water_pump.windows([480,510],[0,0])

    HC_Fridge = HC.Appliance(HC,1,150,1,1440,0,30, 'yes',3)
    HC_Fridge.windows([0,1440],[0,0])
    HC_Fridge.specific_cycle_1(150,20,5,10)
    HC_Fridge.specific_cycle_2(150,15,5,15)
    HC_Fridge.specific_cycle_3(150,10,5,20)
    HC_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

    HC_Fridge2 = HC.Appliance(HC,1,150,1,1440,0,30, 'yes',3)
    HC_Fridge2.windows([0,1440],[0,0])
    HC_Fridge2.specific_cycle_1(150,20,5,10)
    HC_Fridge2.specific_cycle_2(150,15,5,15)
    HC_Fridge2.specific_cycle_3(150,10,5,20)
    HC_Fridge2.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,299],[1201,1440])

    HC_Fridge3 = HC.Appliance(HC,1,150,1,1440,0.1,30, 'yes',3)
    HC_Fridge3.windows([0,1440],[0,0])
    HC_Fridge3.specific_cycle_1(150,20,5,10)
    HC_Fridge3.specific_cycle_2(150,15,5,15)
    HC_Fridge3.specific_cycle_3(150,10,5,20)
    HC_Fridge3.cycle_behaviour([580,1200],[0,0],[420,479],[0,0],[0,419],[1201,1440])

    HC_Fridge4 = HC.Appliance(HC,1,150,1,1440,0.1,30, 'yes',3)
    HC_Fridge4.windows([0,1440],[0,0])
    HC_Fridge4.specific_cycle_1(150,20,5,10)
    HC_Fridge4.specific_cycle_2(150,15,5,15)
    HC_Fridge4.specific_cycle_3(150,10,5,20)
    HC_Fridge4.cycle_behaviour([580,1200],[0,0],[420,479],[0,0],[0,419],[1201,1440])

    HC_microscope = HC.Appliance(HC,2,3,2,120,0.2,10)
    HC_microscope.windows([480,720],[840,960],0.35)

    HC_shower = HC.Appliance(HC,3,3000,2,120,0.1,15)
    HC_shower.windows([360,720],[780,1400],0.35)

    HC_heater = HC.Appliance(HC,2,1500,2,180,0.25,60)
    HC_heater.windows([369,720],[1080,1260],0.35)

    HC_dental_compresor = HC.Appliance(HC,2,500,2,60,0.15,10)
    HC_dental_compresor.windows([480,720],[840,1260],0.2)

    HC_centrifuge = HC.Appliance(HC,2,100,1,60,0.15,10)
    HC_centrifuge.windows([480,720],[0,0],0.35)

    HC_serological_rotator = HC.Appliance(HC,2,10,1,60,0.25,15)
    HC_serological_rotator.windows([480,720],[0,0],0.35)
    
    
#Schools
if (P < 100):
    if (Dist < 1):
        pass
    else:
        S1_indoor_bulb = S1.Appliance(S1,6,7,2,120,0.25,30)
        S1_indoor_bulb.windows([480,780],[840,1140],0.2)

        S1_outdoor_bulb = S1.Appliance(S1,1,13,1,60,0.2,10)
        S1_outdoor_bulb.windows([1007,1080],[0,0],0.35)

        S1_TV = S1.Appliance(S1,1,60,2,120,0.1,5, occasional_use = 0.5)
        S1_TV.windows([480,780],[840,1140],0.2)

        S1_radio = S1.Appliance(S1,3,4,2,120,0.1,5, occasional_use = 0.5)
        S1_radio.windows([480,780],[840,1140],0.2)

        S1_DVD = S1.Appliance(S1,1,8,2,120,0.1,5, occasional_use = 0.5)
        S1_DVD.windows([480,780],[840,1140],0.2)
        
elif (100 < P < 500):
    S2_indoor_bulb = S2.Appliance(S2,12,7,2,120,0.25,30)
    S2_indoor_bulb.windows([480,780],[840,1140],0.2)

    S2_outdoor_bulb = S2.Appliance(S2,1,13,1,60,0.2,10)
    S2_outdoor_bulb.windows([1007,1080],[0,0],0.35)

    S2_TV = S2.Appliance(S2,1,60,2,120,0.1,5, occasional_use = 0.5)
    S2_TV.windows([480,780],[840,1140],0.2)

    S2_radio = S2.Appliance(S2,3,4,2,120,0.1,5, occasional_use = 0.5)
    S2_radio.windows([480,780],[840,1140],0.2)

    S2_DVD = S2.Appliance(S2,2,8,2,120,0.1,5, occasional_use = 0.5)
    S2_DVD.windows([480,780],[840,1140],0.2)

    S2_Freezer = S2.Appliance(S2,1,200,1,1440,0,30, 'yes',3)
    S2_Freezer.windows([0,1440])
    S2_Freezer.specific_cycle_1(200,20,5,10)
    S2_Freezer.specific_cycle_2(200,15,5,15)
    S2_Freezer.specific_cycle_3(200,10,5,20)
    S2_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

    S2_PC = S2.Appliance(S2,1,50,2,210,0.1,10)
    S2_PC.windows([480,780],[840,1140],0.35)
    
    S2_Phone_charger = S2.Appliance(S2,1,2,2,180,0.2,5)
    S2_Phone_charger.windows([480,780],[840,1140],0.35)
else:
    S3_indoor_bulb = S3.Appliance(S3,27,7,1,60,0.2,10)
    S3_indoor_bulb.windows([480,780],[0,0])

    S3_outdoor_bulb = S3.Appliance(S3,7,13,1,60,0.2,10)
    S3_outdoor_bulb.windows([480,780],[0,0])

    S3_TV = S3.Appliance(S3,5,60,2,120,0.1,5, occasional_use = 0.5)
    S3_TV.windows([480,780],[0,0],0.35)
    
    S3_radio = S3.Appliance(S3,24,4,2,120,0.1,5, occasional_use = 0.5)
    S3_radio.windows([480,780],[0,0],0.35)

    S3_DVD = S3.Appliance(S3,2,8,2,120,0.1,5, occasional_use = 0.5)
    S3_DVD.windows([480,780],[0,0],0.35)

    S3_Freezer = S3.Appliance(S3,1,200,1,1440,0,30, 'yes',3)
    S3_Freezer.windows([0,1440])
    S3_Freezer.specific_cycle_1(200,20,5,10)
    S3_Freezer.specific_cycle_2(200,15,5,15)
    S3_Freezer.specific_cycle_3(200,10,5,20)
    S3_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

    S3_PC = S3.Appliance(S3,25,50,2,210,0.1,10)
    S3_PC.windows([480,780],[0,0])

    S3_Phone_charger = S3.Appliance(S3,5,2,2,180,0.2,5)
    S3_Phone_charger.windows([480,780],[0,0])

    S3_Printer = S3.Appliance(S3,1,20,1,30,0.1,5)
    S3_Printer.windows([480,780],[0,0])

    S3_Stereo = S3.Appliance(S3,1,150,1,90,0.1,5, occasional_use = 0.33)
    S3_Stereo.windows([480,780],[0,0],0.35)

    S3_data = S3.Appliance(S3,1,420,1,60,0.1,5, occasional_use = 0.5)
    S3_data.windows([480,780],[0,0],0.35)
 

#Public lighting

    Public_lighting_lamp_post = Public_lighting.Appliance(Public_lighting,12,40,2,310,0,300, 'yes', flat = 'yes')
    Public_lighting_lamp_post.windows([0,362],[1082,1440],0.1)
    
#Commerce (Grocery Stores, Restaurants, Entertainmet bussiness, Workshops)  

#Restaurant  
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

#Grocery store
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

#Entertainment bussiness
    EB_Stereo = EB.Appliance(EB,1,150,2,90,0.1,5, occasional_use = 0.33)
    EB_Stereo.windows([480,780],[0,0],0.35)
    
    EB_TV = EB.Appliance(EB,1,60,2,120,0.1,5, occasional_use = 0.5)
    EB_TV.windows([480,780],[840,1140],0.2)
        
    EB_PC = EB.Appliance(EB,1,50,2,210,0.1,10)
    EB_PC.windows([480,780],[840,1140],0.35)
#Workshop
    
    WS_indoor_bulb = WS.Appliance(WS,2,7,2,120,0.2,10)
    WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

    WS_welding_machine = WS.Appliance(WS,1,5500,1,60,0.5,30,occasional_use = 0.3)
    WS_welding_machine.windows([0,1440],[0,0],0.35)

    WS_grinding_machine = WS.Appliance(WS,1,750,1,480,0.125,60)
    WS_grinding_machine.windows([0,1440],[0,0],0.35)

    WS_Radio = WS.Appliance(WS,1,36,2,60,0.1,5)
    WS_Radio.windows([390,450],[1140,1260],0.35)

#Agriculture    

if (Alt > 3000): #Highlands
    APU1_WP = APU1.Appliance(APU1,1,1700,3,60,0.2,10,occasional_use = 0.33)
    APU1_WP.windows([420,720],[840,1020],[721,839],0.35)

    APU1_GM = APU1.Appliance(APU1,1,11700,1,180,0.2,30,occasional_use = 0.33)
    APU1_GM.windows([420,1080],[0,0],0.35)

    APU1_GD = APU1.Appliance(APU1,1,9360,1,180,0.2,30,occasional_use = 0.33)
    APU1_GD.windows([420,1080],[0,0],0.35)

    APU1_SM = APU1.Appliance(APU1,1,350,1,60,0.2,1)
    APU1_SM.windows([390,450],[0,0],0.35)
    
elif (Alt > 2000): #Valleys
    APU2_WP = APU2.Appliance(APU2,1,1700,2,60,0.2,10,occasional_use = 0.33)
    APU2_WP.windows([420,720],[840,1020],0.35)

    APU2_GM = APU2.Appliance(APU2,1,11700,1,180,0.2,30,occasional_use = 0.33)
    APU2_GM.windows([420,1080],[0,0],0.35)

    APU2_GD = APU2.Appliance(APU2,1,9360,1,180,0.2,30)
    APU2_GD.windows([420,1080],[0,0],0.35)

    APU2_VW = APU2.Appliance(APU2,1,1170,1,480,0.2,15,occasional_use = 0.33)
    APU2_VW.windows([420,1140],[0,0],0.35)

    APU2_SM = APU2.Appliance(APU2,1,350,1,60,0.2,1)
    APU2_SM.windows([390,450],[0,0],0.35)

    APU2_refrigerator = APU2.Appliance(APU2,2,7,2,120,0.2,10)
    APU2_refrigerator.windows([1107,1440],[0,30],0.35)

    APU2_CT = APU2.Appliance(APU2,1,2890,1,300,0.2,15,occasional_use = 0.33)
    APU2_CT.windows([420,1080],[0,0])
    
else: #Lowlands (Chaco, Tropical lowlands, Amazonia)
    APU3_WP = APU3.Appliance(APU3,1,1700,3,60,0.2,10,occasional_use = 0.33)
    APU3_WP.windows([420,720],[840,1020],0.35)

    APU3_GD = APU3.Appliance(APU3,1,9360,1,180,0.2,30)
    APU3_GD.windows([420,1080],[0,0],0.35)

    APU3_VW = APU3.Appliance(APU3,1,1170,1,480,0.2,15,occasional_use = 0.33)
    APU3_VW.windows([420,1140],[0,0],0.35)

    APU3_refrigerator = APU3.Appliance(APU3,2,7,2,120,0.2,10)
    APU3_refrigerator.windows([1107,1440],[0,30],0.35)

    APU3_BT = APU3.Appliance(APU3,1,370,2,900,0.2,180)
    APU3_BT.windows([360,930],[1080,1440],0.35)
 