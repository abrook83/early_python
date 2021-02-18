### 9.5 Number Served ###

class Restaurant:
    """ Gives name & cuisine details of a restaurant """
    def __init__(self, restaurant_name, cuisine_type):
        """ initialise name & cuisine type """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ provides the details of a restaurant """
        print(f"This restaurant is named {self.restaurant_name},")
        print(f"which specialises in {self.cuisine_type}.")

    def open_restaurant(self):
        """ indicates whether the restaurant is open """
        print(f"{self.restaurant_name} is currently open.")

    def set_number_served(self):
        """ sets how many customers have been served """
        print(f"{self.number_served} people have been served.")

restaurant = Restaurant("Luigi's", "Pizza")

restaurant.describe_restaurant()
restaurant.set_number_served()
restaurant.number_served = 15
restaurant.set_number_served()






















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