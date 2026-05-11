import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class DarkSide:
    ICON_SIZE = 54
    ROWS = 5
    COLUMNS = 11
    SPEED = 1.6

    def __init__(self):
        self.image = None
        self.fleet = []
        self.direction = 1        # 1 = right, -1 = left
        self.drop_distance = 20

    def load_image(self):
        # load and resize enemy (dark side)
        image = pygame.image.load("static/tie-fighter.png").convert_alpha()
        self.image = pygame.transform.scale(image, (DarkSide.ICON_SIZE, DarkSide.ICON_SIZE))
        self.build_fleet()
    
    def build_fleet(self):
        total_width = DarkSide.COLUMNS * (DarkSide.ICON_SIZE)
        start_x = (SCREEN_WIDTH - total_width) // 2

        for row in range(DarkSide.ROWS):
            for col in range(DarkSide.COLUMNS):
                x = start_x + col * (DarkSide.ICON_SIZE)
                y = 30 + row * (DarkSide.ICON_SIZE)
                self.fleet.append([x, y])

    def draw(self, screen):
        for x, y in self.fleet:
            screen.blit(self.image, (x, y))
    
    def move(self):
        hit_wall = False
        for pos in self.fleet:
            if pos[0] <= 0 and self.direction == -1:
                hit_wall = True
                break
            if pos[0] + DarkSide.ICON_SIZE >= SCREEN_WIDTH and self.direction == 1:
                hit_wall = True
                break

        if hit_wall:
            # Drop down and reverse direction
            for pos in self.fleet:
                pos[1] += self.drop_distance
            self.direction *= -1
        else:
            # Move horizontally
            for pos in self.fleet:
                pos[0] += DarkSide.SPEED * self.direction
