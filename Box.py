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
            x_pos = spacing / 2 - num.get_width() / 2
            y_pos = spacing / 2 - num.get_height() / 2
            window.blit(num, (x + x_pos, y + y_pos))

    def add_num(self, x):
        self.number = x

    def update_box(self, window, flag=True):
        ft = pygame.font.SysFont('comicsans', 40)

        dim = self.width / 9
        x = dim * self.col
        y = dim * self.row
        pygame.draw.rect(window, (255, 255, 255), (x, y, dim, dim), 0)
        num = ft.render(str(self.number), 1, (0, 0, 0))
        x_pos = dim / 2 - num.get_width() / 2
        y_pos = dim / 2 - num.get_height() / 2
        window.blit(num, (x + x_pos, y + y_pos))
        if flag:
            pygame.draw.rect(window, (0, 255, 0), (x, y, dim, dim), 3)
        else:
            pygame.draw.rect(window, (255, 0, 0), (x, y, dim, dim), 3)




