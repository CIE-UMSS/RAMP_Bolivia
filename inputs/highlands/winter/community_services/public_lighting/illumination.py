from ramp.core.core import User
User_list = []


PL = User("Public Lighting", 1)
User_list.append(PL)


PL_lamp_post = PL.add_appliance(
    PL,        # The user this appliance belongs to
    1,         # Number of appliances
    40,        # Power consumption in watts (W)
    2,         # Number of daily usage cycles
    310,       # Duration of each cycle in minutes
    0,         # (0 = deterministic, 1 = fully random)
    300,       # Minimum interval between uses in minutes
    'yes',     # Uses a specific cycle behavior
    flat = 'yes'  # Flat profile (constant power use during its operating window)
)

PL_lamp_post.windows([0,362],[1082,1440],0.1)
# [0, 362]: First time window of operation (00:00 to 06:02)
# [1082, 1440]: Second time window of operation (18:02 to 24:00)
# 0.1: Probability of use during these windows (10%)
