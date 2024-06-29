import unittest

from main import calculate_boat_race
from data_loader import DataLoader

class TestMain(unittest.TestCase):
    
    def test_finds_correct_results(self):
        input = DataLoader.load_string_array('boat_race_input')
        results = calculate_boat_race(input)
        
        expected_results = [4, 5, 6]
        self.assertEqual(results, 170000)
        
if __name__ == '__main__':
    unittest.main()