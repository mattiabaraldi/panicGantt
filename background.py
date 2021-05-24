import globalvar as g
import pygame
import numpy

class Background(pygame.sprite.Sprite):

    def __init__(self):

        super(Background, self).__init__()

        self.width = g.SCREEN_WIDTH - g.LEFT_UI_WIDTH -g. RIGHT_UI_WIDTH
        self.height = g.SCREEN_HEIGHT - g.TOP_UI_HEIGHT - g.BOTTOM_UI_HEIGHT
        self.left = g.LEFT_UI_WIDTH
        self.right = g.SCREEN_WIDTH - g.RIGHT_UI_WIDTH
        self.top = g.TOP_UI_HEIGHT
        self.bottom = g.SCREEN_HEIGHT - g.BOTTOM_UI_HEIGHT
        self.surf = pygame.Surface((self.width, self.height))

        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.colOffset = 0

        self.rows = 22
        self.cols = 28
        self.cellWidth = self.width / self.cols
        self.cellHeight = self.height/ self.rows

        self.matr = numpy.zeros((self.rows, self.cols))

    def update(self, frame):

        if frame == 0:
            self.colOffset -= self.cellWidth
            self.colOffset = self.colOffset % self.width

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                color = (255, 255, 255)
                if (j % 7 == 0) or (j % 7 == 1):
                    color = (200, 200, 200)
                pygame.draw.rect(self.surf, color, (j * self.cellWidth, i * self.cellHeight, self.cellWidth - 1, self.cellHeight - 1))