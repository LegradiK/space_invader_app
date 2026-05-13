import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_FONT

class DarkSide:
    ICON_SIZE = 54
    COLUMNS = 11
    droid = None
    darth_vader = None

    @classmethod
    def load_class_assets(cls):
        cls.droid = pygame.image.load("static/droid.png").convert_alpha()
        cls.droid = pygame.transform.scale(cls.droid, (cls.ICON_SIZE, cls.ICON_SIZE))
        cls.darth_vader = pygame.image.load("static/dark.png").convert_alpha()
        cls.darth_vader = pygame.transform.scale(cls.darth_vader, (cls.ICON_SIZE, cls.ICON_SIZE))

    def __init__(self, speed=5, rows=5):
        self.image = None
        self.fleet = []
        self.direction = 1
        self.drop_distance = 20
        self.speed = speed
        self.rows = rows

    def load_image(self):
        image = pygame.image.load("static/tie-fighter.png").convert_alpha()
        self.image = pygame.transform.scale(image, (DarkSide.ICON_SIZE, DarkSide.ICON_SIZE))
        self.build_fleet()

    def build_fleet(self):
        total_width = DarkSide.COLUMNS * DarkSide.ICON_SIZE
        start_x = (SCREEN_WIDTH - total_width) // 2
        for row in range(self.rows):
            for col in range(DarkSide.COLUMNS):
                x = start_x + col * DarkSide.ICON_SIZE
                y = 40 + row * DarkSide.ICON_SIZE
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
            for pos in self.fleet:
                pos[1] += self.drop_distance
            self.direction *= -1
        else:
            for pos in self.fleet:
                pos[0] += self.speed * self.direction

    def winning_message(self, screen, game_over):
        text_surface, _ = GAME_FONT.render("Dark Side Reigns", (188, 30, 34), size=52)
        gap = 10
        total_width = DarkSide.ICON_SIZE + gap + text_surface.get_width() + gap + DarkSide.ICON_SIZE
        start_x = SCREEN_WIDTH // 2 - total_width // 2
        center_y = (SCREEN_HEIGHT // 2 - DarkSide.ICON_SIZE // 2 - 40) if not game_over else (SCREEN_HEIGHT // 2 - DarkSide.ICON_SIZE // 2 - 240)

        screen.game_screen.blit(DarkSide.darth_vader, (start_x, center_y))
        screen.game_screen.blit(text_surface, (start_x + DarkSide.ICON_SIZE + gap, center_y + DarkSide.ICON_SIZE // 2 - text_surface.get_height() // 2))
        screen.game_screen.blit(DarkSide.droid, (start_x + DarkSide.ICON_SIZE + gap + text_surface.get_width() + gap, center_y))
        pygame.display.update()