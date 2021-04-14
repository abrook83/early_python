# '*' denotes an unlimited number of arguments...
def add(*nums):
    total = 0
    for num in nums:
        total += num
    print(f"Total = {total}")

add(3,2,4,6,2)

# '**' denotes an unlimited number of keyword arguments (or 'kwargs').
# kwargs are essentially passed in as a dictionary, so values are called by the keys.
def calc(n, **kwargs):
    """Pass in as many keyword arguments as liked. In this case, 'n' is the initial value,
    and will execute whichever arguments that are intput in the kwargs."""
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calc(2, add=3, multiply=5)


# class Car:

#     def __init__(self, **kwargs):
#         """In this code, the function looks for the parameters for 'make' and 'model'."""
#         self.make = kwargs["make"]
#         self.model = kwargs["model"]

# my_car = Car(model="Liberty", make="Subaru")
# print(my_car.model)

class Car:

    def __init__(self, **kwargs):
        """In this code, the function retrieves the parameters for 'make' and 'model',
        but returns 'None' if they are not there."""
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")

my_car = Car(make="Subaru", seats=5)
print(my_car.model)     # will return a 'None' as the model has not been provided