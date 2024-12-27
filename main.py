import pygame
from constants import * #NOQA
from board import Board

class Game():
    def __init__(self, height, width, fps):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.fps = fps
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    def update(self, updatable):
        dt = self.clock.tick(self.fps) / 1000
        updatable.update(dt)

    def draw(self, drawable):
        self.screen.fill("black")
        pygame.draw.circle(self.screen, "red", (500, 500), 40)
        pygame.draw.circle(self.screen, "yellow", (800, 500), 40)
        for i in range(12):
            pygame.draw.line(self.screen, "green", (100 * (i + 1), 0), (100 * (i + 1), 720))
        drawable.draw(self.screen)
        pygame.display.flip()
        

                

def main():
    game = Game(SCREEN_HEIGHT, SCREEN_WIDTH, GAME_FPS)
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    
    Board.containers = (updatable, drawable)

    board = Board()
    # board.draw(game.screen)
    
    
    while game.running:
        game.events()
        game.update(updatable)
        game.draw(drawable)
    
    
    pygame.quit()
    quit()
    
    
if __name__ == "__main__":
    main()