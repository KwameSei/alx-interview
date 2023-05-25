#!/usr/bin/python3
""" Solving the island perimeter puzzle """


def island_perimeter(grid):
    """ Finding the perimeter of an island """
    perimeter = 0

    # Iterate through each row and column index using range
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if grid[row_index][col_index] == 1:
                # Calculate the perimeter for each land cell

                # Check the cell above
                if row_index == 0 or grid[row_index - 1][col_index] == 0:
                    perimeter += 1

                # Check the cell below
                if row_index == len(grid) - 1 or\
                        grid[row_index + 1][col_index] == 0:
                    perimeter += 1

                # Check the cell to the left
                if col_index == 0 or grid[row_index][col_index - 1] == 0:
                    perimeter += 1

                # Check the cell to the right
                if col_index == len(grid[row_index]) - 1 or\
                        grid[row_index][col_index + 1] == 0:
                    perimeter += 1

    return perimeter
