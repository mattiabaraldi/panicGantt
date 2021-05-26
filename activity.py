import pygame
import pygame.freetype
import random

class Activity(pygame.sprite.Sprite):

    def __init__(self, bg, row, type):

        super(Activity, self).__init__()

        self.height = bg.cellHeight * 3 / 5
        self.width = bg.cellWidth

        self.x = bg.right
        self.y = row * bg.cellHeight + bg.top + bg.cellHeight / 5

        self.limitLeft = bg.left
        self.limitRight = bg.right
        self.limitTop = bg.top
        self.limitBottom = bg.bottom

        self.type = type
        if self.type == 0:
            self.R = 80
            self.G = 90
            self.B = 224
        elif self.type == 1:
            self.R = 255
            self.G = 50
            self.B = 60
        elif self.type == 2:
            self.R = 200
            self.G = 90
            self.B = 200

        # self.R, self.G, self.B = 206, 96, 2
        self.color = (self.R, self.G, self.B)
        self.completed = False

        self.FONT = pygame.freetype.SysFont("Lucon.ttf", 10)

        self.days = []
        self.daysPassed = 0
        self.row = row
        self.name = f'{bg.steps}'
        self.randomGen()
        self.getName()
        self.drawSurf()

        self.HPperDay = 10
        self.maxHP = self.daysLeft * self.HPperDay
        self.HP = self.maxHP

    def drawSurf(self):

        self.surf = pygame.Surface((self.daysLeft * self.width, self.height))
        self.surf.fill(self.color)
        pygame.draw.rect(self.surf, (0,0,0), self.surf.get_rect(), 1)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.x, self.y)
        self.FONT.render_to(self.surf, (2, 3), self.name, (0, 0, 0))

    def recolorSurf(self):

        self.surf.fill(self.color)
        pygame.draw.rect(self.surf, (0,0,0), self.surf.get_rect(), 1)
        self.FONT.render_to(self.surf, (2, 3), self.name, (0, 0, 0))

    def getName(self):

        self.name = "20151 KLIMAOPREMA, PK-VS 0316-VIS 2"   

    def randomGen(self):

        self.daysLeft = random.randint(1, 14)
        for i in range(0, self.daysLeft):
            self.days.append(False)

        # self.x = random.randint(0, bg.cols - 1) * bg.cellWidth + bg.left
        # self.y = random.randint(0, bg.rows - 1) * bg.cellHeight + bg.top + bg.cellHeight / 5

        self.totWidth = self.daysLeft * self.width

    def doActivity(self, damage, *args):

        if not self.completed:

            if len(args) != 0:
                if args[0] != self.type:
                    damage = damage / 5
                    # return 2            # destroy projectile

            self.HP -= damage
            if self.HP <= 0:
                self.HP = 0
                self.completed = True

            self.color = (  self.R * self.HP / self.maxHP,
                            self.G * self.HP / self.maxHP + 255 * (1 - self.HP / self.maxHP),
                            self.B * self.HP / self.maxHP   )

            self.recolorSurf()

            return 1                    # destroy projectile after damage

        else:

            return 0                    # pass through

    def update(self, frame):

        removeThis = 0 

        if frame == 0:
            self.rect.move_ip(-self.width, 0)
            self.daysPassed += 1
            if self.daysPassed == self.daysLeft:
                removeThis = 1

        if self.rect.left < self.limitLeft - self.totWidth:
            removeThis = 2

        return removeThis