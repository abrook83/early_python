### 9.1 Restaurant ###

class Restaurant:
    """ Gives name & cuisine details of a restaurant """
    def __init__(self, restaurant_name, cuisine_type):
        """ initialise name & cuisine type """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ provides the details of a restaurant """
        print(f"This restaurant is named {self.restaurant_name},")
        print(f"which specialises in {self.cuisine_type} food.")

    def open_restaurant(self):
        """ indicates whether the restaurant is open """
        print(f"{self.restaurant_name} is currently open.")

my_rest = Restaurant("Luigi's", "Italian")

my_rest.describe_restaurant()
my_rest.open_restaurant()

print("\n")

your_rest = Restaurant("Reggie's", "Pizza")

your_rest.describe_restaurant()
your_rest.open_restaurant()

print("\n")

mums_rest = Restaurant("WacArnold's", "deep-fried shit")

mums_rest.describe_restaurant()
mums_rest.open_restaurant()