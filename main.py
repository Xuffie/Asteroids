import pygame
from constants import *
from player import *

def main():
    pygame.init()

    game_time = pygame.time.Clock()
    

    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while 1 > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)

        screen.fill("black")

        for focus in drawable:
            focus.draw(screen)

        pygame.display.flip()

        
        dt = game_time.tick(60) / 1000



if __name__ == "__main__":
    main()

