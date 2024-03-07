#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:18:25 2024

@author: claudia

MTF
Tier 1 household
"""

from ramp.core.core import User

User_list = []

# Create new user classes
H = User("Tier 1", 1)
User_list.append(H)


# Create new appliances

H_indoor_bulb = H.Appliance(2, 5, 2, 180, 0.2, 10)
H_indoor_bulb.windows([1080, 1440], [0, 30], 0.35)

H_Phone_charger = H.Appliance(2, 5, 2, 120, 0.2, 5)
H_Phone_charger.windows([1080, 1440], [420, 600], 0.35)


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
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'tier_1.csv')