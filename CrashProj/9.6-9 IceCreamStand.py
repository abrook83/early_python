# ### 9.6 Ice Cream Stand ###

#     ### (9.1 Restaurant) ###

# class Restaurant:
#     """ Gives name & cuisine details of a restaurant """
#     def __init__(self, restaurant_name, cuisine_type):
#         """ initialise name & cuisine type """
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """ provides the details of a restaurant """
#         print(f"This restaurant is named {self.restaurant_name},")
#         print(f"which specialises in {self.cuisine_type} food.")

#     def open_restaurant(self):
#         """ indicates whether the restaurant is open """
#         print(f"{self.restaurant_name} is currently open.")

# # my_rest = Restaurant("Luigi's", "Italian")

# # my_rest.describe_restaurant()
# # my_rest.open_restaurant()

# # print("\n")

# # your_rest = Restaurant("Reggie's", "Pizza")

# # your_rest.describe_restaurant()
# # your_rest.open_restaurant()

# # print("\n")

# # mums_rest = Restaurant("WacArnold's", "deep-fried shit")

# # mums_rest.describe_restaurant()
# # mums_rest.open_restaurant()


# class IceCreamstand(Restaurant):
#     """ Creates different attributes for an ice cream stand as opposed to a restaurant """
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavours = []
 
#     def ice_cream_flavours(self):
#         """ display the most popular flavours """
#         print("Our biggest sellers are:")
#         for flavour in self.flavours:
#             print(f"- {flavour.title()}")

# my_stand = IceCreamstand("Big Mama's", "Ice Cream")
# my_stand.flavours = ['vanilla','choc','hokey pokey']

# my_stand.describe_restaurant()
# my_stand.ice_cream_flavours()


### 9.7 Admin ###
   
    ### (9.3 Users) ###

class User:
    def __init__(self, first_name, last_name, age, middle_name, email_addr, username):
        """ creates a user profile with required attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.middle_name = middle_name
        self.email_addr = email_addr
        self.username = username

    def describe_user(self):
        """ prints a desciptive user profile """
        print(f"Username: {self.username}")
        print(f"Full Name: {self.first_name.title()} {self.middle_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"email: {self.email_addr}")

    def greet_user(self):
        """ provides a greeting message to a user """
        print(f"\nHello {self.first_name.title()}, welcome!\n")

class Admin(User):
    """ creates a subclass for admin use with special privileges """
    def __init__(self, first_name, last_name, age, middle_name, email_addr, username):
        """ initialise the admin """
        super().__init__(first_name, last_name, age, middle_name, email_addr, username)
        self.privileges = []            # adds the attribute 'privileges as an empty list

    def show_privileges(self):
        """ display the list of privileges available to admin """
        print("\nThe following privileges are available to admin users:")
        for priv in self.privileges:
            print(f"\t- {priv}")


# dave = User('Dave','Johnson','32','George','dave@gmail.com','dgj32')
# User.describe_user(dave)
# User.greet_user(dave)

# glen = User('glen','davies','56','michael','glen32@hotmail.com','glenneth23')
# User.describe_user(glen)
# User.greet_user(glen)

admin = Admin('wendy','jones','63','elizabeth','librarian@school.com','admin123',)
Admin.describe_user(admin)

admin.privileges = [
    'reset passwords',
    'deduct from your pay when your books are overdue',
    'see your entire academic history!',
]
Admin.show_privileges(admin)