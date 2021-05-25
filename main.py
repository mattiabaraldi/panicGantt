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
ui = UI()
clock = pygame.time.Clock()
enemies = Enemies(bg)

# Variable to keep the main loop running
running = True

newProj = False
projAim = (0, 0)
stopTime = False
GANTT = []

# Main loop
while running:

    dt = clock.tick(g.FPS)
    if not stopTime:
        g.currentFrame = (g.currentFrame + 1) % (0.5 * g.FPS)
        if math.floor(g.currentFrame) == 0:
            g.currentFrame = 0

    screen.fill((0, 0, 0))

    # for loop through the event queue
    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RCTRL:
                stopTime = not stopTime

        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     ROBBA CON MOUSE PREMUTO

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, dt, enemies)
    bg.update(g.currentFrame)
    ui.update(player)
    enemies.updateAll(g.currentFrame, player)
    enemies.spawnAll(bg)

    if pygame.mouse.get_pressed()[0]:
        projAim = pygame.mouse.get_pos()
        player.shoot(projAim)


    # DRAW

    screen.blit(bg.surf, (bg.colOffset + bg.left, bg.top))
    screen.blit(bg.surf, (bg.colOffset - bg.width + bg.left, bg.top))

    for activity in enemies.GANTT:
        screen.blit(activity.surf, activity.rect)

    screen.blit(ui.surf, (0,0))

    for proj in player.projList:
        screen.blit(proj.surf, proj.rect)

    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()