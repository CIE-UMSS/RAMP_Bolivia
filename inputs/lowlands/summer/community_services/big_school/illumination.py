from ramp.core.core import User

User_list = []

IL = User("Illumination", 1)
User_list.append(IL)


IL_indoor_bulb = IL.add_appliance(27,7,1,300,0.2,10)
IL_indoor_bulb.windows([480,840],[0,0],0.35)

IL_outdoor_bulb = IL.add_appliance(7,13,1,60,0.2,10)
IL_outdoor_bulb.windows([480,780],[0,0],0.35)

