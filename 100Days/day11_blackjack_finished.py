### House Rules ###

## The deck is unlimited in size. 
## The the Ace can count as 11 or 1.

import random
from day11_blackjackart import logo, clear
print(logo)

def deal_a_card():
    """ deal a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):             # plug in a list of cards to calculate results....
    if sum(cards) == 21 and len(cards) == 2:  # if there's 2 cards and they amount to 21....
        return 0                            # make an exception that blackjack = a score of zero
    if 11 in cards and sum(cards) > 21:     # check for an 11 and change it to an ace card
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, dealer_score):      # compare the scores to determine the winner
    if player_score > 21 and dealer_score > 21: # if both players over 21, player loses...
        return "\n\tPlayer Bust, You Lose!\n"
    if player_score == dealer_score:
        return "\n\tDraw\n"
    elif dealer_score == 0:
        return "\n\tYou lose, dealer has Blackjack\n"
    elif player_score == 0:
        return "\n\tBlackjack - You Win!\n"
    elif player_score > 21:
        return "\n\tYou went over 21, You lose\n"
    elif dealer_score > 21:
        return "\n\tDealer went over 21, You win!\n"
    elif player_score > dealer_score:
        return "\n\tYou win!\n"
    else:
        return "\n\tYou lose...\n"

def play():       
    """ play a round """
    player_cards = []
    dealer_cards = []
    game_on = True

    for card in range(2):
        player_cards.append(deal_a_card())       # deal and add 2 cards to both the player's and dealer's decks 
        dealer_cards.append(deal_a_card())

    while game_on:
        player_score = calculate_score(player_cards)        # plug the player's 2 cards into the calculate score function
        dealer_score = calculate_score(dealer_cards)        # same for the dealer's cards....
        print(f"Player's cards: {player_cards}")
        print(f"\n\tPlayer's score: {player_score}")
        print(f"\nDealer's first card: {dealer_cards[0]}\n")

        if player_score > 21 or player_score == 0 or dealer_score == 0:     # uses the blackjack score of 0
            game_on = False
        else:
            if input("Would you like another card? (y/n):\n") == 'y':       # asks to continue
                player_cards.append(deal_a_card())
            else:
                game_on = False         # or end

    while dealer_score != 0 and dealer_score < 17:    # sets the boundaries for auto dealing once player calls it quits
        dealer_cards.append(deal_a_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"\nPlayer's cards: {player_cards}\nPlayer's score: {player_score}")
    print(f"Dealer's cards: {dealer_cards}\nDealer's score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Blackjack? y/n?: ") == "y":        # starts the game....
    print(clear)
    play()