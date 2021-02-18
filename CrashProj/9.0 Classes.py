### dog.py

# class Dog:                  # create class names with capital letters to distinguish the difference
#     """ A simple model of a dog """
#                                                     # a function that's part of a class is called a method
#     def __init__(self, name, age):                        # '__init__' is a 'method' run whenever we create a new instance in the class
#         """ initialize name & age attributes """
#         self.name = name
#         self.age = age

#     def sit(self):
#         """ simulate a dog sitting in response to a command """
#         print(f"{self.name.title()} is now sitting.")

#     def roll_over(self):
#         """ simulate a command for the dog to roll over """
#         print(f"{self.name.title()} is rolling over!")

# my_dog = Dog('willie', 6)               # inputs 'willie' and '6' into Class 'Dog'
# # from this, the '__init__' method in the class 'Dog' creates an instance of a dog with the name 'willie' and age '6'.

# print(f"My dog's name is {my_dog.name.title()},")               # access the attribute in the instance with '.name...'
# print(f"My dog is {my_dog.age} years old.")                      # ... or '.age'

# my_dog.sit()            # with input 'willie', run's the method to 'sit'
# my_dog.roll_over()

# print("\n")
# your_dog = Dog('Benji', 2)

# print(f"Your dog's name is {your_dog.name.title()},")
# print(f"Your dog is {your_dog.age} years old.")

# your_dog.sit()
# your_dog.roll_over()


### car.py

class Car:
    """ a representation of a car """

    def __init__(self, make, model, year):
        """ initialise attributes to describe the car """
        self.make = make            # the object (self)'s attribute (make) becomes the argument "make".
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ return a neatly formatted descriptive name """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ print a statement showing the cars mileage """
        print(f"This car has travelled {self.odometer_reading} miles.... highway miles though, they're the good ones")

    def update_odometer(self, mileage):
        """ update mew milage to the odometer reading """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage         # creates an attribute 'mileage' to be input into 'self.odometer_reading()' when called
        else:
            print("Ferris! The miles aren't comin' off!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
                                    # defining the child class
class ElectricCar(Car):             # the parent class 'Car' must be part of the current file, and above the child class ^^
    """ represents aspects of a car, specific to electric cars """
    
    def __init__(self, make, model, year):
        """ Initiatlise attributes of the parent class """
        super().__init__(make, model, year)         # 'super' function allows you to call a method from a parent class...
                                                    # ...and gives all the attributes from that method.
        self.battery_size = 75

    def describe_battery(self):             # created in the child class, will not be reflected in the parent class 'Car'
        """ print a statement giving the battery size """
        print(f"Battery size: {self.battery_size}kWh.")

my_tesla = ElectricCar('tesla','model s','2019')            
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()