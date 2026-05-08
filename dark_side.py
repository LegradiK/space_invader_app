import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class DarkSide:
    ICON_SIZE_WIDTH = 130
    ICON_SIZE_HEIGHT = 90

    def __init__(self):
        self.image = None
        self.x = SCREEN_WIDTH // 2 - DarkSide.ICON_SIZE_WIDTH // 2
        self.y = 10

    def load_image(self):
        # load and resize enemy (dark side)
        image = pygame.image.load("static/tie-fighter.png").convert_alpha()
        self.image = pygame.transform.scale(image, (DarkSide.ICON_SIZE_WIDTH, DarkSide.ICON_SIZE_HEIGHT))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


