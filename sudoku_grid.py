
import numpy as np

BLANK = 0
GRID_FULL = [8, 8]

class SudokuGrid:

    def __init__(self, np_grid):

        self.grid = np_grid

    def get_unassigned_location(self):

        # assuming all the cells in the grid are populated with 0 in the beginning
        for row in range(9):
            for column in range(9):
                if self.grid[row, column] == BLANK:

                    return row,column

        return GRID_FULL