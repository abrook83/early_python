inp = input("Player 1 enter your word: ")

letters = []

for letter in inp:
    letters.append(letter)

# print(letters)

p2_guess = input("Player 2 enter a letter: ")

guesses = []
guesses.append(p2_guess)

for guess in guesses:
    if guess in guesses:
        print("Got one!")
        