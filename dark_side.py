import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class DarkSide:
    ICON_SIZE = 54
    ROWS = 5
    COLUMNS = 11
    SPEED = 5

    def __init__(self):
        self.image = None
        self.fleet = []

    def load_image(self):
        # load and resize enemy (dark side)
        image = pygame.image.load("static/tie-fighter.png").convert_alpha()
        self.image = pygame.transform.scale(image, (DarkSide.ICON_SIZE, DarkSide.ICON_SIZE_HEIGHT))
        self.build_fleet()
    
    def build_fleet(self):
        total_width = DarkSide.COLUMNS * (DarkSide.ICON_SIZE)
        start_x = (SCREEN_WIDTH - total_width) // 2

        for row in range(DarkSide.ROWS):
            for col in range(DarkSide.COLUMNS):
                x = start_x + col * (DarkSide.ICON_SIZE)
                y = 20 + row * (DarkSide.ICON_SIZE)
                self.fleet.append([x, y])

    def draw(self, screen):
        for x, y in self.fleet:
            screen.blit(self.image, (x, y))
    
    def move(self):
        # not to exceed side
        self.x = max(0, min(self.x, SCREEN_WIDTH - DarkSide.ICON_SIZE))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - DarkSide.ICON_SIZE))