from core import User
User_list = []


ME = User("Medical equipment", 1)
User_list.append(IL)


ME_sterilizer_stove = ME.Appliance(3,600,2,120,0.3,30, occasional_use=0.33)
ME_sterilizer_stove.windows([480,720],[780,1020],0.35)

ME_needle_destroyer = ME.Appliance(1,70,1,60,0.3,10, occasional_use=0.33)
ME_needle_destroyer.windows([480,720],[0,0],0.35)

ME_microscope = ME.Appliance(2,3,2,120,0.2,10, occasional_use=0.33)
ME_microscope.windows([480,720],[840,960],0.35)

ME_dental_compresor = ME.Appliance(2,500,2,60,0.15,10, occasional_use=0.33)
ME_dental_compresor.windows([480,720],[840,1260],0.35)

ME_centrifuge = ME.Appliance(2,100,1,60,0.15,10, occasional_use=0.33)
ME_centrifuge.windows([480,720],[0,0],0.35)

ME_serological_rotator = ME.Appliance(2,10,1,60,0.25,15, occasional_use=0.33)
ME_serological_rotator.windows([480,720],[0,0],0.35)