import pygame
from constants import *

class Chip(pygame.sprite.Sprite):
    # def __init__(self, *groups):
    #     super().__init__(*groups)
    def __init__(self, colour):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.image, self.rect = self.create_image(colour)
    
    def create_image(self, colour):
        image = pygame.Surface([CHIP_RADIUS*2, CHIP_RADIUS*2])
        rect = image.get_rect()
        pygame.draw.circle(image, colour, (CHIP_RADIUS, CHIP_RADIUS), CHIP_RADIUS)
        return image, rect
        