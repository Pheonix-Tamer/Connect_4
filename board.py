import pygame
from constants import *

class Board(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.topleft = ((SCREEN_WIDTH/2)-(BOARD_WIDTH/2), 100.0)
        self.image, self.rect = self.create_image()
        self.rect.topleft = self.topleft
        
    def create_image(self):
        image = pygame.Surface([BOARD_WIDTH, BOARD_HEIGHT])
        image.fill("blue")
        for i in range(7):
            for j in range(6):
                # pygame.draw.line(image, "white", ((100 * (i + 1)), 0), ((100 * (i + 1)), BOARD_HEIGHT))
                pygame.draw.circle(image, "black", ((BOARD_GRID_WIDTH * (i + 1)) - BOARD_GRID_WIDTH/2, (BOARD_GRID_WIDTH * (j + 1)) - BOARD_GRID_WIDTH/2), BOARD_CIRCLE_RADIUS)
        rect = image.get_rect()
        return image, rect
