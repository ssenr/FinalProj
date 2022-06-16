# This is where most of the things occur and are called
# we init the different groups for different types of sprites, like those that are drawn are drawn in camera view, bounds are drawn in invisible sprites etc.
# On init, we also create the map, which uses nested for loops to draw the different bounds as well as spawn entities according to values in a .csv file (from tiled)
# When the map is created so is the player

# Attack Instance with proper params and the killing of the attack sprite is also passed to the player so it can be determined it they hit an enemy of not
# endAttack just kills the hitbox sprite so if another enemy walks through it and the sprite is still there they dont take damage

# The attack logic is simple, for every sprite that takes damage, store the collisions in a list, and then get the damage with player

# Then we render all the visible sprites, call their updates so they can do their own logic as well as keep calling attack logic for future updates
# Pygame Import
import pygame
from sys import exit
from menu import deathMenu
from settings import * 
from scripts import * 
from camera import camGroupY
from attack import *
from tiling import Tile
from player import Player
from random import choice
from ui import UI
from enemy import Enemy

class level:
    def __init__(self):
        
        # Main
        self.displaySurf = pygame.display.get_surface()
        self.game_paused = False
        
        # Sprite Groups
        self.visibleSprites = camGroupY()
        self.invisibleSprites = pygame.sprite.Group()
        self.damageSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.attack = None
        
        # Misc.
        self.status = False
        
        # Create Map
        self.initMap()
        
        # UI
        self.ui = UI()
        
        # A
        bgSound = pygame.mixer.Sound(SFX['BG Music']['file'])
        bgSound.set_volume(SFX['BG Music']['_vol'])
        bgSound.play(loops = -1)
        
        ambience = pygame.mixer.Sound(SFX['ambient_sound']['file'])
        ambience.set_volume(SFX['ambient_sound']['_vol'])
        ambience.play(loops = -1)
        
        
    
    def initMap(self):
        mapData = {
            # BOUNDARIES
            'hard_boundary': importCSV("data/graphics/mapData/cstle_HARD_BOUNDARY.csv"),
            'wall_boundary': importCSV("data/graphics/mapData/cstle_WALL_BOUNDARY.csv"),
            'pillar_bounds': importCSV("data/graphics/mapData/cstle_PILLAR_BOUNDS.csv"),
            'entities': importCSV("data/graphics/mapData/cstle_ENTITIES_SPAWN.csv")
        }
        graphics = {
            'pillar': importFolder("data/graphics/tilemap/pillar")
        }
        print(graphics)
        # enumerate() counts each iteration
        for style, layout in mapData.items():
            for row_index,row in enumerate(layout):
                for column_index, column in enumerate(row):
                    if column != '-1':
                        x = column_index * tileSize
                        y = row_index * tileSize
                        if style == 'hard_boundary':
                            Tile((x,y), [self.invisibleSprites], 'hard_boundary')
                        if style == 'wall_boundary':
                            Tile((x,y), [self.invisibleSprites], 'wall_boundary')
                        if style == 'pillar_bounds':
                            pillarImage = choice(graphics['pillar'])
                            Tile((x,y), [self.visibleSprites,self.invisibleSprites], 'pillar', pillarImage)
                        
                        if style == 'entities':
                            if column == '1':
                                self.player = Player(
                                    (x,y), 
                                    [self.visibleSprites], 
                                    self.invisibleSprites, 
                                     # Pass attack Instance through bcuz we call it in player.py
                                    self.attackInstance, 
                                    self.endAttack
                                    )
                            else:
                                Enemy(
                                    (x,y),
                                    [self.visibleSprites,self.enemySprites],
                                    self.invisibleSprites,
                                    self.damagePlayer,
                                    self.enemySprites
                                    )
                                  
    def attackInstance(self):
        self.attack = attack(self.player, [self.visibleSprites, self.damageSprites])
    
    def endAttack(self):
        if self.attack:
            self.attack.kill()
        self.attack = None
    
    def attackLogic(self):
        if self.damageSprites:
            for damage in self.damageSprites:
                collisionList = pygame.sprite.spritecollide(damage,self.enemySprites, False)
                if collisionList:
                    for sprite in collisionList:
                        sprite.getDamage(self.player)
                        
    def damagePlayer(self, amount):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.timeHurt = pygame.time.get_ticks() 

    def render(self):
        if self.player.health <= 0:
            self.deathMenu = deathMenu()
            self.deathMenu.displayMenu()
        else:
            self.visibleSprites.customDraw(self.player)
            self.ui.display(self.player)
            self.visibleSprites.update()
            self.visibleSprites.enemy_update(self.player)
            self.attackLogic()
    
        