import SolveSudoku as sd
from Box import Box
import pygame
pygame.init()


class GUI:

    def __init__(self, grid, width, height, window):
        self.height = height
        self.width = width
        self.window = window
        self.grid = grid
        self.rows = 9
        self.cols = 9
        self.boxes = [[Box(self.grid[i][j], i, j, self.width, self.height) for j in range(self.cols)]
                      for i in range(self.rows)]

    def draw_grid(self):
        space = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.window, (0, 0, 0), (0, i * space), (self.width, i * space), thickness)
            pygame.draw.line(self.window, (0, 0, 0), (i * space, 0), (i * space, self.height), thickness)

        for i in range(self.rows):
            for j in range(self.cols):
                self.boxes[i][j].draw_boxes(self.window)


def redrawWindow(win, grid):
    win.fill((255, 255, 255))
    grid.draw_grid()


def main():
    grid = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    grid = GUI(grid, 540, 540, window)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        redrawWindow(window, grid)
        pygame.display.update()


main()
pygame.quit()

