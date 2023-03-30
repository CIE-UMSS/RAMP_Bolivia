# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:26:25 2021

@author: Clau
"""

'''
Processing results
'''

import pandas as pd

df = pd.read_csv("output_file_41.csv")
df = df.drop('Unnamed: 0', axis=1)
df['0']*=(1/60)

minutes = pd.date_range('2025-01-01 00:00:00','2025-12-31 23:59:00',freq='T')

df.index=minutes

df.resample('H').sum().to_csv('output_file_41_h.csv')

