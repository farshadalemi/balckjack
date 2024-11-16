
from hand_calculator import HandCalculator

class DisplayHand:  
    @staticmethod
    def interface(player_hand, computer_hand, reveal_hand=False):
        print('-' * 50)
        print(f'\nYour cards are: {player_hand} with value of {HandCalculator.calculator(player_hand)}')
        
        if reveal_hand:
            print("Computer's hand:", computer_hand, "Value:", HandCalculator.calculator(computer_hand))
        else:
            print("Computer's hand: [", computer_hand[0], ", <Card is hidden>]")
