import pygame
import globalvar as g
from pygame.locals import K_SPACE

class Projectile(pygame.sprite.Sprite):

    def __init__(self, playerX, playerY, bg):

        super(Projectile, self).__init__()
        self.surf = pygame.Surface((32, 16), pygame.SRCALPHA, 32)
        self.surf = self.surf.convert_alpha()
        self.FONT = pygame.freetype.SysFont("Lucon.ttf", 10)
        self.FONT.render_to(self.surf, (0, 0), "!%@?", (0, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(playerX, playerY)

        # self.velXMax = 5
        # self.velYMax = 5

        self.type = 0

        self.speed = 0.2

        # self.accX = 0
        # self.grav = 0.1
        # self.accY = self.grav
        # self.accM = 0.1
        # self.frictionX = 0.9
        # self.frictionY = 0.95

        self.limitLeft = bg.left
        self.limitRight = bg.right
        self.limitTop = bg.top
        self.limitBottom = bg.bottom

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