# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:20:32 2021

@author: Clau
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker

def get_useful_columns():
    '''
    Selects the useful columns from de dataset. The analysis is made for May, 2015. 
    '''
    df = pd.read_csv("data_base_bolivia/cbba.csv") #Calling the dataframe
    df = df.loc[:, ['COD_MUNI', 'YEAR', 'MONTH', 'CATEGORY', 'CONS_KWH', 'DIST_SYSTEM']] #selecting useful columns
    cbba = df.loc[(df['COD_MUNI'] == 30101) & (df['YEAR'] == 2015) & (df['CATEGORY'] == 1) & (df['MONTH'] == 5) & (df['CONS_KWH'] > 0)] #Selecting the main municipality, for may of 2015, residential category and consumption different from 0.
    cbba.sort_values('CONS_KWH', inplace=True, ascending=False) #sorting consumption from highest to lowest
    cbba.loc[:,'CONS_KWH'] *= 1000 #converting MWH into KWH (there is an error in the name of the consumption column in the data base, it says KWH but is in MWH instead, so we convert it into KWH)
    cb = cbba.drop(['COD_MUNI','YEAR', 'MONTH', 'CATEGORY','DIST_SYSTEM'], axis=1) #deleting extra collumns to obtain just consumption.
    return cb

cb = get_useful_columns()

def applying_natural_logarithm(cb):
    '''
    The natural logarithm is applied to the electricity consumption data to smooth the distribution.
    '''
    cb['log_CONS_KWH'] = np.log(cb['CONS_KWH'])
    cb.drop(['CONS_KWH'], axis=1)
    return cb

cb_log = applying_natural_logarithm(cb)
cb_log = cb.drop(['CONS_KWH'], axis = 1)
cb_log = cb_log.loc[(cb_log['log_CONS_KWH'] > 0)]

# Frequency histogram 
plt.rcParams["font.family"] = 'times new roman'
histogram = cb_log.plot.hist(cb_log['log_CONS_KWH'], bins = 70,edgecolor='dimgray',figsize=(9,7), color='#ffe5ad')

#UNI
bar_value_to_label = 4.66
min_distance = float("inf")  # initialize min_distance with infinity
index_of_bar_to_label = 0
for i, rectangle in enumerate(histogram.patches):  # iterate over every bar
    tmp = abs(  # tmp = distance from middle of the bar to bar_value_to_label
        (rectangle.get_x() +
            (rectangle.get_width() * (1 / 2))) - bar_value_to_label)
    if tmp < min_distance:  # we are searching for the bar with x cordinate
                            # closest to bar_value_to_label
        min_distance = tmp
        index_of_bar_to_label = i
histogram.patches[index_of_bar_to_label].set_color('lightsteelblue')

#PEQ
bar_value_to_label = 4.8
min_distance = float("inf")  # initialize min_distance with infinity
index_of_bar_to_label = 0
for i, rectangle in enumerate(histogram.patches):  # iterate over every bar
    tmp = abs(  # tmp = distance from middle of the bar to bar_value_to_label
        (rectangle.get_x() +
            (rectangle.get_width() * (1 / 2))) - bar_value_to_label)
    if tmp < min_distance:  # we are searching for the bar with x cordinate
                            # closest to bar_value_to_label
        min_distance = tmp
        index_of_bar_to_label = i
histogram.patches[index_of_bar_to_label].set_color('cornflowerblue')

#GRAN
bar_value_to_label = 5
min_distance = float("inf")  # initialize min_distance with infinity
index_of_bar_to_label = 0
for i, rectangle in enumerate(histogram.patches):  # iterate over every bar
    tmp = abs(  # tmp = distance from middle of the bar to bar_value_to_label
        (rectangle.get_x() +
            (rectangle.get_width() * (1 / 2))) - bar_value_to_label)
    if tmp < min_distance:  # we are searching for the bar with x cordinate
                            # closest to bar_value_to_label
        min_distance = tmp
        index_of_bar_to_label = i
histogram.patches[index_of_bar_to_label].set_color('royalblue')

#HP
bar_value_to_label = 3.46
min_distance = float("inf")  # initialize min_distance with infinity
index_of_bar_to_label = 0
for i, rectangle in enumerate(histogram.patches):  # iterate over every bar
    tmp = abs(  # tmp = distance from middle of the bar to bar_value_to_label
        (rectangle.get_x() +
            (rectangle.get_width() * (1 / 2))) - bar_value_to_label)
    if tmp < min_distance:  # we are searching for the bar with x cordinate
                            # closest to bar_value_to_label
        min_distance = tmp
        index_of_bar_to_label = i
histogram.patches[index_of_bar_to_label].set_color('lightcoral')

#MP
bar_value_to_label = 4.23
min_distance = float("inf")  # initialize min_distance with infinity
index_of_bar_to_label = 0
for i, rectangle in enumerate(histogram.patches):  # iterate over every bar
    tmp = abs(  # tmp = distance from middle of the bar to bar_value_to_label
        (rectangle.get_x() +
            (rectangle.get_width() * (1 / 2))) - bar_value_to_label)
    if tmp < min_distance:  # we are searching for the bar with x cordinate
                            # closest to bar_value_to_label
        min_distance = tmp
        index_of_bar_to_label = i
histogram.patches[index_of_bar_to_label].set_color('#db5856')

#LP
bar_value_to_label = 4.88
min_distance = float("inf")  # initialize min_distance with infinity
index_of_bar_to_label = 0
for i, rectangle in enumerate(histogram.patches):  # iterate over every bar
    tmp = abs(  # tmp = distance from middle of the bar to bar_value_to_label
        (rectangle.get_x() +
            (rectangle.get_width() * (1 / 2))) - bar_value_to_label)
    if tmp < min_distance:  # we are searching for the bar with x cordinate
                            # closest to bar_value_to_label
        min_distance = tmp
        index_of_bar_to_label = i
histogram.patches[index_of_bar_to_label].set_color('#c44240')


histogram.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=len(cb_log['log_CONS_KWH']))) 
histogram.set_title("Cochabamba", fontsize=24)
histogram.set_xlabel("log(EC)",fontsize=20)
histogram.set_ylabel("Percentage of users (%)",fontsize=20)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.grid(color='lightgray', linewidth=1, axis='y', alpha=0.5)
plt.savefig('freq_cbba_log.png', dpi=300)
plt.show()