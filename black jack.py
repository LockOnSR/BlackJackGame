import random
import time

    #game start after prompt#
def play_game():
    print("Let's play!")
    time.sleep(3)

    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Deal initial cards
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand, False)

    # Player's turn
    while calculate_score(player_hand) < 21:
        print("Your cards:", player_hand)
        print("Current score:", calculate_score(player_hand))
        if input("Do you want to draw another card? (y/n): ") == "y":
            deal_card(deck, player_hand)
        else:
            break

    # Dealer's turn
    while calculate_score(dealer_hand) < 17:
        deal_card(deck, dealer_hand)

    # Display final hands
    print("Your final hand:", player_hand)
    print("Your final score:", calculate_score(player_hand))
    print("Dealer's final hand:", dealer_hand)
    print("Dealer's final score:", calculate_score(dealer_hand))

    # Determine the winner
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    if player_score > 21:
        print("You went over 21. You lose!")
    elif dealer_score > 21:
        print("Dealer went over 21. You win!")
    elif player_score == dealer_score:
        print("It's a draw!")
    elif player_score > dealer_score:
        print("You win!")
    else:
        print("You lose!")

def create_deck():
    deck = []
    for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
        for card in range(1, 11):
            deck.append(card)
        for card in ["J", "Q", "K"]:
            deck.append(10)
        deck.append(11)  # Ace
    random.shuffle(deck)
    return deck

def deal_card(deck, hand, visible=True):
    card = deck.pop()
    hand.append(card)
    if visible:
        print("Dealt card:", card)

def calculate_score(hand):
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

#Initial screen w/ input#
print("Welcome to the Blackjack Casino!")
time.sleep(3)
print("Let's play a round of Blackjack.")
time.sleep(3)

startGame = input("Are you ready? (Y/N): ")

while startGame == "Y" or startGame == "y":

    play_game()

    startGame = input("Play another hand? (Y/N)")


if startGame == "N" or startGame == "n":
    print("Thanks for stopping by our table, we hope you had good luck!")
    ()
    time.sleep(2)
    print("Stop by our table again for a few more rounds later.")
    time.sleep(2)
    quit
