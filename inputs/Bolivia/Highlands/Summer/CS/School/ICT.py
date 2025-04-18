from core import User
User_list = []


ICT = User("ICT", 1)
User_list.append(ICT)


ICT_TV = ICT.Appliance(ICT,5,60,1,120,0.1,5, occasional_use = 0.5)
ICT_TV.windows([480,780],[0,0],0.35)

ICT_radio = ICT.Appliance(ICT,24,4,1,120,0.1,5, occasional_use = 0.5)
ICT_radio.windows([480,780],[0,0],0.35)

ICT_DVD = ICT.Appliance(ICT,2,8,1,120,0.1,5, occasional_use = 0.5)
ICT_DVD.windows([480,780],[0,0],0.35)

ICT_PC = ICT.Appliance(ICT,25,50,1,210,0.1,10)
ICT_PC.windows([480,780],[0,0],0.35)

ICT_Phone_charger = ICT.Appliance(ICT,5,2,1,180,0.2,5)
ICT_Phone_charger.windows([480,780],[0,0],0.35)

ICT_Printer = ICT.Appliance(ICT,1,20,1,30,0.1,5)
ICT_Printer.windows([480,780],[0,0],0.35)

ICT_Stereo = ICT.Appliance(ICT,1,150,1,90,0.1,5, occasional_use = 0.33)
ICT_Stereo.windows([480,780],[0,0],0.35)

ICT_data = ICT.Appliance(ICT,1,420,1,60,0.1,5, occasional_use = 0.33)
ICT_data.windows([480,780],[0,0],0.35)