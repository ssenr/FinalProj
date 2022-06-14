import pygame
from settings import * 

# pygame.sprite.Sprite for inheritance
# Animate
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups, spriteType, surf = pygame.Surface((tileSize,tileSize))):
        # initiate class
        super().__init__(groups)
        self.spriteType = spriteType
        self.image = surf
        
        #Offset Config
        if spriteType == 'trees':
            self.rect = self.image.get_rect(topleft = pos)
            self.hitbox = self.rect.inflate(-30,0)
        else:
            self.rect = self.image.get_rect(topleft = pos)
            self.hitbox = self.rect.inflate(0,25)
        
        # Making hitbox for tile smaller
        # self.hitbox = self.rect.inflate(0,25) 