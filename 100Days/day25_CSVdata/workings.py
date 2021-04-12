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
# print(type(data))       # the whole data set is a 'dataframe'
# print(type(data["temp"]))   # the column is a 'series'

""" table = dataframe, column = series """

# create dictionary 'data_dict' from the dataframe
data_dict = data.to_dict()
# print(data_dict)

""""Pandas takes the first value as the name of a column's values, hence is addressable via this first value."""

# # temp_list = data["temp"].to_list()
# # print(temp_list)

# # print(data["temp"].max())

# # Get data from columns - 
# """Both below lines produce the same output, values callable by their first value."""
# # print(data["condition"])
# # print(data.condition)

# Get data from rows -
"""From the dataframe 'data', removes the data string where the temp is the maximum.
'data' is the dataframe
'data.temp' in the column
'data.temp.max()' is the value"""
print(data[data.temp == data.temp.max()])

# monday = data[data.day =="Monday"]
# mon_temp = int(monday.temp)
# print((mon_temp * 1.8) + 32)
