p1_word = input("Player 1 enter your word:\n").lower()

letters = []
guess_list = []

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

char_count = len(p1_word)

print(f"Player 2 your word is {char_count} letters long!")

for char in p1_word:
    letters.append(char)
    guess_list.append("_")

for char in guess_list:
    print(char)

# print(letters)

while p1_word != guess_list:
    p2_guess = input("Enter a letter to guess:\n").lower()
    for char in letters:
        if p2_guess == char:
            guess_list.replace(char)
        else:
            print("Woops! Try another one...")
