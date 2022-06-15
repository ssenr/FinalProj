import pygame
from settings import *

class UI:
    def __init__(self):
        self.displaySurf = pygame.display.get_surface()
        
        # Health
        self.healthBars = {
            100: "data/ui/elements/health_states/100.png",
            90: "data/ui/elements/health_states/90.png",
            80: "data/ui/elements/health_states/80.png",
            70: "data/ui/elements/health_states/70.png",
            60: "data/ui/elements/health_states/60.png",
            50: "data/ui/elements/health_states/50.png",
            40: "data/ui/elements/health_states/40.png",
            30: "data/ui/elements/health_states/30.png",
            20: "data/ui/elements/health_states/20.png",
            10: "data/ui/elements/health_states/10.png",
            0 : "data/ui/elements/health_states/0.png"
        }
        
        
    
    def display(self,player):
        # Load Frame
        self.frameIMG = pygame.image.load("data/ui/elements/frame.png").convert_alpha()
        self.frameRect = self.frameIMG.get_rect()
        self.displaySurf.blit(self.frameIMG,self.frameRect)
        
        self.healthBar = pygame.image.load(self.healthBars[player.health]).convert_alpha()
        self.healthRect = self.healthBar.get_rect()
        self.displaySurf.blit(self.healthBar,self.healthRect)