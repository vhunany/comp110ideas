from data_utils import read_csv_rows, columnar, column_values
from DataFrame import DataFrame

""" Use read_csv_rows to import both files of data. """
early_data: list[dict[str, str]] = read_csv_rows("data/baby_names_2012_2017.csv")
later_data: list[dict[str, str]] = read_csv_rows("data/baby_names_2018_2021.csv")

""" Test column_values function. """
names_early_data = column_values(early_data, "name")
print(len(names_early_data))

""" Use columnar to reformat both data sets. """
columnar_early_data: dict[str, list[str]] = columnar(early_data)
print(columnar_early_data.keys())
columnar_later_data: dict[str, list[str]] = columnar(later_data)

""" Create DataFrame objects with each set of data. """
df_early: DataFrame = DataFrame(columnar_early_data)
df_later: DataFrame = DataFrame(columnar_later_data)

""" Use tabulate *method* to view data as a table. """
#  df_early.tabulate()  # <- To prevent large output, comment out after testing.

""" Use __add__ magic method to combine into one data set. """
df: DataFrame = df_early + df_later
# df.tabulate()  # <- To prevent large output, comment out after testing.

""" Use head method to access the first 10 entries of the data frame. """
first_ten: DataFrame = df.head(10)
# first_ten.tabulate()

""" Use select method to access only 'name' and 'count' columns. """
name_and_count: DataFrame = df.head(10).select(["name", "count"])
# name_and_count.tabulate()

""" Use filter_by_col_value to filter out only people born in 2020. """
names_2020: DataFrame = df.filter_by_col_value("year", "2020")
#names_2020.tabulate()

""" From the people born in 2020, get top 10 most popular names. """
top_10: DataFrame = names_2020.filter_by_rank("count", 10)
# top_10.tabulate()
