# ### 9.5 Number Served ###

# class Restaurant:
#     """ Gives name & cuisine details of a restaurant """
#     def __init__(self, restaurant_name, cuisine_type):
#         """ initialise name & cuisine type """
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """ provides the details of a restaurant """
#         print(f"This restaurant is named {self.restaurant_name},")
#         print(f"which specialises in {self.cuisine_type}.")

#     def open_restaurant(self):
#         """ indicates whether the restaurant is open """
#         print(f"{self.restaurant_name} is currently open.")

#     def set_number_served(self, number_served):
#         """ sets how many customers have been served """
#         self.number_served = number_served
#         print(f"{self.number_served} people have been served so far.")

#     def increment_number_served(self, additional_served):
#         """ adds to the total of people served """
#         self.number_served += additional_served

# restaurant = Restaurant("Luigi's", "Pizza")

# restaurant.describe_restaurant()
# restaurant.set_number_served(0)
# restaurant.set_number_served(15)

# restaurant.increment_number_served(50)
# print(f"Now {restaurant.number_served} people have been served.")



### 9.5 Login Attempts ###

class User:
    def __init__(self, first_name, last_name, age, middle_name, email_addr, username):
        """ creates a user profile with required attributes """
        self.first_name = first_name        # set an object's (init) first_name to the attribute `"first_name"
        self.last_name = last_name
        self.age = age
        self.middle_name = middle_name
        self.email_addr = email_addr
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        """ prints a desciptive user profile """
        print(f"Username: {self.username}")
        print(f"Full Name: {self.first_name.title()} {self.middle_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"email: {self.email_addr}")

    def greet_user(self):
        """ provides a greeting message to a user """
        print(f"\nHello {self.first_name.title()}, welcome!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """ resets the login attempts count """
        self.login_attempts = 0
        print("Login count reset")

dave = User('Dave','Johnson','32','George','dave@gmail.com','dgj32')         # create a new object named 'dave' with the class 'User'
dave.describe_user()
dave.greet_user()
dave.increment_login_attempts()
dave.increment_login_attempts()
dave.increment_login_attempts()
print(f"Login attempts: {dave.login_attempts}")

dave.reset_login_attempts()
print(f"Login attempts: {dave.login_attempts}")

# glen = User('glen','davies','56','michael','glen32@hotmail.com','glenneth23')