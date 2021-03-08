from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# create 2 D6 (six-sided dice)
die_1 = Die()     # create an instance of Die, with the default 6 sides...
die_2 = Die()     # make it a 10-sided dice to see the difference
die_3 = Die()

# make a few rolls, store the outomces in a list
results = []
for roll_num in range(100000):    # number of rolls
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# analyse the results
frequencies = []        # empty list
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides      # adds the max. results of both die
for value in range(3, max_result+1):     # add 1 to range so top number is included
    frequency = results.count(value)        # count how many times each value(above) is generated
    frequencies.append(frequency)

# visualise the results
x_values = list(range(3, max_result+1))      # create x-axis values in a list starting at 1, ending at the number of sides
data = [Bar(x=x_values, y=frequencies)]     # calls Plotly's class 'Bar' and identifies its x & y repositories.

x_axis_config = {'title': 'Result', 'dtick': 1}     # set the titles of both axes, 'dtick' controls the spacing between ticks on the x-axis ('1' labels each tick).
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling 3 dice 1000 times',   # sets the layout configuration for the chart
xaxis=x_axis_config, yaxis=y_axis_config)           # imput the dictionaries (of the titles) into the layout.
offline.plot({'data': data, 'layout': my_layout}, filename='d6 X 3.html')   # generates the plot from the provided objuects; gives it a name

print(frequencies)