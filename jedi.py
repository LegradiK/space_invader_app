import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT  

class Jedi:
    ICON_SIZE = 64
    SPEED = 5

    def __init__(self):
        self.image = None
        self.x = SCREEN_WIDTH // 2 - Jedi.ICON_SIZE // 2
        self.y = SCREEN_HEIGHT - Jedi.ICON_SIZE - 10

    def load_image(self):
        # load and resize player (jedi)
        image = pygame.image.load("static/star-fighter.png").convert_alpha()
        self.image = pygame.transform.scale(image, (Jedi.ICON_SIZE, Jedi.ICON_SIZE))

    def move(self, keys):
        # movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            jedi_x -= Jedi.SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            jedi_x += Jedi.SPEED
         # keep jedi within screen bounds
        jedi_x = max(0, min(self.x, SCREEN_WIDTH - Jedi.ICON_SIZE))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))