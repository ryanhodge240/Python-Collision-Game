"""Controls collisions"""

from __future__ import absolute_import

from player import player
from level_creator import level_creator
from control_player import control_player

class CollisionDetection:
    """Controls collisions"""

    def __init__(self) -> None:
        self.player_rect = player.get_player_rect()
        self.brick_rects = level_creator.get_bricks()

    def detect_collisions(self) -> None:
        """Detect collisions"""
        (d_x, d_y) = control_player.get_speed()

        # Reference: https://www.youtube.com/watch?v=WvcNfwIl2Jw
        for brick_rect in self.brick_rects:
            if brick_rect.colliderect(self.player_rect.x, self.player_rect.y + d_y, self.player_rect.width, self.player_rect.height):
                control_player.set_speed((d_x, 0))

collision_detection = CollisionDetection()
