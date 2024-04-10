#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:29:00 2024

@author: claudia
"""


from ramp.core.core import User

User_list = []

"""
This input file represents a (exceptionally) High Consumption household in Raqaypampa Autonomous Territory
"""
# Create new user classes
VHC = User("Very high consumption", 1)
User_list.append(VHC)


# Create new appliances
VHC_LED_1 = VHC.Appliance(1, 3, 1, 180, 0.3, 60)  #luz externa 
VHC_LED_1.windows([1080, 1440], [0, 0], 0.2)

VHC_LED_2 = VHC.Appliance(1, 3, 2, 300, 0.3, 120) #luz interna 2
VHC_LED_2.windows([0, 480], [1080, 1440], 0.2)

VHC_LED_3 = VHC.Appliance(1, 3, 2, 300, 0.3, 120) #luz interna 2
VHC_LED_3.windows([0, 480], [1080, 1440], 0.2)

VHC_Phone_charger = VHC.Appliance(4, 5, 2, 180, 0.3, 60)   
VHC_Phone_charger.windows([720, 1440], [0, 240], 0.35)

VHC_radio = VHC.Appliance(1, 5, 2, 240, 0.3, 60)  # funciona solo conectada
VHC_radio.windows([360, 720], [1080, 1260], 0.35)

VHC_TV = VHC.Appliance(1, 30, 3, 120, 0.2, 5) # 22 inch LED technology #CRT technology 15 inch: 60W, LED/LCD are more efficient: 15 inch, around 15W
VHC_TV.windows([750, 840], [1170, 1440], 0.35, [0, 30])



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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'output_file_4_raq.csv')