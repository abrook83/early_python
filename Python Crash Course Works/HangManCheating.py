# After trying to create a game of hangman by looping through dictionaries etc. I peaked
# at some code online and found I was overthinking things way too much. I've downloaded it
# now and am going through to understand and customise.

# Asks for an input word to be guessed 
guess_word = input("P1 enter a word: ")
 
guesses = ''       # creates an empty string of guesses

# multiply the length of the word to be guessed to get a number of tries
w_length = len(guess_word) * 2
turns = int(w_length)
print(f"Number of turns: {turns}")

while turns > 0:        # from the input length sum
    # counts the number of incorrect input guesses
    incorrect = 0
    for letter in guess_word:      # loops through each letter in the 'guess_word',
        if letter in guesses:      # if the letter in guesses matches it,
            print(letter)          # prints it... else....
        else: 
            print("_")              # ...it'll print a blank space.
            incorrect += 1          # and add 1 to the count for incorrect
 
    if incorrect == 0:      # afer looping through letters 'guess_word' and comparing to those in 'guesses'
        print("Winner Winner Chicken Dinner!!")
        print(f"The word was '{guess_word.title()}'") 
        break

    guess = input("Enter a letter: ")
    
    guesses += guess            # add the input letter into the 'guesses' string
    if guess not in guess_word:      
        turns -= 1          # count down if the guess is wrong
        print(f"Sorry, {guess} is not in the word!")
        print(f"{turns} guesses left!")
            
        if turns == 0:
            print("Game over...")
    
