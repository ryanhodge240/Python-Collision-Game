"""Draws the levels"""

from __future__ import absolute_import
import pygame
from constants import Levels, Sprites

class LevelCreator:
    """Draws the current level"""

    def __init__(self) -> None:
        self.level_dimensions = Levels.LEVEL_DIMENSIONS
        self.brick = Sprites.BRICK
        self.coin = Sprites.COIN
        self.brick_rects = []
        self.coin_rect = []

    def draw_level(self, background: pygame.Surface, level_layout: str) -> pygame.Surface:
        """Draws the specified level"""

        for i in range(self.level_dimensions[1]):
            for j in range(self.level_dimensions[0]):
                character = level_layout[i*self.level_dimensions[0] + j]
                if character == '#':
                    self.brick_rects.append(pygame.Rect((j*20, i*20), Sprites.BRICK_SIZE))
                    background.blit(self.brick, (j*20, i*20))
                elif character == 'O':
                    self.brick_rects.append(pygame.Rect((j*20, i*20), Sprites.COIN_SIZE))
                    background.blit(self.coin, (j*20, i*20))

        return background

    def get_bricks(self) -> list[pygame.Rect]:
        """Returns the array of brick Rects"""

        return self.brick_rects

level_creator = LevelCreator()
