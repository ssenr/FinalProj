# Pygame Import
import pygame
from settings import * 
from tiling import Tile
from player import Player
# Level Classes
# Each level has slightly different behaviour
# While creating different classes kind of defeats the purpose of using a class
# With classes I can easier create instances and have cleaner code
class level:
    def __init__(self, num):
        # Level Num
        self.levelNum = num
        
        # DisplaySurf
        self.displaySurf = pygame.display.get_surface()
        
        # Sprite Groups
        self.visibleSprites = pygame.sprite.Group()
        self.invisibleSprites = pygame.sprite.Group()
        
        # Misc.
        self.status = False
        
        # Test
        self.initMap()
    
    def initMap(self):
        # enumerate() counts each iteration
        for row_index,row in enumerate(map):
            for column_index, column in enumerate(row):
                x = column_index * tileSize
                y = row_index * tileSize
                if column == 'x':
                    Tile((x,y), [self.visibleSprites,self.invisibleSprites])
                if column == 'p':
                    Player((x,y), [self.visibleSprites])
                    
    
    def num(self):
        return self.levelNum
    
    def render(self):
        self.visibleSprites.draw(self.displaySurf)
        self.visibleSprites.update()
    
    def completed(self):
        # Function denotes the completion of a level
        self.status = True
    
    def getStatus(self):
        # Return Status of Level
        return self.status