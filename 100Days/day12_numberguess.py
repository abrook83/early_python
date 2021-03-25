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

# select the level of difficulty
level = input("Select difficulty: Easy(e) / Hard(h):\n")
if level == 'h':
    guesses = 5
else:
    guesses = 10

game_on = True

def play(guesses):
    
    
    
    
    
    while game_on:
        rand_num = random.randrange(1,100)     
        while guesses > 0:
            guess = int(input("Guess a number between 1 & 100:\n"))
            if guesses == 0:
                game_on = False
            if guess == rand_num:
                print(f"The answer was {rand_num}, You Win!!")
                guesses = 0
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

