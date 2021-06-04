import pygame
import sys
import constants
import levelCreator

pygame.init()
screen = pygame.display.set_mode(constants.game.GAME_SIZE)

drawlingLevels = levelCreator.levels

brick = constants.sprites.BRICK
brickRect = brick.get_rect()
levels = (
    constants.levels.LEVEL_ONE,
    constants.levels.LEVEL_TWO,
    constants.levels.LEVEL_THREE
)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    drawlingLevels.drawLevel(screen, levels[0])
    pygame.display.flip()