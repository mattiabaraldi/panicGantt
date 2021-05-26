# Define constants for the screen width and height

SCREEN_WIDTH = 1680
SCREEN_HEIGHT = 1024
FPS = 60

TOP_UI_HEIGHT, BOTTOM_UI_HEIGHT = int((SCREEN_WIDTH / 18)), 16
LEFT_UI_WIDTH, RIGHT_UI_WIDTH = int((SCREEN_HEIGHT - TOP_UI_HEIGHT) / 5), 16

currentFrame = 0