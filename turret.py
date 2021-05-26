import pygame
import pygame.freetype
from turret_proj import TurretProj
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

        self.projList = []

        self.surf = None

        if self.type == 0:
            self.surf = pygame.image.load("sprites\\blu_turret.png")
        elif self.type == 1:
            self.surf = pygame.image.load("sprites\\red_turret.png")
        elif self.type == 2:
            self.surf = pygame.image.load("sprites\\violet_turret.png")

        self.rect = self.surf.get_rect()

        self.width = self.rect.width
        self.height = self.rect.height

        turretX = max(min(x, self.limitRight - self.width / 2), self.limitLeft + self.width / 2)
        self.rect.move_ip(turretX - self.width / 2, self.limitBottom - self.height)

        self.x = self.rect.centerx
        self.y = self.rect.centery

        self.HPperDay = 10
        self.maxHP = 100
        self.HP = self.maxHP

        self.pork = ["maremmaputtanaimpestata", "mannaggialclero", "tivengaunaccidente"][self.type]
        self.cnt = 0
        self.index = len(self.pork) + 1
        self.rateOfFire = 3


    def update(self, tick, bg, enemies):

        projToRemove = []
        for proj in self.projList:
            if proj.update(tick, enemies):
                projToRemove.append(proj)

        for proj in projToRemove:
            self.projList.remove(proj)

        self.cnt += tick
        if self.cnt > 1000 / self.rateOfFire:
            self.cnt = 0
            self.index = self.index % len(self.pork)
            nextLetter = self.pork[-self.index]
            self.index += 1
            newProj = TurretProj(self.x, self.y, self.width, self.height, bg, nextLetter, self.type)      
            self.projList.append(newProj)
        

