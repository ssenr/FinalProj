import pygame
from settings import * 

# pygame.sprite.Sprite for inheritance
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        # initiate class
        super().__init__(groups)
        self.image = pygame.image.load(testGirlImgPath).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)