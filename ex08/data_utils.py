"""Data utility functions."""

__author__ = "720310785"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Function pulls raw data and assigns it to a list of dictionaries consisting of strings."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Function reformats data and produces one 'categories' values as a column."""
    one_column: list[str] = []
    for row in table:
        one_column.append(row[column])
    return one_column


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Function uses the column_values function to reformat ALL data into a format similar to that of a table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result
