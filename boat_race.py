
import re
from math import ceil, floor, prod, sqrt
from data_loader import DataLoader

NUMBER = re.compile(r"\d+")

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
    
def part2(data):
    line1, line2 = filter(None, data)
    return _wincount(
        int("".join(NUMBER.findall(line1))), int("".join(NUMBER.findall(line2)))
    )  