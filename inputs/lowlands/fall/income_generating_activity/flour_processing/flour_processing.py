from ramp.core.core import User
User_list = []

# Definig users

FP = User("Flour Processing", 1)
User_list.append(FP)


FP_grain_dryer = FP.add_appliance(1, 5000, 1, 180, 0.2, 30, wd_we_type=0)
FP_grain_dryer.windows([420, 1080], [0, 0], 0.2)

FP_grain_miller = FP.add_appliance(1, 18500, 1, 180, 0.2, 30, wd_we_type=0)
FP_grain_miller.windows([420, 1080], [0, 0], 0.2)

FP_grain_toaster = FP.add_appliance(1, 780, 1, 90, 0.2, 15, wd_we_type=0)
FP_grain_toaster.windows([420, 1080], [0, 0], 0.2)

FP_pump = FP.add_appliance(1, 1700, 2, 60, 0.2, 10, occasional_use=0.33)
FP_pump.windows([420, 720], [840, 1020], 0.35)