#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:41:34 2023

@author: claudia
"""

import json
from core import User, np
User_list = []

with open('input_variables.json', 'r') as json_file:
    variables = json.load(json_file)
    
def generate_python_scripts(variables):
    for i, params in enumerate(variables):
        # Define the Python script template with placeholders
        template = f'''
        # This is an automatically generated Python script
        param1 = {params['param1']}
        param2 = "{params['param2']}"
        param3 = {params['param3']}
        
        # Your model code here
        '''
    P = {variables["pop_2025"]}
    PPH = 3.68 #people per household
    ALT = {variables["elevation"]}
    PR = {variables["poverty_rate"]}
    TH = {variables["travel_hours"]}
    
#defining users

    #H1 = Lowlands low consumption household
    #H2 = Lowlands high consumption household
    #H3 = Valleys low consumption household
    #H4 = Valleys high consumption household
    #H5 = Highlands low consumption household
    #H6 = Highlands high consumption household

    LC = int(round(P/PPH)*PR) #Low Consumption Household
    HC = round(P/PPH) - LC #High Consumption Household
    if (ALT < 1800): #Lowlands households
        H1 = User("Lowlands low consumption household", LC) 
        User_list.append(H1)
        H2 = User("Lowlands high consumption household", HC)
        User_list.append(H2)
    elif (1800 < ALT < 3000): #Valleys households
        H3 = User("Valleys low consumption household", LC) 
        User_list.append(H3)
        H4 = User("Valleys high consumption household", HC)
        User_list.append(H4)
    else: #highlands housegolds
        H5 = User("Highlands low consumption household", LC)
        User_list.append(H5)
        H6 = User("Highlands high consumption household", HC)
        User_list.append(H6)

        #Health facilities

    if (P < 500):
        if (TH < 2):
            pass
        else:
            HP = User("Health post", 1)
            User_list.append(HP)
        
    elif (500 < P <1000):
        HP = User("Health post", 1)
        User_list.append(HP)
    else:
        HC = User("Health center", 1)
        User_list.append(HC)

        #Schools

    if (P < 100):
        if (TH < 1):
           pass
        else:
            S1 = User("School type 1", 1)
            User_list.append(S1)
    elif (100 < P < 500):
        S2 = User("School type 2", 1)
        User_list.append(S2)
    else:
        S3 = User("School type 3", 1)
        User_list.append(S3)

        #Public lighting

    PL = round(P/30)
    Public_lighting = User("Public lighting ", PL)
    User_list.append(Public_lighting)

    #Potable water system

    if (P<200):
        pass
    else: 
        PW = User("Potable water system", 1)
        User_list.append(PW)

    #IGAs
     
    #Commerce (Grocery Stores, Restaurants, Entertainmet bussiness, Workshops)

    if (ALT > 2000)  :
        R1 = round(P/75)
        R = User("Restaurant 1", R1)
        User_list.append(R)
        GS1 = round(P/65)
        GS = User("Grocery Store 1", GS1)
        User_list.append(GS)
        EB1 = round(P/250)
        EB = User("Entertainment bussiness", EB1)
        User_list.append(EB)
        WS1 = round(P/85)
        WS = User("Workshop 1", WS1)
        User_list.append(WS)
    else:
        R2 = round(P/70)
        R = User("Restaurant 2", R2)
        User_list.append(R)
        GS2 = round(P/350)
        GS = User("Grocery Store 2", GS2)
        User_list.append(GS)
        EB2 = round(P/150)
        EB = User("Entertainment bussiness 2", EB2)
        User_list.append(EB)
        WS2 = round(P/80)
        WS = User("Workshop 2", WS2)
        User_list.append(WS)

    #Agriculture 

    if (Alt > 3000): #Highlands
        Agroproductive_units_1 = round(P/85)
        APU1 = User("Agroproductive Unit 1", Agroproductive_units_1)
        User_list.append(APU1)
    elif (Alt > 2000): #Valleys
        Agroproductive_units_2 = round(P/65)
        APU2 = User("Agroproductive Unit 2", Agroproductive_units_2)
        User_list.append(APU2)
    else: #Lowlands (Chaco, Tropical lowlands, Amazonia)
        Agroproductive_units_3 = round(P/50)
        APU3 = User("Agroproductive Unit 3", Agroproductive_units_3)
        User_list.append(APU3)

        # Write the Python script to a .py file
        script_filename = f'script_{i}.py'
        with open(script_filename, 'w') as script_file:
            script_file.write(template)

# Call the function to generate Python scripts
generate_python_scripts(variables)