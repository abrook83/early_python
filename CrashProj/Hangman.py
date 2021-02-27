inp = input("Player 1 enter your word: ")

letters = []

for letter in inp:
    letters.append(letter)      # make a list of the letters in the word

w_len = len(letters)
print(f"Player 2, your word is {w_len} letters long!")


p2_guess = input("Enter a letter: ")

guesses = []
guesses.append(p2_guess)        # add each guess to the list of guesses

for guess in guesses:
    guess = guess.lower
    if guess in guesses:
        print(f"Yup, {guess} is in the word!")
