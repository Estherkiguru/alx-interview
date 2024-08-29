#!/usr/bin/python3
"""Module for Island_perimeter function"""


def island_perimeter(grid):
    """Returns: Primeter of island described in the grid"""
    per_grid = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                per_grid += 4

                if i > 0 and grid[i - 1][j] == 1:
                    per_grid -= 1

                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    per_grid -= 1

                if j > 0 and grid[i][j - 1] == 1:
                    per_grid -= 1

                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    per_grid -= 1
    return per_grid
