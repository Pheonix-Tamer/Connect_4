import pygame
from constants import *

class Board(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.image = pygame.Surface([BOARD_WIDTH, BOARD_HEIGHT])
        self.image.fill("blue")
        self.topleft = ((SCREEN_WIDTH/2)-(BOARD_WIDTH/2), 100)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft
    
    # def draw(self, screen):
    #     screen.blit(self.image, self.rect)
    #     for i in range(5):
    #         pygame.draw.line(screen, "white", (self.topleft[0] * (i + 1), self.topleft[1]), (self.topleft[0] * (i + 1), self.topleft[1]+ BOARD_HEIGHT))
        
    def __repr__(self):
        return f"topleft x: {self.topleft[0]}, topleft y: {self.topleft[1]}"
    