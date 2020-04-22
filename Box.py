import pygame


class Box:

    def __init__(self, number, row, col, width, height):
        self.number = number
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.isSelected = False

    def draw_boxes(self, window):
        spacing = self.width / 9
        x = spacing * self.col
        y = spacing * self.row
        ft = pygame.font.SysFont('comicsans', 40)

        if self.number != 0:
            num = ft.render(str(self.number), 1, (0, 0, 0))
            window.blit(num, (x + (spacing / 2 - num.get_width()/2), y + (spacing / 2 - num.get_height() / 2)))





