import pygame
import random
import string
import globalvar as g
from pygame.locals import K_SPACE
from numba import vectorize, jit

@jit
def callbackCollideGPU(selfX, selfY, enemyTop, enemyBottom, enemyLeft, enemyRight):

        # return self.rect.collidepoint((enemy.rect.x, enemy.rect.y))
        if enemyTop < selfY < enemyBottom:
            if enemyLeft < selfX < enemyRight:
                return True
            # return enemy.rect.collidepoint((self.rect.x, self.rect.y))
        else:
            return False

class TurretProj(pygame.sprite.Sprite):

    def __init__(self, turretX, turretY, turretW, turretH, bg, pork, type):

        super(TurretProj, self).__init__()

        self.width = 16
        self.height = 16

        # self.surf = pygame.Surface((self.width, self.height))
        self.surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.surf = self.surf.convert_alpha()

        projAlpha = 96

        self.type = type
        self.color = [(63, 72, 204, projAlpha), (227, 28, 36, projAlpha), (173, 63, 174, projAlpha)][self.type]
        
        self.FONT = pygame.freetype.SysFont("Lucon.ttf", 16)
        self.FONT.render_to(self.surf, (0, 0), pork, self.color)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(turretX - turretW / 4, turretY - turretH)

        self.surf = pygame.transform.rotate(self.surf, 90)
        self.rect = self.surf.get_rect(center = self.rect.center)

        self.velX = 0
        self.velY = -0.1
        self.actDamage = 5
        self.accDamage = 1

        self.limitLeft = bg.left
        self.limitRight = bg.right
        self.limitTop = bg.top
        self.limitBottom = bg.bottom


    def callbackCollide(self, enemy2, enemy):

        # return self.rect.collidepoint((enemy.rect.x, enemy.rect.y))
        if enemy.rect.top < self.rect.y < enemy.rect.bottom:
            if enemy.rect.left < self.rect.x < enemy.rect.right:
                return enemy
            # return enemy.rect.collidepoint((self.rect.x, self.rect.y))
        else:
            return False
    

    def update(self, tick, enemies):

        # Actual movement
        self.rect.move_ip(self.velX * tick, self.velY * tick)

        removeThis = False
        
        # collidedActivity = None
        # for enemy in enemies.groupGANTT:
        #     if callbackCollideGPU(self.rect.x, self.rect.y, enemy.rect.top, enemy.rect.bottom, enemy.rect.left, enemy.rect.right):
        #         collidedActivity = enemy
        #         break
        collidedActivity = pygame.sprite.spritecollideany(self, enemies.groupGANTT, self.callbackCollide)
        if collidedActivity != None:
            collisionResult = collidedActivity.doActivity(self.actDamage, self.type)
            if collisionResult == 1:
                removeThis = True
            elif collisionResult == 2:
                collidedActivity.kill()

        collidedAccollo = pygame.sprite.spritecollideany(self, enemies.groupAccolli, self.callbackCollide)
        if collidedAccollo != None:
            if collidedAccollo.doActivity(self.accDamage):
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