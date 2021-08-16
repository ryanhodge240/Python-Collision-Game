"""Controls the player's movement"""

from __future__ import absolute_import
import pygame
from constants import Player as player_constants
from constants import Game
from player import player

class ControlPlayer:
    """Controls the player's movement"""

    def __init__(self) -> None:
        self.d_x, self.d_y = (0, 0)
        self.player_position = player.get_player_position()

    def move_player(self) -> None:
        """Move the player's position"""
        self.d_x, self.d_y = (0, 0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.d_x = player_constants.PLAYER_DEFAULT_SPEED[0]
        if keys[pygame.K_LEFT]:
            self.d_x = -player_constants.PLAYER_DEFAULT_SPEED[0]
        if keys[pygame.K_DOWN]:
            self.duck()
        if keys[pygame.K_SPACE] and self.d_y == 0: # Change to when player reaches (collides with) ground again
            self.d_y = player_constants.PLAYER_DEFAULT_SPEED[1]

        self.d_y += Game.GRAVITY # Set gravity

    # TODO: make this fucntional
    def duck(self) -> None:
        """Make the player duck"""
        self.d_y = player_constants.PLAYER_DEFAULT_SPEED[1]

    def get_speed(self) -> tuple:
        """Return the x and y speeds"""
        return (self.d_x, self.d_y)

    def set_speed(self, speed: tuple) -> None:
        """Set the player's speed"""
        (self.d_x, self.d_y) = speed

    def get_player_position(self) -> tuple:
        """Return player position"""
        self.player_position[1] -= self.d_y
        self.player_position[0] += self.d_x
        return self.player_position

control_player = ControlPlayer()
