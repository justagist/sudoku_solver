import threading
import numpy as np
from sudoku_grid import SudokuGrid
from sudoku_solver import SudokuSolver

def is_valid(seq):

    if len(set(seq+[0])) == 10:
        return True

    return False

def is_valid_box(grid):
    
    return  is_valid(np.reshape(grid,9).tolist())

def validate_solution(grid):

    for i in range(9):

        if not is_valid(grid[i,:].tolist()):
            return False

        if not is_valid(grid[:,i].tolist()):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):

            if not is_valid_box(grid[i:i+3, j:j+3]):
                return False

    return True



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

    solver = SudokuSolver(start_grid = s_grid,visualise = True, visualise_full = False)
    
    solver.solve_sudoku()

    print ("\nSolution is Valid" if validate_solution(solver.final_grid) else "\nSolution is not Valid")


