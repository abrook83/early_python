### Dictionaries ###

# create the dictionary
# alien = {'Colour':'green', 'points':'10'}
# print(alien['Colour'])

# print(f"Congrats, you scored {alien['points']} points!")

# add elements to the dictionary
# alien['X pos'] = 1
# alien['Y pos'] = 25

# print(f"The alien was at {alien['X pos']} & {alien['Y pos']} when you shot him!")
# print(alien)

# change a key's value
# alien['Colour'] = 'yellow'
# print(f"The alien's colour has now changed to {alien['Colour']}")
# print(alien)

# alien['speed'] = 'medium'
# print(f"Original X position: {alien['X pos']}")
# if alien['speed'] == 'slow':
#     x_add = 1
# elif alien['speed'] == 'medium':
#     x_add = 2
# else:
#     x_add = 3

# alien['X pos'] = alien['X pos'] + x_add
# print(f"The alien is now at X = {alien['X pos']}")

# print(alien)
# del alien['points']
# print(alien)

# point_val = alien.get('points','key unassigned')
# print(point_val)


### Languages ###

# #create a long dictionary over many lines
# fave_langs = {
#     'steve':'python',
#     'bill':'C',
#     'bob':'java',
#     'terry':'ruby',
# }

# for name, lang in fave_langs.items():
#     print(f"{name.title()}'s favourite language is {lang.title()}.\n")
# # lang = fave_langs['steve'].title()
# # print(f"Steve's favourite language is {lang}!")

### Looping through dictionaries ###

# user = {
#     'uname':'chooka',
#     'first name':'aaron',
#     'second name':'brook',
# }
# ### Keys AND Values ###

# for k, v in user.items():         # loops through BOTH keys & values
#     print(f"\n{k}: {v.title()}")
                                        
# ### Keys ONLY ###

# for k in sorted(user.keys()):           # Note: loops through keys by default. So '.keys()' not essential.
#     print(f"\nField: {k.title()}")      # 'sorted(__) to sort alphabetically

# ### Values ONLY ###

# for val in sorted(user.values()):
#     print(f"\nInput: {val.title()}")

# #create a long dictionary over many lines
# fave_langs = {
#     'steve':'python',
#     'bill':'C',
#     'bob':'java',
#     'terry':'ruby',
# }

# friends = []
# for name, lang in fave_langs.items():
#     print(f"{name.title()}'s favourite language is {lang.title()}.\n")

#     if name not in friends:
#         friends.append(name.title())
# print(friends)

# lang = fave_langs['steve'].title()
# print(f"Steve's favourite language is {lang}!")

### NESTING ###

# alien_0 = {'colour':'green','points':'5'}
# alien_1 = {'colour':'yellow','points':'10'}
# alien_2 = {'colour':'red','points':'15'}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# aliens = []

# for alien_num in range(30):
#     new_alien = {'colour':'green','points':'5','speed':'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['colour'] == 'green':
#         alien['colour'] = 'yellow'
#         alien['points'] = '10'
#         alien['speed'] = 'medium'

# for alien in aliens[:5]:
#     print(alien)

# print("...")

# print(f"\nThe total number of aliens is {len(aliens)}")


# pizza = {
#     'crust':'thick',
#     'toppings':['ham, cheese, pineapple'],
# }

# print(f"You ordered a {pizza['crust'].title()}-based pizza,")

# for tops in pizza['toppings']:
#     print(f"With toppings of: {tops.title()}")



# #create a long dictionary over many lines
# fave_langs = {
#     'steve':['python','c'],
#     'bill':['c'],
#     'bob':['java','go'],
#     'terry':['ruby','pascal'],
# }

# for key, vals in fave_langs.items():
#     if len(vals) > 1:
#         print(f"\n{key.title()} likes these languages:")
#         for lang in vals:
#             print(f"\t{lang.title()}")
#     elif len(vals) == 1:
#         print(f"\n{key.title()} likes:")
#         for lang in vals:
#             print(f"\t{lang.title()}")


# ### Dictionary within a dictionary ###
# users = {
#     'aeinstein':{
#         'fname':'albert',
#         'lname':'einstein',
#         'loc':'princeton',
#         },
    
#     'mcurie':{
#         'fname':'marie',
#         'lname':'curie',
#         'loc':'paris',
#         },
#     }

# for username, info in users.items():                        # 'username' = outer dictionary, 'info' - inner dictionary
#     print(f"Username: {username}")
#     full_name = f"{info['fname']} {info['lname']}"          # 'info' accesses the inner dictionary
#     location  = info['loc']

#     print(f"\tFull Name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}\n")


