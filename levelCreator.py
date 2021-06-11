import pygame
from constants import levels, sprites

class LevelCreator:
    def __init__(self) -> None:
        self.levelDimensions = levels.LEVEL_DIMENSIONS
        self.brick = sprites.BRICK
        self.brick_rect = []

    def drawLevel(self, background: pygame.Surface, levelLayout: str) -> pygame.Surface:
        for i in range(self.levelDimensions[1]):
            for j in range(self.levelDimensions[0]):
                if levelLayout[i*self.levelDimensions[0] + j] == '#':
                    self.brick_rect.append(pygame.Rect((j*20, i*20), sprites.BRICK_SIZE))
                    background.blit(self.brick, (j*20, i*20))

        return background

    # def isThereABrick(self, obj: object) -> bool:
    #     for rect in self.brick_rect:
    #         if rect
