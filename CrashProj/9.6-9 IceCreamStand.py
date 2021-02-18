### 9.6 Ice Cream Stand ###

### (9.1 Restaurant) ###

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

### I've got no idea at the moment, I'm gunna have to come back to this one! ###

class IceCreamstand(Restaurant):
    """ Creates different attributes for an ice cream stand as opposed to a restaurant """
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def ice_cream_flavours(self):
        """ display the most popular flavours """
        print("Our biggest sellers are:")
        for flavour in self.flavours:
            print(f"- {flavour.title()}")

my_stand = IceCreamstand("Big Mama's", "Ice Cream")
my_stand.flavours = ['vanilla','choc','hokey pokey']

my_stand.describe_restaurant()
my_stand.ice_cream_flavours()
        
