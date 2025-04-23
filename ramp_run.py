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
import time


def load_user_input(filepath):
    try:
        spec = importlib.util.spec_from_file_location("user_module", filepath)
        user_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(user_module)

        if hasattr(user_module, "User_list"):
            return user_module.User_list
        else:
            raise AttributeError(f"{filepath} does not contain a 'User_list'.")
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return []


def get_simulation_dates(config, season=None):
    sim_settings = config['simulation_settings']
    mode = sim_settings.get('simulation_mode', 'seasonal')

    if mode == 'date_range': 
        date_start = pd.to_datetime(sim_settings['date_start'])
        date_end = pd.to_datetime(sim_settings['date_end'])
        days = (date_end - date_start).days + 1

    elif mode == 'seasonal':
        if season is None:
            raise ValueError("Season must be provided in 'seasonal' mode.")
        days = sim_settings['days_per_season'].get(season, 90)
        date_start = pd.to_datetime("2020-01-01")
        date_end = date_start + pd.Timedelta(days=days - 1)

    elif mode == 'full_year':
        total_days = sum(sim_settings['days_per_season'].get(season, 90) for season in sim_settings['seasons'])
        date_start = pd.to_datetime("2020-01-01")
        date_end = date_start + pd.Timedelta(days=total_days - 1)
        days = total_days

    else:
        raise ValueError(f"Unknown simulation mode: {mode}")

    return date_start, date_end, days


def collect_users(config, base_input_dir):
    users_by_level = defaultdict(list)
    sim_settings = config['simulation_settings']

    print(f"Starting user collection with simulation mode: {sim_settings['simulation_mode']}")

    for region in sim_settings['regions']:
        for season in sim_settings['seasons']:
            for sector, user_types in sim_settings['sectors'].items():
                for user_type, settings in user_types.items():
                    count = settings.get('count', 1)
                    services = settings.get('energy_service', [])
                    if count < 1 or not services:
                        continue

                    print(f"Collecting users for region: {region}, season: {season}, sector: {sector}, user_type: {user_type}")

                    for i in range(count):
                        for service in services:
                            path = os.path.join(base_input_dir, region, season, sector, user_type, f"{service}.py")
                            if os.path.isfile(path):
                                print(f"Found user input file: {path}")
                                User_list = load_user_input(path)
                                for user in User_list:
                                    print(f"Loaded user: {user}") 
                                    # Categorize user based on simulation levels
                                    if 'energy_service' in sim_settings['simulation_levels']:
                                        users_by_level['energy_service'].append(user)
                                    if 'sector' in sim_settings['simulation_levels']:
                                        users_by_level[f"sector_{sector}"].append(user)
                                    if 'user_type' in sim_settings['simulation_levels']:
                                        users_by_level[f"user_type_{user_type}"].append(user)
                                    if 'community' in sim_settings['simulation_levels']:
                                        users_by_level[f"community_{region}_{season}"].append(user)
                            else:
                                print(f"Warning: File not found: {path}")

    print(f"Users by level after collection: {dict(users_by_level)}")
    print(f"Total users collected: {sum(len(users) for users in users_by_level.values())}")

    return users_by_level


def run_simulations(users_by_level, config, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    sim_settings = config['simulation_settings']

    for region in sim_settings['regions']:
        for season in sim_settings['seasons']:
            date_start, date_end, season_days = get_simulation_dates(config, season)
            full_year_simulation = sim_settings.get('full_year_simulation', True)

            for level in sim_settings['simulation_levels']:
                matching_keys = [k for k in users_by_level if k.startswith(level)]

                for key in matching_keys:
                    users = users_by_level[key]
                    print(f"Running simulations for key: {key} with {len(users)} user(s)")
                    print(f"Simulation period: {date_start} to {date_end} ({season_days} days)")

                    use_case = UseCase(users=users, date_start=date_start, date_end=date_end)
                    result = use_case.generate_daily_load_profiles()

                    df = pd.DataFrame(result)
                    df.index.name = 'time'

                    suffix = f"{key}_{season}_{region}" if not full_year_simulation else f"{key}_full_year_{region}"
                    output_path = os.path.join(output_dir, f"load_curve_{suffix}.csv")
                    df.to_csv(output_path)

                    print(f"Saved: {output_path}")


if __name__ == "__main__":
    start_time = time.time()  # ⏱️ Start the timer

    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)

    base_input_dir = "inputs"  # directory where input .py files are stored
    output_dir = config['simulation_settings'].get('output_folder', 'output')

    users_by_level = collect_users(config, base_input_dir)
    run_simulations(users_by_level, config, output_dir)

    end_time = time.time()  # ⏱️ End the timer
    duration = end_time - start_time
    print(f"\n✅ Total execution time: {duration:.2f} seconds")

