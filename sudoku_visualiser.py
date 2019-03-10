import sys
import copy
import pygame
import numpy as np
from sudoku_grid import BLANK

_FPS_ = 100

# ===== Colours =====

_WHITE_ =    (255,255,255)
_BLACK_ =    (0,  0,  0)
_LIGHTGRAY_ = (200, 200, 200)
_GREEN_     = (34,139,34)
_RED_   =     (220,20,60)

# ===================

# ===== Dimensions =====

_SIZE_SCALE_ = 5 # ----- change this value for changing size of window
_WINDOWSIZE_ = 90

# ======================


class SudokuVisualiser:

    def __init__(self, solver = None,size_scale = _SIZE_SCALE_ , visualise_full_solving = False):
        '''
            Create a visualiser instance for the SudokuSolver
            @Args:
                solver (SudokuSolver) : The solver instance to be used
                size_scale (int)      : The scale for the visualiser window size
                visualise_full_solving: Set to True to see the solving process (slower)
                
        '''
        self._sudoku_grid = copy.deepcopy(solver._start_grid)

        self._set_dimensions(size_scale)
        self._init_viewer()

        self._solver = solver
        self._visualise_full_solving = visualise_full_solving


    def _set_dimensions(self, size_scale):
        '''
            Define the required dimensions using the given scale
        '''
        self.WINDOWWIDTH = _WINDOWSIZE_ * size_scale
        self.WINDOWHEIGHT = _WINDOWSIZE_ * size_scale
        self.SQUARESIZE = (_WINDOWSIZE_ * size_scale) // 3
        self.CELLSIZE = self.SQUARESIZE // 3

    def _init_viewer(self):
        '''
            Initialise the pygame window 
        '''
        pygame.init()

        self.BASICFONT = pygame.font.Font('freesansbold.ttf', int(0.8*self.CELLSIZE))
        self.FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))

        self._draw_grid()
        self._fill_with_initial_vals()

        self._DISP_COPY = self.DISPLAYSURF.copy()

        pygame.display.set_caption('Sudoku Solver')

    def _draw_grid(self):
        '''
            Draw lines for the grid on display surface
        '''
        self.DISPLAYSURF.fill(_WHITE_)

        # ----- Draw Minor Lines
        for x in range(0, self.WINDOWWIDTH, self.CELLSIZE): # draw vertical lines
            pygame.draw.line(self.DISPLAYSURF, _LIGHTGRAY_, (x,0),(x,self.WINDOWHEIGHT))

        for y in range (0, self.WINDOWHEIGHT, self.CELLSIZE): # draw horizontal lines
            pygame.draw.line(self.DISPLAYSURF, _LIGHTGRAY_, (0,y), (self.WINDOWWIDTH, y))
        
        # ----- Draw Major Lines
        for x in range(0, self.WINDOWWIDTH, self.SQUARESIZE): # draw vertical lines
            pygame.draw.line(self.DISPLAYSURF, _BLACK_, (x,0),(x,self.WINDOWHEIGHT))

        for y in range (0, self.WINDOWHEIGHT, self.SQUARESIZE): # draw horizontal lines
            pygame.draw.line(self.DISPLAYSURF, _BLACK_, (0,y), (self.WINDOWWIDTH, y))

    def _write_num_at(self, num, position, color = _BLACK_):
        '''
            Write the number at the (row,col) given in the position argument    
        '''
        row, col = position

        cellSurf = self.BASICFONT.render('%s' %(num), True, color)

        cellRect = cellSurf.get_rect()
        cellRect.center = ((col + 0.5)*self.CELLSIZE, (row + 0.5)*self.CELLSIZE)

        self.DISPLAYSURF.blit(cellSurf, cellRect)
        

    def _fill_with_initial_vals(self):
        '''
            Fill the grid with the numbers given in the initial grid (in Black)
        '''
        for row in range(self._sudoku_grid.grid.shape[0]):
            for col in range(self._sudoku_grid.grid.shape[1]):
                if self._sudoku_grid.grid[row,col] != BLANK:
                    self._write_num_at(self._sudoku_grid.grid[row,col], [row,col])

    def update_empty_cells(self, new_grid, color = _GREEN_):
        '''
            Empty cells are written with numbers from `new_grid' 
        '''
        for row in range(self._sudoku_grid.grid.shape[0]):
            for col in range(self._sudoku_grid.grid.shape[1]):
                if self._sudoku_grid.grid[row,col] == BLANK and new_grid[row,col] != BLANK:
                    self._write_num_at(new_grid[row,col], [row,col], color = color)


    def _main_loop(self):
        '''
            The main method running the pygame loop
        '''
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop_visaliser()
            if self._visualise_full_solving:
                self._draw_grid()
                self._fill_with_initial_vals()

                if self._solver is not None and self._solver._temp_grid is not None and self._solver.final_grid is None:
                    self.update_empty_cells(self._solver._temp_grid, color = _RED_)
            if self._solver.final_grid is not None:
                self.update_empty_cells(self._solver.final_grid, color = _GREEN_)
            pygame.display.update()
            self.FPSCLOCK.tick(_FPS_)

    def stop_visaliser(self):
        pygame.quit()
        sys.exit()

    def run(self):
        self._main_loop()


