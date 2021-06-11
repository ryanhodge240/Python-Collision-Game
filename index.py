import pygame
import sys

import constants
from LevelCreator import LevelCreator
from Player import Player
from ControlPlayer import ControlPlayer

def main():
    pygame.init()
    pygame.display.set_caption(constants.game.TITLE)

    clock = pygame.time.Clock()
    player = Player()
    levelCreator = LevelCreator()
    controlPlayer = ControlPlayer(player)

    screen = pygame.display.set_mode(constants.game.GAME_SIZE)

    levels = (
        constants.levels.LEVEL_ONE,
        constants.levels.LEVEL_TWO,
        constants.levels.LEVEL_THREE
    )

    while 1:
        clock.tick(constants.game.FRAME_RATE)
        screen.fill(constants.colors.CYAN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    sys.exit()

        screen = levelCreator.drawLevel(screen, levels[0])

        # Display enemies
        
        # Display player
        screen = player.drawPlayer(screen)

        # Control player
        player = controlPlayer.movePlayer()

        # Control camera

        # Collision detection

        # Action listener
        
        pygame.display.flip()

if __name__ == '__main__': main()