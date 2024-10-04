from __future__ import annotations
from tabulate import tabulate  # type: ignore (this just suppresses the warning.)


class DataFrame:

    data: dict[str, list[str]]

    def __init__(self, data: dict[str, list[str]]):
        self.data = data

    def tabulate(self) -> None:
        print(tabulate(self.data, headers=list(self.data.keys()), tablefmt="grid"))

    def head(self, rows: int) -> DataFrame:
        """Function narrows down the table to n rows of data per column."""
        result_dict: dict[str, list[str]] = {}
        for key in self.data:
            n_vals: list[str] = []
            if rows > len(self.data[key]):
                rows = len(self.data[key])
            for idx in range(0, rows):
                n_vals.append(self.data[key][idx])
            result_dict[key] = n_vals
        return DataFrame(result_dict)

    def __add__(self, other: DataFrame) -> DataFrame:
        """Extend a data set by combining two."""
        # Assert both data frames have matching keys
        assert (
            self.data.keys() == other.data.keys()
        ), "Both data frames should have same key values."
        # Create new table
        new_table: dict[str, list[str]] = {}
        # Copy over data from table 1
        for key in self.data:
            new_table[key] = self.data[key]
        # Copy over data from table 2
        for key in new_table:
            new_table[key].extend(other.data[key])
        return DataFrame(new_table)

    def select(self, selected_columns: list[str]) -> DataFrame:
        """Function narrows down full table to just selected columns of interest."""
        new_table: dict[str, list[str]] = {}
        for key in selected_columns:
            new_table[key] = self.data[key]
        return DataFrame(new_table)

    def filter_by_col_value(self, column_name: str, col_value: str) -> DataFrame:
        new_table: dict[str, list[str]] = {}
        # Initialize new table with new key values
        for k in self.data.keys():
            new_table[k] = []

        col_to_check: list = self.data[column_name]
        for index in range(0, len(col_to_check)):
            # If it is correct value
            if col_to_check[index] == col_value:
                # Then copy over all data
                for k in self.data.keys():
                    new_table[k].append(self.data[k][index])
        return DataFrame(new_table)

    def filter_by_rank(self, column_name, n: int) -> DataFrame:
        """Create new DataFrame with only the top n ranking members
        based on the numbers in column_name."""
        # Repeatedly find max, n many times
        max_indexes: list[int] = []  # store indexes of max values
        col_to_check: list = self.data[column_name]
        while len(max_indexes) < n:
            max_idx = -1
            max_val = -1
            for idx in range(0, len(col_to_check)):
                bigger: bool = int(col_to_check[idx]) > max_val
                dne: bool = not (idx in max_indexes)
                if bigger and dne:
                    max_idx = idx
                    max_val = int(col_to_check[idx])
            max_indexes.append(max_idx)
        # Make new data table
        new_table: dict[str, list[str]] = {}
        # Copy over keys
        for key in self.data:
            new_table[key] = []
        # Copy over values for each index
        for key in self.data:
            for i in max_indexes:
                new_table[key].append(self.data[key][i])
        return DataFrame(new_table)
