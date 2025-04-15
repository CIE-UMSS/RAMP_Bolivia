from core import User, np
User_list = []

# Highlands user
HLC = User("Highlands Cooking", 1)
User_list.append(HLC)

# Cooking appliance: soup for lunch or dinner
# Thermal cycle:
# - 5 min at 1200 W (boiling) = 100 Wh
# - 20 min at 750 W (simmering) = 250 Wh
# → Total per use = 350 Wh
# !!!!!! occasional_use = 0.008 to ensure average energy stays below 1.005 kWh/year:
# 350 Wh × 0.008 × 365 ≈ 1.02 kWh/year


HLC_soup = HLC.Appliance(
    HLC,
    1,                 # One appliance per household
    1200,              # Max power (for boiling)
    1,                 # One use per day
    25,                # Total use duration
    0,                 # Deterministic
    30,                # Minimum interval
    "yes",
    1,                  #### PODRIA PONER MAS CICLOS Y MÁS OPCIONES DE COMIDAS ???? ---------------
    occasional_use=0.008  # ~0.8% of household
)

# Two variable usage windows:
# - Lunch: between 11:45 and 12:30 (705–750)
# - Dinner: between 18:45 and 19:30 (1125–1170)
HLC_soup.windows([705, 750], [1125, 1170],0.1)

# Full thermal cycle
HLC_soup.specific_cycle_1(
    1200, 5,
    750, 20
)
