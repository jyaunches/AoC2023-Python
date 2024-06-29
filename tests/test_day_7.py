import unittest

from data_loader import DataLoader
from camel_cards import CamelCards
from camel_cards import Hand

# 180 min
class TestCamelCards(unittest.TestCase):
        
    def test_camel_cards(self):
        input = DataLoader.load_string_array('camel_cards.txt')
        game = CamelCards()
        result = game.playHands(input)
        self.assertEqual(result, 248113761)
        
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