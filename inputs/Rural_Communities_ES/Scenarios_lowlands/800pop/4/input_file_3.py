# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:28:30 2022

@author: pietr
"""
'''
Paper: Energy sufficiency, lowlands.
User: Low Income Household
'''

from core import User, np
User_list = []

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

#Defining users

HP = User("Health post", 1)
User_list.append(HP)

#Appliances

HP_indoor_bulb = HP.Appliance(HP,12,7,2,630,0.1,10)
HP_indoor_bulb.windows([480,870],[870,1440],0.35)

HP_outdoor_bulb = HP.Appliance(HP,1,13,2,690,0.2,10)
HP_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HP_Phone_charger = HP.Appliance(HP,5,2,2,300,0.2,5)
HP_Phone_charger.windows([480,720],[900,1440],0.35)

HP_TV = HP.Appliance(HP,1,150,2,360,0.1,60)
HP_TV.windows([480,720],[780,1020],0.2)

### la radio da problemi --> safe configuration thus changed the original one

HP_radio = HP.Appliance(HP,1,40,2,300,0.2,60)
HP_radio.windows([480,720],[780,1020],0.35)

###

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

#Definig users

CO = User("Coliseum", 1)
User_list.append(CO)

#Appliances

CO_lights = CO.Appliance(CO, 10,150,2,310,0.1,300, 'yes', flat = 'yes')
CO_lights.windows([0,336],[1110,1440],0.2)

#Definig users

CH = User("Church", 1)
User_list.append(CH)

#Church

CH_indoor_bulb = CH.Appliance(CH,10,26,1,210,0.2,60,'yes', flat = 'yes')
CH_indoor_bulb.windows([1200,1440],[0,0],0.1)

CH_outdoor_bulb = CH.Appliance(CH,7,26,1,240,0.2,60, 'yes', flat = 'yes')
CH_outdoor_bulb.windows([1200,1440],[0,0],0.1)

CH_speaker = CH.Appliance(CH,1,100,1,120,0.2,60, occasional_use=0.5)
CH_speaker.windows([1020,1260],[0,0],0.1)
