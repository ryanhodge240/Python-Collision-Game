import pygame
import constants

class player:
    def __init__(self):
        self.characterImage = constants.sprites.PLAYER

    def drawPlayer(self, background):
        background.blit(self.characterImage, (30, 30))

        return background
