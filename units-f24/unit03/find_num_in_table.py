class Table:
    width: int
    height: int
    data: list[list[int]]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.data = []
        for y in range(height):
            row: list[int] = []
            for x in range(width):
                row.append(0)
            self.data.append(row)

    def find(self, inp_num: int) -> dict[int, int]:
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] == inp_num:
                    return {row: col}
        return {-1: -1}

    def __str__(self) -> str:
        """Returns a string representation of the table."""
        table_str: str = ''
        row_idx: int = 0
        while row_idx < len(self.data):
            row: int = self.data[row_idx]
            col_idx: int = 0
            while col_idx < len(row):
                table_str += str(row[col_idx])
                if col_idx < len(row) - 1:
                    table_str += ' '
                col_idx += 1
            if row_idx < len(self.data) - 1:
                table_str += '\n'  # do not worry about this, it just means an intend
            row_idx += 1
        return table_str

# Instantiate the Table class
table: Table = Table(3, 3)

# Modify the table data for testing
table.data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call the find method
position: dict[int, int] = table.find(5)
print(f"Position of 5: {position}")  # Output should be (1, 1)

# Call the find method for a number not in the table
position_not_found: dict[int, int] = table.find(10)
print(f"Position of 10: {position_not_found}")  # Output should be (-1, -1)

# Print the table
print("Table:")
print(table)
