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

    elif mode in ['seasonal', 'full_year']:
        if season is None:
            raise ValueError("Season must be provided in 'seasonal' or 'full_year' mode.")
        season_dates = sim_settings.get('season_dates', {})
        if season not in season_dates:
            raise ValueError(f"Start/end date for season '{season}' not defined in season_dates.")
        date_start = pd.to_datetime(season_dates[season]['start'])
        date_end = pd.to_datetime(season_dates[season]['end'])
        days = (date_end - date_start).days + 1

    else:
        raise ValueError(f"Unknown simulation mode: {mode}")

    return date_start, date_end, days

def collect_users(config, base_input_dir, season=None):
    users_by_level = defaultdict(list)
    sim_settings = config['simulation_settings']

    for region in sim_settings['regions']:
        seasons_to_loop = [season] if season else sim_settings['seasons']
        for s in seasons_to_loop:
            for sector, user_types in sim_settings['sectors'].items():
                for user_type, settings in user_types.items():
                    count = settings.get('count', 1)
                    services = settings.get('energy_service', [])
                    if count < 1 or not services:
                        continue

                    for i in range(count):
                        for service in services:
                            path = os.path.join(base_input_dir, region, s, sector, user_type, f"{service}.py")
                            if os.path.isfile(path):
                                User_list = load_user_input(path)
                                for user in User_list:
                                    if 'energy_service' in sim_settings['simulation_levels']:
                                        users_by_level[f"energy_service_{user_type}_{service}"].append(user)
                                    if 'sector' in sim_settings['simulation_levels']:
                                        users_by_level[f"sector_{sector}"].append(user)
                                    if 'user_type' in sim_settings['simulation_levels']:
                                        users_by_level[f"user_type_{user_type}"].append(user)
                                    if 'community' in sim_settings['simulation_levels']:
                                        users_by_level[f"community_{region}_{s}"].append(user)
                            else:
                                print(f"Warning: File not found: {path}")

    return users_by_level

def run_simulations(config, base_input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    sim_settings = config['simulation_settings']
    simulation_mode = sim_settings.get('simulation_mode', 'seasonal')
    is_full_year = simulation_mode == 'full_year'

    for region in sim_settings['regions']:
        for level in sim_settings['simulation_levels']:
            if is_full_year and level == 'energy_service':
                seasonal_outputs = defaultdict(list)

                for season in sim_settings['seasons']:
                    date_start, date_end, _ = get_simulation_dates(config, season)
                    users_by_level = collect_users(config, base_input_dir, season)
                    matching_keys = [k for k in users_by_level if k.startswith(level)]

                    for key in matching_keys:
                        users = users_by_level[key]
                        use_case = UseCase(users=users, date_start=date_start, date_end=date_end)
                        result = use_case.generate_daily_load_profiles()
                        df = pd.DataFrame(result)
                        df.index.name = 'time'

                        label = key.replace('energy_service_', '')
                        if isinstance(df, pd.DataFrame) and df.shape[1] == 1:
                            df.columns = [label]
                        else:
                            df = df.sum(axis=1).to_frame(label)

                        seasonal_outputs[label].append(df)

                # Concatenate full year per service
                combined_full_year = []
                for label, seasonal_parts in seasonal_outputs.items():
                    full_df = pd.concat(seasonal_parts, axis=0)
                
                    # Set index to be continuous and name it 'time'
                    full_df.index = range(len(full_df))
                    full_df.index.name = 'time'
                
                    combined_full_year.append(full_df)
                
                final_df = pd.concat(combined_full_year, axis=1)
                output_path = os.path.join(output_dir, f"load_curve_{level}_full_year_{region}.csv")
                final_df.to_csv(output_path)
                print(f"✅ Saved: {output_path}")

            else:
                for season in sim_settings['seasons']:
                    date_start, date_end, _ = get_simulation_dates(config, season)
                    users_by_level = collect_users(config, base_input_dir, season)
                    matching_keys = [k for k in users_by_level if k.startswith(level)]

                    season_dfs = []
                    for key in matching_keys:
                        users = users_by_level[key]
                        use_case = UseCase(users=users, date_start=date_start, date_end=date_end)
                        result = use_case.generate_daily_load_profiles()
                        df = pd.DataFrame(result)
                        df.index.name = 'time'

                        if level == 'energy_service':
                            label = key.replace('energy_service_', '')
                        elif level == 'sector':
                            label = key.replace('sector_', '')
                        elif level == 'user_type':
                            label = key.replace('user_type_', '')
                        elif level == 'community':
                            label = 'community'
                        else:
                            label = key

                        if isinstance(df, pd.DataFrame) and df.shape[1] == 1:
                            df.columns = [label]
                        else:
                            df = df.sum(axis=1).to_frame(label)

                        season_dfs.append(df)

                    if season_dfs:
                        season_combined_df = pd.concat(season_dfs, axis=1)
                        suffix = f"{level}_{season}_{region}"
                        output_path = os.path.join(output_dir, f"load_curve_{suffix}.csv")
                        season_combined_df.to_csv(output_path)
                        print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    start_time = time.time()

    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)

    base_input_dir = "inputs"
    output_dir = config['simulation_settings'].get('output_folder', 'output')

    run_simulations(config, base_input_dir, output_dir)

    end_time = time.time()
    print(f"\n✅ Total execution time: {end_time - start_time:.2f} seconds") 
test

