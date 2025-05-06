from ramp.core.core import User
User_list = []


MP = User("Milk Production", 1)
User_list.append(MP)

MP_indoor_bulb = MP.add_appliance(2, 7, 2, 120, 0.2, 10)
MP_indoor_bulb.windows([1107, 1440], [0, 0], 0.35)

MP_outdoor_bulb = MP.add_appliance(1, 13, 2, 600, 0.2, 10)
MP_outdoor_bulb.windows([0, 330], [1107, 1440], 0.35)

MP_cooler_tank = MP.add_appliance(1, 4000, 2, 480, 0.2, 240)
MP_cooler_tank.windows([360, 600], [1080, 1320], 0.2)

MP_milking_machine = MP.add_appliance(1, 800, 2, 120, 0.3, 60, wd_we_type=0)
MP_milking_machine.windows([300, 480], [960, 1080], 0.3)