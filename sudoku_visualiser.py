import sys
import copy
import pygame
import numpy as np
from sudoku_grid import SudokuGrid, GRID_FULL, BLANK

_FPS_ = 30

# ===== Colours =====

_WHITE_ =    (255,255,255)
_BLACK_ =    (0,  0,  0)
_LIGHTGRAY_ = (200, 200, 200)
_GREEN_     = (34,139,34)

# ===================

# ===== Dimensions =====

_SIZE_SCALE_ = 5 # ----- change this value for changing size of window
_WINDOWSIZE_ = 90

# ======================


class SudokuVisualiser:

    def __init__(self, sudoku_grid,size_scale = _SIZE_SCALE_ ):
        self._sudoku_grid = copy.deepcopy(sudoku_grid)

        self._set_dimensions(size_scale)
        self._init_viewer()

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
        self.DISPLAYSURF.fill(_WHITE_)

        self._draw_grid()
        self._fill_with_initial_vals()

        pygame.display.set_caption('Sudoku Solver')

    def _draw_grid(self):
        '''
            Draw lines for the grid on display surface
        '''

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

        # print (color)
        row, col = position

        cellSurf = self.BASICFONT.render('%s' %(num), True, color)

        cellRect = cellSurf.get_rect()
        cellRect.center = ((col + 0.5)*self.CELLSIZE, (row + 0.5)*self.CELLSIZE)

        self.DISPLAYSURF.blit(cellSurf, cellRect)
        

    def _fill_with_initial_vals(self):

        for row in range(self._sudoku_grid.grid.shape[0]):
            for col in range(self._sudoku_grid.grid.shape[1]):
                if self._sudoku_grid.grid[row,col] != BLANK:
                    self._write_num_at(self._sudoku_grid.grid[row,col], [row,col])

    def update_empty_cells(self, new_grid):

        # print (_GREEN_,"YESS")
        for row in range(self._sudoku_grid.grid.shape[0]):
            for col in range(self._sudoku_grid.grid.shape[1]):
                if self._sudoku_grid.grid[row,col] == BLANK:
                    self._write_num_at(new_grid[row,col], [row,col], color = _GREEN_)


    def _main_loop(self):
        '''
            The main method running the pygame loop
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.display.update()
            self.FPSCLOCK.tick(_FPS_)

    def stop_visaliser(self):
        pygame.quit()

    def run(self):
        self._main_loop()



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
    
    sv = SudokuVisualiser(s_grid)
    sv.run()
