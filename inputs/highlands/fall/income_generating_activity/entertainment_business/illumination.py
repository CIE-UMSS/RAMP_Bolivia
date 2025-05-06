from ramp.core.core import User
User_list = []


IL = User("Illumination", 1)
User_list.append(IL)

IL_indoor_bulb = IL.add_appliance(2 ,7 ,2 ,120 ,0.2 ,10)
IL_indoor_bulb.windows([1107 ,1440] ,[0 ,30] ,0.35)

IL_outdoor_bulb = IL.add_appliance(1 ,13 ,2 ,600 ,0.2 ,10)
IL_outdoor_bulb.windows([0 ,330] ,[1107 ,1440] ,0.35)