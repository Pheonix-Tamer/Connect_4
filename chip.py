from email.mime import image
from re import S
import pygame
from constants import *

class Chip(pygame.sprite.Sprite):
    # def __init__(self, *groups):
    #     super().__init__(*groups)
    def __init__(self, colour, x = 100, y=100):
        pygame.sprite.Sprite.__init__(self)
            
        # self.image, self.rect = self.create_image(colour)
        # self.rect.center = (x, y)
        self.image = pygame.Surface((CHIP_RADIUS*2, CHIP_RADIUS*2), pygame.SRCALPHA)
        # self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, colour, self.rect.center, CHIP_RADIUS)
        self.rect.center = (x, y)
    
    # def create_image(self, colour):
    #     image = pygame.Surface([CHIP_RADIUS*2, CHIP_RADIUS*2])
    #     rect = image.get_rect()
    #     pygame.draw.circle(image, colour, (CHIP_RADIUS, CHIP_RADIUS), CHIP_RADIUS)
    #     return image, rect
        