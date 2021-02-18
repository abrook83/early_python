# def greet_user(uname):                    # the argument 'uname' is a handle for the input to the function....
#     """Displays a simple greeting"""      # ...It's what the input ('jesse' in this case) is referred to within the function!
#     print(f"Hello {uname.title()}!")

# greet_user('jesse')


# def describe_pet(animal_type, pet_name):
#     """ Display pet information """
#     print(f"I have a {animal_type},")
#     print(f"His name is {pet_name.title()}.")

# antype = input("What kind of pet do you have? ")
# pname = input("What is his name? ")

# describe_pet(antype,pname)


# def get_full_name(first, last, middle = ''):
#     """ Return a full name from the first & last provided """
#     if middle:
#         fullname = f"{first} {middle} {last}"
#     else:
#         fullname = f"{first} {last}"
#     return fullname.title()

# while True:
#     print("Please tell me your name, enter 'q' at any time to quit.")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Surname: ")
#     if l_name == 'q':
#         break

#     fullname = get_full_name(f_name, l_name)
#     print(f"Hello {fullname}!")



# def greet_users(names):
#     """ print a message to users in a list """
#     for name in names:
#         msg = f"Hello {name.title()}!"
#         print(msg)

# u_names = ['ashley','dave','steve','john']
# greet_users(u_names)            # apply the function 'greet_users' to the list 'u_names'


import printing_functions as pf

unprinted = ['phone case','t-shirt','undies']
printed = []

pf.print_models(unprinted, printed)
pf.display(printed)

# def make_pizza(size, *toppings):              # the * creates a tuple with the number of values input.
#     """ print the list of toppings requested """
#     print(f"\nMake a {size.upper()} pizza with the following topping(s): ")
#     for top in toppings:
#         print(f"\t- {top.title()}")

# make_pizza('L','ham','cheese','salami','olives')
# make_pizza('m','cheese')


# def build_profile(first, last, **user_info):                # ** cause the function to create an empty dictionary
#     """ Build a dictionary containing all info collected from a user """
#     user_info['first_name'] = first
#     user_info['last name'] = last
#     return user_info

# user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')

# print(user_profile)

