# with open("100Days\day25_CSVdata\weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# print(data)

import csv
import pandas

# with open("100Days\day25_CSVdata\weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

### Now do the same using pandas.... ###

data = pandas.read_csv("100Days\day25_CSVdata\weather_data.csv")
print(data["temp"])