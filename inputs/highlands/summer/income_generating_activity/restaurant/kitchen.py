from ramp.core.core import User
User_list = []


K = User("Kitchen", 1)
User_list.append(K)

K_Blender = K.add_appliance(1,350,2,20,0.375,5)
K_Blender.windows([420,480],[720,780],0.5)