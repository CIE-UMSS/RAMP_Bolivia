# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 11:42:48 2025

@author: claudia
"""
import yaml
import os
import importlib.util
from ramp import UseCase
import pandas as pd
from pathlib import Path
from collections import defaultdict


def load_user_input(filepath):
    spec = importlib.util.spec_from_file_location("user_module", filepath)
    user_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(user_module)
    return user_module.user


def collect_users(config, base_input_dir):
    users_by_level = defaultdict(list)
    date_start = config['simulation_settings']['date_start']
    date_end = config['simulation_settings']['date_end']

    for region in config['simulation_settings']['regions']:
        for season in config['simulation_settings']['seasons']:
            for sector, user_types in config['simulation_settings']['sectors'].items():
                for user_type, settings in user_types.items():
                    count = settings.get('count', 1)
                    services = settings.get('energy_service', [])
                    for i in range(count):
                        for service in services:
                            path = os.path.join(base_input_dir, region, season, sector, user_type, f"{service}.py")
                            if os.path.isfile(path):
                                user = load_user_input(path)
                                # Categorize user based on simulation levels
                                if 'energy_service' in config['simulation_settings']['simulation_levels']:
                                    users_by_level['energy_service'].append(user)
                                if 'sector' in config['simulation_settings']['simulation_levels']:
                                    users_by_level[f"sector_{sector}"].append(user)
                                if 'user_type' in config['simulation_settings']['simulation_levels']:
                                    users_by_level[f"user_type_{user_type}"].append(user)
                                if 'community' in config['simulation_settings']['simulation_levels']:
                                    users_by_level[f"community_{region}_{season}"].append(user)

    return users_by_level, date_start, date_end


def run_simulations(users_by_level, date_start, date_end, output_dir, config):
    os.makedirs(output_dir, exist_ok=True)

    # Loop over regions and seasons, running simulations
    for region in config['simulation_settings']['regions']:
        for season in config['simulation_settings']['seasons']:
            season_days = config['simulation_settings']['days_per_season'].get(season, 90)  # Default to 90 days if not defined
            full_year_simulation = config['simulation_settings'].get('full_year_simulation', True)

            if full_year_simulation:
                # Simulate entire year by combining all seasons
                users_by_level_per_season = defaultdict(list)
                for season_name, users in users_by_level.items():
                    users_by_level_per_season[season_name].extend(users)

                use_case = UseCase(users=users_by_level_per_season[season], date_start=date_start, date_end=date_end)
                result = use_case.generate_daily_load_profiles()

                df = pd.DataFrame(result)
                df.index.name = 'time'

                output_path = os.path.join(output_dir, f"load_curve_full_year_{region}.csv")
                df.to_csv(output_path)
                print(f"Saved: {output_path}")
            else:
                # Simulate for specific season days
                use_case = UseCase(users=users_by_level[f"community_{region}_{season}"], date_start=date_start, date_end=date_end)
                result = use_case.generate_daily_load_profiles()

                df = pd.DataFrame(result)
                df.index.name = 'time'

                output_path = os.path.join(output_dir, f"load_curve_{season}_{region}.csv")
                df.to_csv(output_path)
                print(f"Saved: {output_path}")


if __name__ == "__main__":
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    base_input_dir = "inputs"  # directory where input .py files are stored
    output_dir = config['simulation_settings'].get('output_folder', 'output')

    users_by_level, date_start, date_end = collect_users(config, base_input_dir)
    run_simulations(users_by_level, date_start, date_end, output_dir, config)

