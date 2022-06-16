import pygame
from math import sin

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.frameIndex = 0
        self.animationSpeed = 0.25
        self.direction = pygame.math.Vector2()
        
    def plrMove(self, speed):
        # Convert/Normalize to unit vector
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * (speed)
        self.collide("X")
        self.hitbox.y += self.direction.y * (speed)
        self.collide("Y")

        # Center Sprite about Hitbox Center
        self.rect.center = self.hitbox.center
    
    def collide(self, plane):
        # Check for X Collisions
        # Hitbox based collisions 
        if plane == "X":
            for sprite in self.invisibleSprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right based on var multiplied by speed [delta time later]
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        # Check for Y Collisions
        if plane == "Y":
            for sprite in self.invisibleSprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                                         
    def flicker(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else: 
            return 0