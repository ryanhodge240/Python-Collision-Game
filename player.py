"""Draws the player on the screen"""

from __future__ import absolute_import
import pygame
from constants import Player as pl

class Player:
    """Draws the player"""

    def __init__(self) -> None:
        self.character_image = pl.PLAYER_SPRITE
        self.player_x, self.player_y = pl.PLAYER_DEFAULT_LOCATION

    def draw_player(self, background: pygame.Surface) -> pygame.Surface:
        """Draws the player"""

        background.blit(self.character_image, (self.player_x, self.player_y))
        return background

    def set_player_position(self, pos: tuple) -> None:
        """Sets the player's position"""

        self.player_x = pos[0]
        self.player_y = pos[1]

    def get_player_position(self) -> tuple:
        """Gets the player's position"""

        return [self.player_x, self.player_y]
