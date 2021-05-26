# Import the pygame module
import pygame
import math
import globalvar as g
from player import Player
from background import Background
from ui import UI
from enemies import Enemies

from pygame.locals import (
    K_ESCAPE,
    K_RCTRL,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((g.SCREEN_WIDTH, g.SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
bg = Background()
player = Player(bg)
ui = UI(bg)
clock = pygame.time.Clock()
enemies = Enemies(bg, ui)

# Variable to keep the main loop running
running = True

newProj = False
projAim = (0, 0)
stopTime = False
selectedTurret = 0
GANTT = []

alphaTurret = None
bluTurret = pygame.image.load("sprites\\blu_turret.png").convert_alpha()
redTurret = pygame.image.load("sprites\\red_turret.png").convert_alpha()
violetTurret = pygame.image.load("sprites\\violet_turret.png").convert_alpha()

turretW = bluTurret.get_rect().width
turretH = bluTurret.get_rect().height

# Main loop
while running:

    dt = clock.tick(g.FPS)
    if not stopTime:
        g.currentFrame = (g.currentFrame + 1) % (g.FPS)
        if math.floor(g.currentFrame) == 0:
            g.currentFrame = 0

    mousePos = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))

    # for loop through the event queue
    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

            elif event.key == K_RCTRL:
                stopTime = not stopTime

            elif event.key == ord('1'):
                if selectedTurret == 1:
                    selectedTurret = 0
                else:
                    selectedTurret = 1
            elif event.key == ord('2'):
                if selectedTurret == 2:
                    selectedTurret = 0
                else:
                    selectedTurret = 2
            elif event.key == ord('3'):
                if selectedTurret == 3:
                    selectedTurret = 0
                else:
                    selectedTurret = 3

        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[2]:
                if selectedTurret != 0:
                    player.placeTurret(bg, mousePos[0], mousePos[1], selectedTurret - 1)
                else:
                    turretToRemove = []
                    for turret in player.turretList:
                        if turret.rect.collidepoint(mousePos[0], mousePos[1]):
                            turretToRemove.append(turret)
                    for turret in turretToRemove:
                        player.turretNumber[turret.type] -= 1
                        player.turretPrice[turret.type] = 4**(player.turretNumber[turret.type]) * 100
                        player.turretList.remove(turret)


    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, dt, enemies, bg)
    bg.update(g.currentFrame)
    ui.update(player, selectedTurret)
    enemies.updateAll(g.currentFrame, player)
    enemies.spawnAll(bg, player.score)

    if pygame.mouse.get_pressed()[0]:
        projAim = pygame.mouse.get_pos()
        player.shoot(projAim)


    # DRAW

    screen.blit(bg.surf, (bg.colOffset + bg.left, bg.top))
    screen.blit(bg.surf, (bg.colOffset - bg.width + bg.left, bg.top))

    for activity in enemies.GANTT:
        screen.blit(activity.surf, activity.rect)

    screen.blit(ui.surf, (0,0))

    for turret in player.turretList:
        screen.blit(turret.surf, turret.rect)

    for proj in player.projList:
        screen.blit(proj.surf, proj.rect)

    for turret in player.turretList:
        for proj in turret.projList:
            screen.blit(proj.surf, proj.rect)

    if selectedTurret != 0:

        if selectedTurret == 1:
            alphaTurret = bluTurret
        elif selectedTurret == 2:
            alphaTurret = redTurret
        elif selectedTurret == 3:
            alphaTurret = violetTurret

        alphaTurret.set_alpha(96)

        turretX = max(min(mousePos[0], bg.right - turretW / 2), bg.left + turretW / 2)
        screen.blit(alphaTurret, (turretX - turretW / 2 , bg.bottom - turretH))

    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()