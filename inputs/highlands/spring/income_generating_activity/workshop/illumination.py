from ramp.core.core import User
User_list = []


IL = User("Illumination", 1)
User_list.append(IL)


IL_indoor_bulb = IL.add_appliance(2,7,2,120,0.2,10, wd_we_type=0)
IL_indoor_bulb.windows([1107,1440],[0,30],0.35)