# ### 9.1 Restaurant ###

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

# my_rest = Restaurant("Luigi's", "Italian")

# my_rest.describe_restaurant()
# my_rest.open_restaurant()

# print("\n")

# your_rest = Restaurant("Reggie's", "Pizza")

# your_rest.describe_restaurant()
# your_rest.open_restaurant()

# print("\n")

# mums_rest = Restaurant("WacArnold's", "deep-fried shit")

# mums_rest.describe_restaurant()
# mums_rest.open_restaurant()


### 9.3 Users ###

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


dave = User('Dave','Johnson','32','George','dave@gmail.com','dgj32')
User.describe_user(dave)
User.greet_user(dave)

glen = User('glen','davies','56','michael','glen32@hotmail.com','glenneth23')
User.describe_user(glen)
User.greet_user(glen)
