import pygame
import constants

class levels:

    def createRect(rect, width, height):
        rect = pygame.transform.scale(rect, (width, height)) 
        rect = rect.get_rect()
        return rect

    def drawLevel(background, levelLayout):
        levelDimensions = (constants.levels.LEVEL_WIDTH, constants.levels.LEVEL_HEIGHT)
        brick = constants.sprites.BRICK
        brick = pygame.transform.scale(brick, constants.sprites.BRICK_SIZE)
        brick = brick.convert_alpha()

        for i in range(levelDimensions[1]):
            for j in range(levelDimensions[0]):
                if levelLayout[i*levelDimensions[0] + j] == '#':
                    background.blit(brick, (j*20, i*20))

        return background
