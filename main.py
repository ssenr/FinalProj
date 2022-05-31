# Dependencies
import pygame
import levels as lvl
from sys import exit
from settings import *

# Game Class
# When code scales, it will be much easier to modify this class rather than a function
class Game:
    # Init
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(gameName)
        
        # Icon 
        self.Icon = pygame.image.load(iconPath)
        pygame.display.set_icon(self.Icon)
        #######################################
        
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        self.clock = pygame.time.Clock()
        
        # Init Levels
        self.levelOne = lvl.level(1)
        self.levelTwo = lvl.level(2)
        self.levelThree = lvl.level(3)
        
        # Init Level One
        self.level = self.levelOne
        
        # level Progression
        self.levelProgress = {
            "levelOne": self.levelOne.getStatus(),
            "levelTwo": self.levelTwo.getStatus()
        }
            
    # Game Loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
                # Debug Keys
                # if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                #     self.level.completed()
                #     self.levelProgress["levelOne"] = self.level.getStatus()
                #     # pass
                # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                #     x = self.levelProgress.get("levelOne")
                #     print(x)
                #     # pass
                    
            # Game Setup
            self.screen.fill(blackRGB)
                
            # Level Setup
                # Switch Code Not Built
                # Needs Level Clear
            # Render Level
            self.level.render()

            # Update
            pygame.display.update()
            self.clock.tick(FPS)

# Create Game OBJ and call run
game = Game()
game.run()
