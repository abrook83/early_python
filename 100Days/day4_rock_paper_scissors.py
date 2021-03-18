# creating rock/paper/scissors, got a little creative with examples from the 100 Days of Code Udemy course.
# importing rock, paper and scissor basic visuals from the rps_visuals.py file.

import random
import rps_visuals

# assign variable to the imported visuals
rock = rps_visuals.rock
paper = rps_visuals.paper
scissors = rps_visuals.scissors

p1_name = input("Enter player name:\n")

# set win count to allow best of 3 (first to 2)
player_win_count = 0
computer_win_count = 0
while computer_win_count < 2 or player_win_count < 2:
  p1_turn = int(input(f'\nYo {p1_name.title()}, enter Rock(1), Paper(2) or Scissors(3):\n'))
  # error handling -
  if p1_turn not in range(1,4):
    print("Sorry, enter a number between 1 & 3!")
    continue
  else:
    # p1's turn
    if p1_turn == 1:
      print(f"\{p1_name.title()} chose: {rock}")
    elif p1_turn == 2:
      print(f"\{p1_name.title()} chose: {paper}")
    else:
      print(f"\{p1_name.title()} chose: {scissors}")
    
    # pc's turn (random)
    pc_turn = random.randint(1, 3)
    if pc_turn == 1:
      print(f"\nComputer chose: {rock}")
    elif pc_turn == 2:
      print(f"\nComputer chose: {paper}")
    else:
      print(f"\nComputer chose: {scissors}")

    # determine the winner, could shorten this with better math reasoning
    if p1_turn == pc_turn:
      print("It's a tie!!")
    elif p1_turn == 1 and pc_turn == 3:
      print (f"You win this round {p1_name.title()}!")
      player_win_count +=1
    elif p1_turn == 3 and pc_turn == 2:
      print (f"You win this round {p1_name.title()}!")
      player_win_count +=1
    elif p1_turn == 2 and pc_turn == 1:
      print (f"You win this round {p1_name.title()}!")
      player_win_count +=1
    else:
      print("You lose this round!")
      computer_win_count +=1

  # determine best of 3 winner
  if computer_win_count == 2:
    print("\nComputer wins! Better luck next time..." *4)
    print("\n")
  elif player_win_count == 2:
    print("\nWinner winner, chicken dinner!!" *4)
    print("\n")
  
