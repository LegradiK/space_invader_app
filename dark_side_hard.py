import pygame
import random
from config import SCREEN_HEIGHT
from dark_side import DarkSide

BULLET_SPEED = 5
SHOOT_INTERVAL_MS = 1500  # a random enemy fires every ~1.2 seconds

class DarkSideHard(DarkSide):
    bomber_image = None

    @classmethod
    def load_class_assets(cls):
        super().load_class_assets()
        img = pygame.image.load("static/tie-fighter.png").convert_alpha()
        cls.bomber_image = pygame.transform.scale(img, (DarkSide.ICON_SIZE, DarkSide.ICON_SIZE))

    def __init__(self):
        super().__init__(speed=2.5, rows=5)
        self.bullets = []           # each bullet: [x, y]
        self.last_shot_ms = 0

    def load_image(self):
        # Use bomber image instead of tie-fighter
        self.image = DarkSideHard.bomber_image
        self.build_fleet()

    def shoot(self):
        if not self.fleet:
            return
        now = pygame.time.get_ticks()
        if now - self.last_shot_ms > SHOOT_INTERVAL_MS:
            bottom_enemies = {}
            for pos in self.fleet:
                col = pos[0]
                if col not in bottom_enemies or pos[1] > bottom_enemies[col][1]:
                    bottom_enemies[col] = pos
            shooter = random.choice(list(bottom_enemies.values()))
            bullet_x = shooter[0] + DarkSide.ICON_SIZE // 2 - 3
            bullet_y = shooter[1] + DarkSide.ICON_SIZE
            self.bullets.append([bullet_x, bullet_y])
            self.last_shot_ms = now

    def update_bullets(self):
        for b in self.bullets:
            b[1] += BULLET_SPEED
        self.bullets = [b for b in self.bullets if b[1] < SCREEN_HEIGHT]

    def draw(self, screen):
        super().draw(screen)
        for bx, by in self.bullets:
            pygame.draw.rect(screen, (188, 30, 34), (bx, by, 6, 16), border_radius=3)

    def get_bullets(self):
        return self.bullets