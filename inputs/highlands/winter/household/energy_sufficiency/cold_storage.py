from core import User
User_list = []


CS = User("Cold Storage", 1)
User_list.append(CS)


CS_Freezer = CS.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2)
CS_Freezer.windows([0, 1440], [0, 0])
CS_Freezer.specific_cycle_1(200, 15, 5, 15) #intemediate
CS_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
CS_Freezer.cycle_behaviour(
    [540, 959], [0, 0], [0, 539], [960, 1440]
)
