import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_FONT
from screen import GameScreen
from jedi import Jedi
from dark_side import DarkSide
from collision_detector import CollisionDetector

ICON_SIZE = 64

# pygame.init()
# pygame.freetype.init()
# pygame.display.set_caption('Star Wars - Jedi vs Dark side')

# DarkSide.load_class_assets()  # ← must be called after pygame.init()

# screen = GameScreen()

pygame.init()
pygame.freetype.init()
pygame.display.set_caption('Star Wars - Jedi vs Dark side')
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # ← temporary test line

DarkSide.load_class_assets()
screen = GameScreen()

jedi = Jedi()
darkside = DarkSide()

light_saber = pygame.image.load("static/light-saber.png").convert_alpha()
light_saber = pygame.transform.scale(light_saber, (ICON_SIZE, ICON_SIZE))

screen.load_image()
jedi.load_image()
darkside.load_image()
CollisionDetector.load_image()

score = 0
life_num = 3
life_images = [light_saber] * life_num  # ← now a proper list of surfaces

running = True
while running:
    if life_num > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        jedi.move(keys=keys)
        jedi.shoot()
        jedi.update_bullets()

        screen.draw()

        # Draw score
        score_surface, rect = GAME_FONT.render(f"Score: {score}", (255, 232, 31), size=28)
        screen.game_screen.blit(score_surface, (SCREEN_WIDTH - score_surface.get_width() - 20, 10))

        # Draw lives
        life_surface, rect = GAME_FONT.render(f"Life: {life_num}", (255, 232, 31), size=28)  # ← life_num
        screen.game_screen.blit(life_surface, (10, 10))  # ← fixed missing closing paren

        jedi.draw(screen=screen.game_screen)
        darkside.draw(screen=screen.game_screen)
        CollisionDetector.draw_explosions(screen.game_screen)

        darkside.move()

        hits = CollisionDetector.check_bullet_hits(jedi, darkside)
        score += hits * 10

        if CollisionDetector.check_enemy_reached_player(jedi, darkside):
            darkside.winning_message(screen) 
            life_num -= 1

        if len(darkside.fleet) == 0 and not CollisionDetector.check_enemy_reached_player(jedi, darkside):

            pygame.display.update()
            pygame.time.wait(3000)
            running = False

        pygame.display.update()

    else:
        print("Game Over")
        running = False  # ← stops the loop cleanly instead of hanging

pygame.quit()