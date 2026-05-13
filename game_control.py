import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_FONT
from jedi import Jedi
from dark_side import DarkSide
from dark_side_hard import DarkSideHard
from collision_detector import CollisionDetector

ICON_SIZE_SMALL = 24

def wait_for_replay(screen, game_over=False):
    lines = [
        "A long time ago in a galaxy far, far away....",
        "Another chapter has come to an end.",
        "But the journey continues.",
        "",
        "Press SPACE to begin your adventure once more."
    ]

    if game_over:
        y_offset = SCREEN_HEIGHT // 2 - 90
    else:
        y_offset = SCREEN_HEIGHT // 2 - 20

    line_spacing = 40

    for i, line in enumerate(lines):
        text_surface, _ = GAME_FONT.render(line, (255, 232, 31), size=24)
        x = SCREEN_WIDTH // 2 - text_surface.get_width() // 2
        y = y_offset + i * line_spacing
        screen.game_screen.blit(text_surface, (x, y))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.draw()
                    lines = [
                        "Your journey restarts",
                        "in a galaxy far, far away..."
                    ]
                    y_offset = SCREEN_HEIGHT // 2 - 100
                    line_spacing = 40
                    for i, line in enumerate(lines):
                        starting_msg, _ = GAME_FONT.render(line, (255, 232, 31), size=34)
                        x = SCREEN_WIDTH // 2 - starting_msg.get_width() // 2
                        y = y_offset + i * line_spacing
                        screen.game_screen.blit(starting_msg, (x, y))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    return True


def play_round(screen, jedi, darkside, light_saber, life_surface, life_num, score, clock):
    CollisionDetector.load_image()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return score, life_num, 'quit'

        keys = pygame.key.get_pressed()
        jedi.move(keys=keys)
        jedi.shoot()
        jedi.update_bullets()

        screen.draw()

        score_surface, _ = GAME_FONT.render(f"Score: {score}", (255, 232, 31), size=28)
        screen.game_screen.blit(score_surface, (SCREEN_WIDTH - score_surface.get_width() - 20, 10))

        screen.game_screen.blit(life_surface, (10, 10))
        for i in range(life_num):
            screen.game_screen.blit(light_saber, (life_surface.get_width() + 5 + i * ICON_SIZE_SMALL, 10))

        jedi.draw(screen=screen.game_screen)
        darkside.draw(screen=screen.game_screen)
        CollisionDetector.draw_explosions(screen.game_screen)

        darkside.move()

        # Hard mode: enemy shoots back
        if hasattr(darkside, 'shoot'):
            darkside.shoot()
            darkside.update_bullets()

        hits = CollisionDetector.check_bullet_hits(jedi, darkside)
        score += hits * 10

        if CollisionDetector.check_enemy_reached_player(jedi, darkside):
            life_num -= 1

            pygame.draw.rect(screen.game_screen, (0, 0, 0), (life_surface.get_width(), 0, 3 * 28, 48))
            for i in range(life_num):
                screen.game_screen.blit(light_saber, (life_surface.get_width() + 5 + i * ICON_SIZE_SMALL, 10))

            if life_num > 0:
                darkside.winning_message(screen, game_over=False)
                lines = [
                    f"{life_num} life remains... ",
                    "The galaxy still needs you."
                ]
                for i, line in enumerate(lines):
                    msg, _ = GAME_FONT.render(line, (255, 232, 31), size=32)
                    x = SCREEN_WIDTH // 2 - msg.get_width() // 2
                    y = SCREEN_HEIGHT // 2 + 10 + i * 40
                    screen.game_screen.blit(msg, (x, y))
                pygame.display.update()
                pygame.time.wait(3000)
            else:
                darkside.winning_message(screen, game_over=True)
                game_over_msg, _ = GAME_FONT.render("Game Over!", (188, 30, 34), size=52)
                screen.game_screen.blit(game_over_msg, (SCREEN_WIDTH // 2 - game_over_msg.get_width() // 2, SCREEN_HEIGHT // 2 - 200))
                death_msg, _ = GAME_FONT.render("DEAD", (188, 30, 34), size=28)
                screen.game_screen.blit(death_msg, (life_surface.get_width() + 5, 10))
                pygame.display.update()

            return score, life_num, 'life_lost'

        if len(darkside.fleet) == 0:
            jedi.winning_message(screen)
            pygame.display.update()
            pygame.time.wait(3000)
            return score, life_num, 'jedi_won'

        pygame.display.update()
        clock.tick(60)


def play_game(screen, light_saber, life_surface, clock, difficulty):
    while True:
        score = 0
        life_num = 3

        while life_num > 0:
            jedi = Jedi()
            if difficulty['mode'] == 'hard':
                darkside = DarkSideHard()
            else:
                darkside = DarkSide(speed=difficulty['speed'], rows=difficulty['rows'])
            jedi.load_image()
            darkside.load_image()

            score, life_num, result = play_round(screen, jedi, darkside, light_saber, life_surface, life_num, score, clock)
            if result == 'quit':
                return

            if result == 'jedi_won':
                if not wait_for_replay(screen):
                    return
                break

            if life_num <= 0:
                if not wait_for_replay(screen, game_over=True):
                    return