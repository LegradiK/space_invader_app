import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_FONT
from screen import GameScreen
from jedi import Jedi
from dark_side import DarkSide
from collision_detector import CollisionDetector

ICON_SIZE = 64
ICON_SIZE_SMALL = 24

def wait_for_replay(screen):
    """Shows a message and waits for SPACE or QUIT. Returns True to replay, False to quit."""
    replay_msg, _ = GAME_FONT.render("Press SPACE to play again or ESC to quit", (255, 232, 31), size=28)
    screen.game_screen.blit(replay_msg, (SCREEN_WIDTH // 2 - replay_msg.get_width() // 2, SCREEN_HEIGHT // 2 + 80))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False

def play_round(screen, jedi, darkside, light_saber, life_surface, life_num, score):
    
    CollisionDetector.load_image()

    jedi_alive = True

    while jedi_alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return score, life_num, 'quit'

        keys = pygame.key.get_pressed()
        jedi.move(keys=keys)
        jedi.shoot()
        jedi.update_bullets()

        screen.draw()

        # Draw score
        score_surface, _ = GAME_FONT.render(f"Score: {score}", (255, 232, 31), size=28)
        screen.game_screen.blit(score_surface, (SCREEN_WIDTH - score_surface.get_width() - 20, 10))

        # Draw lives
        screen.game_screen.blit(life_surface, (10, 10))
        for i in range(life_num):
            screen.game_screen.blit(light_saber, (life_surface.get_width() + 5 + i * ICON_SIZE_SMALL, 10)) 

        jedi.draw(screen=screen.game_screen)
        darkside.draw(screen=screen.game_screen)
        CollisionDetector.draw_explosions(screen.game_screen)

        darkside.move()

        hits = CollisionDetector.check_bullet_hits(jedi, darkside)
        score += hits * 10

        if CollisionDetector.check_enemy_reached_player(jedi, darkside):
            darkside.winning_message(screen) 
            life_num -= 1

            pygame.draw.rect(screen.game_screen, (0, 0, 0), (life_surface.get_width(), 0, 3 * 28, 48))
            for i in range(life_num):
                screen.game_screen.blit(light_saber, (life_surface.get_width() + 5 + i * ICON_SIZE_SMALL, 10))

            if life_num > 0:
                msg, _ = GAME_FONT.render(f"You have {life_num} life left, keep fighting!", (255, 232, 31), size=32)
                screen.game_screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
                pygame.display.update()
                pygame.time.wait(3000)
            else:
                game_over_msg, _ = GAME_FONT.render("Game Over!", (188, 30, 34), size=52)
                screen.game_screen.blit(game_over_msg, (SCREEN_WIDTH // 2 - game_over_msg.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
                death_msg, _ = GAME_FONT.render("DEAD", (188, 30, 34), size=28)
                screen.game_screen.blit(death_msg, (life_surface.get_width() + 5 + i * ICON_SIZE_SMALL, 10))
                pygame.display.update()
                pygame.time.wait(3000)
            
            return score, life_num, 'life_lost'

        if len(darkside.fleet) == 0 and not CollisionDetector.check_enemy_reached_player(jedi, darkside):
            jedi.winning_message(screen)
            pygame.display.update()
            pygame.time.wait(3000)
            
            return score, life_num, 'jedi_won'

        pygame.display.update()
        clock.tick(60)

    return score, life_num, 'quit'


def play_game(screen, light_saber, life_surface):
    while True:
        score = 0
        life_num = 3

        while life_num > 0:
            jedi = Jedi()
            darkside = DarkSide()
            jedi.load_image()
            darkside.load_image()

            score, life_num, result = play_round(screen, jedi, darkside, light_saber, life_surface, life_num, score)

            if result == 'quit' or result == 'jedi_won':
                if not wait_for_replay(screen):
                    return
                break

        if life_num <= 0:
            darkside.winning_message(screen)
            if not wait_for_replay(screen):
                return
            pygame.display.update()
            pygame.time.wait(1000)

# main

pygame.init()
clock = pygame.time.Clock()
pygame.freetype.init()
pygame.display.set_caption('Star Wars - Jedi vs Dark side')
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # ← temporary test line

DarkSide.load_class_assets()
Jedi.load_class_assets()

screen = GameScreen()
screen.load_image()

light_saber = pygame.image.load("static/light-saber.png").convert_alpha()
light_saber = pygame.transform.scale(light_saber, (ICON_SIZE_SMALL, ICON_SIZE_SMALL))

life_surface, _ = GAME_FONT.render("Life: ", (255, 232, 31), size=28)

play_game(screen, light_saber, life_surface)

pygame.quit()