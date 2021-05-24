# Import the pygame module
import pygame
import numpy
from pygame.constants import K_SPACE

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768 
FPS = 60

currentFrame = 0

class Background(pygame.sprite.Sprite):

    def __init__(self):

        super(Background, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.colOffset = 0
        self.rows = 22
        self.cols = 28
        self.width = SCREEN_WIDTH / self.cols
        self.height = SCREEN_HEIGHT / self.rows
        self.matr = numpy.zeros((self.rows, self.cols))

    def update(self, frame):

        if frame == 0:
            self.colOffset -= self.width
            self.colOffset = self.colOffset % SCREEN_WIDTH
            print(self.colOffset)

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                color = (255, 255, 255)
                if (j % 7 == 0) or (j % 7 == 1):
                    color = (200, 200, 200)
                pygame.draw.rect(self.surf, color, (j * self.width, i * self.height, self.width - 1, self.height - 1))

class Activitiy(pygame.sprite.Sprite):

    def __init__(self):

        super(Background, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.colOffset = 0
        self.rows = 22
        self.cols = 28
        self.width = SCREEN_WIDTH / self.cols
        self.height = SCREEN_HEIGHT / self.rows
        self.matr = numpy.zeros((self.rows, self.cols))

    def update(self, frame):

        if frame == 0:
            self.colOffset -= self.width
            self.colOffset = self.colOffset % SCREEN_WIDTH
            print(self.colOffset)

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                color = (255, 255, 255)
                if (j % 7 == 0) or (j % 7 == 1):
                    color = (200, 200, 200)
                pygame.draw.rect(self.surf, color, (j * self.width, i * self.height, self.width - 1, self.height - 1))

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
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

    def update(self, pressed_keys, tick):

        # User inputs
        if (pressed_keys[ord('w')] or pressed_keys[K_SPACE]) and not self.justJumped:
            if self.rect.bottom == SCREEN_HEIGHT:
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

        if self.rect.left < 0:
            self.rect.left = 0
            self.velX = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.velX = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.velY = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velY = 0


# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()
bg = Background()
clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True

# Main loop
while running:

    dt = clock.tick(FPS)
    currentFrame = (currentFrame + 1) % FPS

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

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, dt)
    bg.update(currentFrame)

    # Draw the player on the screen
    screen.blit(bg.surf, (bg.colOffset, 0))
    screen.blit(bg.surf, (bg.colOffset - SCREEN_WIDTH, 0))
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()