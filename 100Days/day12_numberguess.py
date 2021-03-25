import random
from day12_numberguessart import logo, clear

print(logo)

# Number Guessing Game Scope:

# DONE Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

guesses = 0

def select_difficulty():       
    """ sets the number of guesses to eith 5 or 10 """
    if input("Select difficulty: Easy(e) / Hard(h):\n") == 'h':
        return guesses + 5
    else:
        return guesses + 10

def play(guesses):
    """ runs the game with the selected difficulty """
    rand_num = random.randrange(1,100)
    game_on = True
    print("I'm thinking of a number between 1 & 100, can you guess what it is???")
    while game_on:
        if guesses == 0:
            print("You're out of guesses, better luck next time...")
            game_on = False
        else: 
            guess = int(input("Enter your guess...:\n"))
            if guess == rand_num:
                print(f"Yeeaaaahhhh, the answer was {rand_num}, You Win!!")
                # guesses = 0
                game_on = False
            elif guess > rand_num:
                print("Too high")
                guesses -=1
                print(f"You have {guesses} guesses left")
                continue
            elif guess < rand_num:
                print("Too low")
                guesses -= 1
                print(f"You have {guesses} guesses left")
                continue

if input("Play a game?(y/n):\n") == 'y':
    guesses = select_difficulty()
    play(guesses)

