# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:12:30 2021

@author: Clau
"""

from core import User, np
User_list = []

'''
Paper: Energy sufficiency, lowlands.
User: HIGHLANDS agro-productive unit
Quinoa processing
'''

#Definig users

Quinoa = User("Lowlands agro-productive unit", 1)
User_list.append(Quinoa)

#Appliances

# Quinoa washing
    
Quinoa_washing_machine = Quinoa.Appliance(Quinoa,1,1500,1,300,0.1,15)
Quinoa_washing_machine.windows([420,1080],[0,0],0.1) #  [7 to 18 ]
        
# Flour processing
LAU_grain_dryer = Quinoa.Appliance(Quinoa,1,5000,1,180,0.2,30)
LAU_grain_dryer.windows([420,1080],[0,0],0.2)

LAU_grain_miller = Quinoa.Appliance(Quinoa,1,11700,1,180,0.2,30)
LAU_grain_miller.windows([420,1080],[0,0],0.2)

LAU_grain_toaster = Quinoa.Appliance(Quinoa,1,780,1,90,0.2,15)
LAU_grain_toaster.windows([420,1080],[0,0],0.2)

# no need of a thresher because usally diesel is used as a fuel 

