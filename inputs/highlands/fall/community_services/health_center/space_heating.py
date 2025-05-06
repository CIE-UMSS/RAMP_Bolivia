from ramp.core.core import User
User_list = []


SH = User("Space Heating", 1)
User_list.append(SH)


SH_heater = SH.add_appliance(2,800,1,120,0.1,10, occasional_use = 0.3)
SH_heater.windows([480,780],[0,0],0.35)