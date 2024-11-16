from deck import Deck 
from display_hands import DisplayHand
from hand_calculator import HandCalculator


def main():
    deck = Deck()
    deck.shuffle()
    # print(deck.pop())
    player_hand = [deck.pop(), deck.pop()]
    print(player_hand)
    computer_hand =  [deck.pop(), deck.pop()]

    while True:
        DisplayHand.interface(player_hand, computer_hand)

        player_value = HandCalculator.calculator(player_hand)
        if player_value > 21:
            print("U lost, Computer Won.")
            return

        move = input("Do you want to Hit (Enter h) or Stand (Enter s) ? ").lower()
        if move == 'h':
            player_hand.append(deck.pop())
        elif move:
            break
        else:
            print("Input value is incorrect, Please enter s or h")


    while HandCalculator.calculator(computer_hand) < 17 :
        computer_hand.append(deck.pop())
    
    dh = DisplayHand()
    dh.interface(player_hand, computer_hand)

    player_value = HandCalculator.calculator(player_hand)
    computer_value = HandCalculator.calculator(computer_hand)



    if computer_value > 21:
        print("computer lost, U won")
    elif computer_value > player_value:
        print("Computer Won.")
    elif computer_value < player_value:
        print("U won")
    else:
        print("It's a tie!")


# main()
if __name__ == "__main__":
    main()























from deck import Deck 
from display_hands import DisplayHand  # Make sure to use the updated name
from hand_calculator import HandCalculator

def main():
    deck = Deck()
    deck.shuffle()
    
    player_hand = [deck.pop(), deck.pop()]
    computer_hand = [deck.pop(), deck.pop()]

    while True:
        DisplayHand.interface(player_hand, computer_hand)  # Use the static method directly

        player_value = HandCalculator.calculator(player_hand)
        if player_value > 21:
            print("You lost, Computer won.")
            return

        move = input("Do you want to Hit (Enter h) or Stand (Enter s)? ").lower()
        if move == 'h':
            player_hand.append(deck.pop())
        elif move == 's':
            break
        else:
            print("Input value is incorrect, please enter 's' or 'h'.")

    while HandCalculator.calculator(computer_hand) < 17:
        computer_hand.append(deck.pop())
    
    DisplayHand.interface(player_hand, computer_hand, reveal_hand=True)  # Reveal the computer's hand

    player_value = HandCalculator.calculator(player_hand)
    computer_value = HandCalculator.calculator(computer_hand)

    if computer_value > 21:
        print("Computer lost, you won!")
    elif computer_value > player_value:
        print("Computer won.")
    elif computer_value < player_value:
        print("You won!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()