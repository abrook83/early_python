## 6.4 Glossary 2 ###
print("6.4 Glossary 2")

gloss = {
    'variable':'a location storing a value',
    'list':'a series of strings in a particular order',
    'dictionary':'a repository of values stored against related keys',
    'string':'syntax stored in a variable',
    'print':'a command to display an output',
    'set':'a collection of items stored in no particular order',
    'tuple':'an unchangable list',
    'sort':'a command used to sort variables alphabetically',
}

for k, v in gloss.items():
    print(f"\n'{k.title()}' is {v}.")

## 6.5 Rivers ###
print("\n6.5 Rivers")

rivers = {
    'Nile':'Egypt',
    'Seine':'France',
    'Amstel':'The Netherlands',
    }

for river, country in rivers.items():
    print(f"\nThe {river} runs through {country}.")

for river in sorted(rivers):
    print(f"\n{river}")

for country in sorted(rivers.values()):
    print(f"\n{country}")

## 6.6 Polling ###
print("\n6.6 Polling")

fave_langs = {
    'steve':'python',
    'bill':'C',
    'bob':'java',
    'terry':'ruby',
}

suggs = ('steve','chris','bill','wendy','jake')

for name in suggs:
    if name in fave_langs:
        print(f"\nHey {name.title()}, thanks for taking our poll!")
    elif name not in fave_langs:
        print(f"\nHey {name.title()}, how about taking our poll!")
print("\n")