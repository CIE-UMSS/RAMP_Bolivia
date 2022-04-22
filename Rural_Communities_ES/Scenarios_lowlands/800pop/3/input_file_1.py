# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:31:02 2022

@author: pietr
"""

'''
Paper: Energy sufficiency, lowlands.
User: Low Income Household
'''
## 53%

from core import User, np
User_list = []

###### RESODENTIAL ######
 
#Defining users LI

H1 = User("low income", 181) 
User_list.append(H1)
    
#Appliances
H1_indoor_bulb = H1.Appliance(H1,3,7,2,120,0.2,10)
H1_indoor_bulb.windows([1082,1440],[0,30],0.35)

H1_outdoor_bulb = H1.Appliance(H1,1,13,2,600,0.2,10)
H1_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H1_TV = H1.Appliance(H1,1,60,2,90,0.1,5)
H1_TV.windows([750,840],[1082,1440],0.35)

H1_Antenna = H1.Appliance(H1,1,8,2,90,0.1,5)
H1_Antenna.windows([750,840],[1082,1440],0.35)

H1_Phone_charger = H1.Appliance(H1,2,2,1,300,0.2,5)
H1_Phone_charger.windows([1080,1440],[0,0],0.35)



#Defining users HI

H2 = User("high income", 78)
User_list.append(H2)

#Appliances
H2_indoor_bulb = H2.Appliance(H2,4,7,2,120,0.2,10)
H2_indoor_bulb.windows([1082,1440],[0,30],0.35)
         
H2_outdoor_bulb = H2.Appliance(H2,2,13,2,600,0.2,10)
H2_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H2_TV = H2.Appliance(H2,1,60,2,90,0.1,5)
H2_TV.windows([750,840],[1082,1440],0.35)

H2_DVD = H2.Appliance(H2,1,8,1,40,0.1,5, occasional_use = 0.3)
H2_DVD.windows([1082,1440],[0,0],0.35)

H2_Antenna = H2.Appliance(H2,1,8,2,80,0.1,5)
H2_Antenna.windows([750,840],[1082,1440],0.35)

H2_Phone_charger = H2.Appliance(H2,4,2,1,300,0.2,5)
H2_Phone_charger.windows([1080,1440],[0,0],0.35)


H2_freezer = H2.Appliance(H2,1,200,1,1440,0,30,'yes',3)
H2_freezer.windows([0,1440],[0,0])
H2_freezer.specific_cycle_1(200,20,5,10)
H2_freezer.specific_cycle_2(200,15,5,15)
H2_freezer.specific_cycle_3(200,10,5,20)
H2_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

H2_Mixer = H2.Appliance(H2,1,50,3,30,0.1,1, occasional_use = 0.33)
H2_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

H2_Fan = H2.Appliance(H2,1,17,1,220,0.27,60)
H2_Fan.windows([720,1080],[0,0])

H2_Laptop = H2.Appliance(H2,1,70,1,90,0.3,30)
H2_Laptop.windows([960,1200],[0,0])

###### COMMUNITY SERVICES ######

#Definig users

Public_lighting = User("Public lighting ", 26)
User_list.append(Public_lighting)

#Appliances

Public_lighting_lamp_post = Public_lighting.Appliance(Public_lighting,1,40,2,310,0,300, 'yes', flat = 'yes')
Public_lighting_lamp_post.windows([0,362],[1082,1440],0.1)


WSS = User("water supply system", 3)
User_list.append(WSS)

#Appliances

WSS_water_pump = WSS.Appliance(WSS,1,1700,2,60,0.2,10,occasional_use = 0.33)
WSS_water_pump.windows([420,720],[840,1020],0.35)

#Definig users

SC = User("School type C", 1)
User_list.append(SC)

#Appliances

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


###### IGA's  AGRICULTURAL ######

#Definig users IRRIGATION WATER


IW = User("Irrigation Water", 14)
User_list.append(IW)

#Appliances

IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)


###### IGA's NON AGRICULTURAL ######

#Definig users GROCERY STORE

GS = User("Grocery Store 1", 9)
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

R = User("Restaurant", 9)
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


