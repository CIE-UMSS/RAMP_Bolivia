from ramp.core.core import User
User_list = []


WS = User("Water supply", 1)
User_list.append(WS)


WS_water_pump = WS.add_appliance(1,400,1,30,0.2,10)
WS_water_pump.windows([480,720],[0,0],0.35)