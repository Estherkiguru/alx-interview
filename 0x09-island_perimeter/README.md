# 0x09. Island Perimeter 

Calculates the perimeter of an island in a grid.
The island is represented by `1`s (land) and surrounded by `0`s (water).
The goal is to determine the perimeter of the island by analyzing the grid.
This algorithm iterates through each cell in a 2D grid.
For each land cell, it initially assumes that all four sides contribute to the perimeter.
If the land cell is adjacent to another land cell, the shared side does not contribute to the perimeter, so the algorithm reduces the perimeter count accordingly.
