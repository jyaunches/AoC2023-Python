import json
from data_loader import DataLoader

def calculate_boat_race(input: list) -> list:
    results = [1,2,3]
    for result in results:
        print(f"  {result}")
    return results

input = DataLoader.load_string_array('boat_race_input')
results = calculate_boat_race(input)