import csv

filename = 'CrashProj\Projects\data\sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)       # next function returns the next file in the line (first in this case)
    print(header_row)
