from ramp.core.core import User
User_list = []


M = User("Machinery", 1)
User_list.append(M)

M_welding_machine = M.add_appliance(1,5500,1,60,0.5,30, wd_we_type=0)
M_welding_machine.windows([0,1440],[0,0],0.35)

M_grinding_machine = M.add_appliance(1,750,1,480,0.2,60, wd_we_type=0)
M_grinding_machine.windows([0,1440],[0,0],0.35)
