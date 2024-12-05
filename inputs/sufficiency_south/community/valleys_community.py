#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:46:27 2024

@author: claudia
"""

import pandas as pd

from ramp.core.core import User

User_list = []

H = User("households",200)
User_list.append(H)

HC = User("Health post", 1)
User_list.append(HC)

SC = User("School type C", 1)
User_list.append(SC)

MILK = User("Milk production", 1)			
User_list.append(MILK)

WS = User("Workshop", 2)
User_list.append(WS)

R = User("Restaurant", 5)
User_list.append(R)

GS = User("Grocery Store ", 5)
User_list.append(GS)

EB = User("Entertainment Business", 2)
User_list.append(EB)

#H_shower_P = pd.read_csv('shower_P_LL.csv')

#Households
#Illumination
H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
H_indoor_bulb.windows([300,480],[960,1440],0.35)
         
H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

#Thermal comfort
#Not used in this part of the country

#Cold storage
H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour(
    [330, 1139], [0, 0], [0, 329], [1140, 1440])

#Hygiene
#water heating
#Use of gas for water heating

#ICT

H_TV = H.Appliance(1,30,2,120,0.1,5) 
H_TV.windows([1080,1440],[0,60],0.35)

H_Radio = H.Appliance(1,36,2,120,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
H_Phone_charger.windows([1020,1440],[0,300],0.35)

H_Laptop = H.Appliance(1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)


#SCHOOL

SC_indoor_bulb = SC.Appliance(27,7,1,300,0.2,10)
SC_indoor_bulb.windows([480,840],[0,0],0.35)

SC_outdoor_bulb = SC.Appliance(7,13,1,60,0.2,10)
SC_outdoor_bulb.windows([480,780],[0,0],0.35)

SC_TV = SC.Appliance(5,30,1,120,0.1,10, occasional_use = 0.5)
SC_TV.windows([480,780],[0,0],0.35)

SC_radio = SC.Appliance(15,4,1,120,0.1,5, occasional_use = 0.5)
SC_radio.windows([480,780],[0,0],0.35)

SC_DVD = SC.Appliance(2,8,1,120,0.1,5, occasional_use = 0.5)
SC_DVD.windows([480,780],[0,0],0.35)

SC_Freezer = SC.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
SC_Freezer.windows([0, 1440], [0, 0])
SC_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
SC_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
SC_Freezer.cycle_behaviour(
    [330, 1139], [0, 0], [0, 329], [1140, 1440]
)

SC_PC = SC.Appliance(25,50,1,210,0.1,10)
SC_PC.windows([480,780],[0,0],0.35)

SC_Phone_charger = SC.Appliance(5,2,1,180,0.2,5)
SC_Phone_charger.windows([480,780],[0,0],0.35)

SC_Printer = SC.Appliance(1,20,1,30,0.1,5)
SC_Printer.windows([480,780],[0,0],0.35)

SC_Stereo = SC.Appliance(1,150,1,90,0.1,5, occasional_use = 0.33)
SC_Stereo.windows([480,780],[0,0],0.35)

SC_data = SC.Appliance(1,420,1,60,0.1,5, occasional_use = 0.33)
SC_data.windows([480,780],[0,0],0.35)

#HOSPITAL

HC_indoor_bulb = HC.Appliance(20,7,2,690,0.2,10)
HC_indoor_bulb.windows([480,720],[870,1440],0.35)

HC_outdoor_bulb = HC.Appliance(5,13,2,690,0.2,10)
HC_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HC_Phone_charger = HC.Appliance(5,2,2,300,0.2,5)
HC_Phone_charger.windows([480,720],[900,1440],0.35)

HC_TV = HC.Appliance(2,150,2,360,0.1,60)
HC_TV.windows([480,720],[780,1020],0.2)

HC_radio = HC.Appliance(5,40,2,360,0.3,60)
HC_radio.windows([480,720],[780,1020],0.35)

HC_PC = HC.Appliance(2,200,2,300,0.1,10)
HC_PC.windows([480,720],[1050,1440],0.35)

HC_printer = HC.Appliance(2,100,1,60,0.3,10)
HC_printer.windows([540,1020],[0,0],0.35)

HC_sterilizer_stove = HC.Appliance(3,600,2,120,0.3,30, occasional_use=0.33)
HC_sterilizer_stove.windows([480,720],[780,1020],0.35)

HC_needle_destroyer = HC.Appliance(1,70,1,60,0.3,10, occasional_use=0.33)
HC_needle_destroyer.windows([480,720],[0,0],0.35)

HC_water_pump = HC.Appliance(1,400,1,45,0.2,10)
HC_water_pump.windows([480,720],[0,0],0.35)

HC_Freezer = HC.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
HC_Freezer.windows([0, 1440], [0, 0])
HC_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
HC_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
HC_Freezer.cycle_behaviour(
    [330, 1139], [0, 0], [0, 329], [1140, 1440])

HC_microscope = HC.Appliance(2,3,2,120,0.2,10, occasional_use=0.33)
HC_microscope.windows([480,720],[840,960],0.35)

HC_shower = HC.Appliance(1,5500,2,15,0.1,3, thermal_P_var = 0.2, occasional_use=0.33)
HC_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

HC_dental_compresor = HC.Appliance(2,500,2,60,0.15,10, occasional_use=0.33)
HC_dental_compresor.windows([480,720],[840,1260],0.35)

HC_centrifuge = HC.Appliance(2,100,1,60,0.15,10, occasional_use=0.33)
HC_centrifuge.windows([480,720],[0,0],0.35)

HC_serological_rotator = HC.Appliance(2,10,1,60,0.25,15, occasional_use=0.33)
HC_serological_rotator.windows([480,720],[0,0],0.35)


#IGA
#Appliances

		
                					
MILK_indoor_bulb = MILK.Appliance(2,7,2,120,0.2,10)
MILK_indoor_bulb.windows([1107,1440],[0,0],0.35)
        
MILK_outdoor_bulb = MILK.Appliance(1,13,2,600,0.2,10)                    
MILK_outdoor_bulb.windows([0,330],[1107,1440],0.35)     
    
MILK_cooler_tank = MILK.Appliance(1,4000,2,480,0,240)                    
MILK_cooler_tank.windows([360,600],[1080,1320],0.2)   	

MILK_milking_machine = MILK.Appliance(1,800,2,120,0.3,60, wd_we_type=0)
MILK_milking_machine.windows([300,480],[960,1080],0.3)			


#Workshop

WS_indoor_bulb = WS.Appliance(2,7,2,120,0.2,10, wd_we_type=0)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(1,5500,1,60,0.5,30, wd_we_type=0)
WS_welding_machine.windows([0,1440],[0,0],0.35)

WS_grinding_machine = WS.Appliance(1,750,1,480,0.2,60, wd_we_type=0)
WS_grinding_machine.windows([0,1440],[0,0],0.35)

WS_Radio = WS.Appliance(1,36,2,60,0.1,5, wd_we_type=0)
WS_Radio.windows([390,450],[1140,1260],0.35)

#Restaurant

R_indoor_bulb = R.Appliance(2,7,2,120,0.2,10)
R_indoor_bulb.windows([1107,1440],[0,30],0.35)

R_Blender = R.Appliance(1,350,2,20,0.375,5)
R_Blender.windows([420,480],[720,780],0.5)

R_freezer = R.Appliance(1,200,1,1440,0,30,'yes',2)
R_freezer.windows([0,1440],[0,0])
R_freezer.specific_cycle_1(5,15,200,15)
R_freezer.specific_cycle_2(5,20,200,10)
R_freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

#Grocery Store

GS_indoor_bulb = GS.Appliance(2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_Freezer = GS.Appliance(1,200,1,1440,0,30,'yes',2)
GS_Freezer.windows([0,1440],[0,0])
GS_Freezer.specific_cycle_1(5,15,200,15)
GS_Freezer.specific_cycle_2(5,20,200,10)
GS_Freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

GS_Radio = GS.Appliance(1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)

#entertainment bussiness

EB_indoor_bulb = EB.Appliance(2,7,2,120,0.2,10)
EB_indoor_bulb.windows([1107,1440],[0,30],0.35)

EB_outdoor_bulb = EB.Appliance(1,13,2,600,0.2,10)
EB_outdoor_bulb.windows([0,330],[1107,1440],0.35)

EB_Stereo = EB.Appliance(1,150,2,90,0.1,5, occasional_use = 0.33)
EB_Stereo.windows([480,780],[0,0],0.35)

EB_TV = EB.Appliance(1,60,2,120,0.1,5, occasional_use = 0.33)
EB_TV.windows([480,780],[840,1140],0.2)
    
EB_PC = EB.Appliance(1,50,2,210,0.1,10, occasional_use = 0.33)
EB_PC.windows([480,780],[840,1140],0.35)

EB_Freezer = EB.Appliance(1,200,1,1440,0,30,'yes',2)
EB_Freezer.windows([0,1440],[0,0])
EB_Freezer.specific_cycle_1(5,15,200,15)
EB_Freezer.specific_cycle_2(5,20,200,10)
EB_Freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
        date_start="2022-01-01", date_end="2022-12-31"  
    )
    uc.initialize(peak_enlarge=0.15)

    Profiles_list = uc.generate_daily_load_profiles(flat=False)

    # post-processing
    from ramp.post_process import post_process as pp

    Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
        Profiles_list
    )
    pp.Profile_series_plot(
        Profiles_series
    )  # by default, profiles are plotted as a series
    
    if (
        len(Profiles_list) > 1
    ):  # if more than one daily profile is generated, also cloud plots are shown
        pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
        
    # this would be a new method using work of @mohammadamint
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'valleys_community_final.csv')