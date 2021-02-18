# squares = []
# for value in range(1,6):    # for each value between 1 & 6...
#     squ = value ** 2        # raise to the power of 2
#     squares.append(squ)     # add it to the list of squares

# bears = []
# for value in range(1,6,2):  # for each SECOND value between 1 & 6...
#     bears.append(value**2)  # raise to the power of 2, and add to the list 'bears'

# print(squares)
# print(bears)
# print(f"The largest squared number from the first list is {max(squares)}")
# print(f"The sum of the squares list is {sum(squares)}")
# print(f"The sum of the bears list is {sum(bears)}")

# # LIST COMPREHENSION
# squared = [value**2 for value in range(2,11,2)]     # list comrehension for the above code
# print(squared)

# nums = list(range(0,16,3))
# print(nums)

# players = ['charles', 'steve', 'mark', 'ben', 'will']
# print("The first 3 players are:")
# for player in players[:3]:
#     print(player.title())

# my_foods = ['falafel','pizza','burger','mushrooms','wraps','hotdogs']
# her_foods = my_foods[:]

# for foods in my_foods:
#     print(f"My fvourite foods include {foods.title()}")

# print("\nChristine's favourites are:")
# print(her_foods)

# my_foods.append('lasagne')
# her_foods.append('fish')
# print("\n")
# print(my_foods)
# print(her_foods)

### TUPLES ###

tup1 = (250, 350)
for bdt in tup1:
    print(bdt)

tup1 = (230, 200)
print("\nNew values:")
for bdt in tup1:
    print(bdt)
