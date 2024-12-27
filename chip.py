import pygame
from constants import *

class Chip(pygame.sprite.Sprite):
    # def __init__(self, *groups):
    #     super().__init__(*groups)
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.image, self.rect = self.create_image()
    
    def create_image(self):
        image = pygame.Surface(CHIP_RADIUS/2, CHIP_RADIUS/2)
        
        