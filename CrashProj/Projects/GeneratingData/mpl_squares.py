import matplotlib.pyplot as plt     # import the pyplot module, call it 'plt'
# print(plt.style.available)        # display plot types

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

print(max(y_values))

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# set the chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# set the size of tick labels
ax.tick_params(axis = 'both', labelsize = 14)

# set the tange for each axis
ax.axis([0, 5500, 0, 130000000000])

plt.show()      # opens the view and displays the plot