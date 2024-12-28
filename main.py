import pygame
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
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Board.containers = (drawable, updatable)
Chip.containers = (drawable, updatable)

board = Board()
chip = Chip("yellow")




# Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(GAME_FPS) / 1000
    
    updatable.update(dt)
    
    screen.fill("black")
    
    for i in range(12):
            pygame.draw.line(screen, "green", (100 * (i + 1), 0), (100 * (i + 1), 720))
    drawable.draw(screen)
    
    pygame.display.flip()
    


pygame.quit()