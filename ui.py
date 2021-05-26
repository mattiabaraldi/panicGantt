import globalvar as g
import pygame
import pygame.freetype

class UI(pygame.sprite.Sprite):

    def __init__(self, bg):

        super(UI, self).__init__()

        self.surf = pygame.Surface((g.SCREEN_WIDTH, g.SCREEN_HEIGHT), pygame.SRCALPHA, 32)
        self.surf = self.surf.convert_alpha()
        
        self.surfNames = pygame.Surface((g.LEFT_UI_WIDTH, g.SCREEN_HEIGHT - g.TOP_UI_HEIGHT))
        self.surfMenus = pygame.Surface((g.SCREEN_WIDTH, g.TOP_UI_HEIGHT))
        self.surfBottom = pygame.Surface((g.SCREEN_WIDTH - g.LEFT_UI_WIDTH, g.BOTTOM_UI_HEIGHT))
        self.surfRight = pygame.Surface((g.RIGHT_UI_WIDTH, g.SCREEN_HEIGHT - g.TOP_UI_HEIGHT))

        self.bluTurret = pygame.image.load("sprites\\blu_turret.png")
        self.redTurret = pygame.image.load("sprites\\red_turret.png")
        self.violetTurret = pygame.image.load("sprites\\violet_turret.png")

        self.FONT = pygame.freetype.SysFont("Lucon.ttf", 12)
        self.progList = ["Ivan Battaglia", "Marco Ardizzoni", "Andrea Malaguti", "Fabio Manelli", "Nicola Negossi", "Mattia Baraldi", "Giulio Talassi", "Vincenzo Mauro"]
        self.progDuty = [2, 2, 2, 1, 1, 1, 0, 0]

        self.trasferelloNames = pygame.image.load("sprites\\UI_names.png")
        self.trasferelloNames = pygame.transform.scale(self.trasferelloNames, (self.surfNames.get_rect().width, self.surfNames.get_rect().height))

        self.trasferelloMenus = pygame.image.load("sprites\\UI_top.png")
        self.trasferelloMenus = pygame.transform.scale(self.trasferelloMenus, (self.surfMenus.get_rect().width, self.surfMenus.get_rect().height))

        self.trasferelloBottom = pygame.image.load("sprites\\UI_bottom.png")
        self.trasferelloBottom = pygame.transform.scale(self.trasferelloBottom, (self.surfBottom.get_rect().width, self.surfBottom.get_rect().height))

        self.trasferelloRight = pygame.image.load("sprites\\UI_right.png")
        self.trasferelloRight = pygame.transform.scale(self.trasferelloRight, (self.surfRight.get_rect().width, self.surfRight.get_rect().height))

        # self.surfNames.blit(self.trasferelloNames, (0,0))
        self.surfMenus.blit(self.trasferelloMenus, (0,0))
        self.surfBottom.blit(self.trasferelloBottom, (0,0))
        self.surfRight.blit(self.trasferelloRight, (0,0))

        self.cellHeight = bg.cellHeight
        self.rows = bg.rows
        self.prog = bg.prog

        self.surf.blit(self.surfNames, (0, g.TOP_UI_HEIGHT))
        self.surf.blit(self.surfMenus, (0, 0))
        self.surf.blit(self.surfBottom, (g.LEFT_UI_WIDTH, g.SCREEN_HEIGHT - g.BOTTOM_UI_HEIGHT))
        self.surf.blit(self.surfRight, (g.SCREEN_WIDTH - g.RIGHT_UI_WIDTH, g.TOP_UI_HEIGHT))

    def update(self, player, selectedTurret):

        # self.surfNames.blit(self.trasferelloNames, (0,0))
        self.surfNames.fill((0,0,0))

        for i in range(0, self.prog):
            color = (255, 255, 255)
            pygame.draw.rect(self.surfNames, color, (0, i * self.cellHeight, g.LEFT_UI_WIDTH - 2, self.cellHeight - 2))
            self.FONT.render_to(self.surfNames, (10, i * self.cellHeight + self.cellHeight  / 2), self.progList[i], (0, 0, 0))
        
        pygame.draw.rect(self.surfNames, color, (0, self.prog * self.cellHeight, g.LEFT_UI_WIDTH - 1, g.SCREEN_HEIGHT - g.TOP_UI_HEIGHT - 1))



        uiPos = (self.prog + 1) * self.cellHeight

        uiPos += 20
        self.FONT.render_to(self.surfNames, (10, uiPos), f'Punti: {player.score}', (0, 0, 0))
        uiPos += 20
        self.FONT.render_to(self.surfNames, (10, uiPos), f'Cazzi: {player.cazziatoni}', (0, 0, 0))

        bluAlpha = 127
        redAlpha = 127
        violetAlpha = 127
        if selectedTurret == 1:
            bluAlpha = 255
        elif selectedTurret == 2:
            redAlpha = 255
        elif selectedTurret == 3:
            violetAlpha = 255

        self.bluTurret.set_alpha(bluAlpha)
        self.redTurret.set_alpha(redAlpha)
        self.violetTurret.set_alpha(violetAlpha)

        uiPos += 40
        self.surfNames.blit(self.bluTurret, (10, uiPos))
        self.surfNames.blit(self.redTurret, (30, uiPos))
        self.surfNames.blit(self.violetTurret, (50, uiPos))

        self.surf.blit(self.surfNames, (0, g.TOP_UI_HEIGHT))
        self.surf.blit(self.surfMenus, (0, 0))
        self.surf.blit(self.surfBottom, (g.LEFT_UI_WIDTH, g.SCREEN_HEIGHT - g.BOTTOM_UI_HEIGHT))
        self.surf.blit(self.surfRight, (g.SCREEN_WIDTH - g.RIGHT_UI_WIDTH, g.TOP_UI_HEIGHT))