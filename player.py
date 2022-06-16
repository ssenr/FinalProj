import pygame
from entity import Entity
from settings import * 
from scripts import * 
from menu import MainMenu

# pygame.sprite.Sprite for inheritance
class Player(Entity):
    def __init__(self,pos,groups, invisibleSprites, attackInstance, endAttack):
        # initiate class
        super().__init__(groups)
        self.image = pygame.image.load(loadingFrame).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        
        # Anim Config
        self.plrAnims()
        self.status = 'up'
        self.invisibleSprites = invisibleSprites
        
        self.attacking = False
        self.attackCooldown = 500
        self.attackTime = None
        self.attackInstance = attackInstance
        self.endAttack = endAttack

        # Stats
        self.health = player_data['health']
        self.speed = player_data['speed']
        self.damage = player_data['damage']
        self.aliveStatus = True
        self.kills = 0
        
        self.vulnerable = True
        self.timeHurt = None
        self.invulnerabilityDuration = 800
        
        # Sounds
        self.attackSound = pygame.mixer.Sound(SFX['sword']['file'])
        self.attackSound.set_volume(SFX['sword']['_vol'])
        self.runSound = pygame.mixer.Sound(SFX['footsteps']['file'])
        self.runSound.set_volume(SFX['footsteps']['_vol'])
        
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
                self.attackSound.play()
        
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
    
    def cooldowns(self):
        currentTime = pygame.time.get_ticks()
        if self.attacking:
            if currentTime - self.attackTime >= self.attackCooldown:
                self.attacking = False
                self.endAttack()
        if not self.vulnerable:
            if currentTime - self.timeHurt >= self.invulnerabilityDuration:
                self.vulnerable = True
    
    def animate(self):
        animation = self.animations[self.status]

        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(animation):
            self.frameIndex = 0
        
        self.image = animation[int(self.frameIndex)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
        
        if not self.vulnerable:
            alpha = self.flicker()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
    
    def ifDead(self):
        if self.health <= 0:
            self.aliveStatus = False
    
    def update(self):
        self.input()
        self.cooldowns()
        self.getStatus()
        self.animate()
        self.plrMove(self.speed)
        self.ifDead()