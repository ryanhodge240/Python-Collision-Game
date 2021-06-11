import pygame
import sys

# Import custom classes and files
import constants
from LevelCreator import LevelCreator
from Player import Player
from ControlPlayer import ControlPlayer

def main():
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption(constants.game.TITLE)
    screen = pygame.display.set_mode(constants.game.GAME_SIZE)

    # Define all the classes
    clock = pygame.time.Clock()
    player = Player()
    levelCreator = LevelCreator()
    controlPlayer = ControlPlayer(player)

    # Temporary way to define all the levels
    # TODO: Clean up the levels
    levels = (
        constants.levels.LEVEL_ONE,
        constants.levels.LEVEL_TWO,
        constants.levels.LEVEL_THREE
    )

    # Define variables to be used
    running = True

    # Main while loop that only stops when the game is exited
    while running:
        # Initialize the timer and repaint the background
        clock.tick(constants.game.FRAME_RATE)
        screen.fill(constants.colors.CYAN)

        # Loop through events and see if the window should be closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    running = False

        # Draw the level (the bricks)
        screen = levelCreator.drawLevel(screen, levels[0])

        # Draw enemies
        
        # Draw player
        screen = player.drawPlayer(screen)

        # Control player
        player = controlPlayer.movePlayer()

        # Control camera

        # Collision detection

        # Action listener
        
        # Repaint the screen
        pygame.display.flip()

    sys.exit() # Quit

if __name__ == '__main__': main()