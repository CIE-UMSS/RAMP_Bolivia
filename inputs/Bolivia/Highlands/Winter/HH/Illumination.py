from core import User
User_list = []


IL = User("Illumination", 1)
User_list.append(IL)


IL_indoor_lighting = IL.Appliance(
    IL,
    4,         # Number of appliances
    7,         # Power consumption in watts (W) per bulb
    2,         # Number of daily usage cycles
    120,       # Total maximum usage duration per day (minutes)
    0.2,       # Probability of use per day
    10         # Minimum interval between uses in minutes
)

IL_indoor_lighting.windows(
    [1082, 1440],  # First active window: 18:02 to 24:00
    [0, 30],       # Second active window: 00:00 to 00:30
    0.35           # 35% probability of activation outside these windows
)


IL_outdoor_bulb = IL.Appliance(IL ,2 ,13 ,2 ,600 ,0.2 ,10)
IL_outdoor_bulb.windows([0 ,330] ,[1082 ,1440] ,0.35)