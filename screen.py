import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class GameScreen:
    def __init__(self):
        # setting up screen
        self.game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image = None
        self.clock = pygame.time.Clock()

    def load_image(self):
        # setting background pic
        self.background_image = pygame.image.load("static/background-pic.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self):
        self.game_screen.blit(self.background_image, (0, 0))