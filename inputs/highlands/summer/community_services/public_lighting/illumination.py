from ramp.core.core import User
User_list = []


PL = User("Public Lighting", 1)
User_list.append(PL)

PL_lamp_post = PL.add_appliance(1,40,2,310,0,300)

PL_lamp_post.windows([0,362],[1082,1440],0.1)
# [0, 362]: First time window of operation (00:00 to 06:02)
# [1082, 1440]: Second time window of operation (18:02 to 24:00)
# 0.1: Probability of use during these windows (10%)
