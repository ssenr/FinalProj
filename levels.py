# Pygame Import
import pygame
from settings import * 
from scripts import * 
from camera import *
from tiling import Tile
from player import Player
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
        
        # Misc.
        self.status = False
        
        # Test
        self.initMap()
    
    def initMap(self):
        mapData = {
            'boundary': importCSV("data/graphics/csv/main_floor_BLOCKS.csv"),
            'trees': importCSV("data/graphics/csv/main_floor_Trees.csv"),
            'spawnPoint': importCSV("data/graphics/csv/main_floor_SpawnPoint.csv")
        }
        # enumerate() counts each iteration
        for style, layout in mapData.items():
            for row_index,row in enumerate(layout):
                for column_index, column in enumerate(row):
                    if column != '-1':
                        x = column_index * tileSize
                        y = row_index * tileSize
                        if style == 'boundary':
                            Tile((x,y), [self.invisibleSprites], 'boundary')
                        if style == 'trees':
                            Tile((x,y), [self.invisibleSprites], 'trees')
                        if style == 'spawnPoint':
                            pass
        self.player = Player((400,300), [self.visibleSprites], self.invisibleSprites)
        
    def num(self):
        return self.levelNum
    
    def render(self):
        self.visibleSprites.customDraw(self.player)
        self.visibleSprites.update()
    
    def completed(self):
        # Function denotes the completion of a level
        self.status = True
    
    def getStatus(self):
        # Return Status of Level
        return self.status