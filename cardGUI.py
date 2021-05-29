import pygame
from pygame.constants import K_SPACE

class cardGUI(pygame.sprite.Sprite):
    def __init__(self, cardName):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Cards/%s.png"%(cardName)), (131, 200))
        self.surf = pygame.Surface((131,200))
        self.rect = self.surf.get_rect(center = (300, 300))

    def update(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_SPACE]:
            return True
             
    def draw(self, surface, distance):
        self.rect = self.surf.get_rect(center = (distance, 300))
        surface.blit(self.image, self.rect)