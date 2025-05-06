from ramp.core.core import User
User_list = []


ICT = User("ICT", 1)
User_list.append(ICT)

ICT_Stereo = ICT.add_appliance(1 ,150 ,2 ,90 ,0.1 ,5, occasional_use = 0.33)
ICT_Stereo.windows([480 ,780] ,[0 ,0] ,0.35)

ICT_TV = ICT.add_appliance(1 ,60 ,2 ,120 ,0.1 ,5, occasional_use = 0.33)
ICT_TV.windows([480 ,780] ,[840 ,1140] ,0.2)

ICT_PC = ICT.add_appliance(1 ,50 ,2 ,210 ,0.1 ,10, occasional_use = 0.33)
ICT_PC.windows([480 ,780] ,[840 ,1140] ,0.35)
