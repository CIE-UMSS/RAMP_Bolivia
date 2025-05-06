from ramp.core.core import User
User_list = []


ICT = User("ICT", 1)
User_list.append(ICT)


ICT_TV = ICT.add_appliance(5,30,1,120,0.1,10, occasional_use = 0.5)
ICT_TV.windows([480,780],[0,0],0.35)

ICT_radio = ICT.add_appliance(15,4,1,120,0.1,5, occasional_use = 0.5)
ICT_radio.windows([480,780],[0,0],0.35)

ICT_DVD = ICT.add_appliance(2,8,1,120,0.1,5, occasional_use = 0.5)
ICT_DVD.windows([480,780],[0,0],0.35)

ICT_PC = ICT.add_appliance(25,50,1,210,0.1,10)
ICT_PC.windows([480,780],[0,0],0.35)

ICT_Phone_charger = ICT.add_appliance(5,2,1,180,0.2,5)
ICT_Phone_charger.windows([480,780],[0,0],0.35)

ICT_Printer = ICT.add_appliance(1,20,1,30,0.1,5)
ICT_Printer.windows([480,780],[0,0],0.35)

ICT_Stereo = ICT.add_appliance(1,150,1,90,0.1,5, occasional_use = 0.33)
ICT_Stereo.windows([480,780],[0,0],0.35)

ICT_data = ICT.add_appliance(1,420,1,60,0.1,5, occasional_use = 0.33)
ICT_data.windows([480,780],[0,0],0.35)

