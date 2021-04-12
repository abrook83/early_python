### LIST COMPREHENSION ###

# # new_list = [new_item for item in list]
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)     # prints '2, 3, 4'

# adding an 'if' test at the end...
names = ['Dave', 'Jon', 'Peter', 'Gerald', 'Stavros', 'Glen']
# print(names)
short_names = [name for name in names if len(name) < 5]
print(short_names)

# print the longer (>5 letter) names in UPPERCASE
capit_names = [name.upper() for name in names if len(name) > 5]
print(capit_names)