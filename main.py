import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_FONT
from screen import GameScreen
from jedi import Jedi
from dark_side import DarkSide
from game_control import play_game
from start_screen import show_start_screen

ICON_SIZE_SMALL = 24

pygame.init()
clock = pygame.time.Clock()
pygame.freetype.init()
pygame.display.set_caption('Star Wars - Jedi vs Dark side')
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

DarkSide.load_class_assets()
Jedi.load_class_assets()

screen = GameScreen()
screen.load_image()

light_saber = pygame.image.load("static/light-saber.png").convert_alpha()
light_saber = pygame.transform.scale(light_saber, (ICON_SIZE_SMALL, ICON_SIZE_SMALL))

life_surface, _ = GAME_FONT.render("Life: ", (255, 232, 31), size=28)

difficulty = show_start_screen(screen)
if difficulty:
    play_game(screen, light_saber, life_surface, clock, difficulty)

play_game(screen, light_saber, life_surface, clock)

pygame.quit()