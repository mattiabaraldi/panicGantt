# Import the pygame module
import pygame
import numpy
import globalvar as g
from player import Player
from background import Background
from activity import Activity
from ui import UI
import globalvar as g

from pygame.locals import (
    K_ESCAPE,
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

# Variable to keep the main loop running
running = True

newProj = False
projAim = (0, 0)
GANTT = []

# Main loop
while running:

    dt = clock.tick(g.FPS)
    g.currentFrame = (g.currentFrame + 1) % g.FPS

    screen.fill((0, 0, 0))

    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False

        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                projAim = pygame.mouse.get_pos()
                player.shoot(projAim)
            if pygame.mouse.get_pressed()[2]:
                GANTT.append(Activity(bg))

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, dt)
    bg.update(g.currentFrame)

    # Draw the player on the screen
    screen.blit(bg.surf, (bg.colOffset + bg.left, bg.top))
    screen.blit(bg.surf, (bg.colOffset - bg.width + bg.top, bg.top))

    screen.blit(ui.surfNames, (0, g.TOP_UI_HEIGHT))
    screen.blit(ui.surfMenus, (0, 0))
    screen.blit(ui.surfBottom, (0, g.SCREEN_HEIGHT - g.BOTTOM_UI_HEIGHT))
    screen.blit(ui.surfRight, (g.SCREEN_WIDTH - g.RIGHT_UI_WIDTH, g.TOP_UI_HEIGHT))

    for proj in player.projList:
        screen.blit(proj.surf, proj.rect)
    
    for activity in GANTT:
        screen.blit(activity.surf, activity.rect)

    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()