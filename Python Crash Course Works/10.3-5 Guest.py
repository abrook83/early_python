# ### 10.3, 10.4 Guest Book ###

# guests = 'userlist.txt'

# while True:
#     u_name = input("What is your name? ")
#     if u_name == 'q':
#         break
#     else:
#         with open(guests, 'a') as open_file:        # creates & opens an empty file if one doesn't exist
#             print(f"Hello {u_name.title()}, welcome to our exclusive club!")
#             open_file.write(f"{u_name.title()}\n")


### 10.5 Programming Poll ###

reasons = 'WhyILoveProgramming.txt'

while True:
    participant = input("Tell us why you like programming,\n(Enter 'q' to quit): ")
    if participant == 'q':
        break
    else:
        with open(reasons, 'a') as working_file:
            working_file.write(f"{participant}\n")
