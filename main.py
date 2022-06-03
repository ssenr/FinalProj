# Dependencies
import pygame
import levels as lvl
from sys import exit
from settings import *

# Game Class
# rando

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
        
        # level Progression Check
        self.levelProgress = {
            1 : self.levelOne.getStatus(),
            2 : self.levelTwo.getStatus(),
            3 : self.levelThree.getStatus()
        }
    
    # Allows us to use modifiable debug code within our gameLoop
    def debugMode(self, event):
        # Controls
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            self.level.completed()
            self.updateProgress()
            self.levelUp()
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     self.levelUp()
        #     self.updateProgress()
        #     # pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            print(self.level.num())
    
    # Allows us to progress a level
    def levelUp(self):
        if self.levelProgress[1] == True:
            self.level = self.levelTwo
            if self.levelProgress[2] == True:
                self.level = self.levelThree
                if self.levelProgress[3] == True:
                    print("Finished Game")
        else:
            self.level == self.levelOne
        # pass
    
    # Updating our Dictionary
    def updateProgress(self):
        # Maybe Recreate with For Loop
        self.levelProgress[1] = self.levelOne.getStatus()
        self.levelProgress[2] = self.levelTwo.getStatus()
        self.levelProgress[3] = self.levelThree.getStatus()
    
    # Game Loop
    def run(self):
        global debugStatus
        debugStatus = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                # Debug Key
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    debugStatus = not debugStatus
                    print(debugStatus)
                if debugStatus == True:
                    # self.debugMode(event)
                    self.debugMode(event)
                    
            # Game Setup
            self.screen.fill(blackRGB)
                
            # Level Setup
                # Needs Level Clear
            # Render Level
            self.level.render()

            # Update
            pygame.display.update()
            self.clock.tick(FPS)

# Create Game OBJ and call run
game = Game()
game.run()