from ramp.core.core import User
User_list = []


IL = User("Illumination", 1)
User_list.append(IL)


IL_indoor_bulb = IL.add_appliance(20,7,2,690,0.2,10)
IL_indoor_bulb.windows([0,720],[870,1440],0.35)

IL_outdoor_bulb = IL.add_appliance(5,13,2,240,0.2,10)
IL_outdoor_bulb.windows([0,342],[1037,1440],0.35)