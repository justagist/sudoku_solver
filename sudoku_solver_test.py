import numpy as np
from sudoku_grid import SudokuGrid
from sudoku_solver import SudokuSolver

if __name__ == '__main__':
    
    grid = np.asarray([ [ 0, 9, 0, 0, 0, 0, 8, 5, 3 ],
                       [ 0, 0, 0, 8, 0, 0, 0, 0, 4 ],
                       [ 0, 0, 8, 2, 0, 3, 0, 6, 9 ],
                       [ 5, 7, 4, 0, 0, 2, 0, 0, 0 ],
                       [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                       [ 0, 0, 0, 9, 0, 0, 6, 3, 7 ],
                       [ 9, 4, 0, 1, 0, 8, 5, 0, 0 ],
                       [ 7, 0, 0, 0, 0, 6, 0, 0, 0 ],
                       [ 6, 8, 2, 0, 0, 0, 0, 9, 0 ] ])


    s_grid = SudokuGrid(grid)

    solver = SudokuSolver()

    solver.solve_sudoku(s_grid)
    print (solver)


