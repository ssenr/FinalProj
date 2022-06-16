# create a sprite based on every sprite given
# we have a spritetpye which used to matter but now not so much
# for every bound change the rect (so collisions are less or more frequent)
# mainly use this to help with clipping issues, with the downside that enemies may get stuck on a tile if the vector direction crosses it
# make a rect of the sprite image and make its top left equal to the position of the screen that is passed in the nested for loop in levels.py

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