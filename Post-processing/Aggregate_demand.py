# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:53:22 2021

@author: Clau
"""

import numpy as np
import pandas as pd

#HI
df1 = pd.read_csv('con_IGAS.csv') 
df1.columns = ['T' , 'W'] 
HI_Kwh = (((df1['W'].sum())/60)/1000)
print(HI_Kwh)

'''
#HMI
df2 = pd.read_csv('results/HMI_El_Espino.csv') 
df2.columns = ['T' , 'W'] 
HMI_Kwh = (((df2['W'].sum())/60)/1000)
print(HMI_Kwh)

#LMI
df3 = pd.read_csv('results/LMI_El_Espino.csv') 
df3.columns = ['T' , 'W'] 
LMI_Kwh = (((df3['W'].sum())/60)/1000)
print(LMI_Kwh)

#LI
df4 = pd.read_csv('results/LI_El_Espino.csv') 
df4.columns = ['T' , 'W'] 
LI_Kwh = (((df4['W'].sum())/60)/1000)
print(LI_Kwh)

#If we consider just two categories 

'''














