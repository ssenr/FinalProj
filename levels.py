# Pygame Import
import pygame
from settings import * 
from scripts import * 
from camera import camGroupY
from attack import *
from tiling import Tile
from player import Player
from random import choice
from ui import UI
from enemy import Enemy
# Level Classes
# Each level has slightly different behaviour
# While creating different classes kind of defeats the purpose of using a class
# With classes I can easier create instances and have cleaner code
class level:
    def __init__(self):
        
        # DisplaySurf
        self.displaySurf = pygame.display.get_surface()
        
        # Sprite Groups
        self.visibleSprites = camGroupY()
        self.invisibleSprites = pygame.sprite.Group()
        self.damageSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.attack = None
        
        # Misc.
        self.status = False
        
        # Create Map
        self.initMap()
        
        # UI
        self.ui = UI()
    
    def initMap(self):
        mapData = {
            # BOUNDARIES
            'hard_boundary': importCSV("data/graphics/mapData/cstle_HARD_BOUNDARY.csv"),
            'wall_boundary': importCSV("data/graphics/mapData/cstle_WALL_BOUNDARY.csv"),
            'pillar_bounds': importCSV("data/graphics/mapData/cstle_PILLAR_BOUNDS.csv"),
            'entities': importCSV("data/graphics/mapData/cstle_ENTITIES_SPAWN.csv")
        }
        graphics = {
            'pillar': importFolder("data/graphics/tilemap/pillar")
        }
        print(graphics)
        # enumerate() counts each iteration
        for style, layout in mapData.items():
            for row_index,row in enumerate(layout):
                for column_index, column in enumerate(row):
                    if column != '-1':
                        x = column_index * tileSize
                        y = row_index * tileSize
                        if style == 'hard_boundary':
                            Tile((x,y), [self.invisibleSprites], 'hard_boundary')
                        if style == 'wall_boundary':
                            Tile((x,y), [self.invisibleSprites], 'wall_boundary')
                        if style == 'pillar_bounds':
                            pillarImage = choice(graphics['pillar'])
                            Tile((x,y), [self.visibleSprites,self.invisibleSprites], 'pillar', pillarImage)
                        
                        if style == 'entities':
                            if column == '1':
                                self.player = Player(
                                    (x,y), 
                                    [self.visibleSprites], 
                                    self.invisibleSprites, 
                                     # Pass attack Instance through bcuz we call it in player.py
                                    self.attackInstance, 
                                    self.endAttack
                                    )
                            else:
                                Enemy(
                                    (x,y),
                                    [self.visibleSprites,self.enemySprites],
                                    self.invisibleSprites
                                    )
                                  
    def attackInstance(self):
        self.attack = attack(self.player, [self.visibleSprites, self.damageSprites])
    
    def endAttack(self):
        if self.attack:
            self.attack.kill()
        self.attack = None
    
    def attackLogic(self):
        if self.damageSprites:
            for damage in self.damageSprites:
                collisionList = pygame.sprite.spritecollide(damage,self.enemySprites, False)
                if collisionList:
                    for sprite in collisionList:
                        sprite.getDamage(self.player)
                        
    
    
    def render(self):
        self.visibleSprites.customDraw(self.player)
        self.visibleSprites.update()
        self.visibleSprites.enemy_update(self.player)
        self.attackLogic()
        self.ui.display(self.player)