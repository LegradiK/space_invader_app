import pygame

pygame.init()

# setting up screen
SCREEN_WIDTH = 860
SCREEN_HEIGHT = 950
game_screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))

# setting background pic
background_pic_path = "static/background-pic.jpg"
background_image = pygame.image.load(background_pic_path)
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
running = True

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    game_screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
