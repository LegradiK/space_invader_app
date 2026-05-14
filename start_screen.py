import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_FONT

DIFFICULTIES = {
    'EASY':   {'speed': 3, 'rows': 3, 'mode': 'easy'},
    'MEDIUM': {'speed': 3, 'rows': 5, 'mode': 'medium'},
    'HARD':   {'speed': 3, 'rows': 5, 'mode': 'hard'},
}

def show_start_screen(screen):
    options = list(DIFFICULTIES.keys())
    selected = 1

    while True:
        screen.draw()

        title, _ = GAME_FONT.render("STAR WARS", (255, 232, 31), size=72)
        subtitle, _ = GAME_FONT.render("Jedi vs Dark Side", (255, 232, 31), size=32)
        screen.game_screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 80))
        screen.game_screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 170))

        instr1, _ = GAME_FONT.render("Select difficulty with left and right arrows", (180, 180, 180), size=22)
        instr2, _ = GAME_FONT.render("Press space or enter to start", (180, 180, 180), size=22)
        screen.game_screen.blit(instr1, (SCREEN_WIDTH // 2 - instr1.get_width() // 2, 250))
        screen.game_screen.blit(instr2, (SCREEN_WIDTH // 2 - instr2.get_width() // 2, 280))

        button_y = SCREEN_HEIGHT // 2 - 30
        button_w, button_h = 180, 60
        gap = 40
        total_w = len(options) * button_w + (len(options) - 1) * gap
        start_x = SCREEN_WIDTH // 2 - total_w // 2

        for i, label in enumerate(options):
            x = start_x + i * (button_w + gap)
            is_selected = i == selected
            color = (188, 30, 34) if is_selected else (40, 40, 40)
            border_color = (255, 232, 31) if is_selected else (120, 120, 120)
            pygame.draw.rect(screen.game_screen, color, (x, button_y, button_w, button_h), border_radius=8)
            pygame.draw.rect(screen.game_screen, border_color, (x, button_y, button_w, button_h), 2, border_radius=8)
            text, _ = GAME_FONT.render(label.lower(), (255, 255, 255), size=28)
            screen.game_screen.blit(text, (
                x + button_w // 2 - text.get_width() // 2,
                button_y + button_h // 2 - text.get_height() // 2
            ))

        desc_lines = {
            'easy':   ["3 rows of enemies"],
            'medium': ["5 rows of enemies"],
            'hard':   ["5 rows of enemies", "Tie Bombers that shoot"],
        }
        for j, line in enumerate(desc_lines[options[selected].lower()]):
            desc, _ = GAME_FONT.render(line, (200, 200, 200), size=22)
            screen.game_screen.blit(desc, (
                SCREEN_WIDTH // 2 - desc.get_width() // 2,
                button_y + button_h + 50 + j * 30
            ))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected = (selected - 1) % len(options)
                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % len(options)
                if event.key == pygame.K_SPACE:
                    return DIFFICULTIES[options[selected]]
                if event.key == pygame.K_ESCAPE:
                    return None