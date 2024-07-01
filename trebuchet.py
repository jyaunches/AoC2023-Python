from typing import List, Optional

# class LineValues:
#     def __init__(self):
#         self.first_char: Optional[str] = None
#         self.last_char: Optional[str] = None

#     def assign(self, value: int):
#         value_str = str(value)
#         if self.first_char is None:
#             self.first_char = value_str
#         self.last_char = value_str

#     @property
#     def calibration_value(self) -> Optional[int]:
#         if self.first_char and self.last_char:
#             return int(self.first_char + self.last_char)
#         return None


# class CalibrationSum:
#     LIBRARY = {
#         "one": 1, "two": 2, "three": 3, "four": 4, 
#         "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
#     }

#     def get_sum(self, input_list: list[str]) -> int:
#         return sum(self.parse_line(line).calibration_value or 0 for line in input_list)

#     def parse_line(self, line: str) -> LineValues:
#         values = LineValues()
#         for i in range(len(line)):
#             if line[i].isdigit():
#                 values.assign(int(line[i]))
#             else:
#                 for word, num in self.LIBRARY.items():
#                     if line[i:].startswith(word):
#                         values.assign(num)
#                         break
#         return values











def find_calibration_sum(input):
    total = 0
    for i in input:
        digits = [char for char in i if char.isdigit()]        
        num_str = str(digits[0]) + str(digits[-1])
        total += int(num_str)
        
    return total

def find_calibration_sum_with_words(input):
    DIGITS = {str(d): d for d in range(10)}
    EXTENDED_DIGITS = DIGITS | {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }  
    
    total = 0
    for line in input:
        subset = {key: value for key, value in EXTENDED_DIGITS.items() if key in line}
        print(f"Subset: {subset}")
        if not subset:
            continue
        
        # This tells min to compare the items based on the position of their keys in line from the left.
        x = min(subset.items(), key=lambda item: line.index(item[0]))[1]                
        
        # This tells max to compare the items based on the position of their keys in line from the right.
        y = max(subset.items(), key=lambda item: line.rindex(item[0]))[1]
        
        total += int(str(f"{x}{y}"))
        
    return total