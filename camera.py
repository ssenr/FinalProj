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