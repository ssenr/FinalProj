from csv import reader
from os import walk
import pygame

def importCSV(path):
    tMap = []
    with open(path) as levelMap:
        # reads the , in comma seperated file (csv)
        layout = reader(levelMap, delimiter= ',')
        for row in layout:
            tMap.append(list(row))
        return tMap

def importFolder(path):
    surfs = []
    for x,y,imgFiles in walk(path):
        for image in imgFiles:
            fullPath = path + '/' + image
            imageSurf = pygame.image.load(fullPath).convert_alpha()
            surfs.append(imageSurf)
            
    return surfs