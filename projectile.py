import pygame
import random
import string
import globalvar as g
from pygame.locals import K_SPACE

class Projectile(pygame.sprite.Sprite):

    def __init__(self, playerX, playerY, angle, bg):

        super(Projectile, self).__init__()

        self.width = 16
        self.height = 16

        # self.surf = pygame.Surface((self.width, self.height))
        self.surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.surf = self.surf.convert_alpha()
        
        self.FONT = pygame.freetype.SysFont("Lucon.ttf", 12)
        pork = random.choice(string.punctuation)
        self.FONT.render_to(self.surf, (0, 0), pork, (0, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(playerX - 16, playerY - 8)

        # DA FIXARE, LA ROTAZIONE SVACCA RECT E PUNTO DI ANCHOR
        # def blitRotateCenter(surf, image, topleft, angle):

        #     rotated_image = pygame.transform.rotate(image, angle)
        #     new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

        #     surf.blit(rotated_image, new_rect)

        self.surf = pygame.transform.rotate(self.surf, angle * 180 / 3.14 + 90)
        # self.rect = self.surf.get_rect(center = self.rect.center)

        self.type = 0
        self.speed = 0.5
        self.damage = 1

        self.limitLeft = bg.left
        self.limitRight = bg.right
        self.limitTop = bg.top
        self.limitBottom = bg.bottom

    def update(self, tick, enemies):

        # Actual movement
        self.rect.move_ip(self.velX * tick, self.velY * tick)

        removeThis = False

        collidedActivity = pygame.sprite.spritecollideany(self, enemies.groupGANTT)
        if collidedActivity != None:
            if collidedActivity.doActivity(self.damage):
                removeThis = True

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