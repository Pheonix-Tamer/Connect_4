import pygame
import numpy as np
from enum import Enum
from constants import *

class Board(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.player_matrix = np.ones(GRID_DIMENSIONS)
        self.player_matrix[5][0] = 2
        
        
        self.topleft = ((SCREEN_WIDTH/2)-(BOARD_WIDTH/2), 100.0)
        self.image, self.rect = self.create_image()
        self.rect.topleft = self.topleft
        
    def create_image(self):
        image = pygame.Surface([BOARD_WIDTH, BOARD_HEIGHT])
        image.fill("blue")
        for i in range(6):
            for j in range(7):
                # pygame.draw.line(image, "white", ((100 * (i + 1)), 0), ((100 * (i + 1)), BOARD_HEIGHT))
                if self.player_matrix[i][j] == 1:
                    col = "black"
                elif self.player_matrix[i][j] == 2:
                    col = "red"
                elif self.player_matrix[i][j] == 3:
                    col = "yellow"
                pygame.draw.circle(image, col, ((BOARD_GRID_WIDTH * (j + 1)) - BOARD_GRID_WIDTH/2, (BOARD_GRID_WIDTH * (i + 1)) - BOARD_GRID_WIDTH/2), BOARD_CIRCLE_RADIUS)
        rect = image.get_rect()
        return image, rect

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
        