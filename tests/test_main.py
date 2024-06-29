import unittest

from main import calculate_boat_race, part2
from data_loader import DataLoader
from camel_cards import CamelCards
from camel_cards import Hand

class TestMain(unittest.TestCase):
    
    def test_finds_correct_results(self):
        input = DataLoader.load_string_array('boat_race_input')
        results = calculate_boat_race(input)
            
        self.assertEqual(results, 170000)
        
    # def test_single_big_race(self):
    #     input = "Time:      71530\n" + "Distance:  940200"
    #     results = part2(input)
        
    #     self.assertEqual(results, 170000)
    
    def test_camel_cards(self):
        input = DataLoader.load_string_array('camel_cards.txt')
        game = CamelCards()
        result = game.playHands(input)
        self.assertEqual(result, 999)
        
    def test_hand(self):
        hand = Hand("TJJTJ", 765)
        result = hand.beats_on_order(Hand("TTT44", 320))
        self.assertTrue(result)
        
    def test_hand_with_face_cards(self):
        hand = Hand("KK677", 765)
        result = hand.beats_on_order(Hand("KTJJT", 320))
        self.assertTrue(result)
        
        
if __name__ == '__main__':
    unittest.main()