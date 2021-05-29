import pygame, sys
from pygame.constants import K_SPACE

pygame.init()

#fps settings
FPS = 60
FramePerSec = pygame.time.Clock()

#screen settings
screen = pygame.display.set_mode([750, 750])
pygame.display.set_caption("Blackjack")
font = pygame.font.Font(pygame.font.get_default_font(), 20)

#colors
black = (0, 0, 0)
green = (0, 128, 0)

class cardGUI(pygame.sprite.Sprite):
    def __init__(self, cardName):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Cards/%s.png"%(cardName)), (131, 200))
        self.surf = pygame.Surface((131,200))
        self.rect = self.surf.get_rect()

    # def update(self):
    #     pressed_key = pygame.key.get_pressed()
    #     if pressed_key[K_SPACE]:
            

    def draw(self, surface):
        surface.blit(self.image, self.rect)



text = font.render("Dealer's Cards", True, black)

while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(green)

    testCard = cardGUI("2C")
    testCard.draw(screen)

    screen.blit(text, (50, 25))

    pygame.display.update()
    FramePerSec.tick(FPS)