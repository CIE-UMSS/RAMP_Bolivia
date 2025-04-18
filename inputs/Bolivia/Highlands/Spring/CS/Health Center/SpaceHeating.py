from core import User
User_list = []


SH = User("Space heating", 1)
User_list.append(SH)

SH_heater = SH.Appliance(SH,2,1500,2,160,0.25,60, occasional_use=0.33)
SH_heater.windows([369,720],[1080,1260],0.35)

