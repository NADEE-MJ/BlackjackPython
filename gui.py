import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 255, 0))
    image = pygame.transform.scale(pygame.image.load("Cards/2C.png"), (75, 75))
    screen.blit(image, (50, 50))
    pygame.display.flip()
    
pygame.quit()