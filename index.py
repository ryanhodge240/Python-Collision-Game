"""The main python file for the mario game"""

from __future__ import absolute_import
import sys
import pygame

# Import custom classes and files
import constants
from level_creator import LevelCreator
from player import Player
from control_player import ControlPlayer

def main():
    """The main function for the program"""

    # Initialize pygame
    pygame.init()
    pygame.display.set_caption(constants.Game.TITLE)
    screen = pygame.display.set_mode(constants.Game.GAME_SIZE)

    # Define all the classes
    _clock = pygame.time.Clock()
    _player = Player()
    _level_creator = LevelCreator()
    _control_player = ControlPlayer(_player)

    # Temporary way to define all the levels
    # TODO: Clean up the levels
    levels = (
        constants.Levels.LEVEL_ONE,
        constants.Levels.LEVEL_TWO,
        constants.Levels.LEVEL_THREE
    )

    # Define variables to be used
    running = True

    # Main while loop that only stops when the game is exited
    while running:
        # Initialize the timer and repaint the background
        _clock.tick(constants.Game.FRAME_RATE)
        screen.fill(constants.Colors.CYAN)

        # Loop through events and see if the window should be closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    running = False

        # Draw the level (the bricks)
        screen = _level_creator.draw_level(screen, levels[0])

        # Draw enemies

        # Draw player
        screen = _player.draw_player(screen)

        # Control player
        _player = _control_player.move_player()

        # Control camera

        # Collision detection

        # Action listener

        # Repaint the screen
        pygame.display.flip()

    sys.exit() # Quit

if __name__ == '__main__':
    main()
