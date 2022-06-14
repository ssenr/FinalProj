import pygame
from settings import * 

# pygame.sprite.Sprite for inheritance
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, invisibleSprites):
        # initiate class
        super().__init__(groups)
        self.image = pygame.image.load(testGirlImgPath).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        
        # X, Y 2D Vector
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.invisibleSprites = invisibleSprites
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        # X Movement
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
            
        # Y Movement
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
    def plrMove(self, speed):
        # Convert/Normalize to unit vector
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * speed
        self.collide("X")
        self.hitbox.y += self.direction.y * speed
        self.collide("Y")
        # Center Sprite about Hitbox Center
        self.rect.center = self.hitbox.center
        
    def collide(self, check):
        # Check for X Collisions
        # Hitbox based collisions 
        if check == "X":
            for sprite in self.invisibleSprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right based on var multiplied by speed [delta time later]
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        # Check for Y Collisions
        if check == "Y":
            for sprite in self.invisibleSprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
        
    def update(self):
        self.input()
        self.plrMove(self.speed)