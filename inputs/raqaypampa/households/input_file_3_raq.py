#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:26:35 2024

@author: claudia
"""

from ramp.core.core import User

User_list = []

"""
This input file represents a High Consumption household in Raqaypampa Autonomous Territory
"""
# Create new user classes
HC = User("high consumption", 1)
User_list.append(HC)


# Create new appliances
HC_LED_1 = HC.Appliance(1, 3, 1, 180, 0.3, 60)  #luz externa (considerar para la proxima encuesta diferenciar entre led interno y externo)
HC_LED_1.windows([1080, 1440], [0, 0], 0.2)

HC_LED_2 = HC.Appliance(1, 3, 2, 300, 0.3, 120) #luz interna
HC_LED_2.windows([0, 480], [1080, 1440], 0.2)

HC_Phone_charger = HC.Appliance(2, 5, 1, 180, 0.3, 60)   #considerar cargar de celulares de familiares/vecinos
HC_Phone_charger.windows([720, 1440], [0, 0], 0.35)

HC_radio = HC.Appliance(1, 5, 2, 120, 0.3, 60)  # funciona solo conectada
HC_radio.windows([360, 720], [1080, 1260], 0.35)




if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
    )
    uc.initialize(peak_enlarge=0.15)

    Profiles_list = uc.generate_daily_load_profiles(flat=False)

    # post-processing
    from ramp.post_process import post_process as pp

    Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
        Profiles_list
    )
    pp.Profile_series_plot(
        Profiles_series
    )  # by default, profiles are plotted as a series
    
    if (
        len(Profiles_list) > 1
    ):  # if more than one daily profile is generated, also cloud plots are shown
        pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
        
    # this would be a new method using work of @mohammadamint
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'output_file_3_raq.csv')