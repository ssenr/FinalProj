import pygame
from settings import * 
from scripts import * 

# pygame.sprite.Sprite for inheritance
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, invisibleSprites, attackInstance, endAttack):
        # initiate class
        super().__init__(groups)
        self.image = pygame.image.load(loadingFrame).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        
        # Anim Config
        self.plrAnims()
        self.status = 'up'
        self.frameIndex = 0
        self.animationSpeed = 0.5
        
        # X, Y 2D Vector
        self.direction = pygame.math.Vector2()
        self.speed = 125
        
        self.invisibleSprites = invisibleSprites
        
        self.attacking = False
        self.attackCooldown = 500
        self.attackTime = None
        self.attackInstance = attackInstance
        self.endAttack = endAttack

        # Stats
        self.stats = {
            'health': 70,
        }
        self.health = self.stats['health']
        self.kills = 0
        
        
        
    def plrAnims(self):
        animPath = "data/graphics/anim_mc/"
        self.animations = {
            # Run Keys
            'up': [],           # Done
            'dwn': [],          # Done   
            'lft': [],          # Done
            'rght': [],         # Done
            
            # Idle Keys
            'up_idle': [],      # Done
            'dwn_idle': [],     # Done
            'lft_idle': [],     # Done
            'rght_idle': [],    # Done
            
            # Attack Keys
            'up_attack': [],    # Done
            'dwn_attack': [],   # Done
            'lft_attack': [],   # Done
            'rght_attack': []   # Done
        }
        for animation in self.animations.keys():
            fullPath = animPath + animation
            self.animations[animation] = importFolder(fullPath)
    
    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()
            # X Movement
            if keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'lft'
            elif keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'rght'
            else:
                self.direction.x = 0
                
            # Y Movement
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'dwn'
            else:
                self.direction.y = 0
            
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attackTime = pygame.time.get_ticks()
                self.attackInstance()
        
    def getStatus(self):
        # Idle Status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        
        # Attack Status
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            self.animationSpeed += 0.17
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status +'_attack'
        # Stop Attacking
        else:
            self.animationSpeed = 0.5
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')
    
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
    
    def cooldowns(self):
        currentTime = pygame.time.get_ticks()
        if self.attacking:
            if currentTime - self.attackTime >= self.attackCooldown:
                self.attacking = False
                self.endAttack()
    
    def animate(self):
        animation = self.animations[self.status]

        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(animation):
            self.frameIndex = 0
        
        self.image = animation[int(self.frameIndex)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
        
    def update(self, deltaTime):
        self.input()
        self.cooldowns()
        self.getStatus()
        self.animate()
        self.plrMove(self.speed, deltaTime)