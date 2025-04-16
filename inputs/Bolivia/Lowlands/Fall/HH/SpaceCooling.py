from core import User
User_list = []


SC = User("Space Cooling", 1)
User_list.append(SC)


SC_Fan = SC.Appliance(1,30,2,400,0.27,30)
SC_Fan.windows([600,1200],[0,0],0.35)


# SC_Air_Conditioner = SC.Appliance(1,900,2,300,0.2,15)
# SC_Air_Conditioner.windows([600,1200],[0,0],0.35)
