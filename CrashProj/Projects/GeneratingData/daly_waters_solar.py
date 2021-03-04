import csv
from logging import currentframe

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'CrashProj\Projects\data/the_csv_file_format\DalyWaters_2020\IDCJAC0016_014618_2020_Data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    # retrieve the dates and high temps from the file
    dates, exp_lvls = [], []      # empty list of dates & exposure level
    for row in reader:      # for each row in the opened & read file...
        current_date = datetime.strptime((f"{row[2]}-{row[4]}-{row[3]}"), '%Y-%d-%m')   # date from row 2, 4, 3
        try:
            exp = float(row[5])  # ...take the 5th column as an integer
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            exp_lvls.append(exp)  # add it to the list of highs

    # plot the high & low temps
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, exp_lvls, c='red', alpha=0.5)     # plot the highs, in red
    # ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)    # alpha controls a colour's transparency

    # format the plot
    ax.set_title("Daily Solar Exposure Levels\nDaly Waters, 2020", fontsize=20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()     # draws dates diagonally to prevent overlap
    ax.set_ylabel("Exposure Level", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# for index, column_header in enumerate(header_row):      # 'enumerate' returns each item in the list, as well as its index.
#     print(index, column_header)

# print(highs)