import pygame
import random
from constants import *
from board import Board
from chip import Chip

# initialising content
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Connect 4")
running = True
dt = 0

clock = pygame.time.Clock()

# Groups declaraction
chips = pygame.sprite.Group()

board = Board()
chip_d = Chip("yellow")




# Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            chip = Chip(random.choice(["red", "yellow"]), pos[0], pos[1])
            chips.add(chip)
            
    dt = clock.tick(GAME_FPS) / 1000
    
    chips.update(dt)
    screen.fill("black")
    
    for i in range(12):
            pygame.draw.line(screen, "green", (100 * (i + 1), 0), (100 * (i + 1), 720))
    chips.draw(screen)
    
    
    pygame.display.flip()
    


pygame.quit()