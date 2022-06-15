# Pygame Import
import pygame
from settings import * 
from scripts import * 
from camera import *
from attack import *
from tiling import Tile
from player import Player
from random import choice
from ui import UI
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
            'pillar_bounds': importCSV("data/graphics/mapData/cstle_PILLAR_BOUNDS.csv")
            # 'trees': importCSV("data/graphics/mapData/main_floor_Trees.csv"),
            # 'spawnPoint': importCSV("data/graphics/mapData/main_floor_SpawnPoint.csv")
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
                        # if style == 'trees':
                        #     Tile((x,y), [self.invisibleSprites], 'trees')
                        if style == 'spawnPoint':
                            pass
        # Pass attack Instance through bcuz we call it in player.py
        self.player = Player((400,300), [self.visibleSprites], self.invisibleSprites, self.attackInstance, self.endAttack)
        
    def attackInstance(self):
        self.attack = attack(self.player, [self.visibleSprites])
    
    def endAttack(self):
        if self.attack:
            self.attack.kill()
        self.attack = None
    
    def render(self, deltaTime = 1):
        self.visibleSprites.customDraw(self.player)
        self.visibleSprites.update(deltaTime)
        self.ui.display(self.player)
    