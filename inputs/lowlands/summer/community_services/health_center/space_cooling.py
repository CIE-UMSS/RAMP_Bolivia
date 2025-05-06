from ramp.core.core import User
User_list = []


SC = User("Space Cooling", 1)
User_list.append(SC)


SC_Fan = SC.add_appliance(4,30,2,300,0.27,30)
SC_Fan.windows([540,1200],[0,0],0.35)

SC_Air_Conditioner = SC.add_appliance(2,1000,2,120,0.2,15)
SC_Air_Conditioner.windows([720,900],[1020,1260],0.35)