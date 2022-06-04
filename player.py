import pygame
from settings import * 

# pygame.sprite.Sprite for inheritance
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        # initiate class
        super().__init__(groups)
        self.image = pygame.image.load(testGirlImgPath).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        # X, Y 2D Vector
        self.direction = pygame.math.Vector2()
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_a]:
            self.direction.x = 1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        elif keys [pygame.K_d]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            self.direction.y = 0
    
    def update(self):
        self.input()