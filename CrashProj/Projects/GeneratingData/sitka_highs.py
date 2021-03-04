import csv
from logging import currentframe

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'CrashProj\Projects\data/the_csv_file_format\data\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)          # the csv's reader function, passed the opened file (f)
    header_row = next(reader)       # 'next' function returns the next file in the line (first in this case)
    # print(header_row)
    
    # retrieve the dates and high temps from the file
    dates, highs, lows = [], [], []      # empty list of highs and dates
    for row in reader:      # for each row in the opened & read file...
        current_date = datetime.strptime(row[2], '%Y-%m-%d')        # date from row 2
        high = int(row[5])  # ...take the 5th column as an integer
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)  # add it to the list of highs
        lows.append(low)

    # plot the high & low temps
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')     # plot the highs, in red
    ax.plot(dates, lows, c='blue')     # plot the lows, in blue

    # format the plot
    ax.set_title("Daily high & Low Temps 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()     # draws dates diagonally to prevent overlap
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# for index, column_header in enumerate(header_row):      # 'enumerate' returns each item in the list, as well as its index.
#     print(index, column_header)

# print(highs)