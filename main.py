# Data is from NYC Open Data.
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_count = data.groupby(["Primary Fur Color"]).size()
squirrel_count_df = pandas.DataFrame(
    # Sort prior to generating an index to match the expected answer
    squirrel_count.sort_values(ascending=False)
).reset_index()

# Rename some things to match expected answer
squirrel_count_df = squirrel_count_df.rename(columns={"Primary Fur Color": "Fur Color", 0: "Count"})
squirrel_count_df["Fur Color"] = squirrel_count_df["Fur Color"].str.lower()
squirrel_count_df.loc[squirrel_count_df["Fur Color"] == "cinnamon", "Fur Color"] = "red"
squirrel_count_df.loc[squirrel_count_df["Fur Color"] == "gray", "Fur Color"] = "grey"

squirrel_count_df.to_csv("squirrel_count_via_groupby.csv")

# This approach matched the instructors csv exactly.
# squirrel_color_count = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [
#         sum(data["Primary Fur Color"] == "Gray"),
#         sum(data["Primary Fur Color"] == "Cinnamon"),
#         sum(data["Primary Fur Color"] == "Black")
#     ]
# }
#
# squirrel_data = pandas.DataFrame(squirrel_color_count)
# squirrel_data.to_csv("squirrel_data.csv")
