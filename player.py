"""Draws the player on the screen"""

from __future__ import absolute_import
import pygame
from constants import Player as pl

class Player:
    """Draws the player"""

    def __init__(self) -> None:
        self.character_image = pl.PLAYER_SPRITE
        self.player_x, self.player_y = pl.PLAYER_DEFAULT_LOCATION
        self.player_rect = pygame.Rect((self.player_x, self.player_y), (pl.PLAYER_SIZE))

    def draw_player(self, background: pygame.Surface) -> pygame.Surface:
        """Draws the player"""

        background.blit(self.character_image, self.player_rect)
        return background

    def set_player_position(self, pos: tuple) -> None:
        """Sets the player's position"""
        self.player_rect.topleft = (pos[0], pos[1])

    def get_player_position(self) -> tuple:
        """Gets the player's position"""

        return [self.player_x, self.player_y]

    def get_player_rect(self) -> pygame.Rect:
        """Gets the player's rect object"""

        return self.player_rect

player = Player()
