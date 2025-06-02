import pygame
from constants import *
from player import *

def main():
    pygame.init()

    game_time = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while 1 > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
           
        pygame.Surface.fill(screen,(0,0,0))
        player.draw(screen) 
        player.update(dt)
        pygame.display.flip()

        
        dt = game_time.tick(60) / 1000



if __name__ == "__main__":
    main()

