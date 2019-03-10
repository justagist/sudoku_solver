import time
import threading
from sudoku_visualiser import SudokuVisualiser
from sudoku_grid import BLANK, ALL_DONE

class SudokuSolver:

    def __init__(self, start_grid, visualise = False, visualise_full = False):

        self._start_grid = start_grid

        self.final_grid = None # ----- stores the final grid if solution is found
        self._temp_grid = None # ----- temporary grid used by visualiser

        # ----- Flags for visualisation
        self._visualisation = visualise # ----- enable pygame visualisation
        self._visualise_full = False # ----- visualise solving (slower)

        # ----- Run the visualiser in another thread if needed
        if self._visualisation:
            self._vis = SudokuVisualiser(solver=self, visualise_full_solving = visualise_full)
            self._visualise_full = visualise_full
            self._thread = threading.Thread(target=self._vis.run)
            self._thread.start()

    def solve_sudoku(self):
        '''
            Public method to solve the original SudokuGrid instance
        '''
        self._solve_sudoku(self._start_grid)
        print(self)
        self._thread.join() # ----- end the visualiser thread if it is active


    def _solve_sudoku(self, grid):

        if grid.get_unassigned_location() == ALL_DONE:
            return True

        if self._visualise_full:
            self._temp_grid = grid.grid
            time.sleep(0.001)

        row, col = grid.get_unassigned_location()

        for i in range(1,10):
            if self.is_safe(grid, i, row, col):
                grid.grid[row, col] = i

                if self._solve_sudoku(grid):
                    self.final_grid = grid.grid
                    return True

                grid.grid[row, col] = BLANK

        return False

    # ===== Methods that check if the number in a specific cell is valid ====== 

    def is_used_in_row(self, grid, item, row):
        '''
            Check if the number is valid in the given row in the given SudokuGrid instance
            @Args:
                grid : The SudokuGrid instance to be checked in 
                item : The number whose validity in the grid is to be checked
                row  : The row to be checked
        '''
        for i in range(9):
            if item == grid.grid[row,i]:

                return True

        return False

    def is_used_in_col(self, grid, item, col):
        '''
            Check if the number is valid in the given column in the given SudokuGrid instance
            @Args:
                grid : The SudokuGrid instance to be checked in 
                item : The number whose validity in the grid is to be checked
                col  : The column to be checked
        '''

        for i in range(9):
            if item == grid.grid[i, col]:
                return True

        return False

    def is_used_in_box(self, grid, item, row, col):
        '''
            Check if the number is valid in its 3x3 box in the given SudokuGrid instance
            @Args:
                grid    : The SudokuGrid instance to be checked in 
                item    : The number whose validity in the box is to be checked
                row, col: The row and column where the number will be placed
        '''
        start_row = row - (row % 3)
        start_col = col - (col % 3)

        for i in range(3):
            for j in range(3):
                if item == grid.grid[start_row + i, start_col + j]:
                    return True

        return False

    def is_safe(self, grid, item, row, col):
        '''
            A combined check method which does all the above checks
            @Args:
                grid    : The SudokuGrid instance to be checked in 
                item    : The number whose validity is to be checked
                row, col: The row and column where the number will be placed
        '''
        if not (self.is_used_in_row(grid, item, row) or self.is_used_in_col(grid, item, col) or self.is_used_in_box(grid, item, row, col)):

            return True

        return False

    # ==========================================================================

    def __str__(self): 
        '''
            Print the final grid if the solution is found.
        '''
        return "\nCould Not Solve Sudoku!" if self.final_grid is None else "\nSolution: \n" + str(self.final_grid)


