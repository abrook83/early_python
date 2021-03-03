from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# create a D6 (six-sided dice)
die = Die()     # create an instance of Die, with the default 6 sides...

# make a few rolls, store the outomces in a list
results = []
for roll_num in range(1000):    # number of rolls
    result = die.roll()
    results.append(result)

# analyse the results
frequencies = []        # empty list
for value in range(1, die.num_sides+1):     # add 1 to range so top number is included
    frequency = results.count(value)        # count how many times each value(above) is generated
    frequencies.append(frequency)

# visualise the results
x_values = list(range(1, die.num_sides+1))      # create x-axis values in a list starting at 1, ending at the number of sides
data = [Bar(x=x_values, y=frequencies)]     # calls Plotly's class 'Bar' and identifies its x & y repositories.

x_axis_config = {'title': 'Result'}     # set the titles of both axes
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling D6 dice 1000 times',   # sets the layout configuration for the chart
xaxis=x_axis_config, yaxis=y_axis_config)           # imput the dictionaries (of the titles) into the layout.
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')   # generates the plot from the provided objuects; gives it a name

print(frequencies)