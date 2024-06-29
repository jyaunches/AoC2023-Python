
import math
import re
from math import ceil, floor, prod, sqrt
from data_loader import DataLoader
from functools import reduce

NUMBER = re.compile(r"\d+")

# started 3:40/3:56 4:44/5:20 -> 52 min (to solution coded)
# debugged 5:20-5:38
# restarted 11:40am / 12:24
# restarted 1:15 / 1:43
# total: 152 min

def _wincount(time, distance):
    mid_point = time / 2
    d = sqrt(mid_point * mid_point - distance)
    result = ceil(mid_point + d - 1) - floor(mid_point - d + 1) + 1
    return result

def calculate_boat_race(input: list) -> int:
        
    return prod(
        _wincount(int(time.group()), int(distance.group()))
        for time, distance in zip(NUMBER.finditer(input[0]), NUMBER.finditer(input[1]))
    )        

input = DataLoader.load_string_array('boat_race_input')
results = calculate_boat_race(input)