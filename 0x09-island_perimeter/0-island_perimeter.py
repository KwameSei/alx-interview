#!/usr/bin/python3
""" Solving the island perimeter puzzle """


def island_perimeter(grid):
    """Finding the perimeter of an island"""
    row_index = 0
    col_index = 0
    perimeter = 0

    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == 1:
                # Calculate the perimeter for each land cell

                # Check the cell above
                if row_index > 0 and grid[row_index - 1][col_index] == 0:
                    perimeter += 1

                # Check the cell below
                if row_index < len(grid) - 1 and\
                        grid[row_index + 1][col_index] == 0:
                    perimeter += 1

                # Check the cell to the right
                if col_index < len(row) - 1 and row[col_index + 1] == 0:
                    perimeter += 1

                # Check the cell to the left
                if col_index > 0 and row[col_index - 1] == 0:
                    perimeter += 1

    return perimeter
