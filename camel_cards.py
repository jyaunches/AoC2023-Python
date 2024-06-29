import re
import math
from functools import reduce
from collections import defaultdict
from collections import Counter
from enum import Enum

class PokerHandType(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    OTHER = 0

class Hand:    
    
    def __init__(self, config, bet):
        self.hand_type = self.identify_hand(config)
        self.config = config
        self.bet = int(bet)
        self.rank = 0
    
    def identify_hand(self, config) -> PokerHandType:
        matches = Counter(config).most_common(2)
        first_match = matches[0][1]
        second_match = matches[1][1] if len(matches) > 1 else 0          
        
        if first_match >= 5:
            return PokerHandType.FIVE_OF_A_KIND
        elif first_match >= 4:
            return PokerHandType.FOUR_OF_A_KIND
        elif first_match + second_match >= 5:
            return PokerHandType.FULL_HOUSE
        elif first_match >= 3:
            return PokerHandType.THREE_OF_A_KIND
        elif first_match + second_match >= 4:
            return PokerHandType.TWO_PAIR
        elif first_match >=2:
            return PokerHandType.ONE_PAIR
        else:
            return PokerHandType.OTHER
    
    def win_amount(self) -> int:
        return self.bet * self.rank
    
    def beats_on_order(self, hand) -> bool:
        for lh, rh in zip(self.config, hand.config):
            lhi = '23456789TJQKA'.index(lh)
            rhi = '23456789TJQKA'.index(rh)
            if lh != rh:
                return lhi > rhi                                        
            
        return False
    
class CamelCards:
    def playHands(self, input: list) -> int:
        hands = []
        
        for line in input:
            separated = line.split(" ")
            hand_config = separated[0]
            bet = separated[1]
            hands.append(Hand(hand_config, bet))            
            
        #type_sorted = sorted(hands, key=lambda x: x.hand_type.value)
        
        grouped_hands = defaultdict(list)      
        
        for hand in hands:
            existing_group = grouped_hands.get(hand.hand_type, [])
            
            inserted = False
            for (index, ranked_hand) in enumerate(existing_group):
                if hand.beats_on_order(ranked_hand):
                    existing_group.insert(index, hand)
                    inserted = True
                    break
                
            if not inserted:
                existing_group.append(hand)
                        
            grouped_hands[hand.hand_type] = existing_group
            
        #rank
        ranked = []
        for hand_type in PokerHandType:
            eval_group = grouped_hands[hand_type]
            if eval_group is not None:
                ranked = ranked + eval_group
                
        total_winnings = 0
        
        for (index, ranked_hand) in enumerate(reversed(ranked)):
            total_winnings += (index+1) * ranked_hand.bet
        
        return total_winnings