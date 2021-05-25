import pygame
import globalvar as g
import random
from pygame.locals import K_SPACE

class Activity(pygame.sprite.Sprite):

    def __init__(self, bg):

        super(Activity, self).__init__()

        self.height = bg.cellHeight / 2
        self.width = bg.cellWidth

        self.x = random.randint(1, bg.cols) * bg.cellWidth + bg.left
        self.y = random.randint(1, bg.rows) * bg.cellHeight + bg.top + bg.cellHeight / 4

        self.days = []
        self.randomGen()
        self.getName()
        self.drawSurf()

    def drawSurf(self):

        self.surf = pygame.Surface((self.daysLeft * self.width, self.height))
        self.surf.fill((209, 96, 2))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.x, self.y)

    def getName(self):

        self.name = "ASPEN"

    def randomGen(self):

        self.daysLeft = random.randint(1, 10)
        for i in range(0, self.daysLeft):
            self.days.append(False)

    def update(self, tick):

        # Actual movement
        self.rect.move_ip(self.velX * tick, self.velY * tick)

        removeThis = False

        if self.rect.left < self.limitLeft:
            removeThis = True
            self.velX = 0
        if self.rect.right > self.limitRight:
            removeThis = True
            self.velX = 0
        if self.rect.top < self.limitTop:
            removeThis = True
            self.velY = 0
        if self.rect.bottom > self.limitBottom:
            removeThis = True
            self.velY = 0

        return removeThis