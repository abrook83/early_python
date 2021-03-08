### 8.12 Sandwiches ###

# def make_swich(*fillings):
#     """ create a list of fillings to go into a sandwich """
#     print("Making a sandwich with the following:\n")
#     for fill in fillings:
#         print(f"\t- {fill.title()}")

# make_swich('ham','cheese','tomato','pepper')


### 8.13 User Profile ###

# def build_profile(first, last, **user_info):                # ** cause the function to create an empty dictionary
#     """ Build a dictionary containing all info collected from a user """
#     user_info['first_name'] = first
#     user_info['last name'] = last
#     return user_info

# user_profile = build_profile('aaron','brook',location = 'dubai',field = 'all')

# print(user_profile)


### 8.14 Cars ###

def car_info(make, model, **add_info):
    """ create a dictionary on car information """
    add_info['car make'] = make.title()
    add_info['car model'] = model.title()
    return add_info

car_prof = car_info('subaru','outback', colour = 'blue', tow_pkg = True)

print(car_prof)


