import globalvar as g
import pygame
import pygame.freetype

class UI(pygame.sprite.Sprite):

    def __init__(self):

        super(UI, self).__init__()

        self.surf = pygame.Surface((g.SCREEN_WIDTH, g.SCREEN_HEIGHT), pygame.SRCALPHA, 32)
        self.surf = self.surf.convert_alpha()
        
        self.surfNames = pygame.Surface((g.LEFT_UI_WIDTH, g.SCREEN_HEIGHT - g.TOP_UI_HEIGHT - g.BOTTOM_UI_HEIGHT))
        self.surfMenus = pygame.Surface((g.SCREEN_WIDTH, g.TOP_UI_HEIGHT))
        self.surfBottom = pygame.Surface((g.SCREEN_WIDTH, g.BOTTOM_UI_HEIGHT))
        self.surfRight = pygame.Surface((g.RIGHT_UI_WIDTH, g.SCREEN_HEIGHT - g.TOP_UI_HEIGHT))

        self.FONT = pygame.freetype.SysFont("Lucon.ttf", 20)

        self.surfNames.fill((150, 150, 150))
        self.surfMenus.fill((160, 160, 160))
        self.surfBottom.fill((170, 170, 170))
        self.surfRight.fill((180, 180, 180))

        self.surf.blit(self.surfNames, (0, g.TOP_UI_HEIGHT))
        self.surf.blit(self.surfMenus, (0, 0))
        self.surf.blit(self.surfBottom, (0, g.SCREEN_HEIGHT - g.BOTTOM_UI_HEIGHT))
        self.surf.blit(self.surfRight, (g.SCREEN_WIDTH - g.RIGHT_UI_WIDTH, g.TOP_UI_HEIGHT))

    def update(self, frame):

        self.surf.blit(self.surfNames, (0, g.TOP_UI_HEIGHT))
        self.surf.blit(self.surfMenus, (0, 0))
        self.surf.blit(self.surfBottom, (0, g.SCREEN_HEIGHT - g.BOTTOM_UI_HEIGHT))
        self.surf.blit(self.surfRight, (g.SCREEN_WIDTH - g.RIGHT_UI_WIDTH, g.TOP_UI_HEIGHT))

        self.FONT.render_to(self.surf, (10, 10), f'{frame}', (0, 0, 0))