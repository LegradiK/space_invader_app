import pygame

class CollisionDetector:
    explosion_image = None
    explosions = []  # list of [x, y, start_time]
    EXPLOSION_DURATION = 110  # milliseconds

    @staticmethod
    def load_image():
        image = pygame.image.load("static/explode.png").convert_alpha()
        CollisionDetector.explosion_image = pygame.transform.scale(image, (64, 64))

    @staticmethod
    def check_bullet_hits(jedi, dark_side):
        hits = 0
        bullets_to_remove = []
        enemies_to_remove = []

        for bullet in jedi.bullets:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], 4, 12)
            for enemy in dark_side.fleet:
                enemy_rect = pygame.Rect(enemy[0], enemy[1], dark_side.ICON_SIZE, dark_side.ICON_SIZE)
                if bullet_rect.colliderect(enemy_rect):
                    bullets_to_remove.append(bullet)
                    enemies_to_remove.append(enemy)
                    # record explosion at enemy position
                    CollisionDetector.explosions.append([enemy[0], enemy[1], pygame.time.get_ticks()])
                    hits += 1
                    break

        jedi.bullets = [b for b in jedi.bullets if b not in bullets_to_remove]
        dark_side.fleet = [e for e in dark_side.fleet if e not in enemies_to_remove]
        return hits
    
    @staticmethod
    def draw_explosions(screen):
        now = pygame.time.get_ticks()
        # keep only explosions still within duration
        CollisionDetector.explosions = [
            e for e in CollisionDetector.explosions
            if now - e[2] < CollisionDetector.EXPLOSION_DURATION
        ]
        for x, y, _ in CollisionDetector.explosions:
            screen.blit(CollisionDetector.explosion_image, (x, y))

    @staticmethod
    def check_enemy_reached_player(jedi, dark_side):
        """Returns True if an enemy reaches the player's row — game over."""
        for enemy in dark_side.fleet:
            if enemy[1] + dark_side.ICON_SIZE >= jedi.y:
                return True
        return False

    @staticmethod
    def check_player_hit(jedi, dark_side):
        """For later — enemy bullets hitting the Jedi."""
        player_rect = pygame.Rect(jedi.x, jedi.y, jedi.ICON_SIZE, jedi.ICON_SIZE)
        for bullet in dark_side.bullets:  # when you add enemy shooting
            bullet_rect = pygame.Rect(bullet[0], bullet[1], 4, 12)
            if bullet_rect.colliderect(player_rect):
                return True
        return False