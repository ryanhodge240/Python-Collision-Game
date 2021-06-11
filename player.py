import pygame
from constants import player

class Player:
    def __init__(self) -> None:
        self.characterImage = player.PLAYER_SPRITE
        self.playerX, self.playerY = player.PLAYER_DEFAULT_LOCATION

    def drawPlayer(self, background: pygame.Surface) -> pygame.Surface: 
        background.blit(self.characterImage, (self.playerX, self.playerY))
        return background

    def setPlayerPosition(self, pos: tuple) -> None:
        self.playerX = pos[0]
        self.playerY = pos[1]

    def getPlayerPosition(self) -> tuple:
        return [self.playerX, self.playerY]
