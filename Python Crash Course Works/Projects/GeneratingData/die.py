from random import randint

class Die:
    """ a class representing a single dice """

    def __init__(self, num_sides=6):        # default value for number of sides is 6, unless changed
        """ assume a six-sided dice """
        self.num_sides = num_sides

    def roll(self):
        """ return a number between 1 and the number of sides """
        return randint(1, self.num_sides)