import pygame
import sys

from pygame import draw
import constants
import levelCreator

def main():
    pygame.init()
    pygame.display.set_caption(constants.game.TITLE)

    screen = pygame.display.set_mode(constants.game.GAME_SIZE)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(constants.colors.CYAN)

    drawlingLevels = levelCreator.levels

    levels = (
        constants.levels.LEVEL_ONE,
        constants.levels.LEVEL_TWO,
        constants.levels.LEVEL_THREE
    )

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    sys.exit()

        background = levelCreator.levels.drawLevel(background, levels[0])
        
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()