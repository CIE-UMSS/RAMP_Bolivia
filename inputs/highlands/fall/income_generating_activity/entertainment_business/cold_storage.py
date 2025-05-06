from ramp.core.core import User
User_list = []


CS = User("Cold Storage", 1)
User_list.append(CS)

CS_Freezer = CS.add_appliance(1 ,200 ,1 ,1440 ,0 ,30 ,'yes' ,3)
CS_Freezer.windows([0 ,1440] ,[0 ,0])
CS_Freezer.specific_cycle_1(200 ,15 ,5 ,15)
CS_Freezer.specific_cycle_2(200 ,15 ,5 ,15)
CS_Freezer.specific_cycle_3(200 ,10 ,5 ,20)
CS_Freezer.cycle_behaviour([480 ,1200] ,[0 ,0] ,[300 ,479] ,[0 ,0] ,[0 ,299] ,[1201 ,1440])
