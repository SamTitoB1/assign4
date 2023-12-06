
import random
import time
def create_deck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    for suit in suits:
        for value in values:
            card = f"{value} of {suit}"
            deck.append(card)

    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop(0)

def calculate_score(cards):
    score = 0
    ace_count = 0

    for card in cards:
        if card.startswith('J') or card.startswith('Q') or card.startswith('K'):
            score += 10
        elif card.startswith('A'):
            ace_count += 1
            score += 11
        else:
            score += int(card.split()[0])

    while ace_count > 0 and score > 21:
        score -= 10
        ace_count -= 1

    return score

def show_initial_cards(player_cards, dealer_cards):
    print("\nYour cards:")
    for card in player_cards:
        print(card)
    print("\nDealer's cards:")
    print(dealer_cards[0])
    print("Hidden Card")

def show_all_cards(player_cards, dealer_cards):
    print("\nYour cards:")
    for card in player_cards:
        print(card)
    print("\nDealer's cards:")
    for card in dealer_cards:
        print(card)

def blackjack_game():
    while True:
        print("Welcome to Blackjack!")
        deck = create_deck()
        player_cards = [deal_card(deck), deal_card(deck)]
        dealer_cards = [deal_card(deck), deal_card(deck)]
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        show_initial_cards(player_cards, dealer_cards)

        while player_score < 21:
            choice = input("\nType 'hit' to get another card, or 'stand' to stay: ").lower()
            if choice == 'hit':
                time.sleep(1)
                player_cards.append(deal_card(deck))
                player_score = calculate_score(player_cards)
                show_initial_cards(player_cards, dealer_cards)
            elif choice == 'stand':
                time.sleep(1)
                break

        if player_score == 21:
            print("\nYou have Blackjack!")
        elif player_score > 21:
            print("\nYou bust! Dealer wins.")
            show_all_cards(player_cards, dealer_cards)
        else:
            while dealer_score < 17:
                dealer_cards.append(deal_card(deck))
                dealer_score = calculate_score(dealer_cards)

            show_all_cards(player_cards, dealer_cards)

            if dealer_score > 21:
                print("\nDealer busts! You win.")
            elif dealer_score == player_score:
                print("\nIt's a tie!")
            elif dealer_score > player_score:
                print("\nDealer wins!")
            else:
                print("\nYou win!")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
        print("\nStarting a new game...\n")
        time.sleep(2)  # Add a delay before starting the next game

blackjack_game()