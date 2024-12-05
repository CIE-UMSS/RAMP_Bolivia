#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 14:50:05 2024

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

CAR = User("Carpentry workshop", 1)			
User_list.append(CAR)

GS = User("Grocery Store ", 5)
User_list.append(GS)

CS = User("Copy Store ", 1)
User_list.append(CS)

#Household

H_indoor_bulb = H.Appliance(4,7,3,360,0.2,10)
H_indoor_bulb.windows([240,360],[1080,1440],0.35,[0,60])
         
H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
H_outdoor_bulb.windows([1080,1380],[0,0],0.35)

#thermal comfort
H_Fan = H.Appliance(5,30,1,500,0.2,30)
H_Fan.windows([500,1080],[0,0],0.35)


#Nutrition

H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])

#Hygiene
#Other sources used for this purpose

#ICT
H_TV = H.Appliance(1,30,2,120,0.1,5)
H_TV.windows([1080,1440],[0,60],0.35)

H_Radio = H.Appliance(1,36,2,120,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(6,5,2,120,0.2,10)
H_Phone_charger.windows([1020,1440],[0,300],0.35)

H_Laptop = H.Appliance(1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)

#School

SC_indoor_bulb = SC.Appliance(27,7,1,300,0.2,10)
SC_indoor_bulb.windows([480,840],[0,0],0.35)

SC_outdoor_bulb = SC.Appliance(7,13,1,60,0.2,10)
SC_outdoor_bulb.windows([480,780],[0,0],0.35)

SC_TV = SC.Appliance(5,30,1,120,0.1,10, occasional_use = 0.5)
SC_TV.windows([480,780],[0,0],0.35)

SC_fan = SC.Appliance(15,30,1,240,0.1,5)
SC_fan.windows([540,960],[0,0],0.35)

SC_radio = SC.Appliance(15,4,1,120,0.1,5, occasional_use = 0.5)
SC_radio.windows([480,780],[0,0],0.35)

SC_DVD = SC.Appliance(2,8,1,120,0.1,5, occasional_use = 0.5)
SC_DVD.windows([480,780],[0,0],0.35)

SC_Freezer = SC.Appliance(1,200,1,1440,0,30, 'yes',3)
SC_Freezer.windows([0,1440])
SC_Freezer.specific_cycle_1(200,20,5,10)
SC_Freezer.specific_cycle_2(200,15,5,15)
SC_Freezer.specific_cycle_3(200,10,5,20)
SC_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

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

#Hospital

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

HC_Fan = HC.Appliance(4,30,2,300,0.27,30)
HC_Fan.windows([540,1200],[0,0],0.35)

HC_Air_Conditioner = HC.Appliance(2,1000,2,120,0.2,15)
HC_Air_Conditioner.windows([720,900],[1020,1260],0.35)

HC_sterilizer_stove = HC.Appliance(3,600,2,120,0.3,30, occasional_use=0.33)
HC_sterilizer_stove.windows([480,720],[780,1020],0.35)

HC_needle_destroyer = HC.Appliance(1,70,1,60,0.3,10, occasional_use=0.33)
HC_needle_destroyer.windows([480,720],[0,0],0.35)

HC_water_pump = HC.Appliance(1,400,1,45,0.2,10)
HC_water_pump.windows([480,720],[0,0],0.35)

HC_Freezer = HC.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
HC_Freezer.windows([0, 1440], [0, 0])
HC_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
HC_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
HC_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
HC_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])

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
#carpentry
CAR_indoor_bulb = CAR.Appliance(4,7,2,120,0.2,10, wd_we_type=0)
CAR_indoor_bulb.windows([1107,1440],[0,0],0.35)
        
CAR_outdoor_bulb = CAR.Appliance(1,13,2,600,0.2,10, wd_we_type=0)                    
CAR_outdoor_bulb.windows([0,330],[1107,1440],0.35)     
    
CAR_planer = CAR.Appliance(2,1500,1,180,0.3,10, wd_we_type=0)                    
CAR_planer.windows([420, 1020],[0,0],0.35)   	

CAR_jigsaw = CAR.Appliance(2,650,1,180,0.3,10, wd_we_type=0)
CAR_jigsaw.windows([420, 1020],[0,0],0.35)			

CAR_cicular_saw = CAR.Appliance(2,1850,1,180,0.3,60, wd_we_type=0)
CAR_cicular_saw.windows([420, 1020],[0,0],0.35)	

CAR_drill = CAR.Appliance(1,450,1,60,0.3,5, wd_we_type=0)
CAR_drill.windows([420, 1020],[0,0],0.35)	

CAR_grinder = CAR.Appliance(1,1500,1,120,0.3,10, wd_we_type=0)
CAR_grinder.windows([420, 1020],[0,0],0.35)	

CAR_rotor = CAR.Appliance(1,1650,2,60,0.3,60, wd_we_type=0)
CAR_rotor.windows([420, 1020],[0,0],0.35)

#Grocery store

GS_indoor_bulb = GS.Appliance(2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_freezer = GS.Appliance(1,200,1,1440,0,30,'yes',3)
GS_freezer.windows([0,1440],[0,0])
GS_freezer.specific_cycle_1(200,20,5,10)
GS_freezer.specific_cycle_2(200,15,5,15)
GS_freezer.specific_cycle_3(200,10,5,20)
GS_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

GS_Radio = GS.Appliance(1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)

#Copy Store

CS_indoor_bulb = GS.Appliance(2,7,2,120,0.2,10, wd_we_type=0)
CS_indoor_bulb.windows([1107,1440],[0,30],0.35)

CS_outdoor_bulb = GS.Appliance(1,13,2,600,0.2,10, wd_we_type=0)
CS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

CS_freezer = GS.Appliance(1,200,1,1440,0,30,'yes',3)
CS_freezer.windows([0,1440],[0,0])
CS_freezer.specific_cycle_1(200,20,5,10)
CS_freezer.specific_cycle_2(200,15,5,15)
CS_freezer.specific_cycle_3(200,10,5,20)
CS_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

CS_Radio = CS.Appliance(1,36,2,60,0.1,5, wd_we_type=0)
CS_Radio.windows([390,450],[1140,1260],0.35)

CS_Laptop = CS.Appliance(1,70,1,180,0.3,30, wd_we_type=0)
CS_Laptop.windows([960,1200],[0,0],0.35)

CS_copy_machine = CS.Appliance(1,1200,1,420,0.3,30, wd_we_type=0)
CS_copy_machine.windows([420,1020],[0,0],0.35)

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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'kenya_community_final.csv')