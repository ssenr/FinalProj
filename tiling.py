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
        
        match self.spriteType:
            case 'hard_boundary':
                self.rect = self.image.get_rect(topleft = pos)
                self.hitbox = self.rect.inflate(0,25)
            case 'wall_boundary':
                self.rect = self.image.get_rect(topleft = pos)
                self.hitbox = self.rect.inflate(0,-5)
            case 'pillar':
                self.rect = self.image.get_rect(topleft = (pos[0] + 5, pos[1]))
                self.hitbox = self.rect.inflate(0,-5)
            case _:
                self.rect = self.image.get_rect(topleft = pos)
                self.hitbox = self.rect.inflate(0,0)
        
        
        
        #Offset Config
        # Make with dictionary l8r
        # if spriteType == 'hard_boundary':
        #     self.rect = self.image.get_rect(topleft = pos)
        #     self.hitbox = self.rect.inflate(0,0)
        # elif spriteType == 'wall_boundary':
        #     self.rect = self.image.get_rect(topleft = pos)
        #     self.hitbox = self.rect.inflate(0,-5)
        # else:
        #     self.rect = self.image.get_rect(topleft = pos)
        #     self.hitbox = self.rect.inflate(0,0)
        
        # Making hitbox for tile smaller
        # self.hitbox = self.rect.inflate(0,25) 