import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

    screen.fill((0, 255, 0))


pygame.quit()