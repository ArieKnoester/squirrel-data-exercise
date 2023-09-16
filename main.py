# Data is from NYC Open Data.
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_count = data.groupby(["Primary Fur Color"]).size()

squirrel_data = pandas.DataFrame({
    "Fur Color": ["grey", "red", "black"],
    "Count": [
        squirrel_count[input_fur_color]
        for input_fur_color in ["Gray", "Cinnamon", "Black"]
    ]
})

squirrel_data.to_csv("squirrel_data.csv")
