stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


p1_word = input("Player 1 enter your word:\n").lower()

letters = []
guess_list = []
end_of_game = False

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

char_count = len(p1_word)

print(f"Player 2 your word is {char_count} letters long!")

for char in p1_word:
    letters.append(char)
    guess_list += "_"

### overthought, reverted to saved....

# for char in guess_list:
#     print(char)

print(guess_list)
lives_left = len(stages)

while not end_of_game:
    p2_guess = input("Enter a letter to guess:\n").lower()
    if p2_guess not in letters:
      print(f"\nNope, try another!\n\n{guess_list}")
      lives_left -=1
      # print(stages[wrong_count])
      if lives_left == 0:
        print("\nStop it! He's dead already!!\n")
        end_of_game = True
      else:
        continue
    else:
      for pos in range(len(letters)):
          letter = p1_word[pos]
          if letter == p2_guess:
              guess_list[pos] = letter
      print(f"\nYup, it's in there!\n\n{guess_list}")
      if letters == guess_list:
          print("\nWell done!\n")
          end_of_game = True
          break