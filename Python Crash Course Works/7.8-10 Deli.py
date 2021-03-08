# ### 7.8 Deli ###

# sandwich_orders = ['ham & cheese','vegemite','cheese','jaffle','pickle']
# finished_sandwiches = []

# while sandwich_orders:
#     curr_swich = sandwich_orders.pop()    
#     print(f"I have made a {curr_swich} sandwich for you.\n")

#     finished_sandwiches.append(curr_swich)

# print(sandwich_orders)
# print(finished_sandwiches)


# ### 7.9 No Pastrami ###

# sandwich_orders = ['ham & cheese','pastrami','vegemite','cheese','pastrami','jaffle','pastrami','pickle']
# finished_sandwiches = []

# print(f"Righto, so I've got orders for: ")
# for sanga in sandwich_orders:
#     print(f"- {sanga.title()}")

# if 'pastrami' in sandwich_orders:
#     print("\nSorry, we're out of pastrami!\n")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     curr_swich = sandwich_orders.pop()    
#     print(f"I have made a {curr_swich} sandwich for you.\n")

#     finished_sandwiches.append(curr_swich)

# print(sandwich_orders)
# print(finished_sandwiches)


### 7.10 Dream Vacation ###

locs = {}

poll_active = True

while poll_active:
    name = input("What is your name? ")
    loc = input("What is your dream holiday destination? ")

    locs[name] = loc            # Adds the key & value to the dictionary 'locs'

    again = input("Would you like to ask another person? y/n?: ")
    if again == 'n':
        poll_active = False
    
print("\n--- Poll complete! ---")
for k,v in locs.items():
    print(f"\n{k.title()} wants to go to {v.title()}.")


