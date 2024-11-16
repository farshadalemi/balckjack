from variations import variations

class HandCalculator:
    @staticmethod
    def calculator(hand):
        value = sum(variations[card[0]] for card in hand)
        aces = sum(1 for card in hand if card[0] == 'A')
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value




