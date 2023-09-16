# Data is from NYC Open Data.
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
import pandas


def main() -> pandas.DataFrame:
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

    # My original approach. While this technically worked, my csv did not look
    # the same as the instructors.
    # squirrel_count = data.groupby(["Primary Fur Color"]).size()
    # squirrel_count_df = pandas.DataFrame(squirrel_count).reset_index()
    # squirrel_count_df.to_csv("squirrel_count_via_groupby.csv", header=False)

    # This approach matched the instructors csv exactly.
    squirrel_color_count = {
        "Fur Color": ["grey", "red", "black"],
        "Count": [
            sum(data["Primary Fur Color"] == "Gray"),
            sum(data["Primary Fur Color"] == "Cinnamon"),
            sum(data["Primary Fur Color"] == "Black")
        ]
    }

    return pandas.DataFrame(squirrel_color_count)


if __name__ == "__main__":
    data = main()
    data.to_csv("squirrel_data.csv")
