from sudoku_grid import SudokuGrid, BLANK, GRID_FULL
import numpy as np

class SudokuSolver:

    def __init__(self, s_grid):

        self.final_grid = s_grid

    def is_used_in_row(self, grid, item, row):

        for i in range(9):
            if item == grid[row,i]:

                return True

        return False

    def is_used_in_col(self, grid, item, col):

        for i in range(9):
            if item == grid[i, col]:
                return True

        return False

    def is_used_in_box(self, grid, item, row, col):

        start_row = row - (row % 3)
        start_col = col - (col % 3)

        for i in range(3):
            for j in range(3):
                if item == grid[start_row + i, start_col + j]:
                    return True

        return False

    def is_safe(self, grid, item, row, col):

        if not (self.is_used_in_row(grid, item, row) or self.is_used_in_col(grid, item, col) or self.is_used_in_box(grid, item, row, col)):

            return True

        return False

    def solve_sudoku(self, grid):

        if grid.get_unassigned_location() == GRID_FULL:
            return True

        row, col = grid.get_unassigned_location()

        for i in range(1,10):
            if self.is_safe(grid, i, row, col):
                grid[row, col] = i

                if self.solve_sudoku(grid):
                    self.final_grid = grid
                    return True

                grid[row, col] = BLANK

        return False


