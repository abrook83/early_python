import pandas

squirrel_data = pandas.read_csv("100Days\day25_CSVdata/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(len(squirrel_data["Primary Fur Color"]))
gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Color Count": [gray_count, cinnamon_count, black_count]
}

dframe = pandas.DataFrame(data_dict)
dframe.to_csv("100Days\day25_CSVdata\Squirrel Color Count.csv")