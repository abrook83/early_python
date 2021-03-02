inp = input("Player 1 enter your word: ")

inp = inp.lower()
count = 0
letters = {}            # empty dictionary
guesses = {}                        # empty dict of guesses

for letter in inp:
    count += 1
    letters[count] = letter     # add each letter and its place to the dictionary
    guesses[count] = "_"

print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 2, your word is {count} letters long...")

for k,v in guesses.items():
    print(v)            # prints however many blank (under)spaces

unsolved = True
guess_list = []         # empty list of guesses

while unsolved:
    pguess = input("Enter a letter: ")
    guess_list.append(pguess.lower())        # add each guess to the dict of guesses
    for guess in guess_list:
        if pguess in letters.values():
            print(f"\n'{pguess}' is correct!")
            break
        elif pguess not in letters.values():
            print("\nSorry, try again.")
            break
            
      
#     guess = guess.lower()
#     if guess in guesses:
#         print(f"Yup, {guess} is in the word!")
