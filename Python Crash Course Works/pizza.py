### Create a pizza order ###

def make_pizza(size, *toppings):              # the * creates a tuple with the number of values input.
    """ print the list of toppings requested """
    print(f"\nMake a {size.upper()} pizza with the following topping(s): ")
    for top in toppings:
        print(f"\t- {top.title()}")