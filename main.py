import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()

    game_time = pygame.time.Clock()
    

    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids_group = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids_group, updateable, drawable)
    AsteroidField.containers = (updateable)

    new_asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while 1 > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)

        for asteroid_obj in asteroids_group:
            if player.collision_checker(asteroid_obj) == True:
                print("Game over!")
                raise sys.exit("You suck")

        screen.fill("black")

        for focus in drawable:
            focus.draw(screen)

        pygame.display.flip()

        
        dt = game_time.tick(60) / 1000



if __name__ == "__main__":
    main()

