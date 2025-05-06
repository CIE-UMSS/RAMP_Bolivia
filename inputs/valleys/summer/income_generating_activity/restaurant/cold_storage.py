from ramp.core.core import User
User_list = []


CS = User("Cold Storage", 1)
User_list.append(CS)


CS_freezer = CS.add_appliance(1,200,1,1440,0,30,'yes',2)
CS_freezer.windows([0,1440],[0,0])
CS_freezer.specific_cycle_1(5,15,200,15)
CS_freezer.specific_cycle_2(5,20,200,10)
CS_freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])


