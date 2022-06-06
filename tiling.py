import pygame
from settings import * 

# pygame.sprite.Sprite for inheritance
# Animate
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        # initiate class
        super().__init__(groups)
        self.image = pygame.image.load(testPostImgPath).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)