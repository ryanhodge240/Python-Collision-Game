import pygame
import constants

def drawLevel(background, levelLayout):
    levelDimensions = constants.levels.LEVEL_DIMENSIONS
    brick = constants.sprites.BRICK

    for i in range(levelDimensions[1]):
        for j in range(levelDimensions[0]):
            if levelLayout[i*levelDimensions[0] + j] == '#':
                background.blit(brick, (j*20, i*20))

    return background
