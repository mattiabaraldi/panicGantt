import pygame
import pygame.freetype
import globalvar as g
import random
from pygame.locals import K_SPACE

class Activity(pygame.sprite.Sprite):

    def __init__(self, bg):

        super(Activity, self).__init__()

        self.height = bg.cellHeight * 3 / 5
        self.width = bg.cellWidth

        self.x = random.randint(0, bg.cols - 1) * bg.cellWidth + bg.left
        self.y = random.randint(0, bg.rows - 1) * bg.cellHeight + bg.top + bg.cellHeight / 5

        self.limitLeft = bg.left
        self.limitRight = bg.right
        self.limitTop = bg.top
        self.limitBottom = bg.bottom

        self.FONT = pygame.freetype.SysFont("Lucon.ttf", 10)

        self.days = []
        self.randomGen()
        self.getName()
        self.drawSurf()

    def drawSurf(self):

        self.surf = pygame.Surface((self.daysLeft * self.width, self.height))
        self.surf.fill((209, 96, 2))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.x, self.y)
        self.FONT.render_to(self.surf, (2, 3), "20151 KLIMAOPREMA, PK-VS 0316-VIS 2", (0, 0, 0))

    def getName(self):

        self.name = "ASPEN"

    def randomGen(self):

        self.daysLeft = random.randint(1, 10)
        for i in range(0, self.daysLeft):
            self.days.append(False)
        
        self.totWidth = self.daysLeft * self.width

    def update(self, frame):

        if frame == 0:
            self.rect.move_ip(-self.width, 0)

        removeThis = False
        if self.rect.left < self.limitLeft - self.totWidth:
            removeThis = True

        return removeThis