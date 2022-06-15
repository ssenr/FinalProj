import pygame
from settings import *
from scripts import *
from entity import Entity

class Enemy(Entity):
    def __init__(self,pos,groups, invisibleSprites):
        super().__init__(groups)
        self.spriteType = 'enemy'
        
        self.importGraphics()
        self.status = 'up'
        self.image = self.animations[self.status][self.frameIndex]
        
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.invisibleSprites = invisibleSprites
        
        # Stats
        self.health = skeleton_data['health']
        self.damage = skeleton_data['damage']
        self.speed = skeleton_data['speed']
        self.knockback = skeleton_data['knockback']
        self.attack_radius = skeleton_data['attack_radius']
        self.notice_radius = skeleton_data['notice_radius']
        
        self.canAttack = False

        
        
    def importGraphics(self):
        animPath = "data/graphics/anim_enemy/"
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
             
    def getDirDist(self,player):
        enemyVec = pygame.math.Vector2(self.rect.center)
        playerVec = pygame.math.Vector2(player.rect.center)
        distance = (playerVec - enemyVec).magnitude()
        
        if distance > 0:
            direction = (playerVec - enemyVec).normalize()
        else:
            direction = pygame.math.Vector2()
        
        return (distance, direction)
    
    def getStatus(self, player):
        distance = self.getDirDist(player)[0]
        direction = self.getDirDist(player)[1]
        
        # Idling
        if direction[0] == 0 and direction[1] == 0 and distance >= self.attack_radius and distance >= self.notice_radius:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status +'_idle'
        
        if distance <= self.attack_radius and not 'idle' in self.status and self.canAttack != False:
            self.status = self.status + '_attack'
        if distance <= self.notice_radius and not 'idle' in self.status and not 'attack' in self.status:
            self.status = self.status
        
        # elif not 'idle' in self.status and not 'attack' in self.status and not 'run' in self.status:
        #     self.status = self.status + '_idle'
    
    def actions(self, player):
        if 'attack' in self.status:
            self.direction = self.getDirDist(player)[1]
            match self.direction[0]:
                case -1:
                    self.status = 'lft'
                case 1:
                    self.status = 'rght'
            match self.direction[1]:
                case -1:
                    self.status = 'up'
                case 1:
                    self.stauts = 'dwn'
            print('attack')
        elif not 'attack' in self.status and not 'idle' in self.status:
            self.direction = self.getDirDist(player)[1]
            
            if self.direction.x > 0:
                self.status = 'rght'
            elif self.direction.x < 0:
                self.status = 'lft'
            
            if self.direction.y > 0:
                self.status = 'dwn'
            elif self.direction.y < 0:
                self.status = 'up'
        else:
            self.direction = pygame.math.Vector2()
    
    def animate(self):
        animation = self.animations[self.status]
        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(animation):
            self.frameIndex = 0
            
        self.image = animation[int(self.frameIndex)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
        
    
    def update(self):
        self.plrMove(self.speed)
        self.animate()
    
    def enemy_update(self, player):
        self.getStatus(player)
        self.actions(player)