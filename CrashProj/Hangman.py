inp = input("Player 1 enter your word: ")

inp = inp.lower()
count = 0
letters = {}            # empty dictionary
guesses = {}                        # empty dict of guesses

for letter in inp:
    count += 1
    letters[count] = letter     # add each letter and its place to the dictionary
    guesses[count] = "_"        # create the same length dict with blank spaces.

print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 2, your word is {count} letters long...")

# for k,v in guesses.items():
#     print(v)            # prints however many blank (under)spaces

unsolved = True
guess_list = []         # empty list of guesses

pguess = "Enter a letter to guess: "
pguess += f"\nLetters guessed so far: {guess_list} "

while unsolved:
    pguess = input(pguess)
    pguess = pguess[:1].lower()     # each guess is the first letter entered, lower case
    if letters == guesses:
        unsolved = False            # end the game if the dictionaries are the same
    elif pguess in guess_list:        # skip over duplicate guesses...
        print(f"\n\tYou've already tried '{pguess}'")
        print(f"\nGuesses so far: \n{guess_list}")
        continue
    else:
        guess_list.append(pguess.lower())        # add each guess to the dict of guesses
        # for guess in guess_list:
        print(f"\nGuesses so far: \n{guess_list}")
        if pguess in letters.values():      # if the guess is in the dictionary of letters...
            print(f"\n\t'{pguess}' is correct!\n")
            # for k,v in letters.items():
            #     guesses[k] = letters[v]
            #     print(guesses)
            continue
        elif pguess not in letters.values():
            print("\n\tSorry, try again.\n")
            continue

            
