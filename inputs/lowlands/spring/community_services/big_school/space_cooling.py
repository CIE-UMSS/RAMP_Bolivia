from ramp.core.core import User
User_list = []


SC = User("SpaceCooling", 1)
User_list.append(SC)


SC_fan = SC.add_appliance(15,30,1,240,0.1,5)
SC_fan.windows([540,960],[0,0],0.35)