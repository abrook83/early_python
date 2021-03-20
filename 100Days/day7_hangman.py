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
tried = []

while not end_of_game:
    p2_guess = input("Enter a letter to guess:\n").lower()
    tried.append(p2_guess)
    if p2_guess not in letters:
      print(f"\nNope, try another!\n\n{guess_list}")
      lives_left -=1
      print(stages[lives_left])
      print(f"Letters tried so far: {tried}")
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
      print(f"\nYup, '{p2_guess}' is in there!\n\n{guess_list}")
      print(f"Letters tried so far: {tried}")
      if letters == guess_list:
          print(f"\nThe word was '{p1_word}' - Well done!\n")
          end_of_game = True
          break