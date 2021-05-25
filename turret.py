import pygame
import pygame.freetype
import random

class Turret(pygame.sprite.Sprite):

    def __init__(self, bg, x, y, type):

        super(Turret, self).__init__()

        self.limitLeft = bg.left
        self.limitRight = bg.right
        self.limitTop = bg.top
        self.limitBottom = bg.bottom

        self.radius = 20
        self.type = type

        self.x = x
        self.y = y

        self.surf = None

        if self.type == 1:
            self.surf = pygame.image.load("sprites\\blu_turret.png")
        elif self.type == 2:
            self.surf = pygame.image.load("sprites\\red_turret.png")
        elif self.type == 3:
            self.surf = pygame.image.load("sprites\\violet_turret.png")

        self.rect = self.surf.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        turretX = max(min(x, self.limitRight - self.width / 2), self.limitLeft + self.width / 2)
        self.rect.move_ip(turretX - self.width / 2, self.limitBottom - self.height)

        self.HPperDay = 10
        self.maxHP = 100
        self.HP = self.maxHP
