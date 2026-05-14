import pygame
import pygame.freetype

pygame.freetype.init()

SCREEN_WIDTH = 860
SCREEN_HEIGHT = 950
GAME_FONT = pygame.freetype.Font("static/star-jedi-font/StarJedi-DGRW.ttf", 24)

## For testing fonts
## to see how each letter look like
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Font Map Test")

# def show_font_map(surface, font):
#     chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
#     for i, ch in enumerate(chars):
#         x = (i % 10) * 80 + 20
#         y = (i // 10) * 60 + 20
#         font.render_to(surface, (x, y), ch, (255, 255, 255))

# # Draw once and keep window open
# screen.fill((0, 0, 0))
# show_font_map(screen, font=GAME_FONT)
# pygame.display.flip()

# # Keep window open until closed
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()