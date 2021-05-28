import pygame
import pygame.freetype
import random
import math
from perlin_noise import PerlinNoise

class Accollo(pygame.sprite.Sprite):

    def __init__(self, bg):

        super(Accollo, self).__init__()

        self.radius = 40

        self.limitLeft = bg.left
        self.limitRight = bg.right - 2 * self.radius
        self.limitTop = bg.top + bg.prog * bg.cellHeight
        self.limitBottom = bg.bottom + 2 * self.radius

        self.type = random.choice([0, 1, 2])
        if self.type == 0:
            self.text = "ATP"
        elif self.type == 1:
            self.text = "ATVI"
        elif self.type == 2:
            self.text = "ATColl"

        self.imgAngle = 0

        self.wobble = 0.005
        self.noise = PerlinNoise(octaves=10, seed=1)

        self.maxHP = 100
        textSize = 100 / 6
        self.FONT = pygame.freetype.SysFont("Lucon.ttf", textSize)
        self.HP = self.maxHP

        self.dist = 0

        self.aimAngle = 0
        self.acc = 0
        self.absAcc = 0.005
        self.vel = 0
        self.velX = 0
        self.velY = 0
        self.maxVel = 1
        self.minVel = 0.1
        self.angleAcc = 0
        self.angleVel = 0.05
        self.angle = 0
        self.x = random.randint(self.limitLeft, self.limitRight)
        self.y = random.randint(self.limitTop, self.limitBottom)

        self.surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32).convert_alpha()
        self.basicSurf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32).convert_alpha()
        pygame.draw.circle(self.basicSurf, (255, 0, 0), (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.basicSurf, (0, 0, 0), (self.radius, self.radius), self.radius, 2)
        self.rect = self.surf.get_rect()

        self.drawSurf()
        self.rect.move_ip(self.x, self.y)


    def drawSurf(self):

        self.surf.blit(self.basicSurf, (0,0))

        textThing = self.FONT.render('{:.2f}'.format(self.aimAngle), (0, 0, 0), None)
        textSurf = textThing[0]

        textSurf = pygame.transform.rotate(textSurf, self.angle * 360 / 6.283)
        textRect = textSurf.get_rect()

        self.surf.blit(textSurf, (self.radius - textRect.w / 2, self.radius - textRect.h / 2))
        posi = (self.rect.w / 2 + self.radius * self.velX, self.rect.h / 2 + self.radius * self.velY)
        pygame.draw.line(self.surf, (0, 0, 255), (self.rect.w / 2, self.rect.h / 2), posi, 6)
        # pygame.draw.rect(self.surf, (255, 255, 255), ((self.radius - textRect.w / 2, self.radius - textRect.h / 2), textSurf.get_size()),2)


    def update(self, aim, tick):

        
        self.imgAngle = (self.imgAngle - 3) % 360

        self.move(aim, tick)
        self.drawSurf()


    def move(self, aim, tick):
        
        dX = aim[0] - self.rect.centerx
        dY = aim[1] - self.rect.centery
        if dY == 0:
            dY = 0.001

        # self.aimAngle = math.atan(dX / dY)
        self.aimAngle = math.atan2(dX, dY)
        self.aimAngle %= (2 * math.pi)

        delta = (self.aimAngle * 57 - self.angle * 57 + 540) % 360 - 180

        if delta > 0:
            self.angleVel = abs(self.angleVel)
        else:
            self.angleVel = - abs(self.angleVel)

        self.dist = math.sqrt(dX ** 2 + dY ** 2)
        if (self.velX * dX >= 0) and (self.velY * dY >= 0):
            self.acc = self.absAcc
        else:
            self.acc = -self.absAcc

        self.vel = max(min(self.vel + self.acc, self.maxVel), self.minVel)
        wobbleFactor = self.noise([self.wobble * self.velX / self.maxVel, self.wobble * self.velY / self.maxVel]) * self.angleVel * 10
        self.angle = (self.angle + self.angleVel + wobbleFactor) % (2 * math.pi)

        self.velX = self.vel * math.sin(self.angle + wobbleFactor)
        self.velY = self.vel * math.cos(self.angle + wobbleFactor)

        self.rect.move_ip(self.velX * tick, self.velY * tick)

        # if self.rect.left < self.limitLeft:
        #     self.rect.left = self.limitLeft
        #     self.velX = 0
        # if self.rect.right > self.limitRight:
        #     self.rect.right = self.limitRight 
        #     self.velX = 0
        # if self.rect.top < self.limitTop:
        #     self.rect.top = self.limitTop
        #     self.velY = 0
        # if self.rect.bottom > self.limitBottom:
        #     self.rect.bottom = self.limitBottom
        #     self.velY = 0


