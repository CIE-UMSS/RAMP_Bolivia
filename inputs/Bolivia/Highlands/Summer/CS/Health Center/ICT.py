from core import User
User_list = []


ICT = User("ICT", 1)
User_list.append(ICT)


ICT_Phone_charger = ICT.Appliance(ICT,5,2,2,300,0.2,5)
ICT_Phone_charger.windows([480,720],[900,1440],0.35)

ICT_TV = ICT.Appliance(ICT,2,150,2,360,0.1,60)
ICT_TV.windows([480,720],[780,1020],0.2)

ICT_radio = ICT.Appliance(ICT,5,40,2,360,0.3,60)
ICT_radio.windows([480,720],[780,1020],0.35)

ICT_PC = ICT.Appliance(ICT,2,200,2,300,0.1,10)
ICT_PC.windows([480,720],[1050,1440],0.35)

ICT_printer = ICT.Appliance(ICT,2,100,1,60,0.3,10)
ICT_printer.windows([540,1020],[0,0],0.35)