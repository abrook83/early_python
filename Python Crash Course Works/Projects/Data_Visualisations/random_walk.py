from random import choice       # 'choice' function in the 'random module...

class RandomWalk:
    """ A class to generate random walks """

    def __init__(self, num_points=5000):
        """ initialise attributes of a walk """
        self.num_points = num_points        # sets the default number of points in a walk to 5000

        # all walks start at (0,0)
        self.x_values = [0]     # lists holding the x & y values, beginning at 0,0
        self.y_values = [0]

    def get_step(self):
        """ create each step's direction & distance """
        # decide which direction to go and how far
        direction = choice([1, -1])              # 'choice' selects the y & x direction and distance randomly from
        distance = choice([0, 1, 2, 3, 4])       # the provided arguments.
        step = direction * distance          # multiply the direction by the disatnce to determine where we're going.
        return step
    
    def fill_walk(self):
        """ calculate all the points in the walk """
        # to keep taking steps up to the desired length (in 'num_points')
        while len(self.x_values) < self.num_points:         # sets the length of the walk from the self.num_points
            x_step = self.get_step()
            y_step = self.get_step()
            
            # reject moves that go nowhere
            if y_step == 0 and x_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1] + x_step          # takes the last value in the list([-1]) and adds the new step value
            y = self.y_values[-1] + y_step          # to identify where the current point is.

            self.x_values.append(x)         # add the current values to the list of values.
            self.y_values.append(y)