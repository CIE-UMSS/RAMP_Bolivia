from core import User
User_list = []


SC = User("Space Cooling", 1)
User_list.append(SC)


SC_Fan = SC.Appliance(4,30,2,540,0.27,30)
SC_Fan.windows([540,1200],[0,0],0.35)


# SC_Air_Conditioner = SC.Appliance(1,900,2,450,0.2,15)
# SC_Air_Conditioner.windows([480,1200],[0,0],0.35)