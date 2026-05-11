import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from screen import GameScreen
from jedi import Jedi
from dark_side import DarkSide
from collision_detector import CollisionDetector

ICON_SIZE = 64

pygame.init()

pygame.display.set_caption('Star Wars - Jedi vs Dark side')

screen = GameScreen()
jedi = Jedi()
darkside = DarkSide()

GAME_FONT = pygame.freetype.Font("static/star-jedi-font/StarJedi-DGRW.ttf", 24)

droid = pygame.image.load("static/droid.png").convert_alpha()
droid = pygame.transform.scale(droid, (ICON_SIZE, ICON_SIZE))
darth_vader = pygame.image.load("static/dark.png").convert_alpha()
darth_vader = pygame.transform.scale(darth_vader, (ICON_SIZE, ICON_SIZE))
light_saber = pygame.image.load("static/light-saber.png").convert_alpha()
light_saber = pygame.transform.scale(light_saber, (ICON_SIZE, ICON_SIZE))
padme = pygame.image.load("static/padme.png").convert_alpha()
padme = pygame.transform.scale(padme, (ICON_SIZE, ICON_SIZE))
luke = pygame.image.load("static/luke.png").convert_alpha()
luke = pygame.transform.scale(luke, (ICON_SIZE, ICON_SIZE))

screen.load_image()
jedi.load_image()
darkside.load_image()
CollisionDetector.load_image()

pressed_keys = pygame.key.get_pressed()

score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    jedi.move(keys=keys)
    jedi.shoot()
    jedi.update_bullets()

    screen.draw()
    score_surface, rect = GAME_FONT.render(f"Score: {score}", (255, 232, 31), size=28)
    screen.game_screen.blit(score_surface, (SCREEN_WIDTH - score_surface.get_width() - 20, 10))

    jedi.draw(screen=screen.game_screen)
    darkside.draw(screen=screen.game_screen)
    CollisionDetector.draw_explosions(screen.game_screen)

    darkside.move()
    hits = CollisionDetector.check_bullet_hits(jedi, darkside)
    score += hits * 10

    if CollisionDetector.check_enemy_reached_player(jedi, darkside):
        text_surface, rect = GAME_FONT.render("Dark Side won", (188, 30, 34), size=52)
        
        # calculate total width: icon + gap + text + gap + icon
        gap = 10
        total_width = ICON_SIZE + gap + text_surface.get_width() + gap + ICON_SIZE
        start_x = SCREEN_WIDTH // 2 - total_width // 2
        center_y = SCREEN_HEIGHT // 2 - ICON_SIZE // 2

        screen.game_screen.blit(darth_vader, (start_x, center_y))
        screen.game_screen.blit(text_surface, (start_x + ICON_SIZE + gap, center_y + ICON_SIZE // 2 - text_surface.get_height() // 2))
        screen.game_screen.blit(droid, (start_x + ICON_SIZE + gap + text_surface.get_width() + gap, center_y))
        
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    if len(darkside.fleet) == 0 and not CollisionDetector.check_enemy_reached_player(jedi, darkside):
        text_surface, rect = GAME_FONT.render("Jedi won!", (255, 232, 31), size=52)

        gap = 10
        total_width = ICON_SIZE + gap + text_surface.get_width() + gap + ICON_SIZE
        start_x = SCREEN_WIDTH // 2 - total_width // 2
        center_y = SCREEN_HEIGHT // 2 - ICON_SIZE // 2

        screen.game_screen.blit(luke, (start_x, center_y))
        screen.game_screen.blit(text_surface, (start_x + ICON_SIZE + gap, center_y + ICON_SIZE // 2 - text_surface.get_height() // 2))
        screen.game_screen.blit(padme, (start_x + ICON_SIZE + gap + text_surface.get_width() + gap, center_y))

        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()
    screen.clock.tick(60)

pygame.quit()