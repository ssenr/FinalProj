import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.frameIndex = 0
        self.animationSpeed = 0.5
        self.direction = pygame.math.Vector2()
        
    def plrMove(self, speed, deltaTime = 1):
        # Convert/Normalize to unit vector
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * (speed * deltaTime)
        self.collide("X")
        self.hitbox.y += self.direction.y * (speed * deltaTime)
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