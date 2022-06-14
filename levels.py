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
        self.visibleSprites = camGroupY()
        self.invisibleSprites = pygame.sprite.Group()
        
        # Misc.
        self.status = False
        
        # Test
        self.initMap()
    
    def initMap(self):
        # # enumerate() counts each iteration
        # for row_index,row in enumerate(map):
        #     for column_index, column in enumerate(row):
        #         x = column_index * tileSize
        #         y = row_index * tileSize
        #         # Spawn invisbleSprites and Player
        #         if column == 'x':
        #             Tile((x,y), [self.visibleSprites,self.invisibleSprites])
        #         if column == 'p':
        #             self.player = Player((x,y), [self.visibleSprites], self.invisibleSprites)
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
    
class camGroupY(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurf = pygame.display.get_surface()
        self.hWidth = self.displaySurf.get_size()[0] // 2
        self.hHeight = self.displaySurf.get_size()[1] // 2 
        self.offset = pygame.math.Vector2()

        # floor
        self.floorSurf = pygame.image.load("data/graphics/tilemap/floor.png").convert()
        self.floorRect = self.floorSurf.get_rect(topleft = (0,0))
        
    def customDraw(self, player):
        self.offset.x = player.rect.centerx - self.hWidth
        self.offset.y = player.rect.centery - self.hHeight
        
        floorOffsetPos = self.floorRect.topleft - self.offset
        self.displaySurf.blit(self.floorSurf, floorOffsetPos)
        
        # lambda takes sprite and returns centery of sprite
        for sprite in sorted(self.sprites(), key = lambda sprite : sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurf.blit(sprite.image, offsetPos)