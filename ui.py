import globalvar as g
import pygame

class UI(pygame.sprite.Sprite):

    def __init__(self):

        super(UI, self).__init__()
        
        self.surfNames = pygame.Surface((g.LEFT_UI_WIDTH, g.SCREEN_HEIGHT - g.TOP_UI_HEIGHT - g.BOTTOM_UI_HEIGHT))
        self.surfMenus = pygame.Surface((g.SCREEN_WIDTH, g.TOP_UI_HEIGHT))
        self.surfBottom = pygame.Surface((g.SCREEN_WIDTH, g.BOTTOM_UI_HEIGHT))
        self.surfRight = pygame.Surface((g.RIGHT_UI_WIDTH, g.SCREEN_HEIGHT - g.TOP_UI_HEIGHT))

        self.surfNames.fill((150, 150, 150))
        self.surfMenus.fill((160, 160, 160))
        self.surfBottom.fill((170, 170, 170))
        self.surfRight.fill((180, 180, 180))