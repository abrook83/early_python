inp = input("Player 1 enter your word: ")

inp = inp.lower()
count = 0
letters = {}            # empty dictionary

for letter in inp:
    count += 1
    letters[count] = letter     # add each letter and its place to the dictionary
    
# print(letters)

print(f"\nPlayer 2, your word is {count} letters long...")

pguess = input("Enter a letter: ")

guesses = []
guesses.append(pguess.lower())        # add each guess to the list of guesses
    # for guess in guesses:
      
#     guess = guess.lower()
#     if guess in guesses:
#         print(f"Yup, {guess} is in the word!")
