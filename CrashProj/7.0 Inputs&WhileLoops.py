# prompt = "First, we'll need to know your name,"
# prompt += "\nPlease enter it here: "

# inp = input(prompt)
# print(f"\nHello {inp.title()},")

# age = input("And how old are you? ")
# age = int(age)          # Convert itself to integer

# if age >= 18:
#     print(f"Lucky you {inp.title()}! You're old enough to vote!")
# else:
#     gap = (21 - age)
#     print(f"Ah, too bad {inp.title()}, no voting for you, come back in {gap} years.")

# if age % 2 == 0:
#     print("Lucky you for have an even age though, you've won a prize!")
# else: print("Get outta here oddball!")


### WHILE LOOPS ###

# curr_num = 1
# while curr_num <= 5:
#     print(curr_num)
#     curr_num += 1           # add 1 to itself


# inp = "\nTell me something I don't know so I can say it back to you: "
# inp += "\nEnter 'quit' when you want to leave: "

# active = True
# while active:
#     mess = input(inp)              # ...the message is the input
    
#     if mess == 'quit':          # if the message is not 'quit'
#         active = False
#     else:        
#         print(f"\n{mess}")      # print the message


# prompt = "\nWhat's a city you've been to? "
# prompt += "\nEnter 'quit' when you want to leave. "

# while True:         # a "While True" loop runs until it reaches a 'break' statement.
#     city = input(prompt)

#     if city == 'quit':
#         break       # 'break' ends the while loop
#     else:
#         print(f"\nOh man, I'd love to go to {city.title()}!")


# curr_num = 0
# while curr_num < 10:
#     curr_num += 1
#     if curr_num % 2 == 0:            # if the curr_num is an even number....
#         continue            # restart the loop from here

#     print(curr_num)



# u_user = ['Steve','Dan','Bob']          # list of unconfirmed users
# c_user = []                             # empty list where they'll be deposited

# while u_user:           # runs as long as the list 'u_user' is not empty
#     curr_user = u_user.pop()

#     print(f"Verifying {curr_user.title()}")
#     c_user.append(curr_user)

# print("\nThe following users have beeon confirmed: ")
# for c_use in c_user:
#     print(c_use.title())


# pets = ['dog','cat','ferret','snake','cat','mouse','cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print("Righto, all the cats are gone, now there's...")
# for pet in pets:
#     print(pet.title())


responses = {}

poll_active = True      # flag indicating polling is active

while poll_active:
    name = input("Please enter your name: ")
    resp = input("Which mountain would you like to climb one day? ")

    responses[name] = resp

    rep = input("Would you like to ask another person? y/n?: ")
    if rep == 'n':
        poll_active = False

print("Polling complete. Results are as follows:\n")
for k, v in responses.items():
    print(f"\n{k.title()} would like to climb {v.title()} one day.")


