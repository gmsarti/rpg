import json
import random

# Load travel shifts
with open("data/travel_shifts.json", "r") as f:
    travel_shifts = json.load(f)["travel_shifts"]

# Load weather conditions
with open("data/weather.json", "r") as f:
    weather_conditions = json.load(f)["weather_conditions"]

# Select a random travel shift
selected_shift = random.choice(travel_shifts)

# Simulate rolling 2d6
roll = random.randint(1, 6) + random.randint(1, 6)

# Select weather condition based on the roll
# Note: We're using (roll - 2) as index because the minimum roll is 2
selected_weather = weather_conditions[min(roll - 2, len(weather_conditions) - 1)]

print(f"Travel Shift: {selected_shift}")
print(f"Weather Condition: {selected_weather}")
