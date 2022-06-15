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
        self.invisibleSprite = invisibleSprites
        
        # Stats
        
        
        
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
            
    def update(self):
        self.move(self.speed)