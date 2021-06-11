import pygame
from constants import player as player_constants
from constants import game
from Player import Player

class ControlPlayer:
    def __init__(self, player: Player):
        self.characterImage = player_constants.PLAYER_SPRITE
        self.dx, self.dy = player_constants.PLAYER_DEFAULT_SPEED

        self.player = player
        self.playerPosition = player.getPlayerPosition()
        self.isJumping = False

    def movePlayer(self) -> pygame.Surface:
        keys = pygame.key.get_pressed() 

        if keys[pygame.K_RIGHT]:
                self.playerPosition[0] += self.dx
        if keys[pygame.K_LEFT]:
            self.playerPosition[0] -= self.dx

        if self.isJumping == True:
            self.jump()
        else:
            if keys[pygame.K_SPACE]:
                self.isJumping = True
                self.dy = player_constants.PLAYER_DEFAULT_SPEED[1]
            if keys[pygame.K_DOWN]:
                self.duck()

        self.player.setPlayerPosition(self.playerPosition)

        return self.player

    # TODO: Check for collisions
    def jump(self) -> None:
        self.playerPosition[1] -= self.dy
        self.dy += game.GRAVITY

        # TODO: replace with collision detection
        if self.playerPosition[1] >= player_constants.PLAYER_DEFAULT_LOCATION[1]:
            self.playerPosition[1] = player_constants.PLAYER_DEFAULT_LOCATION[1]
            self.isJumping = False

    # TODO: make this fucntional
    def duck(self):
        self.playerPosition[1] += 4

