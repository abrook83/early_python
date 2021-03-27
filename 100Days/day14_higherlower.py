import random
from day14_higherlowerart import logo, clear, vs
from day14_gamedata import data

# display logo
print(logo)

# start the game
# select 2 * random entries from the dictionary

comparison = []
# takes 2 random entries from the list of data
for entry in range(2):
    to_add = random.choice(data)
    comparison.append(to_add)
# print(comparison)

# display both with vs. logo

# ask for answer from player

# compare answer with actual

# determine winner

# take second entry as first entry to continue play

# ask to play again