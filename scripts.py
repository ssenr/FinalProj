# scripts useful for A. placing sprites and bounds
#                    B. returninga list of animations
# for the CSV importer
# open the file, split based on the comma, read all the numbers and return a list of all the numbers

# for the import Folder
# walks through the file tree, and for every image found, create a path for the directory, then load the image, then append he list of pygame images to a list, then return it




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
    for _,__,imgFiles in walk(path):
        for image in imgFiles:
            fullPath = path + '/' + image
            imageSurf = pygame.image.load(fullPath).convert_alpha()
            surfs.append(imageSurf)
            
    return surfs