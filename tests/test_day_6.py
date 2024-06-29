import unittest

from boat_race import calculate_boat_race, part2
from data_loader import DataLoader

# 152 min
class TestDay6(unittest.TestCase):
    
    # challenge 1 tests
    def test_finds_correct_results(self):
        input = DataLoader.load_string_array('boat_race_input')
        results = calculate_boat_race(input)
            
        self.assertEqual(results, 170000)
        
    # challenge 2 tests
    def test_kerning_solution(self):
        input = DataLoader.load_string_array('boat_race_input')
        results = part2(input)
        
        self.assertEqual(results, 20537782)
    
        
if __name__ == '__main__':
    unittest.main()