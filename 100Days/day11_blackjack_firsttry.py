### House Rules ###

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random
from day11_blackjackart import logo, clear
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# generate 2 random cards for both player & dealer, show player's cards and score, and dealer's 1st card

player_cards = []
dealer_cards = []

for card in range(2):
    player_cards.append(random.choice(cards))
    player_score = sum(player_cards)
    dealer_cards.append(random.choice(cards))
    dealer_score = sum(dealer_cards)    
    if player_score or dealer_score > 21:
        for card in player_cards and dealer_cards:
            if card != 11:
                game_on = False
            else: 
                card = 1
    elif len(dealer_cards) == 2 and dealer_score == 21:
        print("Dealer Blackjack, You Lose!")
        game_on = False   
    elif len(player_cards) == 2 and player_score == 21:
        print("Blackjack, You Win!")
        game_on = False




print(f"Your cards: {player_cards}")
print(f"Your score: {player_score}")
print(f"Dealer's first card: {dealer_cards}")
# print(f"Dealers' score {dealer_score}")

# if player_score > 21:
#     for card in player_cards:
#         if card != 11:
#             print("Player bust, You Lose!")
#             game_on = False
#         else: 
#             card = 1

game_on = True

while game_on:
    if input("Would you like another card? (y/n):\n") == 'y':
        player_cards.append(random.choice(cards))
        player_score = sum(player_cards)
        print(f"Your cards: {player_cards}")
        print(f"Your score: {player_score}")
        if player_score > 21:
            print("You lose")
            game_on = False
        elif player_score == 21:
            print("Blackjack, You Win!")
            game_on = False
        else:
            continue
    elif dealer_score < 17:
        dealer_cards.append(random.choice(cards))
        dealer_score = sum(dealer_cards)
        print(f"Dealer's cards: {dealer_cards}")
        print(f"Dealer's score: {dealer_score}")
    else:
        game_on = False