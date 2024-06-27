import json
import math
from data_loader import DataLoader
from functools import reduce

# started 3:40/3:56 4:44/5:20 -> 52 min (to solution coded)
# debugged 5:20-5:38
# restarted 11:40am / 12:24
def calculate_boat_race(input: list) -> int:
    #parse input
    #construct potential hold ranges
    #trim unneccessary & impossible from front and end (distance to beat / available time = amount to trim)
    #multiple the lengths of the remaining ranges
    #return the result
    
    
    times = input[0].split(':')[1].split(" ")
    times = [s for s in times if s]
    times = list(map(int, times))
    
    distances_to_beat = input[1].split(':')[1].split(" ")
    distances_to_beat = [s for s in distances_to_beat if s]
    distances_to_beat = list(map(int, distances_to_beat))
    

    
    candidates = []
    for i in range(len(times)):
        time = times[i]
        distance_to_beat = distances_to_beat[i]
        
        possible_start_index = math.ceil(distance_to_beat / time) + 1
        print(f"  {possible_start_index}")
        potential_range = list(range(possible_start_index, (time-possible_start_index+1)))
        
        print(f"Initial range:")
        print(f"  {potential_range}")
        
        firm_start_index = False
        firm_end_index = False
        while not firm_start_index and not firm_end_index:
            start_eval_hold = potential_range.pop(0)
            end_eval_hold = potential_range.pop(len(potential_range)-1)
            start_pos_time = (time - start_eval_hold) * start_eval_hold
            if(start_pos_time > distance_to_beat):
                potential_range.insert(0, start_eval_hold)
                firm_start_index = True
               
            end_pos_time = (time - start_eval_hold) * start_eval_hold   
            if(end_pos_time > distance_to_beat):
                potential_range.append(end_eval_hold)
                firm_end_index = True
                                                          
        print(f"Refined range:")
        print(f"  {potential_range}")
        
        candidates.append(potential_range)
        
    
    for candidate in candidates:
        print(f"Candidate:")
        print(f" {candidate}")    
    
    lengths = [len(sub_array) for sub_array in candidates]
    print(f"Lengths")
    print(f"  {lengths}")
    product_of_lengths = reduce(lambda x, y: x * y, lengths, 1)

    print("Product returned")
    print(f"  {product_of_lengths}")
        
    return product_of_lengths

input = DataLoader.load_string_array('boat_race_input')
results = calculate_boat_race(input)