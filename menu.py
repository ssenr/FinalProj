import pygame
from settings import *
from sys import exit
from math import sin

class Menu():
    def __init__(self, game):
        self.game = game
        self.menuStatus = True
        self.displaySurf = pygame.display.get_surface()
        
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.mid_w, self.mid_h = screenWidth / 2, screenHeight / 2
        self.offset = -100
        
    def drawCursor(self):
        cursorFont = pygame.font.Font("data/ui/DungeonFont.ttf", 25)
        cursorSurf = cursorFont.render("*", True, whiteRGB) 
        cursorRect = cursorSurf.get_rect()
        cursorRect.center = (self.cursor_rect.x + 35 ,self.cursor_rect.y + 5)
        self.displaySurf.blit(cursorSurf, cursorRect)
        
    def blitScreen(self):
        self.displaySurf.blit(self.game.screen, (0,0))
        pygame.display.update()
        
        
class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.START_KEY = False
        
        # Sound
        self.confirmTone = pygame.mixer.Sound(SFX['confirm_sound']['file'])
        self.confirmTone.set_volume(SFX['confirm_sound']['_vol'])
        self.cursorTone = pygame.mixer.Sound(SFX['cursor_sound']['file'])
        self.cursorTone.set_volume(SFX['cursor_sound']['_vol'])
        
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
        
    def check_input(self):
        if self.START_KEY:
            if self.state == 'Start':
                self.confirmTone.play()
                self.game.playing = True
            self.menuStatus = False
    
    def displayMenu(self):
        self.menuStatus = True
        while self.menuStatus:
            self.game.screen.fill(blackRGB)
            
            self.check_events()
            self.check_input()
            
            # Import Poster
            self.posterIMG = pygame.image.load('data/ui/poster.png')
            self.posterRect = self.posterIMG.get_rect()
            self.displaySurf.blit(self.posterIMG, self.posterRect)
            
            # Create Title
            titleFont = pygame.font.Font("data/ui/DungeonFont.ttf", 40)
            titleSurf = titleFont.render("What lies ahead?", True, whiteRGB) 
            titleRect = titleSurf.get_rect()
            titleRect.center = (screenWidth / 2 , screenHeight / 2 - 20)
            self.displaySurf.blit(titleSurf, titleRect)
            
            # Option Create
            optionFont = pygame.font.Font("data/ui/DungeonFont.ttf", 30)
            optionSurf = optionFont.render("Start Game", True, whiteRGB) 
            optionRect = optionSurf.get_rect()
            optionRect.center = (self.startx,self.starty)
            self.displaySurf.blit(optionSurf, optionRect)
            
            # Credits
            creditFont = pygame.font.Font("data/ui/DungeonFont.ttf", 15)
            creditSurf = creditFont.render("By Duran Ramlall", True, whiteRGB) 
            creditRect = optionSurf.get_rect(center = (screenWidth / 2 - 253, screenHeight / 2 + 360))
            self.displaySurf.blit(creditSurf, creditRect)
            
            # Draw
            self.drawCursor()
            self.blitScreen()          

class deathMenu():
    def __init__(self):
            super().__init__()
            
            pygame.init()
            self.displaySurf = pygame.display.get_surface()
            self.screen = pygame.display.set_mode((screenWidth, screenHeight))
            self.cursor_rect = pygame.Rect(0,0,20,20)
            self.state = "Quit"
            self.startx, self.starty = screenWidth / 2, screenHeight / 2 + 30
            self.offset = -100
            self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
            self.START_KEY = False
            
            # Sound
            self.confirmTone = pygame.mixer.Sound(SFX['confirm_sound']['file'])
            self.confirmTone.set_volume(SFX['confirm_sound']['_vol'])
            self.cursorTone = pygame.mixer.Sound(SFX['cursor_sound']['file'])
            self.cursorTone.set_volume(SFX['cursor_sound']['_vol'])        
    
    def drawCursor(self):
        cursorFont = pygame.font.Font("data/ui/DungeonFont.ttf", 25)
        cursorSurf = cursorFont.render("*", True, whiteRGB) 
        cursorRect = cursorSurf.get_rect()
        cursorRect.center = (screenWidth / 2 ,screenHeight / 2)
        self.displaySurf.blit(cursorSurf, cursorRect)
        
    def blitScreen(self):
        self.displaySurf.blit(self.screen, (0,0))
        pygame.display.update()
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
        
    def check_input(self):
        if self.START_KEY:
            if self.state == 'Quit':
                self.confirmTone.play()
                pygame.quit()
                exit()
            self.menuStatus = False
    
    def displayMenu(self):
        self.menuStatus = True
        while self.menuStatus:
            self.screen.fill(blackRGB)
            
            self.check_events()
            self.check_input()
            
            # Game Over
            self.gameOverIMG = pygame.image.load('data/ui/gameOver.png')
            self.gameOverRect = self.gameOverIMG.get_rect()
            self.displaySurf.blit(self.gameOverIMG, self.gameOverRect)

            # Option Create
            optionFont = pygame.font.Font("data/ui/DungeonFont.ttf", 30)
            optionSurf = optionFont.render("Quit Game", True, whiteRGB) 
            optionRect = optionSurf.get_rect()
            optionRect.center = (screenWidth / 2,screenHeight / 2)
            self.displaySurf.blit(optionSurf, optionRect)
            
            # Credits
            creditFont = pygame.font.Font("data/ui/DungeonFont.ttf", 15)
            creditSurf = creditFont.render("By Duran Ramlall", True, whiteRGB) 
            creditRect = optionSurf.get_rect(center = (screenWidth / 2 - 253, screenHeight / 2 + 360))
            self.displaySurf.blit(creditSurf, creditRect)
            
            # Draw
            self.drawCursor()
            self.blitScreen()    
        