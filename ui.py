import globalvar as g
import pygame
import pygame.freetype

class UI(pygame.sprite.Sprite):

    def __init__(self):

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

        self.trasferelloNames = pygame.image.load("sprites\\UI_names.png")
        self.trasferelloNames = pygame.transform.scale(self.trasferelloNames, (self.surfNames.get_rect().width, self.surfNames.get_rect().height))

        self.trasferelloMenus = pygame.image.load("sprites\\UI_top.png")
        self.trasferelloMenus = pygame.transform.scale(self.trasferelloMenus, (self.surfMenus.get_rect().width, self.surfMenus.get_rect().height))

        self.trasferelloBottom = pygame.image.load("sprites\\UI_bottom.png")
        self.trasferelloBottom = pygame.transform.scale(self.trasferelloBottom, (self.surfBottom.get_rect().width, self.surfBottom.get_rect().height))

        self.trasferelloRight = pygame.image.load("sprites\\UI_right.png")
        self.trasferelloRight = pygame.transform.scale(self.trasferelloRight, (self.surfRight.get_rect().width, self.surfRight.get_rect().height))

        self.surfNames.blit(self.trasferelloNames, (0,0))
        self.surfMenus.blit(self.trasferelloMenus, (0,0))
        self.surfBottom.blit(self.trasferelloBottom, (0,0))
        self.surfRight.blit(self.trasferelloRight, (0,0))

        self.surf.blit(self.surfNames, (0, g.TOP_UI_HEIGHT))
        self.surf.blit(self.surfMenus, (0, 0))
        self.surf.blit(self.surfBottom, (g.LEFT_UI_WIDTH, g.SCREEN_HEIGHT - g.BOTTOM_UI_HEIGHT))
        self.surf.blit(self.surfRight, (g.SCREEN_WIDTH - g.RIGHT_UI_WIDTH, g.TOP_UI_HEIGHT))

    def update(self, player, selectedTurret):

        self.surfNames.blit(self.trasferelloNames, (0,0))

        self.FONT.render_to(self.surfNames, (10, self.surfNames.get_rect().height / 2 + 100), f'Punti: {player.score}', (0, 0, 0))
        self.FONT.render_to(self.surfNames, (10, self.surfNames.get_rect().height / 2 + 120), f'Cazzi: {player.cazziatoni}', (0, 0, 0))

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

        self.surfNames.blit(self.bluTurret, (10, self.surfNames.get_rect().height / 2 + 150))
        self.surfNames.blit(self.redTurret, (30, self.surfNames.get_rect().height / 2 + 150))
        self.surfNames.blit(self.violetTurret, (50, self.surfNames.get_rect().height / 2 + 150))

        self.surf.blit(self.surfNames, (0, g.TOP_UI_HEIGHT))
        self.surf.blit(self.surfMenus, (0, 0))
        self.surf.blit(self.surfBottom, (g.LEFT_UI_WIDTH, g.SCREEN_HEIGHT - g.BOTTOM_UI_HEIGHT))
        self.surf.blit(self.surfRight, (g.SCREEN_WIDTH - g.RIGHT_UI_WIDTH, g.TOP_UI_HEIGHT))