import sys
import pygame

_FPS_ = 30

# ===== Colours =====

_WHITE_ =    (255,255,255)
_BLACK_ =    (0,  0,  0)
_LIGHTGRAY_ = (200, 200, 200)

# ===================

# ===== Dimensions =====

_SIZE_SCALE_ = 5 # ----- change this value for changing size of window
_WINDOWSIZE_ = 90

# ======================


class SudokuVisualiser:

    def __init__(self, size_scale = _SIZE_SCALE_ ):
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

        self.FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        self.DISPLAYSURF.fill(_WHITE_)

        self._draw_grid()

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


    def _main_loop(self):
        '''
            The main method running the pygame loop
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.FPSCLOCK.tick(_FPS_)

    def run(self):
        self._main_loop()



if __name__ == '__main__':
    
    sv = SudokuVisualiser()
    sv.run()
