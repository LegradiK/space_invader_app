import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_FONT

class Jedi:
    ICON_SIZE = 64
    SPEED = 5
    BULLET_SPEED = 3
    BULLET_COOLDOWN = 900   

    luke = None
    padme = None

    @classmethod
    def load_class_assets(cls):
        """Call once after pygame.init() to load shared class-level images."""
        cls.padme = pygame.image.load("static/padme.png").convert_alpha()
        cls.padme = pygame.transform.scale(cls.padme, (Jedi.ICON_SIZE, Jedi.ICON_SIZE))
        cls.luke = pygame.image.load("static/luke.png").convert_alpha()
        cls.luke = pygame.transform.scale(cls.luke, (Jedi.ICON_SIZE, Jedi.ICON_SIZE))

    def __init__(self):
        self.image = None
        self.x = SCREEN_WIDTH // 2 - Jedi.ICON_SIZE // 2
        self.y = SCREEN_HEIGHT - Jedi.ICON_SIZE - 10
        self.bullets = []
        self.last_shot = 0

    def load_image(self):
        # load and resize player (jedi)
        image = pygame.image.load("static/star-fighter.png").convert_alpha()
        self.image = pygame.transform.scale(image, (Jedi.ICON_SIZE, Jedi.ICON_SIZE))

    def move(self, keys):
        # movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= Jedi.SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += Jedi.SPEED
         # keep jedi within screen bounds
        self.x = max(0, min(self.x, SCREEN_WIDTH - Jedi.ICON_SIZE))


    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= Jedi.BULLET_COOLDOWN:
            bullet_x = self.x + Jedi.ICON_SIZE // 2
            bullet_y = self.y
            self.bullets.append([bullet_x, bullet_y])
            self.last_shot = now
        
    def update_bullets(self):
        for bullet in self.bullets:
            bullet[1] -= Jedi.BULLET_SPEED
        
        # remove bullets that go off the top of the screen
        self.bullets = [b for b in self.bullets if b[1] > 0]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            pygame.draw.rect(screen, (255, 255, 0), (bullet[0], bullet[1], 4, 12))

    def winning_message(self, screen):
        text_surface, _ = GAME_FONT.render("Jedi won!", (255, 232, 31), size=52)
        gap = 10
        total_width = Jedi.ICON_SIZE + gap + text_surface.get_width() + gap + Jedi.ICON_SIZE
        start_x = SCREEN_WIDTH // 2 - total_width // 2
        center_y = SCREEN_HEIGHT // 2 - Jedi.ICON_SIZE // 2

        text_surface2, _ = GAME_FONT.render("Play again? Press 'space'..", (255, 232, 31), size=52)

        screen.game_screen.blit(Jedi.luke, (start_x, center_y))
        screen.game_screen.blit(
            text_surface,
            (start_x + Jedi.ICON_SIZE + gap, center_y + Jedi.ICON_SIZE // 2 - text_surface.get_height() // 2)
        )
        screen.game_screen.blit(
            Jedi.padme,
            (start_x + Jedi.ICON_SIZE + gap + text_surface.get_width() + gap, center_y)
        )
        screen.game_screen.blit(
            text_surface2,
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - text_surface.get_height())
        )

