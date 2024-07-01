import unittest

from data_loader import DataLoader
from trebuchet import find_calibration_sum, find_calibration_sum_with_words


class TestDay1(unittest.TestCase):
    
    # 9 min
    # challenge 1 tests
    def test_finds_correct_results(self):
        input = DataLoader.load_string_array('trebuchet.txt')
        result = find_calibration_sum(input)
            
        self.assertEqual(result, 54390)
    
    # started 10:55
    def test_incorporates_words(self):    
        input = DataLoader.load_string_array('trebuchet.txt')
        result = find_calibration_sum_with_words(input)
            
        self.assertEqual(result, 54277)
    
        
if __name__ == '__main__':
    unittest.main()