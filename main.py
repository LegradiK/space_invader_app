import pygame
from screen import GameScreen
from jedi import Jedi
from dark_side import DarkSide


pygame.init()

screen = GameScreen()
jedi = Jedi()
darkside = DarkSide()

screen.load_image()
jedi.load_image()
darkside.load_image()

pressed_keys = pygame.key.get_pressed()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys:
        jedi.move(keys=keys)

    screen.draw()
    jedi.draw(screen=screen.game_screen)
    darkside.draw(screen=screen.game_screen)

    pygame.display.update()
    screen.clock.tick(60)

pygame.quit()