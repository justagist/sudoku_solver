
# ===== Global Constants ======
BLANK = 0 # ----- represents empty cells 
ALL_DONE = [8,8]
# =============================

class SudokuGrid:
    '''
        Create an instance of SudokuGrid
    '''
    def __init__(self, np_grid):
        '''
            @Args:
                np_grid (numpy.ndarray): A 9x9 numpy array of the sudoku puzzle (with zeros in the blank cells)
        '''
        self.grid = np_grid

    def get_unassigned_location(self):
        '''
            Gets the (lexicographically) first empty cell in the SudokuGrid object
        '''

        for row in range(9):
            for column in range(9):
                if self.grid[row, column] == BLANK:
                    return row,column

        # ----- if no cell is BLANK, return ALL_DONE, marking that the grid is filled
        return ALL_DONE 
