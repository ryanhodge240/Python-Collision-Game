"""Controls collisions"""

from __future__ import absolute_import
import pygame
from constants import Game
from player import player
from level_creator import level_creator

class CollisionDetection:
    """Controls collisions"""

    def __init__(self) -> None:
        self.player_rect = player.get_player_rect()
        self.brick_rects = level_creator.get_bricks()

    def detect_collisions(self) -> None:
        """Detect collisions"""
        for brick_rect in self.brick_rects:
            if self.player_rect.colliderect(brick_rect):
                if abs(brick_rect.top - self.player_rect.bottom) < Game.COLLISION_THRESHOLD:
                    player
                if abs(brick_rect.bottom - self.player_rect.top) < Game.COLLISION_THRESHOLD:
                    player
                if abs(brick_rect.right - self.player_rect.left) < Game.COLLISION_THRESHOLD:
                    player
                if abs(brick_rect.left - self.player_rect.right) < Game.COLLISION_THRESHOLD:
                    player

collision_detection = CollisionDetection()
