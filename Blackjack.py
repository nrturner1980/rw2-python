# Blackjack 21
import random

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
    '7': 7, '8': 8, '9': 9, '10': 10, 
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = list(card_values.keys())
    return[rank + suit for rank in ranks for suit in suits]

def calculate_hand(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[:-1]
        value += card_values[rank]
        if rank == 'A':
            aces += 1
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    

def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def display_hands(player_hand, dealer_hand, show_dealer=False):
    print("\nYour Hand:", ', '.join(player_hand), f"({calculate_hand(player_hand)})")
    if show_dealer:
        print("Dealer's hand", ', '.join(dealer_hand), f"({calculate_hand(dealer_hand)})")
    else:
        print("Dealer's hand: ??, " + ', '.join(dealer_hand[1:]))

def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    while True:
        display_hands(player_hand, dealer_hand)
        if calculate_hand(player_hand) > 21:
            print("You busted! Dealer wins.")
            return
        choice = input("Do you want to (h)it or (s)tand? ").lower()
        if choice == 'h':
            player_hand.append(deal_card(deck))
        elif choice == 's':
            break
        else:
            print("Invalid choice. Type 'h' to hit or 's' to stand.")

    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    display_hands(player_hand, dealer_hand, show_dealer=True)

    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    if dealer_total > 21 or player_total > dealer_total:
        print("You win!")
    elif dealer_total == player_total:
        print("Tie Game!")
    else:
        print("Dealer wins!")


if __name__ == "__main__":
    while True:
        play_blackjack()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break