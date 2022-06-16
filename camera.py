# This is the camera file for the game
# The cameraGroupY Class inherits from sprite group, so at it's basics, it's just a sprite group with additional properties
# I use the camera to draw what's on the screen for the viewer 
# this is done in the customDraw method
# basically, I load the base floor in the init method
# and for every sprite that's in this group (called visible sprites), we sort them based off their y position
# This gives them fake depth
# For scaling the camera in, I create a another surface, and scale it in based on it's size in vector format * a scale factor found in settings.py

# enemy update is also here, basicaly we call it's update method if it has the sprite type attribute
# (sprite type) is used to determine what type of tile it is 
# and if its and enemy
import pygame
from settings import *
# Camnera Class
class camGroupY(pygame.sprite.Group):
    def __init__(self):
        # Inherit from pygame sprite group
        super().__init__()
        
        self.displaySurf = pygame.display.get_surface()
        self.hWidth = self.displaySurf.get_size()[0] // 2
        self.hHeight = self.displaySurf.get_size()[1] // 2 
        self.offset = pygame.math.Vector2()

        # floor
        self.floorSurf = pygame.image.load("data/graphics/tilemap/castle_floor.png").convert()
        self.floorRect = self.floorSurf.get_rect(topleft = (0,0))
        
        # Scale
        self.iSurfSize = (screenWidth,screenHeight)
        self.iSurf = pygame.Surface(self.iSurfSize, pygame.SRCALPHA)
        self.iSurfRect = self.iSurf.get_rect(center = (self.hWidth, self.hHeight))
        self.iSurfVec = pygame.math.Vector2(self.iSurfSize)
        
    def customDraw(self, player):
        
        self.iSurf.fill(tsBlack)
        
        self.offset.x = player.rect.centerx - self.hWidth
        self.offset.y = player.rect.centery - self.hHeight
        
        floorOffsetPos = self.floorRect.topleft - self.offset
        self.iSurf.blit(self.floorSurf, floorOffsetPos)
        
        # lambda takes sprite and returns centery of sprite
        for sprite in sorted(self.sprites(), key = lambda sprite : sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.iSurf.blit(sprite.image, offsetPos)
            
        scaledSurf = pygame.transform.scale(self.iSurf, self.iSurfVec * scaleFac)
        scaledRect = scaledSurf.get_rect(center = (self.hWidth, self.hHeight))
        
        self.displaySurf.blit(scaledSurf,scaledRect)
        
    def enemy_update(self,player):
        enemySprites = [ sprite for sprite in self.sprites() if hasattr(sprite, 'spriteType') and sprite.spriteType == 'enemy']
        for enemy in enemySprites:
            enemy.enemy_update(player)
            pass