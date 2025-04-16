from core import User
User_list = []


SH = User("Space Heating", 1)
User_list.append(SH)


SH_heater = SH.Appliance(1,800,2,240,0.1,10, occasional_use = 0.66)
SH_heater.windows([480,660],[1080,1200],0.35)

