#!/usr/bin/python3
""" Solving the island perimeter puzzle """


def island_perimeter(grid):
    """ Finding the perimeter of an island """
    row_index = 0
    col_index = 0
    perimeter = 0

    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == 1:
                # perimeter += 4

                if row_index > 0 and row_index < (len(grid) - 1):
                    if grid[row_index + 1][col_index] == 0:
                        perimeter += 1
                    else: perimeter += 0

                    if grid[row_index - 1][col_index] == 0:
                        perimeter += 1
                    else: perimeter += 0

                    if row[col_index + 1] == 0:
                        perimeter += 1
                    else: perimeter += 0

                    if row[col_index - 1] == 0:
                        perimeter += 1
                    else: perimeter += 0

    return perimeter
