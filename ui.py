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

        self.FONT = pygame.freetype.SysFont("Lucon.ttf", 20)

        stickerSurface = pygame.image.load("sprites\\UI_names.png")
        stickerSurface = pygame.transform.scale(stickerSurface, (self.surfNames.get_rect().width, self.surfNames.get_rect().height))
        self.surfNames.blit(stickerSurface, (0,0))
        stickerSurface = pygame.image.load("sprites\\UI_top.png")
        stickerSurface = pygame.transform.scale(stickerSurface, (self.surfMenus.get_rect().width, self.surfMenus.get_rect().height))
        self.surfMenus.blit(stickerSurface, (0,0))
        stickerSurface = pygame.image.load("sprites\\UI_bottom.png")
        stickerSurface = pygame.transform.scale(stickerSurface, (self.surfBottom.get_rect().width, self.surfBottom.get_rect().height))
        self.surfBottom.blit(stickerSurface, (0,0))
        stickerSurface = pygame.image.load("sprites\\UI_right.png")
        stickerSurface = pygame.transform.scale(stickerSurface, (self.surfRight.get_rect().width, self.surfRight.get_rect().height))
        self.surfRight.blit(stickerSurface, (0,0))

        self.surf.blit(self.surfNames, (0, g.TOP_UI_HEIGHT))
        self.surf.blit(self.surfMenus, (0, 0))
        self.surf.blit(self.surfBottom, (g.LEFT_UI_WIDTH, g.SCREEN_HEIGHT - g.BOTTOM_UI_HEIGHT))
        self.surf.blit(self.surfRight, (g.SCREEN_WIDTH - g.RIGHT_UI_WIDTH, g.TOP_UI_HEIGHT))

    def update(self, frame):

        stickerSurface = pygame.image.load("sprites\\UI_names.png")
        stickerSurface = pygame.transform.scale(stickerSurface, (self.surfNames.get_rect().width, self.surfNames.get_rect().height))
        self.surfNames.blit(stickerSurface, (0,0))
        stickerSurface = pygame.image.load("sprites\\UI_top.png")
        stickerSurface = pygame.transform.scale(stickerSurface, (self.surfMenus.get_rect().width, self.surfMenus.get_rect().height))
        self.surfMenus.blit(stickerSurface, (0,0))
        stickerSurface = pygame.image.load("sprites\\UI_bottom.png")
        stickerSurface = pygame.transform.scale(stickerSurface, (self.surfBottom.get_rect().width, self.surfBottom.get_rect().height))
        self.surfBottom.blit(stickerSurface, (0,0))
        stickerSurface = pygame.image.load("sprites\\UI_right.png")
        stickerSurface = pygame.transform.scale(stickerSurface, (self.surfRight.get_rect().width, self.surfRight.get_rect().height))
        self.surfRight.blit(stickerSurface, (0,0))

        # self.FONT.render_to(self.surf, (10, 10), f'{frame}', (0, 0, 0))