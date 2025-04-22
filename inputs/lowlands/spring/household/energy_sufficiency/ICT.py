from core import User
User_list = []


ICT = User("ICT", 1)
User_list.append(ICT)


ICT_TV = ICT.Appliance(1,30,2,120,0.1,5)
ICT_TV.windows([1080,1440],[0,60],0.35)

ICT_Radio = ICT.Appliance(1,36,2,120,0.1,5)
ICT_Radio.windows([390,450],[1082,1260],0.35)

ICT_Phone_charger = ICT.Appliance(4,5,2,120,0.2,10)
ICT_Phone_charger.windows([1020,1440],[0,300],0.35)

ICT_Laptop = ICT.Appliance(1,70,1,90,0.3,30)
ICT_Laptop.windows([960,1200],[0,0],0.35)



