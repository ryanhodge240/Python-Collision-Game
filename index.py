from player import player
import pygame
import sys

from pygame import draw
import constants
import levelCreator

def main():
    pygame.init()
    pygame.display.set_caption(constants.game.TITLE)

    playerClass = player()

    screen = pygame.display.set_mode(constants.game.GAME_SIZE)
    screen.fill(constants.colors.CYAN)

    levels = (
        constants.levels.LEVEL_ONE,
        constants.levels.LEVEL_TWO,
        constants.levels.LEVEL_THREE
    )

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    sys.exit()

        screen = levelCreator.drawLevel(screen, levels[0])

        # Display enemies
        
        # Display player
        screen = playerClass.drawPlayer(screen)

        # Control player

        # Collision detection

        # Action listener
        
        pygame.display.flip()

if __name__ == '__main__': main()