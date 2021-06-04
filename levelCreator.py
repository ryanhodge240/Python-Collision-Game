import pygame
import constants

class levels:
    def __init__(self):
        self.brick = pygame.image.load('brick.png')
        self.brickRect = self.brick.get_rect()
        self.levelDimensions = (constants.levels.LEVEL_WIDTH, constants.levels.LEVEL_HEIGHT)

    def drawLevel(self, screen, levelLayout):
        screen.fill(constants.colors.CYAN)

        for i in range(self.levelDimensions[1]):
            for j in range(self.levelDimensions[0]):
                if levelLayout[i*j + j] == '#':
                    self.brickRect.topleft = (j, i)
                    screen.blit(self.brick, self.brickRect)