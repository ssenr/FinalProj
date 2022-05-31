# Dependencies
import pygame
from sys import exit
from settings import *

# Init
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

# Game Loop
def gameLoop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill('black')
        pygame.display.update()
        clock.tick(FPS)

# Run Game
gameLoop()

