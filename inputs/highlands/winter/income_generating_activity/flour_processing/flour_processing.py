from ramp.core.core import User
User_list = []

# Definig users

Quinoa = User("FlourProcessing", 1)
User_list.append(Quinoa)

# Appliances

# Quinoa washing

Quinoa_washing_machine = Quinoa.add_appliance(1, 1500, 1, 300, 0.1, 15)
Quinoa_washing_machine.windows([420, 1080], [0, 0], 0.1)  # [7 to 18 ]

# Flour processing
LAU_grain_dryer = Quinoa.add_appliance(1, 5000, 1, 180, 0.2, 30)
LAU_grain_dryer.windows([420, 1080], [0, 0], 0.2)

LAU_grain_miller = Quinoa.add_appliance(1, 11700, 1, 180, 0.2, 30)
LAU_grain_miller.windows([420, 1080], [0, 0], 0.2)

LAU_grain_toaster = Quinoa.add_appliance(1, 780, 1, 90, 0.2, 15)
LAU_grain_toaster.windows([420, 1080], [0, 0], 0.2)
