from ramp.core.core import User
User_list = []


PL = User("Public Lighting", 1)
User_list.append(PL)


PL_lamp_post = PL.add_appliance(PL,1,40,2,310,0,300, 'yes', flat = 'yes')
PL_lamp_post.windows([0,362],[1082,1440],0.1)