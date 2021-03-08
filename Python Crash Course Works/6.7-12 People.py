# ### 6.7 People ###

# xtine = {'name':'christine','age':'35', 'hair':'pink' ,'sex':'female', 'eyes':'brown'}
# aaron = {'name':'aaron','age':'37', 'hair':'blonde' ,'sex':'male', 'eyes':'blue'}
# hazel = {'name':'hazel','age':'7', 'hair':'tortoise' ,'sex':'female', 'eyes':'mustard'}

# people = [xtine, aaron, hazel]

# for person in people:
#     name = person['name']
#     age = person['age']
#     hair = person['hair']
#     sex = person['sex']
#     eyes = person['eyes']

#     print(f"{name.title()}, aged {age}, with {hair}-coloured hair & {eyes} eyes, is {sex}.\n")


### 6.8 Pets ###

# pets = []

# pet = {
#     'name':'daisy',
#     'animal':'dog',
#     'colour':'white',
#     'age':'4',
#     'good?':'yes'
# }
# pets.append(pet)

# pet = {
#     'name':'chop',
#     'animal':'dog',
#     'colour':'black',
#     'age':'7',
#     'good boy?':'no'
# }
# pets.append(pet)

# pet = {
#     'name':'ace',
#     'animal':'dog',
#     'colour':'brown',
#     'age':'2',
#     'good boy?':'yes'
# }    
# pets.append(pet)

# for pet in pets:
#     print(f"{pet['name'].title()} is a {pet['age']} y.o. {pet['colour']} {pet['animal']}")


# ### 6.9 Favourite Places ###

# favourite_places = {
#     'rocket':['tassie','mawson','home'],
#     'mum':['launceston','tannum','perth'],
#     'chris':['rockingham','willis','lady garden'],
# }

# for k, v in favourite_places.items():    
#     print(f"\n{k.title()}'s favourite places are -")
#     for places in v:
#         print(f"- {places.title()}")


# ### 6.10 Favourite Numbers ###

# fnums = {
#     'christine':['11','23'],            # lists within a dictionary
#     'aaron':['37','17'],
#     'mum':['52','7'],
#     'dad':['6','42'],
#     'jared':['13','86'],
# }

# for k,v in fnums.items():
#     print(f"\n{k.title()}'s favourite numbers are:")
#     for num in v:                   # for each 'num' in the variables list....
#         print(f"\t{num}")           # ...print that number (num)


### 6.11 Cities ###

cities = {
    'brisbane':{'country':'Australia','pop':'2000000','fact':'home to many wild turkeys'},
    'dubai':{'country':'UAE','pop':'3000000','fact':'a holder of hundreds of Guinness World Records'},
    'hamburg':{'country':'Germany','pop':'2000000','fact':'a major European port'},
}

for city,info in cities.items():
    print(f"Things I know about {city.title()}:")
    print(f"{city.title()}'s population is around {info['pop'].title()}, and it is {info['fact']}.\n")


