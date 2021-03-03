### 15.3 Molecular Motion ###

import matplotlib.pyplot as plt
# print(plt.__version__)
from random_walk import RandomWalk

# make new walks as program runs
while True:
    # make a random walk
    rw = RandomWalk()
    rw.fill_walk()      # create a random walk (by calling 'fill_walk') and store it in 'rw'

    # plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(20, 15))    # 'figsize' gives the plotting window size in inches
    point_numbers = range(rw.num_points)        # create a range from 'num_points' in RandomWalk
    ax.plot(rw.x_values, rw.y_values, 
    c='Blue', linewidth=1)  # feeds the data to the 'scatter' function, 's' is the dot size.
    
    # emphasise the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)       # at 0,0, where the walk starts, make first point green and larger
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='Red', edgecolors='none', s=100)    # make the last point in the list of values blue and larger
       
    # remove the axes
    ax.get_xaxis().set_visible(False)   # use 'ax.get_x/yaxis' to modify the axes. 
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Create another random walk? y/n?: ")
    if keep_running == 'n':
        break
