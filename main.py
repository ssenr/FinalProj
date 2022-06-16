# Basic Game loop
# Initially I made it a class for a levelling system I wanted to implement
# However, the code alredy takes a long time to load, so I felt like adding different instances without proper optimizations would do more harm than good
# Also the framework I had though of for levelling wasn't working out too well so I stopped
# Dependencies
import pygame
from sys import exit
from settings import *
from levels import *
from menu import MainMenu

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
        
        # Init Level One
        self.level = level()
        self.playing = True
        self.startMenu = MainMenu(self)
        
        
        # BG Music
        
    # Game Loop
    def run(self):
        self.startMenu.displayMenu()
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.startMenu.running = False
                    pygame.quit()
                    exit()
                                  
            # Game Setup
            self.screen.fill(blackRGB)
                
            # Render Level
            self.level.render()

            # Update
            pygame.display.update()
            self.clock.tick(FPS)

# Create Game OBJ and call run
game = Game()
game.run()