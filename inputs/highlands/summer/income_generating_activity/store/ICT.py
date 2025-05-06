from ramp.core.core import User
User_list = []


ICT = User("ICT", 1)
User_list.append(ICT)


ICT_Radio = ICT.add_appliance(1,36,2,60,0.1,5)
ICT_Radio.windows([390,450],[1140,1260],0.35)