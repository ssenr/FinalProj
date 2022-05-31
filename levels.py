# Pygame Import
import pygame

# Level Classes
# Each level has slightly different behaviour
# While creating different classes kind of defeats the purpose of using a class
# With classes I can easier create instances and have cleaner code
class level:
    def __init__(self, num):
        self.levelNum = num
        
        # Sprite Groups
        self.visibleSprites = pygame.sprite.Group()
        self.invisibleSprites = pygame.sprite.Group()
        
        # Misc.
        self.status = False
        
    def render(self):
        pass
    
    def completed(self):
        # Function denotes the completion of a level
        self.status = True
    
    def getStatus(self):
        # Return Status of Level
        return self.status