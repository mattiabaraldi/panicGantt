import pygame
import math
import globalvar as g
from pygame.locals import K_SPACE
from projectile import Projectile
from turret import Turret

class Player(pygame.sprite.Sprite):

    def __init__(self, bg):

        super(Player, self).__init__()

        # self.surf = pygame.Surface((16, 32))
        # self.surf.fill((255, 0, 0))

        self.surf = pygame.image.load("sprites\\player_sprite.png")
        self.rect = self.surf.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.rect.move_ip(g.SCREEN_WIDTH / 2, g.SCREEN_HEIGHT / 2)
        self.velXMax = 5
        self.velYMax = 5
        self.velX = 0
        self.velY = 0
        self.jumpSpeed = 1.5
        self.accX = 0
        self.grav = 0.1
        self.accY = self.grav
        self.accM = 0.1
        self.frictionX = 0.9
        self.frictionY = 0.95

        self.score = 0
        self.cazziatoni = 0

        self.flipped = False

        self.limitLeft = bg.left
        self.limitRight = bg.right
        self.limitTop = bg.top
        self.limitBottom = bg.bottom

        self.projList = []
        self.turretList = []

        self.bg = bg

    def shoot(self, aim):

        dX = aim[0] - self.rect.centerx
        dY = aim[1] - self.rect.centery
        if dY == 0:
            dY = 0.001

        newProj = Projectile(self.rect.centerx, self.rect.centery, self.width, self.height, math.atan(dX / dY), self.bg)

        ratio = math.sqrt(dX ** 2 + dY ** 2)
        newProj.velX = newProj.speed * dX / ratio
        newProj.velY = newProj.speed * dY / ratio
       
        self.projList.append(newProj)

    def facingPos(self):

        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > self.rect.centerx:
            if self.flipped:
                self.surf = pygame.transform.flip(self.surf, True, False)
                self.flipped = False
        else:
            if not self.flipped:
                self.surf = pygame.transform.flip(self.surf, True, False)
                self.flipped = True

    def placeTurret(self, bg, x, y, selectedTurret):

        newTurret = Turret(bg, x, y, selectedTurret)
        self.turretList.append(newTurret)

    def updateTurrets(self):

        pass

    def update(self, pressed_keys, tick, enemies):

        self.updateTurrets()

        self.facingPos()

        projToRemove = []
        for proj in self.projList:
            if proj.update(tick, enemies):
                projToRemove.append(proj)

        for proj in projToRemove:
            self.projList.remove(proj)

        # User inputs
        if (pressed_keys[ord('w')] or pressed_keys[K_SPACE]) and not self.justJumped:
            if self.rect.bottom == self.limitBottom:
                self.velY -= self.jumpSpeed
                self.justJumped = True
                self.accY = self.grav / 3
        elif not (pressed_keys[ord('w')] or pressed_keys[K_SPACE]):
            self.justJumped = False
            self.accY = self.grav
        elif self.velY > 0:
            self.accY = self.grav
            
        if pressed_keys[ord('s')]:
            self.velY += self.accM
        if pressed_keys[ord('a')]:
            self.velX -= self.accM
        if pressed_keys[ord('d')]:
            self.velX += self.accM

        # Velocity calculations
        self.velX += self.accX
        self.velY += self.accY

        # Friction
        self.velX *= self.frictionX
        self.velY *= self.frictionY

        # Max speed controls
        self.velX = min(self.velX, self.velXMax)
        self.velX = max(self.velX, -self.velXMax)
        self.velY = min(self.velY, self.velYMax)
        self.velY = max(self.velY, -self.velYMax)

        # Actual movement
        self.rect.move_ip(self.velX * tick, self.velY * tick)

        if self.rect.left < self.limitLeft:
            self.rect.left = self.limitLeft
            self.velX = 0
        if self.rect.right > self.limitRight:
            self.rect.right = self.limitRight
            self.velX = 0
        if self.rect.top < self.limitTop:
            self.rect.top = self.limitTop
            self.velY = 0
        if self.rect.bottom > self.limitBottom:
            self.rect.bottom = self.limitBottom
            self.velY = 0