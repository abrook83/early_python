# ### 6.1 Person ###

# xtine = {'age':'35', 'hair':'pink' ,'sex':'female', 'eyes':'brown'}
# print(xtine['age'])
# print(xtine['hair'].title())
# print(xtine['sex'].upper())
# print(xtine['eyes'].title())

# ### 6.2 Fave Numbers ###

# fnums = {
#     'christine':'11',
#     'aaron':'37',
#     'mum':'52',
#     'dad':'6',
#     'jared':'13'
# }
# num = fnums['christine']
# print(f"Christine's favourite number is {num}.")

# num = fnums['aaron']
# print(f"Aaron's favourite number is {num}.")

# num = fnums['mum']
# print(f"Mum's favourite number is {num}.")

# num = fnums['dad']
# print(f"Dads favourite number is {num}.")

# num = fnums['jared']
# print(f"Jared's favourite number is {num}.")

### 6.3 Glossary ###

gloss = {
    'variable':'a location storing a value',
    'list':'a series of strings in a particular order',
    'dictionary':'a repository of values stored against related keys',
    'string':'syntax stored in a variable',
    'print':'a command to display an output'
}

element = 'variable'
print(f"\n{element.title()}: {gloss['variable']}.")

element = 'list'
print(f"\n{element.title()}: {gloss['list']}.")

element = 'dictionary'
print(f"\n{element.title()}: {gloss['dictionary']}.")

element = 'string'
print(f"\n{element.title()}: {gloss['string']}.")

element = 'print'
print(f"\n{element.title()}: {gloss['print']}.\n")