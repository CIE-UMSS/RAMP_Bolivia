# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:26:25 2021

@author: Clau
"""

'''
Processing results
'''

import pandas as pd
'''
df1 = pd.read_csv("Scenario_1_1.csv")
df2 = pd.read_csv("Scenario_1_2.csv")
df3 = pd.read_csv("Scenario_1_3.csv")

df = pd.concat([df1,df2,df3])

'''
df = pd.read_csv("PP_of.csv")
df = df.drop('Unnamed: 0', axis=1)
df['0']*=(1/60)

minutes = pd.date_range('2019-01-01 00:00:00','2019-12-31 23:59:00',freq='T')

df.index=minutes

df.resample('H').sum().to_csv('PP_of.csv')

