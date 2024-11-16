import random
from variations import variations
from card_types import Card_Types

class Deck:
    def __init__(self):

        self.full_deck = []
        # print(variations.items())
        for real_card, value in variations.items():
            for card_type in Card_Types:
                self.full_deck.append((real_card, card_type, value))
            
            # for card in self.full_deck:
            #     print(f"{card[0]} of {card[1]} has {card[2]} value.")
        

        self.deck_items = len(self.full_deck) 

        print("Deck size is 52" if self.deck_items else "Deck size is not 52")

    def shuffle(self):
        random.shuffle(self.full_deck)
        
    def check_deck_size(deck_items):
        if deck_items == 52:
            return True
        else:
            return False
    
    def pop(self):
        return self.full_deck.pop() if self.full_deck else None




if __name__ == "__main__":
    deck = Deck()


