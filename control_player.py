"""Controls the player's movement"""

from __future__ import absolute_import
import pygame
from constants import Player as player_constants
from constants import Game
from player import pl

class ControlPlayer:
    """Controls the player's movement"""

    def __init__(self, player: pl):
        self.character_image = player_constants.PLAYER_SPRITE
        self.d_x, self.d_y = player_constants.PLAYER_DEFAULT_SPEED

        self.player = player
        self.player_position = player.get_player_position()
        self.is_jumping = False

    def move_player(self) -> pygame.Surface:
        """Move the player's position"""

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.player_position[0] += self.d_x
        if keys[pygame.K_LEFT]:
            self.player_position[0] -= self.d_x
        if keys[pygame.K_DOWN]:
            self.duck()
        if self.is_jumping is True:
            self.jump()
        elif keys[pygame.K_SPACE]:
            self.is_jumping = True
            self.d_y = player_constants.PLAYER_DEFAULT_SPEED[1]

        self.player.set_player_position(self.player_position)

        return self.player

    # TODO: Check for collisions
    def jump(self) -> None:
        """Make the player jump"""

        self.player_position[1] -= self.d_y
        self.d_y += Game.GRAVITY

        # TODO: replace with collision detection
        if self.player_position[1] >= player_constants.PLAYER_DEFAULT_LOCATION[1]:
            self.player_position[1] = player_constants.PLAYER_DEFAULT_LOCATION[1]
            self.is_jumping = False

    # TODO: make this fucntional
    def duck(self):
        """Make the player duck"""

        self.player_position[1] += 4
